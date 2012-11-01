"""
Cubulus OLAP - free aggregation and reporting
Copyright (C)2007 Alexandru Toth

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation version 2.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

#
# pyparsing Copyright (c) 2003, Paul McGuire
#
from pyparsing import *

def test():
    for t in ("[a]", "[2006]", "[a].[2006]", "[1].[2].[3]"):
        print t, '->', level.parseString(t)

    for t in ("{[a]} on rows","{[a].[b]} on rows"):
        print t, '->', rowAxis.parseString(t)
        
    for t in ("{[a]} on columns","{[a].[b]} on columns"):
        print t, '->', colAxis.parseString(t)
        
    for t in ("from xx","FROM yy"):
        print t, '->', fromCube.parseString(t)
        
    for t in ("where ([a])", "where ([a].[b])", "where ([a].[b], [1].[2])"):
        print t, '->', whereClause.parseString(t)

    for t in ("{[a]} on columns, {[a]} on rows", \
            "{[a].[2].[4]} on rows, {[a]} on columns"):
        print t, '->', rowCol.parseString(t)

    for t in (\
        "select {[c]} on columns, {[r]} on rows from CUBE where ([w],[w2].[e])",
        "select {[r]} on rows, {[c]} on columns from CUBE where ([w],[w2].[e])"):
        print t, '->', mdx.parseString(t)
        
def mdxParser(t):
    #print t, '->'
    tokens = mdx.parseString(t)
    #print "onrows", tokens.onrows
    #print "oncols", tokens.oncols
    #print "cube", tokens.cube
    #print "slicers", tokens.slicers
    return tokens

id = Word(alphas)
scalar = Word(alphanums+"_"+" ")
selectToken = Keyword("select", caseless=True).suppress()
fromToken   = Keyword("from", caseless=True).suppress()
whereToken   = Keyword("where", caseless=True).suppress()
onToken   = Keyword("on", caseless=True).suppress()
rowToken  = Keyword("rows", caseless=True).suppress()
colToken   = Keyword("columns", caseless=True).suppress()
childrenToken = Keyword("children", caseless=True) #DON*T SUPRRESS
crossJoinToken = Keyword("crossjoin", caseless=True).suppress()

dot = Literal(".").suppress()
comma = Literal(",").suppress()
semicolon = Literal(";").suppress()
leftBr = Literal("(").suppress()
rightBr = Literal(")").suppress()
leftSqBr = Literal("[").suppress()
rightSqBr = Literal("]").suppress()
leftCurlBr = Literal("{").suppress()
rightCurlBr = Literal("}").suppress()

level = Group(\
    delimitedList(leftSqBr + scalar + rightSqBr, ".", combine=False)\
    ).setResultsName("level")
#levelWithChildren = Group(level + Optional(dot + childrenToken))

levelWithChildren = Group(
    delimitedList(leftSqBr + scalar + rightSqBr, ".", combine=False) +
    Optional(dot + childrenToken)).setResultsName("level")
    
onRows = onToken + rowToken
onCols = onToken + colToken

rcSet = leftCurlBr + delimitedList(levelWithChildren, ",") + rightCurlBr
rowList = (rcSet + onRows).setResultsName("onrows")
colList = (rcSet + onCols).setResultsName("oncols")
rowNest = crossJoinToken + leftBr + levelWithChildren.setResultsName("onrows")+\
    comma + levelWithChildren.setResultsName("rownest") + rightBr + onRows
colNest = crossJoinToken + leftBr + levelWithChildren.setResultsName("oncols")+\
    comma + levelWithChildren.setResultsName("colnest") + rightBr + onCols
rowAxis = rowList | rowNest
colAxis = colList | colNest
fromCube = (fromToken + id).setResultsName("cube")
whereClause = (whereToken + leftBr + level + Optional(comma + level) + \
    rightBr).setResultsName("slicers")
rowCol = rowAxis + comma + colAxis | colAxis + comma + rowAxis
mdx = selectToken + rowCol + fromCube + Optional(whereClause) + Optional(semicolon)

if __name__ == "__main__":
    print mdxParser("Select {[region].[all region].children} on rows, {[prod].[all prod].children} on columns from cubulus where ([time].[all time].[time_2005])")
    print mdxParser("Select {[time].[all time].children} on rows, crossjoin([region].[all region].children, [region].[all region].children) on columns from cubulus")
#print mdxParser(\
#    "select {[time].[2006]} on columns, {[measures]} on rows from CUBE where ([Scenario].[Plan],[Customer].[Small])")

#print mdxParser(\
#    "select {[time].[2005].children, [time].[2006].children} on rows, {[measures].children} on columns from CUBE where ([Scenario].[Plan],[Customer].[Small])")
    
#print mdxParser("Select {[time].[all time].children} on rows, {[region].[all region].children} on columns from cubulus")

    

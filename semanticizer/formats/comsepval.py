from . import BaseFormatter, do_transformation
from django.contrib.gis.geos import Point
import csv
import StringIO
import json

class Formatter(BaseFormatter):
    def extract_columns(self, url, **kwargs):
        file = self.get_file(url)
        splitter = kwargs['splitter'] if "splitter" in kwargs else ","
        f = StringIO.StringIO(file)
        reader = csv.reader(f, delimiter=splitter)        
        return reader.next()
    
    def to_dict(self, url, transformation, **kwargs):
        file = self.get_file(url)
        splitter = kwargs['splitter'] if "splitter" in kwargs else ","
        print transformation
        geo = True
        selected_cols = transformation.keys()
        cols = self.extract_columns(url, **kwargs)
        print cols
        col_nums = {}
        single_geo_col = False
        for i in range(0,len(cols)):
            for sc in selected_cols:
                if cols[i] == sc:
                    if transformation[sc][0]['target'] =="GEOMETRY":
                        print transformation[sc]
                        if "col_x" in transformation[sc][0] and transformation[sc][0]['col_x'] and 'col_y' in transformation[sc][0] and transformation[sc][0]['col_y']:
                            col_x = i
                            col_y = i
                            single_geo_col = True
                        elif "col_x" in transformation[sc][0] and transformation[sc][0]['col_x']:
                            col_x = i
                        elif 'col_y' in transformation[sc][0] and transformation[sc][0]['col_y']:
                            col_y = i
                        else:
                            col_nums[i] = sc   
                    else:
                        col_nums[i] = sc                    
        #now we have the data from the cols. Now let's extract!
        js = []
        f = StringIO.StringIO(file)
        reader = csv.reader(f, delimiter=splitter)
        reader.next()
        for row in reader:
            rr = {}
            if geo:
                if single_geo_col:
                    geom = OGRGeometry('POINT'+row[col_x].replace(','," "))
                else:
                    r_x = row[col_x]
                    r_y = row[col_y]
                    geom = Point(float(r_y),float(r_x)) 
                rr ['geo_location'] = json.loads(geom.json)
            for i in range(0, len(row)):
                if i in col_nums.keys():
                    for trans in transformation[col_nums[i]]:
                        rr[trans['target']] = do_transformation(row[i], trans['op'])
            js.append(rr)
            
        return js
                
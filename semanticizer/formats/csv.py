from . import BaseFormatter, do_transformation
from django.contrib.gis.geos import Point
import csv

class Formatter(BaseFormatter):
    def extract_columns(self, url, **kwargs):
        file = self.get_file(url)
        splitter = kwargs['splitter'] if "splitter" in kwargs else ","
        f = StringIO.StringIO(file)
        reader = csv.reader(f, delimiter=splitter)        
        return reader[0]
    
    def to_dict(self, url, transformation, **kwargs):
        file = self.get_file(url)
        splitter = kwargs['splitter'] if "splitter" in kwargs else ","
        geo = kwargs['geo'] if "geo" in kwargs else False
        selected_cols = transformation.keys()
        cols = self.extract_columns(file, **kwargs)
        col_nums = {}
        for i in range(1,len(cols)):
            for sc in selected_cols:
                if cols[i] == sc:
                    if geo:
                        if "col_x" in transformation[sc]:
                            col_x = i
                        elif 'col_y' in transformation[sc]:
                            col_y = i
                        else:
                            col_nums[i] = sc   
                    else:
                        col_nums[i] = sc                    
        #now we have the data from the cols. Now let's extract!
        js = []
        for row in csv.reader(f, delimiter=splitter):
            for i in range(1, len(row)):
                rr = {}
                if i in col_nums.keys():
                    for trans in transformation[col_nums[i]]:
                        rr[trans['target']] = do_transformation(row[i], trans['op'])
                js.append(rr)
            if geo:
                r_x = row[col_x]
                r_y = row[col_y]
                geom = Point(r_x, r_y) 
                js ['geo_location'] = geom
        return js
                
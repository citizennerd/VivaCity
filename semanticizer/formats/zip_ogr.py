from . import BaseFormatter, do_transformation
from django.contrib.gis import gdal

import tempfile
import zipfile

class Formatter(BaseFormatter):
    def extract_columns(self, file, **kwargs):
        data = self.get_file(file)        
        
        tz = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)
        tz.write(data)
        tz.close()
        td = tempfile.mkdtemp()
        zf = zipfile.ZipFile(tz.name)
        f = zf.namelist()
        zf.extractall(td)        
        
        data = gdal.DataSource(os.path.join(td,'.'.join(zf.namelist()[0].split('.')[:-1])))
        layer = data[0]
        return layer.fields
    
    def to_dict(self, file, transformation, **kwargs):
        tz = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)
        tz.write(data)
        tz.close()
        td = tempfile.mkdtemp()
        zf = zipfile.ZipFile(tz.name)
        f = zf.namelist()
        zf.extractall(td)        
        
        data = gdal.DataSource(os.path.join(td,'.'.join(zf.namelist()[0].split('.')[:-1])))
        layer = data[0]
        
        selected_cols = transformation.keys()
        cols = layer.fields
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
                
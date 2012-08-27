from . import BaseFormatter, do_transformation
from django.contrib.gis import gdal

import json
import tempfile
import zipfile
import os

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
        files = zf.namelist()
        files = [{f.lower():f} for f in files]
        file = [o for f,o in files.items() if f.endswith("shp")][0]
        
        data = gdal.DataSource(os.path.join(td,file))
        layer = data[0]
        return layer.fields
    
    def to_dict(self, file, transformation, **kwargs):
        tz = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)
        data = self.get_file(file)    
        tz.write(data)
        tz.close()
        td = tempfile.mkdtemp()
        zf = zipfile.ZipFile(tz.name)
        f = zf.namelist()
        zf.extractall(td)        
        files = zf.namelist()
        files = [{f.lower():f} for f in files]
        file = [o for f,o in files.items() if f.endswith("shp")][0]
        
        data = gdal.DataSource(os.path.join(td,file))
        layer = data[0]
        
        selected_cols = transformation.keys()
        cols = layer.fields
        #now we have the data from the cols. Now let's extract!
        js = []
        for feat in layer:
            rr = {}
            for col in selected_cols:
                for trans in transformation[col]:
                    rr[trans['target']] = {"value":do_transformation(feat.get(col), trans['op']),'via':trans['via']}
            
            try: 
                rr ['geo_location'] = json.loads(feat.geom.transform("EPSG:4326",clone=True).json)
            except Exception, E: 
                raise Exception('%s: projection was: %s' % (E, feat.geom.srs)) 
            js.append(rr)
        return js
                
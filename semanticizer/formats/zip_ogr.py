from . import BaseFormatter, do_transformation, lowercase_rename
from django.contrib.gis import gdal
from django.contrib.gis.gdal import SpatialReference

import json
import tempfile
import zipfile
import os

class Formatter(BaseFormatter):
        
    def extract_columns(self, file):
        data = self.get_file(file)        
        
        tz = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)
        tz.write(data)
        tz.close()
        td = tempfile.mkdtemp()
        zf = zipfile.ZipFile(tz.name)
        f = zf.namelist()
        zf.extractall(td)      
        files = zf.namelist()
        files = [f.lower() for f in files]
        file = [f for f in files if f.endswith("shp")][0]
        lowercase_rename(td)
        fname = os.path.join(td,file)
        data = gdal.DataSource(td)
        layer = data[0]
        return layer.fields
    
    def to_dict(self, file, transformation):
        tz = tempfile.NamedTemporaryFile(suffix=".zip", delete=False)
        data = self.get_file(file)    
        tz.write(data)
        tz.close()
        td = tempfile.mkdtemp()
        zf = zipfile.ZipFile(tz.name)
        f = zf.namelist()
        zf.extractall(td)        
        files = zf.namelist()
        files = [f.lower() for f in files]
        file = [f for f in files if f.endswith("shp")][0]
        lowercase_rename(td)
        fname = os.path.join(td,file)
        data = gdal.DataSource(td)
        layer = data[0]
        
        selected_cols = transformation.keys()
        cols = layer.fields
        #now we have the data from the cols. Now let's extract!
        js = []
        srs = ""
        srid = ""
        for feat in layer:
            rr = {}
            for col in selected_cols:
                for trans in transformation[col]:
                    rr[trans['target']] = {"value":do_transformation(feat.get(col), trans['op']),'via':trans['via']}
            
            try:
                srs = feat.geom.srs
                srid = feat.geom.srid 
                jjj = feat.geom.json
                if ("ED_1950_UTM_Zone_32N" in str(feat.geom.srs)):
                    feat.geom.srs = SpatialReference(23032)
                rr ['geo_location'] = json.loads(feat.geom.transform("EPSG:4326",clone=True).json)
                js.append(rr)
            except Exception, E: 
                pass 
        return js, [str(srs),str(srid)]
                
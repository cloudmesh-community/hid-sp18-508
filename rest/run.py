# -*- coding: utf-8 -*-
from eve import Eve
import platform
import psutil
import shutil
import json
from flask import Response
settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'DOMAIN': {}
}

app = Eve(settings = settings)

@app.route('/diskspace')
def diskspace():
    

    disk = shutil.disk_usage("/home/yueguo")
    
    data = {
        'total' : disk[0],
        'used' : disk[1],
        'free' : disk[2],
    }
    
    response = Response()
    response.headers["status"] = 200
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.data = json.dumps(data)
    
    return response

if __name__ == '__main__':
    app.run()
    

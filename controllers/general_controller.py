from flask import jsonify, request
import psutil
import datetime

def health():
    uptime = datetime.datetime.now() - datetime.datetime.fromtimestamp(
        psutil.boot_time()
    )
    
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent

    data = {
        'status': 'healthy',
        'uptime': str(uptime),
        'cpu': cpu_percent,
        'mem': mem_percent
    }
    
    return jsonify(data), 200


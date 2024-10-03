from fastapi import FastAPI
import os
import platform
import psutil

app = FastAPI()

def get_system_info():
    system_info = {
        "os_name": platform.system(),
        "os_version": platform.version(),
        "hostname": platform.node(),
        "cpu": {
            "architecture": platform.machine(),
            "cores": os.cpu_count(),
            "usage_percent": psutil.cpu_percent(interval=1),
        },
        "memory": {
            "total": psutil.virtual_memory().total // (1024 ** 2),  # in MB
            "available": psutil.virtual_memory().available // (1024 ** 2),  # in MB
            "used_percent": psutil.virtual_memory().percent,
        },
        "disk": {
            "total": psutil.disk_usage('/').total // (1024 ** 3),  # in GB
            "used": psutil.disk_usage('/').used // (1024 ** 3),  # in GB
            "free": psutil.disk_usage('/').free // (1024 ** 3),  # in GB
            "used_percent": psutil.disk_usage('/').percent,
        }
    }
    return system_info

@app.get("/system-info")
def read_system_info():
    return get_system_info()


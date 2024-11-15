from flask import Flask, jsonify
import psutil
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Resource monitoring application started")


app = Flask(__name__)

@app.route('/health')
def health():
    # CPU metrics
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)
    cpu_count = psutil.cpu_count(logical=True)

    # Memory metrics
    memory = psutil.virtual_memory()
    memory_total = memory.total
    memory_available = memory.available
    memory_used = memory.used
    memory_percent = memory.percent

    # Disk metrics
    disk = psutil.disk_usage('/')
    disk_total = disk.total
    disk_used = disk.used
    disk_free = disk.free
    disk_percent = disk.percent

    # Disk I/O metrics
    disk_io = psutil.disk_io_counters()
    disk_read = disk_io.read_bytes
    disk_write = disk_io.write_bytes

    # Network metrics
    net_io = psutil.net_io_counters()
    net_sent = net_io.bytes_sent
    net_recv = net_io.bytes_recv

    return jsonify({
        "cpu": {
            "cpu_percent": cpu_percent,
            "cpu_per_core": cpu_per_core,
            "cpu_count": cpu_count
        },
        "memory": {
            "memory_total": memory_total,
            "memory_available": memory_available,
            "memory_used": memory_used,
            "memory_percent": memory_percent
        },
        "disk": {
            "disk_total": disk_total,
            "disk_used": disk_used,
            "disk_free": disk_free,
            "disk_percent": disk_percent
        },
        "disk_io": {
            "disk_read": disk_read,
            "disk_write": disk_write
        },
        "network": {
            "net_sent": net_sent,
            "net_recv": net_recv
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

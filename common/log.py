from datetime import datetime

def log(msg, level="INFO"):
    
    ts = datetime.now().strftime("%H:%M:%S")
    prefix = {"INFO": "  ", "WARNING": "⚠️ ", "ERROR": "❌ ", "OK": "✅ "}
    print(f"[{ts}] {prefix.get(level, '  ')} {msg}", flush=True)

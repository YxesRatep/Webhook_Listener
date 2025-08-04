from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return 'Alive', 200

@app.route('/prtg', methods=['POST'])
def prtg_webhook():
    data = request.form.to_dict()
    print(f"[{datetime.now(datetime.timezone.utc)}] Received webhook from PRTG:")
    for key, value in data.items():
        print(f"  {key}: {value}")
    
    # Optional: Forward this to another API or write to file/DB

    return '', 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
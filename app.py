from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import time

# Inicializa o app Flask
app = Flask(__name__)

# Inicializa o Prometheus Exporter
metrics = PrometheusMetrics(app)

# Rota principal
@app.route("/")
def home():
    return jsonify({
        "message": "API funcionando!",
        "timestamp": time.time()
    })

# Rota de verificação de saúde
@app.route("/health")
def health():
    return jsonify({"status": "ok"})

# Rota de métricas (exposta automaticamente pelo PrometheusMetrics)
# Não precisa declarar manualmente /metrics

# Inicializa o servidor Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
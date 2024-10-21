import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Usar el puerto asignado por Render
    app.run(host='0.0.0.0', port=port)

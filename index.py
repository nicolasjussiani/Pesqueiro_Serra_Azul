from flask import Flask
import app

# Precisamos criar uma variável chamada 'app' que o Vercel irá procurar
# Estamos apenas redirecionando para a instância do Flask em app.py
app = app.app

# Este handler é necessário para funcionar no ambiente serverless
@app.route('/_vercel/path0', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/_vercel/path1/<path:path1>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/_vercel/path2/<path:path1>/<path:path2>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
@app.route('/_vercel/path3/<path:path1>/<path:path2>/<path:path3>', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def vercel_handler(path1="", path2="", path3=""):
    """Handle Vercel serverless requests."""
    return app.dispatch_request()

# Para desenvolvimento local
if __name__ == '__main__':
    app.run(debug=True)
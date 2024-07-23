@app.after_request
def add_security_headers(response):
    response.headers['Content-Security-Policy'] = "script-src 'self';"
    return response

@app.route('/content', methods=['POST', 'GET'])
@cors
def content():
    user_input = "<script>alert('This script should not run');</script>"
    HTML = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
        {user_input}
    </body>
    </html>
    """
    return HTML
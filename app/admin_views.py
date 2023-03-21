from app import app

@app.route('/admin')
def admin():
    return "Hello Admin"

@app.route('/admin/page')
def admin_page():
    return "<h1> This is about Admin PAGE </h1>"
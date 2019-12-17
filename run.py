from app import create_app

app = create_app()

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(host="0.0.0.0", debug=True, port="7001")
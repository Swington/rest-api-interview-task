from factory import initialize_app

app = initialize_app()

if __name__ == '__main__':
    app.run(port=5000, debug=True)

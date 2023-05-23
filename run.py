from src import create_app

app, socketio = create_app()
socketio.run(app, host=app.config['HOST'], port=app.config['PORT'])

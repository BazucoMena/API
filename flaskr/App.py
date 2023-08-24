from flaskr import create_app

app = create_app('default')
app_context = app.app_cotext()
app_context.push()
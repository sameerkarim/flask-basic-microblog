from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	# fake data
	user = { 'nickname': 'Miguel'}
	posts = [
		{
			'author': { 'nickname': 'John'},
			'body': 'Beautiful day in Portland!'
		}, 
		{
			'author': { 'nickname': 'Susan'},
			'body': 'That movie rocked!'
		}, 
		{
			'author' : { 'nickname': 'Sameer'},
			'body': 'Getting a bit tired.'
		}
	]


	return render_template("index.html", 
		title = 'Home',
		user = user, 
		posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + 
                form.openid.data + '", remember_me = "' + 
                str(form.remember_me.data))
        return redirect('/index')

    # render the login template again if there are errors
    # later we'll add some error messages here.
    return render_template('login.html', 
		title = 'Sign in', 
		form = form, 
        providers = app.config['OPENID_PROVIDERS'])



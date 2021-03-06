from app import app
from flask import render_template, flash, redirect, url_for, session
from app.forms import LoginForm, SignupForm, HHSULForm
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from database import *
import pickle
#from sklearn import linear_model

engine = create_engine('sqlite:///test.db', echo=True)




@app.route('/index')

def index():
    user = {'username': 'Amir'}
    messages = [
        {
            'author': {'username': 'Oscar'},
            'body': 'Take prots bro!'
        },
        {
            'author': {'username': 'Zoulette'},
            'body': 'Nice gains today bro.'
        }
    ]
    perfs_deadlift = [180, 145]
    
    return render_template('index.html', title='Test', user=user, messages=messages, perfs_deadlift=perfs_deadlift)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = SignupForm()
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data
        password_hash = generate_password_hash(password)
        Session = sessionmaker(bind=engine)
        s = Session()
        query = s.query(User).filter(User.username.in_([username]))
        result = query.first()
        if not result:
            user = User(username = username,password = password_hash)
            s.add(user)
            s.commit()
        else:
            flash('u already signed up bruh')
        return redirect('/index')

    return render_template('sign_up.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data
        Session = sessionmaker(bind=engine)
        s = Session()
        for instance in s.query(User).filter(User.username.in_([username])): # assert no double in database
            password_hash = instance.password
            bool_pass = check_password_hash(password_hash, password)
            if bool_pass:
                #flash('Welcome {} bruh'.format(form.username.data))
                # Create session data, we can access this data in other routes
                #people_logged_in[username] = True
                session['loggedin'] = True
                session['username'] = username
                return redirect('/login/home')
            else:
                flash('dunno u bruh')
                return redirect('/login')

    return render_template('login.html', title='Log in', form=form)

@app.route('/login/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/login/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        flash('hey {}'.format(session['username']))
        return render_template('profile.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/login/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('username', None)
   session.pop('_flashes', None)

   # Redirect to login page
   return redirect(url_for('index'))
   
@app.route('/')
@app.route('/who_am_i', methods=['GET', 'POST'])
def who_am_i():
    return render_template('who_am_i.html')

pkl_filename = "Are_you_strong.pkl"
# Load from file
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

@app.route('/HHSUL', methods=['GET', 'POST'])
def How_Heavy_Should_U_Lift():
    prediction = 'your prediction will appear here bruh'
    form = HHSULForm()
    if form.validate_on_submit():

        age = form.age.data
        time_training = form.time_training.data
        wheight = form.wheight.data
        height = form.height.data
        body_fat = form.body_fat.data
        natty = form.natty.data
        bulking_shredding = form.bulking_shredding.data
        prediction = pickle_model.predict([[age,time_training,wheight,height,body_fat,natty,bulking_shredding]])
    return render_template('HHSUL.html', form=form,prediction = prediction)


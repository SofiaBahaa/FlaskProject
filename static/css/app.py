from flask import Flask, render_template, redirect, url_for, request, session

app = Flask(name)
app.secret_key = 'your_secret_key_here'  # مفتاح لحماية السيشن

# بيانات تجريبية (مؤقتة)
users = {
    "admin@example.com": {"password": "adminpass", "role": "admin", "name": "Admin User"},
    "student@example.com": {"password": "studentpass", "role": "student", "name": "Student User"},
}

# المسارات Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = users.get(email)
        if user and user['password'] == password:
            session['user'] = {'email': email, 'name': user['name'], 'role': user['role']}
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # مفيش حفظ حقيقي هنا، مثال بس
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=session['user'])

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        session['user']['name'] = request.form['name']
        session['user']['email'] = request.form['email']
    return render_template('profile.html', user=session['user'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if name == "main":
    app.run(debug=True)
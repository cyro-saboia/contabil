from ..database import db
from validate_docbr import CPF
from ..models.userModel import User
from ..forms.loginForm import LoginForm
from ..forms.registerForm import RegisterForm
from ..rotas.loginRout import login_bp
from flask_login import login_user, logout_user
from flask import render_template, request, redirect, url_for, flash, session

class loginController:

    @login_bp.route('/register', methods=['GET', 'POST'])
    def register():

        form = RegisterForm(request.form)

        if request.method == 'POST': 

            name = form.name.data
            email = form.email.data
            txtcpf = form.cpf.data
            pwd = form.password.data

            cpf = CPF()
            if not cpf.validate(txtcpf): 
               flash('Ops. Não nos parece um CPF válido', 'error')
               return render_template('register.html', form=form)

            try:
                
                user = User(name,email, txtcpf, pwd)

                db.session.add(user)
                db.session.commit()
                flash('Usuário cadastrado com sucesso!', 'sucess') 
                return redirect(url_for('login.login')) 

            except Exception as e:
                db.session.rollback()
                flash('Erro: {}'.format(e), 'error')  
                return render_template('register.html', form=form)   
        else:
            return render_template('register.html', form=form) 

    @login_bp.route('/login', methods=['GET', 'POST'] )
    def login(): 

        form = LoginForm(request.form)

        if request.method == 'POST' and form.validate(): 

            try:
                email = form.email.data
                pwd = form.password.data

                user = User.query.filter_by(email=email).first()

                if not user or not user.verify_password(pwd):
                    flash('Usuário ou senha inválidos')
                    return redirect(url_for('login.login'))        

                # if user.flgAdmin:
                #     session["roles"] = ['URBANMOB_ADMIN','URBANMOB_GOVERNO']
                # elif user.flgGoverno :
                #     session["roles"] = ['URBANMOB_GOVERNO']
                # else:
                #     session["roles"] = ['URBANMOB_USER']

                login_user(user)

                return render_template('home.html')  
            except Exception as e:
                flash('Erro: {}'.format(e), 'error')                   
                return render_template('login.html', form=form)  
        else:
            return render_template('login.html', form=form)
            
    @login_bp.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('login.login'))

    @login_bp.route('/site')
    def site():
        logout_user()
        return redirect('/')
# from xml.dom import ValidationErr
from validate_docbr import CPF
from wtforms import BooleanField, Form, PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import (DataRequired, Email, EqualTo, InputRequired,
                                Length)

class ValidCpf(object):
    def __init__(self, message=None):
        if message is None:
            message = 'Ops. Não nos parece um CPF válido.'
        self.message = message

    def __call__(self, form, field):
        cpf = CPF()
        if not cpf.validate(field.data):
            raise ValidationError(self.message)
        
class RegisterForm(Form):

    # def validaCpf(self, field):
    #     cpf = CPF()
    #     if not cpf.validate(field.data): 
    #         raise ValidationErr('Ops. Não nos parece um CPF válido.')

    name = StringField(
    'Informe seu Nome',
    [
        InputRequired(message=('Por favor, informe seu Nome.'))
    ])

    email = StringField(
    'Digite seu email',
    validators = [
        Email(message=('Ops. Não nos parece um e-mail válido.'))
    ])

    cpf = StringField(
    'Digite seu CPF',
    render_kw={'placeholder': 'Digite apenas números'},
    validators = [
        DataRequired(message='*Campo Requerido'),
        Length(max=11, min=11, message='O CPF deve ter conter exatamente 11 caracteres'),
        ValidCpf()
    ])

    password = PasswordField('Password', 
    validators = [
        DataRequired(),
        EqualTo('confirm_password', message='As senhas não são iguais'),
        Length(min=8, message='A senha deve ter no mínimo %(min)d caracteres')
    ])

    confirm_password = PasswordField('Confirm Password',
    validators = [
        DataRequired(message='*Campo Requerido'),
        EqualTo('password', message='As senhas devem ser iguais')
    ])

    submit = SubmitField('Cadastrar')
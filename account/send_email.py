from django.core.mail import send_mail


def send_activation_code(email, code):
    send_mail(
        'Film platform', # title
        f'http://localhost:8000/api/v1/account/activate/{code}', # body
        'lucifercommander@gmail.com', # from
        [email] # to
    )

def send_password_code(email, secret_word, code):
    send_mail(
        'Film platform', # title
        f'Привет, чтобы сбросить пароль, тебе нужно знать этот токен: {code}', # body
        'lucifercommander@gmail.com', # from
        [email] # to
    )


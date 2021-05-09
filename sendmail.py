def sendemail(subject, body):
    import smtplib
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login("blingharmony2008@gmail.com", "Initialquesco3")

        subject = subject
        body = body
        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail("blingharmony2008@gmail.com", "phong.nguyen@wellcare.vn", msg)
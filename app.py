from flask import Flask, request, render_template
import qrcode
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

SMTP_USERNAME = 'yaredshi3@gmail.com'
SMTP_PASSWORD = 'yusp nbxq hsbv rnjk'  # Use the app-specific password here

def send_email(name, email, comment):
    sender_email = SMTP_USERNAME
    receiver_email = 'yaredshi3@gmail.com'  # Update with your own email address
    subject = 'Feedback from Website'
    body = f'Name: {name}\nEmail: {email}\nComment: {comment}'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    text = message.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

    return 'Email sent successfully'

@app.route('/')
def index():
    return render_template('feedback.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get('name')
    email = request.form.get('email')
    comment = request.form.get('comment')

    send_email(name, email, comment)

    return 'Feedback received successfully'

@app.route('/generate-qr')
def generate_qr():
    data = "https://127.0.0.1:5000/feedback"
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("static/qr_code.png")  # Save the QR code image in the static folder

    return 'QR code generated successfully'

if __name__ == '__main__':
    app.run(debug=True)

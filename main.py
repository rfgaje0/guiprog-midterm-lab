from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def contact_form():
    return render_template('contact.html')


@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('message')
    subject = request.form.get('subject')
    other_subject = request.form.get('other_subject')
    contact_methods = request.form.getlist('contact_method')
    agreement = request.form.get('agreement')

    errors = []

    if not name or not email or not phone or not message:
        errors.append("Please fill in all required fields.")
    if not phone.isdigit():
        errors.append("Phone number must be numeric.")
    if not agreement:
        errors.append("You must agree to the terms and conditions.")

    if subject == 'Other':
        if not other_subject:
            errors.append("Please specify a subject.")
        else:
            subject = other_subject

    if errors:
        return render_template('contact.html', errors=errors,
                               name=name, email=email, phone=phone,
                               message=message, subject=subject,
                               contact_methods=contact_methods,
                               agreement=agreement)

    return render_template('confirmation.html', name=name, email=email, phone=phone,
                           message=message, subject=subject,
                           contact_methods=", ".join(contact_methods),
                           agreement="Yes" if agreement else "No")


if __name__ == '__main__':
    app.run()
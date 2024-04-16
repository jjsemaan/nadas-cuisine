/* ---- emailjs config ---- */
function sendEmail() {
    emailjs.sendForm("service_lsnrkzb", "template_parabim", "#contact-form")
        .then(function (response) {
            console.log('Email sent successfully:', response);
            // Show alert with success message
            alert('Email sent successfully!');

            // Delay the form reset by a short interval
            setTimeout(function () {
                document.getElementById('contact-form').reset();
            }, 100);
        })
        .catch(function (error) {
            console.error('Error sending email:', error);
            // Handle error if needed
        });
}


function validateForm() {
    var name = document.getElementById('name_id');
    var email = document.getElementById('email_id');
    var mobile = document.getElementById('mobile_id');
    var message = document.getElementById('message_id');

    if (name.value.trim() === '') {
        alert('Name is required.');
        name.classList.add('error');
        return false;
    } else if (name.value.length > 25) {
        alert('Name should not exceed 25 characters.');
        name.classList.add('error');
        return false;
    } else {
        name.classList.remove('error');
    }

    if (email.value.trim() === '' || !validateEmail(email.value)) {
        alert('Invalid email address.');
        email.classList.add('error');
        return false;
    } else if (email.value.length > 50) {
        alert('Email should not exceed 50 characters.');
        email.classList.add('error');
        return false;
    } else {
        email.classList.remove('error');
    }

    if (mobile.value.trim() === '' || !validateMobile(mobile.value)) {
        mobile.classList.add('error');
        return false;
    } else {
        mobile.classList.remove('error');
    }

    if (message.value.trim() === '') {
        alert('Message is required.');
        message.classList.add('error');
        return false;
    } else if (message.value.length > 1000) {
        alert('Message should not exceed 1000 characters.');
        message.classList.add('error');
        return false;
    } else {
        message.classList.remove('error');
    }

    return true;
}

function validateEmail(email) {
    // You can use a more sophisticated email validation regex if needed
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function validateMobile(mobile) {
    var mobileRegex = /^[0-9]+$/;
    var isValidLength = mobile.length <= 10;

    if (!isValidLength) {
        alert('Mobile number should not exceed 10 digits.');
        return false;
    }

    if (!mobileRegex.test(mobile)) {
        alert('Mobile number should only contain numeric digits.');
        return false;
    }

    return true;
}

document.getElementById("contact-form-button").addEventListener("click", function (event) {
    event.preventDefault(); // Prevent the default form submission behavior

    if (validateForm()) {
        sendEmail();
    }
});
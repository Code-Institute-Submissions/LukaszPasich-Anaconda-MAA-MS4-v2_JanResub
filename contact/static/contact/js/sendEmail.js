function sendMail(contactForm) {
    emailjs.send("service_0qbc6d9", "anacondamaa", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "phone": contactForm.phone.value,
        "contact_form_query": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            var messageEmail = document.getElementById("email-message-container");
            var messageEmailBody = document.getElementById("email-message-body");
            messageEmail.style.display = 'inline-block';
            messageEmailBody.innerHTML = "Message sent successfully";
        },
        function(error) {
            console.log("FAILED", error);
            var messageEmail = document.getElementById("email-message-container");
            var messageEmailBody = document.getElementById("email-message-body");
            messageEmail.style.display = 'inline-block';
            messageEmailBody.innerHTML = "Message not sent";
        }
    );
    setTimeout(function(){window.location.reload();},4500);
    return false;
}
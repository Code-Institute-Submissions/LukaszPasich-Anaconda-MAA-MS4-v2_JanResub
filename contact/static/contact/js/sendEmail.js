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
            // var flashEmail = document.getElementById("flash-messages-email");
            // flashEmail.style.display = 'inline-block';
            // flashEmail.innerHTML = "Message sent successfully";
        },
        function(error) {
            console.log("FAILED", error);
            // var flashEmail = document.getElementById("flash-messages-email");
            // flashEmail.style.display = 'inline-block';
            // flashEmail.innerHTML = "Message not sent!";
        }
    );
    setTimeout(function(){window.location.reload();},4000);
    return false;
}
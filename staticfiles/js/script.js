document.addEventListener('DOMContentLoaded', function () {

    console.log("Life, The Universe and Everything!");

    document.querySelectorAll('.back-btn').forEach(button => {
        button.addEventListener('click', function () {
            console.log("Back button clicked");
            window.history.back();
        });
    });

});




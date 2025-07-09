document.addEventListener("DOMContentLoaded", function () {

    console.log("Life, The Universe and Everything!");


    document.querySelectorAll('back-btn').forEach(button => {
        button.addEventListener('click', function () {
            window.history.back();
        });
    });


});
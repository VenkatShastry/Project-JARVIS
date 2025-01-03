$(document).ready(function () {
    // eel.init()()

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        }

    });



    // SiriWave Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: 1, // Numeric value, not a string
        speed: 0.3   // Numeric value, not a string
    });


    //Siri Message Animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        }

    });

    // Mic Button Click Event
    $("#micBtn").click(function () { 
        $("#oval").attr("hidden", true);
        $("#siriWave").attr("hidden", false);
        
    });
});

$(document).ready(function () {

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


    // SiriWave Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style: "ios9",
        amplitude: 1, // Numeric value, not a string
        speed: 0.3   // Numeric value, not a string
    });

    $("#micBtn").click(function () {
        $("#oval").attr("hidden", true);
        $("#siriWave").attr("hidden", false);
        eel.playAssistantSound() // Call the exposed Python function
        eel.allCommands()()
    });

});

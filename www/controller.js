// This JavaScript file is used for connecting the front-end HTML file to the back-end.
//connecting siri-message class to te command.py



$(document).ready(function () {
    // Display Speak Message
    eel.expose(DisplayMessage)
    function DisplayMessage(message) {
        $(".siri-message li:first").text(message);
        $(".siri-message").textllite('start');
    }

    //Display Hood
    eel.expose(ShowHood)
    function ShowHood() {
        $('#oval').attr("hidden", false); // here when we click on mic then oval class should be hiden
        $('#siriWave').attr("hidden", true);
    }
});


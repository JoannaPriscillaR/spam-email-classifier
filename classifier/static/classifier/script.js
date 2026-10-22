const textarea = document.getElementById("message");
const charCount = document.getElementById("charCount");

if (textarea) {
    textarea.addEventListener("input", function () {
        charCount.textContent = textarea.value.length + " characters";
    });
}

function clearText() {
    textarea.value = "";
    charCount.textContent = "0 characters";
}

function fillSpamSample() {
    textarea.value = "Congratulations! You won a cash prize. Click here now to claim your free lottery bonus.";
    charCount.textContent = textarea.value.length + " characters";
}

function fillSafeSample() {
    textarea.value = "Hello team, please find attached the meeting agenda for tomorrow's project discussion.";
    charCount.textContent = textarea.value.length + " characters";
}
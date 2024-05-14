const button = document.querySelector("button");
const SpeechRecognition =
 window.SpeechRecognition || window.webkitSpeechRecognition;

 const recognition = new SpeechRecognition();

recognition.onstart = function() {
 console.log("Speech recognition is started ");    
};

recognition.onresult = function (event) {
    console.log(event);

    const spokenwords = event.results[0] [0].transcript;

    console.log("spoken words are",spokenwords);
    computerSpeech(spokenwords);
};


function computerSpeech(words) {
    const speech = new SpeechSynthesisUtterance();
    speech.lang  = "en-US";
    speech.lang  = "ml-IN";
    speech.pitch = 1;
    speech.volume= 100;
    speech.rate  = 1;

    determineWords(speech, words);

    window.speechSynthesis.speak(speech); 
}

 function determineWords(speech,words) {
 if (words.includes("day or night")) {
    speech.text = "day";

 }
    
    
}


 
button.addEventListener("click", () => {
    recognition.start();
});
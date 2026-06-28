
document.addEventListener("DOMContentLoaded", function() {
    const sendBtn = document.getElementById("send-btn");
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    sendBtn.addEventListener("click", sendMessage);
    input.addEventListener("keypress", function(event){
        if(event.key==="Enter"){
            sendMessage();
        }
    });

    function addMessage(sender,text){
        const div=document.createElement("div");
        div.innerHTML=`<b>${sender}:</b> ${text}<br><br>`;
        chatBox.appendChild(div);
        chatBox.scrollTop=chatBox.scrollHeight;
    }

    async function sendMessage(){
        const message=input.value.trim();
        if(message==="") return;
        addMessage("You",message);
        input.value="";
        const response=await fetch("/chat",{
            method:"POST",
            headers:{"Content-Type":"application/json"},
            body:JSON.stringify({message:message})
        });
        const data=await response.json();
        addMessage("Gemini",data.response);
    }
});
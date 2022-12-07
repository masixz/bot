class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button'),
            zoomButton: document.querySelector('.zoom__button')
        }

        this.state = false;
        this.messages = [];
    }

    display() {
        const {openButton, chatBox, sendButton, zoomButton} = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox))

        sendButton.addEventListener('click', () => this.onSendButton(chatBox))

        zoomButton.addEventListener('click', () => this.zoom(chatBox))

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(chatBox)
            }
        })
    }

    toggleState(chatbox){
        this.state = !this.state;
        
        if(this.state) {
            chatbox.classList.add('chatbox--active')
            
        } else {
            chatbox.classList.remove('chatbox--active')
        }
    }

    zoom(chatbox){
        this.state = !this.state;

        if(this.state) {
            const element = document.querySelector('.chatbox__support');
            element.style.height = '450px';
            element.style.width = '350px';
        } else {
            const element = document.querySelector('.chatbox__support');
            element.style.height = '600px';
            element.style.width = '650px';
            const element2 = document.querySelector('.chatbox__header');
            element2.style.position = 'sticky';
        }
    }
    
    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 }
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
              'Content-Type': 'application/json'
            },
          })
          .then(r => r.json())
          
          .then(r => {
            let msg2 = { name: "Bot", message: r.answer };
            this.messages.push(msg2);
            this.updateChatText(chatbox)
            textField.value = ''

        }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(chatbox)
            textField.value = ''
          });
    }


    updateChatText(chatbox) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {

            //if (item.name === "Bot" && item.text1 == "mat0001"){
                //html += '<div class="messages__item messages__item--visitor">' + item.message + '<p>&nbsp;</p>' + '<button class="chatbox__send--footer send__button" onClick="openPopup()">Price</button>' + '<p>&nbsp;</p>' + '</div>'

            //}
        let gg = "MAT0001"
        // let vastaus = item.messages.includes(gg)

            if (item.name === "Bot")
            {
                // for (let i = 0; i < cars.length; i++) {
                //     text += cars[i] + "<br>";
                //   }
                  
                if(item.text2.includes(gg)===true){
                    html += '<div class="messages__item messages__item--visitor">' + item.message  + '<p>&nbsp;</p>' + '<button class="chatbox__send--footer send__button" onClick="openPopup()">Price</button>' + '<p>&nbsp;</p>'+'</div>'

                }
                else{
                    html += '<div class="messages__item messages__item--visitor">' + item.message  + '</div>' 
                }
                
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message  + '</div>' 
            }
          });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;
    }

   // updateChatTextStart(chatbox){
        //var html1 = '';
            //message1= "Hi! Wlcome to the materialbot! You can search materials by using material codes. In left top corner is zoom button, if you want to zoom the window"
            //html1 += '<div class="messages__item messages__item--visitor">' + item.message1 + '</div>'
            //const chatmessage1 = chatbox.querySelector('.chatbox__messages');
            //chatmessage1.innerHTML = html1;
   // }

}

const chatbox = new Chatbox();
chatbox.display();

document.addEventListener('DOMContentLoaded',()=>{
  //MAKE Enter key submit messages
  let msg = document.querySelector('#user_message');
  msg.addEventListener('keyup',event => {
    event.preventDefault();
    if (event.keyCode === 13) {
      document.querySelector('#send_message').click();
    }
  })
})

document.addEventListener('DOMContentLoaded',()=> {
  var socket = io.connect('http://' + document.domain + ':' + location.port);

  let room = "General";
  joinRoom("General");
//Display incoming messages
  socket.on('message',data => {
    const p = document.createElement('p');
    const span_username = document.createElement('span');
    const span_timestamp = document.createElement('span');
    const br = document.createElement('br');
    if (data.username) {
      span_username.innerHTML = data.username;
      span_timestamp.innerHTML = data.time_stamp;
      p.innerHTML = span_username.outerHTML+br.outerHTML+data.msg+br.outerHTML+span_timestamp.outerHTML;
      document.querySelector('#display_message_section').append(p);
    } else {
      printSysMsg(data.msg);
    }

  });

  //send message
  document.querySelector('#send_message').onclick = () => {
    socket.send({'msg':document.querySelector('#user_message').value,
                  'username':username,'room':room});
  //clear input area
  document.querySelector('#user_message').value = '';
  }
  //Room selection
  document.querySelectorAll('.select-room').forEach(p=>{
    p.onclick = () => {
      let newRoom = p.innerHTML;
      if (newRoom==room) {
        msg = `You are already in ${room} room.`
        printSysMsg(msg);
      } else {
        leaveRoom(room);
        joinRoom(newRoom);
        room = newRoom;
      }
    }
  });
  //Leave rooms
  function leaveRoom(room) {
    socket.emit('leave',{'username':username,'room':room});
  }
  //join rooms
  function joinRoom(room){
    socket.emit('join',{'username':username,'room':room});
    //clear message area
    document.querySelector('#display_message_section').innerHTML = ''
    //autofocus on the text box
    document.querySelector('#user_message').focus()
  }
  //print system messages
  function printSysMsg(msg) {
    const p = document.createElement('p');
    p.innerHTML = msg;
    document.querySelector('#display_message_section').append(p)
  }
})

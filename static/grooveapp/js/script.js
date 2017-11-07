$(function(){
    var messages = [];
    function loadMessages() {
         $.getJSON('/api/lobby_messages', {after: 'a minute ago'}, function(res) {
             messages = res;
             showMessages();
        })
    }
    function showMessages() {
        var html = '';
        messages.forEach(function (msg) {
        html +=  '<div class="message" id="lobby_message">'
        html +=        '<p class="user-message">Message: '  + msg.text + '</p>'
        html +=        '<p class="posted-by">posted by: ' + msg.author + '</p>'
        html +=        '<p class="time">time: ' + msg.time + '</p>'
        html +=   '</div>'
        })
        $('#messages').html(html)
    }
    function addMessage() {
        var text = $('#message').val();
        messages.push({
            "author": "me",
            "time": new Date(),
            "text": text
        });
        showMessages();
        $.ajax({
                type: "POST",
                url: '',
                data: $("#form").serialize(),
                    success: function(data)
                    {
                          console.log(data, 'success')
                    }
         });

    }

    $('#message').keydown(function() {
    if ($('#message').val().length > 0) {
        if(e.ctrlKey && e.keyCode == 13 ) {
            addMessage()
        } else {
            alert('Please type smt')
        }

    })
    $('#submit').click(function() {
        if ($('#message').val().length > 0) {
            addMessage()
            loadMessage()
        }else {
            alert('Please type smt')
        }
    })
    // $('button').click(addMessage)
     setInterval(function() {
        console.log('refresh')
        loadMessages();
    }, 2000)

    console.log('first load')
    loadMessages();

});
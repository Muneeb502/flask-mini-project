const messageTextArea = document.getElementById('message');

messageTextArea.addEventListener('mouseenter', function() {
    this.style.backgroundColor = '#f3d111';
    this.style.color = 'black';
});

messageTextArea.addEventListener('mouseleave', function() {
    this.style.backgroundColor = ''; 
    this.style.color = ''; 
});
function clearText() {
    var textarea = document.getElementById('message');
    if (textarea.value === 'how may we help you?') {
        textarea.value = '';
    }
}

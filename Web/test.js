function launch_command(){
   console.log("Button clicked");
   console.log(document.getElementById('input').value);
   $.ajax({
      url: 'http://ks.x-ray.fr:5000/run/'+Base64.encode(document.getElementById('input').value),
      dataType: 'text',
      complete: function(data){
         console.log(data)
         document.getElementById('output').value = data.responseText
         document.getElementById('inputid').value = JSON.parse(data.responseText).result
      },
      success: function(data){
         console.log(data.responseText)
      },
      error: function(){
         console.log("failure")
      },
      timeout: 3000
   });
}


function launch_command_id(){
   console.log("Button id clicked");
   console.log(document.getElementById('input').value);
   $.ajax({
      url: 'http://ks.x-ray.fr:5000/id/'+document.getElementById('inputid').value,
      dataType: 'text',
      complete: function(data){
         console.log(data);
         document.getElementById('outputid').value = data.responseText
      },
      success: function(data){
         console.log(data.responseText)
      },
      error: function(){
         console.log("failure")
      },
      timeout: 3000
   });
}



function check(){
    var uname = document.getElementById('checkuname').value;
    url = "https://api.apispreadsheets.com/data/14419/?query=select*from14419whereusername='" + uname + "'";
    fetch(url)
        .then(response => response.json())
        .then((json)=>{
            if(json['data'].length == 0){
                alert("username available and set");
                document.getElementById('username').value = uname;
            }
            else{
                alert('unavailable try another');
            }
        })
}





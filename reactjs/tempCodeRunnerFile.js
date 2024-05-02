let url = "http://20.244.56.144/test/register";

fetch(url, {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({ 
        
            "companyName": "Affordmed",
            "ownerName": "PRASANTH S",
            "rollNo": "113021104083",
            "ownerEmail": "sprasanth_cse21@velhightech.com",
            "accessCode": "yqlhcX"
    })
})
   .then(response => response.json())
   .then(response => console.log(JSON.stringify(response)))

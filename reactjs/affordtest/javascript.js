let url = "http://20.244.56.144/test/auth";

fetch(url, {
  method: "POST",
  headers: {
    Accept: "application/json",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    companyName: "Affordmed technologies",
    clientID: "d08e019c-0698-479c-b8b7-2b4a818b5a09",
    clientSecret: "dVIrgjXzugELtyyw",
    ownerName: "PRASANTH",
    ownerEmail: "divya@gmail.com",
    rollNo: "83",
  }),
})
  .then((response) => response.json())
  .then((response) => console.log(JSON.stringify(response)));

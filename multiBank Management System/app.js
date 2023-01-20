// How_We_Structure_This_Application = {
//     "client":"Rahega",
//     "Server":"Rahega",
//     "database":"Rahega"
// }

// Three-Tier-Architecture
/*

        req             req
CLIENT <-----> SERVER <-----> DATABASE
        res             res           

req_Type = [
    'login',
    'registration'
]

*/



// const { validate } = require("node-cron")

// Login

// userName and password shold be validated

// get data from database;

// get data based on userName;
// then use Password to validate;

// if usernot found --> userNot found please register
// if userFound
//     match password --> if matched then Login    
//                         else password incorrect



// ----

obj = {
    "users": [
        {
            "Name": "Amol",
            "age": 25
        },
        {
            "Name": "Kishor",
            "age": 25
        },
        {
            "Name": "Ankus",
            "age": 25
        }
    ]
}

// {key:value}

user = {
    "name":"Aditi",
    "age":23,
    "address":{
        "street":"MG Road",
        "area":"friends Colony",
        "city":"Butibory",
        "Dist":"Nagpur",
        "State":"Maharashtra"
    }
}




console.log("My objects type is: ",user.age)
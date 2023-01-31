profile={"name":"Ram","Genger":"male",
"Education":[
    {"college":"ABC college","Level":"+2"},
    {"college":"XYZ college","Level":"Bachelor"},
],
"address":[

    {"tempprary":{
        "word":1,
        "city":"Kathmandu",
    },
    "permanent":{
        "word":2,
        "city":"Kavre",
    }
    }
]

}

# now printing the value
print(f"Name:{profile.get('name')}")
print(f"Gender:{profile.get('Gender')}")
print(f"Education:{profile.get('Education')}")
Education=profile.get("Education")
for Education in Education:
    print(f"college:{Education.get('college')} and Level:{Education.get('Level')}")

address=profile.get("address")
for address in address:
  #  print(f"college:{address.get('tempprary')} and word:{address.get('word')}")
  for key, val in address.items():
    print(key,val.get('word'))
    print(key,val.get('city'))

    


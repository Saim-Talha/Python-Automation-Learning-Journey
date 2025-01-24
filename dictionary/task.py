myinfo = {
"server1" : {
"IBM": {
"datacenter":"Bangalore",
"env": {
"PR": "192.168.1.1",
"DR": "192.168.1.2"
}
}
    }
}
#print("dictionary syntaxx is ok")
pr_addr=(myinfo['server1']['IBM']['env']['PR'])
dr_addr=(myinfo['server1']['IBM']['env']['DR'])

print("Banglore daatcenter PR address is: ",pr_addr)
print("Banglore daatcenter DR address is: ",dr_addr)


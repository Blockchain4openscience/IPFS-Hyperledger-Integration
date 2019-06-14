import ipfshttpclient
import requests

input("Welcome, Please ensure IPFS daemon is running. If not, Use command 'sudo ipfs daemon'")

try:
	client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001/http')
	filename = input("Enter the filename stored in current directory (with extension)")
	res = client.add(filename)
	print("The hash of file is : ",res['Hash'])
	rid = input("\nEnter the Researcher ID")
	researcher = "resource:org.jro.Researcher#"+str(rid)
	rojid = input("\nEnter the Research object ID")
	print("\n Adding the research object to the blockchain")
	r = requests.post('http://localhost:3000/api/Add', data = { "$class": "org.jro.Add", "rojId": rojid, "node": res['Hash'], "creator": researcher })
	if r.status_code==200:
		print("\n Success")
	

except ConnectionRefusedError:
	print("Connection error, Please ensure ipfs daemon is running.")



# IPFS-Hyperledger integration

This is a Python script which adds a given Research Object to IPFS and stores the hash into Hyperledger based blockchain using composer-rest-server and ipfshttpclient (or py-ipfs-api : https://github.com/ipfs/py-ipfs-api). 
## Download
You need to install IPFS, Follow instruction here to do so : https://docs.ipfs.io/guides/guides/install/

Clone this git repo on your local computer and enter the working directory 

```bash
cd IPFS-Hyperledger-Integration/
```

## Installation

Create a Python Virtualenvironment
```bash
virtualenv venv
source venv/bin/activate
```
Install required dependencies 
```bash
pip install -r requirements.txt
```
## Usage

Run IPFS daemon :
```bash
ipfs daemon
```


Start composer-rest-server (Write no if asked for api protection):
```bash
composer-rest-server
```


Lets say you have a file alice.txt in the same directory as the add-to-ipfs.py and would like to add this file to IPFS and store the resulting hash into the blockchain which is currently using the Journal of Research Objects BNA file (jro@0.0.1.bna).

Run the script : 
```bash
python3 add-to-ipfs.py
```
Press enter when prompted to run ipfs daemon. Now, enter the name of file you want to be added, ROJ ID and Researcher ID. The script will return the hash of the file and will output 'Success!' if the metadata (hash) is successfully entered in the blockchain.

To verify that script has worked properly, Go to composer-rest-server explorer at http://localhost:3000/explorer/ and click on ROJ/<id>. Send a GET request with the  ROJ id you had specified and click on "Try it out". If it returns the hash and other metadata, The script has worked properly.



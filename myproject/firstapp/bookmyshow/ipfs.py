from ipfshttpclient import Client


#adding a file to ipfs 
def clientipfs1():
    print("file content CID Hash")
    client = Client()
    with open(r"C:\Users\aparna\myproject\firstapp\bookmyshow\trial.txt", "rb") as f:
        response = client.add(f)
        print(response["Hash"])
clientipfs1()



# #content IPFS cid
# def fetch_content_from_ipfs(cid):
#     client = Client()    
#     content = client.cat(cid)
# #     #sample = client.
#     return content.decode()
# cid = r"QmSr84r9v9XF84xveJr1nPxy2Kh6HQXoXPhEP89Hm4MhhZ"
# content = fetch_content_from_ipfs(cid)
# print(content)
# https://leetcode.com/problems/defanging-an-ip-address/
def defangIPaddr(address: str) -> str:
    return address.replace('.', '[.]')

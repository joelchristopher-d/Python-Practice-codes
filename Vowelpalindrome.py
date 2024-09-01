def isPalindrome(low,high,s):
    while(low<=high):
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    return True


string = "miami"
string="welcome"
string="boat"
string=str(input()).lower()
vowels = ["a","e","i","o","u"]
store = ""
for i in string:
    if i in vowels:
        store+=i
# print(store)
isPalindrome(0,len(store)-1,store)

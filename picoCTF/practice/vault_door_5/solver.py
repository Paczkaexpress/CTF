arr = ["3b","65","21","a", "38","0", "36","1d","a", "3d","61","27","11","66","27","a", "21","1d","61","3b","a", "2d","65","27","a", "66","36","30","67","6c","64","6c"]

arr = [chr(int(x,16) - 33) for x in arr]
print(arr)
from datetime import datetime

class solution:
    def time_conv(self, s):
        time_12hr = datetime.strptime(s, "%I:%M:%S%p")
        time_24hr = time_12hr.strftime("%H:%M:%S")
        return time_24hr
    
if __name__ == "__main__":
    s = str(input('Enter the time :'))
    time = solution().time_conv(s)
    print(f"Converted time :{time}")
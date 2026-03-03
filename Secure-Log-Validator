from validator_collection import validators
import re 


def main():
    try:
        x = input("Login: ").split("|")
    except ValueError:
        raise ValueError("Invalid input format")
    n,g,t = x[0].strip(), x[1].strip(), x[2].strip()
    
    print(f"Usser: {name(n)}\nEmail: {email(g)}\nHours: {time(t)}")




def name(n):
    name = re.search(r"^(\w+).*$",n)
    if name:
      return name.group(1)
    else:
        raise ValueError




def email(g):
    try:
        validators.email(g)
        return g 
    except ValueError:
        raise ValueError



def time(t):
    t= re.search(r"^(\d{1,2})(?:\:?(\d{2}))?\s(AM|PM)\s?to\s?(\d{1,2})(?:\:?(\d{2}))?\s(AM|PM)$")
    if t:
        h,h1 = int(t.group(1)), int(t.group(4))
        m,m1 = int(t.group(2) or 0), int(t.group(5) or 0)
        p,p1 = t.group(3), t.group(6)
        if m <0 or m > 59 or m1 <0 or m1 > 59 or h1>12 or h> 12 :
            raise ValueError
        if p == "PM" and h != 12:
            h+=12
        elif p == "AM" and h == 12:
            h =0
        if p1 == "PM" and h1 != 12:
            h1+=12
        elif p1 == "AM" and h1 == 12:
            h1 =0
        return f"{h:02}:{m:02} to {h1:02}:{m1:02}"
    if not t:
        raise ValueError

import requests, re, string, random
upper_case = 1
name_upper_chars = string.ascii_uppercase
upper_name = ''.join(random.choice(name_upper_chars) for y in range(upper_case))
name_size = 4
name_chars = string.ascii_lowercase
name = ''.join(random.choice(name_chars) for x in range(name_size))
digits_size = 4
digits_chars = string.digits
digits = ''.join(random.choice(digits_chars) for z in range(digits_size))
username = upper_name + name + digits

Year, Month, Day = (1990,1,10)

password = username[::-1]
email = username+"@goplaypkm.xyz"
public = False

country = "US"

session = requests.Session()
session.headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:47.0) Gecko/20100101 Firefox/47.0"
tokenRE = re.compile(r"<input type='hidden' name='csrfmiddlewaretoken' value='([\s\S]+)' \/>")

first = session.get("https://club.pokemon.com/us/pokemon-trainer-club/parents/sign-up")

csrfmatch = tokenRE.search(first.text)

if csrfmatch is None:
    raise Exception("First CSRF Token Missing!")

postData = [
    ('csrfmiddlewaretoken',csrfmatch.group(1)),
    ('dob','%d-%d-%d' % (Year, Month, Day)),
    ('country',country),
    ('country',country),
    ('undefined',"%d" % (Month-1)),
    ('undefined',"%d" % Year),
    ]
session.headers['Referer'] = "https://club.pokemon.com/us/pokemon-trainer-club/sign-up/"
second = session.post("https://club.pokemon.com/us/pokemon-trainer-club/sign-up/",data=postData)

csrfmatch = tokenRE.search(second.text)

if csrfmatch is None:
    raise Exception("Second CSRF Token Missing!")

postData = [
    ('csrfmiddlewaretoken',csrfmatch.group(1)),
    ('username',username),
    ('password',password),
    ('confirm_password',password),
    ('email',email),
    ('confirm_email',email),
    ('public_profile_opt_in',public),
    ('screen_name',""),
    ('terms',"on"),
    ]
session.headers['Referer'] = "https://club.pokemon.com/us/pokemon-trainer-club/parents/sign-up"
third = session.post("https://club.pokemon.com/us/pokemon-trainer-club/parents/sign-up",data=postData)

print username+","+password

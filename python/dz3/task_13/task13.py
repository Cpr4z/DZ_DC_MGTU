import re

def check_string(string:str) -> bool:
    return check_num(string) or check_email(string)

def check_num(string:str) -> bool:
    pattern_phone = re.compile(r'^(8[-\s]?|\+?7[-\s]?)?'
                               r'\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2}$')
    return pattern_phone.match(string) is not None

def check_email(string:str) -> bool:
    pattern_email = re.compile(r'^[\w.]+@[\w.]+\.\w{2,}$')
    return pattern_email.match(string) is not None

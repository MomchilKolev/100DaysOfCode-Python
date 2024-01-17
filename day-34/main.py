# age: int
# name: str
# height: float
# is_human: bool

def police_check(age: int) -> bool:
    if age > 10:
        can_drive = True
    else:
        can_drive = False
    return can_drive

if police_check(19):
    print("May pass")
else:
    print("Stop")

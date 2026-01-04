full_dot = '●'
empty_dot = '○'
name = str(input('Enter Name')).strip()
strength = int(input('Enter Strength'))
intel = int(input('Enter Intelligence'))
rizz = int(input('Enter Charisma'))
def create_character(name, strength, intel, rizz):
    if len(name) < 0:
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif type(name) is not str:
        return 'The character name should be a string'
    elif name.count(' ') >= 1:
        return 'The character name should not contain spaces'
    

    if strength < 1 or intel < 1 or rizz < 1:
        return 'All stats should be no less than 1'
    elif type(strength) is not int or type(intel) is not int or type(rizz) is not int:
        return 'All stats should be integers'
    elif strength > 4 or intel > 4 or rizz > 4:
        return 'All stats should be no more than 4'
    elif (strength + intel + rizz) != 7:
        return 'The character should start with 7 points'
    else:
        x = full_dot * strength
        x1 = empty_dot * (10 - strength)
        y = full_dot * intel
        y1 = empty_dot * (10 - intel)
        z = full_dot * rizz
        z1 = empty_dot * (10 - rizz)
        return f'{name}\nSTR {x}{x1}\nINT {y}{y1}\nCHA {z}{z1}'
    
if __name__ == '__main__':
    print(create_character(name, strength, intel, rizz))

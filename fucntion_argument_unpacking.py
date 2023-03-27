def greeting(*args):
    print('Hi ' + ' '.join(args))
    # print(args) Nos devuelve los valores en forma de tupla


greeting('Tiffany', 'Hudgens')
greeting('Tiffany', 'M', 'Hudgens')


def greeting(time_of_day, *args):
    print(f"Hi  {' '.join(args)}, I hope that you are having a good {time_of_day}")


greeting('Morning', 'Tiffany', 'Hudgens')
greeting('Afternoon', 'Tiffany', 'M', 'Hudgens')
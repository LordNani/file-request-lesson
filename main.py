import os
import zipfile
def testLists():
    animals = ['cat', 'dog', 'bird', 'bat']
    animals3 = ['horse', 'pig']
    print(animals[0])
    print(animals[len(animals) - 1])
    print(animals[-1])
    print(animals[-4])
    print(animals[0:-1])
    print(animals[:2])
    print(animals[:])
    animals2 = animals[1:]
    animals.append('shark')
    print(animals2)
    animals = animals + animals3
    # animals = animals*2
    del animals[2]
    print(animals)
    a, b = 'Alice', 'Bob'
    a, b = b, a

    if 'cat' in animals:
        print('Yes it is')


def testPath():
    localfile = '../../tawt/pyconfig.cfg'
    file = 'C:/Users/Lord/source/python/filesystem-lesson'

    path1 = R"% HOMEPATH %\Directory\file.txt"
    path2 = R"C:\Users\$USERNAME\Directory\file.txt"
    path3 = R"${TEMP}\file.txt"
    exp_var1 = os.path.expandvars(path1)
    exp_var2 = os.path.expandvars(path2)
    exp_var3 = os.path.expandvars(path3)
    print(f'{exp_var3 = }')

    path_to_file = os.path.join('python', 'venv', 'python.cfg')
    print(path_to_file)

    print(os.getcwd())

    # os.makedirs('files')
    print(os.path.exists('main.py'))

def testFiles():
    path = os.path.join(os.getcwd(), 'files', 'test.txt')
    print(f'{path=}')
    if os.path.exists(path):
        with open(path) as file:
            content = file.readlines()
            for line in content:
                print(line)
            file.close()

    with open(path, 'a') as file:
        file.write('New text!awdawdwa')
        file.close()

    with zipfile.ZipFile('new2.zip', 'w') as new_zip:
        new_zip.write('files/test.txt', compress_type=zipfile.ZIP_DEFLATED)

    with zipfile.ZipFile('new2.zip') as example_zip:
        example_zip.extractall('test')

if __name__ == '__main__':
    testFiles()


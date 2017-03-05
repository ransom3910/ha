import yaml
import sys
from pyperclip import copy
from pyperclip import paste




def main():
    document=str()
    final=str()
    for lines in iter(input,'###'):
     document=document+lines+'\n'

    print(document)
    dump=yaml.load(document)
    for x in dump:
        temp = x.get('alias').lower().replace(' ', '_')
        temp = temp.replace(':','').replace('-','')
        temp =  '    - automation.' + temp
        print(temp)
        final = temp + final
    copy(final)
if __name__ == '__main__':
    main()








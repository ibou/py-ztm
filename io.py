import sys, os
from translate import Translator

directory = os.path.dirname(os.path.abspath(__file__))

def read_file(filename):
    with open(os.path.join(directory, filename), 'r') as f:
        return f.read()
      
def write_file(filename, content):
    with open(os.path.join(directory, filename), 'w') as f:
        f.write(content)
        
def main():
    try:
        with open('test.txt') as f:
          text = f.read()
          translator = Translator(to_lang='es')
          translation = translator.translate(text)
          write_file('test-fr.txt', translation)
          print(translation) 
    except FileNotFoundError as e:
        print(e)
    
if __name__ == '__main__':
   main()
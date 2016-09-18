# NOTE: Need Python 2 because compatibility is awful. :(

import clipboard
import xeger


if __name__ == '__main__':
   while True:
      try:
         _regex = raw_input()
         clipboard.copy(xeger.xeger(_regex))
         print("SUCCESS!")
      except Exception:
         print("FAILED!")

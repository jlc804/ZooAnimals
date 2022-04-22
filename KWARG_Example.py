# learning **kwrgs
# client (as a function) -----------------------------------
def main():
   show_all(a = 2, b = "three", c = 1, d = 4.5, e = "eieio", f = -200)
   print()
   show_two_then_others(a = 2, b = "three", c = 1, d = 4.5, e = "eieio", f = -200)
   print()
   a = 2
   y = a
   print(id(a),id(y))
   a = 10000
   y = 9999+1
   print(id(a), id(y))
   print(a, y)


# END CLIENT main()  -------------------------------------------
# BEGIN Global Scope functions ---------------------------------

def show_two_then_others(d = 0, a = 0, **kwargs):
   print( "keyname args d and a are {} and {}.".format(d, a) )
   print( "the rest are:" )
   show_all(**kwargs)

def show_all(**kwargs):
   for z in kwargs:
      print( "  {} : {}".format(z, kwargs[z]) )

# END Global Scope functions ---------------------------------
# -------------- main program -------------------
if __name__ == "__main__":
    main()


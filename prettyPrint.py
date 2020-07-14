import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
pp = pprint.PrettyPrinter(indent=4)
#pp = pprint.PrettyPrinter(width=41, compact=True)
pp.pprint(stuff)

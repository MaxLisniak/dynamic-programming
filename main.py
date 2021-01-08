items = {}
items["stereo"] = [3000, 4]
items["laptop"] = [2000, 3]
items["guitar"] = [1500, 1]
items["iphone"] = [2000, 1]
items["mp3"] = [1000, 1]
items["computer"] = [2500, 2]
columns = [1,2,3,4]
rows = [item for item in items]

table = [[] for ]
table = {item:{}for item in items}
prev_item = None
for item in table:
  table[item] = {title:[] for title in columns}
  for size in table[item].keys():

  #     if prev_item == None:
  #       if items[item][1] > size:
  #         table[item][size] = None
  #       else:
  #         table[item][size].append(items[item][0])
  #         table[item][size].append(item)
  #     else:
  #       if size == items[item][1]:
  #         if table[prev_item][size] == None:
  #           table[item][size] = [items[item][0], item]
  #         else:
  #           if table[prev_item][size][0] >= items[item][0]:
  #             table[item][size] = table[prev_item][size]
  #           else:
  #             table[item][size].append(items[item][0])
  #             table[item][size].append(item)
  #       elif items[item][1] > size:
  #         if table[prev_item][size] == None:
  #           table[item][size] = None
  #         else:
  #           table[item][size] = table[prev_item][size]
  #       else:  
  #         if table[prev_item][size] == None:
  #           table[item][size] = [items[item][0], item]
  #         else:
  #           if table[prev_item][size][0] >= items[item][0] + table[prev_item][size - items[item][1]][0]:
  #             table[item][size] = table[prev_item][size]
  #           else:
  #             table[item][size] = table[prev_item][size - items[item][1]]
  #             table[item][size][0:0]=(items[item][0] + table[prev_item][size - items[item][1]][0])
  #             table[item][size].append(item)


  prev_item = item

def oxford_comma(items):
    if len(items) == 1 :
       return "".join(items)  
    elif len(items) == 2:
       return " and ".join(items)
    else:
        str_item=""
        i=1
        for item in items:
            if (len(items) == i ):
              str_item=str_item + "and " + item
            else:  
              i+=1
              str_item=str_item + item + ", "
    return str_item

print(oxford_comma(["kiwi", "durian", "starfruit", "mangos", "dragon fruits"]))
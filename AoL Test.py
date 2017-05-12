def readnames(textfile, namesfile):
  #Open the files
  textWithNames = open(textfile, "r")
  namesFile = open(namesfile, "r")
  #create a results string
  #use sring.split to make each word into a list object
  results = []
  amountoflines = 0
  #create information I will test
  names[] = namesFile.split()
  textLines[] = textWithNames.split()
  #start checking for names


  while lines:
      amountoflines += 1
      lines = textWithNames.readline()
    textLines.close()
    
  #append, adds on whatever you want directly to the list. e.g. 
  #(x = [1, 2, 3] x.append([4, 5]) printing x returns
  # [1, 2, 3, [4, 5]]
  for(name in names):
    #load names into result
    results = results.append([name, ""])
 
     
    #find the lines that contain the name
    for i in range(1, amountoflines + 1):
      if(textLines[i].index(names) >= 0)
        results[name].extend([i])
  print(results)
    
  
  
  
  
  




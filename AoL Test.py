import os
os.chdir(r"C:\Users\georg_ozhdqy2\Documents\Names")
class Reader:
  def readnames(self):
  
    linenumber = 0
    namecount = 0
    results = []
    textLines = []
  
    #importing os so i can get file directory
    
    
    #Open the files
    #textWithNamesFile = open("TextWithNames.txt")
    #namesFile = open("Names.txt")

    #create a results list
    
    
    
    
    #Load the file into Memory
    
    with open("TextWithNames.txt") as f:
      text = f.readlines()
    text = [x.strip() for x in text]
    f.close()
   # Load the names into Memory
    with open("Names.txt") as q:
      names = q.readlines()
    names = [y.strip() for y in names] 
      
    q.close()
    
    for i in range(0, len(text)):
      textLines.append([text[i]]) 
  #you may also want to remove whitespace characters like `\n` at the end of each line
    

      
    #Find the names in the text
    for name in names:
      results.append(names[namecount])
      
      
      linenumber = 0
      for whichline in textLines:
        
        if (any(names[namecount][0] in sublist for sublist in textLines[linenumber]) == True):
          
          results[namecount] = results[namecount] + " -> " + str(linenumber)
      
        linenumber = linenumber + 1
      namecount = namecount + 1
      
    print(results)  
      

      

reader = Reader()
reader.readnames()
  
  
  
  




from datetime import datetime
file1 ='inputFile.log'

fLogs_FILE = 'failed test cases.txt'
output='fully parsed ouptut.txt'
important = []
#a function to parse the logs
    
def parse_logs():                  
                  
#check whether test is failed or passed according to logs     
    get_lines= True
    with open(file1) as f:
        f = f.readlines()
    
    for line in reversed(f):
      if  "Failed" in line :
        get_lines=True
        index=0
        important.append("\n")
      if  "Passed" in line:
        get_lines=False
        
    
      if  "Failed" in line or line.startswith("20") and get_lines:
        important.append(line)
       
    important.append("\n") 
#write failed logs to a text file
    with open(fLogs_FILE,'w') as text_file:
        text_file.writelines(important) 
    text_file.close()
    with open(fLogs_FILE) as flogs_file:
        fLogs = flogs_file.readlines()
#from failed logs text file get the timestamps
#group the rows using new line as delimeter  
        groups = [[]] #used to extract the time stamps
        out_logs=[[]] #used to make final log file
        index = 0
        for line in fLogs:
            if line != '\n':
                out_logs[index].append(line)
                groups[index].append(line[:23])
    
            else:
                index += 1
                groups.append([])
                out_logs.append([])
    groups=groups[1:-1]
    out_logs=out_logs[1:-1]
    titles=[]# extract test case as titles
    for item in groups:
      titles.append(' '.join(item[0].split()[:3]))
      item.pop(0)
      item.pop(0)
      
    res = {}
    for key in titles:
        for value in groups:
            res[key] = value
            groups.remove(value)
            break
    deltas=[]#calculate time delta
    for item in res.values():
      i=len(item)
      deltas.append(str(datetime.strptime(item[0],'%Y-%m-%d %H:%M:%S.%f')- datetime.strptime(item[i-1],'%Y-%m-%d %H:%M:%S.%f')))
    time_delta_result ={}
    time_complete_result = [] 
    output_results={}
    #merge time delta and titles in a dictionary
    for key in titles:
      for value in deltas:
        time_delta_result[key]=value
        deltas.remove(value)
        break
    #merge title and time delta as a string
    for key, val in time_delta_result.items(): 
        time_complete_result.append(' '.join([key,str(" DOS time: "+val) ]))
      #merge logs and detailed title into one log list   
    for key in time_complete_result:
      for value in out_logs:
        output_results[key]=value
        out_logs.remove(value)
        break 
       #wrie final output to a text file called output   
    with open(output,'w') as out_file:
      for key,val in output_results.items():
         out_file.writelines(key)
         out_file.writelines("\n")
         out_file.writelines(val)
         out_file.writelines("\n\n")         

    return time_complete_result
print(parse_logs())

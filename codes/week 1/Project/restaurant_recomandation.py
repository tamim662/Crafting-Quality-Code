import re


def read_restaurent(file):
    name_to_rating={}
    price_to_names={'$':[],'$$':[],'$$$':[],'$$$$':[]}
    cusine_to_names={}
    file_contents=[]
    for line in file:
        if line!= '\n':
            #the strip method is used to remove white spaces in any of the given lines
            file_contents.append(line.strip())
        else:
            #the replace method is used to remove the blank line or new line after the 4th line
            #here instead of replace method we could have used pass too.
            # line.replace('\n', '')
            pass
    #print(file_contents)
    #Creating  a name_to_rating dictionary
    for i  in range(0,len(file_contents),4):
        name=file_contents[i]
        rating=file_contents[i+1]
        rating=int(rating[:2])
        
        
        name_to_rating[name]=rating #put every value with corresponding value
    
    # Creating a price_to_names dictionary
    for key in price_to_names:
        for i in range(0,len(file_contents)):
            if file_contents[i]==key:
            

                price_to_names[key].append(file_contents[i-2])
    
    # Creating a Cusine_to_names dictionary
    for i in range(3,len(file_contents),4):
        dishes=file_contents[i].split(',')
        for dish in dishes:
            cusine_to_names.setdefault(dish,[]) #The magic of setdefault is that it initializes the value for that key if that key is                                             #not defined, 
                                                #not defined.
            cusine_to_names[dish].append(file_contents[i-3])

    # print(cusine_to_names)
    return name_to_rating,price_to_names,cusine_to_names

def filter_by_cusine(names,cuis_dict,cusine):
    name_match_cusine=[]
    for key in cuis_dict:
        for name in cusine:
            if name == key:
                name_match_cusine.append(cuis_dict[key])
    name_match_cusine=sum(name_match_cusine,[])
    updated_list=[]
    for i in range(len(names)):
        if names[i] in name_match_cusine:
            updated_list.append(names[i])
    print("updated_list",updated_list)
    return updated_list
        

def rating_list(final_list,rating_dict):
    new_list=[]
    tmp=[]
    for key in rating_dict:
        if key in final_list:
            temp=[rating_dict[key],key]
            new_list.append(temp)
            
        
    return new_list  # return the list of restaurents name with rating

    



def recommand(file,price,cusine_list):
    name_to_rating, price_to_names, cuisine_to_names =read_restaurent(file)
    names_matching=[]
    for key in price_to_names:
        
        if price==key:
            names_matching.append(price_to_names[key])
    
    names_matching=sum(names_matching,[])

    names_final=filter_by_cusine(names_matching,cuisine_to_names,cusine_list)
    result=rating_list(names_final,name_to_rating)
    rlt=sorted(result,key=lambda l:l[0], reverse=True) # sorting the list according to rating
    return rlt

    

print("Welcome to our Recommandation Site!")

price_demand=input("Enter the Price In the form of $ or $$ or $$$:")
cusine_demand=input("Enter the cusine list with Comma: ").split(',')

my_file=open('restaurants_small.txt','r')

got_result=recommand(my_file,price_demand,cusine_demand)

print("Recommanded Restaurents are:",got_result)
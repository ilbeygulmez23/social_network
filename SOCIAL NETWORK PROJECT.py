#Take all the users in a user list.
#Arrange a dictionary that sets the key as the user and the value as user's friends.
import sys
f=open(sys.argv[1],"r" , encoding="utf-8")
f2=open(sys.argv[2],"r",encoding="utf-8")
f3=open("output.txt","w",encoding="utf-8")
user_list=[]
dict_friends={}
for user in f:
    user_list.append(user.split(":")[0])
    dict_friends[user.split(":")[0]]=[user.split(":")[1].split()]
#Add New User (ANU) function defined by appending to user_list.
def ANU(username):
    if username not in user_list:
        user_list.append(username)
        dict_friends.update({username : [[]]})
        f3.write("User "+"'"+username+"'"+" has been added to the social network successfully.\n")
    else:
        f3.write("ERROR:Wrong input type! for 'ANU'! -- This user already exists!!\n")
#Delete Existing User (DEU) function defined by removing from user_list.Delete the user from all users' friends list with for loop and user_list.remove()
def DEU(username):
    if username not in user_list:
        f3.write("ERROR: Wrong input type! for 'DEU'!--There is no user named "+"'"+username+"'"+" !!\n")
    else:
        user_list.remove(username)
        del dict_friends[username]
        for user1 in dict_friends:
            for user2 in dict_friends[user1][0]:
                if username==user2:
                    dict_friends[user1][0].remove(user2)
        f3.write("User "+"'"+username+"'"+" and his/her all relations have been deleted successfully.\n")
#Add New Friend (ANF) function defined by reaching the value then appending to that index.*Added for both users.
def ANF(source,target):
    if source not in user_list and target in user_list:
        f3.write("ERROR: Wrong input type! for 'ANF'! -- No user named "+"'"+source+"'"+" found!!\n")
    elif target not in user_list and source in user_list:
        f3.write("ERROR: Wrong input type! for 'ANF'! -- No user named "+"'"+target+"'"+" found!!\n")
    elif source and target not in user_list:
        f3.write("ERROR: Wrong input type! for 'ANF'! -- No user named "+"'"+source+"'"+" and "+"'"+target+"'"+" found!!\n")
    elif target in dict_friends[source][0] or source in dict_friends[target][0]:
        f3.write("ERROR: A relation between "+"'"+source+"'"+" and "+"'"+target+"'"+" already exists!!\n")
    else:
        dict_friends[source][0].append(target)
        dict_friends[target][0].append(source)
        f3.write("Relation between "+"'"+source+"'"+" and "+"'"+target+"'"+" has been added successfully.\n")
#Delete Existing Friend (DEF) function defined by reaching the value then equating that index to "".*Delete from both users.
def DEF(source,target):
    if source not in user_list and target in user_list:
        f3.write("ERROR: Wrong input type! for 'DEF'! -- No user named " +"'"+source+"'"+ " found!!\n")
    elif target not in user_list and source in user_list:
        f3.write("ERROR: Wrong input type! for 'DEF'! -- No user named "+"'"+target+"'"+" found!!\n")
    elif source and target not in user_list:
        f3.write("ERROR: Wrong input type! for 'DEF'! -- No user named "+"'"+source+"'"+" and "+"'"+target+"'"+" found!!\n")
    elif target not in dict_friends[source][0] or source not in dict_friends[target][0]:
        f3.write("ERROR: No relation between "+"'"+source+"'"+" and "+"'"+target+"'"+" found!!\n")
    else:
        dict_friends[source][0].remove(target)
        dict_friends[target][0].remove(source)
        f3.write("Relation between "+"'"+source+"'"+" and "+"'"+target+"'"+" has been deleted successfully.\n")
#Count Friend (CF) function defined by reaching the value then print the length of that list.
def CF(username):
    if username not in user_list:
        f3.write("ERROR: Wrong input type! for 'CF'! -- No user named "+"'"+username+"'"+" found!\n")
    else:
        f3.write("User "+"'"+username+"'"+" has "+str(len(dict_friends[username][0]))+" friends.\n")
#Find Possible Friends (FPF) function defined by putting possible friends in a set (so we have no duplicates) then printing the length of it for each distance value seperately.
def FPF(username,maximum_distance):
    friend_tempdict={}
    friend_set=set(friend_tempdict)
    if maximum_distance>=3 or maximum_distance<=0:
        f3.write("ERROR: Wrong input type! for 'FPF'! -- Maximum distance should be less than 3!!\n")
    if username not in user_list:
        f3.write("ERROR: Wrong input type! for 'FPF'! -- No user named "+"'"+username+"'"+" found!!\n")
    if username in user_list and maximum_distance<3 and maximum_distance>0:
        for friend in dict_friends[username][0]:
            friend_set.add(friend)
            for poss_friend in dict_friends[friend][0]:
                if maximum_distance==1:
                    friend_set.add(poss_friend)
                elif maximum_distance==2:
                    friend_set.add(poss_friend)
                    for poss1_friend in dict_friends[poss_friend][0]:
                        friend_set.add(poss1_friend)
        friend_set.remove(username)
        f3.write("User "+"'"+username+"'"+" has "+str(len(friend_set))+" possible friends when maximum distance is "+str(maximum_distance)+"\n")
        f3.write("These possible friends: "+"{"+str(sorted(friend_set))[1:-1]+"}\n")
#Suggest Friends (SF) function defined by putting friends' friends in a list then checking if the list.count matches with MD and printing the matched ones.
def SF(username,mutuality_degree):
    friend_list=[]
    duplicate_list=[]
    duplicate_set=set({})
    if mutuality_degree>3 or mutuality_degree<=1:
        f3.write("ERROR: Wrong input type! for 'SF'! -- Mutuality Degree should be 2 or 3!!\n")
    if username not in user_list:
        f3.write("ERROR: Wrong input type! for 'SF'! -- No user named " +"'"+ username+"'" + " found!!\n")
    if username in user_list and mutuality_degree==2 or username in user_list and mutuality_degree==3:
        for friend in dict_friends[username][0]:
            for friendsfriend in dict_friends[friend][0]:
                if friendsfriend==username:
                    pass
                else:
                    friend_list.append(friendsfriend)
        for duplicate in friend_list:
            if mutuality_degree==2:
                if friend_list.count(duplicate)>=2:
                    duplicate_list.append("'"+duplicate+"'")
                    duplicate_set.add("'"+duplicate+"'")
            if mutuality_degree==3:
                if friend_list.count(duplicate)>=3:
                    duplicate_list.append("'"+duplicate+"'")
                    duplicate_set.add("'"+duplicate+"'")
        f3.write("Suggestion List for "+"'"+username+"'"+" (when MD is "+str(mutuality_degree)+"):\n")
        for dup1 in sorted(duplicate_set):
            f3.write("'"+username+"'"+" has "+str(duplicate_list.count(dup1))+" mutual friends with "+dup1+"\n")
        f3.write("The suggested friends for "+"'"+username+"'"+": "+",".join(sorted(duplicate_set))+"\n")
#Now take command by using if statements.
for command_line in f2:
    command_list=command_line.split()
    if command_list[0]=="ANU":
        ANU(command_list[1])
    if command_list[0]=="DEU":
        DEU(command_list[1])
    if command_list[0]=="ANF":
        ANF(command_list[1],command_list[2])
    if command_list[0]=="DEF":
        DEF(command_list[1],command_list[2])
    if command_list[0]=="CF":
        CF(command_list[1])
    if command_list[0]=="FPF":
        FPF(command_list[1],int(command_list[2]))
    if command_list[0]=="SF":
        SF(command_list[1], int(command_list[2]))
#RUN ON DEV
import random

# author: Jette, Emily

def create_network(file_name):
    '''
    (str)->list of tuples where each tuple has 2 elements (int, list of int) 

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()
    network=[]
    
    users = []
    for i in range(1,len(friends)):
      users = []
    for i in range(1,len(friends)):
        friends[i] = friends[i].split()
        #len(users) must be friends[0], contain no repeats, include every number
        if int(friends[i][0]) not in users:
            users.append(int(friends[i][0]))
        if int(friends[i][1]) not in users:
            users.append(int(friends[i][1]))
    users.sort()
    
    for x in range(len(users)):
        u = user_friends(users[x],friends)
        network.append(u)
         
    return network

def user_friends(user,friends):
    '''
    (list of int, list of str) -> tuple of int and list of int
    function that I created to easily create a tuple 
    '''
    friend_list = []
    for y in range(1,len(friends)):
        if str(user) in str(friends[y]) :    
            if friends[y][0] == str(user) and int(friends[y][0]) not in friend_list:
                friend_list.append(int(friends[y][1]))
            elif friends[y][1] == str(user) and int(friends[y][1]) not in friend_list:
                friend_list.append(int(friends[y][0]))
            friend_list.sort()
    return user,friend_list 
 
def getCommonFriends(user1, user2, network):
    '''
    (int, int, 2D list) ->list
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]
    #find the users in the list and their friends
    u1 = None
    u2 = None
    for i in range(len(network)):
        if network[i][0] == user1:
            u1 = network[i][1]
        if network[i][0] == user2:
            u2 = network[i][1]
   
    for i in u1:
        if i in u2:
            common.append(i)
    common.sort()
    return common
 
def recommend(user, network):
    '''
    (int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID.
    '''

    #find person with MOST friends in common with and if multiple only return the smallest ID number
    user_friends = None
    i = 0
    
    num_in_common = 0
    most = 0 
    u_id = None
    
    while user_friends == None and i < len(network):
        if network[i][0] == user:
            user_friends = network[i][1]
        i += 1
    #print(user_friends) 
    for i in range(len(network)):
        if network[i][0] != user and network[i][0] not in user_friends:
            for j in range(len(network[i][1])):
                if network[i][1][j] in user_friends:
                    num_in_common +=1
            if num_in_common > most:
                u_id = (network[i][0])
                most = num_in_common
            num_in_common = 0 
    return u_id
    pass

def k_or_more_friends(network, k):
    '''
    (2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative
    '''
    
    counter = 0

    for i in range(len(network)):
        if len(network[i][1]) >= k:
            counter +=1
    return counter
    pass
 
def maximum_num_friends(network):
    '''
    (2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
   
    max_num = 0

    for i in network:
        if len(i[1]) > max_num:
            max_num = len(i[1])
    return max_num
    pass

def people_with_most_friends(network):
    '''
    (2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs)
    who have the most friends in network.
    '''
    max_friends=[]
    max_num = maximum_num_friends(network)
    for i in network:
        if len(i[1]) == max_num:
            max_friends.append(i[0])   
    return max_friends

def average_num_friends(network):
    '''
    (2Dlist)->number (int or float)
    Returns an average number of friends overs all users in the network
    '''

    num_of_friends = 0
    for i in network:
        num_of_friends += len(i[1])
    avg = num_of_friends / len(network)
    return avg  
    pass
    
def knows_everyone(network):
    '''
    (2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise
    '''
    
    return maximum_num_friends(network) == len(network)-1
    pass

####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''
    None -> str or None
    '''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''
    ()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name, then returns
    '''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid(network):
    '''
    (2Dlist)->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then returns it
    '''
    
    u_id = None
    user_list = []
    for i in network:
        user_list.append(i[0])
    while u_id == None:
        try:
            u_id = int(input("Enter an integer for a user ID: "))
        except ValueError:
            print("That was not an integer. Please try again.")
            u_id = None
        if u_id not in user_list and u_id != None:
            print("That user ID doe not exist. Please try again.")
            u_id = None
    return u_id
    pass
    

##############################
# main
##############################

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid(net)
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since they are dominating in their connected component")
else:
    print("For user with ID", uid,"we recommend the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinally, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid(net)
print("About 2st user ...")
uid2=get_uid(net)
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    

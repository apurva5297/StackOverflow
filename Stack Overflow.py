import pandas as pd
comment_data=pd.read_excel('comments.xlsx')
post_data=pd.read_excel('post.xlsx')
posttype_data=pd.read_excel('posttypes.xlsx')
users_data=pd.read_excel('users.xlsx')
df1=pd.DataFrame(comment_data)
df2=pd.DataFrame(post_data)
df3=pd.DataFrame(posttype_data)
df4=pd.DataFrame(users_data)
master_data=pd.concat([df1,df2,df3,df4],axis=1).fillna(0)
def probA():
   max_data=df4['REPUTATION'].max()
   name=master_data[master_data['REPUTATION']==max_data]
   print("the display name and no. of posts created by the user who has got maximum reputation:\n\n", name[['NAME','SCORE','REPUTATION']],"\n\n")
   print("--------------------------------------------------------------------------------------------")
   print("\n\n")


def probB():
    avg=df4["AGE"].mean()
    print("the average age of users on the Stack Overflow site: ",avg,"\n\n")
    print("--------------------------------------------------------------------------------------------")
    print("\n\n")


def probC():
   old_data=df2['CREATION DATE'].min()
   name=master_data[master_data['CREATION DATE']==old_data]
   print("the display name of user who posted the oldest post on Stack Overflow (in terms of date): \n\n",name[['NAME', 'CREATION DATE']],"\n\n")
   print("--------------------------------------------------------------------------------------------")
   print("\n\n")


def probD():
   max_data=df4['REPUTATION'].max()
   name=master_data[master_data['REPUTATION']==max_data]
   print("the display name and no. of comments done by the user who has got maximum reputation: \n\n",name[['NAME', 'SCORE', 'REPUTATION']],"\n\n")
   print("--------------------------------------------------------------------------------------------")
   print("\n\n")


def probE():
   max_data=master_data['SCORE'].max()
   name=master_data[master_data['SCORE']==max_data]
   print("the display name of user who has created maximum no. of posts on Stack Overflow: \n\n", name[['NAME', 'SCORE']],"\n\n")
   print("--------------------------------------------------------------------------------------------")
   print("\n\n")


def probF():
    max_data = master_data['VIEW COUNT'].max()
    name= master_data[master_data['VIEW COUNT'] == max_data]
    print("the owner name and id of user whose post has got maximum no. of view counts so far: \n\n",name[['NAME','USER ID','VIEW COUNT']],"\n\n")
    print("--------------------------------------------------------------------------------------------")
    print("\n\n")


def probI():
   max_data=master_data['VIEW COUNT'].max()
   name=master_data[master_data['VIEW COUNT']==max_data]
   print("the location which has maximum no of Stack Overflow users: \n\n",name[['LOC','VIEW COUNT']],"\n\n")
   print("--------------------------------------------------------------------------------------------")
   print("\n\n")


def probJ():
    name = master_data[master_data['LOC'] == 'India']
    total=name['SCORE'].sum()
    print("total no. of posts created by Indian users: ",total,"\n\n")
    print("--------------------------------------------------------------------------------------------")
    print("\n\n")

probA()
probB()
probC()
probD()
probE()
probF()
probI()
probJ()













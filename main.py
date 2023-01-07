from instabot import Bot 
bot=Bot()
bot.login(username="vhgvchgc",password="vhvhc")
bot.follow('andre') # enter the id tou want to follow
bot.upload_photo("photo path",caption="i love python") #for uploading photos
bot.unfollow('ghhghg') #for un follow
bot.send_message("i love python",["username1","username2","username3"]) #for sending message in a group
followers=bot.get_user_followers("username(your)")
for follower in followers:
    print(bot.get_user_info(follower))  #it will give follower list
followings=bot.get_user_following("username(your)")   
for following in followings:
    print(bot.get_user_info(following)) #it will give following list
     
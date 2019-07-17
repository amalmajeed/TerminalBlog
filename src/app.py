from models.blog import Blog
from models.post import Post
from src.menu import Menu
from models.database import Database

Database.initialize()

menu = Menu()

#blog = Blog(author="Amal",title="Amaal's Blog",description="This is a test blog about random shit")
#try:
#    sr = Database.find_one(collection="blogs", query={"title": blog.title})
#    a = sr[0]
#    blog = Blog(author=sr[0]['author'],title=sr[0]['title'],description=sr[0]['description'],id=sr[0]['id'])
#except IndexError:
#    blog.save_to_mongo()

#blog.new_post()

#fromdb = Blog.get_from_mongo(blog.id)
#posts_from_blog=blog.get_posts()

#for i in posts_from_blog :
#    print(i,"\n")
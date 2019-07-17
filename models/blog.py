from models.database import Database
from models.post import Post
import uuid
import datetime

class Blog(object):
    def __init__(self,author,title,description,id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input("Enter the title :")
        content = input("Enter your content here :")
        date = input("Enter post date or leave blank for today (DDMMYYYY): ")
        if date=="":
            date=datetime.datetime.now()
        else:
            date=datetime.datetime.strptime(date,"%d%m%Y")
        p = Post(blog_id=self.id,title=title,author=self.author,content=content,created_date=date)
        p.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs',data=self.json())

    def json(self):
        return {
                "author":self.author,
                "title":self.title,
                "description":self.description,
                "id":self.id
                }

    @classmethod
    def get_from_mongo(cls,id):
        blog_data = Database.find_one(collection="blogs",query={'id':id})
        return cls(author=blog_data[0]['author'],title=blog_data[0]['title'],description=blog_data[0]['description'],id=blog_data[0]['id'])


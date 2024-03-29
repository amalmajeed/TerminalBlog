from models.database import Database
import uuid
import datetime

class Post(object):
    def __init__(self,blog_id,title,author,content,id=None,created_date=datetime.datetime.now()):
        self.title = title
        self.author = author
        self.blog_id = blog_id
        self.id = uuid.uuid4().hex if id is None else id
        self.content = content
        self.created_date = created_date

    def save_to_mongo(self):
        Database.insert(collection='posts',data=self.json())

    def json(self):
        return {'id':self.id,
                'blog_id':self.blog_id,
                'author':self.author,
                'title':self.title,
                'content':self.content,
                'created_date':self.created_date}

    @classmethod
    def from_mongo(cls,id):
        post_data = Database.find_one(collection='posts',query={'id':id})
        return cls(blog_id=post_data['blog_id'],title=post_data['title'],author=post_data['author'],content=post_data['content'])

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
from models.database import Database
from models.post import Post
from models.blog import Blog


class Menu(object):
    def __init__(self):
        self.user = input("Enter Blog App Username : ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome Back {}".format(self.user))
        else:
            self._prompt_new_account()
        self.run_menu()

    def run_menu(self):
        read_or_write=input("Do you want to read/write (r/w) ? :")
        if read_or_write=="r":
            self._list_blogs()
            self._view_blog()
        elif read_or_write=='w':
            self.user_blog.new_post()
        else:
            print("INVALID!")

    def _user_has_account(self):
        try:
            sr = Database.find_one(collection="blogs", query={"author":self.user})
            a=sr[0]
            self.user_blog = Blog.get_from_mongo(sr[0]['id'])
            return True
        except IndexError:
            return False

    def _prompt_new_account(self):
        title = input("Enter a title for your new Blog :")
        description = input("Enter description :")
        blog = Blog(author=self.user,title=title,description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    def _list_blogs(self):
        lis = Database.find(collection='blogs',query={})
        for i in lis:
            print("ID : {}\tTITLE : {}\tDESCRIPTION : {}\tAUTHOR : {}\n".format(i['id'],i['title'],i['description'],i['author']))

    def _view_blog(self):
        text = input("Which Blog do you want to view (id) ? :")
        blog = Blog.get_from_mongo(text)
        lis = blog.get_posts()
        print("\t\t\t\t\t{}\t\tBy Author : {}\t\t\t\n".format(blog.title,blog.author))
        for i in lis:
            print("ID : {}\tTITLE : {}\tCONTENT : {}\tDATE : {}\n".format(i['id'],i['title'],i['content'],i['created_date']))



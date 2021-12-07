from django.test import TestCase
from .models import Image,Profile,Likes,Comments
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        self.user=User(username='Jojo',email='hhhhh2@gmail.com',password='1234')
        self.image=Image(image='food.jpg',name='food',caption='pretty awesome',user=self.user)
        self.comment=Comments(image=self.image,user=self.user,content='yeahh')
        self.like=Likes(image=self.image,user=self.user)
    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))
        self.assertTrue(isinstance(self.image,Image))
        self.assertTrue(isinstance(self.comment,Comments))
        self.assertTrue(isinstance(self.like,Likes))
    def test_save(self):
        self.user.save().save()
        self.image.save().save_image()
        self.comment.save().save_comments()
        self.like.save().save_likes()
        users = User.objects.all()
        images = Image.objects.all()
        comments = Comments.objects.all()
        likes = Likes.objects.all()
        self.assertTrue(len(images) > 0)
        self.assertTrue(len(users) > 0)
        self.assertTrue(len(comments) > 0)
        self.assertTrue(len(likes) > 0)

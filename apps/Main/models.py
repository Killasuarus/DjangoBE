from __future__ import unicode_literals

from django.db import models
from ..logres.models import User
# Create your models here.

class WishlistManager(models.Manager):
    def new(self, postData, user_id):
        errors = []
        modelResponse = {}
        user = User.objects.get(id=user_id)
        if len(postData['itemname']) < 3:
            errors.append('Item must be at least 3 characters!')
        if errors:
            modelResponse['status'] = False
            modelResponse['errors'] = errors
        else:
            new_item = self.create(item = postData['itemname'], user = user)
            curr_user = new_item.user

            new_item.wish.add(curr_user)
            modelResponse['status'] = True
            modelResponse['item'] = new_item
        return modelResponse


    def editlist(self, user_id, item_id):
        curr_user = User.objects.get(id=user_id)
        curr_item = Wishlist.objects.get(id=item_id)
        curr_item.wish.add(curr_user)
        pass



class Wishlist(models.Model):
    item = models.CharField(max_length= 100)
    user = models.ForeignKey(User, related_name='useritems')
    wish = models.ManyToManyField(User, related_name='list_items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = WishlistManager()

# class List(models.Model):
#     item = models.ManyToManyField(Wishlist, related_name='list_items')
#     user = models.ManyToManyField(User, related_name='list_users')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

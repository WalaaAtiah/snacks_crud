from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class test_snack(TestCase):
    def test_snack_list_status(self):
        url = reverse('Snack_List')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_template(self):
        url = reverse('Snack_List')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    def setUp(self):
        self.user=get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='test'
         )
        self.snack=Snack.objects.create (
            title  = 'test',
            purchaser = self.user ,
            description = "description ",
            image ="image"
            )
    def test_str_method(self):
        self.assertEqual(str(self.snack),'test') 

    def test_detail_view(self):
        url = reverse('Snack_Detail',args=[self.snack.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response,'snack_detail.html')  

    def test_create_view_length(self):
    
           data={
               'title':'test',
               'purchaser':self.user.id,
               'description':'description',
               'image':"image"
    
            }
           url = reverse('Snack_Create')
           response= self.client.post(path=url,data=data,follow=True)
           self.assertEqual(len(Snack.objects.all()),2)
         
    def test_create_view_Template(self):
    
           data={
               'title':'test',
               'purchaser':self.user.id,
               'description':'description',
               'image':"image"
    
            }
           url = reverse('Snack_Create')
           response= self.client.post(path=url,data=data,follow=True)
           self.assertTemplateUsed(response,'snack_detail.html')
       
    

    def test_create_view_Redirects(self):
        data={
            "title"  : 'test2',
            "purchaser" : self.user.id ,
            "description" : "description2 ",
            "image" :"image2"
         }
        url = reverse('Snack_Create')
        response= self.client.post(path=url,data=data,follow=True)
        self.assertRedirects(response,reverse('Snack_Detail',args=[2]))

    def test_create_view_Redirects2(self):
        data={
            "title"  : 'test2',
            "purchaser" : self.user.id ,
            "description" : "description2 ",
            "image" :"image2"
         }
        url = reverse('Snack_Create')
        response= self.client.post(path=url,data=data,follow=True)
        response= self.client.post(path=url,data=data,follow=True) # now i have 3 object in the table 
        self.assertRedirects(response,reverse('Snack_Detail',args=[3]))



    def test_Update_view_Template(self):
        data={
            "title"  : 'test2',
            "purchaser" : self.user.id ,
            "description" : "description2 ",
            "image" :"image2"
         }
        url = reverse('Snack_Update',args=[self.snack.id])
        response = self.client.post(path=url,data=data,follow=True)
        self.assertTemplateUsed(response,'snack_detail.html') 

    def test_Update_view_length(self):
    
           data={
               'title':'test',
               'purchaser':self.user.id,
               'description':'description',
               'image':"image"
    
            }
           url = reverse('Snack_Update',args=[self.snack.id])
           response= self.client.post(path=url,data=data,follow=True)
           self.assertEqual(len(Snack.objects.all()),1) 

    def test_create_view_Redirects2(self):
        data={
            "title"  : 'test2',
            "purchaser" : self.user.id ,
            "description" : "description2 ",
            "image" :"image2"
         }
        url = reverse('Snack_Update',args=[self.snack.id])   
        response= self.client.post(path=url,data=data,follow=True)  
        self.assertRedirects(response,reverse('Snack_Detail',args=[1]))
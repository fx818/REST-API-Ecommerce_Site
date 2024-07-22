from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from . import models


class CategoryTestCase(APITestCase):

    def test_getallCategory(self):
        response = self.client.get(reverse('category'))
        return self.assertEqual(response.status_code, status.HTTP_200_OK)

class ProductTestCase(APITestCase):
    
    def setUp(self) -> None:
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.refresh = RefreshToken.for_user(user)
        self.access_token = self.refresh.access_token
        self.prod = models.ProductModel.objects.create(productname='testprod', description='test desc', active=True, price=1299)
        
        
    
    def test_allproducts(self):
        response = self.client.get(reverse('all-product'))
        return self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_product_add(self):
        data = {
            'productname': 'test',
            'price': 100,
            'description': 'test desc',
            'active': True  
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.post(reverse('all-product'), data)
        return self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_prod_put(self):
        data = {
            'productname': 'test-put',
            'price': 100,
            'description': 'test desc',
            'active': True  
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.put(reverse('product-detail', args=(self.prod.id,)), data)
        return self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_prod_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.delete(reverse('product-detail', args=(self.prod.id,)))
        return self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        

class SellerTestCase(APITestCase):
    
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.refresh = RefreshToken.for_user(user)
        self.access_token = self.refresh.access_token
        
        self.seller = models.SellerModel.objects.create(
            sellername = 'testSeller name',
            phone = 9876546789,
            active = False
        )
    
    
    def test_sellerData(self):
        response = self.client.get(reverse('seller-list'))
        return self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_seller_add(self):
        data = {
            'sellername': 'testSeller',
            'phone': 9876546789,
            'active': True
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.post(reverse('seller-list'), data)
        return self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_seller_update(self):
        data = {
            'sellername': 'testSeller',
            'phone': 9876546789,
            'active': True
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.put(reverse('seller-detail', args=(self.seller.id,)), data)
        return self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_seller_delete(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.delete(reverse('seller-detail', args=(self.seller.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        

class ReviewTestCase(APITestCase):
    
    def setUp(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.refresh = RefreshToken.for_user(user)
        self.access_token = self.refresh.access_token
        
        user2 = User.objects.create_user(username='testuser2', password='testpassword')
        self.refresh2 = RefreshToken.for_user(user2)
        self.access_token2 = self.refresh2.access_token
        self.prod = models.ProductModel.objects.create(productname='testprod', description='test desc', active=True, price=1299)
        self.review = models.ReviewModel.objects.create(review_user = user, rating = 5, description='test desc', product = self.prod)
    
    def test_getAllReview(self):
        response = self.client.get(reverse('review-by-prod-id', args=(self.prod.id,)))
        return self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_createReview(self):
        data = {
            'rating': 5,
            'description': 'test review desc'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        
        # response = self.client.post(reverse('review-create', args=(self.prod.id,)), data)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
        response = self.client.post(reverse('review-create', args=(self.prod.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_review_update(self):
        data = {
            'rating': 5,
            'description': 'test review desc'
        }
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token2))
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        self.client.credentials(HTTP_AUTHORIZATION=None)
        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
    def test_review_delete(self):
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token2))
        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))
        response = self.client.delete(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    
    

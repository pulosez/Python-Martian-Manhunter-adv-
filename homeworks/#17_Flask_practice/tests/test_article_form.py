from tests.conftest import client
from io import BytesIO


def test_article_form(client):
    response = client.get('/article/create')
    assert response.status_code == 200

    with open('static/uploads/img1.jpg', 'rb') as img1:
        img_bytes = BytesIO(img1.read())
    data = {
        'title': 'test record',
        'slug': 'test-record',
        'description': 'la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la la',
        'short_description': 'la la la la la la la',
        'img': (img_bytes, 'img1.jpg')
    }

    response = client.post('/article/store', content_type='multipart/form-data', data=data)
    assert response.status_code == 302

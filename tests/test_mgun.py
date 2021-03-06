import pytest
import json


class TestUrlBuilder:
    def test_url(self, client):
        assert client.__str__() == 'https://httpbin.org'

    def test_simple_url(self, client):
        assert client.api.__str__() == 'https://httpbin.org/api'

    def test_parameter_url(self, client):
        assert client.api.users[34].first.__str__() == 'https://httpbin.org/api/users/34/first'

    def test_str_parameters_url(self, client):
        assert client['api'].users['f3d4a'].first.__str__() == 'https://httpbin.org/api/users/f3d4a/first'


class TestHttpRequests:
    @pytest.mark.asyncio
    async def test_get(self, client):
        response = await client.get_.get()
        assert response.status == 200

    @pytest.mark.asyncio
    async def test_delete(self, client):
        response = await client.delete_.delete()
        assert response.status == 200

    @pytest.mark.asyncio
    async def test_get_with_data(self, client):
        data = {'q': '1'}
        response = await client.get_.get(data)
        assert response.status == 200
        assert response.data['args'] == data

    @pytest.mark.asyncio
    async def test_post(self, client):
        data = {'data': [1, 2, 3]}
        response = await client.post_.post(data)
        assert response.status == 200
        assert json.loads(response.data['data']) == data
        print(response)

    @pytest.mark.asyncio
    async def test_put(self, client):
        data = {'data': [1, 2, 3]}
        response = await client.put_.put(data)
        assert response.status == 200
        assert json.loads(response.data['data']) == data
        print(response)

    @pytest.mark.asyncio
    async def test_patch(self, client):
        data = {'data': [1, 2, 3]}
        response = await client.patch_.patch(data)
        assert response.status == 200
        assert json.loads(response.data['data']) == data
        print(response)

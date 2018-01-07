import pytest


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

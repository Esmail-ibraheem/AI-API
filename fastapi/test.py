import unittest
from fastapi.testclient import TestClient
from API import app  # Replace with the actual name of the file where your FastAPI app is defined
from jose import jwt
from datetime import timedelta

class TestFastAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)
        cls.username = "bob"
        cls.password = "mypassword"
        cls.secret_key = "your-secret-key"
        cls.algorithm = "HS256"
        cls.token_expiry = timedelta(minutes=30)

    def get_token(self):
        response = self.client.post(
            "/token",
            data={"username": self.username, "password": self.password}
        )
        self.assertEqual(response.status_code, 200)
        token = response.json()["access_token"]
        return token

    def test_token_authentication(self):
        # Test login and token generation
        response = self.client.post(
            "/token",
            data={"username": self.username, "password": self.password}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("access_token", response.json())

    # def test_generate_image(self):
    #     # Generate token
    #     token = self.get_token()

    #     # Test image generation
    #     headers = {"Authorization": f"Bearer {token}"}
    #     response = self.client.post(
    #         "/generate_image",
    #         headers=headers,
    #         json={
    #             "prompt": "A futuristic city skyline",
    #             "cfg_scale": 7.5,
    #             "num_inference_steps": 50,
    #             "sampler": "euler"
    #         }
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("image", response.json())

    # def test_chat_with_ollama(self):
    #     # Generate token
    #     token = self.get_token()

    #     # Test chat with ollama
    #     headers = {"Authorization": f"Bearer {token}"}
    #     response = self.client.post(
    #         "/chat_with_ollama",
    #         headers=headers,
    #         json={"model_name": "aya", "prompt": "Describe a futuristic city."}
    #     )
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn("response", response.json())

    def test_apply_blueprint(self):
        # Generate token
        token = self.get_token()

        # Test applying a blueprint
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.post(
            "/apply_blueprint",
            headers=headers,
            json={"blueprint_name": "Visual Story"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("sd_prompt", response.json())
        self.assertIn("ollama_prompt", response.json())

    def test_tokenize(self):
        # Generate token
        token = self.get_token()

        # Test tokenization
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.post(
            "/tokenize",
            headers=headers,
            json={"text": "Hello, world!"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("tokens", response.json())

    def test_chatbot_arabic(self):
        # Generate token
        token = self.get_token()

        # Test chatbot Arabic
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.post(
            "/chatbot_arabic",
            headers=headers,
            json={"question": "ما هو أفضل مكان للسفر؟"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("response", response.json())

if __name__ == "__main__":
    unittest.main()

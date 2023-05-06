import json
import unittest
from app import app

class TestIdeaGenerator(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_generate_ideas(self):
        # Create sample input data
        data = {
            "category": "technology"
        }

        # Send a POST request to the /generate route
        response = self.app.post(
            "/generate",
            data=json.dumps(data),
            content_type="application/json",
        )

        # Check if the status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the response contains 'ideas'
        json_response = json.loads(response.data)
        self.assertIn("ideas", json_response)

if __name__ == "__main__":
    unittest.main()

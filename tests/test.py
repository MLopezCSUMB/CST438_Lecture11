import unittest 
import functions

class ChatBotTest(unittest.TestCase):
    def test_add_command(self):
        response = functions.get_chatbot_response('!! add 4 5')
        self.assertEqual(response, '45')

if __name__ == '__main__':
    unittest.main()
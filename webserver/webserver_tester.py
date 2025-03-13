from email.policy import HTTP
from http.server import BaseHTTPRequestHandler, HTTPServer
from unittest.mock import MagicMock, patch
from urllib.parse import urlparse
import requests
import unittest
from webserver import Machine, User, MachineManager, RequestHandler

class TestMachine(unittest.TestCase):

    @patch('serial.Serial')
    def test_init(self, mock_serial):
        machine_id = 'lab_0'
        com_num = 'COM1'
        machine = Machine(machine_id)
        self.assertEqual(machine.machine_id, machine_id)
        self.assertIsNone(machine.assigned_user)
        self.assertEqual(machine.baudrate, 9600)

    @patch('serial.Serial')
    def test_press_button(self, mock_serial):
        machine_id = 'lab_0'
        machine = Machine(machine_id)
        mock_obj = MagicMock()
        mock_serial.return_value.__enter__.return_value = mock_obj
        machine.press_button()
        mock_obj.write.assert_called_once_with(b'press')

    @patch('serial.Serial')
    def test_repress_button(self, mock_serial):
        machine_id = 'lab_0'
        machine = Machine(machine_id)
        mock_obj = MagicMock()
        mock_serial.return_value.__enter__.return_value = mock_obj
        machine.repress_button()
        mock_obj.write.assert_called_once_with(b'repress')

    # TODO: tests to handle multiple presses

class TestUser(unittest.TestCase):
    def test_init(self):
        user = User('abc123')
        self.assertEqual(user.user_id, 'abc123')
        self.assertIsNone(user.assigned_machine)

class TestMachineManager(unittest.TestCase):
    def test_init(self):
        machine_manager = MachineManager()
        self.assertEqual(len(machine_manager.available_machines), 5)
        self.assertEqual(len(machine_manager.inuse_machines), 0)
        self.assertEqual(len(machine_manager.users), 0)

    def test_assign_user_to_machine(self):
        machine_manager = MachineManager()
        machine = machine_manager.assign_user_to_machine('abc123')
        self.assertIsNotNone(machine)
        self.assertEqual(len(machine_manager.available_machines), 4)
        self.assertEqual(len(machine_manager.inuse_machines), 1)
        self.assertEqual(len(machine_manager.users), 1)

    def test_release_machine(self):
        machine_manager = MachineManager()
        _ = machine_manager.assign_user_to_machine('abc123')
        self.assertTrue(machine_manager.release_machine('abc123'))
        self.assertEqual(len(machine_manager.available_machines), 5)
        self.assertEqual(len(machine_manager.inuse_machines), 0)
        self.assertEqual(len(machine_manager.users), 0)

    def test_get_machine_for_user(self):
        machine_manager = MachineManager()
        machine = machine_manager.assign_user_to_machine('abc123')
        self.assertEqual(machine_manager.get_machine_for_user('abc123'), machine)

    def test_assign_two_users_to_machines(self):
        machine_manager = MachineManager()
        machine_one = machine_manager.assign_user_to_machine('abc123')
        machine_two = machine_manager.assign_user_to_machine('xyz789')
        self.assertIsNotNone(machine_one)
        self.assertIsNotNone(machine_two)
        self.assertEqual(len(machine_manager.available_machines), 3)
        self.assertEqual(len(machine_manager.inuse_machines), 2)
        self.assertEqual(len(machine_manager.users), 2)

    def test_release_two_users_machines(self):
        machine_manager = MachineManager()
        _ = machine_manager.assign_user_to_machine('abc123')
        _ = machine_manager.assign_user_to_machine('xyz789')
        self.assertTrue(machine_manager.release_machine('abc123'))
        self.assertTrue(machine_manager.release_machine('xyz789'))
        self.assertEqual(len(machine_manager.available_machines), 5)
        self.assertEqual(len(machine_manager.inuse_machines), 0)
        self.assertEqual(len(machine_manager.users), 0)


    def test_assign_users_machines(self):
        machine_manager = MachineManager()
        for i in range(1, 5):
            machine = machine_manager.assign_user_to_machine(f'user_{i}')
            self.assertIsNotNone(machine)
            self.assertEqual(len(machine_manager.available_machines), 5-i)
            self.assertEqual(len(machine_manager.inuse_machines), i)
            self.assertEqual(len(machine_manager.users), i)

    def test_release_users_machines(self):
        machine_manager = MachineManager()
        for i in range(5):
            _ = machine_manager.assign_user_to_machine(f'user_{i}')
        for i in range(1, 5):
            self.assertTrue(machine_manager.release_machine(f'user_{i}'))
            self.assertEqual(len(machine_manager.available_machines), i)
            self.assertEqual(len(machine_manager.inuse_machines), 5-i)
            self.assertEqual(len(machine_manager.users), 5-i)

# TODO: this isn't tested at all / correctly but i'm also not sure how to...
class TestRequestHandler(unittest.TestCase):

    def setUp(self):
        server_address = ('', 9090)
        self.server = HTTPServer(server_address, RequestHandler)
        self.server.allow_reuse_address = True

    def tearDown(self):
        self.server.server_close()

    def test_do_GET(self):
        self.path = '/abc123/press'





if __name__ == "__main__":
    unittest.main()

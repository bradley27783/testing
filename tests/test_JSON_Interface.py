import unittest

from JSON_Interface import JSON_Interface
class TestSearchForValue(unittest.TestCase):
    def test_base_find(self):
        test_json = {
            'POS 1': {
                "ip": "172.168.1.1",
                "mac": "40:11",
                "vhpos": {
                    "vhpos_ip": "192.168.1.1",
                    "mac": "a0:11"
                }
            },
            'POS 2': {
                "ip": "172.168.1.2",
                "mac": "40:11",
                "vhpos": {
                    "vhpos_ip": "192.168.1.2",
                    "mac": "a0:11"
                }
            }
        }
        ji = JSON_Interface(test_json)
        val = ji.find(['ip'])
        assert ['172.168.1.1', '172.168.1.2'] == val

    def test_nested_find(self):
        test_json = {
            'POS 1': {
                "ip": "172.168.1.1",
                "mac": "40:11",
                "vhpos": {
                    "vhpos_ip": "192.168.1.1",
                    "mac": "a0:11"
                }
            },
            'POS 2': {
                "ip": "172.168.1.2",
                "mac": "40:11",
                "vhpos": {
                    "vhpos_ip": "192.168.1.2",
                    "mac": "a0:11"
                }
            }
        }
        ji = JSON_Interface(test_json)
        val = ji.find(['vhpos_ip'])
        assert ['192.168.1.1', '192.168.1.2'] == val


    def test_get_particular_object(self):
        test_json = {
            'POS 1': {
                "ip": "172.168.1.1",
                "mac": "40:11",
                "vhpos": {
                    "vhpos_ip": "192.168.1.1",
                    "mac": "a0:11"
                }
            },
            'POS 2': {
                "ip": "172.168.1.2",
                "mac": "40:11",
                "vhpos": {
                    "vhpos_ip": "192.168.1.2",
                    "mac": "a0:11"
                }
            }
        }
        ji = JSON_Interface(test_json)
        val = ji.find(['POS 1'])
        assert val == [{"ip": "172.168.1.1", "mac": "40:11", "vhpos": {"vhpos_ip": "192.168.1.1","mac": "a0:11"}}]


    def test_get_particular_value(self):
        test_json = {
            'POS 1': {
                "ip": "172.168.1.1",
                "mac": "40:11",
                "vhpos": {
                    "vhpos_ip": "192.168.1.1",
                    "mac": "a0:11"
                }
            },
            'POS 2': {
                "ip": "172.168.1.2",
                "mac": "40:11",
                "vhpos": {
                    "vhpos_ip": "192.168.1.2",
                    "mac": "a0:11"
                }
            }
        }
        ji = JSON_Interface(test_json)
        val = ji.find(['POS 1', 'vhpos_ip'])
        assert val == ['192.168.1.1']

if __name__ == '__main__':
    unittest.main()
import unittest
from ibra_os.agents.secretary import SecretaryAgent
from ibra_os.database.db_manager import init_db
import os
import sqlite3

class TestIbraOS(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_db = "tests/test_garage_memory.db"
        init_db(cls.test_db)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.test_db):
            os.remove(cls.test_db)

    def test_secretary_dispatch(self):
        secretary = SecretaryAgent()
        # Test vision dispatch
        res = secretary.process("Peux-tu regarder cette image de frein?")
        self.assertEqual(res['target'], "Vision")

        # Test memory dispatch
        res = secretary.process("Quels sont les rendez-vous de demain?")
        self.assertEqual(res['target'], "Memory")

    def test_database_schema(self):
        self.assertTrue(os.path.exists(self.test_db))

        conn = sqlite3.connect(self.test_db)
        cursor = conn.cursor()

        # Check tables exist
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cursor.fetchall()]
        self.assertIn('clients', tables)
        self.assertIn('appointments', tables)
        self.assertIn('part_orders', tables)

        conn.close()

if __name__ == "__main__":
    unittest.main()

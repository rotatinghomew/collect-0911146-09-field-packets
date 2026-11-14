import tempfile
import unittest
from fixtures import sample_packet
from packet import unpack
from packet_preview import preview
from forms import map_fields
from register import register_rows
from assignment import verify_assignment


class PacketTests(unittest.TestCase):
    def test_missing_photo_is_not_ready(self):
        self.assertEqual(unpack(sample_packet(with_photo=False))['attachments'][0]['state'], 'missing')
        self.assertEqual(unpack(sample_packet())['attachments'][0]['state'], 'ready')

    def test_schema_mapping_preserves_unknown(self):
        result = map_fields('v1', {'memo': '现场', 'new_field': 'retain'})
        self.assertEqual(result['fields']['note'], '现场')
        self.assertEqual(result['unknown'], {'new_field': 'retain'})

    def test_preview_exposes_parallel_parents(self):
        with tempfile.TemporaryDirectory() as directory:
            first = preview(sample_packet('a'), directory)['records'][0]
            second = preview(sample_packet('b'), directory)['records'][0]
            self.assertEqual(first['parents'], second['parents'])
            self.assertNotEqual(first['version'], second['version'])
            self.assertEqual(second['mapping']['note'], 'note')

    def test_unsigned_device_and_unproven_acceptance(self):
        record = unpack(sample_packet())['records'][0]
        record['device'] = 'unissued'
        with self.assertRaises(ValueError):
            verify_assignment(record)
        with self.assertRaises(ValueError):
            register_rows([{'state': 'accepted'}])

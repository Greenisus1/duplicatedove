import tempfile,unittest
from pathlib import Path
import duplicatedove as r
class RepeatTests(unittest.TestCase):
    def test_empty(self):self.assertEqual(r.analyze(b'')['lines'],0)
    def test_unique(self):self.assertEqual(r.analyze(b'a\nb')['unique_lines'],2)
    def test_duplicate(self):self.assertEqual(r.analyze(b'a\nb\na')['duplicate_groups'],[{'count':2,'line_numbers':[1,3]}])
    def test_excess(self):self.assertEqual(r.analyze(b'a\na\na')['repeated_occurrences_beyond_first'],2)
    def test_no_text(self):self.assertNotIn('secret',str(r.analyze(b'secret\nsecret')))
    def test_no_hash(self):self.assertNotIn('hash',r.analyze(b'a\na'))
    def test_case(self):self.assertEqual(r.analyze(b'a\nA')['unique_lines'],2)
    def test_spaces(self):self.assertEqual(r.analyze(b'a\na ')['unique_lines'],2)
    def test_endings(self):self.assertEqual(r.analyze(b'a\r\na\ra\n')['unique_lines'],1)
    def test_blank(self):self.assertEqual(r.analyze(b'\n\n')['duplicate_groups'][0]['line_numbers'],[1,2])
    def test_unicode(self):self.assertEqual(r.analyze('é\né'.encode())['unique_lines'],1)
    def test_bom(self):self.assertEqual(r.analyze(b'\xef\xbb\xbfa\na')['unique_lines'],2)
    def test_separator(self):self.assertEqual(r.analyze('a\u2028a'.encode())['lines'],1)
    def test_invalid_utf8(self):
        with self.assertRaises(UnicodeError):r.analyze(b'\xff')
    def test_limit(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'x';p.write_bytes(b'x'*(r.MAX+1))
            with self.assertRaises(ValueError):r.inspect(p)
    def test_order(self):self.assertEqual([x['line_numbers'][0] for x in r.analyze(b'b\na\na\nb')['duplicate_groups']],[1,2])
if __name__=='__main__':unittest.main()

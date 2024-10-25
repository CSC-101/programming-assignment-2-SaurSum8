import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        p1 = data.Point(2,2)
        p2 = data.Point(10,10)
        rect = data.Rectangle(data.Point(2, 10), data.Point(10, 2))
        self.assertEqual(rect, hw2.create_rectangle(p1, p2))

    def test_create_rectangle_2(self):
        p1 = data.Point(-5,6)
        p2 = data.Point(-6,5)
        rect = data.Rectangle(data.Point(-6, 6), data.Point(-5, 5))
        self.assertEqual(rect, hw2.create_rectangle(p1, p2))

    # Part 2
    def test_shorter_duration_than_1(self):
        x = data.Duration(10, 20)
        y = data.Duration(10, 29)
        self.assertEqual(True, hw2.shorter_duration_than(x, y))

    def test_shorter_duration_than_2(self):
        x = data.Duration(0, 0)
        y = data.Duration(0, 0)
        self.assertEqual(False, hw2.shorter_duration_than(x, y))

    # Part 3
    def test_songs_shorter_than_1(self):
        D = data.Song("Decemberists", "June Hymn", data.Duration(4, 30))
        B = data.Song("Broken Bells", "October", data.Duration(3, 40))
        K = data.Song("Kansas", "Dust in the Wind", data.Duration(3, 29))
        L = data.Song("Local Natives", "Airplanes", data.Duration(3, 58))

        l = [D, B, K, L]
        self.assertEqual(l, hw2.songs_shorter_than(l, data.Duration(5,00)))

    def test_songs_shorter_than_2(self):
        D = data.Song("Decemberists", "June Hymn", data.Duration(4, 30))
        B = data.Song("Broken Bells", "October", data.Duration(3, 40))
        K = data.Song("Kansas", "Dust in the Wind", data.Duration(3, 29))
        L = data.Song("Local Natives", "Airplanes", data.Duration(3, 58))

        l = [D, B, K, L]
        m = [B, K]
        self.assertEqual(m, hw2.songs_shorter_than(l, data.Duration(3,58)))

    # Part 4
    def test_running_time_1(self):
        D = data.Song("Decemberists", "June Hymn", data.Duration(4, 30))
        B = data.Song("Broken Bells", "October", data.Duration(3, 40))
        K = data.Song("Kansas", "Dust in the Wind", data.Duration(3, 29))
        L = data.Song("Local Natives", "Airplanes", data.Duration(3, 58))

        l = [D, B, K, L]
        t = [0, 2, 1, 3, 0]

        self.assertEqual(data.Duration(20,7), hw2.running_time(l, t))

    def test_running_time_2(self):
        D = data.Song("Decemberists", "June Hymn", data.Duration(4, 30))
        B = data.Song("Broken Bells", "October", data.Duration(3, 40))
        K = data.Song("Kansas", "Dust in the Wind", data.Duration(3, 29))
        L = data.Song("Local Natives", "Airplanes", data.Duration(3, 58))

        l = [D, B, K, L]
        t = [0, 2, 1, 1, -1]

        self.assertEqual(data.Duration(15,19), hw2.running_time(l, t))

    # Part 5
    def test_validate_route_1(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]

        t = ['san luis obispo', 'santa margarita', 'atascadero']

        self.assertEqual(True, hw2.validate_route(city_links, t))

    def test_validate_route_2(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston']
        ]

        t = []

        self.assertEqual(True, hw2.validate_route(city_links, t))

    def test_validate_route_3(self):
        city_links = [
            ['san luis obispo', 'santa margarita'],
            ['san luis obispo', 'pismo beach'],
            ['atascadero', 'santa margarita'],
            ['atascadero', 'creston'],
            ['san jose', 'san francisco']
        ]

        t = ['san luis obispo', 'santa margarita', 'atascadero', 'san francisco']

        self.assertEqual(False, hw2.validate_route(city_links, t))

    # Part 6
    def test_longest_repetition_1(self):
        l = [1, 1, 2, 2, 1, 1, 1, 3]
        self.assertEqual(4, hw2.longest_repetition(l))

    def test_longest_repetition_2(self):
        l = [1, 1, 2, 2, 1, 1, 1, 3, 3, 3, 3, 3]
        self.assertEqual(7, hw2.longest_repetition(l))

    def test_longest_repetition_3(self):
        l = [1, 2, 3, 4, 5]
        self.assertEqual(None, hw2.longest_repetition(l))

if __name__ == '__main__':
    unittest.main()

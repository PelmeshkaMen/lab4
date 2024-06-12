import unittest
from the_volume_of_the_shapes import calculate_volume
from the_volume_of_the_shapes import error_precision

class FlaskTest(unittest.TestCase):
    #def setUp(self):
    #    self.app = app.test_client()
    
    def test_cube_volume(self):
        params = {'side_length': '3'}
        precision = 2
        volume = calculate_volume('cube', params, precision)
        self.assertEqual(volume, 27.0)
    
    def test_sphere_volume(self):
        params = {'radius': '2'}
        precision = 2
        volume = calculate_volume('sphere', params, precision)
        self.assertAlmostEqual(volume, 33.51, places=2)
    
    def test_cylinder_volume(self):
        params = {'radius_с': '2', 'height': '4'}
        precision = 2
        volume = calculate_volume('cylinder', params, precision)
        self.assertAlmostEqual(volume, 50.27, places=2)
    
    def test_invalid_shape(self):
        params = {'side_length': '3'}
        precision = 2
        volume = calculate_volume('invalid_shape', params, precision)
        self.assertIsNone(volume)

    def test_cube_volume_none_precision(self):
        params = {'side_length': '3'}
        precision = None
        volume = calculate_volume('cube', params, precision)
        self.assertEqual(volume, 27.0)
    
    def test_sphere_volume_none_precision(self):
        params = {'radius': '2'}
        precision = None
        volume = calculate_volume('sphere', params, precision)
        self.assertAlmostEqual(volume, 34, places=2) # при незаданном precision, precision = 1 volume = 34
    
    def test_cylinder_volume_none_precision(self):
        params = {'radius_с': '2', 'height': '4'}
        precision = None
        volume = calculate_volume('cylinder', params, precision)
        self.assertAlmostEqual(volume, 50, places=2) # при незаданном precision, precision = 1 volume = 50

    def test_cube_volume_none_params(self):
        params = {'side_length':''}
        precision = 2
        volume = calculate_volume('cube', params, precision)
        self.assertEqual(volume, "Ошибка вычисления. Введите длину стороны куба!")
    
    def test_sphere_volume_none_params(self):
        params = {'radius': ''}
        precision = 2
        volume = calculate_volume('sphere', params, precision)
        self.assertAlmostEqual(volume, "Ошибка вычисления. Введите радиус сферы!", places=2)
    
    def test_cylinder_volume_none_params(self):
        params = {'radius_с': '', 'height': ''}
        precision = 2
        volume = calculate_volume('cylinder', params, precision)
        self.assertAlmostEqual(volume, "Ошибка вычисления. Введите значения радиуса и высоты цилиндра!", places=2)

    def test_cube_volume_otrits_precision(self):
        params = {'side_length':'3'}
        precision = -2
        error = error_precision(precision)
        self.assertEqual(error, 1)

    def test_sphere_volume_otrits_precision(self):
        params = {'radius': '2'}
        precision = -2
        error = error_precision(precision)
        self.assertAlmostEqual(error, 1, places=2)
    
    def test_cylinder_volume_otrits_precision(self):
        params = {'radius_с': '2', 'height': '4'}
        precision = -2
        error = error_precision(precision)
        self.assertAlmostEqual(error, 1, places=2)

    def test_cube_volume_otrits_params(self):
        params = {'side_length':'-3'}
        precision = 2
        volume = calculate_volume('cube', params, precision)
        self.assertEqual(volume, "Ошибка вычисления. Длина стороны не может быть отрицательным!")

    def test_sphere_volume_otrits_params(self):
        params = {'radius': '-2'}
        precision = 2
        volume = calculate_volume('sphere', params, precision)
        self.assertAlmostEqual(volume, "Ошибка вычисления. Радиус не может быть отрицательным!", places=2)
    
    def test_cylinder_volume_otrits_params(self):
        params = {'radius_с': '-2', 'height': '-4'}
        precision = 2
        volume = calculate_volume('cylinder', params, precision)
        self.assertAlmostEqual(volume, "Ошибка вычисления. Радиус и высота не могут быть отрицательными!", places=2)
    

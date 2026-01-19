import pytest

from source import shapes


@pytest.mark.parametrize("side_length, expected_area", [(5,25), (1,1), (3, 9), (4, 16)])
def test_multiple_square_areas(side_length, expected_area):
    assert shapes.Square(side_length).area() == expected_area

@pytest.mark.parametrize("side_length, expected_perimeter", [(5,20), (1,4), (3, 12), (4, 16)])
def test_multiple_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter
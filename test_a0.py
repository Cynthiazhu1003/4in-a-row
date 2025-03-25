"""CSC148 Assignment 0

=== CSC148 Winter 2024 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jonathan Calver and Sophia Huynh

All of the files in this directory and all subdirectories are:
Copyright (c) Jonathan Calver, Diane Horton, and Sophia Huynh.

=== Module Description ===

This file contains some provided tests for the assignment and is where
you will write additional tests.

To run the tests in this file, right-click here and select the option
that says "Run 'Python tests in test...'"

Note: We will not run pyTA on this file when grading your assignment.

"""
from __future__ import annotations

from four_in_a_row import *
from a0 import *


# TODO add tests for each method and function as indicated in the assignment
#      Note: we have scaffolded some code below for you to add your tests into.
#      Make sure each test has a unique name and that each test starts
#      with test_
#      The tests below are organized into classes to help keep related tests
#      grouped together. In PyCharm you can choose to run all tests in a single
#      class by using the run button beside the class name (just like how you
#      can choose to run a single test). Alternatively, you can run all tests
#      in the file by right-clicking the file name and choosing to run tests.

class TestHelpers:
    """
    These are provided tests related to Task 1, which are meant to remind you
    of the structure of a pytest for later tasks. For Task 1, you are asked
    to write doctests instead.

    While not required, you are welcome to add other pytests here as you
    develop your code.
    """

    def test_within_grid_in_grid(self):
        """Test that (0, 0) is inside a 4-by-4 grid."""
        assert within_grid((0, 0), 4)

    def test_within_grid_outside_grid(self):
        """Test that (4, 4) is outside a 4-by-4 grid."""
        assert not within_grid((4, 4), 4)

    def test_all_within_grid_all_in_grid(self):
        """Test when the four coordinates are all within a 4-by-4 grid."""
        assert all_within_grid([(0, 0), (1, 1), (2, 2), (3, 3)], 4)

    def test_reflect_vertically_above(self):
        """Test reflecting vertically for a coordinate above the middle."""
        assert reflect_vertically((0, 1), 5) == (4, 1)

    def test_reflect_vertically_middle(self):
        """Test reflecting vertically for a coordinate on the middle row."""
        assert reflect_vertically((2, 1), 5) == (2, 1)

    def test_reflect_points(self):
        """Test reflecting a very short line"""
        assert reflect_points([(0, 1), (1, 2)], 5) == [(4, 1), (3, 2)]


class TestLine:
    """
    TODO Task 2: add tests for the Line methods and related functions
                 You must write two tests for each of:
                   - is_row, is_column, and is_diagonal
                   - Line.drop, Line.is_full, and Line.has_fiar
    """

    def test_is_row(self):
        """Test Class Square is a valid row. As it satisfies the conditions
         being a valid row. """
        line = [Square((1, 1)), Square((1, 2)), Square((1, 3)), Square((1, 4))]
        assert is_row(line) is True

    def test_is_not_row(self):
        """Test Class Square is not a valid row
        because their columns are not the same."""
        line = [Square((1, 1)), Square((2, 2)), Square((3, 3)), Square((4, 4))]
        assert is_row(line) is False

    def test_is_not_anything(self):
        """Test Class Square is not a valid row, column, and diagonal."""
        # with pytest.raises(AssertionError):
        line = [Square((1, 3)), Square((2, 1)), Square((2, 3)), Square((4, 1))]
        assert is_row(line) is False
        assert is_column(line) is False
        assert is_diagonal(line) is False

    def test_is_column(self):
        """Test Class Square is a valid column. As it satisfies the conditions
         being a valid column. """
        line = [Square((1, 2)), Square((2, 2)), Square((3, 2)), Square((4, 2))]
        assert is_column(line) is True

    def test_is_not_column(self):
        """Test Class Square is a not a valid column. Because the row
        coordinates all increase by -1 not by 1 from the previous square """
        line = [Square((4, 2)), Square((3, 2)), Square((2, 2)), Square((1, 2))]
        assert is_column(line) is False

    def test_is_down_diagonal(self):
        """Test list of instances squares is a valid down diagonal"""
        line = [Square((0, 2)), Square((1, 3)), Square((2, 4)), Square((3, 5))]
        assert is_diagonal(line) is True

    def test_is_up_diagonal(self):
        """Test list of instances squares is a valid up diagonal"""
        line = [Square((4, 1)), Square((3, 2)), Square((2, 3)), Square((1, 4))]
        assert is_diagonal(line) is True

    def test_is_not_diagonal(self):
        """Test list of instances squares is not a valid diagonal"""
        line = [Square((0, 2)), Square((2, 4)), Square((4, 3)), Square((3, 1))]
        assert is_diagonal(line) is False

    def test_line_drop_non_empty_column(self):
        """Test if the item is dropped correctly on a non_empty column"""
        l = Line([Square((0, 1)), Square((1, 1)),
                  Square((2, 1)), Square((3, 1))])
        row_coord = l.drop('X')
        assert row_coord == 3
        assert l[row_coord].symbol == 'X'

    def test_line_drop_empty_column(self):
        """Test if the item is dropped correctly"""
        l = Line([Square((0, 0)), Square((1, 0)),
                  Square((2, 0)), Square((3, 0)), Square((4, 0))])
        row_coord = l.drop('O')
        assert row_coord == 4
        assert l[row_coord].symbol == 'O'

    def test_line_is_not_completely_full(self):
        """Test if the line is not completely full"""
        l = Line([Square((0, 1)), Square((1, 1)),
                  Square((2, 1), 'X'), Square((3, 1), 'X')])
        assert l.is_full() is False

    def test_line_column_is_full(self):
        """Test if the column line is full"""
        line = Line([Square((0, 1), 'X'), Square((1, 1), 'X'),
                     Square((2, 1), 'X'), Square((3, 1), 'X')])
        assert line.is_full() is True

    def test_line_another_column_is_full(self):
        """Test if the column line is full"""
        line = Line([Square((1, 2), 'X'), Square((2, 2), 'X'),
                     Square((3, 2), 'X'), Square((4, 2), 'X')])
        assert line.is_full() is True

    def test_line_has_no_fiar(self):
        """Test the line contains a four-in-a-row that do not pass through
        the given <coord>"""
        line = Line([Square((0, 1), 'X'), Square((0, 2)),
                     Square((0, 3)), Square((0, 4))])
        assert line.has_fiar((0, 2)) is False

    def test_line_has_fiar(self):
        """Test the line contains a four-in-a-row that does pass through
        the given <coord>"""

        line = Line([Square((0, 1), 'X'), Square((0, 2), 'X'),
                 Square((0, 3), 'X'), Square((0, 4), 'X')])
        assert line.has_fiar((0, 1)) is True


class TestGrid:
    """
    TODO Task 3.1: add tests for the Grid methods and related functions
                 You must write two tests for each of:
                   - Grid.drop, Grid.is_full
                   - create_rows_and_columns

    TODO Task 3.2: add tests for the Grid methods and related functions
                 You must write two tests for each of:
                   - Grid.has_fiar
                   - create_mapping
    """

    def test_grip_drop(self):
        """Test grid will land on the corresponding row"""
        g = Grid(4)
        col = 0
        item = 'X'
        g.drop(col, item)
        assert g.drop(col, item) == 2

    def test_grip_several_drop(self):
        """Test grid will land on the corresponding row after several drops."""
        g = Grid(4)
        col = 0
        item = 'X'
        g.drop(col, item)
        g.drop(col, item)
        g.drop(col, item)
        assert g.drop(col, item) == 0

    def test_grid_has_no_fiar(self):
        """Test if the grid has no four-in-a-row."""
        g = Grid(4)
        coord = (0, 0)
        assert g.has_fiar(coord) is False

    def test_grid_has_fiar(self):
        """Test if a grid has fiar."""
        g = Grid(5)
        coord = [4, 4]
        for _ in range(5):  # make a four-in-a-row
            g.drop(4, 'X')
        assert g.has_fiar((4, 4)) is True

    def test_create_rows_and_columns_six_by_six(self):
        """Test if rows and columns are created based on given squares
        with same index of columns and rows"""
        squares = create_squares(6)
        rows, columns = create_rows_and_columns(squares)
        assert columns[5][5] == rows[5][5]
        assert columns[5][5] == squares[5][5]

    def test_create_rows_and_columns_five_by_five(self):
        """Test if rows and columns are created based on given squares"""
        squares = create_squares(5)
        rows, columns = create_rows_and_columns(squares)
        assert rows[0][1] is columns[1][0]
        assert rows[0][0] is squares[0][0]

    def test_create_mapping(self):
        """Test if mapping is that coordinate is the initial square (0, 0). """
        squares = create_squares(5)
        mapping = create_mapping(squares)
        lines = mapping[(0, 0)]
        assert len(lines) == 3
        assert is_row(lines[0].cells) is True
        assert is_column(lines[1].cells) is True
        assert is_diagonal(lines[2].cells) is True

    def test_create_another_mapping(self):
        """Test if mapping is that coordinate is the square in the middle. """
        squares = create_squares(5)
        mapping = create_mapping(squares)
        lines = mapping[(2, 2)]
        assert len(lines) == 4
        assert is_row(lines[0].cells) is True
        assert is_column(lines[1].cells) is True
        assert is_diagonal(lines[2].cells) is True

    def test_grid_is_empty(self):
        """Test method Grid.is_full when grid is empty """
        g = Grid(4)
        result = g.is_full()
        assert result is False

    def test_grid_is_partial_full(self):
        g = Grid(4)
        for c in range(4 - 1):
            for r in range(4):
                rslt = g.drop(c, 'X')
        assert g.is_full() is False


class TestFourInARow:
    """
    TODO TASK 4:
     - run check_coverage.py to get the code coverage report.
     - Using the code coverage report, identify which branches of the code
       are not currently being tested.
     - add tests below in order to achieve 100% code coverage when you run
       check_coverage.py. Your tests should follow a similar structure
       to the test_x_wins test defined below.
    """

    def test_x_wins(self) -> None:
        """
        Provided test demonstrating how you can test FourInARow.play using
        a StringIO object to "script" the input.

        See both the handout and the Task 4 section of the supplemental slides
        for a detailed explanation of this example.
        """
        fiar = play_game(GAME_SCRIPT_X_WINS)

        assert fiar.result == WIN

    def test_x_loses(self) -> None:
        """Test when the player use x loses"""
        fiar = play_game(GAME_SCRIPT_X_LOSES)
        assert fiar.result == LOSS

    def test_x_draw(self) -> None:
        """Test when the board is full and the players enter a draw"""
        fiar = play_game(GAME_SCRIPT_X_DRAWS)
        assert fiar.result == DRAW

    def test_computer_player(self) -> None:
        """Test when both players are computers"""
        g = FourInARow(4, False, False)
        g.play()
        assert g.result == WIN or g.result == LOSS or g.result == DRAW


if __name__ == '__main__':
    import pytest

    pytest.main(['test_a0.py'])

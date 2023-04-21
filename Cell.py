class Cell:

    def __init__(self, value, row, col, screen):
        # Constructor for the Cell class
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch = 0
        self.selected = False

    def set_cell_value(self, value):
        # Setter for this cell’s value
        self.value = value

    def set_sketched_value(self, value):
        # Setter for this cell’s sketched value
        self.sketch = value

    def draw(self):
        pass
        # Draws this cell, along with the value inside it. If this cell has a nonzero value, that value is displayed.
        # Otherwise, no value is displayed in the cell. The cell is outlined red if it is currently selected.


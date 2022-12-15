# Advent of Code Day 9 solution code


class Rope:
    def __init__(self) -> None:
        self.head = (0, 0)
        self.tail = (0, 0)
        self.tail_visited = set([self.tail])

    def move_head(self, dx: int, dy: int) -> None:
        """
        Moves the rope head in _either_ the x or y direction by dx or dy.
        """
        if dx != 0 and dy != 0:
            raise ValueError("Can only move in of x or y directions, not both")
        if abs(dx) > 1 or abs(dy) > 1:
            raise ValueError("Can only move head 1 unit at a time")

        head_x, head_y = self.head
        tail_x, tail_y = self.tail
        new_head_x, new_head_y = head_x + dx, head_y + dy
        self.head = (new_head_x, new_head_y)

        # Calculate distance between new head and current tail positions
        diff_x, diff_y = new_head_x - tail_x, new_head_y - tail_y

        # Tail needs to move only if now separated by 2 in either dimension
        if abs(diff_x) < 2 and abs(diff_y) < 2:
            return
        else:  # Otherwise, tail moves to spot previously occupied by the head
            self.update_tail_position(new_x=head_x, new_y=head_y)

    def update_tail_position(self, new_x: int, new_y: int) -> None:
        """
        Updates the current position of the tail to new_x, new_y
        and adds the new position to the set of visited tail coordinates
        """
        self.tail = (new_x, new_y)
        self.tail_visited.update([self.tail])

    def move(self, direction: str, steps: int) -> None:
        """
        Moves the rope head in the specified direction (R, L, U, D)
        by the specified number of steps
        """
        moves = {
            'R': (1, 0),
            'L': (-1, 0),
            'U': (0, 1),
            'D': (0, -1),
        }
        if direction not in moves:
            raise ValueError("direction must be one of: R, L, U, D")

        dx, dy = moves[direction]

        for _ in range(steps):
            self.move_head(dx, dy)


class LongRope(Rope):
    def __init__(self, num_knots: int = 10) -> None:
        self.knots = {k: (0, 0) for k in range(num_knots)}
        self.tail_visited = set([self.knots[num_knots-1]])
        self.tail_knot = num_knots-1

    def move_knot(self, knot: int, new_x: int, new_y: int) -> None:
        """
        Moves the specified know head in _either_ the x or y direction by dx or dy.
        Recursively moves all following knots accordingly
        """
        if knot == self.tail_knot:
            # If updating the tail knot, update coordinates & visited set only
            # This is the base case for updating recursively.
            self.knots[knot] = (new_x, new_y)
            self.tail_visited.update([self.knots[knot]])

            return

        current_head_x, current_head_y = self.knots[knot]
        current_tail_x, current_tail_y = self.knots[knot+1]
        self.knots[knot] = (new_x, new_y)

        # Calculate distance between new head and current tail positions
        diff_x, diff_y = new_x - current_tail_x, new_y - current_tail_y

        # Tail needs to move only if now separated by 2 in either dimension
        if abs(diff_x) < 2 and abs(diff_y) < 2:
            self.move_knot(knot=knot+1, new_x=current_tail_x, new_y=current_tail_y)
        else:  # Otherwise, tail moves to spot previously occupied by the head
            self.move_knot(knot=knot+1, new_x=current_head_x, new_y=current_head_y)

    def move_head(self, dx: int, dy: int) -> None:
        """Overrides super().move_head(dx, dy) to move the first knot"""
        if dx != 0 and dy != 0:
            raise ValueError("Can only move in of x or y directions, not both")
        if abs(dx) > 1 or abs(dy) > 1:
            raise ValueError("Can only move head 1 unit at a time")

        head_x, head_y = self.knots[0]
        new_x, new_y = head_x + dx, head_y + dy
        self.move_knot(knot=0, new_x=new_x, new_y=new_y)
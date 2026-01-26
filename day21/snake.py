import turtle as t

class Snake(t.Turtle):
    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment((-20 * i, 0))
    
    def add_segment(self, position):
        turtle = t.Turtle(shape="square")
        turtle.pu()
        turtle.color("white")
        turtle.goto(position)
        self.body.append(turtle)

    def move(self):
        for segment_idx in range(len(self.body) - 1, 0, -1):
            next_pos = self.body[segment_idx - 1].pos()
            self.body[segment_idx].goto(next_pos)
        self.head.fd(20)

    def grow(self):
        tail = self.body[-1].pos()
        self.add_segment(tail)
        
    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)
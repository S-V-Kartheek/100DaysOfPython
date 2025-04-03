import turtle
POSITIONS= [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
RIGHT=0
UP=90
LEFT=180
DOWN=270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_new_segment(position)

    def add_new_segment(self,position):
            new_segment = turtle.Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)


    def extend(self):
        self.add_new_segment(self.segments[-1].position())

     #from last every segment is coming to the position of its before segment until 1st segment and oth segment is moving forward
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.segments:
            seg.goto(-1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

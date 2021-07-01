class Robot:
    all_disabled = False
    latitude = -999999
    longitude = -999999
    robot_count = 0

    def __init__(self, speed = 0, direction = 180, sensor_range = 10):
        self.speed = speed
        self.direction = direction
        self.sensor_range = sensor_range
        self.obstacle_found = False
        Robot.robot_count += 1
        self.id = Robot.robot_count

    def control_bot(self, new_speed, new_direction):
        self.speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range

    def avoid_obstacles(self):
        if self.obstacle_found:
            self.direction = (self.direction + 180) % 360
            self.obstacle_found = False

    def __add__(self, value):
        self.speed += value

    def __sub__(self, value):
        self.speed -= value


class DriveBot(Robot):

    def __init__(self, motor_speed = 0, direction = 180, sensor_range = 10):
        super().__init__(motor_speed, direction, sensor_range)

    def __add__(self, value):
        super().__add__(value)
        self.sensor_range += value

    def __sub__(self, value):
        super().__sub__(value)
        self.sensor_range -= value


class WalkBot(Robot):
    walk_bot_count = 0
    def __init__(self, steps_per_minute = 0, direction = 180, sensor_range = 10, step_length = 5):
        super().__init__(steps_per_minute, direction, sensor_range)
        self.step_length = step_length
        WalkBot.walk_bot_count +=1
        if WalkBot.walk_bot_count >= 5 and Robot.robot_count >= 10:
          Robot.all_disabled = True
    def adjust_sensor(self, new_sensor_range):
       super().adjust_sensor(new_sensor_range)
       self.obstacle_found = False
       self.step_length = 5

    def avoid_obstacles(self):
       if(self.obstacle_found):
           if(self.speed <= 60):
               super().avoid_obstacles()
           else:
               self.direction = (self.direction + 90) % 360
               self.obstacle_found = False
           self.speed /= 2
           self.step_length /= 2

    def __add__(self, value):
       super().__add__(value)
       self.step_length += value / 2

    def __sub__(self, value):
       super().__sub__(value)
       self.step_length -= value / 2

robot_1 = DriveBot()
robot_2 = WalkBot()
robot_3 = DriveBot()
robot_4 = DriveBot()
robot_5 = WalkBot()
robot_6 = DriveBot()
robot_7 = DriveBot()
robot_8 = WalkBot()
robot_9 = WalkBot()
print(Robot.all_disabled)
robot_10 = WalkBot()
print(Robot.all_disabled)

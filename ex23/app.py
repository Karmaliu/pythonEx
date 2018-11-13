# 场景
class Scene(object):

    def enter(self):
        pass


# 引擎
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    # 玩法
    def play(self):
        print(self.scene_map)


# 死亡场景
class Death(Scene):
    # 回车
    def enter(self):
        pass


# 中央走廊
class CentralCorridor(Scene):

    def enter(self):
        pass


# 普通房间
class Normal(Scene):

    def enter(self):
        print('这个房间很普通,什么也没有发生')

# 武器室


class LaserWeaponArmory(Scene):

    def enter(self):
        print('这里有一把小刀')


# 主控室
class TheBridge(Scene):

    def enter(self):
        pass


# 救生仓
class EscapePod(Scene):

    def enter(self):
        print('恭喜你获救了')


# 地图
class Map(object):
    def __init__(self, start_scene):
        self.scene_name = start_scene

    # 下一个场景
    def next_scene(self, scene_name):
        self.scene_name = scene_name

    # 打开场景
    def opening_scene(self):
        print(f'这是一个{self.scene_name}')
        return self.scene_name


# 正常房间
normal_room = '正常房间'
escapePod_room = '救生仓'
thebridge_room = '主控室'
laserweaponarmory_room = '武器室'
centralcorridor_room = '中央走廊'
next_room = '请输入要进入的房间,1 or 2'


a_map = Map('central_corridor')
a_game = Engine(a_map.scene_name)
a_game.play()
print(next_room)
room_1 = input()
if room_1 is '1':
    a_map.next_scene(normal_room)
elif room_1 is '2':
    a_map.next_scene(laserweaponarmory_room)
a_map.opening_scene()
a_game.play()
print(next_room)
room_2 = input()
if room_2 is '1':
    a_map.next_scene(centralcorridor_room)
elif room_2 is '2':
    a_map.next_scene(escapePod_room)
a_map.opening_scene()

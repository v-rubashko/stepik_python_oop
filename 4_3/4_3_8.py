class Gun:
    def __init__(self):
        self.cnt = 0

    def shoot(self):
        print('pif' if self.cnt % 2 == 0 else 'paf')
        self.cnt += 1

    def shots_count(self):
        return self.cnt

    def shots_reset(self):
        self.cnt = 0

gun = Gun()

gun.shoot()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())

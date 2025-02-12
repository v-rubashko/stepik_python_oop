class Gun:
    def __init__(self):
        self.flag = True

    def shoot(self):
        if self.flag:
            print('pif')
            self.flag = False
        else:
            print('paf')
            self.flag = True


gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()

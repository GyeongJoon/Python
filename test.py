class ParkingManager:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        print(f'총 {capacity}대를 등록할 수 있습니다.')

    def register(self):
        if self.count>=self.capacity:
            print('더 이상 등록할 수 없습니다.')
            return
        self.count+=1
        print(f'차량 신규 등록{self.count}/{self.capacity}')


manager = ParkingManager(3)
for i in range(6):
    manager.register()
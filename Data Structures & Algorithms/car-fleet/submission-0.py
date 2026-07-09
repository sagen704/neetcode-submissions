class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleets = []

        position_speed = [[i, j] for i, j in zip(position, speed)]

        position_speed = sorted(position_speed, key=lambda x: x[0])

        while len(position_speed) > 1:
            
            first_car = position_speed.pop()
            second_car = position_speed.pop()

            time_first_car = (target - first_car[0]) / first_car[1]
            time_second_car = (target - second_car[0]) / second_car[1]
            
            # second car will catch up
            if time_first_car >= time_second_car:
                position_speed.append(first_car)
            # second car does not catch up 
            else: 
                position_speed.append(second_car)
                fleets.append(first_car)

        if position_speed:
            fleets.append(position_speed[0])

        # print(position_speed)
        # print(fleets)

        return len(fleets)
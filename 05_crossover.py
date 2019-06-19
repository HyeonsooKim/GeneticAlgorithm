import random
import time


class BinaryGeneticAlgorithm:
    # 랜덤으로 초기집단 염색체 생성 후 적합도 평가
    def __init__(self, n, goal):
        self.n = n
        self.goal = goal
        self.generation = 0
        self.chromosomes = []

        for i in range(n):
            chromosome = ''
            for j in range(4):
                if random.random() <= 0.5:
                    chromosome += '0'
                else:
                    chromosome += '1'
            self.chromosomes.append((chromosome, self.evaluation(chromosome)))
        self.chromosomes.sort(key=lambda x: x[1], reverse=True)

    # 적합도를 계산하는 평가 함수
    def evaluation(self, chromosome):
        return int(chromosome, 2)

    # 목표 적합도에 도달했는지 검사
    def goal_check(self):
        return self.chromosomes[0][1] == self.goal

    # 목표 세대에 도달했는지 검사
    def generation_check(self):
        return self.generation == 10

    # 룰렛 휠을 이용한 선택 연산
    # 각 염색체가 선택될 확률 = (염색체의 적합도 / 모든 염색체의 적합도 총합)
    def roulette_wheel(self):
        total_fit = sum([i[1] for i in self.chromosomes])
        roulette_pos1, roulette_pos2 = 0, 0
        while roulette_pos1 == roulette_pos2:
            roulette_pos1 = random.randint(0, total_fit)
            roulette_pos2 = random.randint(0, total_fit)

        chromosome1 = None
        chromosome2 = None
        pos = 0
        for i in self.chromosomes:
            pos += i[1]
            if chromosome1 is None and roulette_pos1 <= pos:
                chromosome1 = i
            if chromosome2 is None and roulette_pos2 <= pos:
                chromosome2 = i

        return chromosome1, chromosome2

    # 교차를 이용한 교배 연산
    def crossover(self, chromosome1, chromosome2):
        pivot = random.randint(0, len(chromosome1))
        offspring = chromosome1[:pivot] + chromosome2[pivot:]
        return offspring

    # 진화 수행
    def evolution(self):
        self.generation += 1

    def __str__(self):
        ret = '=== ' + str(self.generation) + '세대 ===\n'
        ret += '(염색체, 적합도) : ' + str(self.chromosomes) + '\n'
        return ret


if __name__ == "__main__":
    # 한 집단의 개체 수(4), 목표 적합도(15)
    BGA = BinaryGeneticAlgorithm(4, 15)
    print(BGA)
    chromosome1 = BGA.roulette_wheel()
    chromosome2 = BGA.roulette_wheel()
    offspring = BGA.crossover(chromosome1[0], chromosome2[0])
    print('선택된 부모 염색체 : ' + str(chromosome1) + ', ' + str(chromosome2))
    print('생성된 자식 염색체 : ' + str(offspring))

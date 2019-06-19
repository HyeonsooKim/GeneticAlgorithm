import random
import matplotlib.pyplot as plt


class BinaryGeneticAlgorithm:
    # 랜덤으로 초기집단 염색체 생성 후 적합도 평가
    def __init__(self, n, goal):
        self.n = n
        self.goal = goal
        self.generation = 0
        self.chromosomes = []
        self.ranking_rate = [40, 30, 20, 10]

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

    # 토너먼트 선택 연산
    # 임의의 개체를 무작위로 선택하고 그 중에서 적합도가 가장 높은 개체 선택
    def tournament_selectiont(self):
        chromosome1, chromosome2 = 0, 0
        while chromosome1 == chromosome2:
            chromosome1 = random.randint(0, self.n - 1)
            chromosome2 = random.randint(0, self.n - 1)
        chromosome1 = self.chromosomes[chromosome1]
        chromosome2 = self.chromosomes[chromosome2]
        if chromosome1[1] > chromosome2[1]:
            chromosome = chromosome1
        else:
            chromosome = chromosome2
        return chromosome1, chromosome2, chromosome

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
    result = BGA.tournament_selectiont()
    print('토너먼트 대진 : ' + str(result[:2]))
    print('선택된 염색체 : ' + str(result[-1:]))

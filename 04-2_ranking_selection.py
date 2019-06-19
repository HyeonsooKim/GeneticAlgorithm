import random
import matplotlib.pyplot as plt


class BinaryGeneticAlgorithm:
    # 랜덤으로 초기집단 염색체 생성 후 적합도 평가
    def __init__(self, n):
        self.n = n
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

    # 랭킹을 이용한 선택 연산
    # 각 염색체가 선택될 확률 = ranking_rate에 미리 정의된 확률 값
    def ranking_selection(self):
        total_fit = sum(self.ranking_rate)
        roulette_pos1, roulette_pos2 = 0, 0
        while roulette_pos1 == roulette_pos2:
            roulette_pos1 = random.randint(0, total_fit)
            roulette_pos2 = random.randint(0, total_fit)

        chromosome1 = None
        chromosome2 = None
        pos = 0
        for i in range(len(self.chromosomes)):
            pos += self.ranking_rate[i]
            if chromosome1 is None and roulette_pos1 <= pos:
                chromosome1 = self.chromosomes[i]
            if chromosome2 is None and roulette_pos2 <= pos:
                chromosome2 = self.chromosomes[i]

        # pie chart 시각화
        labels = [i[0] for i in self.chromosomes]
        plt.pie(self.ranking_rate, labels=labels, startangle=90)
        plt.show()

        return chromosome1, chromosome2

    # 진화 수행
    def evolution(self):
        self.generation += 1

    def __str__(self):
        ret = '=== ' + str(self.generation) + '세대 ===\n'
        ret += '(염색체, 적합도) : ' + str(self.chromosomes) + '\n'
        return ret


if __name__ == "__main__":
    # 한 집단의 개체 수(4)
    BGA = BinaryGeneticAlgorithm(4)
    print(BGA)
    print('선택된 염색체 : ' + str(BGA.ranking_selection()))

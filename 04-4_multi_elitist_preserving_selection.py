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

    # 엘리트 보존 선택 연산
    # 가장 적합도가 높았던 개체를 여러개 선택
    def multi_elitist_preserving_selection(self, cnt):
        return self.chromosomes[:cnt]

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
    print('선택된 염색체 : ' + str(BGA.multi_elitist_preserving_selection(2)))

import random


class BinaryGeneticAlgorithm:
    # 랜덤으로 초기집단 염색체 생성
    def __init__(self, n):
        self.n = n
        self.chromosomes = []

        for i in range(n):
            chromosome = ''
            for j in range(4):
                r = random.random()
                if r <= 0.5:
                    chromosome += '0'
                else:
                    chromosome += '1'
            self.chromosomes.append(chromosome)


if __name__ == "__main__":
    BGA = BinaryGeneticAlgorithm(4)
    print(BGA.chromosomes)

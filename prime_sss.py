import math

class Prime:
    def __init__(self):
        self.order = []
        self.num = 0
        #self.orderで素因数のリストを取得可能
        #self.numで入力した整数を取得可能

    #入力受付とデータ型・閾値の確認
    def process_first(self, num):
        self.order = []
        if str(num).isnumeric():
            if int(num) >= 2:
                return self.process_main(int(num))
            else:
                return "Error 101: 0, 1は素因数分解できません"
        else:
            return "Error 102: 負の数または数字以外は入力できません"

    #再帰処理を用いた素因数分解を行うプログラム
    def process_main(self, num):
        for i in range(1, math.ceil(math.sqrt(num)) + 2, 2):
            if i == 1:
                i = 2
            if (num % i == 0) and (num != i):
                self.order.append(i)
                return self.process_main(num // i)
            else:
                if i >= math.ceil(math.sqrt(num)):
                    #素数判定
                    self.num = num
                    if len(self.order) == 0:
                        return "Error 103: 素数です"

        generate_ans = "素因数分解をすると" + self.exponent() + "になります"
        return generate_ans

    #素因数のリストを文字列に変換
    def exponent(self):
        self.order.extend([self.num, 0])
        ans = ""
        power = 1
        for i in range(0, len(self.order) - 1):
            if self.order[i] == self.order[i + 1]:
                power += 1
            else:
                ans += str(self.order[i]) + ("^" + str(power)) * (power != 1) + " * " * (len(self.order) - i != 2)
                power = 1
        self.order.pop()
        return ans

if __name__ == '__main__':
    alpha = Prime()
    print(alpha.process_first(4))
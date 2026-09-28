import time


class RhythmicNumberGenerator:
    def __init__(self):
        # 定义数字属性
        # tone: 1=平(高), 2=升, 3=折(低), 4=降(促)
        # open_sound: True=开口音(响亮), False=闭口/撮口音(收敛)
        self.num_properties = {
            "0": {"tone": 2, "open": True, "name": "líng"},
            "1": {"tone": 1, "open": False, "name": "yī"},
            "2": {"tone": 4, "open": False, "name": "èr"},
            "3": {"tone": 1, "open": True, "name": "sān"},
            "4": {"tone": 4, "open": False, "name": "sì"},
            "5": {"tone": 3, "open": False, "name": "wǔ"},
            "6": {"tone": 4, "open": False, "name": "liù"},
            "7": {"tone": 1, "open": True, "name": "qī"},
            "8": {"tone": 1, "open": True, "name": "bā"},
            "9": {"tone": 3, "open": False, "name": "jiǔ"},
        }

        self.tone_names = {1: "平", 2: "升", 3: "折", 4: "降"}

    def get_tone_sequence(self, num_str):
        """获取数字串的声调序列"""
        return [self.num_properties[d]["tone"] for d in num_str]

    def get_open_sequence(self, num_str):
        """获取数字串的开口度序列"""
        return [self.num_properties[d]["open"] for d in num_str]

    def calculate_rhythm_score(self, num_str):
        """
        计算韵律得分
        规则：
        1. 相邻声调变化越多越好
        2. 声调跨度越大越好 (如 3->1 比 1->2 更好)
        3. 开口度交替
        4. 3+3 结构中间的断层感
        """
        tones = self.get_tone_sequence(num_str)
        opens = self.get_open_sequence(num_str)
        score = 0

        # 1. 相邻声调变化与跨度
        for i in range(len(tones) - 1):
            diff = abs(tones[i] - tones[i + 1])
            if diff == 0:
                score -= 5  # 同声调惩罚
            elif diff == 1:
                score += 2  # 小变化
            elif diff == 2:
                score += 5  # 中变化
            elif diff >= 3:
                score += 8  # 大跨度 (抑扬顿挫的核心)

        # 2. 开口度交替奖励
        for i in range(len(opens) - 1):
            if opens[i] != opens[i + 1]:
                score += 3  # 开口闭口交替

        # 3. "顿"的检查：第3位和第4位之间必须有大声调落差
        mid_diff = abs(tones[2] - tones[3])
        if mid_diff >= 2:
            score += 10  # 中间停顿感强

        # 4. 避免前三位和后三位声调模式完全一致 (避免机械重复)
        if tones[:3] == tones[3:]:
            score -= 10

        return score

    def is_valid_pattern(self, num_str):
        """基础过滤：排除顺子、逆子、全同"""
        digits = [int(d) for d in num_str]

        # 排除全同
        if len(set(digits)) == 1:
            return False

        # 排除顺子 (如 123456, 234567)
        is_sequential = all(digits[i + 1] - digits[i] == 1 for i in range(len(digits) - 1))
        if is_sequential:
            return False

        # 排除逆子
        is_reverse = all(digits[i] - digits[i + 1] == 1 for i in range(len(digits) - 1))
        if is_reverse:
            return False

        return True

    def generate_top_rhythmic_numbers(self, limit=20):
        """生成得分最高的数字排列"""
        print("正在枚举并计算 100,000 到 999,999 之间的数字韵律...")
        start_time = time.time()

        candidates = []

        # 为了演示效率，这里不枚举所有 90 万个数，而是随机采样或针对性构造
        # 但为了严谨，我们遍历所有 6 位组合 (0-9)，排除首位为0的情况
        # 注意：完整遍历 10^6 = 1,000,000 次，在现代计算机上很快 (<2秒)

        for i in range(100000, 1000000):
            num_str = str(i)

            if not self.is_valid_pattern(num_str):
                continue

            score = self.calculate_rhythm_score(num_str)

            # 设定一个高分阈值，只保留韵律感极强的
            if score >= 45:
                candidates.append((score, num_str))

        # 按分数排序
        candidates.sort(key=lambda x: x[0], reverse=True)

        end_time = time.time()
        print(f"搜索完成！耗时: {end_time - start_time:.2f} 秒")
        print(f"找到 {len(candidates)} 个高韵律感数字。\n")

        return candidates[:limit]

    def explain_number(self, num_str):
        """详细解释某个数字为什么有韵律"""
        tones = self.get_tone_sequence(num_str)
        opens = self.get_open_sequence(num_str)
        pinyin = [self.num_properties[d]["name"] for d in num_str]
        tone_labels = [self.tone_names[t] for t in tones]

        print(f"\n--- 数字分析: {num_str} ---")
        print(f"读音: {' - '.join(pinyin)}")
        print(f"声调: {' - '.join(tone_labels)} ({tones})")
        print(
            f"开口: {'开' if opens[0] else '闭'} - {'开' if opens[1] else '闭'} - {'开' if opens[2] else '闭'} | {'开' if opens[3] else '闭'} - {'开' if opens[4] else '闭'} - {'开' if opens[5] else '闭'}"
        )

        # 分析起伏
        changes = []
        for i in range(len(tones) - 1):
            d = abs(tones[i] - tones[i + 1])
            direction = "↑" if tones[i + 1] > tones[i] else ("↓" if tones[i + 1] < tones[i] else "-")
            changes.append(f"{d}{direction}")
        print(f"起伏强度: {' -> '.join(changes)}")
        print(f"韵律评分: {self.calculate_rhythm_score(num_str)}")


# 执行主程序
if __name__ == "__main__":
    generator = RhythmicNumberGenerator()

    # 获取前 10 个最佳组合
    top_numbers = generator.generate_top_rhythmic_numbers(limit=10)

    print("=== 🏆 最具抑扬顿挫感的六位数字 Top 10 ===")
    for rank, (score, num) in enumerate(top_numbers, 1):
        print(f"NO.{rank}: {num} (得分: {score})")

    # 详细分析前三名
    print("\n=== 🔍 深度解析 Top 3 ===")
    for _, num in top_numbers[:3]:
        generator.explain_number(num)

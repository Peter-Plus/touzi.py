import random

def 掷骰子(次数):
  """
  模拟掷骰子 N 次，并返回掷骰子结果的统计信息。

  参数：
    次数: 掷骰子的次数。

  返回值：
    一个字典，包含以下键值对：
      - 总次数: 掷骰子的总次数。
      - 1点次数: 掷出 1 点的次数。
      - 2点次数: 掷出 2 点的次数。
      - ...
      - 6点次数: 掷出 6 点的次数。
      - 平均值: 掷骰子结果的平均值。
      - 标准差: 掷骰子结果的标准差。
  """

  results = {}
  for _ in range(次数):
    roll = random.randint(1, 6)  # 随机生成 1 到 6 之间的整数
    if roll not in results:
      results[roll] = 0
    results[roll] += 1

  # 计算统计信息
  total_rolls = sum(results.values())
  average = sum(roll * count for roll, count in results.items()) / total_rolls
  standard_deviation = sum((roll - average)**2 * count for roll, count in results.items()) / total_rolls
  standard_deviation = standard_deviation**0.5  # 开平方计算标准差

  # 更新结果字典
  results["总次数"] = total_rolls
  results["平均值"] = average
  results["标准差"] = standard_deviation

  return results

# 示例用法
次数 = 1000
results = 掷骰子(次数)

print(f"掷骰子 {次数} 次，结果如下：")
for key, value in results.items():
  print(f"- {key}: {value}")

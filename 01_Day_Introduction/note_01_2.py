# 复数类型 实数与虚数的组合叫做复数 j表示虚数单位（只能是j才表示虚数单位，其它字符报错） 3表示虚部
print(type(1 + 3j))

# 创建一个复数
c1 = 1 + 3j
print(c1)
# 或者
c2 = complex(2, 4)
print(c2)
# 访问复数的实部和虚部
print("实部:", c1.real)
print("虚部:", c1.imag)
# 复数相加
print("复数相加:", c1 + c2)
# 复数相减
print("复数相减:", c1 - c2)
# 复数相乘
print("复数相乘:", c1 * c2)
# 复数相除
print("复数相除:", c1 / c2)
# 复数的绝对值
print("复数的绝对值:", abs(c1))
# 复数的共轭
print("复数的共轭:", c1.conjugate())

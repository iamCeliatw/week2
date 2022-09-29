#問題1
def calculate(min, max, step):
    sum = 0
    step > 0
    max > min
    for i in range(min, max + 1, step):
        sum = sum + i
    print(sum)

calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2)

#問題2
def avg(data):
    sum = 0
    a = 0
    for x in data['employees']:
        if not x['manager']:
            a = a+1
            sum = sum + x['salary']
        else:
            continue
    print(sum / a )


avg({
    "employees": [
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
{
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
{
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
{
            "name":"Tony",
            "salary":40000,
            "manager":False
        },
    ]
})

#問題3
def func(a):
  def f(b,c):
      result = a + b *c
      print(result)
  return f

func(2)(3,4)
func(5)(1, -5)
func(-3)(2, 9)

#問題4
def maxProduct(nums):
    n = len(nums)
    if n < 2:
        return
    nums.sort()

    if (nums[0]*nums[1]>nums[n-1]*nums[n-2]):
        result = nums[0]*nums[1]
        print(result)
    else:
        result = nums[n-1]*nums[n-2]
        print(result)

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([10, -20, 0, -3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([5, -1, -2, 0])
maxProduct([-5, -2])

#問題5
def twoSum(nums, target):
    size = len(nums)
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if (nums[i] + nums[j] == target):
                return [i,j]
result = twoSum([2, 11, 7, 5, 9], 9)
print(result)

#問題6
def maxZeros(nums):
    zeroCount = 0
    maxZeroCount = 0
    lens = len(nums)
    for i in range (lens):
        if nums[i] == 1:
            zeroCount = 0
        else:
            zeroCount= zeroCount+1
            maxZeroCount = max(zeroCount,maxZeroCount)
    print(maxZeroCount)

maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])
maxZeros([0, 0, 0, 1, 1])

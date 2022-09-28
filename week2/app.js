//問題1
function calculate(min, max, step) {
  sum = 0;
  for (i = min; i < max + 1; i += step) {
    sum = sum + i;
  }
  console.log(sum);
}
calculate(1, 3, 1);
calculate(4, 8, 2);
calculate(-1, 2, 2);

// 問題2;
function avg(data) {
  let sum = 0;
  let a = 0;
  let len = data.employees.length;
  for (i = 0; i < len; i++) {
    if (data.employees[i].manager === false) {
      a++;
    } else continue;
    sum += data.employees[i].salary;
  }
  console.log(sum / a);
  //如果使用return 回傳函式的話
  //要將以下的function 放入一個變數 接住return的值
  //才能把回傳值傳遞出去
}

avg({
  employees: [
    {
      name: "John",
      salary: 30000,
      manager: false,
    },
    {
      name: "Bob",
      salary: 60000,
      manager: true,
    },
    {
      name: "Jenny",
      salary: 50000,
      manager: false,
    },
    {
      name: "Tony",
      salary: 40000,
      manager: false,
    },
  ],
});

//問題3
function func(a) {
  function f(b, c) {
    let result = a + b * c;
    console.log(result);
  }
  return f;
}

func(2)(3, 4);
func(5)(1, -5);
func(-3)(2, 9);

//問題4
function maxProduct(nums) {
  // 排列array的順序
  nums.sort(function (a, b) {
    return a - b;
  });
  let n = nums.length;
  let num1, num2;
  let sum1 = nums[0] * nums[1];
  let sum2 = nums[n - 1] * nums[n - 2];

  if (sum1 > sum2) {
    num1 = nums[0];
    num2 = nums[1];
  } else {
    num1 = nums[n - 2];
    num2 = nums[n - 1];
  }
  console.log(num1 * num2);
}
maxProduct([5, 20, 2, 6]);
maxProduct([10, -20, 0, 3]);
maxProduct([10, -20, 0, -3]);
maxProduct([-1, 2]);
maxProduct([-1, 0, 2]);
maxProduct([5, -1, -2, 0]);
maxProduct([-5, -2]);

//問題5
function twoSum(nums, target) {
  let lens = nums.length;
  for (let i = 0; i < lens - 1; i++) {
    for (let j = i + 1; j < lens; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result);

class SortAlgorithm
  bubbleSort: (nums) ->
    _nums = nums[..]
    for i in [0.._nums.length]
      for j in [i + 1.._nums.length]
        if _nums[i] > _nums[j]
          tmp = _nums[i];
          _nums[i] = _nums[j]
          _nums[j] = tmp
    _nums

  quickSort: (nums) ->
    _nums = nums[..]
    if _nums.length < 1
      return _nums

    pi = _nums[0]
    left = []
    right = []
    for i in _nums[1..]
      if i < pi
        left.push(i)
      else
        right.push(i)

    @quickSort(left).concat([pi]).concat(@quickSort(right))


sort = new SortAlgorithm
nums = (Math.floor(Math.random() * 10) for i in [0...10])
console.log sort.bubbleSort(nums)

console.log sort.quickSort(nums)

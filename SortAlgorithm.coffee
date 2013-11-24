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


sort = new SortAlgorithm
nums = (Math.floor(Math.random() * 10) for i in [0...10])
console.log sort.bubbleSort(nums)


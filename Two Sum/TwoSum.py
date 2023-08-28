def twoSum(nums : list[int], target : int)  -> list[int] :
    dict_diff = {}

    for i in range(len(nums)) :
        if nums[i] in dict_diff :
            return [i, dict_diff[nums[i]]]
        else :
            dict_diff[target - nums[i]] = i

    return []
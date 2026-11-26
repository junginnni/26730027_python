#리스트 정렬 -> 리스트이름.sort() (오름차순, 내림차순)
data = [2, 4, 3, 1, 5, 10, 9]
data.sort(reverse=False) #오름차순 sort()
data.sort(reverse=True) #내림차순
print(data)
#sorted(리스트이름) -> sorted(리스트이름, reverse=True) <- 내림
nums=[5, 3, 1, 4, 2]
result = sorted(nums, reverse=True)
print(result)

#中毒时长
class Solution:
    def findPoisonedDuration(timeSeries, duration):
        time = 0
        for i in range(1,len(timeSeries)):
            if timeSeries[i] - timeSeries[i-1] >= duration:
                time += duration
            else:
                time += timeSeries[i] - timeSeries[i-1]
        return time + duration
timeSeries = [1,4]
duration = 2
print(Solution.findPoisonedDuration(timeSeries,duration))

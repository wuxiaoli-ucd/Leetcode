class Solution:
    def alertNames(self, keyName: list[str], keyTime: list[str]) -> list[str]:
        name_dict = {}
        alert_set = set()

        for i, name in enumerate(keyName):
            if name not in name_dict:
                name_dict[name] = []

            hour, minute = keyTime[i].split(":")
            time = int(hour) * 60 + int(minute)
            name_dict[name].append(time)

        for name in name_dict:
            times = name_dict[name]
            times.sort()

            for i in range(len(times) - 2):
                if times[i + 2] - times[i] <= 60:
                    alert_set.add(name)
                    break

        return sorted(alert_set)

        # store the people in the dict, and save the time as the value.
        # if the name not in dict, continue. othervise,check the loop in the dict. and keep a temp value in the loop to judge if there is 2 time in the range,thinking about instead of loop the whole loop ,maybe just loop the last 2. there might be some way to improve here
        # 这道题有个关注点在于就是这里没有说时间是有序的，所以我需要把他们loop一遍，然后把时间都存进字典里面。
        # sort time
        # loop the list time, if i+2>i, store name into the set and break
        # sort the name list


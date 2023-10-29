import pandas as pd
import csv
import statistics

class Data:
    def __init__(self, csv_file, name):
        self.name = name
        self.csv_file = csv_file
        self.data = []
        self.readcsv()
        self.dataheader()


    def dataheader(self):
        header = self.data[0]
        new_header = [col.capitalize() for col in header]
        return new_header
    
    def readcsv(self):
        with open(self.csv_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.data.append(row)

    ## Methods to group and analyse

    ## Data info mehtod
    def datainfo(self):
        total = len(self.data)
        columns = len(self.dataheader)

    ## Total Methods

    def count(self, group, subgroup=None):
        header = self.data[0]
        if subgroup is not None:
            grouped_data = self.groupby(subgroup)
            if group.lower() in header:
                index = header.index(group)
                result = {}
                for k, v in grouped_data.items():
                    key, subgroup_value = k # Unpack the tuple
                    group_list = [item[index] for item in v]
                    count_dict = {}  # Create a dictionary to count distinct values
                    for item in group_list:
                        if item not in count_dict:
                            count_dict[item] = 1
                        else:
                            count_dict[item] += 1
                    result[(key, subgroup_value)] = count_dict  # Store (region, subgroup) and its count
                return result
        else:
            if group.lower() in header:
                index = header.index(group)
                group_data = [item[index] for item in self.data[1:]]
                count_dict = {}  # Create a dictionary to count distinct values
                for value in group_data:
                    if value not in count_dict:
                        count_dict[value] = 1
                    else:
                        count_dict[value] += 1
                return count_dict

        
    ## Median Methods
    def median(self, group, subgroup = None):
        header = self.data[0]
        if subgroup is not None:
            grouped_data = self.groupby(subgroup)
            if group.lower() in header:
                index = header.index(group)
                new_group = {}
                for k,v in grouped_data.items():
                    name, value = k
                    group_list = [float(item[index]) for item in v]  # Creating a list of values which will append
                    sorted_list = sorted(group_list)
                    length = len(sorted_list)
                    if length % 2 == 0:
                        half1 = sorted_list[(length // 2) - 1]
                        half2 = sorted_list[length // 2]
                        median = (half1 + half2) / 2
                    else:
                        median = sorted_list[length // 2]
                    new_group[k] = median
                return new_group
        else:
            if group.lower() in header:
                index = header.index(group)
                group_data = [float(item[index]) for item in self.data[1:]]
                sorted_data = sorted(group_data)
                ##Calculate median
                length = len(sorted_data)
                if length % 2 == 0:
                    half_index_1 = sorted_data[(length // 2) -1]
                    half_index_2 = sorted_data[length // 2]
                    median = (half_index_1+half_index_2) / 2
                else:
                    median = sorted_data[length // 2]
            return median

    ## Mean Methods :(
    def mean(self, group, subgroup=None):
        header = self.data[0]
        if subgroup is not None:
            grouped_data = self.groupby(subgroup)
            if group.lower() in header:
                index = header.index(group)
                new_group = {}
                for k, v in grouped_data.items():
                    name, value = k
                    group_list = [float(item[index]) for item in v]
                    length = len(group_list)
                    total = 0
                    for item in group_list:
                        total += item
                    mean = total/length
                    new_group[k] = round(mean)
                return new_group
        else:
            if group.lower() in header:
                index = header.index(group)
                group_data = [float(item[index]) for item in self.data[1:]]
                length = len(group_data)
                total = 0
                for value in group_data:
                    total += value
                mean = total / length
            return round(mean)

    ## Group Data
    def groupby(self, group):
        new_dict = {}
        header = self.data[0]
        if group.lower() in header:
            header_index = header.index(group)
            values = self.data[1:]
            for item in values:
                key = (header[header_index], item[header_index])
                if key not in new_dict:
                    new_dict[key] = [item]
                else:
                    new_dict[key].append(item)
        return new_dict

    ## This is to print a formatted output to terminal/window
    def printgrouping(self, group):
        group_dict = self.groupby(group)
        header = self.dataheader()
        fomratted_output = ""
        for k, v in group_dict.items():
            fomratted_output += f"\n{k[0].capitalize()}: {k[1].capitalize()}\n"
            fomratted_output += f"{', '.join(header)}\n\n"
            for i in v:
                fomratted_output += f"{', '.join(i)}\n"
        return fomratted_output




md = Data("insurance.csv", "Medical Insurance Data")

# for items in md.data:
#     print(items)

region = md.groupby("region")
# print(region)

sortmd = md.median("age", "region")
print(sortmd)

mean = md.mean("charges", "smoker")
print(mean)

t_num = md.count("children", "smoker")
print(t_num)





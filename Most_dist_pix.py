import os
import sys
import glob
import math
import csv

work_dir = sys.argv[1:]

for sub_dir in work_dir:
    print('Processing: '+sub_dir)
    os.chdir(sub_dir)
    files = glob.glob('*.txt')
    files.sort()
    max_dist_master = [] #a matrix with maximum distances from all files
    for file in files:
        max_dist_list = [] #a list of maximum distances in a file timeframes
        max_dist_list.append(file[:-4])
        coor_list = [[]] #a list with all pixels coordinates in a file
        frame = 0
        with open(file) as f:
            for line in f:
                line = list(map(int, line.split("\t")))
                if line[2] > frame: #3rd number in line = number of frame
                    frame += 1
                    coor_list.append([])
                coor_list[frame].append(line)
        for coor_frame in coor_list:
            max_distance = 0
            for i in range(len(coor_frame)-1):
                for j in range(i+1,len(coor_frame)):
                    a = coor_frame[i][0:2]
                    b = coor_frame[j][0:2]
                    distance=math.dist(a, b)
                    if(distance>max_distance):
                        max_distance = distance
            max_dist_list.append(max_distance)
        max_dist_master.append(max_dist_list)
    #transpose (make rows into columns)
    max_dist_master = list(zip(*max_dist_master))
    #save into csv
    result_file = sub_dir.split("/")[-1] + ".csv"
    os.chdir("..")
    with open(result_file, "w+", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(max_dist_master)
        



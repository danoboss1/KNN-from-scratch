# https://www.youtube.com/watch?v=xtaom__-drE&list=PLzjH1ZFHdrC-J6J_cq6AWKeQx2FwUz2UJ&index=28&t=955s

import numpy as np
import matplotlib.pyplot as plt

GLOBAL_white = "#FFFFFF"
GLOBAL_blue = "#104DCA"
GLOBAL_red = "#FF0000"

def euclidean_distance(p, q):
    return np.sqrt(np.sum((np.array(p) - np.array(q)) ** 2))

def count_distances_from_points(new_point, input_points):
    result_list = []

    for gift in input_points:
        new_distance = euclidean_distance(new_point, gift)
        result_list.append(new_distance)

    return result_list

def KNN_algorithm(k, distances_from_brother, distances_from_girlfriend):
    number_brother_distance = 0
    number_girlfriend_distance = 0

        # a podla neho to porovnat
    for i in range(k):
        number_brother_distance += max(distances_from_brother)
        distances_from_brother.remove(max(distances_from_brother))
        # print(distances_from_brother)
        
    for j in range(k):
        number_girlfriend_distance += max(distances_from_girlfriend)
        distances_from_girlfriend.remove(max(distances_from_girlfriend))
        # print(distances_from_girlfriend)

    if number_brother_distance < number_girlfriend_distance:
        print('The gift will be for brother')
        new_point_color = GLOBAL_blue
    elif number_brother_distance == number_girlfriend_distance:
        print('The gift can be for both of them')
        #white
        new_point_color = GLOBAL_white
    else:
        print('The gift is for your girlfriend')
        new_point_color = GLOBAL_red

    return number_brother_distance, number_girlfriend_distance, new_point_color


def visualization(brother, girlfriend, new_point, new_point_color):
    ax = plt.subplot()
    ax.grid(True, color="#323232")
    ax.set_facecolor("#000000")
    ax.figure.set_facecolor("#121212")
    ax.tick_params(axis="x", color="white")
    ax.tick_params(axis="y", color="white")

    # blue
    for point in brother:
        ax.scatter(point[0], point[1], color=GLOBAL_blue, s=60)
    # red
    for point in girlfriend:
        ax.scatter(point[0], point[1], color=GLOBAL_red, s=60)

    ax.scatter(new_point[0], new_point[1], color=new_point_color, marker="*", s=200, zorder=100)

    for point in brother:
        ax.plot([new_point[0], point[0]], [new_point[1], point[1]], color=GLOBAL_blue, linestyle="--", linewidth=1)
    for point in girlfriend:
        ax.plot([new_point[0], point[0]], [new_point[1], point[1]], color=GLOBAL_red, linestyle="--", linewidth=1)
    
    plt.show()


def main():
    # darceky su zabalene a prve je velkost a druhe je na nich nalepena cenovka
    brother = [[23,4], [15,7], [16,5], [20,8], [19,2]]
    girlfriend = [[3,20], [5,11], [4,19], [3,17], [9,11]]

    new_point = [10, 10]

    distances_from_brother = count_distances_from_points(new_point, brother)
    distances_from_girlfriend = count_distances_from_points(new_point, girlfriend)

    print(f"Distances from brothers previous gifts are {distances_from_brother}")
    print(f"Distances from brothers previous gifts are {distances_from_girlfriend}")

    # vybrat z toho k=pocet_ktory_chceme_bodov
    k = 3

    number_brother_distance, number_girlfriend_distance, new_point_color = KNN_algorithm(k, distances_from_brother, distances_from_girlfriend)

    print(f"Distance from brother is {number_brother_distance}")
    print(f"Distance from girlfriend is {number_girlfriend_distance}")

    # visualize
    visualization(brother, girlfriend, new_point, new_point_color)

if __name__ == "__main__":
    main()
import matplotlib.pyplot as plt
import numpy as np

negative = [[1, 1],[2, 1],[1,-1], [2,-1]]
positive = [[4,0],[5,1],[5,-1],[6,0]]


def draw_plot(data1, data2, marker1='x', marker2='o', color1='blue', color2='red'):
    data1 = np.array(data1)
    data2 = np.array(data2)
    plt.scatter(data1[:,0],data1[:,1], marker=marker1, c=color1)
    plt.scatter(data2[:,0], data2[:,1], marker=marker2, c=color2)
    plt.grid()
    plt.show()

def draw_plot_with_sv(data1, data2, sv1, sv2):
    data1 = np.array(data1)
    data2 = np.array(data2)
    sv1 = np.array(sv1)
    sv2 = np.array(sv2)
    

    plt.scatter(data1[:,0],data1[:,1], marker='o', c='red')
    plt.scatter(data2[:,0], data2[:,1], marker='x', c='blue')
    plt.scatter(sv1[:,0], sv1[:,1], marker='d')
    plt.scatter(sv2[:,0], sv2[:,1], marker='d')
    plt.grid()
    plt.show()
    
def find_distance_2D(a, b):
    return (b[0]-a[0])**2 + (b[1]-a[1])**2 # (x2 - x1 )^2 + (y2 - y1)^2
    
def find_support_vectors_2D(X, Y):
    support_vectors = []
    distances = []
    distances_points = []
    
    for x in X:
        for y in Y:
            d = find_distance_2D(x, y)
            # print(f"positive {x} and negative {y} = {d}")
            distances.append(d)
            distances_points.append([x, y])

    combined = list(zip(distances, distances_points)) # make tupple of first and second list
    sorted_combined = sorted(combined) # sorting base on first value of tupple, use 'key' for other values
    
    temp = sorted_combined[0][0]
    for dist, point in sorted_combined:
        if temp == dist:
            support_vectors.append(point)
        else:
            break
    
    first_para_sv = []
    second_para_sv = []
    
    for i in support_vectors:
        print(i)
        first_para_sv.append(i[0])
        second_para_sv.append(i[1])
    
    
    # Convert list of lists to a set of tuples, since lists are not hashable
    unique_first_set = {tuple(sublist) for sublist in first_para_sv}
    unique_second_set = {tuple(sublist) for sublist in second_para_sv}

    # Convert back to list of lists
    unique_first_list = [list(sublist) for sublist in unique_first_set]
    unique_second_list = [list(sublist) for sublist in unique_second_set]
    
    return (unique_first_list, unique_second_list)
 
draw_plot(positive, negative, marker1='o', marker2='x')

posi_sv, neg_sv = find_support_vectors_2D(positive, negative)

print(f"Positive support vectors: {posi_sv}")
print(f"Negative support vectors: {neg_sv}")

draw_plot_with_sv(positive, negative, posi_sv, neg_sv)
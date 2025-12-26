import numpy as np

def main():
    # Core logic here
    string = "Hello, World!"
    print(string)
    # Sample numpy operation
    array = np.array([1, 2, 3, 4, 5])
    A = 2+2
    print("Numpy array:", array)
    np.save('array.npy', array) # Save large outputs to ceph

if __name__ == "__main__":
    main()
# Insertion sort

插入排序，举一个从小到大排序的例子。有一个数组，我们应该从第二个位置开始比较，当前位置的值和前一位置的值进行比较，如果前一位置更大那就把前一位置的值存到当前位置上。此时第一和第二位置的值已经是排序好的状态。进入下一次迭代，此时用前一个位置（第一步的再前一个位置）和当前位置比较，如果前一位置更大则把前一位置的值保存到当前位置上。后面剩下的位置都以此类推，最终将得到排序好的数组。

/resources/image-20210422190057370.png

伪代码为：

![image-20210422190113749](C:\Users\정성환\AppData\Roaming\Typora\typora-user-images\image-20210422190113749.png)

```python
def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i>=0 and array[i]>key:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key
	return array

a = insertion_sort([5,2,4,6,1,3])
print(a)
>>>

```


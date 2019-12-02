基本排序算法
====

冒泡排序
---

重复的走访要排序的数列，如果他们的顺序错误就把他们交换过来

```java
public static int[] bubbleSort(int[] array) {
    if (array.length == 0)
        return array;
    for (int i = 0; i < array.length; i++)
        for (int j = 0; j < array.length - 1 - i; j++)
            if (array[j + 1] < array[j]) {
                int temp = array[j + 1];
                array[j + 1] = array[j];
                array[j] = temp;
            }
    return array;
}
```

最佳情况： T（n） = O（n）
最差情况： T（n） = O（n^2）
平均情况： T（n） = O（n^2）

选择排序
---

表现最稳定的排序，数据规模越小越好，不占用额外空间。选择排序队列中最小的元素放到已排序队列的末尾

```java
public static int[] selectionSort(int[] array) {
    if (array.length == 0)
        return array;
    for (int i = 0; i < array.length; i++) {
        int minIndex = i;
        for (int j = i; j < array.length; j++) {
            if (array[j] < array[minIndex]) //找到最小的数
                minIndex = j; //将最小数的索引保存
        }
        int temp = array[minIndex];
        array[minIndex] = array[i];
        array[i] = temp;
    }
    return array;
}
```

最佳情况： T（n） = O（n^2）
最差情况： T（n） = O（n^2）
平均情况： T（n） = O（n^2）

插入排序
---

构建有序队列，对未排序数据，在已排序序列中从后向前扫描，找到相应的位置插入

```java
public static int[] insertionSort(int[] array) {
    if (array.length == 0)
        return array;
    int current;
    for (int i = 0; i < array.length - 1; i++) {
        current = array[i + 1];
        int preIndex = i;
        while (preIndex >= 0 && current < array[preIndex]) {
            array[preIndex + 1] = array[preIndex];
            preIndex--;
        }
        array[preIndex + 1] = current;
    }
    return array;
}
```

最佳情况： T（n） = O（n）
最差情况： T（n） = O（n^2）
平均情况： T（n） = O（n^2）

希尔排序
---

希尔排序也是一种插入算法，他会优先比较距离较远的元素，希尔排序又叫缩小增量排序。希尔排序是把记录下标的一定增量分组，对每组使用直接插入排序算法，随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个序列被分成一组，算法终止

```java
public static int[] ShellSort(int[] array) {
    int len = array.length;
    int temp, gap = len / 2;
    while (gap > 0) {
        for (int i = gap; i < len; i++) {
            temp = array[i];
            int preIndex = i - gap;
            while (preIndex >= 0 && array[preIndex] > temp) {
                array[preIndex + gap] = array[preIndex];
                preIndex -= gap;
            }
            array[preIndex + gap] = temp;
        }
        gap /= 2;
    }
    return array;
}
```

最佳情况： T（n） = O（nlog2n）
最差情况： T（n） = O（nlog2n）
平均情况： T（n） = O（nlog2n）

归并排序
---

与选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好很多。算法采用分治法，将有序的子序列合并，得到完全有序的序列。

```java
public static int[] MergeSort(int[] array) {
    if (array.length < 2) return array;
    int mid = array.length / 2;
    int[] left = Arrays.copyOfRange(array, 0, mid);
    int[] right = Arrays.copyOfRange(array, mid, array.length);
    return merge(MergeSort(left), MergeSort(right));
}
public static int[] merge(int[] left, int[] right) {
    int[] result = new int[left.length + right.length];
    for (int index = 0, i = 0, j = 0; index < result.length; index++) {
        if (i >= left.length)
            result[index] = right[j++];
        else if (j >= right.length)
            result[index] = left[i++];
        else if (left[i] > right[j])
            result[index] = right[j++];
        else
            result[index] = left[i++];
    }
    return result;
}
```

最佳情况： T（n） = O（n）
最差情况： T（n） = O（nlogn）
平均情况： T（n） = O（nlogn）

快速排序
---

通过一趟排序将待排记录分割成独立的两部分，其中一部分记录关键字均比另一部分关键字小，则可分别对这两部分记录继续排序

```java
public static int[] quickSort(int[] array, int start, int end) {
    if (array.length < 1 || start < 0 || end >= array.length || start > end) return null;
    int smallIndex = partition(array, start, end);
    if (smallIndex > start)
        quickSort(array, start, smallIndex - 1);
    if (smallIndex < end)
        quickSort(array, smallIndex + 1, end);
    return array;
}
public static int partition(int[] array, int start, int end) {
    int pivot = (int) (start + Math.random() * (end - start + 1));
    int smallIndex = start - 1;
    swap(array, pivot, end);
    for (int i = start; i <= end; i++)
        if (array[i] <= array[end]) {
            smallIndex++;
            if (i > smallIndex)
                swap(array, i, smallIndex);
        }
    return smallIndex;
}
public static void swap(int[] array, int i, int j) {
    int temp = array[i];
    array[i] = array[j];
    array[j] = temp;
}
```

最佳情况： T（n） = O（nlogn）
最差情况： T（n） = O（n^2）
平均情况： T（n） = O（nlogn）

堆排序
---

子节点的值总是大于（或小于）他的父节点

```java
//声明全局变量，用于记录数组array的长度；
static int len;
/**
    * 堆排序算法
    *
    * @param array
    * @return
    */
public static int[] HeapSort(int[] array) {
    len = array.length;
    if (len < 1) return array;
    //1.构建一个最大堆
    buildMaxHeap(array);
    //2.循环将堆首位（最大值）与末位交换，然后在重新调整最大堆
    while (len > 0) {
        swap(array, 0, len - 1);
        len--;
        adjustHeap(array, 0);
    }
    return array;
}
/**
    * 建立最大堆
    *
    * @param array
    */
public static void buildMaxHeap(int[] array) {
    //从最后一个非叶子节点开始向上构造最大堆
    //for循环这样写会更好一点：i的左子树和右子树分别2i+1和2(i+1)
    for (int i = (len/2- 1); i >= 0; i--) {
        adjustHeap(array, i);
    }
}
/**
    * 调整使之成为最大堆
    *
    * @param array
    * @param i
    */
public static void adjustHeap(int[] array, int i) {
    int maxIndex = i;
    //如果有左子树，且左子树大于父节点，则将最大指针指向左子树
    if (i * 2 < len && array[i * 2] > array[maxIndex])
        maxIndex = i * 2+1;   //感谢网友矫正，之前是i*2
    //如果有右子树，且右子树大于父节点，则将最大指针指向右子树
    if (i * 2 + 1 < len && array[i * 2 + 1] > array[maxIndex])
        maxIndex = i * 2 + 2;   //感谢网友矫正，之前是i*2+1
    //如果父节点不是最大值，则将父节点与最大值交换，并且递归调整与父节点交换的位置。
    if (maxIndex != i) {
        swap(array, maxIndex, i);
        adjustHeap(array, maxIndex);
    }
}
```

最佳情况： T（n） = O（nlogn）
最差情况： T（n） = O（nlogn）
平均情况： T（n） = O（nlogn）

计数排序
---

将输入的数据值转化为键存储在额外开辟的空间，记录排序元素的个数（排序元素的数值范围需要确认）

```java
public static int[] CountingSort(int[] array) {
    if (array.length == 0) return array;
    int bias, min = array[0], max = array[0];
    for (int i = 1; i < array.length; i++) {
        if (array[i] > max)
            max = array[i];
        if (array[i] < min)
            min = array[i];
    }
    bias = 0 - min;
    int[] bucket = new int[max - min + 1];
    Arrays.fill(bucket, 0);
    for (int i = 0; i < array.length; i++) {
        bucket[array[i] + bias]++;
    }
    int index = 0, i = 0;
    while (index < array.length) {
        if (bucket[i] != 0) {
            array[index] = i - bias;
            bucket[i]--;
            index++;
        } else
            i++;
    }
    return array;
}
```

最佳情况： T（n） = O（n+k）
最差情况： T（n） = O（n+k）
平均情况： T（n） = O（n+k）

桶排序
---

将数据分到有限个数量的桶里，每个桶再分别排序

```java
public static ArrayList<Integer> BucketSort(ArrayList<Integer> array, int bucketSize) {
    if (array == null || array.size() < 2)
        return array;
    int max = array.get(0), min = array.get(0);
    // 找到最大值最小值
    for (int i = 0; i < array.size(); i++) {
        if (array.get(i) > max)
            max = array.get(i);
        if (array.get(i) < min)
            min = array.get(i);
    }
    int bucketCount = (max - min) / bucketSize + 1;
    ArrayList<ArrayList<Integer>> bucketArr = new ArrayList<>(bucketCount);
    ArrayList<Integer> resultArr = new ArrayList<>();
    for (int i = 0; i < bucketCount; i++) {
        bucketArr.add(new ArrayList<Integer>());
    }
    for (int i = 0; i < array.size(); i++) {
        bucketArr.get((array.get(i) - min) / bucketSize).add(array.get(i));
    }
    for (int i = 0; i < bucketCount; i++) {
        if (bucketSize == 1) { // 如果带排序数组中有重复数字时
            for (int j = 0; j < bucketArr.get(i).size(); j++)
                resultArr.add(bucketArr.get(i).get(j));
        } else {
            if (bucketCount == 1)
                bucketSize--;
            ArrayList<Integer> temp = BucketSort(bucketArr.get(i), bucketSize);
            for (int j = 0; j < temp.size(); j++)
                resultArr.add(temp.get(j));
        }
    }
    return resultArr;
}
```

最佳情况： T（n） = O（n+k）
最差情况： T（n） = O（n+k）
平均情况： T（n） = O（n^2）

基数排序
---

按照低位排序再收集，再高位排序再收集

```java
public static int[] RadixSort(int[] array) {
    if (array == null || array.length < 2)
        return array;
    // 1.先算出最大数的位数；
    int max = array[0];
    for (int i = 1; i < array.length; i++) {
        max = Math.max(max, array[i]);
    }
    int maxDigit = 0;
    while (max != 0) {
        max /= 10;
        maxDigit++;
    }
    int mod = 10, div = 1;
    ArrayList<ArrayList<Integer>> bucketList = new ArrayList<ArrayList<Integer>>();
    for (int i = 0; i < 10; i++)
        bucketList.add(new ArrayList<Integer>());
    for (int i = 0; i < maxDigit; i++, mod *= 10, div *= 10) {
        for (int j = 0; j < array.length; j++) {
            int num = (array[j] % mod) / div;
            bucketList.get(num).add(array[j]);
        }
        int index = 0;
        for (int j = 0; j < bucketList.size(); j++) {
            for (int k = 0; k < bucketList.get(j).size(); k++)
                array[index++] = bucketList.get(j).get(k);
            bucketList.get(j).clear();
        }
    }
    return array;
}
```

最佳情况： T（n） = O（n*k）
最差情况： T（n） = O（n*k）
平均情况： T（n） = O（n*k）
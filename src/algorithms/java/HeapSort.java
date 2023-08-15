public class HeapSort {
    private int left(int i) {
        return 2 * i + 1;
    }

    private int right(int i) {
        return 2 * i + 2;
    }

    private int parent(int i) {
        return i / 2;
    }

    private void maxHepify(int[] heap, int n, int i) {
        int largest = i;
        int l = left(i);
        int r = right(i);

        if (l < n && heap[l] > heap[largest]) {
            largest = l;
        }

        if (r < n && heap[r] > heap[largest]) {
            largest = r;
        }

        if (largest != i) {
            int temp = heap[i];
            heap[i] = heap[largest];
            heap[largest] = temp;

            maxHepify(heap, n, largest);
        }
    }

    private void buildHeap(int[] heap, int n) {
        for (int i = (n / 2) - 1; i >= 0; i--) {
            maxHepify(heap, n, i);
        }
    }

    public void heapSort(int[] heap) {
        int n = heap.length;
        buildHeap(heap, n);

        for (int i = n - 1; i > 0; i--) {
            int temp = heap[0];
            heap[0] = heap[i];
            heap[i] = temp;

            maxHepify(heap, i, 0);
        }
    }

    private void print(int[] heap) {
        for (int h : heap) {
            System.out.printf("%d ", h);
        }

        System.out.println();
    }

    public static void main(String[] args) {
        int[] heap = {19, 7, 17, 3, 5, 12, 10, 1, 2};
        HeapSort heapSort = new HeapSort();
        heapSort.heapSort(heap);
        heapSort.print(heap);

        System.out.println("Heap Sort...");
    }
}

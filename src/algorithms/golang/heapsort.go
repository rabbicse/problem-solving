package main

import "fmt"

func left(i int) int {
	return 2*i + 1
}

func right(i int) int {
	return 2*i + 2
}

func maxHepify(heap []int, n int, i int) {
	l := left(i)
	r := right(i)
	largest := i

	if l < n && heap[l] > heap[largest] {
		largest = l
	}

	if r < n && heap[r] > heap[largest] {
		largest = r
	}

	if largest != i {
		heap[i], heap[largest] = heap[largest], heap[i]

		maxHepify(heap, n, largest)
	}
}

func buildHeap(heap []int, n int) {
	for i := (n / 2) - 1; i >= 0; i-- {
		maxHepify(heap, n, i)
	}
}

func heapSort(heap []int) {
	n := len(heap)
	buildHeap(heap, n)

	for i := n - 1; i > 0; i-- {
		heap[i], heap[0] = heap[0], heap[i]
		maxHepify(heap, i, 0)
	}
}

func print(heap []int) {
	for i := 0; i < len(heap); i++ {
		fmt.Print(heap[i])
		fmt.Print(" ")
	}

	fmt.Println()
}

func main() {
	heap := []int{19, 7, 17, 3, 5, 12, 10, 1, 2}

	heapSort(heap)

	print(heap)
}

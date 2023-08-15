package main

import "fmt"

func left(i int) int {
	return 2*i + 1
}

func right(i int) int {
	return 2*i + 1
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

		maxHepify(heap, n-1, i)
	}
}

func buildHeap(heap []int, n int) {
	for i := n/2 - 1; i >= 0; i-- {
		maxHepify(heap, n, i)
	}
}

func heapSort(heap []int) {
	n := len(heap)
	for i := n - 1; i > 0; i-- {

	}
}

func main() {
	heap := []int{5, 3}

	fmt.Println("Hello")
}

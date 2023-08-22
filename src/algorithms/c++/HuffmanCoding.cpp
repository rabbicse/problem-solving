// Online C++ compiler to run C++ program online
#include <iostream>
#include <queue>
#include <unordered_map>

using namespace std;

struct Node {
    char data;
    int freq;
    Node *left;
    Node *right;
    
    Node(char data, int freq) {
        this->data = data;
        this->freq = freq;
        this->left = nullptr;
        this->right = nullptr;
    }
};

struct Compare {
    bool operator()(Node *l, Node *r) {
        return (l->freq > r->freq);
    }
};

Node* buildHuffmanTree(string text) {
    unordered_map<char, int> freqMap;
    for(char c : text) {
        freqMap[c]++;
    }
    
    // declare priority queue
    priority_queue<Node*, vector<Node*>, Compare> pq;
    for(auto& m : freqMap) {
        pq.push(new Node(m.first, m.second));
    }
    
    while(pq.size() > 1) {
        Node* left = pq.top();
        pq.pop();
        
        Node* right = pq.top();
        pq.pop();
        
        Node* node = new Node('\0', left->freq + right->freq);
        node->left = left;
        node->right = right;
        
        pq.push(node);
    }
    
    return pq.top();
}

void encode(Node* root, string str, unordered_map<char, string> &huffmanCode) {
    if(root == nullptr) return;
    
    // found a leaf node
	if (!root->left && !root->right) {
		huffmanCode[root->data] = str;
	}
	
	encode(root->left, str + "0", huffmanCode);
	encode(root->right, str + "1", huffmanCode);
}

// Prints huffman codes from
// the root of Huffman Tree.
void printCodes(struct Node* root, string str)
{
    if (!root) return;
 
    if (root->data != '$')
        cout << root->data << ": " << str << "\n";
 
    printCodes(root->left, str + "0");
    printCodes(root->right, str + "1");
}

int main() {
    // Write C++ code here
    string text = "hello world";
    Node* node = buildHuffmanTree(text);
    // printCodes(node, "");
    
    // traverse the Huffman Tree and store Huffman Codes
	// in a map. Also prints them
	unordered_map<char, string> huffmanCode;
	encode(node, "", huffmanCode);
	
// 	printCodes(node, "");
	
// 	cout << "Huffman Codes are :\n" << '\n';
// 	for (auto pair: huffmanCode) {
// 		cout << pair.first << " " << pair.second << '\n';
// 	}

	cout << "\nOriginal string was :\n" << text << '\n';

	// print encoded string
	string str = "";
	for (char ch: text) {
		str += huffmanCode[ch];
	}
    cout << "\nEncoded string is :\n" << str << '\n';
    return 0;
}

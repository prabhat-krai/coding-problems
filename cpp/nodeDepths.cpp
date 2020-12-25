#include<iostream>
using namespace std;

class BinaryTree {
public:
  int value;
  BinaryTree *left;
  BinaryTree *right;

  BinaryTree(int value) {
    this->value = value;
    left = NULL;
    right = NULL;
  }
};

void bfs(BinaryTree *root, int &sum, int depth){
  BinaryTree *currentNode = root;

  if(currentNode == NULL)
    return;

  sum = sum + depth;
  depth++;

  bfs(currentNode->left, sum, depth);
  bfs(currentNode->right, sum, depth);
}

int nodeDepths(BinaryTree *root) {
  int sum = 0;
  int depth = 0;

  bfs(root, sum, depth);
  return sum;
}

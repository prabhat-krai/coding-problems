#include<iostream>
#include<vector>

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

void dfs(BinaryTree *root, int sum, vector<int> &result){
  BinaryTree *currentNode = root;

  if(currentNode == NULL)
    return;
  
  int newSum = sum + currentNode -> value;
  if(currentNode -> left == NULL && currentNode -> right == NULL){
    result.push_back(newSum);
    return;
  }

  dfs(currentNode -> left, newSum, result);
  dfs(currentNode -> right, newSum, result);
}

vector<int> branchSums(BinaryTree *root) {
  vector<int> result;
  dfs(root, 0, result);
  return result;
}

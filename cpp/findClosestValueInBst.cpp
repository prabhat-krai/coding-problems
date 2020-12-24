#include<iostream>

using namespace std;

class BST {
  public:
    int value;
    BST* left;
    BST* right;

    BST(int val);
    BST& insert(int val);
};

int findClosestValueInBstHelper(BST* tree, int target, int closest) {
  BST *currentNode = tree;

  while(currentNode != NULL){
    if(abs(currentNode -> value - target) < abs(target - closest)){
      closest = currentNode -> value;
    }
    if(target < currentNode -> value){
      currentNode = currentNode -> left;
    } else if(target > currentNode -> value){
      currentNode = currentNode -> right;
    } else{
      break;
    }
  }
  return closest;
}

int findClosestValueInBst(BST* tree, int target) {
  return findClosestValueInBstHelper(tree, target, tree->value);
}
using namespace std;

int getNthFib(int n) {
  if (n == 0)
    return 0;
  if (n == 1)
    return 1;

  int first = 0;
  int second = 1;
  int temp;
  for(int i = 0; i <= n - 2;  i++){
    temp = second;
    second = first + second;
    first = temp;
  }
  return second;
}

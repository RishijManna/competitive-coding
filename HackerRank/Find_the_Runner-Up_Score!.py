#Question Link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true


#Python Code:
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    el = max(arr)
    no= arr.count(el)
    for i in range(0,no):
        arr.remove(el)
    print(max(arr))


#---------------------------------------------------------------------------------------------------------

#C code
'''
#include <stdio.h>
int main() {
    // Write C code here
    int arr[] = {5,1,5,2,4};
    int max=0,max2=-1;
    for (int i =0; i<5;i++){
        if (arr[i]>max) {
            max2=max;
            max= arr[i];
        }
        else{
            if (arr[i]<max  && arr[i]>max2){
                max2=arr[i];
            }
        }
    }
    printf("%d",max2);

    return 0;
}
'''

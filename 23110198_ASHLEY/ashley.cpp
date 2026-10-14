#include <stdio.h>
int main(){
    int A;
    printf("Enter the number of elements:");
    scanf("%d",&A);
    int b;
    int arr[A];
    int arr2[A];
    int diff;

    for (int i =0;i< A; i++){
        printf("enter elements of the array :");
        scanf("%i",&b);
        arr[i] = b;
    }
     for(int j; j<A;j++){
        for(int k; k<j; k++){
            if(arr[k] == arr[j]){
                diff= j - k;
                printf("%d",&diff);
            }
            else{
                printf("NONE");
            }
        }
     }
}
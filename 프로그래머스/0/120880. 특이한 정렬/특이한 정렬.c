#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> // qsort, abs, malloc 함수를 사용하기 위해 필요합니다.
#include <string.h> // memcpy 함수를 사용하기 위해 필요합니다.

// qsort의 비교 함수는 파라미터를 2개만 받으므로,
// 기준값 n을 전달하기 위해 정적(static) 변수를 활용합니다.
static int g_n;

// qsort에 전달할 사용자 정의 비교 함수
int compare(const void* a, const void* b) {
    int num1 = *(int*)a;
    int num2 = *(int*)b;

    // n과의 거리(절대값)를 계산합니다.
    int dist1 = abs(num1 - g_n);
    int dist2 = abs(num2 - g_n);

    // 1순위: 거리가 가까운 순서대로 정렬 (오름차순)
    // 두 수의 거리가 같지 않다면, 거리 차이를 반환하여 정렬합니다.
    // (dist1 - dist2)가 음수이면 num1이 앞으로, 양수이면 num2가 앞으로 갑니다.
    if (dist1 != dist2) {
        return dist1 - dist2;
    }
    
    // 2순위: 거리가 같다면, 더 큰 수가 앞에 오도록 정렬 (내림차순)
    // (num2 - num1)이 양수이면 num2가 더 크므로 앞으로, 음수이면 num1이 앞으로 갑니다.
    else {
        return num2 - num1;
    }
}

int* solution(int numlist[], size_t numlist_len, int n) {
    // 1. 결과를 저장할 배열을 동적으로 할당합니다.
    // 배열의 크기는 원본 배열과 같습니다.
    int* answer = (int*)malloc(sizeof(int) * numlist_len);
    // 원본 배열의 내용을 복사합니다. (원본 배열을 직접 수정하지 않기 위함)
    memcpy(answer, numlist, sizeof(int) * numlist_len);

    // 2. 비교 함수에서 사용할 수 있도록 기준값 n을 정적 변수에 저장합니다.
    g_n = n;

    // 3. C 표준 라이브러리의 qsort 함수를 호출하여 배열을 정렬합니다.
    qsort(answer, numlist_len, sizeof(int), compare);

    // 4. 정렬된 배열의 주소를 반환합니다.
    return answer;
}
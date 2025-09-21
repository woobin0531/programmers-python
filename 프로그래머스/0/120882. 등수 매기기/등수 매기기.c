#include <stdio.h>
#include <stdlib.h>

int* solution(int** score, size_t score_rows, size_t score_cols) {
    // 1. 등수를 담을 배열 동적 할당
    int* answer = (int*)malloc(sizeof(int) * score_rows);
    if (answer == NULL) {
        // 메모리 할당 실패 처리
        return NULL;
    }

    // 2. 각 학생의 평균 점수 계산 및 임시 배열에 저장
    double* avg_scores = (double*)malloc(sizeof(double) * score_rows);
    if (avg_scores == NULL) {
        free(answer);
        return NULL;
    }

    for (int i = 0; i < score_rows; i++) {
        avg_scores[i] = (double)(score[i][0] + score[i][1]) / 2.0;
    }

    // 3. 등수 계산
    for (int i = 0; i < score_rows; i++) {
        int rank = 1;
        for (int j = 0; j < score_rows; j++) {
            // 다른 학생과 평균 점수 비교
            if (i != j && avg_scores[j] > avg_scores[i]) {
                rank++;
            }
        }
        answer[i] = rank;
    }

    // 4. 동적으로 할당한 임시 배열 메모리 해제
    free(avg_scores);

    // 5. 등수 배열 반환
    return answer;
}
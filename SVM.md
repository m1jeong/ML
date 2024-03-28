## SVM(Support Vector machine)
> 오 머신러닝 공부좀 했눈데?  
svm = 국경만들기   
머신러닝 알고리즘으로 분류에 사용되는 강력한 알고리즘. 

    
+ 데이터를 분류하기 위해 __decision boundary__ 를 찾는 기법  
+ 주어진 데이터를 고차원 공간으로 매핑한 후, 해당 공간에서 데이터를 가장 잘 구분하는 __hyperplane__ 을 찾음(feature가 3개 이상일 경우의 decision boundary)
+ 데이터의 클래스간 __최대마진__ 을 갖는것을 목표로 함
(margin = 결정경계와 클래스 사이의 거리)
![svm](https://www.reneshbedre.com/assets/posts/svm/svm_linear.webp)
 

----
## sklearn parameter
- gamma
- c(controls tradeoff between smooth decision boundary and classfying training points correctly, C가 크면 더 굴곡지고 C가 작으면 직선에 가깝습니다.)
- 

데이터가 선형적으로 구분되지 않는경우, __커널트릭__ 을 사용하여 데이터를 고차원으로 변환한 후 선형분리함.
커널함수로는,
1. 선형
2. 다항식
3. 가우시안(RBF, Radial Basis Function)    
4. sigmoid
https://velog.io/@everyman123/%EC%84%A0%ED%98%95%EB%8C%80%EC%88%98%EC%9D%98-%EA%B8%B0%EC%B4%88-%EA%B0%9C%EB%85%90%EB%93%A4


SVM의 장점.
1. 다른 분류 알고리즘과 비교하여 일반화 능력이 높음 
2. 과대적합(overfitting) 경향이 적다는 특징
3. SVM은 이상치(outlier)에 대해서도 민감하지 않으며, 비선형 분류 문제에도 효과적으로 적용

SVM의 단점.
1. 큰 규모의 데이터셋에 대해서는 계산 비용이 높음
2. 매개 변수 설정에 민감하다는 단점.
3. 다중 클래스 분류 문제에 직접적으로 적용하기는 어렵기 때문에 일반적으로 이진 분류(binary classification) 문제에 주로 사용



## Adaption mesh
> 이 기능은 무엇일까?


+ 결합하여 사용하면 좋은 case   
    * 셀과 하나 이상의 경계와의 근접성을 바탕으로 경계층 조밀화를 요구하는 메시
    * 충격 또는 커다란 압력 변동이 있는 공기 역학 유동 시뮬레이션
    * 연소 모델을 사용하는 유동
    * 유체 부피(VOF) 다상 모델을 사용하는 유동
    * 오펀 및/또는 도너-리셉터 셀 크기 차이에 의해 부정적인 영향을 받는 오버셋 메시 시뮬레이션
<br>

![open](https://ansyshelp.ansys.com/Views/Secured/corp/v231/en/flu_ug/graphics/g_flu_ug_auto_adaption.png)

#  Predefine Adaption 
> 미리 정의된 기준에 따라 셀을 마킹하기 위해 명명된 표현식을 사용하는것.
1. Boundary Layer
2. Aerodynamics
3. Combusion
4. multiphase
5. Overset

### 1. Boundary Layer
2가지 옵션이 있음.
- Cell distance
- Volume distance    
![boundary](https://ansyshelp.ansys.com/Views/Secured/corp/v231/ko/flu_ug/graphics/g_flu_ug_adapt_bound_cell_dis.png)

### 2. Aerodynamics
- Shock Indicator 및 Density-based
    * density gradient 기준으로 충격을 적절히 처리하기 위해 mesh adapt 할때 사용.    
    * 단, density based 솔버 선택시 사용가능.
- Error-based 및 Pressure Hessian Indicator     
    * 큰 압력변동이 있을것 같은 case
    * 솔루션 오차를 기반.
    * 강도가 서로다른 충격과 후류를 동시에 캡처할 경우
    > 단점 : 광범위한 영역을 대상으로 하기때문에 지나친 조밀화가 이어질 수 있음.    

사용예시)
![density gradient](https://ansyshelp.ansys.com/Views/Secured/corp/v231/ko/flu_ug/graphics/g_flu_ug_adapt_aero_reg.png)

### 3. Combustion - Flame indicator

1. include Votex Indicator 옵션 : 와동 크기를 지정.
2. Spark Region refinement 옵션 : 구형 스파크 region의 반경 및 적용 시간 등을 적용해서 조밀화를 진행.

3. solution>cellresiters>temperature_refinement>Edit...
온도에 대한 STD LIMIT 보다 크면 REMARK, Adaption 하겠다! 
![flame](https://ansyshelp.ansys.com/Views/Secured/corp/v231/en/flu_ug/graphics/g_flu_ug_adapt_com_reg.png)



### 4. multiphase
> vof 모델 활성화시 사용

![expression](https://ansyshelp.ansys.com/Views/Secured/corp/v231/ko/flu_ug/graphics/g_flu_ug_adapt_vof_exp.png)
- __Volume of Fluid:__ 표준 VOF 시뮬레이션에 적합합니다.

- __VOF-to-DPM [Generic]:__ VOF-DPM 모델 전환 메커니즘을 사용하는 경우에 적합합니다. 결과 어댑션 기준은 상당히 간단한 셀 레지스터를 통해 정의됩니다.

- __VOF-to-DPM [Advanced]:__ VOF-DPM 모델 전환 메커니즘을 사용하는 경우에 적합합니다. 결과 어댑션 기준은 셀 레지스터를 사용하는 복잡한 표현식과 정의에 필요한 매개변수를 통해 정의됩니다.

![vof_Criteria](https://ansyshelp.ansys.com/Views/Secured/corp/v231/ko/flu_ug/graphics/flu_ug_adapt_crit_set.png)

### 5. overset
이동하는 메쉬나 동적메쉬
____
```md
셀 레지스터(셀 마킹)의 수단
- Refinement Criterion
> 조밀화
- Coarsening Criterion
> 조대화

```

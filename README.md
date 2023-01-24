# 마니또-마로 md 파일 만들어 주는 코드

## 소개
제목 그대로의 코드 입니다.

그룹내에서 또는 교우 간에 이벤트로 마니또 게임을 할 때 ***Argument*** 만 바꾸어 활용하실 수 있습니다.

코드 안에 주석으로 ***생각해볼 거리*** 를 넣어보았습니다.
해당 줄 이외의 소스코드에도 의미 없는 줄은 없기 때문에
***왜 이렇게 짰을까*** 를 생각해보면서 공부해보셔도 좋을 것 같습니다.

예를 들어, txt 파일이 아닌 ***md 파일*** 을 생성하는 이유는 글씨에 ***기울기와 강조효과*** 를 주고 싶었기 때문입니다. 

md 파일은 ***vscode*** 로도 열어볼 수 있으며, ***Markdown All in One*** 이라는 vscode 내 확장프로그램을 통해 Markdown 문법이 적용된 것을 확인 해보실 수 있습니다.

## 함수
- **maro_generator(** *[마니또 리스트]* **)**

        마로 리스트를 생성하여 반환합니다.



- **create__manito_maro_md(** *[마니또 리스트]* **)**

        maro_generator를 이용해 마로 리스트를 생성한 뒤, 
        아래 예시와 같은 Markdown 파일을 만듭니다.
    ---
    파일이름 : ***마니또 이름***

    ---
    당신의 마로는 ***마로 이름*** 입니다.

    ***마로 이름*** 의 마니또(수호천사)가 되어주세요.

    ---

import random

def maro_generator(manito):
    maro=[group for group in manito] # 무슨 의미일까, 왜 이렇게 했을까 생각해봅시다.
    random.shuffle(maro) # 여기서 return 하지 않았을까 생각해봅시다.
    maro_dict = {}
    for i in range(len(manito)):
        if ( maro_dict.get(maro[i]) == manito[i] ) or manito[i] == maro[i]: # 무슨 의미일까, 왜 이렇게 했을까 생각해봅시다.
            return maro_generator(manito)
        else:
            maro_dict[manito[i]] = maro[i]
    return maro

def create__manito_maro_md(manito):
    maro = maro_generator(manito)
    for i in range(len(manito)):
        f =  open(f"{manito[i]}.md", "w", encoding="utf-8")
        f.write(f"당신의 마로는 ***{maro[i]}*** 입니다. \n***{maro[i]}*** 의 마니또(수호천사)가 되어주세요.")
        f.close()

create__manito_maro_md( ["1번 그룹", "2번 그룹", "3번 그룹", "4번 그룹","5번 그룹","6번 그룹"] )
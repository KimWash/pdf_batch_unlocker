# 교수님 PDF좀 그냥 올려주세요
교수님이 PDF를 자꾸 비밀번호를 걸어서 올리시네요. 불편한데..

그럼 그냥 일괄로 잠금해제 해버립시다

## 사용법
```bash
pip install -r requirements.txt # 실행에 필요한 pikepdf, argparse 를 깔아줍니다. 
python main.py --password PASSWORD --src SOURCE_DIRECTORY --dst DESTINATION_DIRECTORY
```
- `src`와 `dst`의 기본값은 `pdf_files`, `result` 입니다. `pdf_files` 디렉토리에 암호가 걸린 파일을 넣으면 `result` 폴더에서 확인하실 수 있어요!
- 현재는 상대 경로만 지원합니다. 귀찮으니까 누가 절대 경로 대응시켜서 PR좀 날려주세요.
- 이것도 못 쓰시면... 아시죠..?
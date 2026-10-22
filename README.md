# WON 플러스원 | 예선 제안서 작업 공간

목표: 우리은행 X SSAFY 우리WON뱅킹 아이디어 경진대회 예선용 5페이지 PDF 제작.
현재 상태: 협업용 뼈대. 서비스 아이디어·팀원 이름·실증 근거 미확정. 제출본 아님.

## 시작 순서
1. docs/CONTEST_BRIEF.md에서 포스터 조건 확인
2. docs/IDEA_BRIEF.md에서 주제 하나와 핵심 문제 확정
3. docs/WORK_GUIDE.md 기준으로 A/B/C 역할 배정
4. slides/storyboard.md와 slides/content.json 작성
5. python scripts/build_pdf.py 실행 후 output/pdf/proposal_skeleton.pdf 검수

## 구성
- assets/originals/: 포스터·팀 로고 원본 사본
- docs/: 디자인 기준, 아이디어 정의, 협업 지침
- data/processed/: 포스터 전사 데이터·근거/주장 관리 양식
- data/raw/: 이후 수집할 인터뷰·공개자료 원본
- slides/: 5페이지 스토리보드와 편집 가능한 내용 JSON
- scripts/build_pdf.py: 내용 JSON으로 PDF 재생성
- output/pdf/proposal_skeleton.pdf: 정확히 5페이지인 작성용 뼈대

현재 앱 기능, 경쟁 서비스, 시장 규모는 조사하지 않은 상태. 빈 양식을 실제 조사 데이터로 해석하지 않음.
포스터 원본 수정 금지. Git 커밋·푸시·외부 공유는 별도 수행 필요.

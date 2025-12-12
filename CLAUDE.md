# 프로젝트: Lumina AI (주식 투자 플랫폼)

## 아키텍처 원칙
- **패턴**: Django MTV (Model-Template-View) 모놀리식 아키텍처
- **AI 엔진**: Scikit-learn (Linear Regression) 기반 예측 모델
- **Frontend**: Django Templates + TailwindCSS (CDN) + Chart.js
- **데이터베이스**: SQLite (개발용), PostgreSQL (운영 고려)

## 코딩 규칙
- **언어 버전**: Python 3.11+
- **스타일**: PEP 8 준수
- **타입 힌트**: 모든 함수 및 메서드 시그니처에 Type Hint 사용 필수
    - 예: `def predict(self, data: pd.DataFrame) -> float:`
- **문서화**: Docstring을 사용하여 클래스와 함수의 목적 명시
- **환경 변수**: 민감한 정보(API Key 등)는 `.env` 파일로 관리 및 `python-dotenv`로 로드

## 테스트 요구 사항
- `python manage.py test` 명령어로 테스트 실행 가능해야 함
- 데이터 처리 및 모델 예측 로직에 대한 단위 테스트 포함

## 보안 고려 사항
- API 키는 절대 코드에 하드코딩하지 않음
- `DEBUG=True`는 개발 환경에서만 사용

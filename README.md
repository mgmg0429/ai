# Lumina AI - AI 기반 주식 투자 플랫폼 

## 소개 

Lumina AI는 최첨단 인공지능 기술을 활용한 주식 투자 플랫폼입니다. 실시간 시장 분석, 자동 매매, 포트폴리오 관리 등 투자자를 위한 종합적인 솔루션을 제공합니다.

### 주요 기능 

- **실시간 AI 예측**
  - 빅데이터 기반의 AI가 실시간으로 시장을 분석
  - 98.7% 예측 정확도
  - 실시간 매매 신호 생성

- **자동 매매 시스템**
  - 24시간 자동 모니터링
  - 설정된 전략에 따른 자동 매매 실행
  - 리스크 관리 시스템 탑재

- **대시보드 & 분석**
  - 직관적인 실시간 차트
  - 포트폴리오 성과 분석
  - 시장 동향 및 인사이트 제공

## 기술 스택 

- **Frontend**: HTML5, CSS3, JavaScript, TailwindCSS
- **Backend**: Python, Django
- **AI/ML**: TensorFlow, Scikit-learn
- **API**: 한국투자증권 API
- **차트**: TradingView, Chart.js
- **실시간 데이터**: WebSocket
  
## 설치 방법 

1. 저장소 클론

git clone https://github.com/mgmg0429/ai

2. 의존성 설치

pip install -r requirements.txt

## API 키 설정 

한국투자증권 API 사용을 위해 다음 정보가 필요합니다:
- API Key
- API Secret
- 계좌번호

`koreainvestment.key` 파일에 다음 형식으로 저장:

```
your_api_key
your_api_secret
your_account_number
```

## 라이선스 

이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 기여하기 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

# WarmCoolServer

이 프로젝트는 [WarmCoolModel](https://github.com/anyoungjin20040106/WarmCoolModel)을 활용하여 피부 톤 분류 기능을 API 형태로 제공하는 FastAPI 서버입니다.

## 프로젝트 개요

- **목적**: 피부 톤 분류 모델을 API 서버로 구현하여 Unity 애플리케이션에서 활용 가능하도록 제공
- **사용 기술**:
  - 웹 프레임워크: FastAPI
  - 프로그래밍 언어: Python

## 주요 기능

- **이미지 업로드**: 사용자 이미지를 서버에 업로드
- **피부 톤 분류**: 업로드된 이미지를 WarmCoolModel을 통해 분석하여 피부 톤 분류
- **결과 반환**: 분류된 결과를 JSON 형태로 반환

## 주요 파일 구조

```
.
├── main.py              # FastAPI 서버 메인 파일
├── model.keras          # WarmCoolModel에서 학습된 모델 파일
├── requirements.txt     # 필요한 패키지 목록
├── img     # 가상 메이크업 텍스쳐가 들어간 폴더
└── README.md            # 프로젝트 설명
```

## 설치 및 실행 방법

1. **필요한 패키지 설치**:

   ```bash
   pip install -r requirements.txt
   ```
2. **서버 실행**:

   ```bash
   uvicorn main:app --reload
   ```
3. **API 사용**:

   - **엔드포인트**: `/predict`
   - **메서드**: POST
   - **파라미터**:
     - `image`: 사용자 이미지 파일
   - **응답**:
     - `tone`: 분류된 피부 톤 (예: '쿨톤', '웜톤')

---

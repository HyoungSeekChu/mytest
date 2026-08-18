# mytest

`mytest`는 FastAPI와 Uvicorn으로 만든 간단한 Python Web API입니다.

## 요구 사항

- Python 3.11 이상
- [uv](https://docs.astral.sh/uv/)

## 설치

Windows PowerShell에서 다음 명령을 실행합니다.

```powershell
uv venv
uv sync --all-groups
.\.venv\Scripts\Activate.ps1
```

PowerShell 실행 정책으로 활성화가 차단되면 현재 프로세스에만 허용한 뒤 다시 실행합니다.

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## 실행

가상 환경이 활성화된 상태에서 Uvicorn을 포트 8000으로 실행합니다.

```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

- API: http://127.0.0.1:8000/
- API 문서: http://127.0.0.1:8000/docs

## 테스트

```powershell
pytest
```

작업을 마치려면 가상 환경을 비활성화합니다.

```powershell
deactivate
```

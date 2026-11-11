# macOS Codex 설치 및 확인

사내 설치 정책 확인 후, 터미널에서 아래 명령을 차례로 실행한다.

    command -v codex
    command -v uvx
    codex mcp add --help
    codex mcp list
    codex mcp add korean-tax-calc -- uvx korean-tax-calc-mcp@0.31.0
    codex mcp list

이는 확인 시점 버전 0.31.0의 설치 예시이며 실제 도구·법령 지원 연도 검증이 필요하다. UPSTAGE_API_KEY는 기본 설정하지 않는다.

저장소 프로젝트에서 스킬은 .agents/skills/snu-research-tax 에 둔다. 다른 프로젝트와 공용으로 쓰려면 스킬 폴더 전체를 ~/.agents/skills/snu-research-tax 에 복사한다. 이 스킬 설치만으로 MCP가 자동 등록되지는 않는다.

스킬 루트에서 테스트:

    python3 -m unittest discover -s scripts -p 'test_*.py' -v
    python3 scripts/reconcile.py --gross 200000 --national-tax 16000 --local-tax 1600

가상 테스트 입력만 사용한다.

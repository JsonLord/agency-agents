#!/usr/bin/env bash
# Duplicate normalized names must not silently overwrite one agent's output.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
scratch="$(mktemp -d)"
trap 'rm -rf "$scratch"' EXIT

mkdir -p "$scratch/repo/scripts" "$scratch/repo/agents/discovery" "$scratch/output/gemini-cli"
cp "$SCRIPT_DIR/convert.sh" "$SCRIPT_DIR/lib.sh" "$scratch/repo/scripts/"

cat > "$scratch/repo/agents/discovery/first.md" <<'EOF'
---
name: Dev Ops
description: First agent
color: blue
---
# First agent
EOF
cat > "$scratch/repo/agents/discovery/second.md" <<'EOF'
---
name: Dev/Ops
description: Second agent
color: red
---
# Second agent
EOF

printf 'keep existing output\n' > "$scratch/output/gemini-cli/sentinel"
if AGENT_DIRS_OVERRIDE=discovery AGENT_DIRS_OVERRIDE=discovery bash "$scratch/repo/scripts/convert.sh" --tool gemini-cli --out "$scratch/output" > "$scratch/log" 2>&1; then
  echo "FAIL: converter accepted two agents with the same output slug"
  exit 1
fi
grep -q "duplicate agent slug 'dev-ops'" "$scratch/log"
grep -q 'agents/discovery/first.md' "$scratch/log"
grep -q 'agents/discovery/second.md' "$scratch/log"
[[ "$(cat "$scratch/output/gemini-cli/sentinel")" == 'keep existing output' ]]
echo "PASS: duplicate slug refused before existing output changed"

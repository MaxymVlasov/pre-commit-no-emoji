# pre-commit-no-emoji

Simple [pre-commit.com](https://pre-commit.com) hook, which will remove emoji from codebase.

## Usage

Add to `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/MaxymVlasov/pre-commit-no-emoji
    rev: v1.0.0
    hooks:
      - id: remove-emoji-from-codebase
```

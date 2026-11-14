---
declaration: definition
origin: cited
lean: TailoredGameValue.TailoredHaltingReduction
statement: formalized
---

# The tailored halting reduction, as a proposition

The proposition that the halting problem reduces to tailored games: the statement of Theorem [$\mathrm{TMIP}^* = \mathrm{RE}$; II:1505, Theorem 7.4 of (BCLV24)](thm-tmip-re.md), written in `MIPRE/TailoredGameValue.lean` on top of Mathlib alone. It is a definition, so that the conditional theorem proving it from a compression (Theorem [Halting from tailored compression; II:1887–2066](../part-02/thm-tailored-halting.md)) can name it while Theorem [$\mathrm{TMIP}^* = \mathrm{RE}$; II:1505, Theorem 7.4 of (BCLV24)](thm-tmip-re.md) awaits that compression.

## Depends on

- [Tailored game descriptions, standalone; II:1243, II:1279](def-tailored-game-data.md)

## Lean

Formalized as [`TailoredGameValue.TailoredHaltingReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredHaltingReduction).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 473](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L473)

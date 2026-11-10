---
declaration: theorem
origin: cited
lean: WeierstrassCurve.fifteenIsogenyClassification
statement: formalized
proof: formalized
---

# WeierstrassCurve.fifteenIsogenyClassification

```lean
open WeierstrassCurve
theorem WeierstrassCurve.fifteenIsogenyClassification (W : WeierstrassCurve ℤ) (hΔ : W.Δ ≠ 0) (h3 : ¬ W.ModRepIsIrreducible 3) (h5 : ¬ W.ModRepIsIrreducible 5) : (W.c₄ : ℚ) ^ 3 / (W.Δ : ℚ) = -25 / 2 ∨ (W.c₄ : ℚ) ^ 3 / (W.Δ : ℚ) = -349938025 / 8 ∨ (W.c₄ : ℚ) ^ 3 / (W.Δ : ℚ) = -121945 / 32 ∨ (W.c₄ : ℚ) ^ 3 / (W.Δ : ℚ) = 46969655 / 32768
```

*Quoted from [Theorems/Thm_WeierstrassCurve_fifteenIsogenyClassification.lean, line 8](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_fifteenIsogenyClassification.lean#L8) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

PROOF-PATH.md names it in [4. Modularity](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Lean

`WeierstrassCurve.fifteenIsogenyClassification`, stated in [Theorems/Thm_WeierstrassCurve_fifteenIsogenyClassification.lean, line 8](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_fifteenIsogenyClassification.lean#L8) and proved in [P2M/Sol/S_WeierstrassCurve_fifteenIsogenyClassification.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_fifteenIsogenyClassification.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.fifteenIsogenyClassification` in Theorems/Thm_WeierstrassCurve_fifteenIsogenyClassification.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_fifteenIsogenyClassification.lean#L8)
- [Proof of `WeierstrassCurve.fifteenIsogenyClassification` in P2M/Sol/S_WeierstrassCurve_fifteenIsogenyClassification.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_fifteenIsogenyClassification.lean)
- [The repository's documentation page for `WeierstrassCurve.fifteenIsogenyClassification`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.fifteenIsogenyClassification)

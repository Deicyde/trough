---
declaration: theorem
origin: cited
lean: WeierstrassCurve.modThreeOrFiveIrreducible
statement: formalized
proof: formalized
---

# WeierstrassCurve.modThreeOrFiveIrreducible

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
open CuspForm ModularFormClass UpperHalfPlane
theorem WeierstrassCurve.modThreeOrFiveIrreducible (W : WeierstrassCurve ℤ) (hΔ : W.Δ ≠ 0) (hW : W.IsSemistableModel) : W.ModRepIsIrreducible 3 ∨ W.ModRepIsIrreducible 5
```

*Quoted from [Theorems/Thm_WeierstrassCurve_modThreeOrFiveIrreducible.lean, line 15](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_modThreeOrFiveIrreducible.lean#L15) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “3-5 trick”, “X0(15)”, “15-isogeny”.

PROOF-PATH.md names it in [4. Modularity](README.md).

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [WeierstrassCurve.fifteenIsogenyClassification](weierstrasscurve-fifteenisogenyclassification.md)

## Lean

`WeierstrassCurve.modThreeOrFiveIrreducible`, stated in [Theorems/Thm_WeierstrassCurve_modThreeOrFiveIrreducible.lean, line 15](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_modThreeOrFiveIrreducible.lean#L15) and proved in [P2M/Sol/S_WeierstrassCurve_modThreeOrFiveIrreducible.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_modThreeOrFiveIrreducible.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.modThreeOrFiveIrreducible` in Theorems/Thm_WeierstrassCurve_modThreeOrFiveIrreducible.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_modThreeOrFiveIrreducible.lean#L15)
- [Proof of `WeierstrassCurve.modThreeOrFiveIrreducible` in P2M/Sol/S_WeierstrassCurve_modThreeOrFiveIrreducible.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_modThreeOrFiveIrreducible.lean)
- [The repository's documentation page for `WeierstrassCurve.modThreeOrFiveIrreducible`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.modThreeOrFiveIrreducible)

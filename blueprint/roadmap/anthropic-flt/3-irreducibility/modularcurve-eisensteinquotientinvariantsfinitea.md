---
declaration: theorem
origin: cited
lean: ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar
statement: formalized
proof: formalized
---

# ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar

```lean
open ModularCurve AlgebraicCurve
theorem ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar (p : ℕ) [Fact p.Prime]
    (hcomm : HeckeOperatorsCommuteBar p) :
    EisensteinQuotientInvariantsFiniteAt p (heckeModuleBar p)
```

*Quoted from [Theorems/Thm_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean, line 61](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean#L61) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [ModularForm.S2_Gamma0_one_eq_zero](../6-s2-0-2-0/modularform-s2-gamma0-one-eq-zero.md)

## Lean

`ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar`, stated in [Theorems/Thm_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean, line 61](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean#L61) and proved in [P2M/Sol/S_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar` in Theorems/Thm_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean#L61)
- [Proof of `ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar` in P2M/Sol/S_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_ModularCurve_eisensteinQuotientInvariantsFiniteAt_heckeModuleBar.lean)
- [The repository's documentation page for `ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#ModularCurve.eisensteinQuotientInvariantsFiniteAt_heckeModuleBar)

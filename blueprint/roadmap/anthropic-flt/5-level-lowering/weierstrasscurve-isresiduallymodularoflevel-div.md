---
declaration: theorem
origin: cited
lean: WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf
statement: formalized
proof: formalized
---

# WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf

```lean
set_option autoImplicit false

open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point

theorem WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf
    (p : ℕ) [Fact p.Prime] (_hp2 : p ≠ 2) (W : WeierstrassCurve ℤ) (_hΔ : W.Δ ≠ 0)
    (_hW : W.IsSemistableModel)
    (hcard₁ : Nat.card (Submodule.torsionBy ℤ
      ((W.map (Int.castRingHom ℚ))⁄(AlgebraicClosure ℚ)).Point p) = p ^ 2)
    (hker : GaloisFactorsThroughFiniteLevel
      (WeierstrassCurve.Affine.Point.galoisRepModuleEnd (K := AlgebraicClosure ℚ) ℚ
        (W.map (Int.castRingHom ℚ)) p))
    (_hirr : W.ModRepIsIrreducible p) (M q : ℕ) (hq : q.Prime) (hqp : q ≠ p)
    (hqM : q ∣ M) (hq2 : ¬ q ^ 2 ∣ M) (hM : Squarefree M)
    (hunr : ((W.map (Int.castRingHom ℚ)).residualGaloisRepOf p hcard₁ hker).IsUnramifiedAt q)
    (hres : W.IsResiduallyModularOfLevel p M) :
    W.IsResiduallyModularOfLevel p (M / q)
```

*Quoted from [Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean, line 87](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean#L87) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [ResidualGaloisRep.isAbsolutelyIrreducible_of_isIrreducible_of_isOdd](../4-modularity/residualgaloisrep-isabsolutelyirreducible-of-isi.md)

## Lean

`WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf`, stated in [Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean, line 87](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean#L87) and proved in [P2M/Sol/S_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf` in Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean#L87)
- [Proof of `WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf` in P2M/Sol/S_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf.lean)
- [The repository's documentation page for `WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.isResiduallyModularOfLevel_div_of_isUnramifiedAt_sqf)

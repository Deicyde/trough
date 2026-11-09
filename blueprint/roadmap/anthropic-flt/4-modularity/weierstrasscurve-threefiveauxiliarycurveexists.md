---
declaration: theorem
origin: cited
lean: WeierstrassCurve.threeFiveAuxiliaryCurveExists
statement: formalized
proof: formalized
---

# WeierstrassCurve.threeFiveAuxiliaryCurveExists

```lean
open WeierstrassCurve WeierstrassCurve.Affine WeierstrassCurve.Affine.Point
theorem WeierstrassCurve.threeFiveAuxiliaryCurveExists (W : WeierstrassCurve ℤ) (hΔ : W.Δ ≠ 0) (hW : W.IsSemistableModel) (h5 : W.ModRepIsIrreducible 5) : ∃ W' : WeierstrassCurve ℤ, W'.Δ ≠ 0 ∧ W'.IsSemistableModel ∧ W'.ModRepIsIrreducible 3 ∧ ∃ φ : Submodule.torsionBy ℤ ((W.map (Int.castRingHom ℚ))⁄(AlgebraicClosure ℚ)).Point (5 : ℕ) ≃ₗ[ZMod 5] Submodule.torsionBy ℤ ((W'.map (Int.castRingHom ℚ))⁄(AlgebraicClosure ℚ)).Point (5 : ℕ), ∀ (σ : AlgebraicClosure ℚ ≃ₐ[ℚ] AlgebraicClosure ℚ) (x : Submodule.torsionBy ℤ ((W.map (Int.castRingHom ℚ))⁄(AlgebraicClosure ℚ)).Point (5 : ℕ)), φ (σ • x) = σ • φ x
```

*Quoted from [Theorems/Thm_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean, line 8](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean#L8) of [anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem) at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), Apache-2.0: the file's text from the end of its imports and `attribute` lines to the top-level `:=`.*

Aliases on the repository's web pages: “3-5 switch”, “Rubin-Silverberg family”.

## Depends on

The repository's citation graph records the theorems each proof cites, not what statements use, so no statement dependencies are listed.

## Proof depends on

- [WeierstrassCurve.exists_forall_not_isRoot_Psi3_specialization](weierstrasscurve-exists-forall-not-isroot-psi3-s.md)
- [WeierstrassCurve.galoisRepIsIrreducible_three_of_forall_eval_Psi3_ne_zero](weierstrasscurve-galoisrepisirreducible-three-of.md)

## Lean

`WeierstrassCurve.threeFiveAuxiliaryCurveExists`, stated in [Theorems/Thm_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean, line 8](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean#L8) and proved in [P2M/Sol/S_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean). Read at commit [6e837e75](https://github.com/anthropics/fermats-last-theorem/tree/6e837e75355538c7f80bab5b956861e86c4eacc2), without running Lean.

## Sources

- [Statement of `WeierstrassCurve.threeFiveAuxiliaryCurveExists` in Theorems/Thm_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/Theorems/Thm_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean#L8)
- [Proof of `WeierstrassCurve.threeFiveAuxiliaryCurveExists` in P2M/Sol/S_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean](https://github.com/anthropics/fermats-last-theorem/blob/6e837e75355538c7f80bab5b956861e86c4eacc2/P2M/Sol/S_WeierstrassCurve_threeFiveAuxiliaryCurveExists.lean)
- [The repository's documentation page for `WeierstrassCurve.threeFiveAuxiliaryCurveExists`](https://tianyipeng.github.io/fermats-last-theorem/thm.html#WeierstrassCurve.threeFiveAuxiliaryCurveExists)

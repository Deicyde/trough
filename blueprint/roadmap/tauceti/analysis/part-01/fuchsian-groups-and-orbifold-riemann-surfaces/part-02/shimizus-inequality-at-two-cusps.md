---
declaration: theorem
origin: cited
lean: TauCeti.Subgroup.CuspDatum.im_scaling_smul_smul_mul_im_scaling_smul_le
statement: formalized
proof: formalized
---

# Shimizu's inequality at two cusps

Let `D` and `D'` be normalized cusp data of a discrete
`Γ ≤ PSL(2, ℝ)`. If `g ∈ Γ` does not carry the cusp of `D'` to the cusp of `D`, then the height of
`g • z` above the cusp of `D` and the height of `z` above the cusp of `D'`, each measured in the
scaling coordinate of its datum, have product at most `D.width * D'.width`.

This is Shimizu's lemma (`Subgroup.im_smul_mul_im_le_abs_mul_of_upperRightHom_mem`) for the
conjugate group `σ Γ σ⁻¹`, which contains the translation by `D.width`, applied to `σ g σ'⁻¹`,
which conjugates the translation by `D'.width` into it.

```lean
TauCeti.Subgroup.CuspDatum.im_scaling_smul_smul_mul_im_scaling_smul_le
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} (D : Γ.CuspDatum)
  [DiscreteTopology ↥Γ] (D' : Γ.CuspDatum) {g : ↥Γ} (hg : g • D'.cusp ≠ D.cusp)
  (z : UpperHalfPlane) : (D.scaling • g • z).im * (D'.scaling • z).im ≤ D.width * D'.width
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shimizu's lemma](shimizus-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Subgroup.CuspDatum.im_scaling_smul_smul_mul_im_scaling_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Cusp/Horodisc.html#TauCeti.Subgroup.CuspDatum.im_scaling_smul_smul_mul_im_scaling_smul_le).

## Sources

- [Tau Ceti documentation: `TauCeti.Subgroup.CuspDatum.im_scaling_smul_smul_mul_im_scaling_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Cusp/Horodisc.html#TauCeti.Subgroup.CuspDatum.im_scaling_smul_smul_mul_im_scaling_smul_le)
- [Source of `TauCeti.Subgroup.CuspDatum.im_scaling_smul_smul_mul_im_scaling_smul_le` in TauCeti/Analysis/Complex/Fuchsian/Cusp/Horodisc.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/Cusp/Horodisc.lean#L219)

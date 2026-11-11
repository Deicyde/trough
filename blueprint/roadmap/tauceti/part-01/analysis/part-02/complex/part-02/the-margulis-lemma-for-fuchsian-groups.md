---
declaration: theorem
origin: cited
lean: Subgroup.conj_eq_or_conj_eq_inv_of_dist_le
statement: formalized
proof: formalized
---

# The Margulis lemma for Fuchsian groups

Let `Γ ≤ PSL(2, ℝ)` be a discrete subgroup and let
`g, h ∈ Γ` both move a point `z ∈ ℍ` a distance at most `1 / 4`. If `g` fixes no point of `ℍ`, that
is, if `g` is parabolic or hyperbolic, then `h g h⁻¹ = g` or `h g h⁻¹ = g⁻¹`.

```lean
Subgroup.conj_eq_or_conj_eq_inv_of_dist_le
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ]
  {g h : Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ} (hg : g ∈ Γ) (hh : h ∈ Γ)
  (hfix : ∀ (w : UpperHalfPlane), g • w ≠ w) {z : UpperHalfPlane} (hgz : dist (g • z) z ≤ 1 / 4)
  (hhz : dist (h • z) z ≤ 1 / 4) : h * g * h⁻¹ = g ∨ h * g * h⁻¹ = g⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jørgensen's inequality](jrgensens-inequality.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.conj_eq_or_conj_eq_inv_of_dist_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Margulis.html#Subgroup.conj_eq_or_conj_eq_inv_of_dist_le).

## Sources

- [Tau Ceti documentation: `Subgroup.conj_eq_or_conj_eq_inv_of_dist_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Margulis.html#Subgroup.conj_eq_or_conj_eq_inv_of_dist_le)
- [Source of `Subgroup.conj_eq_or_conj_eq_inv_of_dist_le` in TauCeti/Analysis/Complex/Fuchsian/Margulis.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Fuchsian/Margulis.lean#L91)

---
declaration: theorem
origin: cited
lean: ModularForm.abscissaOfAbsConv_qExpansion_coeff_le
statement: formalized
proof: formalized
---

# Hecke's abscissa bound for modular forms

the Dirichlet series of the `q`-expansion
coefficients converges absolutely for `Re s > k + 1` (from `aₙ = O(nᵏ)` for `k ≥ 0`; in negative
weight the form is zero).

```lean
ModularForm.abscissaOfAbsConv_qExpansion_coeff_le.{u_1} {k : ℤ} {Γ : Subgroup (GL (Fin 2) ℝ)}
  [Γ.IsArithmetic] {F : Type u_1} [FunLike F UpperHalfPlane ℂ] [ModularFormClass F Γ k] (f : F) :
  (LSeries.abscissaOfAbsConv fun n =>
      (PowerSeries.coeff n) (UpperHalfPlane.qExpansion Γ.strictWidthInfty ⇑f)) ≤
    ↑↑k + 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ModularForm.abscissaOfAbsConv_qExpansion_coeff_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LFunction/Basic.html#ModularForm.abscissaOfAbsConv_qExpansion_coeff_le).

## Sources

- [Tau Ceti documentation: `ModularForm.abscissaOfAbsConv_qExpansion_coeff_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/LFunction/Basic.html#ModularForm.abscissaOfAbsConv_qExpansion_coeff_le)
- [Source of `ModularForm.abscissaOfAbsConv_qExpansion_coeff_le` in TauCeti/NumberTheory/ModularForms/LFunction/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/LFunction/Basic.lean#L92)

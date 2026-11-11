---
declaration: theorem
origin: cited
lean: TauCeti.exists_eq_smul_linearIsometry_add_or_inversion_of_conformalAt
statement: formalized
proof: formalized
---

# Liouville's theorem on conformal maps

Let `E` and `F` be real inner product spaces of
the same finite dimension `n ≥ 3`, and let `f : E → F` be `C³` and conformal at every point of a
connected open set `U`. Then `f` is the restriction to `U` of a Möbius transformation: there are
`r > 0`, a linear isometry `A` and a vector `a` such that either `f x = r • A x + a` on `U`, or
`f x = r • A (inversion b 1 x) + a` on `U` for some point `b ∉ U`.

```lean
TauCeti.exists_eq_smul_linearIsometry_add_or_inversion_of_conformalAt.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup F] [InnerProductSpace ℝ F] [FiniteDimensional ℝ F] {f : E → F} {U : Set E}
  (hE : 3 ≤ Module.finrank ℝ E) (hEF : Module.finrank ℝ E = Module.finrank ℝ F)
  (hf : ContDiffOn ℝ 3 f U) (hU : IsOpen U) (hU' : IsConnected U)
  (hconf : ∀ x ∈ U, ConformalAt f x) :
  ∃ r A a,
    0 < r ∧
      ((∀ x ∈ U, f x = r • A x + a) ∨
        ∃ b ∉ U, ∀ x ∈ U, f x = r • A (EuclideanGeometry.inversion b 1 x) + a)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eq_smul_linearIsometry_add_or_inversion_of_conformalAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Conformal/Liouville.html#TauCeti.exists_eq_smul_linearIsometry_add_or_inversion_of_conformalAt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eq_smul_linearIsometry_add_or_inversion_of_conformalAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Conformal/Liouville.html#TauCeti.exists_eq_smul_linearIsometry_add_or_inversion_of_conformalAt)
- [Source of `TauCeti.exists_eq_smul_linearIsometry_add_or_inversion_of_conformalAt` in TauCeti/Analysis/Calculus/Conformal/Liouville.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Conformal/Liouville.lean#L489)

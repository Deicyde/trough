---
declaration: theorem
origin: cited
lean: TauCeti.mem_exactCompactlySupportedForms_one_real, TauCeti.mem_exactCompactlySupportedForms_iff_integralTopForm_eq_zero_normedSpace, TauCeti.mem_exactCompactlySupportedForms_of_integralTopForm_eq_zero_normedSpace
statement: formalized
proof: formalized
---

# The compactly supported Poincaré lemma on the line

A compactly supported `1`-form on `ℝ`
(automatically closed, as every `1`-form on the line is) whose integral against Lebesgue measure
vanishes is the exterior derivative of a compactly supported function.

```lean
TauCeti.mem_exactCompactlySupportedForms_one_real
  {φ : TauCeti.SmoothForm (modelWithCornersSelf ℝ ℝ) ℝ ℝ 1}
  (hφ : φ ∈ TauCeti.compactlySupportedForms (modelWithCornersSelf ℝ ℝ) ℝ 1)
  (h : (∫ (t : ℝ), (↑φ t) fun x => 1) = 0) :
  φ ∈ TauCeti.exactCompactlySupportedForms (modelWithCornersSelf ℝ ℝ) ℝ 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The de Rham cohomology of a normed space vanishes in positive degrees](the-de-rham-cohomology-of-a-normed-space-vanishe.md)
- [The fundamental theorem of calculus for line integrals, for a `C¹` form `ψ` of degree zero](the-fundamental-theorem-of-calculus-for-line-int.md)
- [Homotopy invariance of de Rham cohomology](homotopy-invariance-of-de-rham-cohomology.md)
- [The Mayer–Vietoris short exact sequence of de Rham complexes](the-mayer-vietoris-short-exact-sequence-of-de-rh.md)
- [The Poincaré lemma on manifolds](../../manifold/part-02/the-poincare-lemma-on-manifolds.md)
- [TauCeti.compactlySupportedDeRhamCohomology](tauceti-compactlysupportedderhamcohomology.md)
- [TauCeti.compactlySupportedDeRhamCohomology.integral](tauceti-compactlysupportedderhamcohomology-integ.md)
- [TauCeti.pathIntegral](tauceti-pathintegral.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_exactCompactlySupportedForms_one_real`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/RealLine.html#TauCeti.mem_exactCompactlySupportedForms_one_real).

## Other forms

**The compactly supported Poincaré lemma in top degree, as a characterization.** Formalized in Tau Ceti as [`TauCeti.mem_exactCompactlySupportedForms_iff_integralTopForm_eq_zero_normedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Euclidean.html#TauCeti.mem_exactCompactlySupportedForms_iff_integralTopForm_eq_zero_normedSpace).

```lean
TauCeti.mem_exactCompactlySupportedForms_iff_integralTopForm_eq_zero_normedSpace.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {n : ℕ}
  (o : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) E (Fin n))
  {φ : TauCeti.SmoothForm (modelWithCornersSelf ℝ E) E ℝ n}
  (hφ : φ ∈ TauCeti.compactlySupportedForms (modelWithCornersSelf ℝ E) E n) :
  φ ∈ TauCeti.exactCompactlySupportedForms (modelWithCornersSelf ℝ E) E n ↔
    TauCeti.integralTopForm o ↑φ = 0
```

**The compactly supported Poincaré lemma in top degree [Lee, Lemma 17.27].** Formalized in Tau Ceti as [`TauCeti.mem_exactCompactlySupportedForms_of_integralTopForm_eq_zero_normedSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Euclidean.html#TauCeti.mem_exactCompactlySupportedForms_of_integralTopForm_eq_zero_normedSpace).

```lean
TauCeti.mem_exactCompactlySupportedForms_of_integralTopForm_eq_zero_normedSpace.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {n : ℕ}
  (o : TauCeti.Manifold.Orientation (modelWithCornersSelf ℝ E) E (Fin n))
  {φ : TauCeti.SmoothForm (modelWithCornersSelf ℝ E) E ℝ n}
  (hφ : φ ∈ TauCeti.compactlySupportedForms (modelWithCornersSelf ℝ E) E n)
  (h : TauCeti.integralTopForm o ↑φ = 0) :
  φ ∈ TauCeti.exactCompactlySupportedForms (modelWithCornersSelf ℝ E) E n
```

## Sources

- [Tau Ceti documentation: `TauCeti.mem_exactCompactlySupportedForms_one_real`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/RealLine.html#TauCeti.mem_exactCompactlySupportedForms_one_real)
- [Source of `TauCeti.mem_exactCompactlySupportedForms_one_real` in TauCeti/Geometry/Manifold/DeRham/RealLine.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/DeRham/RealLine.lean#L62)

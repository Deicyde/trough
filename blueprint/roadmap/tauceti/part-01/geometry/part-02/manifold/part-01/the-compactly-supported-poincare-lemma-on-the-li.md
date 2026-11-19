---
declaration: theorem
origin: cited
lean: TauCeti.mem_exactCompactlySupportedForms_one_real, TauCeti.mem_exactCompactlySupportedForms_iff_integralTopForm_eq_zero
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

- [The fundamental theorem of calculus for line integrals](../part-02/the-fundamental-theorem-of-calculus-for-line-int.md)
- [The Poincaré lemma on manifolds](../part-03/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.mem_exactCompactlySupportedForms_one_real`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/RealLine.html#TauCeti.mem_exactCompactlySupportedForms_one_real).

## Other forms

**The compactly supported Poincaré lemma in top degree, on a preconnected manifold.** Formalized in Tau Ceti as [`TauCeti.mem_exactCompactlySupportedForms_iff_integralTopForm_eq_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/Integration/Bijective.html#TauCeti.mem_exactCompactlySupportedForms_iff_integralTopForm_eq_zero).

```lean
TauCeti.mem_exactCompactlySupportedForms_iff_integralTopForm_eq_zero.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [BoundarylessManifold I M] [T2Space M] [SigmaCompactSpace M] {n : ℕ}
  [PreconnectedSpace M] (o : TauCeti.Manifold.Orientation I M (Fin n))
  {φ : TauCeti.SmoothForm I M ℝ n} (hφ : φ ∈ TauCeti.compactlySupportedForms I M n) :
  φ ∈ TauCeti.exactCompactlySupportedForms I M n ↔ TauCeti.integralTopForm o ↑φ = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.mem_exactCompactlySupportedForms_one_real`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/RealLine.html#TauCeti.mem_exactCompactlySupportedForms_one_real)
- [Source of `TauCeti.mem_exactCompactlySupportedForms_one_real` in TauCeti/Geometry/Manifold/DeRham/RealLine.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DeRham/RealLine.lean#L62)

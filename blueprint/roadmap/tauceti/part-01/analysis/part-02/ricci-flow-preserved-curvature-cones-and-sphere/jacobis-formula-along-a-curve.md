---
declaration: theorem
origin: cited
lean: Matrix.hasDerivAt_det_of_entries, Matrix.hasDerivWithinAt_det_of_entries
statement: formalized
proof: formalized
---

# Jacobi's formula along a curve

If every entry of a matrix curve `A` has derivative given
by the corresponding entry of `A'` at `t`, and `A t` is invertible, then `det A` has derivative
`det (A t) * trace ((A t)⁻¹ * A')` at `t`.

```lean
Matrix.hasDerivAt_det_of_entries.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2}
  [NontriviallyNormedField 𝕜] [Fintype ι] [DecidableEq ι] {A : 𝕜 → Matrix ι ι 𝕜} {A' : Matrix ι ι 𝕜}
  {t : 𝕜} (hA : ∀ (i j : ι), HasDerivAt (fun τ => A τ i j) (A' i j) t) (hdet : IsUnit (A t).det) :
  HasDerivAt (fun τ => (A τ).det) ((A t).det * ((A t)⁻¹ * A').trace) t
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's adjugate formula along a curve](jacobis-adjugate-formula-along-a-curve.md)
- [Jacobi's inverse formula](../../part-03/calculus/part-01/jacobis-inverse-formula.md)

## Lean

Formalized in Tau Ceti as [`Matrix.hasDerivAt_det_of_entries`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Deriv/Matrix.html#Matrix.hasDerivAt_det_of_entries).

## Other forms

**Jacobi's formula along a curve.** Formalized in Tau Ceti as [`Matrix.hasDerivWithinAt_det_of_entries`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Deriv/Matrix.html#Matrix.hasDerivWithinAt_det_of_entries).

```lean
Matrix.hasDerivWithinAt_det_of_entries.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2}
  [NontriviallyNormedField 𝕜] [Fintype ι] [DecidableEq ι] {A : 𝕜 → Matrix ι ι 𝕜} {A' : Matrix ι ι 𝕜}
  {t : 𝕜} {s : Set 𝕜} (hA : ∀ (i j : ι), HasDerivWithinAt (fun τ => A τ i j) (A' i j) s t)
  (hdet : IsUnit (A t).det) :
  HasDerivWithinAt (fun τ => (A τ).det) ((A t).det * ((A t)⁻¹ * A').trace) s t
```

## Sources

- [Tau Ceti documentation: `Matrix.hasDerivAt_det_of_entries`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Deriv/Matrix.html#Matrix.hasDerivAt_det_of_entries)
- [Source of `Matrix.hasDerivAt_det_of_entries` in TauCeti/Analysis/Calculus/Deriv/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/Deriv/Matrix.lean#L84)
- [Tau Ceti roadmap status: Ricci flow, preserved curvature cones, and sphere theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RicciFlow/STATUS.md)

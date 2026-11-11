---
declaration: theorem
origin: cited
lean: TauCeti.isSmoothEmbedding_subtypeVal_complexProjectiveZeroLocus
statement: formalized
proof: formalized
---

# The smooth part of a projective zero locus is an embedded complex submanifold

For the
atlas `TauCeti.complexProjectiveZeroLocusChartedSpace`, the inclusion into `ℂℙⁿ` is a `C^r`
embedding for every `r`.

```lean
TauCeti.isSmoothEmbedding_subtypeVal_complexProjectiveZeroLocus.{u_1} {ι : Type u_1} {n : ℕ}
  {p : ι → MvPolynomial (Fin (n + 1)) ℂ} {d : ι → ℕ} [Fintype ι]
  (hp : ∀ (k : ι), (p k).IsHomogeneous (d k)) {s V : Set (Projectivization ℂ (Fin (n + 1) → ℂ))}
  (hV : IsOpen V) (hs : s = TauCeti.complexProjectiveZeroLocus p ∩ V)
  (hrank : ∀ L ∈ s, Function.Surjective (TauCeti.jacobiMatrixAt p L.rep).mulVec) (r : WithTop ℕ∞) :
  Manifold.IsSmoothEmbedding (modelWithCornersSelf ℂ (Fin (n - Fintype.card ι) → ℂ))
    (modelWithCornersSelf ℂ (Fin n → ℂ)) r Subtype.val
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jacobian criterion in a ratio chart](../../../ring-theory/part-01/multivariate-polynomials/the-jacobian-criterion-in-a-ratio-chart.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isSmoothEmbedding_subtypeVal_complexProjectiveZeroLocus`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/ZeroLocus.html#TauCeti.isSmoothEmbedding_subtypeVal_complexProjectiveZeroLocus).

## Sources

- [Tau Ceti documentation: `TauCeti.isSmoothEmbedding_subtypeVal_complexProjectiveZeroLocus`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Projectivization/ZeroLocus.html#TauCeti.isSmoothEmbedding_subtypeVal_complexProjectiveZeroLocus)
- [Source of `TauCeti.isSmoothEmbedding_subtypeVal_complexProjectiveZeroLocus` in TauCeti/Geometry/Manifold/Projectivization/ZeroLocus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Projectivization/ZeroLocus.lean#L470)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)

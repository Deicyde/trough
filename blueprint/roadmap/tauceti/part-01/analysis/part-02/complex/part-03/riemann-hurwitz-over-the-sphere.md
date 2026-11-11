---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree, TauCeti.RiemannSurface.FiniteHolomorphicMap.exists_isCanonicalDivisor_degree_eq_neg_two_mul_degree_add_ramificationDegree, TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_degree_mul_add_ramificationDegree, TauCeti.RiemannSurface.FiniteHolomorphicMap.ramificationDegree_eq_two_mul_degree_sub_two
statement: formalized
proof: formalized
---

# Riemann–Hurwitz over the sphere

If `f : X → ℙ¹` is a finite holomorphic map from a
compact connected Riemann surface, every canonical divisor `K` of `X` has degree
`-2 deg f + deg R_f`.

```lean
TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree.{u_1}
  {X : Type u_1} [TopologicalSpace X] [ChartedSpace ℂ X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X]
  [CompactSpace X] [ConnectedSpace X] [T2Space X] {K : TauCeti.AlgebraicGeometry.WeilDivisor X}
  (hK : TauCeti.RiemannSurface.IsCanonicalDivisor K)
  (f : TauCeti.RiemannSurface.FiniteHolomorphicMap X (OnePoint ℂ)) :
  TauCeti.AlgebraicGeometry.WeilDivisor.degree K =
    -2 * ↑(TauCeti.RiemannSurface.degree ↑f) + ↑(TauCeti.RiemannSurface.ramificationDegree ↑f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic inverse function theorem](../../analytic/the-analytic-inverse-function-theorem.md)
- [The identity theorem for Riemann surfaces](../part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The open mapping theorem](the-open-mapping-theorem.md)
- [Rouché's theorem for a disc, classical form](rouches-theorem-for-a-disc-classical-form.md)
- [TauCeti.RiemannSurface.MeromorphicFunction](../../../../field-theory/belyi-maps-dessins-denfants-and-three-point-cove/tauceti-riemannsurface-meromorphicfunction.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Canonical/Degree.html#TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree).

## Other forms

**Riemann–Hurwitz for a canonical divisor.** Formalized in Tau Ceti as [`TauCeti.RiemannSurface.FiniteHolomorphicMap.exists_isCanonicalDivisor_degree_eq_neg_two_mul_degree_add_ramificationDegree`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/RiemannHurwitz.html#TauCeti.RiemannSurface.FiniteHolomorphicMap.exists_isCanonicalDivisor_degree_eq_neg_two_mul_degree_add_ramificationDegree).

```lean
TauCeti.RiemannSurface.FiniteHolomorphicMap.exists_isCanonicalDivisor_degree_eq_neg_two_mul_degree_add_ramificationDegree.{u_1}
  {X : Type u_1} [TopologicalSpace X] [ChartedSpace ℂ X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X]
  [CompactSpace X] [T2Space X] (f : TauCeti.RiemannSurface.FiniteHolomorphicMap X (OnePoint ℂ)) :
  ∃ K,
    TauCeti.RiemannSurface.IsCanonicalDivisor K ∧
      TauCeti.AlgebraicGeometry.WeilDivisor.degree K =
        -2 * ↑(TauCeti.RiemannSurface.degree ↑f) + ↑(TauCeti.RiemannSurface.ramificationDegree ↑f)
```

**Riemann–Hurwitz for canonical divisors.** Formalized in Tau Ceti as [`TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_degree_mul_add_ramificationDegree`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Canonical/Degree.html#TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_degree_mul_add_ramificationDegree).

```lean
TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_degree_mul_add_ramificationDegree.{u_1, u_2}
  {X : Type u_1} {Y : Type u_2} [TopologicalSpace X] [ChartedSpace ℂ X]
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X] [CompactSpace X] [ConnectedSpace X] [T2Space X]
  [TopologicalSpace Y] [ChartedSpace ℂ Y] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 Y]
  [CompactSpace Y] [T2Space Y] [ConnectedSpace Y] {KX : TauCeti.AlgebraicGeometry.WeilDivisor X}
  {KY : TauCeti.AlgebraicGeometry.WeilDivisor Y}
  (hKX : TauCeti.RiemannSurface.IsCanonicalDivisor KX)
  (hKY : TauCeti.RiemannSurface.IsCanonicalDivisor KY)
  (f : TauCeti.RiemannSurface.FiniteHolomorphicMap X Y) :
  TauCeti.AlgebraicGeometry.WeilDivisor.degree KX =
    ↑(TauCeti.RiemannSurface.degree ↑f) * TauCeti.AlgebraicGeometry.WeilDivisor.degree KY +
      ↑(TauCeti.RiemannSurface.ramificationDegree ↑f)
```

**Riemann–Hurwitz for maps of the sphere.** Formalized in Tau Ceti as [`TauCeti.RiemannSurface.FiniteHolomorphicMap.ramificationDegree_eq_two_mul_degree_sub_two`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Canonical/Degree.html#TauCeti.RiemannSurface.FiniteHolomorphicMap.ramificationDegree_eq_two_mul_degree_sub_two).

```lean
TauCeti.RiemannSurface.FiniteHolomorphicMap.ramificationDegree_eq_two_mul_degree_sub_two
  (f : TauCeti.RiemannSurface.FiniteHolomorphicMap (OnePoint ℂ) (OnePoint ℂ)) :
  ↑(TauCeti.RiemannSurface.ramificationDegree ↑f) = 2 * ↑(TauCeti.RiemannSurface.degree ↑f) - 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Canonical/Degree.html#TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree)
- [Source of `TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree` in TauCeti/Analysis/Complex/RiemannSurface/Differential/Canonical/Degree.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/RiemannSurface/Differential/Canonical/Degree.lean#L85)

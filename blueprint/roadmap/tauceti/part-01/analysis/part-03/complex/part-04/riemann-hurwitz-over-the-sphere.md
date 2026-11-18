---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree, TauCeti.RiemannSurface.FiniteHolomorphicMap.exists_isCanonicalDivisor_degree_eq_neg_two_mul_degree_add_ramificationDegree, TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_degree_mul_add_ramificationDegree, TauCeti.RiemannSurface.FiniteHolomorphicMap.ramificationDegree_eq_two_mul_degree_sub_two, TauCeti.RiemannSurface.FiniteHolomorphicMap.two_mul_genus_sub_two_eq_of_eulerChar_eq, TauCeti.RiemannSurface.FiniteHolomorphicMap.neg_two_mul_degree_add_ramificationDegree_eq_neg_eulerChar, TauCeti.RiemannSurface.FiniteHolomorphicMap.eulerChar_eq_two_mul_degree_sub_ramificationDegree
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

- [A CW structure lifts along a covering map](../../../../algebraic-topology/classifying-spaces-of-discrete-groups/a-cw-structure-lifts-along-a-covering-map.md)
- [A maximal integral curve confined to a compact set is defined for all time](../../../../geometry/part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [The analytic inverse function theorem](../../analytic/the-analytic-inverse-function-theorem.md)
- [Euler--Poincaré for cellular chains](../../../../algebraic-topology/other-results/euler-poincare-for-cellular-chains.md)
- [The identity theorem for Riemann surfaces](../part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [ModelWithCorners.restrictScalars](../../../../geometry/part-01/complex-manifolds-transport-quotients-bundles-an/modelwithcorners-restrictscalars.md)
- [The open mapping theorem](../part-03/the-open-mapping-theorem.md)
- [Osgood's lemma](../../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [The relative small-chain theorem](../../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
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

**Riemann–Hurwitz in genus form, for surfaces whose Euler numbers are `2 - 2 · genus`.** Formalized in Tau Ceti as [`TauCeti.RiemannSurface.FiniteHolomorphicMap.two_mul_genus_sub_two_eq_of_eulerChar_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Genus.html#TauCeti.RiemannSurface.FiniteHolomorphicMap.two_mul_genus_sub_two_eq_of_eulerChar_eq).

```lean
TauCeti.RiemannSurface.FiniteHolomorphicMap.two_mul_genus_sub_two_eq_of_eulerChar_eq.{u}
  {X Y : Type u} [TopologicalSpace X] [ChartedSpace ℂ X] [TopologicalSpace Y] [ChartedSpace ℂ Y]
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 Y]
  [CompactSpace X] [T2Space X] [T2Space Y] [PreconnectedSpace Y] [TauCeti.FiniteCWType X]
  [TauCeti.FiniteCWType Y] (f : TauCeti.RiemannSurface.FiniteHolomorphicMap X Y)
  [TauCeti.FiniteCWType ↑f.branchValuesᶜ]
  (hX : TauCeti.eulerChar X = 2 - 2 * ↑(TauCeti.RiemannSurface.genus X))
  (hY : TauCeti.eulerChar Y = 2 - 2 * ↑(TauCeti.RiemannSurface.genus Y)) :
  2 * ↑(TauCeti.RiemannSurface.genus X) - 2 =
    ↑(TauCeti.RiemannSurface.degree ↑f) * (2 * ↑(TauCeti.RiemannSurface.genus Y) - 2) +
      ↑(TauCeti.RiemannSurface.ramificationDegree ↑f)
```

**Riemann–Hurwitz over the sphere, negated form.** Formalized in Tau Ceti as [`TauCeti.RiemannSurface.FiniteHolomorphicMap.neg_two_mul_degree_add_ramificationDegree_eq_neg_eulerChar`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Branch/Sphere.html#TauCeti.RiemannSurface.FiniteHolomorphicMap.neg_two_mul_degree_add_ramificationDegree_eq_neg_eulerChar).

```lean
TauCeti.RiemannSurface.FiniteHolomorphicMap.neg_two_mul_degree_add_ramificationDegree_eq_neg_eulerChar
  {X : Type} [TopologicalSpace X] [ChartedSpace ℂ X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X]
  [CompactSpace X] [T2Space X] [TauCeti.FiniteCWType X]
  (f : TauCeti.RiemannSurface.FiniteHolomorphicMap X (OnePoint ℂ)) :
  -2 * ↑(TauCeti.RiemannSurface.degree ↑f) + ↑(TauCeti.RiemannSurface.ramificationDegree ↑f) =
    -TauCeti.eulerChar X
```

**Riemann–Hurwitz over the sphere, topological form.** Formalized in Tau Ceti as [`TauCeti.RiemannSurface.FiniteHolomorphicMap.eulerChar_eq_two_mul_degree_sub_ramificationDegree`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Branch/Sphere.html#TauCeti.RiemannSurface.FiniteHolomorphicMap.eulerChar_eq_two_mul_degree_sub_ramificationDegree).

```lean
TauCeti.RiemannSurface.FiniteHolomorphicMap.eulerChar_eq_two_mul_degree_sub_ramificationDegree
  {X : Type} [TopologicalSpace X] [ChartedSpace ℂ X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X]
  [CompactSpace X] [T2Space X] [TauCeti.FiniteCWType X]
  (f : TauCeti.RiemannSurface.FiniteHolomorphicMap X (OnePoint ℂ)) :
  TauCeti.eulerChar X =
    2 * ↑(TauCeti.RiemannSurface.degree ↑f) - ↑(TauCeti.RiemannSurface.ramificationDegree ↑f)
```

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Canonical/Degree.html#TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree)
- [Source of `TauCeti.RiemannSurface.IsCanonicalDivisor.degree_eq_neg_two_mul_degree_add_ramificationDegree` in TauCeti/Analysis/Complex/RiemannSurface/Differential/Canonical/Degree.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/RiemannSurface/Differential/Canonical/Degree.lean#L85)

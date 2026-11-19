---
declaration: theorem
origin: cited
lean: TauCeti.HomologicalOrientation.bijective_dualityMap_of_convex, TauCeti.HomologicalOrientation.bijective_dualityMap_self, TauCeti.HomologicalOrientation.isIso_dualityMap_self, TauCeti.HomologicalOrientation.bijective_dualityMap_of_starConvex
statement: formalized
proof: formalized
---

# Poincaré duality for a convex open subset

for an open embedding `j : U → F` whose image
is convex, the duality map `Hᵖ_c(U; L) ⟶ H_q(U; L)` of any homological orientation of `U` is
bijective.

```lean
TauCeti.HomologicalOrientation.bijective_dualityMap_of_convex {F : Type} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {d : ℕ} (hd : Module.finrank ℝ F = d) (L : ModuleCat ℤ)
  {p q : ℕ} (h : p + q = d) {U : Type} [TopologicalSpace U] [T2Space U] [ChartedSpace F U]
  (oU : TauCeti.HomologicalOrientation U F d) {j : U → F} (hj : Topology.IsOpenEmbedding j)
  (hU : Convex ℝ (Set.range j)) :
  Function.Bijective ⇑(CategoryTheory.ConcreteCategory.hom (oU.dualityMap hd L p q h))
```

## Depends on

- [The duality map](../algebraic-topology-of-spaces-and-manifolds/the-duality-map.md)

## Proof depends on

- [Capping with the fundamental class along a compact star-convex set is bijective](../algebraic-topology-of-spaces-and-manifolds/capping-with-the-fundamental-class-along-a-compa.md)
- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)
- [The relative small-chain theorem for cochains](the-relative-small-chain-theorem-for-cochains.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HomologicalOrientation.bijective_dualityMap_of_convex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Euclidean/Duality.html#TauCeti.HomologicalOrientation.bijective_dualityMap_of_convex).

## Other forms

**Poincaré duality for a finite-dimensional real normed space.** Formalized in Tau Ceti as [`TauCeti.HomologicalOrientation.bijective_dualityMap_self`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Euclidean/Duality.html#TauCeti.HomologicalOrientation.bijective_dualityMap_self).

```lean
TauCeti.HomologicalOrientation.bijective_dualityMap_self {F : Type} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {d : ℕ} (hd : Module.finrank ℝ F = d) (L : ModuleCat ℤ)
  {p q : ℕ} (h : p + q = d) (o : TauCeti.HomologicalOrientation F F d) :
  Function.Bijective ⇑(CategoryTheory.ConcreteCategory.hom (o.dualityMap hd L p q h))
```

**Poincaré duality for a finite-dimensional real normed space, as an isomorphism.** Formalized in Tau Ceti as [`TauCeti.HomologicalOrientation.isIso_dualityMap_self`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Euclidean/Duality.html#TauCeti.HomologicalOrientation.isIso_dualityMap_self).

```lean
TauCeti.HomologicalOrientation.isIso_dualityMap_self {F : Type} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {d : ℕ} (hd : Module.finrank ℝ F = d) (L : ModuleCat ℤ)
  {p q : ℕ} (h : p + q = d) (o : TauCeti.HomologicalOrientation F F d) :
  CategoryTheory.IsIso (o.dualityMap hd L p q h)
```

**Poincaré duality for a star-convex open subset.** Formalized in Tau Ceti as [`TauCeti.HomologicalOrientation.bijective_dualityMap_of_starConvex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Euclidean/Duality.html#TauCeti.HomologicalOrientation.bijective_dualityMap_of_starConvex).

```lean
TauCeti.HomologicalOrientation.bijective_dualityMap_of_starConvex {F : Type} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] {d : ℕ} (hd : Module.finrank ℝ F = d) (L : ModuleCat ℤ)
  {p q : ℕ} (h : p + q = d) {U : Type} [TopologicalSpace U] [T2Space U] [ChartedSpace F U]
  (oU : TauCeti.HomologicalOrientation U F d) {j : U → F} (hj : Topology.IsOpenEmbedding j) {y : F}
  (hU : StarConvex ℝ y (Set.range j)) :
  Function.Bijective ⇑(CategoryTheory.ConcreteCategory.hom (oU.dualityMap hd L p q h))
```

## Sources

- [Tau Ceti documentation: `TauCeti.HomologicalOrientation.bijective_dualityMap_of_convex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Euclidean/Duality.html#TauCeti.HomologicalOrientation.bijective_dualityMap_of_convex)
- [Source of `TauCeti.HomologicalOrientation.bijective_dualityMap_of_convex` in TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Euclidean/Duality.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cohomology/CompactSupport/Euclidean/Duality.lean#L133)

---
declaration: theorem
origin: cited
lean: TauCeti.HomologicalOrientation.bijective_singularCap_fundamentalClassOn_of_starConvex
statement: formalized
proof: formalized
---

# Capping with the fundamental class along a compact star-convex set is bijective

for a
compact set `K` in a finite-dimensional real normed space `F` of dimension `d`, star-convex about
a point `y ∈ K`, capping with the fundamental class `μ_K` of a homological orientation along `K`
is bijective `Hᵖ(F, F ∖ K; L) ⟶ H_q(F; L)` for every abelian group `L` and all `p + q = d`.

```lean
TauCeti.HomologicalOrientation.bijective_singularCap_fundamentalClassOn_of_starConvex {F : Type}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [FiniteDimensional ℝ F] {d : ℕ}
  (o : TauCeti.HomologicalOrientation F F d) (hd : Module.finrank ℝ F = d) (L : ModuleCat ℤ)
  {K : Set F} (hK : IsCompact K) {y : F} (hKy : StarConvex ℝ y K) (hy : y ∈ K) (p q : ℕ)
  (h : p + q = d) :
  Function.Bijective fun α =>
    (ModuleCat.Hom.hom
        (((TopPair.ofSubset Kᶜ).singularCap ℤ
            (CategoryTheory.MonoidalCategoryStruct.rightUnitor ↧(ULift.{0, 0} ℤ)).inv
            (CategoryTheory.MonoidalCategoryStruct.rightUnitor L).hom p q d h)
          α))
      (o.fundamentalClassOn hd hK)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)
- [The relative universal coefficient theorem over a field](../cohomology/the-relative-universal-coefficient-theorem-over.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HomologicalOrientation.bijective_singularCap_fundamentalClassOn_of_starConvex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Cap/Euclidean.html#TauCeti.HomologicalOrientation.bijective_singularCap_fundamentalClassOn_of_starConvex).

## Sources

- [Tau Ceti documentation: `TauCeti.HomologicalOrientation.bijective_singularCap_fundamentalClassOn_of_starConvex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/Cap/Euclidean.html#TauCeti.HomologicalOrientation.bijective_singularCap_fundamentalClassOn_of_starConvex)
- [Source of `TauCeti.HomologicalOrientation.bijective_singularCap_fundamentalClassOn_of_starConvex` in TauCeti/AlgebraicTopology/Cohomology/Cap/Euclidean.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cohomology/Cap/Euclidean.lean#L101)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AlgebraicTopology/STATUS.md)

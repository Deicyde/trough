---
declaration: theorem
origin: cited
lean: TauCeti.ContCohomology.dualityMap2_injective_of_injective_discreteCoind
statement: formalized
proof: formalized
---

# Injectivity of Tate's duality map `α₂` descends to an open subgroup

If
`α₂ : H²(G, Coind_U^G A) → Hom(H⁰(G, Hom(Coind_U^G A, N)), H²(G, N))` is injective, then so is
`α₂ : H²(U, A) → Hom(H⁰(U, Hom(A, N)), H²(U, N))`: a class of `H²(U, A)` killed by every invariant
of `Hom(A, N)` has, by `explicitDualityPairing02_explicitCoeff0_toInternalHom`, an inverse Shapiro
image killed by every invariant of `Hom(Coind_U^G A, N)`, all of which are coinduced. The
continuity of the conjugation action of `U` on `Hom(A, N)`, automatic for a finite `A`, is what
makes `toInternalHom` surjective.

```lean
TauCeti.ContCohomology.dualityMap2_injective_of_injective_discreteCoind.{uG, uN, uA} (G : Type uG)
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] (U : Subgroup G) [U.FiniteIndex] (hU : IsOpen ↑U) (A : Type uA)
  [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction (↥U) A]
  [ContinuousSMul (↥U) A] (N : Type uN) [AddCommGroup N] [TopologicalSpace N] [DiscreteTopology N]
  [DistribMulAction G N] [ContinuousSMul G N] [ContinuousSMul (↥U) (TauCeti.InternalHom (↥U) A N)]
  (h : Function.Injective ⇑(TauCeti.ContCohomology.dualityMap2 G (TauCeti.DiscreteCoind G U A) N)) :
  Function.Injective ⇑(TauCeti.ContCohomology.dualityMap2 (↥U) A N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shapiro's lemma in every degree](shapiros-lemma-in-every-degree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.dualityMap2_injective_of_injective_discreteCoind`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/OpenSubgroup.html#TauCeti.ContCohomology.dualityMap2_injective_of_injective_discreteCoind).

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.dualityMap2_injective_of_injective_discreteCoind`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/OpenSubgroup.html#TauCeti.ContCohomology.dualityMap2_injective_of_injective_discreteCoind)
- [Source of `TauCeti.ContCohomology.dualityMap2_injective_of_injective_discreteCoind` in TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/OpenSubgroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/ContCohomology/Cup/Duality/OpenSubgroup.lean#L454)

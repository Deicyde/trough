---
declaration: theorem
origin: cited
lean: TauCeti.strictCohomologicalDimensionLE_iff_forall_openSubgroup
statement: formalized
proof: formalized
---

# The strict cohomological dimension through integral coefficients (NSW (3.3.4)), as vanishing predicates

For a profinite group `G` and a prime `p`,
`StrictCohomologicalDimensionLE p G n` holds if and only if `CohomologicalDimensionLE p G n` holds
and the `p`-primary component of `Hⁿ⁺¹(U, ℤ)` vanishes for every open subgroup `U`, the integers
carrying the trivial action.

```lean
TauCeti.strictCohomologicalDimensionLE_iff_forall_openSubgroup.{u} {p : ℕ} {G : Type u} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] {n : ℕ}
  (hp : Nat.Prime p) :
  TauCeti.StrictCohomologicalDimensionLE p G n ↔
    TauCeti.CohomologicalDimensionLE p G n ∧
      ∀ (U : OpenSubgroup G),
        AddCommGroup.primaryComponent
            (↑(continuousCohomology (n + 1)
                  (TopRep.of (ContRepresentation.trivial ℤ (↥↑U) (ULift.{u, 0} ℤ)))).toModuleCat)
            p =
          ⊥
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shapiro's lemma in degree one](../homological/shapiros-lemma-in-degree-one.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.strictCohomologicalDimensionLE_iff_forall_openSubgroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/CohomologicalDimension/IntegralCriterion.html#TauCeti.strictCohomologicalDimensionLE_iff_forall_openSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.strictCohomologicalDimensionLE_iff_forall_openSubgroup`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/CohomologicalDimension/IntegralCriterion.html#TauCeti.strictCohomologicalDimensionLE_iff_forall_openSubgroup)
- [Source of `TauCeti.strictCohomologicalDimensionLE_iff_forall_openSubgroup` in TauCeti/RepresentationTheory/Homological/ContCohomology/CohomologicalDimension/IntegralCriterion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/ContCohomology/CohomologicalDimension/IntegralCriterion.lean#L290)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)

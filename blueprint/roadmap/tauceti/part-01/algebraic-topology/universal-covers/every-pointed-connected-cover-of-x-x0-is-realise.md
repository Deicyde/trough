---
declaration: theorem
origin: cited
lean: TauCeti.UniversalCover.existsUnique_subgroup_homeomorph_subgroupQuotient
statement: formalized
proof: formalized
---

# Every pointed connected cover of `(X, x₀)` is realised by exactly one subgroup of `π₁(X, x₀)`

The subgroups of `π₁(X, x₀)` therefore parametrise the pointed connected covers
of `(X, x₀)` bijectively, up to isomorphism over `X` respecting the chosen lifts.

```lean
TauCeti.UniversalCover.existsUnique_subgroup_homeomorph_subgroupQuotient.{u_1, u_2} {X : Type u_1}
  [TopologicalSpace X] [LocallyPathConnectedSpace X] [TauCeti.SemilocallySimplyConnectedSpace X]
  (x₀ : X) {E : Type u_2} [TopologicalSpace E] [PathConnectedSpace E] {p : E → X}
  (hp : IsCoveringMap p) {e₀ : E} (hpe : p e₀ = x₀) :
  ∃! H,
    ∃ h,
      h e₀ = TauCeti.UniversalCover.SubgroupQuotient.basepoint x₀ H ∧
        TauCeti.UniversalCover.subgroupQuotientProj x₀ H ∘ ⇑h = p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UniversalCover.existsUnique_subgroup_homeomorph_subgroupQuotient`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Classification/Bijection.html#TauCeti.UniversalCover.existsUnique_subgroup_homeomorph_subgroupQuotient).

## Sources

- [Tau Ceti documentation: `TauCeti.UniversalCover.existsUnique_subgroup_homeomorph_subgroupQuotient`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/UniversalCover/Classification/Bijection.html#TauCeti.UniversalCover.existsUnique_subgroup_homeomorph_subgroupQuotient)
- [Source of `TauCeti.UniversalCover.existsUnique_subgroup_homeomorph_subgroupQuotient` in TauCeti/AlgebraicTopology/UniversalCover/Classification/Bijection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/UniversalCover/Classification/Bijection.lean#L96)
- [Tau Ceti roadmap status: Universal covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/UniversalCovers/STATUS.md)

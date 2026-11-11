---
declaration: theorem
origin: cited
lean: OpenSubgroup.evensNorm_trans
statement: formalized
proof: formalized
---

# Transitivity of the Evens norm

Let `V ≤ U` be compact open subgroups of finite index in
`G`, and regard `V` as the open subgroup `V.subgroupOf U` of `U`. For `x ∈ Hⁿ(V, 𝔽₂)`, the norm
from `V` to `G` of `x` is the norm from `U` to `G` of the norm from `V.subgroupOf U` to `U` of the
pullback of `x` along `V.subgroupOf U ≃ V`: `N_V^G x = N_U^G (N_V^U x)`, after transporting the
degree `[G : U] ([U : V] n)` to `[G : V] n`.

```lean
OpenSubgroup.evensNorm_trans.{u} {G : Type u} [Group G] [TopologicalSpace G] [IsTopologicalGroup G]
  {U V : OpenSubgroup G} (hVU : V ≤ U) [(↑U).FiniteIndex] [CompactSpace ↥↑U] [Fintype (G ⧸ ↑U)]
  [(↑V).FiniteIndex] [CompactSpace ↥↑V] [Fintype (G ⧸ ↑V)] [CompactSpace ↥((↑V).subgroupOf ↑U)]
  [Fintype (↥↑U ⧸ (↑V).subgroupOf ↑U)] {n : ℕ}
  (x : ↑(continuousCohomology n (TauCeti.trivialF2 ↥↑V)).toModuleCat) :
  V.evensNorm x =
    (CategoryTheory.ConcreteCategory.hom
        (TauCeti.ContinuousCohomology.degreeCast (TauCeti.trivialF2 G) ⋯).hom)
      (U.evensNorm
        ({ toSubgroup := (↑V).subgroupOf ↑U, isOpen' := ⋯ }.evensNorm
          ((CategoryTheory.ConcreteCategory.hom
              (TauCeti.trivialF2Map (↑(Subgroup.subgroupOfContinuousMulEquivOfLe ⋯)) n))
            x)))
```

## Depends on

- [The Evens norm](the-evens-norm.md)

## Proof depends on

- [Frobenius reciprocity for `coind₁`, uniqueness](../other-results/frobenius-reciprocity-for-coind1-uniqueness.md)

## Lean

Formalized in Tau Ceti as [`OpenSubgroup.evensNorm_trans`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/Transitivity.html#OpenSubgroup.evensNorm_trans).

## Sources

- [Tau Ceti documentation: `OpenSubgroup.evensNorm_trans`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/Transitivity.html#OpenSubgroup.evensNorm_trans)
- [Source of `OpenSubgroup.evensNorm_trans` in TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/Transitivity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Homological/ContCohomology/Evens/Norm/Transitivity.lean#L380)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)

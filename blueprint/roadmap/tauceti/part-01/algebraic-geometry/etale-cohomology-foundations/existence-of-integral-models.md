---
declaration: theorem
origin: cited
lean: TauCeti.GaloisLattice.IntegralModel.nonempty
statement: formalized
proof: formalized
---

# Existence of integral models

A jointly continuous representation of a compact group on a
finite-dimensional vector space over a field with a valuative topology, for instance a
nonarchimedean local field, has an integral model over the valuation ring `𝒪[E]`.

```lean
TauCeti.GaloisLattice.IntegralModel.nonempty.{u_1, u_2, u_3} {Γ : Type u_1} [Group Γ]
  [TopologicalSpace Γ] [CompactSpace Γ] {E : Type u_2} [Field E] [ValuativeRel E]
  [TopologicalSpace E] [IsValuativeTopology E] {V : Type u_3} [AddCommGroup V] [_root_.Module E V]
  [_root_.Module (↥(ValuativeRel.valuation E).integer) V]
  [IsScalarTower (↥(ValuativeRel.valuation E).integer) E V] [TopologicalSpace V]
  [IsModuleTopology E V] [FiniteDimensional E V] (ρ : TauCeti.ContinuousRep Γ E V) :
  Nonempty (TauCeti.GaloisLattice.IntegralModel (↥(ValuativeRel.valuation E).integer) ρ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GaloisLattice.IntegralModel.nonempty`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/IntegralModel/Basic.html#TauCeti.GaloisLattice.IntegralModel.nonempty).

## Sources

- [Tau Ceti documentation: `TauCeti.GaloisLattice.IntegralModel.nonempty`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/IntegralModel/Basic.html#TauCeti.GaloisLattice.IntegralModel.nonempty)
- [Source of `TauCeti.GaloisLattice.IntegralModel.nonempty` in TauCeti/RepresentationTheory/Continuous/IntegralModel/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Continuous/IntegralModel/Basic.lean#L241)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)

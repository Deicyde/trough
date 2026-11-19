---
declaration: theorem
origin: cited
lean: Subgroup.isCompact_closure_iff_exists_stable_lattice
statement: formalized
proof: formalized
---

# A subgroup of `GL(V)` stabilizes a lattice if and only if its closure is compact

Here
`V` is a finite-dimensional vector space over a nonarchimedean local field `E`, and `GL(V)` is
the group `V ≃ₗ[E] V` of linear automorphisms with its natural topology.

```lean
Subgroup.isCompact_closure_iff_exists_stable_lattice.{u_1, u_2} {E : Type u_1} {V : Type u_2}
  [Field E] [ValuativeRel E] [TopologicalSpace E] [IsNonarchimedeanLocalField E] [AddCommGroup V]
  [_root_.Module E V] [_root_.Module (↥(ValuativeRel.valuation E).integer) V]
  [IsScalarTower (↥(ValuativeRel.valuation E).integer) E V] [TopologicalSpace V]
  [IsModuleTopology E V] [FiniteDimensional E V] (K : Subgroup (V ≃ₗ[E] V)) :
  IsCompact (closure ↑K) ↔ ∃ L, Submodule.IsLattice E L ∧ ∀ k ∈ K, ∀ x ∈ L, k x ∈ L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.isCompact_closure_iff_exists_stable_lattice`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/StableLattice.html#Subgroup.isCompact_closure_iff_exists_stable_lattice).

## Sources

- [Tau Ceti documentation: `Subgroup.isCompact_closure_iff_exists_stable_lattice`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/StableLattice.html#Subgroup.isCompact_closure_iff_exists_stable_lattice)
- [Source of `Subgroup.isCompact_closure_iff_exists_stable_lattice` in TauCeti/RepresentationTheory/Continuous/StableLattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Continuous/StableLattice.lean#L130)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)

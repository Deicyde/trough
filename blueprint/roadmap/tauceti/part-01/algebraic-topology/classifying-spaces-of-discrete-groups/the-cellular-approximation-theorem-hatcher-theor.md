---
declaration: theorem
origin: cited
lean: TauCeti.exists_isCellular_homotopicRel, TauCeti.exists_isCellular_homotopic
statement: formalized
proof: formalized
---

# The cellular approximation theorem (Hatcher, Theorem 4.8)

Every map `f : C → C'` of
relative CW complexes sending the base `D` into the base `E` is homotopic, relative to `D`, to a
cellular map.

```lean
TauCeti.exists_isCellular_homotopicRel.{w} {X Y : Type w} [TopologicalSpace X] [T2Space X]
  [TopologicalSpace Y] [T2Space Y] {C D : Set X} [Topology.RelCWComplex C D] {C' E : Set Y}
  [Topology.RelCWComplex C' E] (f : ↧↑C ⟶ ↧↑C')
  (hf : Set.MapsTo ⇑(CategoryTheory.ConcreteCategory.hom f) {x | ↑x ∈ D} {y | ↑y ∈ E}) :
  ∃ g, TauCeti.IsCellular C C' g ∧ (TopCat.Hom.hom f).HomotopicRel (TopCat.Hom.hom g) {x | ↑x ∈ D}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCellular_homotopicRel`](https://taucetiproject.org/docs/TauCeti/Topology/CWComplex/Classical/CellularApproximation.html#TauCeti.exists_isCellular_homotopicRel).

## Other forms

**The cellular approximation theorem for CW complexes (Hatcher, Theorem 4.8).** Formalized in Tau Ceti as [`TauCeti.exists_isCellular_homotopic`](https://taucetiproject.org/docs/TauCeti/Topology/CWComplex/Classical/CellularApproximation.html#TauCeti.exists_isCellular_homotopic).

```lean
TauCeti.exists_isCellular_homotopic.{w} {X Y : Type w} [TopologicalSpace X] [T2Space X]
  [TopologicalSpace Y] [T2Space Y] {C : Set X} [Topology.CWComplex C] {C' : Set Y}
  [Topology.CWComplex C'] (f : ↧↑C ⟶ ↧↑C') :
  ∃ g, TauCeti.IsCellular C C' g ∧ (TopCat.Hom.hom f).Homotopic (TopCat.Hom.hom g)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCellular_homotopicRel`](https://taucetiproject.org/docs/TauCeti/Topology/CWComplex/Classical/CellularApproximation.html#TauCeti.exists_isCellular_homotopicRel)
- [Source of `TauCeti.exists_isCellular_homotopicRel` in TauCeti/Topology/CWComplex/Classical/CellularApproximation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/CWComplex/Classical/CellularApproximation.lean#L91)

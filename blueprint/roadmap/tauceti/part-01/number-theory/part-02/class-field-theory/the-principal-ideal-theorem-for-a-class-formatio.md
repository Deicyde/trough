---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.ClassFormation.groundInclusion_mem_normSubgroup_of_range_eq_commutator
statement: formalized
proof: formalized
---

# The principal ideal theorem for a class formation

Let `V ◁ U` be a layer, `K/F` in field
notation, and restrict it to the ground subgroup `U'` whose image `U'/V` is the commutator subgroup
of `U/V`, the layer `K/E` over the maximal abelian subextension `E`. Then every element of the
ground level `A^U` is, in `A^{U'}`, a norm from `A^V`.

```lean
TauCeti.ClassFieldTheory.ClassFormation.groundInclusion_mem_normSubgroup_of_range_eq_commutator
  {G : Type} [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G]
  [TotallyDisconnectedSpace G] {F : TauCeti.ClassFieldTheory.Formation G}
  (cf : TauCeti.ClassFieldTheory.ClassFormation F)
  {small big : TauCeti.ClassFieldTheory.NormalLayer G}
  (T : TauCeti.ClassFieldTheory.LayerRestriction small big)
  (hT : T.galHom.range = commutator big.Gal) (a : ↥(F.level big.ground)) :
  (T.groundInclusion F) a ∈ small.normSubgroup F
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Furtwängler's theorem, the group-theoretic principal ideal theorem](../../../group-theory/other-results/furtwanglers-theorem-the-group-theoretic-princip.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../../part-01/class-field-theory/tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ClassFormation.groundInclusion_mem_normSubgroup_of_range_eq_commutator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/PrincipalIdeal.html#TauCeti.ClassFieldTheory.ClassFormation.groundInclusion_mem_normSubgroup_of_range_eq_commutator).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.ClassFormation.groundInclusion_mem_normSubgroup_of_range_eq_commutator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/PrincipalIdeal.html#TauCeti.ClassFieldTheory.ClassFormation.groundInclusion_mem_normSubgroup_of_range_eq_commutator)
- [Source of `TauCeti.ClassFieldTheory.ClassFormation.groundInclusion_mem_normSubgroup_of_range_eq_commutator` in TauCeti/NumberTheory/ClassFieldTheory/Formation/PrincipalIdeal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/Formation/PrincipalIdeal.lean#L63)

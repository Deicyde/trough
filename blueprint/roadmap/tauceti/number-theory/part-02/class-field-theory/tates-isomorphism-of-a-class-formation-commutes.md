---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj
statement: formalized
proof: formalized
---

# Tate's isomorphism of a class formation commutes with conjugation

conjugating
`x ∪ u_{U/V}` by `g` gives the cup product of the conjugate of `x` with the fundamental class of
the conjugate layer.

```lean
TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj {G : Type} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  {F : TauCeti.ClassFieldTheory.Formation G} (cf : TauCeti.ClassFieldTheory.ClassFormation F)
  (L : TauCeti.ClassFieldTheory.NormalLayer G) (g : G) (r : ℤ) (x : ↑(L.TrivialTateH r)) :
  (CategoryTheory.ConcreteCategory.hom (L.conjugateTateIso F g (r + 2)).hom) ((cf.tateIso L r) x) =
    (cf.tateIso (L.conjugate g) r)
      ((CategoryTheory.ConcreteCategory.hom (L.conjugateTrivialTateIso g r).hom) x)
```

## Depends on

- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../../part-01/class-field-theory/tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Conjugation.html#TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Conjugation.html#TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj)
- [Source of `TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj` in TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Conjugation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Conjugation.lean#L153)

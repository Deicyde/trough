---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj, TauCeti.ClassFieldTheory.ClassFormation.tateIso_layerHom
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

- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Shapiro's isomorphism on an adjunct](../../../representation-theory/homological/shapiros-isomorphism-on-an-adjunct.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Conjugation.html#TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj).

## Other forms

**Tate's isomorphism is carried along a layer morphism matching the fundamental classes.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ClassFormation.tateIso_layerHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Layer/Hom.html#TauCeti.ClassFieldTheory.ClassFormation.tateIso_layerHom).

```lean
TauCeti.ClassFieldTheory.ClassFormation.tateIso_layerHom {G : Type} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G] {G' : Type} [Group G']
  [TopologicalSpace G'] [IsTopologicalGroup G'] [CompactSpace G'] [TotallyDisconnectedSpace G']
  {F : TauCeti.ClassFieldTheory.Formation G} {L : TauCeti.ClassFieldTheory.NormalLayer G}
  {F' : TauCeti.ClassFieldTheory.Formation G'} {L' : TauCeti.ClassFieldTheory.NormalLayer G'}
  (cf : TauCeti.ClassFieldTheory.ClassFormation F)
  (cf' : TauCeti.ClassFieldTheory.ClassFormation F')
  (E : TauCeti.ClassFieldTheory.LayerHom F L F' L')
  (hu :
    (CategoryTheory.ConcreteCategory.hom (E.cohomologyMap 2)) (cf.fundamentalClass L) =
      cf'.fundamentalClass L')
  (r : ℤ) (x : ↑(L.TrivialTateH r)) :
  (CategoryTheory.ConcreteCategory.hom (E.tateCohomologyMap (r + 2))) ((cf.tateIso L r) x) =
    (cf'.tateIso L' r) ((CategoryTheory.ConcreteCategory.hom (E.trivialTateCohomologyIso r).hom) x)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Conjugation.html#TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj)
- [Source of `TauCeti.ClassFieldTheory.ClassFormation.tateIso_conj` in TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Conjugation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Conjugation.lean#L153)

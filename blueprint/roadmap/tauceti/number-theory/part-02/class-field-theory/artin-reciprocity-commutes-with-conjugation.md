---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_conj, TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_layerHom
statement: formalized
proof: formalized
---

# Artin reciprocity commutes with conjugation

Artin reciprocity of the conjugate layer,
applied to the conjugate of a class modulo norms, is the conjugate of its Artin symbol.

```lean
TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_conj {G : Type} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  {F : TauCeti.ClassFieldTheory.Formation G} (cf : TauCeti.ClassFieldTheory.ClassFormation F)
  (L : TauCeti.ClassFieldTheory.NormalLayer G) (g : G) (y : L.NormQuotient F) :
  (cf.artinEquiv (L.conjugate g)) ((L.conjugateNormQuotientEquiv F g) y) =
    (MulEquiv.toAdditive (L.conjugateGalEquiv g).abelianizationCongr) ((cf.artinEquiv L) y)
```

## Depends on

- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Tate's isomorphism of a class formation commutes with conjugation](tates-isomorphism-of-a-class-formation-commutes.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../../part-01/class-field-theory/tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_conj`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/ArtinMap.html#TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_conj).

## Other forms

**Artin reciprocity is carried along a layer morphism matching the fundamental classes.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_layerHom`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Layer/Hom.html#TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_layerHom).

```lean
TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_layerHom {G : Type} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  {G' : Type} [Group G'] [TopologicalSpace G'] [IsTopologicalGroup G'] [CompactSpace G']
  [TotallyDisconnectedSpace G'] {F : TauCeti.ClassFieldTheory.Formation G}
  {L : TauCeti.ClassFieldTheory.NormalLayer G} {F' : TauCeti.ClassFieldTheory.Formation G'}
  {L' : TauCeti.ClassFieldTheory.NormalLayer G'} (cf : TauCeti.ClassFieldTheory.ClassFormation F)
  (cf' : TauCeti.ClassFieldTheory.ClassFormation F')
  (E : TauCeti.ClassFieldTheory.LayerHom F L F' L')
  (hu :
    (CategoryTheory.ConcreteCategory.hom (E.cohomologyMap 2)) (cf.fundamentalClass L) =
      cf'.fundamentalClass L')
  (y : L.NormQuotient F) :
  (cf'.artinEquiv L') (E.normQuotientMap y) =
    (MulEquiv.toAdditive E.galEquiv.abelianizationCongr) ((cf.artinEquiv L) y)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_conj`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/ArtinMap.html#TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_conj)
- [Source of `TauCeti.ClassFieldTheory.ClassFormation.artinEquiv_conj` in TauCeti/NumberTheory/ClassFieldTheory/Formation/ArtinMap.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Formation/ArtinMap.lean#L254)

---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.ClassFormation.artinMap_layerEquiv
statement: formalized
proof: formalized
---

# The Artin map is transported by a layer isomorphism matching the invariant maps

the Artin
symbol in `L'` of the image of `a` is the image under `(U/V)^ab ≃ (U'/V')^ab` of the Artin symbol
of `a` in `L`.

```lean
TauCeti.ClassFieldTheory.ClassFormation.artinMap_layerEquiv {G : Type} [Group G]
  [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  {G' : Type} [Group G'] [TopologicalSpace G'] [IsTopologicalGroup G'] [CompactSpace G']
  [TotallyDisconnectedSpace G'] {F : TauCeti.ClassFieldTheory.Formation G}
  {L : TauCeti.ClassFieldTheory.NormalLayer G} {F' : TauCeti.ClassFieldTheory.Formation G'}
  {L' : TauCeti.ClassFieldTheory.NormalLayer G'} (cf : TauCeti.ClassFieldTheory.ClassFormation F)
  (cf' : TauCeti.ClassFieldTheory.ClassFormation F')
  (E : TauCeti.ClassFieldTheory.LayerEquiv F L F' L')
  (hinv :
    ∀ (x : ↑(L.H F 2)),
      (cf'.inv L') ((CategoryTheory.ConcreteCategory.hom (E.cohomologyIso 2).hom) x) = (cf.inv L) x)
  (a : ↥(F.level L.ground)) :
  (cf'.artinMap L') (E.groundEquiv a) =
    (MulEquiv.toAdditive E.galEquiv.abelianizationCongr) ((cf.artinMap L) a)
```

## Depends on

- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Artin reciprocity is carried along a layer morphism matching the fundamental classes](artin-reciprocity-is-carried-along-a-layer-morph.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ClassFormation.artinMap_layerEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Layer/Equiv.html#TauCeti.ClassFieldTheory.ClassFormation.artinMap_layerEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.ClassFormation.artinMap_layerEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Layer/Equiv.html#TauCeti.ClassFieldTheory.ClassFormation.artinMap_layerEquiv)
- [Source of `TauCeti.ClassFieldTheory.ClassFormation.artinMap_layerEquiv` in TauCeti/NumberTheory/ClassFieldTheory/Formation/Layer/Equiv.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Formation/Layer/Equiv.lean#L336)

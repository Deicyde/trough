---
declaration: theorem
origin: cited
lean: TauCeti.TopCat.normalSpace_of_isPushout
statement: formalized
proof: formalized
---

# TauCeti.TopCat.normalSpace\_of\_isPushout

Attaching a normal space `B` to a normal space `X` along a closed subspace of `B` gives a
normal space: in a pushout square in `TopCat` whose side `m : A ⟶ B` is a closed embedding, the
corner `P` is normal.

```lean
TauCeti.TopCat.normalSpace_of_isPushout.{u} {A B X P : TopCat} {g : A ⟶ X} {m : A ⟶ B} {f : X ⟶ P}
  {g₂ : B ⟶ P} (sq : CategoryTheory.IsPushout g m f g₂)
  (hm : Topology.IsClosedEmbedding ⇑(CategoryTheory.ConcreteCategory.hom m)) [NormalSpace ↑X]
  [NormalSpace ↑B] : NormalSpace ↑P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TopCat.normalSpace_of_isPushout`](https://taucetiproject.org/docs/TauCeti/Topology/Category/TopCat/Normal.html#TauCeti.TopCat.normalSpace_of_isPushout).

## Sources

- [Tau Ceti documentation: `TauCeti.TopCat.normalSpace_of_isPushout`](https://taucetiproject.org/docs/TauCeti/Topology/Category/TopCat/Normal.html#TauCeti.TopCat.normalSpace_of_isPushout)
- [Source of `TauCeti.TopCat.normalSpace_of_isPushout` in TauCeti/Topology/Category/TopCat/Normal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Category/TopCat/Normal.lean#L68)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Orbifolds/STATUS.md)

---
declaration: theorem
origin: cited
lean: TauCeti.Amenable.of_isColimit
statement: formalized
proof: formalized
---

# TauCeti.Amenable.of_isColimit

The apex of a colimit cocone over a filtered diagram of amenable topological groups in `GrpCat`
is amenable, provided the legs of the cocone are continuous.

```lean
TauCeti.Amenable.of_isColimit.{u, v_1, u_1} {J : Type u_1} [CategoryTheory.Category.{v_1, u_1} J]
  [CategoryTheory.IsFiltered J] {F : CategoryTheory.Functor J GrpCat}
  [(j : J) → TopologicalSpace ↑(F.obj j)] {c : CategoryTheory.Limits.Cocone F}
  [TopologicalSpace ↑c.pt] [IsTopologicalGroup ↑c.pt] [∀ (j : J), IsTopologicalGroup ↑(F.obj j)]
  [∀ (j : J), TauCeti.Amenable ↑(F.obj j)] (hc : CategoryTheory.Limits.IsColimit c)
  (hcont : ∀ (j : J), Continuous ⇑(GrpCat.Hom.hom (c.ι.app j))) : TauCeti.Amenable ↑c.pt
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [TauCeti.amenable_iff_forall_finset_exists](tauceti-amenable-iff-forall-finset-exists.md)
- [TauCeti.UCB.leftTranslation](tauceti-ucb-lefttranslation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Amenable.of_isColimit`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Colimit.html#TauCeti.Amenable.of_isColimit).

## Sources

- [Tau Ceti documentation: `TauCeti.Amenable.of_isColimit`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/Colimit.html#TauCeti.Amenable.of_isColimit)
- [Source of `TauCeti.Amenable.of_isColimit` in TauCeti/GroupTheory/Amenable/Colimit.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/Colimit.lean#L62)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)

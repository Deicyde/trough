---
declaration: theorem
origin: cited
lean: TauCeti.Amenable.of_directed_of_iSup_eq_top
statement: formalized
proof: formalized
---

# TauCeti.Amenable.of_directed_of_iSup_eq_top

A topological group which is the union of a nonempty directed family of amenable subgroups is
amenable.

```lean
TauCeti.Amenable.of_directed_of_iSup_eq_top.{u_1, u_2} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] {ι : Type u_2} [Nonempty ι] {H : ι → Subgroup G}
  (hH : Directed (fun x1 x2 => x1 ≤ x2) H) (htop : ⨆ i, H i = ⊤)
  [∀ (i : ι), TauCeti.Amenable ↥(H i)] : TauCeti.Amenable G
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)

## Proof depends on

- [TauCeti.amenable_iff_forall_finset_exists](tauceti-amenable-iff-forall-finset-exists.md)
- [TauCeti.UCB.leftTranslation](tauceti-ucb-lefttranslation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Amenable.of_directed_of_iSup_eq_top`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/DirectedUnion.html#TauCeti.Amenable.of_directed_of_iSup_eq_top).

## Sources

- [Tau Ceti documentation: `TauCeti.Amenable.of_directed_of_iSup_eq_top`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/DirectedUnion.html#TauCeti.Amenable.of_directed_of_iSup_eq_top)
- [Source of `TauCeti.Amenable.of_directed_of_iSup_eq_top` in TauCeti/GroupTheory/Amenable/DirectedUnion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/DirectedUnion.lean#L87)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)

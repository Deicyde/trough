---
declaration: theorem
origin: cited
lean: TauCeti.Amenable.of_tendsto
statement: formalized
proof: formalized
---

# TauCeti.Amenable.of\_tendsto

Cluster-point criterion: a topological group is amenable when it carries means `ms i` which
are approximately left invariant along a nontrivial filter, that is, `ms i (L_g f) - ms i f → 0`
for every `g` and `f`.

```lean
TauCeti.Amenable.of_tendsto.{u_1, u_2} {G : Type u_1} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] {ι : Type u_2} {l : Filter ι} [l.NeBot] {ms : ι → TauCeti.Mean G}
  (h :
    ∀ (g : G) (f : TauCeti.UCB G),
      Filter.Tendsto (fun i => (ms i) ((TauCeti.UCB.leftTranslation g) f) - (ms i) f) l (nhds 0)) :
  TauCeti.Amenable G
```

## Depends on

- [TauCeti.Amenable](tauceti-amenable.md)
- [TauCeti.UCB.leftTranslation](tauceti-ucb-lefttranslation.md)

## Proof depends on

- [TauCeti.Mean.instCompactSpace](tauceti-mean-instcompactspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Amenable.of_tendsto`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/WeakStar.html#TauCeti.Amenable.of_tendsto).

## Sources

- [Tau Ceti documentation: `TauCeti.Amenable.of_tendsto`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Amenable/WeakStar.html#TauCeti.Amenable.of_tendsto)
- [Source of `TauCeti.Amenable.of_tendsto` in TauCeti/GroupTheory/Amenable/WeakStar.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Amenable/WeakStar.lean#L201)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AmenableGroups/STATUS.md)

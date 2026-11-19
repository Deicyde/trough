---
declaration: structure
origin: cited
lean: TauCeti.Hive.IsRhombus
statement: formalized
---

# TauCeti.Hive.IsRhombus

A unit rhombus in perimeter order, with `a,c` the obtuse (short-diagonal) corners.
All squared distances here use barycentric coordinates.

```lean
TauCeti.Hive.IsRhombus {n : ℕ} (a b c d : TauCeti.Hive.Vertex n) : Prop
```

## Depends on

- [TauCeti.Hive.Vertex](tauceti-hive-vertex.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hive.IsRhombus`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hive/Lattice.html#TauCeti.Hive.IsRhombus).

## Sources

- [Tau Ceti documentation: `TauCeti.Hive.IsRhombus`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hive/Lattice.html#TauCeti.Hive.IsRhombus)
- [Source of `TauCeti.Hive.IsRhombus` in TauCeti/Combinatorics/Hive/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Hive/Lattice.lean#L369)
- [Tau Ceti roadmap status: Hives, honeycombs, puzzles and type-A tensor products](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TensorProductCombinatorics/STATUS.md)

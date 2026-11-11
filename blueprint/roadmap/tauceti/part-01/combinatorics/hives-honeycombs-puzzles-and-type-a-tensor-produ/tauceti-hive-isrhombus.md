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
- [Source of `TauCeti.Hive.IsRhombus` in TauCeti/Combinatorics/Hive/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Hive/Lattice.lean#L204)
- [Tau Ceti roadmap status: Hives, honeycombs, puzzles and type-A tensor products](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TensorProductCombinatorics/STATUS.md)

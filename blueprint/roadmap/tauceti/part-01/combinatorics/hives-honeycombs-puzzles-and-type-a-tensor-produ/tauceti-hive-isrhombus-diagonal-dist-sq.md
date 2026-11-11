---
declaration: theorem
origin: cited
lean: TauCeti.Hive.IsRhombus.diagonal_dist_sq
statement: formalized
proof: formalized
---

# TauCeti.Hive.IsRhombus.diagonal_dist_sq

The planar squared lengths of the two diagonals are 1 and 3.

```lean
TauCeti.Hive.IsRhombus.diagonal_dist_sq {n : ℕ} {a b c d : TauCeti.Hive.Vertex n}
  (h : TauCeti.Hive.IsRhombus a b c d) : dist a.plane c.plane ^ 2 = 1 ∧ dist b.plane d.plane ^ 2 = 3
```

## Depends on

- [TauCeti.Hive.IsRhombus](tauceti-hive-isrhombus.md)
- [TauCeti.Hive.Vertex](tauceti-hive-vertex.md)
- [TauCeti.Hive.Vertex.plane](tauceti-hive-vertex-plane.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hive.IsRhombus.diagonal_dist_sq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hive/Lattice.html#TauCeti.Hive.IsRhombus.diagonal_dist_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.Hive.IsRhombus.diagonal_dist_sq`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hive/Lattice.html#TauCeti.Hive.IsRhombus.diagonal_dist_sq)
- [Source of `TauCeti.Hive.IsRhombus.diagonal_dist_sq` in TauCeti/Combinatorics/Hive/Lattice.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Combinatorics/Hive/Lattice.lean#L305)
- [Tau Ceti roadmap status: Hives, honeycombs, puzzles and type-A tensor products](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TensorProductCombinatorics/STATUS.md)

---
declaration: def
origin: cited
lean: ZLattice.successiveMin
statement: formalized
---

# ZLattice.successiveMin

The successive minima of a `ℤ`-submodule `L` of `E` with respect to a convex body `K`, indexed
from zero: `successiveMin L K i` is the infimum of the dilation factors `t ≥ 0` for which `t • K`
contains `i + 1` vectors of `L` that are linearly independent over `ℝ`.

When no dilate of `K` contains `i + 1` independent vectors of `L` (for instance when `L` has rank
at most `i`, or when `K` is a segment containing `0` and `1 ≤ i`), the infimum is over the empty
set and `successiveMin L K i` takes the junk value `sInf ∅ = 0`; the minima then need not be
positive or monotone. For a discrete spanning lattice `L` and `0` in the interior of `K`, the
hypotheses of the main results, the set is nonempty and the infimum is attained
(`ZLattice.successiveMin_isLeast`).

```lean
ZLattice.successiveMin.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (L : Submodule ℤ E) (K : ConvexBody E) (i : Fin (Module.finrank ℝ E)) : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ZLattice.successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#ZLattice.successiveMin).

## Sources

- [Tau Ceti documentation: `ZLattice.successiveMin`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.html#ZLattice.successiveMin)
- [Source of `ZLattice.successiveMin` in TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/ZLattice/SuccessiveMinima.lean#L101)
- [Tau Ceti roadmap status: Heights, units and S-units of number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HeightsAndUnits/STATUS.md)

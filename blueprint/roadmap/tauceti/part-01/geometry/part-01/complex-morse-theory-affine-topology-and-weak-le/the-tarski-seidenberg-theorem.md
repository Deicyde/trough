---
declaration: theorem
origin: cited
lean: TauCeti.instHasSemialgebraicProjectionsReal
statement: formalized
proof: formalized
---

# The Tarski–Seidenberg theorem

The projection of a semialgebraic subset of `ℝ ^ (n + 1)`
forgetting the coordinate `0` is semialgebraic. So quantifier elimination, the identification of
semialgebraic sets with definable sets, and the image and composition laws of semialgebraic
functions, which assume `HasSemialgebraicProjections`, hold over `ℝ` unconditionally.

```lean
TauCeti.instHasSemialgebraicProjectionsReal : TauCeti.HasSemialgebraicProjections ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Existence of adapted cylindrical algebraic decompositions](../real-algebraic-geometry-sign-determination-and-c/existence-of-adapted-cylindrical-algebraic-decom.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.instHasSemialgebraicProjectionsReal`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Existence.html#TauCeti.instHasSemialgebraicProjectionsReal).

## Sources

- [Tau Ceti documentation: `TauCeti.instHasSemialgebraicProjectionsReal`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/CAD/Existence.html#TauCeti.instHasSemialgebraicProjectionsReal)
- [Source of `TauCeti.instHasSemialgebraicProjectionsReal` in TauCeti/Geometry/RealAlgebraic/CAD/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/CAD/Existence.lean#L98)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/RealAlgebraicGeometry/STATUS.md)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)

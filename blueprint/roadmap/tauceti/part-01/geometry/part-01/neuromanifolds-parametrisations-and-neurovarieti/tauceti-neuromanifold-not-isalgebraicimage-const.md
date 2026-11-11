---
declaration: theorem
origin: cited
lean: TauCeti.Neuromanifold.not_isAlgebraicImage_const_sq
statement: formalized
proof: formalized
---

# TauCeti.Neuromanifold.not_isAlgebraicImage_const_sq

The coefficient image of the real scalar model `g_w(x) = w² x` is not algebraic: its
neurovariety contains the coefficient `-1`, which is not a square.

```lean
TauCeti.Neuromanifold.not_isAlgebraicImage_const_sq :
  ¬TauCeti.Neuromanifold.IsAlgebraicImage fun w => Function.const Unit (w ^ 2)
```

## Depends on

- [TauCeti.Neuromanifold.IsAlgebraicImage](tauceti-neuromanifold-isalgebraicimage.md)

## Proof depends on

- [TauCeti.Neuromanifold.neurovariety](tauceti-neuromanifold-neurovariety.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Neuromanifold.not_isAlgebraicImage_const_sq`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Scalar.html#TauCeti.Neuromanifold.not_isAlgebraicImage_const_sq).

## Sources

- [Tau Ceti documentation: `TauCeti.Neuromanifold.not_isAlgebraicImage_const_sq`](https://taucetiproject.org/docs/TauCeti/Geometry/Neuromanifold/Scalar.html#TauCeti.Neuromanifold.not_isAlgebraicImage_const_sq)
- [Source of `TauCeti.Neuromanifold.not_isAlgebraicImage_const_sq` in TauCeti/Geometry/Neuromanifold/Scalar.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Neuromanifold/Scalar.lean#L136)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Neuromanifolds/STATUS.md)

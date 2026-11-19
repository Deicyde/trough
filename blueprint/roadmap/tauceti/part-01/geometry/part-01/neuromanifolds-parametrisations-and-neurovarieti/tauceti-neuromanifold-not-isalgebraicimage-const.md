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
- [Source of `TauCeti.Neuromanifold.not_isAlgebraicImage_const_sq` in TauCeti/Geometry/Neuromanifold/Scalar.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Neuromanifold/Scalar.lean#L136)
- [Tau Ceti roadmap status: Neuromanifolds, parametrisations, and neurovarieties](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Neuromanifolds/STATUS.md)

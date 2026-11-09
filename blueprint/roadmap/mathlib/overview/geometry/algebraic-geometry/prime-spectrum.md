# Prime spectrum

The prime spectrum of a commutative (semi)ring `R` is the type of all prime ideals of `R`.

It is naturally endowed with a topology (the Zariski topology),
and a sheaf of commutative rings (see `Mathlib/AlgebraicGeometry/StructureSheaf.lean`).
It is a fundamental building block in algebraic geometry.

```lean
PrimeSpectrum.{u_1} (R : Type u_1) [CommSemiring R] : Type u_1
```

## Depends on

- [Natural number](../../general-algebra/numbers/natural-number.md)
- [Prime ideal](../../general-algebra/ideals-and-quotients/prime-ideal.md)

## Sources

- [Mathlib documentation: `PrimeSpectrum`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Spectrum/Prime/Defs.html#PrimeSpectrum)
- [Source of `PrimeSpectrum` in Mathlib/RingTheory/Spectrum/Prime/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/RingTheory/Spectrum/Prime/Defs.lean#L28)
- [Mathlib overview: Geometry › Algebraic geometry](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/overview.yaml#L481)

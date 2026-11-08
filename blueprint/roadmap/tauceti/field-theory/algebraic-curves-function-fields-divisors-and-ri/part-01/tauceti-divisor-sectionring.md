---
declaration: abbrev
origin: cited
lean: TauCeti.Divisor.sectionRing
statement: formalized
---

# TauCeti.Divisor.sectionRing

The **section ring** `⨁ₙ L(nD)` of a divisor `D`: the `k`-subalgebra of `F[X]` of polynomials
`∑ fₙ Xⁿ` with `fₙ ∈ L(nD)` for every `n`.

It is an abbreviation for `TauCeti.coeffSubalgebra` of the family `n ↦ L(nD)`, so that the
grading and its API apply to it directly.

```lean
TauCeti.Divisor.sectionRing.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k] [Field F]
  [Algebra k F] (D : TauCeti.Divisor k F) : Subalgebra k (Polynomial F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Divisor.sectionRing`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/SectionRing.html#TauCeti.Divisor.sectionRing).

## Sources

- [Tau Ceti documentation: `TauCeti.Divisor.sectionRing`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/SectionRing.html#TauCeti.Divisor.sectionRing)
- [Source of `TauCeti.Divisor.sectionRing` in TauCeti/FieldTheory/FunctionField/RiemannRoch/SectionRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/RiemannRoch/SectionRing.lean#L122)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicCurves/STATUS.md)

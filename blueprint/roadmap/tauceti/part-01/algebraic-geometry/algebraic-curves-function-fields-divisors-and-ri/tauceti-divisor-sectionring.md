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
- [Source of `TauCeti.Divisor.sectionRing` in TauCeti/FieldTheory/FunctionField/RiemannRoch/SectionRing.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/RiemannRoch/SectionRing.lean#L122)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicCurves/STATUS.md)

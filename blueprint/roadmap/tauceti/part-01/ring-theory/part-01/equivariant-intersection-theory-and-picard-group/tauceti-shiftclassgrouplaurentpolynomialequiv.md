---
declaration: def
origin: cited
lean: TauCeti.shiftClassGroupLaurentPolynomialEquiv
statement: formalized
---

# TauCeti.shiftClassGroupLaurentPolynomialEquiv

For the Laurent ring `R[T;T⁻¹]` over a nontrivial commutative semiring, graded with `T` of
degree `w`, the degrees of the homogeneous units are the multiples of `w` (by
`homogeneousUnitDegrees_gradeBy`), so the shift class group is `ZMod |w|`. This is the graded ring
of `𝔾_m` acting on itself by `s • x = s ^ w * x`.

```lean
TauCeti.shiftClassGroupLaurentPolynomialEquiv.{u_1} (R : Type u_1) [CommSemiring R] [Nontrivial R]
  (w : ℤ) :
  TauCeti.ShiftClassGroup (AddMonoidAlgebra.gradeBy R ⇑((zmultiplesHom ℤ) w)) ≃+ ZMod w.natAbs
```

## Depends on

- [TauCeti.homogeneousUnitDegrees](tauceti-homogeneousunitdegrees.md)
- [TauCeti.ShiftClassGroup](tauceti-shiftclassgroup.md)

## Proof depends on

- [TauCeti.homogeneousUnitDegrees_gradeBy](tauceti-homogeneousunitdegrees-gradeby.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.shiftClassGroupLaurentPolynomialEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Laurent/Units.html#TauCeti.shiftClassGroupLaurentPolynomialEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.shiftClassGroupLaurentPolynomialEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Laurent/Units.html#TauCeti.shiftClassGroupLaurentPolynomialEquiv)
- [Source of `TauCeti.shiftClassGroupLaurentPolynomialEquiv` in TauCeti/Algebra/Polynomial/Laurent/Units.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Polynomial/Laurent/Units.lean#L107)
- [Tau Ceti roadmap status: Equivariant intersection theory and Picard groups of quotient stacks](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EquivariantIntersectionTheory/STATUS.md)

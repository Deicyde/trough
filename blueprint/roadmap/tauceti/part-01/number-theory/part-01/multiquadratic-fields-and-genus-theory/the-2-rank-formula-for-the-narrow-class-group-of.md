---
declaration: theorem
origin: cited
lean: TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one
statement: formalized
proof: formalized
---

# The `2`-rank formula for the narrow class group of a quadratic field

For `K = ℚ(√d)` with
`d` squarefree, of either signature, the `2`-rank of `Cl⁺(K)` is exactly `t - 1`, where `t` is the
number of rational primes ramifying in `K`. For an imaginary `K` the narrow and ordinary class
groups coincide, and this recovers `twoRank_eq_ncard_ramifiedPrimes_sub_one`; that identity is also
how the Gaussian field `d = -1`, which the ambiguous class number bound excludes, is covered.

```lean
TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one.{u_1} {K : Type u_1} [Field K]
  [NumberField K] {θ : NumberField.RingOfIntegers K} {d : ℤ}
  (hmin : minpoly ℤ θ = Polynomial.X ^ 2 - Polynomial.C d) (hgen : ℚ[↑θ] = ⊤) (hsf : Squarefree d) :
  NumberField.NarrowClassGroup.twoRank K = (NumberField.ramifiedPrimes K).ncard - 1
```

## Depends on

- [NumberField.NarrowClassGroup](numberfield-narrowclassgroup.md)

## Proof depends on

- [Dirichlet's theorem for prime-discriminant characters](../../part-02/multiquadratic/dirichlets-theorem-for-prime-discriminant-charac.md)
- [Dirichlet's unit theorem (`NumberField.fg_units_integralClosure`)](../../part-02/number-field/dirichlets-unit-theorem-numberfield-fg-units-int.md)
- [The genus character on the narrow class group](the-genus-character-on-the-narrow-class-group.md)
- [Hilbert's Theorem 90 for quadratic conjugation](../../part-02/number-field/hilberts-theorem-90-for-quadratic-conjugation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Quadratic/TwoRank.html#TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Quadratic/TwoRank.html#TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one)
- [Source of `TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one` in TauCeti/NumberTheory/Multiquadratic/Quadratic/TwoRank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Multiquadratic/Quadratic/TwoRank.lean#L256)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Multiquadratic/STATUS.md)

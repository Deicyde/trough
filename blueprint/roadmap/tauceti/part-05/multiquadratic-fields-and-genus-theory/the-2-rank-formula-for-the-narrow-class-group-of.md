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

- [The genus character on the narrow class group](the-genus-character-on-the-narrow-class-group.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Quadratic/TwoRank.html#TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one).

## Sources

- [Tau Ceti documentation: `TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiquadratic/Quadratic/TwoRank.html#TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one)
- [Source of `TauCeti.Multiquadratic.narrowTwoRank_eq_ncard_ramifiedPrimes_sub_one` in TauCeti/NumberTheory/Multiquadratic/Quadratic/TwoRank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Multiquadratic/Quadratic/TwoRank.lean#L234)
- [Tau Ceti roadmap status: Multiquadratic fields and genus theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Multiquadratic/STATUS.md)

---
declaration: theorem
origin: cited
lean: TauCeti.sq_sum_range_cexp_two_pi_I_mul_sq_div
statement: formalized
proof: formalized
---

# The squared Landsberg–Schaar identity

For a positive integer `a` and a natural number `c`,
`(∑_{u < c} e(a u² / c))² = (c / (2a)) · i · (∑_{u < 2a} e(-c u² / (4a)))²`.
This is the reciprocity law `ZLattice.IsEven.gaussSum_eq_mul_dualGaussSum` for the lattice
`L = √2 ℤ²` of rank `2`, with covolume `2`, whose two Gauss sums are the squares of the
one-variable sums. The Landsberg–Schaar identity itself,
`∑_{u < c} e(a u² / c) = √(c / (2a)) e(1/8) ∑_{u < 2a} e(-c u² / (4a))`, is the case of rank one,
which is not covered by the reciprocity law of even rank.

```lean
TauCeti.sq_sum_range_cexp_two_pi_I_mul_sq_div (a c : ℕ) [NeZero a] :
  (∑ u ∈ Finset.range c, Complex.exp (2 * ↑Real.pi * Complex.I * ↑a * ↑u ^ 2 / ↑c)) ^ 2 =
    ↑c / (2 * ↑a) * Complex.I *
      (∑ u ∈ Finset.range (2 * a),
          Complex.exp (-(2 * ↑Real.pi * Complex.I * ↑c * ↑u ^ 2 / (4 * ↑a)))) ^
        2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inversion law of theta series](the-inversion-law-of-theta-series.md)
- [Poisson's summation formula](../../../analysis/part-02/fourier/poissons-summation-formula.md)
- [ZLattice.gaussSum](zlattice-gausssum.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sq_sum_range_cexp_two_pi_I_mul_sq_div`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/SqrtTwoCubic.html#TauCeti.sq_sum_range_cexp_two_pi_I_mul_sq_div).

## Sources

- [Tau Ceti documentation: `TauCeti.sq_sum_range_cexp_two_pi_I_mul_sq_div`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/SqrtTwoCubic.html#TauCeti.sq_sum_range_cexp_two_pi_I_mul_sq_div)
- [Source of `TauCeti.sq_sum_range_cexp_two_pi_I_mul_sq_div` in TauCeti/NumberTheory/ModularForms/ThetaSeries/SqrtTwoCubic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/ThetaSeries/SqrtTwoCubic.lean#L331)

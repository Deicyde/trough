---
declaration: theorem
origin: cited
lean: TauCeti.Probability.gammaPDFReal_mul_multivariateGaussianPDFReal
statement: formalized
proof: formalized
---

# The Gamma–Gaussian density identity

On the positive half-line,
the Gamma density of the precision `τ` (shape and rate `ν / 2`) times the density of
`N(a, τ⁻¹ • R)` at `x` factors as the multivariate t density at `x` times the Gamma density of
shape `(ν + d) / 2` and rate `(ν + q) / 2` at `τ`, where `q` is the Mahalanobis form of `x - a`.

```lean
TauCeti.Probability.gammaPDFReal_mul_multivariateGaussianPDFReal.{u_1} {ι : Type u_1} [Fintype ι]
  [DecidableEq ι] {ν : ℝ} (a : EuclideanSpace ℝ ι) {R : Matrix ι ι ℝ} (hR : R.PosDef) (hν : 0 < ν)
  {τ : ℝ} (hτ : 0 < τ) (x : EuclideanSpace ℝ ι) :
  ProbabilityTheory.gammaPDFReal (ν / 2) (ν / 2) τ *
      TauCeti.Probability.multivariateGaussianPDFReal a (τ⁻¹ • R) x =
    TauCeti.Probability.multivariateTPDFReal a R ν x *
      ProbabilityTheory.gammaPDFReal ((ν + ↑(Fintype.card ι)) / 2)
        ((ν + inner ℝ (x - a) ((Matrix.toEuclideanLin R⁻¹) (x - a))) / 2) τ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Probability.gammaPDFReal_mul_multivariateGaussianPDFReal`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/MultivariateT/PDF.html#TauCeti.Probability.gammaPDFReal_mul_multivariateGaussianPDFReal).

## Sources

- [Tau Ceti documentation: `TauCeti.Probability.gammaPDFReal_mul_multivariateGaussianPDFReal`](https://taucetiproject.org/docs/TauCeti/Probability/Distributions/MultivariateT/PDF.html#TauCeti.Probability.gammaPDFReal_mul_multivariateGaussianPDFReal)
- [Source of `TauCeti.Probability.gammaPDFReal_mul_multivariateGaussianPDFReal` in TauCeti/Probability/Distributions/MultivariateT/PDF.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Probability/Distributions/MultivariateT/PDF.lean#L308)

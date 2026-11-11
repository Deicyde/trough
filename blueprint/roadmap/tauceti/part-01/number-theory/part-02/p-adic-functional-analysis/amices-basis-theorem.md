---
declaration: theorem
origin: cited
lean: TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm
statement: formalized
proof: formalized
---

# Amice's basis theorem

The disc expansions `amiceTerm p h n 1` of Amice's polynomials
`e_{h,n}(x) = ⌊n / pʰ⌋! (x choose n)` form an orthonormal basis of `LA_h(ℤ_p)`.

```lean
TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm (p : ℕ) [hp : Fact (Nat.Prime p)] (h : ℕ) :
  TauCeti.IsOrthonormalBasis ℤ_[p] fun n => TauCeti.AnalyticStage.amiceTerm p h n 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Amice's theorem](amices-theorem.md)
- [Legendre's formula for `(pᵏ)!`](../padics/legendres-formula-for-pk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm)
- [Source of `TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm` in TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean#L198)

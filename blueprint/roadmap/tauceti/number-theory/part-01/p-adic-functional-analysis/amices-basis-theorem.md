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
- [Legendre's formula for `(pᵏ)!`](../../part-02/padics/legendres-formula-for-pk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm)
- [Source of `TauCeti.AnalyticStage.isOrthonormalBasis_amiceTerm` in TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean#L198)

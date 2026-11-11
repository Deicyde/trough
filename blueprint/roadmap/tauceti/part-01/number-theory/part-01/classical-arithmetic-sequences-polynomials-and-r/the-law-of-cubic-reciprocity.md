---
declaration: theorem
origin: cited
lean: TauCeti.IsPrimaryEisenstein.cubic_reciprocity
statement: formalized
proof: formalized
---

# The law of cubic reciprocity

Let `K = ℚ(ζ₃)`, so that `𝓞 K = ℤ[ω]`, and let `π₁` and `π₂`
be primary primes of `𝓞 K` with different norms. Then `(π₂ / π₁)_3 = (π₁ / π₂)_3`, the cubic
residue symbols being taken at the ideals `π₁ 𝓞 K` and `π₂ 𝓞 K`. A primary element is prime to
`3`, so neither symbol is taken at the prime above `3`.

```lean
TauCeti.IsPrimaryEisenstein.cubic_reciprocity.{u_1} {K : Type u_1} [Field K] [NumberField K]
  [IsCyclotomicExtension {3} ℚ K] {π₁ π₂ : NumberField.RingOfIntegers K}
  (hπ₁ : TauCeti.IsPrimaryEisenstein π₁) (hπ₂ : TauCeti.IsPrimaryEisenstein π₂) (hp₁ : Prime π₁)
  (hp₂ : Prime π₂) (hN : (Algebra.norm ℤ) π₁ ≠ (Algebra.norm ℤ) π₂) :
  ((Ideal.span {π₁}).powerResidueSymbolIdeal 3) ((Ideal.Quotient.mk (Ideal.span {π₁})) π₂) =
    ((Ideal.span {π₂}).powerResidueSymbolIdeal 3) ((Ideal.Quotient.mk (Ideal.span {π₂})) π₁)
```

## Depends on

- [The `n`-th power residue symbol at an ideal](the-n-th-power-residue-symbol-at-an-ideal.md)

## Proof depends on

- [The Gauss sum power `Φ(A) ∈ 𝓞 K` of an ideal `A` of `𝓞 K`](the-gauss-sum-power-a-o-k-of-an-ideal-a-of-o-k.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsPrimaryEisenstein.cubic_reciprocity`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Cyclotomic/Three/CubicReciprocity.html#TauCeti.IsPrimaryEisenstein.cubic_reciprocity).

## Sources

- [Tau Ceti documentation: `TauCeti.IsPrimaryEisenstein.cubic_reciprocity`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Cyclotomic/Three/CubicReciprocity.html#TauCeti.IsPrimaryEisenstein.cubic_reciprocity)
- [Source of `TauCeti.IsPrimaryEisenstein.cubic_reciprocity` in TauCeti/NumberTheory/NumberField/Cyclotomic/Three/CubicReciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Cyclotomic/Three/CubicReciprocity.lean#L140)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)

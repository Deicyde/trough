---
declaration: def
origin: cited
lean: Ideal.stickelbergerPhi
statement: formalized
---

# The Gauss sum power `Φ(A) ∈ 𝓞 K` of an ideal `A` of `𝓞 K`

If `A = P₁ ⋯ Pᵣ` is the
factorisation of `A` into maximal ideals, `Φ(A)` is the product of the `Φ(Pᵢ)` over the factors
whose norm is prime to `m`. For `m ≥ 2`, `Φ(P) = g(χ_P, ψ)^m` is the `m`-th power of the Gauss
sum of `χ_P = (· / P)_m⁻¹` with any primitive additive character `ψ`
(`Ideal.stickelbergerPhi_prime`); for `m = 1`, `Φ(P)` is just the Jacobi-sum expression of
`Ideal.stickelbergerPhi_eq_mul_prod_jacobiSum`.

```lean
Ideal.stickelbergerPhi.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (A : Ideal (NumberField.RingOfIntegers K)) (m : ℕ) [NeZero m]
  [HasEnoughRootsOfUnity (NumberField.RingOfIntegers K) m] : NumberField.RingOfIntegers K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ideal.stickelbergerPhi`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/PowerResidueSymbol/StickelbergerPhi/Basic.html#Ideal.stickelbergerPhi).

## Sources

- [Tau Ceti documentation: `Ideal.stickelbergerPhi`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/PowerResidueSymbol/StickelbergerPhi/Basic.html#Ideal.stickelbergerPhi)
- [Source of `Ideal.stickelbergerPhi` in TauCeti/NumberTheory/NumberField/PowerResidueSymbol/StickelbergerPhi/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/PowerResidueSymbol/StickelbergerPhi/Basic.lean#L103)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)

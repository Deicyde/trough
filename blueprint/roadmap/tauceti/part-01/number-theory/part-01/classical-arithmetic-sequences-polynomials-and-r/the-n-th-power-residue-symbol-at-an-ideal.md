---
declaration: def
origin: cited
lean: Ideal.powerResidueSymbolIdeal
statement: formalized
---

# The `n`-th power residue symbol at an ideal

**The `n`-th power residue symbol at an ideal** `𝔞` of `𝓞 K`, as a multiplicative character of
`𝓞 K ⧸ 𝔞` with values in `𝓞 K`. If `𝔞 = P₁ ⋯ Pᵣ` is the factorisation of `𝔞` into maximal
ideals, it sends the class of `α` coprime to `𝔞` to `∏ᵢ (α / Pᵢ)_n`, and it vanishes on the
classes not coprime to `𝔞`.

```lean
Ideal.powerResidueSymbolIdeal.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (𝔞 : Ideal (NumberField.RingOfIntegers K)) (n : ℕ) [NeZero n]
  [HasEnoughRootsOfUnity (NumberField.RingOfIntegers K) n] :
  MulChar (NumberField.RingOfIntegers K ⧸ 𝔞) (NumberField.RingOfIntegers K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ideal.powerResidueSymbolIdeal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/PowerResidueSymbol/Ideal.html#Ideal.powerResidueSymbolIdeal).

## Sources

- [Tau Ceti documentation: `Ideal.powerResidueSymbolIdeal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/PowerResidueSymbol/Ideal.html#Ideal.powerResidueSymbolIdeal)
- [Source of `Ideal.powerResidueSymbolIdeal` in TauCeti/NumberTheory/NumberField/PowerResidueSymbol/Ideal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/PowerResidueSymbol/Ideal.lean#L90)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)

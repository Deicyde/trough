---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.ncard_primesOverOfInertiaDeg_le
statement: formalized
proof: formalized
---

# The Kummer–Dedekind counting bound

For a `θ` whose conductor exponent is prime to `p`,
the primes of `𝓞 K` above `p` with residue degree `d` are no more numerous than the degree-`d`
monic irreducible factors of `minpoly ℤ θ` modulo `p`.

```lean
TauCeti.NumberField.ncard_primesOverOfInertiaDeg_le.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (p : ℕ) [Fact (Nat.Prime p)] {θ : NumberField.RingOfIntegers K}
  (hp : ¬p ∣ RingOfIntegers.exponent θ) (d : ℕ) :
  (TauCeti.NumberField.primesOverOfInertiaDeg K p d).ncard ≤
    {Q ∈ RingOfIntegers.monicFactorsMod θ p | Q.natDegree = d}.card
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.ncard_primesOverOfInertiaDeg_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Index/CommonIndexDivisor.html#TauCeti.NumberField.ncard_primesOverOfInertiaDeg_le).

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.ncard_primesOverOfInertiaDeg_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Index/CommonIndexDivisor.html#TauCeti.NumberField.ncard_primesOverOfInertiaDeg_le)
- [Source of `TauCeti.NumberField.ncard_primesOverOfInertiaDeg_le` in TauCeti/NumberTheory/NumberField/Index/CommonIndexDivisor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Index/CommonIndexDivisor.lean#L155)

---
declaration: theorem
origin: cited
lean: Polynomial.hasseDeriv_prod_mem_ideal_pow
statement: formalized
proof: formalized
---

# Hasse derivatives of a product in an ideal power (IK, Lemma 11.14 and (11.22))

if every
Hasse derivative of order at most `K` of each of the `card ι` factors `f i` evaluates into `J` at
`a`, then every Hasse derivative of order at most `K` of the product with an arbitrary cofactor
`g` evaluates into `J ^ card ι`.

```lean
Polynomial.hasseDeriv_prod_mem_ideal_pow.{u_1, u_2} {R : Type u_1} {ι : Type u_2} [CommSemiring R]
  [Fintype ι] (f : ι → Polynomial R) (g : Polynomial R) (a : R) (J : Ideal R) (K : ℕ)
  (hf : ∀ (i : ι), ∀ k ≤ K, Polynomial.eval a ((Polynomial.hasseDeriv k) (f i)) ∈ J) (k : ℕ) :
  k ≤ K → Polynomial.eval a ((Polynomial.hasseDeriv k) (g * ∏ i, f i)) ∈ J ^ Fintype.card ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.hasseDeriv_prod_mem_ideal_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/DerivativeIdealPow.html#Polynomial.hasseDeriv_prod_mem_ideal_pow).

## Sources

- [Tau Ceti documentation: `Polynomial.hasseDeriv_prod_mem_ideal_pow`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/DerivativeIdealPow.html#Polynomial.hasseDeriv_prod_mem_ideal_pow)
- [Source of `Polynomial.hasseDeriv_prod_mem_ideal_pow` in TauCeti/RingTheory/Polynomial/DerivativeIdealPow.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Polynomial/DerivativeIdealPow.lean#L72)
- [Tau Ceti roadmap status: Polynomial interpolation and arithmetic determinants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ArithmeticInterpolationDeterminants/STATUS.md)

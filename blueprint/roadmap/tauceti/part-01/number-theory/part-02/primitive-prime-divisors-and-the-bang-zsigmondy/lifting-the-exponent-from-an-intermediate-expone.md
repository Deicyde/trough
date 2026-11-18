---
declaration: theorem
origin: cited
lean: Nat.multiplicity_pow_sub_pow_of_dvd_pow_sub_pow
statement: formalized
proof: formalized
---

# Lifting the exponent from an intermediate exponent `d`

for an odd prime `p` and `y < x`
with `p ∣ x ^ d - y ^ d`, `p ∤ x` and `p ∤ d`, every nonzero multiple `n` of `d` satisfies
`v_p(x ^ n - y ^ n) = v_p(x ^ d - y ^ d) + v_p(n)`. Taking for `d` the order of `x / y` modulo
`p` gives the valuation of `x ^ n - y ^ n` at every exponent `n` it divides.

```lean
Nat.multiplicity_pow_sub_pow_of_dvd_pow_sub_pow {p : ℕ} [hp : Fact (Nat.Prime p)] (hp1 : Odd p)
  {x y d n : ℕ} (hyx : y < x) (hxy : p ∣ x ^ d - y ^ d) (hx : ¬p ∣ x) (hd : ¬p ∣ d) (hdn : d ∣ n)
  (hn : n ≠ 0) : multiplicity p (x ^ n - y ^ n) = multiplicity p (x ^ d - y ^ d) + multiplicity p n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Nat.multiplicity_pow_sub_pow_of_dvd_pow_sub_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiplicity.html#Nat.multiplicity_pow_sub_pow_of_dvd_pow_sub_pow).

## Sources

- [Tau Ceti documentation: `Nat.multiplicity_pow_sub_pow_of_dvd_pow_sub_pow`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Multiplicity.html#Nat.multiplicity_pow_sub_pow_of_dvd_pow_sub_pow)
- [Source of `Nat.multiplicity_pow_sub_pow_of_dvd_pow_sub_pow` in TauCeti/NumberTheory/Multiplicity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Multiplicity.lean#L89)
- [Tau Ceti roadmap status: Primitive prime divisors and the Bang–Zsigmondy theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PrimitivePrimeDivisors/STATUS.md)

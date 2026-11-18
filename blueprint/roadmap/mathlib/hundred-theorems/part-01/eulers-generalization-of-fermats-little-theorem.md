# Euler’s Generalization of Fermat’s Little Theorem

The **Fermat-Euler totient theorem**. `ZMod.pow_totient` is an alternative statement
of the same theorem.

```lean
Nat.ModEq.pow_totient {x n : ℕ} (h : x.Coprime n) : x ^ n.totient ≡ 1 [MOD n]
```

## Depends on

- [Euler's totient function ($\varphi$)](../../overview/general-algebra/divisibility-in-integral-domains/eulers-totient-function-varphi.md)

## Proof depends on

- [Finite set](../../overview/data-structures/sets/finite-set.md)

## Sources

- [Mathlib documentation: `Nat.ModEq.pow_totient`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/FieldTheory/Finite/Basic.html#Nat.ModEq.pow_totient)
- [Source of `Nat.ModEq.pow_totient` in Mathlib/FieldTheory/Finite/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/FieldTheory/Finite/Basic.lean#L529)
- [Freek Wiedijk's 100 theorems, no. 10](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/100.yaml#L54)
- [1000+ theorems list: Q193910](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/1000.yaml#L182)
- [1000+ theorems project: Q193910](https://1000-plus.github.io/all.html?length=-1#Q193910)
- [Wikipedia: Euler's theorem](https://en.wikipedia.org/wiki/Euler's_theorem)
- [Wikidata: Q193910](https://www.wikidata.org/wiki/Q193910)

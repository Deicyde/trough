---
declaration: theorem
origin: cited
lean: DubnerConjecture.dubner_conjecture
statement: formalized
---

# Dubner's conjecture

> *Reference*: [Every even number greater than 4208 is the sum of two t-primes](https://scispace.com/pdf/twin-prime-conjectures-3icaxy6b0m.pdf)
> by *Harvey Dubner*.

*Quoted from [FormalConjectures/Paper/Dubner.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/Dubner.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 5 test statements, counted here but not shown.

## `DubnerConjecture.dubner_conjecture`

Open: stated without proof.

> Every even number greater than 4208 is the sum of two twin primes.

```lean
theorem dubner_conjecture (n : ℕ) (hn : 4208 < n) (h : Even n) :
    ∃ p q : ℕ,
      IsTwinPrime p ∧
      IsTwinPrime q ∧
      p + q = n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/Dubner.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/Dubner.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/Dubner.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Paper/Dubner.lean)
- [Every even number greater than 4208 is the sum of two t-primes](https://scispace.com/pdf/twin-prime-conjectures-3icaxy6b0m.pdf)

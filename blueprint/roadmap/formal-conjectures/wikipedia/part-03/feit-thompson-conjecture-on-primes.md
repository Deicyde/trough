---
declaration: theorem
origin: cited
lean: FeitThompsonPrimeConjecture.feit_thompson_primes
statement: formalized
---

# Feit-Thompson conjecture on primes

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Feit%E2%80%93Thompson_conjecture)

*Quoted from [FormalConjectures/Wikipedia/FeitThompsonPrimeConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FeitThompsonPrimeConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `FeitThompsonPrimeConjecture.feit_thompson_primes`

Open: stated without proof.

> There are no distinct primes $p$ and $q$ such that $\frac{q^p - 1}{q - 1}$ divides $\frac{p^q - 1}{p - 1}$

```lean
theorem feit_thompson_primes (p q : ℕ) (hp : p.Prime) (hq : q.Prime) (h : p < q) :
    ¬ (q ^ p - 1) / (q - 1) ∣ (p ^ q - 1) / (p - 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/FeitThompsonPrimeConjecture.lean, line 34](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FeitThompsonPrimeConjecture.lean#L34).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/FeitThompsonPrimeConjecture.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/FeitThompsonPrimeConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Feit%E2%80%93Thompson_conjecture)

---
declaration: theorem
origin: cited
lean: Grimm.grimm_conjecture, Grimm.grimm_conjecture_weak
statement: formalized
---

# Grimm's conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Grimm%27s_conjecture)

*Quoted from [FormalConjectures/Wikipedia/Grimm.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Grimm.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open.

## `Grimm.grimm_conjecture`

Open: stated without proof.

> **Grimm's Conjecture**
> If $n, n+1, \dots, n+k-1$ are all composite numbers, then there are $k$ distinct primes $p_i$
> such that $p_i$ divides $n + i$ for all $0 \le i \le k-1$.

```lean
theorem grimm_conjecture (n k : ℕ) (hn : 1 ≤ n) (hk : 1 ≤ k)
    (h : ∀ i : Fin k, (n + i).Composite) :
    ∃ ps : Fin k ↪ ℕ,  ∀ i : Fin k, (ps i).Prime ∧ ps i ∣ (n + i)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Grimm.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Grimm.lean#L38).

## `Grimm.grimm_conjecture_weak`

Open: stated without proof.

> **Grimm's Conjecture, weaker version**
> If $n, n+1, \dots, n+k-1$ are all composite numbers, then their product
> has at least $k$ distinct prime divisors.

```lean
theorem grimm_conjecture_weak (n k : ℕ) (hn : 1 ≤ n) (hk : 1 ≤ k)
    (h : ∀ i : Fin k, (n + i).Composite) :
    ∃ ps : Fin k ↪ ℕ,  ∀ i : Fin k, (ps i).Prime ∧ ∃ j : Fin k, ps i ∣ (n + j)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Grimm.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Grimm.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Grimm.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Grimm.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Grimm%27s_conjecture)

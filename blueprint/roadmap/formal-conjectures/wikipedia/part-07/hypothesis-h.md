---
declaration: theorem
origin: cited
lean: Schinzel.schinzel_conjecture
statement: formalized
---

# Hypothesis H

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Schinzel%27s_hypothesis_H)

*Quoted from [FormalConjectures/Wikipedia/Schinzel.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Schinzel.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Schinzel.schinzel_conjecture`

Open: stated without proof.

> **Schinzel conjecture (H hypothesis)**
> If a finite set of polynomials $f_i$ satisfies both Schinzel and Bunyakovsky conditions,
> there exist infinitely many natural numbers $n$ such that $f_i(n)$ are primes for all $i$.

```lean
theorem schinzel_conjecture (fs : Finset ℤ[X]) (hfs : ∀ f ∈ fs, BunyakovskyCondition f)
    (hfs' : SchinzelCondition fs) : Infinite {n : ℕ | ∀ f ∈ fs, (f.eval (n : ℤ)).natAbs.Prime}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/Schinzel.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Schinzel.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Schinzel.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/Schinzel.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Schinzel%27s_hypothesis_H)

---
declaration: theorem
origin: cited
lean: Erdos479.erdos_479
statement: formalized
---

# Erdős Problem 479

> *Reference:* [erdosproblems.com/479](https://www.erdosproblems.com/479)

*Quoted from [FormalConjectures/ErdosProblems/479.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/479.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/479](https://www.erdosproblems.com/479).

The file states 1 research or textbook statement: 1 open.

## `Erdos479.erdos_479`

Open: stated without proof.

> Is it true that, for every integer $k\neq 1$, there are infinitely many $n$ such that
> $2^n\equiv k\pmod{n}$?

```lean
theorem erdos_479 : ∀ᵉ (k : ℤ) (k ≠ 1),
    { n : ℕ | (2 : ℤ) ^ n ≡ k [ZMOD (n : ℤ)] }.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/479.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/479.lean#L35).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/479.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/479.lean)
- [erdosproblems.com/479](https://www.erdosproblems.com/479)

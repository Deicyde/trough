---
declaration: theorem
origin: cited
lean: Erdos472.erdos_472
statement: formalized
---

# Erdős Problem 472

> *Reference:* [erdosproblems.com/472](https://www.erdosproblems.com/472)

*Quoted from [FormalConjectures/ErdosProblems/472.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/472.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/472](https://www.erdosproblems.com/472).

The file states 1 research or textbook statement: 1 open.

## `Erdos472.erdos_472`

Open: stated without proof.

> Given a finite sequence of primes $q_1\lt \cdots\lt q_m$, extend it by taking $q_{n+1}$ to be the
> smallest prime of the form $q_n+q_i-1$ for $n\geq m$. Is there an initial sequence for which
> this process continues forever?

```lean
theorem erdos_472 : ∃ m : ℕ, ∃ q : ℕ → ℕ, UlamPrimeExtension m q
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/472.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/472.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/472.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/472.lean)
- [erdosproblems.com/472](https://www.erdosproblems.com/472)

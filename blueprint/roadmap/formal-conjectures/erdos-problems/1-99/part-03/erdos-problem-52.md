---
declaration: theorem
origin: cited
lean: Erdos52.erdos_52
statement: formalized
---

# Erdős Problem 52

> *Reference:* [erdosproblems.com/52](https://www.erdosproblems.com/52)

*Quoted from [FormalConjectures/ErdosProblems/52.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/52.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/52](https://www.erdosproblems.com/52).

The file states 1 research or textbook statement: 1 open.

## `Erdos52.erdos_52`

Open: stated without proof.

> Let $A$ be a finite set of integers. Is it true that for every $\epsilon>0$
> $\max( \lvert A+A\rvert,\lvert AA\rvert)\gg_\epsilon \lvert A\rvert^{2-\epsilon}?$

```lean
theorem erdos_52 : ∀ (ε : ℝ), 0 < ε → ε < 1 → ∃ (C : ℝ), 0 < C ∧ ∀ (A : Finset ℤ),
    (max (A + A).card (A * A).card : ℝ) ≥ C * (A.card : ℝ) ^ (2 - ε)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/52.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/52.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/52.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/52.lean)
- [erdosproblems.com/52](https://www.erdosproblems.com/52)

---
declaration: theorem
origin: cited
lean: Erdos348.erdos_348
statement: formalized
---

# Erdős Problem 348

> *References:*
> - [erdosproblems.com/348](https://www.erdosproblems.com/348)
> - [Ge26] Geneson, J., *Deletion thresholds and exponential examples for complete sequences*.
>   [arXiv:2609.25107](https://arxiv.org/abs/2609.25107) (2026).

*Quoted from [FormalConjectures/ErdosProblems/348.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/348.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/348](https://www.erdosproblems.com/348).

The file states 1 research or textbook statement: 1 solved.

## `Erdos348.erdos_348`

Solved: stated here without proof.

> For what values of $0 \leq m < n$ is there a complete sequence
> $A = \{a_1 \leq a_2 \leq \cdots\}$ of integers such that
>  1. $A$ remains complete after removing any $m$ elements, but
>  2. $A$ is not complete after removing any $n$ elements.
>
> Geneson [Ge26, Theorem 1] proved that the pairs are exactly those with $m \leq 1$.
> Completeness allows finitely many exceptions, and deletions remove indexed occurrences.

```lean
theorem erdos_348 :
    { (m, n) | (m) (n) (_ : m < n) (a : ℕ → ℕ) (_ : Monotone a)
      (_ : ∀ s, s.card = m → IsAddCompleteNatSeq' (Function.updateFinset a s 0))
        (_ : ∀ t, t.card = n → ¬IsAddCompleteNatSeq' (Function.updateFinset a t 0)) } =
    erdos_348.answer
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/348.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/348.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/348.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/348.lean)
- [erdosproblems.com/348](https://www.erdosproblems.com/348)

---
declaration: theorem
origin: cited
lean: Erdos488.erdos_488
statement: formalized
---

# Erdős Problem 488

> *Reference:* [erdosproblems.com/488](https://www.erdosproblems.com/488)

*Quoted from [FormalConjectures/ErdosProblems/488.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/488.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/488](https://www.erdosproblems.com/488).

The file states 1 research or textbook statement: 1 open.

## `Erdos488.erdos_488`

Open: stated without proof.

> Let $A$ be a finite set and
> $$B=\{ n \geq 1 : a\mid n\textrm{ for some }a\in A\}.$$
> Is it true that, for every $m>n\geq \max(A)$,
> $$\frac{\lvert B\cap [1,m]\rvert }{m}< 2\frac{\lvert B\cap [1,n]\rvert}{n}?$$

```lean
theorem erdos_488 : ∀ (A : Finset ℕ), A.Nonempty →
    -- These are needed for the reasons outlined here: https://github.com/google-deepmind/formal-conjectures/pull/256
    0 ∉ A → 1 ∉ A →
    letI B := {n ≥ 1 | ∃ a ∈ A, a ∣ n}
    ∀ᵉ (n : ℕ) (m > n), A.max ≤ n →
      ((Finset.Icc 1 m).filter (· ∈ B)).card / (m : ℚ) <
        2 * ((Finset.Icc 1 n).filter (· ∈ B)).card / n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/488.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/488.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/488.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/488.lean)
- [erdosproblems.com/488](https://www.erdosproblems.com/488)

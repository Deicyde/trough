---
declaration: theorem
origin: cited
lean: Erdos881.erdos_881
statement: formalized
---

# Erdős Problem 881

> *Reference:* [erdosproblems.com/881](https://www.erdosproblems.com/881)

*Quoted from [FormalConjectures/ErdosProblems/881.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/881.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/881](https://www.erdosproblems.com/881).

The file states 1 research or textbook statement: 1 open.

## `Erdos881.erdos_881`

Open: stated without proof.

> Let `A ⊂ ℕ` be an additive basis of order `k` which is minimal in the sense that
> if `B ⊂ A` is any infinite set, then `A \ B` is not a basis of order `k`.
>
> Must there exist an infinite `B ⊂ A` such that `A \ B`
> is an additive basis of order `k + 1`?

```lean
theorem erdos_881 :
    ∀ (k : ℕ) (A : Set ℕ),
      IsMinimalAsymptoticAddBasisOfOrder k A →
        ∃ (B : Set ℕ), B ⊆ A ∧ B.Infinite ∧
          (A \ B).IsAsymptoticAddBasisOfOrder (k + 1)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/881.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/881.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/881.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/881.lean)
- [erdosproblems.com/881](https://www.erdosproblems.com/881)

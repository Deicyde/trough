---
declaration: theorem
origin: cited
lean: Erdos13.erdos_13, Erdos13.erdos_13.variants.general
statement: formalized
---

# Erdős Problem 13

> *Reference:* [erdosproblems.com/13](https://www.erdosproblems.com/13)

*Quoted from [FormalConjectures/ErdosProblems/13.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/13.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/13](https://www.erdosproblems.com/13).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos13.erdos_13`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos13.lean#L8261](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos13.lean#L8261).

> If $A \subseteq \{1, ..., N\}$ is a set with no $a, b, c \in A$ such that $a | (b+c)$ and
> $a < \min(b,c)$, then $|A| \le N/3 + O(1)$. This has been solved by Bedert [Be23].
>
> [Be23] Bedert, B., _On a problem of Erdős and Sárközy about sequences with no term dividing
> the sum of two larger terms_. arXiv:2301.07065 (2023).

```lean
theorem erdos_13 : ∃ C : ℝ, ∀ N : ℕ, ∀ A ⊆ Icc 1 N, IsForbiddenTripleFree A →
    (A.card : ℝ) ≤ (N : ℝ) / 3 + C
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/13.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/13.lean#L49).

## `Erdos13.erdos_13.variants.general`

Open: stated without proof.

> A general version asks, for a fixed $r \in \mathbb{N}$, if a set
> $A \subseteq \{1, ..., N\}$ has no $a \in A$ and $b_1, ..., b_r \in A$ such that
> $a | (b_1 + ... + b_r)$ and $a < \min(b_1, ..., b_r)$, then is it true that
> $|A| \le N/(r+1) + O(1)$?

```lean
theorem erdos_13.variants.general : ∀ r : ℕ, ∃ C : ℝ, ∀ N : ℕ,
    ∀ A ⊆ Icc 1 N,
    (∀ a ∈ A, ∀ (b : Fin r → ℕ), (∀ i, b i ∈ A) → (∀ i, a < b i) →
      ¬ (a ∣ ∑ i, b i)) →
    (A.card : ℝ) ≤ (N : ℝ) / (r + 1) + C
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/13.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/13.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/13.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/13.lean)
- [erdosproblems.com/13](https://www.erdosproblems.com/13)

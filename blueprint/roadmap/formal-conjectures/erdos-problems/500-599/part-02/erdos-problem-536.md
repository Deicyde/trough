---
declaration: theorem
origin: cited
lean: Erdos536.erdos_536
statement: formalized
---

# Erdős Problem 536

> *Reference:* [erdosproblems.com/536](https://www.erdosproblems.com/536)

*Quoted from [FormalConjectures/ErdosProblems/536.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/536.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/536](https://www.erdosproblems.com/536).

The file states 1 research or textbook statement: 1 open.

## `Erdos536.erdos_536`

Open: stated without proof.

> Let $\epsilon>0$ and $N$ be sufficiently large. Is it true that if $A\subseteq \{1,\ldots,N\}$ has
> size at least $\epsilon N$ then there must be distinct $a,b,c\in A$ such that
>
> $$[a, b]=[b, c]=[a, c],$$
>
> where $[\cdot, \cdot]$ denotes the least common multiple?

```lean
theorem erdos_536 :
    ∀ᵉ (ε > (0: ℝ)), ∀ᶠ N in atTop,
    ∀ (A : Finset ℕ), A ⊆ Icc 1 N → (ε * (N : ℝ)) ≤ (A.card : ℝ) →
    ∃ᵉ  (a ∈ A) (b ∈ A) (c ∈ A),
    # {a, b, c} = 3 ∧ a.lcm b = b.lcm c ∧ b.lcm c = a.lcm c
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/536.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/536.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/536.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/536.lean)
- [erdosproblems.com/536](https://www.erdosproblems.com/536)

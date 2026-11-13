---
declaration: theorem
origin: cited
lean: Erdos1110.erdos_1110
statement: formalized
---

# Erdős Problem 1110

> *Reference:* [Erdős Problem 1110](https://www.erdosproblems.com/1110)

*Quoted from [FormalConjectures/ErdosProblems/1110.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1110.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1110](https://www.erdosproblems.com/1110).

The file states 1 research or textbook statement: 1 open.

## `Erdos1110.erdos_1110`

Open: stated without proof.

> Let $p>q\geq 2$ be two coprime integers. We call $n$ representable if it is the sum of
> integers of the form $p^kq^l$, none of which divide each other.
>
> If $\{p,q\}\neq \{2,3\}$ then what can be said about the density of non-representable
> numbers? Are there infinitely many coprime non-representable numbers, that is, an infinite
> family of pairwise coprime non-representable integers?

```lean
theorem erdos_1110 :
    ∀ (p q : ℕ), q < p → 2 ≤ q →
      Nat.Coprime p q → ¬(p = 3 ∧ q = 2) →
      ∃ A : Set ℕ, A.Infinite ∧ A.Pairwise Nat.Coprime ∧
        ∀ n ∈ A, ¬Representable p q n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1110.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1110.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1110.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1110.lean)
- [erdosproblems.com/1110](https://www.erdosproblems.com/1110)

---
declaration: theorem
origin: cited
lean: Erdos39.erdos_39
statement: formalized
---

# Erdős Problem 39

> *Reference:* [erdosproblems.com/39](https://www.erdosproblems.com/39)

*Quoted from [FormalConjectures/ErdosProblems/39.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/39.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/39](https://www.erdosproblems.com/39).

The file states 1 research or textbook statement: 1 open.

## `Erdos39.erdos_39`

Open: stated without proof.

> Is there an infinite Sidon set $A\subset \mathbb{N}$ such that
> $\lvert A\cap \{1\ldots,N\}\rvert \gg_\epsilon N^{1/2-\epsilon}$
> for all $\varepsilon > 0$?

```lean
theorem erdos_39 : ∃ (A : Set ℕ), A.Infinite ∧ IsSidon A ∧
    ∀ᵉ  (ε  > (0 : ℝ)),
    (· ^ (1 / 2 - ε) : ℕ → ℝ) =O[atTop] fun N => (((Set.Icc 1 N) ∩ A).ncard : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/39.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/39.lean#L38).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/39.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/39.lean)
- [erdosproblems.com/39](https://www.erdosproblems.com/39)

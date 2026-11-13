---
declaration: theorem
origin: cited
lean: Erdos462.erdos_462
statement: formalized
---

# Erdős Problem 462

> *Reference:* [erdosproblems.com/462](https://www.erdosproblems.com/462)

*Quoted from [FormalConjectures/ErdosProblems/462.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/462.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/462](https://www.erdosproblems.com/462).

The file states 1 research or textbook statement: 1 open.

## `Erdos462.erdos_462`

Open: stated without proof.

> Let $p(n)$ denote the least prime factor of $n$. Is there a constant $C>0$ such that
>
> $$\sum_{x\leq n\leq x+C\sqrt{x}(\log x)^2}\frac{p(n)}{n}\gg 1$$
>
> for all sufficiently large $x$?

```lean
theorem erdos_462 :
    ∃ C c : ℝ, 0 < C ∧ 0 < c ∧ ∀ᶠ x : ℕ in atTop,
      c ≤ ∑ n ∈ Finset.Icc x
        ⌊(x : ℝ) + C * Real.sqrt x * (Real.log x) ^ 2⌋₊, (n.minFac : ℝ) / n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/462.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/462.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/462.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/462.lean)
- [erdosproblems.com/462](https://www.erdosproblems.com/462)

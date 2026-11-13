---
declaration: theorem
origin: cited
lean: Erdos705.erdos_705
statement: formalized
---

# Erdős Problem 705

> *References:*
> - [erdosproblems.com/705](https://www.erdosproblems.com/705)
> - [OD99] P. O'Donnell, High girth unit-distance graphs. PhD Dissertation, Rutgers University (1999).

*Quoted from [FormalConjectures/ErdosProblems/705.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/705.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/705](https://www.erdosproblems.com/705).

The file states 1 research or textbook statement: 1 solved.

## `Erdos705.erdos_705`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos705.lean#L8323](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos705.lean#L8323).

> Let $G$ be a finite unit distance graph in $\mamthbb{R}^2$.
> Is there some $k$ such that if $G$ has girth $≥ k$, then $\chi(G) ≤ 3$?
>
> The general case was solved by O'Donnell [OD99], who constructed finite unit distance graphs with
> chromatic number $4$ and arbitrarily large girth.

```lean
theorem erdos_705:
  ¬ ∃ k, ∀ V : Set ℝ², V.Finite →
    (UnitDistancePlaneGraph V).girth ≥ k → (UnitDistancePlaneGraph V).chromaticNumber ≤ 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/705.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/705.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/705.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/705.lean)
- [erdosproblems.com/705](https://www.erdosproblems.com/705)

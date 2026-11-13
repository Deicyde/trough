---
declaration: theorem
origin: cited
lean: Erdos414.erdos_414
statement: formalized
---

# Erdős Problem 414

> *Reference:* [erdosproblems.com/414](https://www.erdosproblems.com/414)

*Quoted from [FormalConjectures/ErdosProblems/414.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/414.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/414](https://www.erdosproblems.com/414).

The file states 1 research or textbook statement: 1 open.

## `Erdos414.erdos_414`

Open: stated without proof.

> Let $h_1(n) = h(n)$ and $h_k(n) = h(h_{k-1}(n))$. Is it true, for any $m,n$, there exist
> $i$ and $j$ such that $h_i(m) = h_j(n)$?

```lean
theorem erdos_414 : ∀ᵉ  (m > 0) (n > 0), ∃ i j, h^[i] m = h^[j] n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/414.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/414.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/414.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/414.lean)
- [erdosproblems.com/414](https://www.erdosproblems.com/414)

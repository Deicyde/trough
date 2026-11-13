---
declaration: theorem
origin: cited
lean: Erdos555.erdos_555
statement: formalized
---

# Erdős Problem 555

> *Reference:* [erdosproblems.com/555](https://www.erdosproblems.com/555)

*Quoted from [FormalConjectures/ErdosProblems/555.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/555.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/555](https://www.erdosproblems.com/555).

The file states 1 research or textbook statement: 1 open.

## `Erdos555.erdos_555`

Open: stated without proof.

> Let $R_k(G)$ be the least $m$ such that every $k$-colouring of the edges of $K_m$ contains a
> monochromatic copy of $G$. Determine $R_k(C_{2n})$.

```lean
theorem erdos_555 : EvenCycleRamseyFunction erdos_555.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/555.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/555.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/555.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/555.lean)
- [erdosproblems.com/555](https://www.erdosproblems.com/555)

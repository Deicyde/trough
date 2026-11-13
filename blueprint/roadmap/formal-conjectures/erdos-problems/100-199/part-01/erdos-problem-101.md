---
declaration: theorem
origin: cited
lean: Erdos101.erdos_101
statement: formalized
---

# Erdős Problem 101

> *Reference:* [erdosproblems.com/101](https://www.erdosproblems.com/101)

*Quoted from [FormalConjectures/ErdosProblems/101.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/101.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/101](https://www.erdosproblems.com/101).

The file states 1 research or textbook statement: 1 open.

## `Erdos101.erdos_101`

Open: stated without proof.

> Given $n$ points in $\mathbb{R}^2$, no five of which are on a line, the number of
> lines containing four points is $o(n^2)$.

```lean
theorem erdos_101 : (fun n => (numLinesWithFourPointMax n : ℝ)) =o[atTop] (fun n => (n : ℝ)^2)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/101.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/101.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/101.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/101.lean)
- [erdosproblems.com/101](https://www.erdosproblems.com/101)

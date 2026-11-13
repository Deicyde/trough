---
declaration: theorem
origin: cited
lean: Erdos96.erdos_96
statement: formalized
---

# Erdős Problem 96

> *Reference:* [erdosproblems.com/96](https://www.erdosproblems.com/96)

*Quoted from [FormalConjectures/ErdosProblems/96.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/96.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/96](https://www.erdosproblems.com/96).

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `Erdos96.erdos_96`

Open: stated without proof.

> If $n$ points in $\mathbb{R}^2$ form a convex polygon then there are $O(n)$ many pairs which are
> distance $1$ apart.

```lean
theorem erdos_96 :
    (fun n => (maxConvexUnitDistances n : ℝ)) =O[atTop] fun n => (n : ℝ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/96.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/96.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/96.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/96.lean)
- [erdosproblems.com/96](https://www.erdosproblems.com/96)

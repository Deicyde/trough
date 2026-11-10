---
declaration: theorem
origin: cited
lean: Erdos101.erdos_101
statement: formalized
---

# Erdős Problem 101

> *Reference:* [erdosproblems.com/101](https://www.erdosproblems.com/101)

*Quoted from [FormalConjectures/ErdosProblems/101.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/101.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/101](https://www.erdosproblems.com/101).

The file states 1 research or textbook statement: 1 open.

## `Erdos101.erdos_101`

Open: stated without proof.

> Given $n$ points in $\mathbb{R}^2$, no five of which are on a line, the number of
> lines containing four points is $o(n^2)$.

```lean
theorem erdos_101 : (fun n => (numLinesWithFourPointMax n : ℝ)) =o[atTop] (fun n => (n : ℝ)^2)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/101.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/101.lean#L47).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/101.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/101.lean)
- [erdosproblems.com/101](https://www.erdosproblems.com/101)

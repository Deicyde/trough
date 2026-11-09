---
declaration: theorem
origin: cited
lean: Erdos735.erdos_735
statement: formalized
---

# Erdős Problem 735

> *References:*
> - [erdosproblems.com/735](https://www.erdosproblems.com/735)
> - [Er81] Erdős, P., *On the combinatorial problems which I would most like to see solved*.
>   Combinatorica 1 (1981), 25-42. [PDF](https://www.renyi.hu/~p_erdos/1981-16.pdf)
> - [ABKPR08] Ackerman, E., Buchin, K., Knauer, C., Pinchasi, R. and Rote, G., *There are not too
>   many magic configurations*. Discrete Comput. Geom. 39 (2008), 3-16.
>   [DOI](https://doi.org/10.1007/s00454-007-9023-0)

*Quoted from [FormalConjectures/ErdosProblems/735.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/735.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/735](https://www.erdosproblems.com/735).

The file states 1 research or textbook statement: 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos735.erdos_735`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos735/Final.lean#L54](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos735/Final.lean#L54).

> Given any $n$ points in $\mathbb{R}^2$ when can one give positive weights to the points such that
> the sum of the weights of the points along every line containing at least two points is the same?
>
> This is a problem of Murty [Er81], who conjectured that this is only possible in one of
> four cases: all points on a line, no three points on a line, $n-1$ points on a line, and a
> triangle, the angle bisectors, and the incentre (or a projective equivalent). Ackerman, Buchin,
> Knauer, Pinchasi and Rote [ABKPR08] proved this conjecture. Conversely, every set in these four
> cases is magic.

```lean
theorem erdos_735 : {S : Finset ℝ² | IsMagic S} = erdos_735.answer
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/735.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/735.lean#L93).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/735.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/735.lean)
- [erdosproblems.com/735](https://www.erdosproblems.com/735)

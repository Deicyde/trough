---
declaration: theorem
origin: cited
lean: Erdos130.erdos_130
statement: formalized
---

# Erdős Problem 130

> *Reference:* [erdosproblems.com/130](https://www.erdosproblems.com/130)

*Quoted from [FormalConjectures/ErdosProblems/130.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/130.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/130](https://www.erdosproblems.com/130).

The file states 1 research or textbook statement: 1 solved.

## `Erdos130.erdos_130`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-130/Research/Basic.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-130/Research/Basic.lean).

> Let $A\subset\mathbb{R}^2$ be an infinite set which contains no three points on a
> line and no four points on a circle. Consider the graph with vertices the points
> in $A$, where two vertices are joined by an edge if and only if they are an
> integer distance apart. How large can the chromatic number and clique number of
> this graph be? In particular, can the chromatic number be infinite?
>
> The chromatic number can be infinite: there is an infinite general-position set
> whose integer-distance graph admits no finite proper colouring. How large the
> *clique* number can be is not addressed here.

```lean
theorem erdos_130 :
    ∃ A : Set ℝ², A.Infinite ∧ InGeneralPosition A ∧
      (IntegerDistancePlaneGraph A).chromaticNumber = ⊤
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/130.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/130.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/130.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/130.lean)
- [erdosproblems.com/130](https://www.erdosproblems.com/130)

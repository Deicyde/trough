---
declaration: theorem
origin: cited
lean: Erdos103.erdos_103, Erdos103.erdos_103.variants.two_le
statement: formalized
---

# Erdős Problem 103

> *References:*
> - [erdosproblems.com/103](https://www.erdosproblems.com/103)

*Quoted from [FormalConjectures/ErdosProblems/103.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/103.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/103](https://www.erdosproblems.com/103).

The file states 2 research or textbook statements: 2 open.

## `Erdos103.erdos_103`

Open: stated without proof.

> Let $h(n)$ count the number of incongruent sets of $n$ points in $\mathbb{R}^2$ which minimise
> the diameter subject to the constraint that $d(x,y)\geq 1$ for all points $x\neq y$. Is it true
> that $h(n)\to \infty$?

```lean
theorem erdos_103 : Tendsto h atTop (nhds ⊤)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/103.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/103.lean#L61).

## `Erdos103.erdos_103.variants.two_le`

Open: stated without proof.

> It is not even known whether $h(n)\geq 2$ for all large $n$.

```lean
theorem erdos_103.variants.two_le : ∀ᶠ n in atTop, 2 ≤ h n
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/103.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/103.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/103.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/103.lean)
- [erdosproblems.com/103](https://www.erdosproblems.com/103)

---
declaration: theorem
origin: cited
lean: Erdos95.erdos_95, Erdos95.erdos_95.variants.guth_katz
statement: formalized
---

# Erdős Problem 95

> *References:*
> - [erdosproblems.com/95](https://www.erdosproblems.com/95)
> - [Er92e] Erdős, Pál, *Some Unsolved problems in Geometry, Number Theory and Combinatorics*.
>   Eureka (1992), 44-48.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
>   geometry*. Resenhas (1995), 165-186.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul
>   Erdős, I (1997), 47-67.
> - [Er97f] Erdős, Paul, *Some unsolved problems*. Combinatorics, geometry and probability
>   (Cambridge, 1993) (1997), 1-10.
> - [Al63] Altman, E., *On a problem of P. Erdős*. Amer. Math. Monthly (1963), 148-157.
> - [GuKa15] Guth, Larry and Katz, Nets Hawk, *On the Erdős distinct distances problem in the
>   plane*. Ann. of Math. (2) (2015), 155-190.

*Quoted from [FormalConjectures/ErdosProblems/95.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/95.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/95](https://www.erdosproblems.com/95).

The file states 2 research or textbook statements: 2 solved.

## `Erdos95.erdos_95`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos95.lean#L1005](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos95.lean#L1005).

> Let $x_1,\ldots,x_n\in\mathbb{R}^2$ determine the set of distances $\{u_1,\ldots,u_t\}$. Suppose
> $u_i$ appears as the distance between $f(u_i)$ many pairs of points. Then for all $\epsilon>0$
>
> $$\sum_i f(u_i)^2 \ll_\epsilon n^{3+\epsilon}.$$
>
> The case when the points determine a convex polygon was solved by Altman [Al63]. Note it is
> trivial that $\sum f(u_i)=\binom{n}{2}$.
>
> Solved by Guth and Katz [GuKa15] who proved the upper bound
>
> $$\sum_i f(u_i)^2 \ll n^3\log n.$$
>
> See also [94](https://www.erdosproblems.com/94).

```lean
theorem erdos_95 : ∀ ε : ℝ, 0 < ε → ∃ C : ℝ, 0 < C ∧ ∀ P : Finset ℝ²,
    ∑ u ∈ distanceSet P, (distanceMultiplicity P u : ℝ) ^ 2 ≤
      C * (P.card : ℝ) ^ (3 + ε)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/95.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/95.lean#L60).

## `Erdos95.erdos_95.variants.guth_katz`

Solved: stated here without proof.

> Guth and Katz [GuKa15] proved the upper bound $\sum_i f(u_i)^2 \ll n^3\log n$.

```lean
theorem erdos_95.variants.guth_katz : ∃ C : ℝ, 0 < C ∧ ∀ P : Finset ℝ², 2 ≤ P.card →
    ∑ u ∈ distanceSet P, (distanceMultiplicity P u : ℝ) ^ 2 ≤
      C * (P.card : ℝ) ^ 3 * Real.log P.card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/95.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/95.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/95.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/95.lean)
- [erdosproblems.com/95](https://www.erdosproblems.com/95)

---
declaration: theorem
origin: cited
lean: Erdos94.erdos_94, Erdos94.erdos_94.variants.no_three_on_a_line, Erdos94.erdos_94.variants.regular_ngon
statement: formalized
---

# Erdős Problem 94

> *References:*
> - [erdosproblems.com/94](https://www.erdosproblems.com/94)
> - [Er92e] Erdős, Pál, *Some Unsolved problems in Geometry, Number Theory and Combinatorics*. Eureka
>   (1992), 44-48.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul Erdős, I
>   (1997), 47-67.
> - [LeTh95] Lefmann, Hanno and Thiele, Torsten, *Point sets with distinct distances*. Combinatorica
>   (1995), 379-408.

*Quoted from [FormalConjectures/ErdosProblems/94.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/94.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/94](https://www.erdosproblems.com/94).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos94.erdos_94`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos94.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos94.lean).

> Suppose $n$ points in $\mathbb{R}^2$ determine a convex polygon and the set of distances between
> them is $\{u_1,\ldots,u_t\}$. Suppose $u_i$ appears as the distance between $f(u_i)$ many pairs of
> points. Then
> $$\sum_i f(u_i)^2 \ll n^3.$$
>
> In [Er97c] Erdős claims that Fishburn solved this, but gives no reference.

```lean
theorem erdos_94 : ∃ C > (0 : ℝ), ∀ P : Finset ℝ², ConvexIndep (P : Set ℝ²) →
    ∑ u ∈ distanceSet P, (distanceMultiplicity P u : ℝ) ^ 2 ≤ C * (P.card : ℝ) ^ 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/94.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/94.lean#L54).

## `Erdos94.erdos_94.variants.no_three_on_a_line`

Solved: stated here without proof.

> Lefmann and Theile [LeTh95] prove a stronger version of this question, that
> $$\sum_i f(u_i)^2 \ll n^3$$
> under the weaker assumption that no three points are on a line.

```lean
theorem erdos_94.variants.no_three_on_a_line : ∃ C > (0 : ℝ), ∀ P : Finset ℝ²,
    NonTrilinear (P : Set ℝ²) →
    ∑ u ∈ distanceSet P, (distanceMultiplicity P u : ℝ) ^ 2 ≤ C * (P.card : ℝ) ^ 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/94.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/94.lean#L72).

## `Erdos94.erdos_94.variants.regular_ngon`

Open: stated without proof.

> Erdős and Fishburn also make the stronger conjecture that $\sum f(u_i)^2$ is maximal for the
> regular $n$-gon (for large enough $n$).

```lean
theorem erdos_94.variants.regular_ngon : ∀ᶠ n : ℕ in atTop, ∀ P : Finset ℝ²,
    P.card = n → ConvexIndep (P : Set ℝ²) →
    ∑ u ∈ distanceSet P, (distanceMultiplicity P u : ℝ) ^ 2 ≤
      ∑ u ∈ distanceSet (regularNGon n), (distanceMultiplicity (regularNGon n) u : ℝ) ^ 2
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/94.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/94.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/94.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/94.lean)
- [erdosproblems.com/94](https://www.erdosproblems.com/94)

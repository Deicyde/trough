---
declaration: theorem
origin: cited
lean: Erdos660.erdos_660, Erdos660.erdos_660.variants.altman_planar, Erdos660.erdos_660.variants.Er75f
statement: formalized
---

# Erdős Problem 660

> *References:*
> - [erdosproblems.com/660](https://www.erdosproblems.com/660)
> - [Er97e] Erdős, Paul, *Some of my favorite problems and results*, The mathematics of Paul Erdős,
>   I (1997), 47–67.
> - [Al63] Altman, E., *On a problem of P. Erdős*, Amer. Math. Monthly (1963), 148–157.
> - [Er75f] Erdős, Paul, *On some problems of elementary and combinatorial geometry*, Ann. Mat. Pura
>   Appl. (4) (1975), 99–108.

*Quoted from [FormalConjectures/ErdosProblems/660.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/660.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/660](https://www.erdosproblems.com/660).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos660.erdos_660`

Open: stated without proof.

> Let $x_1, \ldots, x_n \in \mathbb{R}^3$ be the vertices of a convex polyhedron. Are there at least
>
> $$(1 - o(1)) \frac{n}{2}$$
>
> many distinct distances between the $x_i$?
>
> The $(1 - o(1)) \frac{n}{2}$ lower bound is formalised as: for every $\varepsilon > 0$, every set
> of $n$ vertices of a convex polyhedron with $n$ sufficiently large determines at least
> $(1 - \varepsilon) \frac{n}{2}$ distinct distances.

```lean
theorem erdos_660 :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ n in Filter.atTop, ∀ P : Finset ℝ³,
      P.card = n → IsPolyhedronVertices P →
      (1 - ε) * ((n : ℝ) / 2) ≤ (distinctDistances P : ℝ)
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/660.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/660.lean#L56).

## `Erdos660.erdos_660.variants.altman_planar`

Solved: stated here without proof.

> For the similar problem in $\mathbb{R}^2$ there are always at least $n/2$ distances, as proved by
> Altman [Al63].

```lean
theorem erdos_660.variants.altman_planar (n : ℕ) (P : Finset ℝ²)
    (hcard : P.card = n) (hconv : ConvexIndependent ℝ ((↑) : ↥(P : Set ℝ²) → ℝ²))
    (haff : affineSpan ℝ (P : Set ℝ²) = ⊤) :
    n / 2 ≤ distinctDistances P
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/660.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/660.lean#L67).

## `Erdos660.erdos_660.variants.Er75f`

Open: stated without proof.

> In [Er75f] Erdős claims that Altman proved that the vertices determine $\gg n$ many distinct
> distances, but gives no reference.

```lean
theorem erdos_660.variants.Er75f :
    ∃ c > (0 : ℝ), ∀ᶠ n in Filter.atTop, ∀ P : Finset ℝ³,
      P.card = n → IsPolyhedronVertices P →
      c * n ≤ (distinctDistances P : ℝ)
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/660.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/660.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/660.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/660.lean)
- [erdosproblems.com/660](https://www.erdosproblems.com/660)

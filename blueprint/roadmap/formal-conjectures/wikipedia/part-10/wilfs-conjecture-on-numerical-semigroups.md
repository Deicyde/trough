---
declaration: theorem
origin: cited
lean: WilfNumericalSemigroupConjecture.wilf_numerical_semigroup_conjecture, WilfNumericalSemigroupConjecture.wilf_conjecture_embedding_dim_le_three
statement: formalized
---

# Wilf's Conjecture on Numerical Semigroups

> An additive submonoid $S \le \mathbb{N}$ with finite complement $G(S) = \mathbb{N} \setminus S$
> forms a *numerical semigroup*. Write
> $c(S) = \min\{c \in \mathbb{N} : \forall m \ge c,\, m \in S\}$
> for its conductor, $n(S) = |S \cap [0, c(S))| = c(S) - |G(S)|$ for the count of sporadic elements
> below $c(S)$, and $e(S) = |S_{>0} \setminus (S_{>0} + S_{>0})|$ for its embedding dimension (the
> size of its unique minimal generating set).
>
> Herbert S. Wilf [Wi78] conjectured that $c(S) \le e(S) \cdot n(S)$ holds for all numerical
> semigroups $S$ (equivalently $e(S) \ge (F(S) + 1) / (F(S) + 1 - |G(S)|)$ when $S \subsetneq
> \mathbb{N}$ has largest gap $F(S) = c(S) - 1$, as stated on Wikipedia's Coin problem page).
> Fröberg, Gottlieb, and Häggkvist [FGH87, Theorem 20] proved the inequality whenever $e(S) \le 3$
> (sourced directly from [FGH87]); the general case remains open.
>
> *References:*
> - [Wi78] H. S. Wilf, *A circle-of-lights algorithm for the "money-changing problem"*, Amer. Math.
>   Monthly **85** (1978), no. 7, 562–565, DOI: `10.1080/00029890.1978.11994639`.
> - [FGH87] R. Fröberg, C. Gottlieb, and R. Häggkvist, *On numerical semigroups*, Semigroup Forum
>   **35** (1987), no. 1, 63–83, DOI: `10.1007/BF02573091`.
> - [Wikipedia: Coin problem — Wilf's conjecture](https://en.wikipedia.org/wiki/Coin_problem#Wilf%27s_conjecture)

*Quoted from [FormalConjectures/Wikipedia/WilfNumericalSemigroupConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WilfNumericalSemigroupConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 2 test statements, counted here but not shown.

## `WilfNumericalSemigroupConjecture.wilf_numerical_semigroup_conjecture`

Open: stated without proof.

> **Wilf's Conjecture** [Wi78]: Every numerical semigroup $S \le \mathbb{N}$ obeys
> $c(S) \le e(S) \cdot n(S)$.

```lean
theorem wilf_numerical_semigroup_conjecture {S : AddSubmonoid ℕ} (hS : IsNumericalSemigroup S) :
    conductor S ≤ embeddingDim S * sporadicCount S
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/WilfNumericalSemigroupConjecture.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WilfNumericalSemigroupConjecture.lean#L97).

## `WilfNumericalSemigroupConjecture.wilf_conjecture_embedding_dim_le_three`

Solved: stated here without proof.

> **Fröberg–Gottlieb–Häggkvist Theorem** [FGH87, Theorem 20]: Every numerical semigroup
> $S \le \mathbb{N}$ with embedding dimension $e(S) \le 3$ satisfies $c(S) \le e(S) \cdot n(S)$.

```lean
theorem wilf_conjecture_embedding_dim_le_three {S : AddSubmonoid ℕ} (hS : IsNumericalSemigroup S)
    (he : embeddingDim S ≤ 3) :
    conductor S ≤ embeddingDim S * sporadicCount S
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/Wikipedia/WilfNumericalSemigroupConjecture.lean, line 104](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WilfNumericalSemigroupConjecture.lean#L104).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/WilfNumericalSemigroupConjecture.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/Wikipedia/WilfNumericalSemigroupConjecture.lean)
- [Wikipedia: Coin problem — Wilf's conjecture](https://en.wikipedia.org/wiki/Coin_problem#Wilf%27s_conjecture)

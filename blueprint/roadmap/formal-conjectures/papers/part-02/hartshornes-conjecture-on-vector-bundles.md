---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.harthshorne_conjecture
statement: formalized
---

# Hartshorne's conjecture on Vector Bundles

> *References:*
> * [Har1974] R. Hartshorne, [Varieties of small codimension in projective space](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-80/issue-6/Varieties-of-small-codimension-in-projective-space/bams/1183535999.full).
> * [MO2010] [Evidences on Hartshorne's conjecture? References?](https://mathoverflow.net/questions/13990/evidences-on-hartshornes-conjecture-references)

*Quoted from [FormalConjectures/Paper/HartshorneConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/HartshorneConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 API statement, counted here but not shown.

## `AlgebraicGeometry.Scheme.harthshorne_conjecture`

Open: stated without proof.

> There are no indecomposable vector bundles of rank 2 on $\mathbb{P}^n$ for $n \ge 7$.
> This is Conjecture 6.3 in [Har1974].

```lean
theorem harthshorne_conjecture (n : ℕ) (hn : 7 ≤ n)
    (𝓕 : VectorBundles ℙ(Fin (n + 1); Spec (.of ℂ)))
    (h𝓕 : 𝓕.rank = 2) :
    Nonempty (𝓕.Splitting (Fin 2))
```

Category `research open`; AMS [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Paper/HartshorneConjecture.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/HartshorneConjecture.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/HartshorneConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/HartshorneConjecture.lean)
- [Varieties of small codimension in projective space](https://projecteuclid.org/journals/bulletin-of-the-american-mathematical-society-new-series/volume-80/issue-6/Varieties-of-small-codimension-in-projective-space/bams/1183535999.full)

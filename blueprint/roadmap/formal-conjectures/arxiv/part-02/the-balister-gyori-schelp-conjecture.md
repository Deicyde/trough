---
declaration: theorem
origin: cited
lean: Arxiv.«2607.08630».balister_gyori_schelp_conjecture
statement: formalized
---

# The Balister–Győri–Schelp conjecture

> *References:*
> - [Perfect Matchings with Prescribed Differences Beyond Hall: The Two-Hole Problem](https://arxiv.org/abs/2607.08630)
>   by *Aryeh Lev Zabokritskiy (Yohananov)* (2026)
> - [Coloring vertices and edges of a graph by nonempty subsets of a set](https://doi.org/10.1016/j.ejc.2010.11.008)
>   by *P. N. Balister, E. Győri, and R. H. Schelp*, European Journal of Combinatorics 32(4),
>   533–537 (2011)

*Quoted from [FormalConjectures/Arxiv/2607.08630/BalisterGyoriSchelp.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.08630/BalisterGyoriSchelp.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `Arxiv.«2607.08630».balister_gyori_schelp_conjecture`

Open: stated without proof.

> The **Balister–Győri–Schelp conjecture** ([Conjecture 1](https://arxiv.org/pdf/2607.08630#page=6)):
> for $s \ge 2$, every zero-sum list of $2^{s-1}$ nonzero vectors in $\mathbb{F}_2^s$ is the
> prescribed-difference profile of a perfect matching of $\mathbb{F}_2^s$.
>
> The equivalence $e$ indexes the two endpoints of each pair and ensures that the pairs are disjoint
> and exhaust the ambient vector space.

```lean
theorem balister_gyori_schelp_conjecture (s : ℕ) (hs : 2 ≤ s)
    (v : Fin (2 ^ (s - 1)) → 𝔽₂ s)
    (hv_nonzero : ∀ i, v i ≠ 0)
    (hv_sum : ∑ i, v i = 0) :
    ∃ e : Fin (2 ^ (s - 1)) × Fin 2 ≃ 𝔽₂ s,
      ∀ i, e (i, 0) + e (i, 1) = v i
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Arxiv/2607.08630/BalisterGyoriSchelp.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.08630/BalisterGyoriSchelp.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/2607.08630/BalisterGyoriSchelp.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Arxiv/2607.08630/BalisterGyoriSchelp.lean)
- [Perfect Matchings with Prescribed Differences Beyond Hall: The Two-Hole Problem](https://arxiv.org/abs/2607.08630)

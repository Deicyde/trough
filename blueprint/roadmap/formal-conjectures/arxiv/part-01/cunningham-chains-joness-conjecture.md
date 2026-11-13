---
declaration: theorem
origin: cited
lean: CunninghamChain.infinitely_many_firstKind_chains, CunninghamChain.infinitely_many_secondKind_chains
statement: formalized
---

# Cunningham chains — Jones's conjecture

> A Cunningham chain is a sequence of primes satisfying either $p_{i+1}=2p_i+1$
> (first kind) or $p_{i+1}=2p_i-1$ (second kind). It is conjectured that there
> are infinitely many chains of every positive exact length, of both kinds.
>
> A chain has **exact length k** when its first $k$ terms are prime and the
> $(k+1)$-th generated term is composite.
>
> Lenny Jones conjectures that for every positive integer $k$, infinitely many
> primes start a chain of exact length $k$, for each of the two kinds.
>
> *References:*
> - Lenny Jones, [Polynomial Cunningham Chains](https://arxiv.org/abs/1104.1579)
> - [OEIS A181697](https://oeis.org/A181697), first-kind chain lengths
> - [OEIS A181715](https://oeis.org/A181715), second-kind chain lengths

*Quoted from [FormalConjectures/Arxiv/1104.1579/CunninghamChain.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1104.1579/CunninghamChain.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 2 test statements, counted here but not shown.

## `CunninghamChain.infinitely_many_firstKind_chains`

Open: stated without proof.

> Jones's conjecture (first kind): for every positive integer $k$, there are
> infinitely many primes $p$ that start a first-kind Cunningham chain of
> exactly length $k$.

```lean
theorem infinitely_many_firstKind_chains (k : ℕ) (hk : 0 < k) :
    Set.Infinite {p : ℕ | IsFirstKindChainOfLength p k}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/1104.1579/CunninghamChain.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1104.1579/CunninghamChain.lean#L83).

## `CunninghamChain.infinitely_many_secondKind_chains`

Open: stated without proof.

> Jones's conjecture (second kind): for every positive integer $k$, there are
> infinitely many primes $p$ that start a second-kind Cunningham chain of
> exactly length $k$.

```lean
theorem infinitely_many_secondKind_chains (k : ℕ) (hk : 0 < k) :
    Set.Infinite {p : ℕ | IsSecondKindChainOfLength p k}
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Arxiv/1104.1579/CunninghamChain.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1104.1579/CunninghamChain.lean#L93).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Arxiv/1104.1579/CunninghamChain.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Arxiv/1104.1579/CunninghamChain.lean)
- [Polynomial Cunningham Chains](https://arxiv.org/abs/1104.1579)

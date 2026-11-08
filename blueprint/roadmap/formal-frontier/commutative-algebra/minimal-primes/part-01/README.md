---
navigation: transparent
---

# Prime spectra of products of… to Krull dimension of dependent…

## Highlights

- [Prime spectra of products of semifields](prime-spectra-of-products-of-semifields.md)
- [Ideals in products of division semirings](ideals-in-products-of-division-semirings.md)
- [Nontrivial dependent reduced products](nontrivial-dependent-reduced-products.md)
- [Krull dimension and chain cardinalities of lexicographic sums](krull-dimension-and-chain-cardinalities-of-lexic.md)
- [Dimension and point ranks of finite dependent lexicographic products](dimension-and-point-ranks-of-finite-dependent-le.md)

## Headline results

- [Successors of finite product expansions](successors-of-finite-product-expansions.md)

**Ranks of dependent pointwise products.** For arbitrary `ι : Type u`, independently universed given preorders
`β : ι → Type v`, and a section `f : ∀ i, β i`,
[`Order.height_pi_eq_iSup_finset` and `Order.coheight_pi_eq_iSup_finset`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)
state

```lean
Order.height f = ⨆ s : Finset ι, ∑ i ∈ s, Order.height (f i)
Order.coheight f = ⨆ s : Finset ι, ∑ i ∈ s, Order.coheight (f i)
```

The supremum includes every finite coordinate set, including the empty set.
No finite-support condition on `f` or finiteness assumption on the index is needed.
Infinitely many positive finite coordinate ranks, or one infinite coordinate rank,
can give infinite rank. The proof detects each finite strict series on finitely
many coordinates and reuses the finite product formula on that restriction;
the reverse bound fills the remaining coordinates with the supplied `f`.

For a finite index `ι : Type u`, independently universed given preorders
`β : ι → Type v`, and a section `f : ∀ i, β i`,
[`Order.height_pi` and `Order.coheight_pi`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)
state

```lean
Order.height f = ∑ i, Order.height (f i)
Order.coheight f = ∑ i, Order.coheight (f i)
```

These are equalities in `ℕ∞` for the original pointwise product preorder and the
original fibre preorders, including infinite ranks and unbounded finite chain
lengths with no attaining chain. No antisymmetry, fibre inhabitation, finite-height
or attainment hypothesis is required. An empty index gives both ranks zero;
the top of the pointwise `Fin 2 → Fin 2` square has height two, not lexicographic
rank three. The proofs compose the binary rank identities with Mathlib's
order-isomorphism rank invariance, canonical finite-Pi head/tail splitting and
reindexing, and finite-sum formulas.

- [Dimension from finite coordinate-restriction images](dimension-from-finite-coordinate-restriction-ima.md)
- [Chain cardinalities of unions](chain-cardinalities-of-unions.md)
- [Chain cardinalities of exclusive-piece unions](chain-cardinalities-of-exclusive-piece-unions.md)
- [Krull dimension of exclusive-piece unions](krull-dimension-of-exclusive-piece-unions.md)
- [Dimension comparison and arbitrary unions](dimension-comparison-and-arbitrary-unions.md)
- [Krull dimension under finite covers](krull-dimension-under-finite-covers.md)
- [Chain cardinalities of disjoint sums](chain-cardinalities-of-disjoint-sums.md)
- [Finite localization near a minimal prime](finite-localization-near-a-minimal-prime.md)
- [Directed suprema of relations on a fixed set](directed-suprema-of-relations-on-a-fixed-set.md)
- [Directed unions: chain cardinality and order dimension](directed-unions-chain-cardinality-and-order-dime.md)
- [Chain cardinalities of lexicographic products](chain-cardinalities-of-lexicographic-products.md)
- [Chain cardinalities of lexicographic sums](chain-cardinalities-of-lexicographic-sums.md)
- [Chain cardinalities of dependent lexicographic sums](krull-dimension-and-chain-cardinalities-of-lexic.md)
- [Krull dimension of dependent lexicographic sums](krull-dimension-and-chain-cardinalities-of-lexic.md)

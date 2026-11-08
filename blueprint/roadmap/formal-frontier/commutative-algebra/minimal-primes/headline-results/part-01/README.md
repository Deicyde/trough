---
navigation: transparent
---

# Successors of finite product… to Common finite bases of…

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/README.md#headline-results) of [FormalFrontier/minimal-primes](https://github.com/FormalFrontier/minimal-primes) at commit [45952e34](https://github.com/FormalFrontier/minimal-primes/tree/45952e34e2da84045925cdfa45f0514356a2a608), Apache-2.0.*

- [Successors of finite product expansions](successors-of-finite-product-expansions.md)

### Ranks of dependent pointwise products

For arbitrary `ι : Type u`, independently universed given preorders
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
- [Chain cardinalities of dependent lexicographic sums](../../krull-dimension-and-chain-cardinalities-of-lexic.md)
- [Krull dimension of dependent lexicographic sums](../../krull-dimension-and-chain-cardinalities-of-lexic.md)
- [Krull dimension of lexicographic sums](../../krull-dimension-and-chain-cardinalities-of-lexic.md)
- [Krull dimension of lexicographic products](krull-dimension-of-lexicographic-products.md)

### Point heights and coheights of binary lexicographic products

For independently universed given preorders `α : Type u`, `β : Type v` and points
`a : α`, `b : β`, put `Hβ = (Set.univ : Set β).chainHeight (· < ·)`. The formulas
[`Order.height_toLex_prod` and `Order.coheight_toLex_prod`](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/KrullDimension.lean)
are

```text
height (toLex (a, b))   = height a   * Hβ + height b
coheight (toLex (a, b)) = coheight a * Hβ + coheight b
```

All arithmetic is in `ℕ∞`. Both use the same whole-second-factor strict-chain
**vertex cardinality**, not its Krull dimension, the rank of `b`, or the cardinality
of `β`. The target retains Mathlib's binary `Prod.Lex` preorder on `α ×ₗ β`:
`toLex (a, b) ≤ toLex (a', b')` means `a < a'` or `a = a' ∧ b ≤ b'`;
strict comparison replaces the second `≤` by `<`. Distinct weakly equivalent
first coordinates therefore give incomparable fibres. Within a fixed first
coordinate, distinct weakly equivalent second points remain mutually weakly
comparable. This is the binary preorder, not the equality-or-strict partial order
on dependent functions or the pointwise product order.

The supporting identities `Order.height_eq_chainHeight_Iio` and
`Order.coheight_eq_chainHeight_Ioi` identify point height and coheight with the
strict-chain vertex heights of the original strict lower and upper segments.
They use the given preorder's strict relation, without decomposing a closed
segment into its strict segment and an endpoint, which fails for general preorders.
There is no linearity, antisymmetry, finiteness, decidable equality, global
nonemptiness, bottom/top, finite-height or attainment hypothesis. The supplied
points inhabit both factors; empty strict segments have height zero, and
`0 * ⊤ = 0`. Infinite values include unbounded finite chains without a longest
or infinite chain.

The [middle-point client](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimesTest/Order/KrullDimension.lean) gives both
height four and coheight four at `toLex ((1 : Fin 3), (1 : Fin 3))`, whereas the
pointwise pair has both ranks two. Here `Hβ = 3`, not the second-factor dimension
two. The proofs combine the strict-segment identities with the existing whole
lexicographic product, disjoint-union, singleton-slice and direction-reversal
chain-height APIs.

- [Dimension and point ranks of finite dependent lexicographic products](../../dimension-and-point-ranks-of-finite-dependent-le.md)
- [Semimodules, annihilators and faithful actions on dependent reduced products](semimodules-annihilators-and-faithful-actions-on.md)

### Matrix rings over dependent reduced products

For an arbitrary filter `F`, given semirings `R i` and a fixed index type `J` with
`Fintype J` and `DecidableEq J`, the
[matrix leaf](https://github.com/FormalFrontier/minimal-primes/blob/45952e34e2da84045925cdfa45f0514356a2a608/MinimalPrimes/Order/Filter/Product/Matrix.lean) constructs
`Filter.Product.matrixRingEquiv` between `F.Product (fun i => Matrix J J (R i))`
and `Matrix J J (F.Product R)`. Its underlying equivalence composes the existing
finite-Pi equivalences. The source and target retain the given semirings and stock
matrix records: multiplication is a finite row-column sum, not pointwise entry
multiplication. Representative and all-point entry equations in both directions
form its characteristic interface. `Filter.Product.isUnit_matrix_coe_iff` states
invertibility of a represented matrix exactly on the eventual unit locus of those
same fibre matrices; it does not assert that each entry is a scalar unit.
Index, coefficient and matrix-index universes are independent; empty matrices,
empty index types, bottom filters and zero semirings are included. There are no
commutativity, ring, field, properness or nontriviality hypotheses.

- [Common finite bases of dependent reduced products](common-finite-bases-of-dependent-reduced-product.md)

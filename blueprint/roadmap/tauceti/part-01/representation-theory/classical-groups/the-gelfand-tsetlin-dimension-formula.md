---
declaration: theorem
origin: cited
lean: TauCeti.GTPattern.card_topRow_eq_weylDimension, TauCeti.GTPattern.card_topWeight_eq_weylDimension
statement: formalized
proof: formalized
---

# The Gelfand-Tsetlin dimension formula

The Gelfand-Tsetlin patterns with top row a
weakly decreasing sequence `λ` are counted by the Weyl dimension formula
`∏_{i < j} (λᵢ - λⱼ + j - i) / (j - i)`.

Both sides are candidates for the dimension of the irreducible rational representation of `GL n`
with highest weight `λ`, but that representation and the Gelfand-Tsetlin basis are not built here
and do not enter the proof: what is proved is the identity of a lattice-point count with a product
formula, obtained by checking that both satisfy the branching recursion of `GL (n + 1) ↓ GL n`.

This is deliberately not a `simp` lemma: `{P : GTPattern n // P.topRow = l}` carries a `Fintype`
instance, so `Nat.card_eq_fintype_card` rewrites the left-hand side first and the `simpNF` linter
rejects the tag.  The `DominantWeight`-indexed
`TauCeti.GTPattern.card_topWeight_eq_weylDimension` below, whose subtype has no such instance, is
the `simp` form.

```lean
TauCeti.GTPattern.card_topRow_eq_weylDimension {n : ℕ} (l : TauCeti.DominantWeight n) :
  Nat.card { P // P.topRow = ↑l } = TauCeti.weylDimension l
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GTPattern.card_topRow_eq_weylDimension`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Dimension.html#TauCeti.GTPattern.card_topRow_eq_weylDimension).

## Other forms

**The Gelfand-Tsetlin dimension formula, indexed by a dominant weight.** Formalized in Tau Ceti as [`TauCeti.GTPattern.card_topWeight_eq_weylDimension`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Dimension.html#TauCeti.GTPattern.card_topWeight_eq_weylDimension).

```lean
TauCeti.GTPattern.card_topWeight_eq_weylDimension {n : ℕ} (l : TauCeti.DominantWeight n) :
  Nat.card { P // P.topWeight = l } = TauCeti.weylDimension l
```

## Sources

- [Tau Ceti documentation: `TauCeti.GTPattern.card_topRow_eq_weylDimension`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Dimension.html#TauCeti.GTPattern.card_topRow_eq_weylDimension)
- [Source of `TauCeti.GTPattern.card_topRow_eq_weylDimension` in TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Dimension.lean#L171)

---
declaration: theorem
origin: cited
lean: TauCeti.isInternal_gtLine, TauCeti.GTPattern.card_topRow_eq_weylDimension, TauCeti.GTPattern.card_topWeight_eq_weylDimension
statement: formalized
proof: formalized
---

# The Gelfand–Tsetlin decomposition

The rational Weyl module `V_λ` of `GL n ℂ` is the
internal direct sum of the Gelfand–Tsetlin lines of the patterns with top weight `λ`.

```lean
TauCeti.isInternal_gtLine {n : ℕ} (l : TauCeti.DominantWeight n) :
  DirectSum.IsInternal (TauCeti.gtLine l)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse of Frobenius's formula](../symmetric/the-inverse-of-frobeniuss-formula.md)
- [Jacobi's bialternant formula](../../ring-theory/part-01/mv-polynomial/jacobis-bialternant-formula.md)
- [James's submodule theorem](../symmetric/jamess-submodule-theorem.md)
- [Schur-Weyl duality: the commutant of the image of `k[S_d]` is the image of `k[GLₙ]`](../symmetric/schur-weyl-duality-the-commutant-of-the-image-of.md)
- [The spectral theorem for normal matrices](../../analysis/part-02/matrix/the-spectral-theorem-for-normal-matrices.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isInternal_gtLine`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Line.html#TauCeti.isInternal_gtLine).

## Other forms

**The Gelfand-Tsetlin dimension formula.** Formalized in Tau Ceti as [`TauCeti.GTPattern.card_topRow_eq_weylDimension`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Dimension.html#TauCeti.GTPattern.card_topRow_eq_weylDimension).

```lean
TauCeti.GTPattern.card_topRow_eq_weylDimension {n : ℕ} (l : TauCeti.DominantWeight n) :
  Nat.card { P // P.topRow = ↑l } = TauCeti.weylDimension l
```

**The Gelfand-Tsetlin dimension formula, indexed by a dominant weight.** Formalized in Tau Ceti as [`TauCeti.GTPattern.card_topWeight_eq_weylDimension`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Dimension.html#TauCeti.GTPattern.card_topWeight_eq_weylDimension).

```lean
TauCeti.GTPattern.card_topWeight_eq_weylDimension {n : ℕ} (l : TauCeti.DominantWeight n) :
  Nat.card { P // P.topWeight = l } = TauCeti.weylDimension l
```

## Sources

- [Tau Ceti documentation: `TauCeti.isInternal_gtLine`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Line.html#TauCeti.isInternal_gtLine)
- [Source of `TauCeti.isInternal_gtLine` in TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Line.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Line.lean#L171)

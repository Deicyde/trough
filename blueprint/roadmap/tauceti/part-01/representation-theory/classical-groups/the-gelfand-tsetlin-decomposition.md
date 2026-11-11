---
declaration: theorem
origin: cited
lean: TauCeti.isInternal_gtLine
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
- [Jacobi's bialternant formula](../../ring-theory/part-01/multivariate-polynomials/jacobis-bialternant-formula.md)
- [James's submodule theorem](../symmetric/jamess-submodule-theorem.md)
- [Schur-Weyl duality: the commutant of the image of `k[S_d]` is the image of `k[GLₙ]`](../symmetric/schur-weyl-duality-the-commutant-of-the-image-of.md)
- [The spectral theorem for normal matrices](../../analysis/part-03/matrix/the-spectral-theorem-for-normal-matrices.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isInternal_gtLine`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Line.html#TauCeti.isInternal_gtLine).

## Sources

- [Tau Ceti documentation: `TauCeti.isInternal_gtLine`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Line.html#TauCeti.isInternal_gtLine)
- [Source of `TauCeti.isInternal_gtLine` in TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Line.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/ClassicalGroups/GelfandTsetlin/Line.lean#L171)

---
declaration: theorem
origin: cited
lean: ContRepresentation.frobeniusSchurIndicator_trichotomy
statement: formalized
proof: formalized
---

# The Frobenius-Schur reality trichotomy for compact groups

The indicator of an irreducible
unitary representation of a compact group on a finite-dimensional complex inner product space is
`1`, `0` or `-1`.

The indicator is the difference `dim (Sym²V)ᴳ - dim (Λ²V)ᴳ`
(`ContRepresentation.frobeniusSchurIndicator_eq_sub_finrank_invariants`) and those two dimensions
add up to at most `1` (`ContRepresentation.finrank_invariants_squares_le_one`), so the difference
is one of the three values.

```lean
ContRepresentation.frobeniusSchurIndicator_trichotomy.{u_1, u_2} {G : Type u_1} {V : Type u_2}
  [Group G] [TopologicalSpace G] [IsTopologicalGroup G] [CompactSpace G] [MeasurableSpace G]
  [BorelSpace G] [NormedAddCommGroup V] [InnerProductSpace ℂ V] [FiniteDimensional ℂ V]
  (π : ContRepresentation ℂ G V) (hπ : Continuous ⇑π) (hunitary : π.IsUnitary)
  (hirr : (ContRepresentation.toRepresentation ℂ G V π).IsIrreducible) :
  π.frobeniusSchurIndicator hπ = 1 ∨
    π.frobeniusSchurIndicator hπ = 0 ∨ π.frobeniusSchurIndicator hπ = -1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContRepresentation.frobeniusSchurIndicator_trichotomy`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/FrobeniusSchur/Trichotomy.html#ContRepresentation.frobeniusSchurIndicator_trichotomy).

## Sources

- [Tau Ceti documentation: `ContRepresentation.frobeniusSchurIndicator_trichotomy`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Compact/FrobeniusSchur/Trichotomy.html#ContRepresentation.frobeniusSchurIndicator_trichotomy)
- [Source of `ContRepresentation.frobeniusSchurIndicator_trichotomy` in TauCeti/RepresentationTheory/Compact/FrobeniusSchur/Trichotomy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Compact/FrobeniusSchur/Trichotomy.lean#L99)

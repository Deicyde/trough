---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_center_algEquiv_conjClasses
statement: formalized
proof: formalized
---

# The good-splitting structure theorem for a finite coefficient field

The centre of `K[G]`
is `K`-algebra isomorphic to the functions on the conjugacy classes of `G`.

The indexing is by cardinality only: the canonical indexing of the factors is by the maximal ideals
of the centre (`TauCeti.centerAlgEquivPi`), which `TauCeti.card_maximalSpectrum_center` counts.

```lean
TauCeti.nonempty_center_algEquiv_conjClasses.{u_1, u_2} {K : Type u_1} {G : Type u_2} [Field K]
  [Fintype K] [Group G] [Finite G] (hexp : ∀ (g : G), g ^ Fintype.card K = g) :
  Nonempty (↥(Subalgebra.center K (MonoidAlgebra K G)) ≃ₐ[K] ConjClasses G → K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_center_algEquiv_conjClasses`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/FiniteField.html#TauCeti.nonempty_center_algEquiv_conjClasses).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_center_algEquiv_conjClasses`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/FiniteField.html#TauCeti.nonempty_center_algEquiv_conjClasses)
- [Source of `TauCeti.nonempty_center_algEquiv_conjClasses` in TauCeti/RepresentationTheory/CharacterTable/FiniteField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/CharacterTable/FiniteField.lean#L205)

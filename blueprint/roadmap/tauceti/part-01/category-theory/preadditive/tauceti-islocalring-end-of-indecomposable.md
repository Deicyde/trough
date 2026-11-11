---
declaration: theorem
origin: cited
lean: TauCeti.isLocalRing_end_of_indecomposable
statement: formalized
proof: formalized
---

# TauCeti.isLocalRing_end_of_indecomposable

**Fitting's lemma: an indecomposable object has a local endomorphism ring**, in an
idempotent-complete linear category over a commutative Artinian ring `R` when the endomorphisms of
the object are finitely generated over `R`, for instance in a Hom-finite linear category over a
field. Indecomposability leaves `0` and `1` as the only idempotents of `End X`
(`TauCeti.idempotent_eq_zero_or_id_of_indecomposable`).

```lean
TauCeti.isLocalRing_end_of_indecomposable.{v, u, u_1} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C] {R : Type u_1} [CommRing R]
  [IsArtinianRing R] [CategoryTheory.Linear R C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  [CategoryTheory.IsIdempotentComplete C] {X : C} [Module.Finite R (X ⟶ X)]
  (hX : CategoryTheory.Indecomposable X) : IsLocalRing (CategoryTheory.End X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Fitting's lemma](../../ring-theory/part-01/krull-schmidt/fittings-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isLocalRing_end_of_indecomposable`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/Indecomposable.html#TauCeti.isLocalRing_end_of_indecomposable).

## Sources

- [Tau Ceti documentation: `TauCeti.isLocalRing_end_of_indecomposable`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/Indecomposable.html#TauCeti.isLocalRing_end_of_indecomposable)
- [Source of `TauCeti.isLocalRing_end_of_indecomposable` in TauCeti/CategoryTheory/Preadditive/Indecomposable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Preadditive/Indecomposable.lean#L276)

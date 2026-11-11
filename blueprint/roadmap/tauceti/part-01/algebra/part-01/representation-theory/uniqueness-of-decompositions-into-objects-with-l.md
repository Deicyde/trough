---
declaration: theorem
origin: cited
lean: TauCeti.exists_equiv_iso_of_biproduct_iso_of_isLocalRing
statement: formalized
proof: formalized
---

# Uniqueness of decompositions into objects with local endomorphism rings

two
decompositions `⨁ X ≅ ⨁ Y` of the same object into objects with local endomorphism rings match up
to a bijection of the summands. No hypothesis on the category beyond finite biproducts is needed;
in a Krull-Schmidt category this is the uniqueness of the decomposition of every object.

```lean
TauCeti.exists_equiv_iso_of_biproduct_iso_of_isLocalRing.{w, w', v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasFiniteBiproducts C] {ι : Type w} {κ : Type w'} [Finite ι] [Finite κ]
  (X : ι → C) (Y : κ → C) (hX : ∀ (i : ι), IsLocalRing (CategoryTheory.End (X i)))
  (hY : ∀ (j : κ), IsLocalRing (CategoryTheory.End (Y j))) (e : ⨁ X ≅ ⨁ Y) :
  ∃ σ, ∀ (i : ι), Nonempty (X i ≅ Y (σ i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_equiv_iso_of_biproduct_iso_of_isLocalRing`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Uniqueness.html#TauCeti.exists_equiv_iso_of_biproduct_iso_of_isLocalRing).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_equiv_iso_of_biproduct_iso_of_isLocalRing`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Uniqueness.html#TauCeti.exists_equiv_iso_of_biproduct_iso_of_isLocalRing)
- [Source of `TauCeti.exists_equiv_iso_of_biproduct_iso_of_isLocalRing` in TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Uniqueness.lean#L125)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RepresentationTheory/STATUS.md)

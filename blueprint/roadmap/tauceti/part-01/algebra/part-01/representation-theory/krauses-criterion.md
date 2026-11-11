---
declaration: theorem
origin: cited
lean: TauCeti.isKrullSchmidt_iff_isIdempotentComplete_and_isSemiperfectRing_end
statement: formalized
proof: formalized
---

# Krause's criterion

a category with finite biproducts is Krull-Schmidt exactly when
idempotents split and the endomorphism ring of every object is semiperfect.

```lean
TauCeti.isKrullSchmidt_iff_isIdempotentComplete_and_isSemiperfectRing_end.{v_1, u_1} {C : Type u_1}
  [CategoryTheory.Category.{v_1, u_1} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasFiniteBiproducts C] :
  TauCeti.IsKrullSchmidt C ↔
    CategoryTheory.IsIdempotentComplete C ∧
      ∀ (X : C), TauCeti.IsSemiperfectRing (CategoryTheory.End X)
```

## Depends on

- [A Krull-Schmidt category](a-krull-schmidt-category.md)

## Proof depends on

- [Fitting's lemma](../../../ring-theory/part-01/krull-schmidt/fittings-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isKrullSchmidt_iff_isIdempotentComplete_and_isSemiperfectRing_end`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Semiperfect.html#TauCeti.isKrullSchmidt_iff_isIdempotentComplete_and_isSemiperfectRing_end).

## Sources

- [Tau Ceti documentation: `TauCeti.isKrullSchmidt_iff_isIdempotentComplete_and_isSemiperfectRing_end`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Semiperfect.html#TauCeti.isKrullSchmidt_iff_isIdempotentComplete_and_isSemiperfectRing_end)
- [Source of `TauCeti.isKrullSchmidt_iff_isIdempotentComplete_and_isSemiperfectRing_end` in TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Semiperfect.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Preadditive/KrullSchmidt/Semiperfect.lean#L133)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RepresentationTheory/STATUS.md)

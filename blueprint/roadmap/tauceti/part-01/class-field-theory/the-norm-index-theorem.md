---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.card_ideleClassNormQuotient
statement: formalized
proof: formalized
---

# The norm index theorem

for a finite abelian extension `L/K` of number fields,
`[C_K : N_{L/K}(C_L)] = [L : K]`, since finite global reciprocity identifies the norm quotient with
`Gal(L/K)^ab`, which is `Gal(L/K)` itself.

```lean
TauCeti.ClassFieldTheory.card_ideleClassNormQuotient.{u_1} (K : Type) [Field K] [NumberField K]
  (L : Type u_1) [Field L] [NumberField L] [Algebra K L] [IsAbelianGalois K L] :
  Nat.card
      (NumberField.IdeleClassGroup (NumberField.RingOfIntegers K) K ⧸
        (↑(TauCeti.GlobalNumberFields.ideleClassNormMap K L)).range) =
    Module.finrank K L
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Finite global reciprocity](finite-global-reciprocity.md)
- [The semi-local decomposition](../../part-05/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.card_ideleClassNormQuotient`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.html#TauCeti.ClassFieldTheory.card_ideleClassNormQuotient).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.card_ideleClassNormQuotient`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.html#TauCeti.ClassFieldTheory.card_ideleClassNormQuotient)
- [Source of `TauCeti.ClassFieldTheory.card_ideleClassNormQuotient` in TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.lean#L245)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)

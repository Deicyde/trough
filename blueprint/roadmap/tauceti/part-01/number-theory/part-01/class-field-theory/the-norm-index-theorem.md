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

- [The global class formation](the-global-class-formation.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.card_ideleClassNormQuotient`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.html#TauCeti.ClassFieldTheory.card_ideleClassNormQuotient).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.card_ideleClassNormQuotient`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.html#TauCeti.ClassFieldTheory.card_ideleClassNormQuotient)
- [Source of `TauCeti.ClassFieldTheory.card_ideleClassNormQuotient` in TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.lean#L245)

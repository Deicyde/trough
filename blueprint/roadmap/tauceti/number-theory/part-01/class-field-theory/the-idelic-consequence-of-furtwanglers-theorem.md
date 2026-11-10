---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator
statement: formalized
proof: formalized
---

# The idelic consequence of Furtwängler's theorem

If `Lay` represents `L/F` and `E` is
its maximal abelian subextension, every idele class of `F`, extended to `E`, is a norm from `L`.
The field `E` is pinned as the fixed field of the preimage of the commutator subgroup of the
finite Galois group; no norm or principalization hypothesis is assumed.

```lean
TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator {K : Type}
  [Field K] [NumberField K] {F E L : IntermediateField K (SeparableClosure K)} [NumberField ↥F]
  [NumberField ↥E] [NumberField ↥L] [Algebra ↥F ↥E] [IsScalarTower (↥F) (↥E) (SeparableClosure K)]
  [Algebra ↥E ↥L] [IsScalarTower (↥E) (↥L) (SeparableClosure K)]
  (Lay : TauCeti.ClassFieldTheory.NormalLayer (TauCeti.AbsoluteGaloisGroup K))
  (hF : IntermediateField.fixedField ↑Lay.ground = F)
  (hE : IntermediateField.fixedField ↑(Lay.subgroupLayer (commutator Lay.Gal)).ground = E)
  (hL : IntermediateField.fixedField ↑Lay.top = L)
  (c : NumberField.IdeleClassGroup (NumberField.RingOfIntegers ↥F) ↥F) :
  (TauCeti.GlobalNumberFields.ideleClassExtension ↥F ↥E) c ∈
    (↑(TauCeti.GlobalNumberFields.ideleClassNormMap ↥E ↥L)).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global class formation](the-global-class-formation.md)
- [The principal ideal theorem for a class formation](../../part-02/class-field-theory/the-principal-ideal-theorem-for-a-class-formatio.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/PrincipalIdeal.html#TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/PrincipalIdeal.html#TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator)
- [Source of `TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator` in TauCeti/NumberTheory/ClassFieldTheory/Global/PrincipalIdeal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/PrincipalIdeal.lean#L52)

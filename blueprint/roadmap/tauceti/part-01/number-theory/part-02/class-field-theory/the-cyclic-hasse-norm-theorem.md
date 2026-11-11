---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.cyclicHasseNorm, TauCeti.ClassFieldTheory.isGlobalNorm_iff_isLocalNormEverywhere
statement: formalized
proof: formalized
---

# The cyclic Hasse norm theorem

For a cyclic extension `L/K` of number fields, an element
`a ∈ Kˣ` lies in `N_{L/K}(Lˣ)` exactly when its principal idele is the norm of an idele of `L`.

```lean
TauCeti.ClassFieldTheory.cyclicHasseNorm (K : Type) [Field K] [NumberField K] (L : Type) [Field L]
  [NumberField L] [Algebra K L] [IsGalois K L] [IsCyclic Gal(L/K)] (a : Kˣ) :
  a ∈ TauCeti.normGroup K L ↔
    (NumberField.IdeleGroup.unitEmbedding (NumberField.RingOfIntegers K) K) a ∈
      (TauCeti.GlobalNumberFields.ideleNormMap K L).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [The Galois action on the semi-local decomposition](../number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [The Kummer case of the second fundamental inequality](the-kummer-case-of-the-second-fundamental-inequa.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma for the normalized order](shapiros-lemma-for-the-normalized-order.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [The Sylow reduction of Tate's triviality criterion (Milne II 3.10, last paragraph)](../../../representation-theory/homological/the-sylow-reduction-of-tates-triviality-criterio.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.cyclicHasseNorm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/HasseNorm/Basic.html#TauCeti.ClassFieldTheory.cyclicHasseNorm).

## Other forms

**The cyclic Hasse norm theorem, placewise.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.isGlobalNorm_iff_isLocalNormEverywhere`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/HasseNorm/Basic.html#TauCeti.ClassFieldTheory.isGlobalNorm_iff_isLocalNormEverywhere).

```lean
TauCeti.ClassFieldTheory.isGlobalNorm_iff_isLocalNormEverywhere (K : Type) [Field K] [NumberField K]
  (L : Type) [Field L] [NumberField L] [Algebra K L] [IsGalois K L] [IsCyclic Gal(L/K)] (a : Kˣ) :
  a ∈ TauCeti.normGroup K L ↔ TauCeti.GlobalNumberFields.IsLocalNormEverywhere K L a
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.cyclicHasseNorm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/HasseNorm/Basic.html#TauCeti.ClassFieldTheory.cyclicHasseNorm)
- [Source of `TauCeti.ClassFieldTheory.cyclicHasseNorm` in TauCeti/NumberTheory/ClassFieldTheory/Global/HasseNorm/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/Global/HasseNorm/Basic.lean#L153)

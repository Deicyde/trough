---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.globalArtinEquiv
statement: formalized
---

# Finite global reciprocity `C_K / N_{L/K}(C_L) ≃ Gal(L/K)^ab` for a finite Galois extension `L/K` of number fields, embedded in the separable closure of `K` by `ι`

the abstract Artin
reciprocity isomorphism `ClassFormation.artinEquiv` of the global class formation on the layer of
`L`, read through `globalLayerNormQuotientEquiv K L` and `layerGalEquiv ι`. It does not depend on
`ι` (`globalArtinEquiv_eq_of_iota`).

```lean
TauCeti.ClassFieldTheory.globalArtinEquiv.{u_1} (K : Type) [Field K] [NumberField K] (L : Type u_1)
  [Field L] [NumberField L] [Algebra K L] [IsGalois K L] (ι : L →ₐ[K] SeparableClosure K) :
  Additive
      (NumberField.IdeleClassGroup (NumberField.RingOfIntegers K) K ⧸
        (↑(TauCeti.GlobalNumberFields.ideleClassNormMap K L)).range) ≃+
    Additive (Abelianization Gal(L/K))
```

## Depends on

- [The global class formation](the-global-class-formation.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.globalArtinEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.html#TauCeti.ClassFieldTheory.globalArtinEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.globalArtinEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.html#TauCeti.ClassFieldTheory.globalArtinEquiv)
- [Source of `TauCeti.ClassFieldTheory.globalArtinEquiv` in TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/Reciprocity.lean#L108)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)

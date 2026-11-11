---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.rayClassField
statement: formalized
---

# The ray class field of a modulus `𝔪` of a number field `K`

the class field in `Kˢ` of
the ray subgroup of `𝔪` under the global class-field correspondence, that is, the unique finite
abelian extension of `K` in `Kˢ` whose idele-class norm group is the ray subgroup of `𝔪`
(`range_ideleClassNormMap_rayClassField`).

```lean
TauCeti.ClassFieldTheory.rayClassField {K : Type} [Field K] [NumberField K]
  (𝔪 : TauCeti.GlobalNumberFields.Modulus K) : IntermediateField K (SeparableClosure K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Global existence (Milne VII, Theorem 9.5)](global-existence-milne-vii-theorem-9-5.md)
- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](../global-number-fields-ray-classes-adeles-and-heck/isdedekinddomain-finiteadelering-sintegraladeles.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.rayClassField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/RayClassField.html#TauCeti.ClassFieldTheory.rayClassField).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.rayClassField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/RayClassField.html#TauCeti.ClassFieldTheory.rayClassField)
- [Source of `TauCeti.ClassFieldTheory.rayClassField` in TauCeti/NumberTheory/ClassFieldTheory/ClassFields/RayClassField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/RayClassField.lean#L122)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassFieldTheory/STATUS.md)

---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.ringClassField
statement: formalized
---

# The ring class field of an order `O` of a number field `K`

the class field in `Kˢ` of the
kernel of the ring-class quotient `C_K → Pic O` under the global class-field correspondence, that
is, the unique finite abelian extension of `K` in `Kˢ` whose idele-class norm group is that kernel
(`range_ideleClassNormMap_ringClassField`).

```lean
TauCeti.ClassFieldTheory.ringClassField {K : Type} [Field K] [NumberField K]
  (O : TauCeti.GlobalNumberFields.NumberFieldOrder K) : IntermediateField K (SeparableClosure K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Global existence (Milne VII, Theorem 9.5)](global-existence-milne-vii-theorem-9-5.md)
- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](../global-number-fields-ray-classes-adeles-and-heck/isdedekinddomain-finiteadelering-sintegraladeles.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ringClassField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/RingClass/Field.html#TauCeti.ClassFieldTheory.ringClassField).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.ringClassField`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/RingClass/Field.html#TauCeti.ClassFieldTheory.ringClassField)
- [Source of `TauCeti.ClassFieldTheory.ringClassField` in TauCeti/NumberTheory/ClassFieldTheory/ClassFields/RingClass/Field.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/RingClass/Field.lean#L137)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassFieldTheory/STATUS.md)

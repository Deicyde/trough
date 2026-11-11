---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.globalClassFieldCorrespondence
statement: formalized
---

# The global class-field correspondence

Open finite-index subgroups of `C_K` correspond
order preservingly to finite abelian layers of `G_K`, and hence order reversingly to their fixed
fields.

```lean
TauCeti.ClassFieldTheory.globalClassFieldCorrespondence {K : Type} [Field K] [NumberField K] :
  TauCeti.ClassFieldTheory.GlobalNormSubgroups K ≃o
    TauCeti.ClassFieldTheory.AbelianLayer (TauCeti.AbsoluteGaloisGroup K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [The global class formation](the-global-class-formation.md)
- [Global existence (Milne VII, Theorem 9.5)](global-existence-milne-vii-theorem-9-5.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](../global-number-fields-ray-classes-adeles-and-heck/isdedekinddomain-finiteadelering-sintegraladeles.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.globalClassFieldCorrespondence`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Correspondence.html#TauCeti.ClassFieldTheory.globalClassFieldCorrespondence).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.globalClassFieldCorrespondence`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Correspondence.html#TauCeti.ClassFieldTheory.globalClassFieldCorrespondence)
- [Source of `TauCeti.ClassFieldTheory.globalClassFieldCorrespondence` in TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Correspondence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Correspondence.lean#L115)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassFieldTheory/STATUS.md)

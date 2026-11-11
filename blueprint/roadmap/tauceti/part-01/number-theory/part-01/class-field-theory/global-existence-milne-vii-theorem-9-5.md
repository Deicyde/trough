---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.globalAbelianExistence
statement: formalized
proof: formalized
---

# Global existence (Milne VII, Theorem 9.5)

For a number field `K`, every open subgroup of
finite index of the idele class group `C_K` is the norm subgroup of a finite abelian extension of
`K`.

```lean
TauCeti.ClassFieldTheory.globalAbelianExistence {K : Type} [Field K] [NumberField K]
  {N : Subgroup (NumberField.IdeleClassGroup (NumberField.RingOfIntegers K) K)} (hN : IsOpen ↑N)
  [N.FiniteIndex] :
  ∃ V, V.IsAbelianClassFieldLayer ∧ TauCeti.ClassFieldTheory.globalNormSubgroup K V = N
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's bound](../../../linear-algebra/other-results/dedekinds-bound.md)
- [The Galois action on the semi-local decomposition](../../part-02/number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [The global class formation](the-global-class-formation.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../../part-02/number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [The local class formation](the-local-class-formation.md)
- [The norm index theorem](the-norm-index-theorem.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.globalAbelianExistence`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Existence.html#TauCeti.ClassFieldTheory.globalAbelianExistence).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.globalAbelianExistence`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Existence.html#TauCeti.ClassFieldTheory.globalAbelianExistence)
- [Source of `TauCeti.ClassFieldTheory.globalAbelianExistence` in TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Existence.lean#L210)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassFieldTheory/STATUS.md)

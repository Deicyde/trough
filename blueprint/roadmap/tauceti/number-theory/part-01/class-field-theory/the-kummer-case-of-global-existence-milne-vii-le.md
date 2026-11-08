---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem
statement: formalized
proof: formalized
---

# The Kummer case of global existence (Milne VII, Lemma 9.3)

Let `K` be a number field
containing the `p`-th roots of unity for a prime `p`. Every open subgroup of the idele class group
`C_K` containing the `p`-th powers is the norm subgroup of a finite abelian extension of `K`.

```lean
TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem {K : Type} [Field K]
  [NumberField K] {p : ℕ} [Fact (Nat.Prime p)] [HasEnoughRootsOfUnity K p]
  {N : Subgroup (NumberField.IdeleClassGroup (NumberField.RingOfIntegers K) K)} (hN : IsOpen ↑N)
  (hpow : ∀ (c : NumberField.IdeleClassGroup (NumberField.RingOfIntegers K) K), c ^ p ∈ N) :
  ∃ V, V.IsAbelianClassFieldLayer ∧ TauCeti.ClassFieldTheory.globalNormSubgroup K V = N
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's bound](../../../linear-algebra/other-results/dedekinds-bound.md)
- [The Galois action on the semi-local decomposition](../../part-02/number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [The global class formation](the-global-class-formation.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The local class formation](the-local-class-formation.md)
- [The norm index theorem](the-norm-index-theorem.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Kummer.html#TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Kummer.html#TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem)
- [Source of `TauCeti.ClassFieldTheory.exists_abelianLayer_globalNormSubgroup_eq_of_pow_mem` in TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Kummer.lean#L124)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)

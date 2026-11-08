---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.kroneckerWeber
statement: formalized
proof: formalized
---

# The Kronecker–Weber theorem

every finite abelian extension of `ℚ` embeds in a cyclotomic
field `ℚ(ζ_n)`.

```lean
TauCeti.ClassFieldTheory.kroneckerWeber (E : Type) [Field E] [NumberField E] [IsAbelianGalois ℚ E] :
  ∃ n, n ≠ 0 ∧ Nonempty (E →ₐ[ℚ] CyclotomicField n ℚ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin reciprocity commutes with conjugation](artin-reciprocity-commutes-with-conjugation.md)
- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [Finite global reciprocity](../../part-01/class-field-theory/finite-global-reciprocity.md)
- [The first half of Dedekind's different theorem](../local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois action on the semi-local decomposition](../number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [The Galois group of the maximal unramified extension is the profinite integers](../../part-01/local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The global class formation](../../part-01/class-field-theory/the-global-class-formation.md)
- [The global invariant](../../part-01/class-field-theory/the-global-invariant.md)
- [The Hasse principle for Brauer classes, from idele-class `H¹`](the-hasse-principle-for-brauer-classes-from-idel.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The ideal-theoretic Artin map](../../part-01/number-fields-ramification-frobenius-and-the-lmf/the-ideal-theoretic-artin-map.md)
- [The inverse of Shapiro's isomorphism in homology is corestriction of the unit](../../../representation-theory/homological/the-inverse-of-shapiros-isomorphism-in-homology.md)
- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](../../part-01/global-number-fields-ray-classes-adeles-and-heck/isdedekinddomain-finiteadelering-sintegraladeles.md)
- [The Kummer case of the second fundamental inequality](the-kummer-case-of-the-second-fundamental-inequa.md)
- [The local Artin symbol is finite local reciprocity at a place above `v`](the-local-artin-symbol-is-finite-local-reciproci.md)
- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [The Mackey formula for the degree-one corestriction cochain](../../../representation-theory/homological/the-mackey-formula-for-the-degree-one-corestrict.md)
- [The ray class group of `ℚ` modulo `(n)·∞` is the Galois group of `ℚ(ζ_n)`](../../part-01/global-number-fields-ray-classes-adeles-and-heck/the-ray-class-group-of-q-modulo-n-is-the-galois.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-01/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [The Sylow reduction of Tate's triviality criterion (Milne II 3.10, last paragraph)](../../../representation-theory/homological/the-sylow-reduction-of-tates-triviality-criterio.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../../part-01/class-field-theory/tauceti-classfieldtheory-tatetheorem.md)
- [TauCeti.relDiscr](../../part-01/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.kroneckerWeber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/KroneckerWeber.html#TauCeti.ClassFieldTheory.kroneckerWeber).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.kroneckerWeber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/KroneckerWeber.html#TauCeti.ClassFieldTheory.kroneckerWeber)
- [Source of `TauCeti.ClassFieldTheory.kroneckerWeber` in TauCeti/NumberTheory/ClassFieldTheory/ClassFields/KroneckerWeber.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/KroneckerWeber.lean#L176)

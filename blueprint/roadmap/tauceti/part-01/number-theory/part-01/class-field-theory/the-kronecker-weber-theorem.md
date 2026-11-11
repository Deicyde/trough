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

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois action on the semi-local decomposition](../../part-02/number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [The Galois group of the maximal unramified extension is the profinite integers](../local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The global class formation](the-global-class-formation.md)
- [The global invariant](the-global-invariant.md)
- [The Hasse principle for Brauer classes, from idele-class `H¹`](../../part-02/class-field-theory/the-hasse-principle-for-brauer-classes-from-idel.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The ideal-theoretic Artin map](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-ideal-theoretic-artin-map.md)
- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../../part-02/number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](../global-number-fields-ray-classes-adeles-and-heck/isdedekinddomain-finiteadelering-sintegraladeles.md)
- [The Kummer case of the second fundamental inequality](../../part-02/class-field-theory/the-kummer-case-of-the-second-fundamental-inequa.md)
- [The local class formation](the-local-class-formation.md)
- [The local invariant](the-local-invariant.md)
- [The Mackey formula for the degree-one corestriction cochain](../../../representation-theory/homological/the-mackey-formula-for-the-degree-one-corestrict.md)
- [The ray class group of `ℚ` modulo `(n)·∞` is the Galois group of `ℚ(ζ_n)`](../global-number-fields-ray-classes-adeles-and-heck/the-ray-class-group-of-q-modulo-n-is-the-galois.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [The Sylow reduction of Tate's triviality criterion (Milne II 3.10, last paragraph)](../../../representation-theory/homological/the-sylow-reduction-of-tates-triviality-criterio.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.kroneckerWeber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/KroneckerWeber.html#TauCeti.ClassFieldTheory.kroneckerWeber).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.kroneckerWeber`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/KroneckerWeber.html#TauCeti.ClassFieldTheory.kroneckerWeber)
- [Source of `TauCeti.ClassFieldTheory.kroneckerWeber` in TauCeti/NumberTheory/ClassFieldTheory/ClassFields/KroneckerWeber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/ClassFields/KroneckerWeber.lean#L176)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassFieldTheory/STATUS.md)

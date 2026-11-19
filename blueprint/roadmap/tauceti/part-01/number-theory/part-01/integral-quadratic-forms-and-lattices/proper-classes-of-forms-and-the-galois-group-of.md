---
declaration: def
origin: cited
lean: TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal
statement: formalized
---

# Proper classes of forms and the Galois group of the ring class field

The proper classes
of primitive positive definite forms of discriminant `-n` are in bijection with the Galois group
of the ring class field of the quadratic order of discriminant `-n` over `ℚ(√(-n))`: the
bijection with the Picard group of the order, followed by ring-class reciprocity.

```lean
TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal (n : ℕ) [NeZero n]
  (hn : -↑n % 4 = 0 ∨ -↑n % 4 = 1) :
  TauCeti.BinaryQuadraticForm.PosDefProperClass n ≃
    Gal(↥(TauCeti.ClassFieldTheory.ringClassField
          (TauCeti.QuadraticOrder.numberFieldOrder (-↑n) hn))/QuadraticAlgebra ℚ (↑(-↑n)) 0)
```

## Depends on

- [The local invariant](../class-field-theory/the-local-invariant.md)
- [The ring class field of an order `O` of a number field `K`](../class-field-theory/the-ring-class-field-of-an-order-o-of-a-number-f.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Tate's theorem for a class formation, in every integer degree](../class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic](tauceti-binaryquadraticform-posdefproperclassequ.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/part-01/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois action on the semi-local decomposition](../../part-03/number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [The Galois group of the maximal unramified extension is the profinite integers](../local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [Global existence (Milne VII, Theorem 9.5)](../class-field-theory/global-existence-milne-vii-theorem-9-5.md)
- [The Hasse principle for Brauer classes, from idele-class `H¹`](../../part-02/class-field-theory/the-hasse-principle-for-brauer-classes-from-idel.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../../part-02/number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](../global-number-fields-ray-classes-adeles-and-heck/isdedekinddomain-finiteadelering-sintegraladeles.md)
- [The Kummer case of the second fundamental inequality](../../part-02/class-field-theory/the-kummer-case-of-the-second-fundamental-inequa.md)
- [The Mackey formula for the degree-one corestriction cochain](../../../representation-theory/homological/the-mackey-formula-for-the-degree-one-corestrict.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [The Sylow reduction of Tate's triviality criterion (Milne II 3.10, last paragraph)](../../../representation-theory/homological/the-sylow-reduction-of-tates-triviality-criterio.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../class-field-theory/tauceti-classfieldtheory-tatetheorem.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/RingClassField.html#TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/RingClassField.html#TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal)
- [Source of `TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal` in TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/RingClassField.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/RingClassField.lean#L79)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/IntegralLattices/STATUS.md)

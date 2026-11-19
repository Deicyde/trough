---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator
statement: formalized
proof: formalized
---

# The idelic consequence of Furtwängler's theorem

If `Lay` represents `L/F` and `E` is
its maximal abelian subextension, every idele class of `F`, extended to `E`, is a norm from `L`.
The field `E` is pinned as the fixed field of the preimage of the commutator subgroup of the
finite Galois group; no norm or principalization hypothesis is assumed.

```lean
TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator {K : Type}
  [Field K] [NumberField K] {F E L : IntermediateField K (SeparableClosure K)} [NumberField ↥F]
  [NumberField ↥E] [NumberField ↥L] [Algebra ↥F ↥E] [IsScalarTower (↥F) (↥E) (SeparableClosure K)]
  [Algebra ↥E ↥L] [IsScalarTower (↥E) (↥L) (SeparableClosure K)]
  (Lay : TauCeti.ClassFieldTheory.NormalLayer (TauCeti.AbsoluteGaloisGroup K))
  (hF : IntermediateField.fixedField ↑Lay.ground = F)
  (hE : IntermediateField.fixedField ↑(Lay.subgroupLayer (commutator Lay.Gal)).ground = E)
  (hL : IntermediateField.fixedField ↑Lay.top = L)
  (c : NumberField.IdeleClassGroup (NumberField.RingOfIntegers ↥F) ↥F) :
  (TauCeti.GlobalNumberFields.ideleClassExtension ↥F ↥E) c ∈
    (↑(TauCeti.GlobalNumberFields.ideleClassNormMap ↥E ↥L)).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/part-01/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois action on the semi-local decomposition](../../part-03/number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [The Galois group of the maximal unramified extension is the profinite integers](../../part-01/local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The Hasse principle for Brauer classes, from idele-class `H¹`](the-hasse-principle-for-brauer-classes-from-idel.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [The Kummer case of the second fundamental inequality](the-kummer-case-of-the-second-fundamental-inequa.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [The Mackey formula for the degree-one corestriction cochain](../../../representation-theory/homological/the-mackey-formula-for-the-degree-one-corestrict.md)
- [The principal ideal theorem for a class formation](the-principal-ideal-theorem-for-a-class-formatio.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [The Sylow reduction of Tate's triviality criterion (Milne II 3.10, last paragraph)](../../../representation-theory/homological/the-sylow-reduction-of-tates-triviality-criterio.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../../part-01/class-field-theory/tauceti-classfieldtheory-tatetheorem.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/PrincipalIdeal.html#TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/PrincipalIdeal.html#TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator)
- [Source of `TauCeti.ClassFieldTheory.ideleClassExtension_mem_range_ideleClassNormMap_commutator` in TauCeti/NumberTheory/ClassFieldTheory/Global/PrincipalIdeal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ClassFieldTheory/Global/PrincipalIdeal.lean#L52)

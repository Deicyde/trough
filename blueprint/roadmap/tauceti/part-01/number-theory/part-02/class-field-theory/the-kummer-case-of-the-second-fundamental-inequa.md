---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.index_range_ideleClassNormMap_le_of_finrank_prime
statement: formalized
proof: formalized
---

# The Kummer case of the second fundamental inequality

Let `L/K` be a Galois extension of
number fields of prime degree `p`, and suppose that `K` contains the `p`-th roots of unity. Then
the idele-class norm group has index at most `p`:
`[C_K : N_{L/K}(C_L)] ≤ p`.

```lean
TauCeti.ClassFieldTheory.index_range_ideleClassNormMap_le_of_finrank_prime (K L : Type) [Field K]
  [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L] (p : ℕ)
  [Fact (Nat.Prime p)] [HasEnoughRootsOfUnity K p] (hfin : Module.finrank K L = p) :
  (TauCeti.GlobalNumberFields.ideleClassNormMap K L).range.index ≤ p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's bound](../../../linear-algebra/other-results/dedekinds-bound.md)
- [Euler's criterion in a finite residue domain](../../../ring-theory/part-02/other-results/part-01/eulers-criterion-in-a-finite-residue-domain.md)
- [The Galois action on the semi-local decomposition](../number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.index_range_ideleClassNormMap_le_of_finrank_prime`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Kummer/Index.html#TauCeti.ClassFieldTheory.index_range_ideleClassNormMap_le_of_finrank_prime).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.index_range_ideleClassNormMap_le_of_finrank_prime`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Kummer/Index.html#TauCeti.ClassFieldTheory.index_range_ideleClassNormMap_le_of_finrank_prime)
- [Source of `TauCeti.ClassFieldTheory.index_range_ideleClassNormMap_le_of_finrank_prime` in TauCeti/NumberTheory/ClassFieldTheory/Global/Kummer/Index.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/Global/Kummer/Index.lean#L277)

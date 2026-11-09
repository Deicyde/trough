---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_groupCohomology_one, TauCeti.ClassFieldTheory.brLocalization_injective, TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_h1_globalFormation
statement: formalized
proof: formalized
---

# The Hasse principle for Brauer classes, from idele-class `H¹`

If `H¹(Gal(L/K), C_L)`
vanishes for every finite Galois extension `L/K`, then a Brauer class of `K` whose localizations
at all places vanish is zero: `Br K → ⨁_v Br K_v` is injective.

```lean
TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_groupCohomology_one (K : Type)
  [Field K] [NumberField K]
  (h :
    ∀ (L : Type) [inst : Field L] [inst_1 : NumberField L] [inst_2 : Algebra K L] [IsGalois K L],
      Subsingleton ↑(groupCohomology (TauCeti.ClassFieldTheory.ideleClassRep K L) 1)) :
  Function.Injective ⇑(TauCeti.ClassFieldTheory.brLocalization K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [The Galois action on the semi-local decomposition](../number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The Kummer case of the second fundamental inequality](the-kummer-case-of-the-second-fundamental-inequa.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-01/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma for the normalized order](shapiros-lemma-for-the-normalized-order.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [The Sylow reduction of Tate's triviality criterion (Milne II 3.10, last paragraph)](../../../representation-theory/homological/the-sylow-reduction-of-tates-triviality-criterio.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-01/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_groupCohomology_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Brauer/LocalizationKernel.html#TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_groupCohomology_one).

## Other forms

**The Hasse principle for the Brauer group (Albert–Brauer–Hasse–Noether).** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.brLocalization_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Brauer/SumFormula.html#TauCeti.ClassFieldTheory.brLocalization_injective).

```lean
TauCeti.ClassFieldTheory.brLocalization_injective (K : Type) [Field K] [NumberField K] :
  Function.Injective ⇑(TauCeti.ClassFieldTheory.brLocalization K)
```

**The Hasse principle from the vanishing of `H¹` on the idele-class formation.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_h1_globalFormation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Brauer/LocalizationKernel.html#TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_h1_globalFormation).

```lean
TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_h1_globalFormation (K : Type)
  [Field K] [NumberField K]
  (h :
    ∀ (V : OpenNormalSubgroup (TauCeti.AbsoluteGaloisGroup K)),
      Subsingleton
        ↑((TauCeti.ClassFieldTheory.NormalLayer.ofOpenNormal V).H
            (TauCeti.ClassFieldTheory.globalFormation K) 1)) :
  Function.Injective ⇑(TauCeti.ClassFieldTheory.brLocalization K)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_groupCohomology_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Brauer/LocalizationKernel.html#TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_groupCohomology_one)
- [Source of `TauCeti.ClassFieldTheory.brLocalization_injective_of_subsingleton_groupCohomology_one` in TauCeti/NumberTheory/ClassFieldTheory/Global/Brauer/LocalizationKernel.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/Brauer/LocalizationKernel.lean#L137)

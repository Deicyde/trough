---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self, TauCeti.ClassFieldTheory.dualityMap_bijective_discreteCoind_kummerCoeff
statement: formalized
proof: formalized
---

# Tate's duality on an open subgroup acting trivially on `μₙ`

Let `V` be an open subgroup of
`G_K` acting trivially on `μₙ`, for `n` invertible in the local field `K`. For every finite discrete
`V`-module `A` killed by `n` on which `V` acts trivially, the three duality maps
`Hⁱ(V, A) → Hom(H²⁻ⁱ(V, Hom(A, μₙ)), H²(V, μₙ))` are bijective.

```lean
TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self {K : Type} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} (hn : IsUnit ↑n)
  (V : Subgroup (TauCeti.AbsoluteGaloisGroup K)) (hV : IsOpen ↑V)
  (hVN : ∀ v ∈ V, ∀ (y : TauCeti.KummerCoeff K n), v • y = y) (A : Type) [AddCommGroup A]
  [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction (↥V) A] [ContinuousSMul (↥V) A]
  [Finite A] (hA : ∀ (a : A), n • a = 0) (hAV : ∀ (v : ↥V) (a : A), v • a = a) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 (↥V) A (TauCeti.KummerCoeff K n)) ∧
    Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 (↥V) A (TauCeti.KummerCoeff K n)) ∧
      Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap2 (↥V) A (TauCeti.KummerCoeff K n))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Dedekind's different theorem, the tame case](../local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.html#TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self).

## Other forms

**Tate's duality on a module coinduced from an open subgroup acting trivially on `μₙ`.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap_bijective_discreteCoind_kummerCoeff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.html#TauCeti.ClassFieldTheory.dualityMap_bijective_discreteCoind_kummerCoeff).

```lean
TauCeti.ClassFieldTheory.dualityMap_bijective_discreteCoind_kummerCoeff {K : Type} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} (hn : IsUnit ↑n)
  (V : Subgroup (TauCeti.AbsoluteGaloisGroup K)) (hV : IsOpen ↑V)
  (hVN : ∀ v ∈ V, ∀ (y : TauCeti.KummerCoeff K n), v • y = y) (A : Type) [AddCommGroup A]
  [TopologicalSpace A] [DiscreteTopology A] [DistribMulAction (↥V) A] [ContinuousSMul (↥V) A]
  [Finite A] (hA : ∀ (a : A), n • a = 0) (hAV : ∀ (v : ↥V) (a : A), v • a = a) [V.FiniteIndex] :
  Function.Bijective
      ⇑(TauCeti.ContCohomology.dualityMap0 (TauCeti.AbsoluteGaloisGroup K)
          (TauCeti.DiscreteCoind (TauCeti.AbsoluteGaloisGroup K) V A) (TauCeti.KummerCoeff K n)) ∧
    Function.Bijective
        ⇑(TauCeti.ContCohomology.dualityMap1 (TauCeti.AbsoluteGaloisGroup K)
            (TauCeti.DiscreteCoind (TauCeti.AbsoluteGaloisGroup K) V A) (TauCeti.KummerCoeff K n)) ∧
      Function.Bijective
        ⇑(TauCeti.ContCohomology.dualityMap2 (TauCeti.AbsoluteGaloisGroup K)
            (TauCeti.DiscreteCoind (TauCeti.AbsoluteGaloisGroup K) V A) (TauCeti.KummerCoeff K n))
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.html#TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self)
- [Source of `TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self` in TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.lean#L131)

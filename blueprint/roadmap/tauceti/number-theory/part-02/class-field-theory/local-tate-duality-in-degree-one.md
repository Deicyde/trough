---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.dualityMap1_kummerCoeff_bijective, TauCeti.ClassFieldTheory.tateDualityPairing_flip_perfect, TauCeti.ClassFieldTheory.dualityMap2_kummerCoeff_bijective, TauCeti.ClassFieldTheory.dualityMap0_kummerCoeff_bijective
statement: formalized
proof: formalized
---

# Local Tate duality in degree one

Let `K` be a nonarchimedean local field and `n` a natural
number invertible in `K`. For every finite discrete `G_K`-module `A` killed by `n`, Tate's duality
map `H¹(G_K, A) → Hom(H¹(G_K, Hom(A, μₙ)), H²(G_K, μₙ))` is bijective.

```lean
TauCeti.ClassFieldTheory.dualityMap1_kummerCoeff_bijective {K : Type} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} (hn : IsUnit ↑n) (A : Type)
  [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A]
  [DistribMulAction (TauCeti.AbsoluteGaloisGroup K) A]
  [ContinuousSMul (TauCeti.AbsoluteGaloisGroup K) A] [Finite A] (hA : ∀ (a : A), n • a = 0) :
  Function.Bijective
    ⇑(TauCeti.ContCohomology.dualityMap1 (TauCeti.AbsoluteGaloisGroup K) A
        (TauCeti.KummerCoeff K n))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](../../part-01/class-field-theory/the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [Tate's duality map `α₀` on a module with trivial action](../../../representation-theory/homological/tates-duality-map-0-on-a-module-with-trivial-act.md)
- [Tate's duality on an open subgroup acting trivially on `μₙ`](tates-duality-on-an-open-subgroup-acting-trivial.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap1_kummerCoeff_bijective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.html#TauCeti.ClassFieldTheory.dualityMap1_kummerCoeff_bijective).

## Other forms

**Local Tate duality for the named evaluation pairing.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.tateDualityPairing_flip_perfect`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/Perfect.html#TauCeti.ClassFieldTheory.tateDualityPairing_flip_perfect).

```lean
TauCeti.ClassFieldTheory.tateDualityPairing_flip_perfect {n : ℕ} {F : Type} [Field F]
  [ValuativeRel F] [TopologicalSpace F] [IsNonarchimedeanLocalField F] (hn : IsUnit ↑n)
  (A : TauCeti.ClassFieldTheory.GalRep n F) [DiscreteTopology ↑A] [Finite ↑A]
  [Fact (TauCeti.IsSmoothDiscrete (ZMod n) A)]
  (tr : ↑(continuousCohomology 2 (TauCeti.ClassFieldTheory.muNRep n F)).toModuleCat ≃+ ZMod n)
  (i j : ℕ) (hij : i + j = 2) :
  (∀ (y : ↑(continuousCohomology j A).toModuleCat),
      (∀ (x : ↑(continuousCohomology i (TauCeti.ClassFieldTheory.tateDual A)).toModuleCat),
          TauCeti.ClassFieldTheory.tateDualityPairing A tr i j hij x y = 0) →
        y = 0) ∧
    ∀ (ψ : ↑(continuousCohomology i (TauCeti.ClassFieldTheory.tateDual A)).toModuleCat →+ ZMod n),
      ∃ y,
        ∀ (x : ↑(continuousCohomology i (TauCeti.ClassFieldTheory.tateDual A)).toModuleCat),
          TauCeti.ClassFieldTheory.tateDualityPairing A tr i j hij x y = ψ x
```

**Local Tate duality in degree two.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap2_kummerCoeff_bijective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.html#TauCeti.ClassFieldTheory.dualityMap2_kummerCoeff_bijective).

```lean
TauCeti.ClassFieldTheory.dualityMap2_kummerCoeff_bijective {K : Type} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} (hn : IsUnit ↑n) (A : Type)
  [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A]
  [DistribMulAction (TauCeti.AbsoluteGaloisGroup K) A]
  [ContinuousSMul (TauCeti.AbsoluteGaloisGroup K) A] [Finite A] (hA : ∀ (a : A), n • a = 0) :
  Function.Bijective
    ⇑(TauCeti.ContCohomology.dualityMap2 (TauCeti.AbsoluteGaloisGroup K) A
        (TauCeti.KummerCoeff K n))
```

**Local Tate duality in degree zero.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap0_kummerCoeff_bijective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.html#TauCeti.ClassFieldTheory.dualityMap0_kummerCoeff_bijective).

```lean
TauCeti.ClassFieldTheory.dualityMap0_kummerCoeff_bijective {K : Type} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} (hn : IsUnit ↑n) (A : Type)
  [AddCommGroup A] [TopologicalSpace A] [DiscreteTopology A]
  [DistribMulAction (TauCeti.AbsoluteGaloisGroup K) A]
  [ContinuousSMul (TauCeti.AbsoluteGaloisGroup K) A] [Finite A] (hA : ∀ (a : A), n • a = 0) :
  Function.Bijective
    ⇑(TauCeti.ContCohomology.dualityMap0 (TauCeti.AbsoluteGaloisGroup K) A
        (TauCeti.KummerCoeff K n))
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.dualityMap1_kummerCoeff_bijective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.html#TauCeti.ClassFieldTheory.dualityMap1_kummerCoeff_bijective)
- [Source of `TauCeti.ClassFieldTheory.dualityMap1_kummerCoeff_bijective` in TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.lean#L258)

---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self, TauCeti.ClassFieldTheory.dualityMap0_zmod_bijective_of_isPrimitiveRoot, TauCeti.ClassFieldTheory.dualityMap0_bijective_of_isPrimitiveRoot, TauCeti.ClassFieldTheory.dualityMap1_zmod_bijective_of_isPrimitiveRoot, TauCeti.ClassFieldTheory.dualityMap1_bijective_of_isPrimitiveRoot, TauCeti.ClassFieldTheory.dualityMap2_bijective_of_isPrimitiveRoot, TauCeti.ClassFieldTheory.dualityMap_bijective_discreteCoind_kummerCoeff
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
- [Dedekind's different theorem, the tame case](../local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../../part-01/counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](../../part-01/class-field-theory/the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [Tate's duality map `α₀` on a module with trivial action](../../../representation-theory/homological/tates-duality-map-0-on-a-module-with-trivial-act.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/FiniteModule.html#TauCeti.ClassFieldTheory.dualityMap_bijective_of_smul_kummerCoeff_eq_self).

## Other forms

**Tate's duality map `α₀` at the trivial module `ℤ/n` is bijective for a topological group `H` isomorphic to `G_K`, when the local field `K` contains a primitive `n`th root of unity.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap0_zmod_bijective_of_isPrimitiveRoot`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/TrivialZMod.html#TauCeti.ClassFieldTheory.dualityMap0_zmod_bijective_of_isPrimitiveRoot).

```lean
TauCeti.ClassFieldTheory.dualityMap0_zmod_bijective_of_isPrimitiveRoot {K : Type} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} [NeZero n] {ζ : K}
  (hζ : IsPrimitiveRoot ζ n) {H : Type} [Group H] [TopologicalSpace H] [IsTopologicalGroup H]
  (φ : TauCeti.AbsoluteGaloisGroup K ≃ₜ* H) [DistribMulAction H (ZMod n)]
  (htriv : ∀ (h : H) (m : ZMod n), h • m = m) (x✝ : ContinuousSMul H (ZMod n) := ⋯) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 H (ZMod n) (ZMod n))
```

**Tate's duality map `α₀` on a finite module with trivial action is bijective for a topological group `H` isomorphic to `G_K`, when the local field `K` contains a primitive `n`th root of unity.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap0_bijective_of_isPrimitiveRoot`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/TrivialZMod.html#TauCeti.ClassFieldTheory.dualityMap0_bijective_of_isPrimitiveRoot).

```lean
TauCeti.ClassFieldTheory.dualityMap0_bijective_of_isPrimitiveRoot.{u_1} {K : Type} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} [NeZero n] {ζ : K}
  (hζ : IsPrimitiveRoot ζ n) {H : Type} [Group H] [TopologicalSpace H] [IsTopologicalGroup H]
  (φ : TauCeti.AbsoluteGaloisGroup K ≃ₜ* H) [DistribMulAction H (ZMod n)]
  (htriv : ∀ (h : H) (m : ZMod n), h • m = m) (A : Type u_1) [AddCommGroup A] [TopologicalSpace A]
  [DiscreteTopology A] [DistribMulAction H A] [Finite A] (hA : ∀ (a : A), n • a = 0)
  (hAtriv : ∀ (h : H) (a : A), h • a = a) (x✝ : ContinuousSMul H (ZMod n) := ⋯)
  (x✝¹ : ContinuousSMul H A := ⋯) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap0 H A (ZMod n))
```

**Tate's duality map `α₁` at the trivial module `ℤ/n` is bijective for a topological group `H` isomorphic to `G_K`, when the local field `K` contains a primitive `n`th root of unity.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap1_zmod_bijective_of_isPrimitiveRoot`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/TrivialZMod.html#TauCeti.ClassFieldTheory.dualityMap1_zmod_bijective_of_isPrimitiveRoot).

```lean
TauCeti.ClassFieldTheory.dualityMap1_zmod_bijective_of_isPrimitiveRoot {K : Type} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} [NeZero n] {ζ : K}
  (hζ : IsPrimitiveRoot ζ n) {H : Type} [Group H] [TopologicalSpace H] [IsTopologicalGroup H]
  (φ : TauCeti.AbsoluteGaloisGroup K ≃ₜ* H) [DistribMulAction H (ZMod n)]
  (htriv : ∀ (h : H) (m : ZMod n), h • m = m) (x✝ : ContinuousSMul H (ZMod n) := ⋯) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 H (ZMod n) (ZMod n))
```

**Tate's duality map `α₁` on a finite module with trivial action is bijective for a topological group `H` isomorphic to `G_K`, when the local field `K` contains a primitive `n`th root of unity.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap1_bijective_of_isPrimitiveRoot`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/TrivialZMod.html#TauCeti.ClassFieldTheory.dualityMap1_bijective_of_isPrimitiveRoot).

```lean
TauCeti.ClassFieldTheory.dualityMap1_bijective_of_isPrimitiveRoot.{u_1} {K : Type} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} [NeZero n] {ζ : K}
  (hζ : IsPrimitiveRoot ζ n) {H : Type} [Group H] [TopologicalSpace H] [IsTopologicalGroup H]
  (φ : TauCeti.AbsoluteGaloisGroup K ≃ₜ* H) [DistribMulAction H (ZMod n)]
  (htriv : ∀ (h : H) (m : ZMod n), h • m = m) (A : Type u_1) [AddCommGroup A] [TopologicalSpace A]
  [DiscreteTopology A] [DistribMulAction H A] [Finite A] (hA : ∀ (a : A), n • a = 0)
  (hAtriv : ∀ (h : H) (a : A), h • a = a) (x✝ : ContinuousSMul H (ZMod n) := ⋯)
  (x✝¹ : ContinuousSMul H A := ⋯) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap1 H A (ZMod n))
```

**Tate's duality map `α₂` on a finite module with trivial action is bijective for a topological group `H` isomorphic to `G_K`, when the local field `K` contains a primitive `n`th root of unity.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.dualityMap2_bijective_of_isPrimitiveRoot`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/Duality/TrivialZMod.html#TauCeti.ClassFieldTheory.dualityMap2_bijective_of_isPrimitiveRoot).

```lean
TauCeti.ClassFieldTheory.dualityMap2_bijective_of_isPrimitiveRoot.{u_1} {K : Type} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} [NeZero n] {ζ : K}
  (hζ : IsPrimitiveRoot ζ n) {H : Type} [Group H] [TopologicalSpace H] [IsTopologicalGroup H]
  (φ : TauCeti.AbsoluteGaloisGroup K ≃ₜ* H) [DistribMulAction H (ZMod n)]
  (htriv : ∀ (h : H) (m : ZMod n), h • m = m) (A : Type u_1) [AddCommGroup A] [TopologicalSpace A]
  [DiscreteTopology A] [DistribMulAction H A] [Finite A] (hA : ∀ (a : A), n • a = 0)
  (hAtriv : ∀ (h : H) (a : A), h • a = a) (x✝ : ContinuousSMul H (ZMod n) := ⋯)
  (x✝¹ : ContinuousSMul H A := ⋯) :
  Function.Bijective ⇑(TauCeti.ContCohomology.dualityMap2 H A (ZMod n))
```

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

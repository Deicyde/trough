---
declaration: section
origin: cited
lean: StrongGeneration.comp_eq_zero_of_mem_triangEnvelopeIter, StrongGeneration.isRegularRing_and_ringKrullDim_ne_top_of_isStrongGenerator, StrongGeneration.subsingleton_hom_of_isGE_of_isLE, StrongGeneration.iso_biproduct_truncations_of_cohomology_isZero, StrongGeneration.exists_triangEnvelopeIter_eq_isPerfect_of_isRegularRing, StrongGeneration.isRegularRing_and_ringKrullDim_ne_top_iff_hasStrongGenerator_iff_regularModule
statement: formalized
proof: formalized
---

# 15.81 Strong generators and regular rings

Section 15.81 of the Stacks Project, [Tag 0FXG](https://stacks.math.columbia.edu/tag/0FXG). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FXH, a lemma

[Tag 0FXH](https://stacks.math.columbia.edu/tag/0FXH) in the Stacks Project.

**`StrongGeneration.comp_eq_zero_of_mem_triangEnvelopeIter`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean#L406).

> **Stacks 0FXH**.
> If `K` belongs to `⟨R⟩ₙ` in the derived category of a ring and a chain of `n` morphisms beginning
> at `K` induces the zero map on cohomology in every degree, then the composite of the chain is
> zero.

```lean
theorem comp_eq_zero_of_mem_triangEnvelopeIter
    {R : Type u} [Ring R] (n : ℕ) (hn : 0 < n)
    (F : ComposableArrows (DerivedCategory (ModuleCat.{u} R)) n)
    (hFleft :
      ObjectProperty.triangEnvelopeIter
        (ObjectProperty.singleton
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R)))
        (n - 1) F.left)
    (hF : ∀ (i : ℕ) (_ : i < n) (j : ℤ),
      (DerivedCategory.homologyFunctor (ModuleCat.{u} R) j).map (F.map' i (i + 1)) = 0) :
    F.hom = 0
```

## Tag 0FXI, a lemma

[Tag 0FXI](https://stacks.math.columbia.edu/tag/0FXI) in the Stacks Project.

**`StrongGeneration.isRegularRing_and_ringKrullDim_ne_top_of_isStrongGenerator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean, line 629](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean#L629).

> **Stacks 0FXI**.
> A Noetherian ring for which `R` strongly generates its perfect derived category — that is, for
> which a single stage `⟨R⟩ₙ` already exhausts `⟨R⟩` — is regular and has finite Krull dimension.

```lean
theorem isRegularRing_and_ringKrullDim_ne_top_of_isStrongGenerator
    {R : Type u} [CommRing R] [IsNoetherianRing R]
    (h : ∃ n : ℕ,
      ObjectProperty.triangEnvelopeIter
        (ObjectProperty.singleton
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))) n =
      ObjectProperty.triangEnvelope
        (ObjectProperty.singleton
          ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R)))) :
    IsRegularRing R ∧ ringKrullDim R ≠ ⊤
```

## Tag 0FXJ, a lemma

[Tag 0FXJ](https://stacks.math.columbia.edu/tag/0FXJ) in the Stacks Project.

**`StrongGeneration.subsingleton_hom_of_isGE_of_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean, line 861](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean#L861).

> **Stacks 0FXJ**.
> Let `R` be a regular Noetherian ring of finite dimension `d`. If `K` and `L` are bounded-above
> derived `R`-modules, the cohomology of `K` vanishes in degrees at most `k`, and the cohomology of
> `L` vanishes in degrees at least `k - d + 1`, then every morphism from `K` to `L` is zero.

```lean
theorem subsingleton_hom_of_isGE_of_isLE [IsRegularRing R]
    (d : ℕ) (hdim : ringKrullDim R = d)
    (K L : DerivedCategory.Minus (ModuleCat.{u} R)) (k : ℤ)
    (hK : K.obj.IsGE (k + 1)) (hL : L.obj.IsLE (k - d)) :
    Subsingleton (K.obj ⟶ L.obj)
```

## Tag 0FXK, a lemma

[Tag 0FXK](https://stacks.math.columbia.edu/tag/0FXK) in the Stacks Project.

**`StrongGeneration.iso_biproduct_truncations_of_cohomology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean, line 879](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean#L879).

> **Stacks 0FXK**.
> Let `R` be a regular Noetherian ring of finite positive dimension `d`. If a perfect derived
> `R`-module `K` has zero cohomology in every degree from `k - d + 2` through `k`, then `K` is
> isomorphic to the biproduct of its truncations in degrees at most `k - d + 1` and at least
> `k + 1`.

```lean
theorem iso_biproduct_truncations_of_cohomology_isZero [IsRegularRing R]
    (d : ℕ) (hdim : ringKrullDim R = d) (hd : 1 ≤ d)
    (K : DerivedCategory (ModuleCat.{u} R)) (hKperfect : StacksDraft.Perfect.IsPerfect K) (k : ℤ)
    (hK : ∀ i : ℤ, k - d + 2 ≤ i → i ≤ k →
      IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{u} R) i).obj K)) :
    Nonempty
      (K ≅
        (DerivedCategory.TStructure.t.truncLE (k - d + 1)).obj K ⊞
          (DerivedCategory.TStructure.t.truncGE (k + 1)).obj K)
```

## Tag 0FXL, a lemma

[Tag 0FXL](https://stacks.math.columbia.edu/tag/0FXL) in the Stacks Project.

**`StrongGeneration.exists_triangEnvelopeIter_eq_isPerfect_of_isRegularRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean, line 1268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean#L1268).

> **Stacks 0FXL**.
> Over a regular ring of finite Krull dimension, the regular module placed in degree zero is a strong
> generator of the perfect derived category: a single stage `⟨R⟩ₙ` of the triangulated envelope of
> `R[0]` already contains every perfect complex. One may take for `n` the global dimension of `R`.

```lean
theorem exists_triangEnvelopeIter_eq_isPerfect_of_isRegularRing
    {R : Type u} [CommRing R] [IsRegularRing R] (hdim : ringKrullDim R ≠ ⊤) :
    ∃ n : ℕ,
      ObjectProperty.triangEnvelopeIter
          (ObjectProperty.singleton
            ((DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R))) n =
        (StacksDraft.Perfect.IsPerfect :
          ObjectProperty (DerivedCategory (ModuleCat.{u} R)))
```

## Tag 0FXM, a proposition

[Tag 0FXM](https://stacks.math.columbia.edu/tag/0FXM) in the Stacks Project.

**`StrongGeneration.isRegularRing_and_ringKrullDim_ne_top_iff_hasStrongGenerator_iff_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean, line 1298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/DerivedCategory/StrongGenerator.lean#L1298).

> **Stacks 0FXM**.
> For a Noetherian ring `R` the following are equivalent: `R` is regular of finite Krull dimension;
> the perfect derived category of `R` admits a strong generator; and the regular module placed in
> degree zero is such a strong generator. The implication from an arbitrary strong generator to the
> regular module uses that any object of the perfect derived category already lies in some finite
> stage of the envelope of `R[0]`, so the stages of its own envelope are absorbed into those of
> `R[0]`.

```lean
theorem isRegularRing_and_ringKrullDim_ne_top_iff_hasStrongGenerator_iff_regularModule
    {R : Type u} [CommRing R] [IsNoetherianRing R] :
    let D := DerivedCategory (ModuleCat.{u} R)
    let perfect := (StacksDraft.Perfect.IsPerfect : ObjectProperty D)
    let regularModule :=
      (DerivedCategory.singleFunctor (ModuleCat.{u} R) 0).obj (ModuleCat.of R R)
    let regularFinite := IsRegularRing R ∧ ringKrullDim R ≠ ⊤
    let hasStrongGenerator := ∃ E : D, ∃ n : ℕ,
      ObjectProperty.triangEnvelopeIter (ObjectProperty.singleton E) n = perfect
    let regularModuleIsStrongGenerator := ∃ n : ℕ,
      ObjectProperty.triangEnvelopeIter (ObjectProperty.singleton regularModule) n = perfect
    (regularFinite ↔ hasStrongGenerator) ∧
      (hasStrongGenerator ↔ regularModuleIsStrongGenerator)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.81, Tag 0FXG](https://stacks.math.columbia.edu/tag/0FXG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

---
declaration: section
origin: cited
lean: StacksDraft.ProjectiveAmplitude.hom_eq_zero_and_existsUnique_iso_biprod, StacksDraft.Perfect.exists_localization_perfect_truncGE_and_iso_biprod, StacksDraft.Perfect.exists_localization_finite_free_homology_and_iso_biprod, StacksDraft.Perfect.exists_localization_iso_biprod_truncGE_truncLE, StacksDraft.ProjectiveAmplitude.existsUnique_iso_biprod_truncations_of_ext_map_injective, StacksDraft.ProjectiveAmplitude.existsUnique_iso_biprod_truncations_of_ext_vanishing
statement: formalized
proof: formalized
---

# 15.78 Splitting complexes

Section 15.78 of the Stacks Project, [Tag 0BCF](https://stacks.math.columbia.edu/tag/0BCF). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BCG, a lemma

[Tag 0BCG](https://stacks.math.columbia.edu/tag/0BCG) in the Stacks Project.

**`StacksDraft.ProjectiveAmplitude.hom_eq_zero_and_existsUnique_iso_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/ProjectiveAmplitude.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/ProjectiveAmplitude.lean#L181).

> **Stacks 0BCG.** If `L` has projective amplitude in `[a, b]`, then every morphism from `L` to
> an object whose cohomology vanishes in all degrees `≥ a` is zero. A distinguished triangle
> `K ⟶ M ⟶ L ⟶ K⟦1⟧` has a splitting `M ≅ K ⊞ L` compatible with its maps as soon as the
> cohomology of `K` vanishes in all degrees `≥ a + 1`; if it vanishes in all degrees `≥ a`, that
> compatible splitting is moreover unique.

```lean
theorem hom_eq_zero_and_existsUnique_iso_biprod
    {R : Type u} [Ring R] (K L : DerivedCategory (ModuleCat.{v} R)) (a b : ℤ)
    (hL : HasProjectiveAmplitude L a b) :
    ((∀ i : ℤ, a ≤ i → IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) →
        ∀ f : L ⟶ K, f = 0) ∧
      ((∀ i : ℤ, a + 1 ≤ i →
          IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) →
        ∀ (M : DerivedCategory (ModuleCat.{v} R)) (f : K ⟶ M) (g : M ⟶ L)
          (h : L ⟶ K⟦(1 : ℤ)⟧),
          Triangle.mk f g h ∈ distTriang _ →
            ∃ e : M ≅ K ⊞ L, f ≫ e.hom = biprod.inl ∧ g = e.hom ≫ biprod.snd) ∧
      ((∀ i : ℤ, a ≤ i → IsZero ((DerivedCategory.homologyFunctor (ModuleCat.{v} R) i).obj K)) →
        ∀ (M : DerivedCategory (ModuleCat.{v} R)) (f : K ⟶ M) (g : M ⟶ L)
          (h : L ⟶ K⟦(1 : ℤ)⟧),
          Triangle.mk f g h ∈ distTriang _ →
            ∃! e : M ≅ K ⊞ L, f ≫ e.hom = biprod.inl ∧ g = e.hom ≫ biprod.snd)
```

## Tag 0A1U, a lemma

[Tag 0A1U](https://stacks.math.columbia.edu/tag/0A1U) in the Stacks Project.

**`StacksDraft.Perfect.exists_localization_perfect_truncGE_and_iso_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/FibreCriterion/BaseChangeSurjective.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/FibreCriterion/BaseChangeSurjective.lean#L328).

> Let `R` be a ring, `p ⊂ R` a prime and `K` a pseudo-coherent object of
> `D(R)`. If for some `i ∈ ℤ` the map `H^i(K) ⊗_R κ(p) → H^i(K ⊗_R^L κ(p))` is surjective, then
> there is `f ∈ R`, `f ∉ p`, such that `τ_{≥ i+1}(K ⊗_R R_f)` is a perfect object of `D(R_f)` with
> Tor amplitude in `[i + 1, ∞]`, together with a canonical isomorphism
> `K ⊗_R R_f ≅ τ_{≤ i}(K ⊗_R R_f) ⊕ τ_{≥ i+1}(K ⊗_R R_f)` in `D(R_f)`.

```lean
theorem exists_localization_perfect_truncGE_and_iso_biprod
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    (K : DerivedCategory (ModuleCat.{max u v} R))
    (_hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) (i : ℤ)
    (hbase : CohomologyBaseChangeSurjective.{u, v} p K i) :
    ∃ f : R, f ∉ p ∧
      let Kf := (PseudoCoherence.localizationAwayFunctorAux.{u, v} f).obj K
      let upper := (DerivedCategory.TStructure.t.truncGE (i + 1)).obj Kf
      let lower := (DerivedCategory.TStructure.t.truncLE i).obj Kf
      IsPerfect upper ∧
        (∃ (P : CochainComplex (ModuleCat.{max u v} (Localization.Away f)) ℤ) (b : ℤ),
          P.IsStrictlyGE (i + 1) ∧ P.IsStrictlyLE b ∧
            (∀ j : ℤ, Module.Finite (Localization.Away f) (P.X j)) ∧
            (∀ j : ℤ, Module.Projective (Localization.Away f) (P.X j)) ∧
            Nonempty (upper ≅ DerivedCategory.Q.obj P) ∧
            ∀ (M : ModuleCat.{max u v} (Localization.Away f)) (j : ℤ), j < i + 1 →
              IsZero ((TorAmplitude.tensorComplex P M).homology j)) ∧
        ∃! e : Kf ≅ lower ⊞ upper,
          (DerivedCategory.TStructure.t.truncLEι i).app Kf ≫ e.hom = biprod.inl ∧
            (DerivedCategory.TStructure.t.truncGEπ (i + 1)).app Kf = e.hom ≫ biprod.snd
```

## Tag 0A1V, a lemma

[Tag 0A1V](https://stacks.math.columbia.edu/tag/0A1V) in the Stacks Project.

**`StacksDraft.Perfect.exists_localization_finite_free_homology_and_iso_biprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/FibreCriterion/ThreeTermSplitting.lean, line 615](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/FibreCriterion/ThreeTermSplitting.lean#L615).

> Let `R` be a ring, `p ⊂ R` a prime and `K` a pseudo-coherent object of
> `D(R)`. If for some `i ∈ ℤ` both maps `H^i(K) ⊗_R κ(p) → H^i(K ⊗_R^L κ(p))` and
> `H^{i-1}(K) ⊗_R κ(p) → H^{i-1}(K ⊗_R^L κ(p))` are surjective, then there is `f ∈ R`, `f ∉ p`,
> such that
>
> 1. `τ_{≥ i+1}(K ⊗_R R_f)` is a perfect object of `D(R_f)` with Tor amplitude in `[i + 1, ∞]`,
> 2. `H^i(K)_f` is a finite free `R_f`-module, and
> 3. there is a canonical direct sum decomposition
>    `K ⊗_R R_f ≅ τ_{≤ i-1}(K ⊗_R R_f) ⊕ H^i(K)_f[-i] ⊕ τ_{≥ i+1}(K ⊗_R R_f)` in `D(R_f)`.

```lean
theorem exists_localization_finite_free_homology_and_iso_biprod
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    (K : DerivedCategory (ModuleCat.{max u v} R))
    (hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) (i : ℤ)
    (hbase_i : CohomologyBaseChangeSurjective.{u, v} p K i)
    (hbase_prev : CohomologyBaseChangeSurjective.{u, v} p K (i - 1)) :
    ∃ f : R, f ∉ p ∧
      let Rf := Localization.Away f
      let Kf := (PseudoCoherence.localizationAwayFunctorAux.{u, v} f).obj K
      let upper := (DerivedCategory.TStructure.t.truncGE (i + 1)).obj Kf
      let lower := (DerivedCategory.TStructure.t.truncLE (i - 1)).obj Kf
      let HiLocalized :=
        (ModuleCat.extendScalars (algebraMap R Rf)).obj
          ((DerivedCategory.homologyFunctor (ModuleCat.{max u v} R) i).obj K)
      let middle :=
        (DerivedCategory.singleFunctor (ModuleCat.{max u v} Rf) i).obj HiLocalized
      let comparison := (localizationAwayHomologyFunctorIso.{u, v} f i).app K
      IsPerfect upper ∧
        (∃ (P : CochainComplex (ModuleCat.{max u v} Rf) ℤ) (b : ℤ),
          P.IsStrictlyGE (i + 1) ∧ P.IsStrictlyLE b ∧
            (∀ j : ℤ, Module.Finite Rf (P.X j)) ∧
            (∀ j : ℤ, Module.Projective Rf (P.X j)) ∧
            Nonempty (upper ≅ DerivedCategory.Q.obj P) ∧
            ∀ (M : ModuleCat.{max u v} Rf) (j : ℤ), j < i + 1 →
              IsZero ((TorAmplitude.tensorComplex P M).homology j)) ∧
        Module.Finite Rf HiLocalized ∧ Module.Free Rf HiLocalized ∧
        ∃! e : Kf ≅ (lower ⊞ middle) ⊞ upper,
          (DerivedCategory.TStructure.t.truncLEι (i - 1)).app Kf ≫ e.hom =
              biprod.inl ≫ biprod.inl ∧
            (DerivedCategory.TStructure.t.truncGEπ (i + 1)).app Kf =
              e.hom ≫ biprod.snd ∧
            (DerivedCategory.homologyFunctor (ModuleCat.{max u v} Rf) i).map e.hom ≫
                (DerivedCategory.homologyFunctor (ModuleCat.{max u v} Rf) i).map biprod.fst ≫
                (DerivedCategory.homologyFunctor (ModuleCat.{max u v} Rf) i).map biprod.snd ≫
                (DerivedCategory.singleFunctorCompHomologyFunctorIso
                  (ModuleCat.{max u v} Rf) i).hom.app HiLocalized = comparison.hom
```

## Tag 068U, a lemma

[Tag 068U](https://stacks.math.columbia.edu/tag/068U) in the Stacks Project.

**`StacksDraft.Perfect.exists_localization_iso_biprod_truncGE_truncLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/FibreCriterion/FibreCohomologyVanishing.lean, line 707](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/FibreCriterion/FibreCohomologyVanishing.lean#L707).

> Let `R` be a ring, `p ⊂ R` a prime, `i ∈ ℤ` and let `K` be a pseudo-coherent
> object of `D(R)` with `H^i(K ⊗_R^L κ(p)) = 0`. Then there is `f ∈ R`, `f ∉ p`, and a canonical
> direct sum decomposition
> `K ⊗_R R_f = τ_{≥ i+1}(K ⊗_R R_f) ⊕ τ_{≤ i-1}(K ⊗_R R_f)` in `D(R_f)`, in which
> `τ_{≥ i+1}(K ⊗_R R_f)` is a perfect complex with Tor amplitude in `[i + 1, ∞]`.

```lean
theorem exists_localization_iso_biprod_truncGE_truncLE
    {R : Type u} [CommRing R] (p : Ideal R) [p.IsPrime]
    (K : DerivedCategory (ModuleCat.{max u v} R))
    (_hK : StacksDraft.PseudoCoherence.IsPseudoCoherent K) (i : ℤ)
    (hfibre : FibreCohomologyVanishes.{u, v} p K i) :
    ∃ f : R, f ∉ p ∧
      let Kf := (PseudoCoherence.localizationAwayFunctorAux.{u, v} f).obj K
      let upper := (DerivedCategory.TStructure.t.truncGE (i + 1)).obj Kf
      let lower := (DerivedCategory.TStructure.t.truncLE (i - 1)).obj Kf
      IsPerfect upper ∧
        (∃ (P : CochainComplex (ModuleCat.{max u v} (Localization.Away f)) ℤ) (b : ℤ),
          P.IsStrictlyGE (i + 1) ∧ P.IsStrictlyLE b ∧
            (∀ j : ℤ, Module.Finite (Localization.Away f) (P.X j)) ∧
            (∀ j : ℤ, Module.Projective (Localization.Away f) (P.X j)) ∧
            Nonempty (upper ≅ DerivedCategory.Q.obj P) ∧
            ∀ (M : ModuleCat.{max u v} (Localization.Away f)) (j : ℤ), j < i + 1 →
              IsZero ((TorAmplitude.tensorComplex P M).homology j)) ∧
        ∃! e : Kf ≅ upper ⊞ lower,
          (DerivedCategory.TStructure.t.truncGEπ (i + 1)).app Kf = e.hom ≫ biprod.fst ∧
            (DerivedCategory.TStructure.t.truncLEι (i - 1)).app Kf ≫ e.hom = biprod.inr
```

## Tag 0G97, a lemma

[Tag 0G97](https://stacks.math.columbia.edu/tag/0G97) in the Stacks Project.

**`StacksDraft.ProjectiveAmplitude.existsUnique_iso_biprod_truncations_of_ext_map_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/ProjectiveAmplitude.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/ProjectiveAmplitude.lean#L294).

> **Stacks 0G97.** Let `K` be a bounded above object of `D(R)` and let `a` be an integer.
> Assume that for every injective `R`-module map `M ⟶ M'` the induced map
> `Ext^{-a}(K, M) ⟶ Ext^{-a}(K, M')` is injective. Then `τ_{≥ a + 1}K` has projective amplitude in
> `[a + 1, b]` for some `b`, and there is a *unique* direct sum decomposition
> `K ≅ τ_{≤ a}K ⊞ τ_{≥ a + 1}K` compatible with the two canonical truncation maps.

```lean
theorem existsUnique_iso_biprod_truncations_of_ext_map_injective
    {R : Type u} [Ring R] (K : DerivedCategory (ModuleCat.{max u v} R)) (a : ℤ)
    (hK : ∃ n : ℤ, K.IsLE n)
    (hExt : ∀ (M M' : ModuleCat.{max u v} R) (f : M ⟶ M'), Mono f →
      Function.Injective (fun x : DerivedCategory.Ext K
          ((DerivedCategory.singleFunctor (ModuleCat.{max u v} R) 0).obj M) (-a) ↦
        x.comp (ShiftedHom.mk₀ 0 rfl
          ((DerivedCategory.singleFunctor (ModuleCat.{max u v} R) 0).map f)) (zero_add _))) :
    ∃ b : ℤ,
      HasProjectiveAmplitude
          ((DerivedCategory.TStructure.t.truncGE (a + 1)).obj K) (a + 1) b ∧
        ∃! e : K ≅
            ((DerivedCategory.TStructure.t.truncLE a).obj K ⊞
              (DerivedCategory.TStructure.t.truncGE (a + 1)).obj K),
          (DerivedCategory.TStructure.t.truncLEι a).app K ≫ e.hom = biprod.inl ∧
            (DerivedCategory.TStructure.t.truncGEπ (a + 1)).app K =
              e.hom ≫ biprod.snd
```

## Tag 0G98, a lemma

[Tag 0G98](https://stacks.math.columbia.edu/tag/0G98) in the Stacks Project.

**`StacksDraft.ProjectiveAmplitude.existsUnique_iso_biprod_truncations_of_ext_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Perfect/ProjectiveAmplitude.lean, line 401](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Perfect/ProjectiveAmplitude.lean#L401).

> **Stacks 0G98.** Let `K` be a bounded above object of `D(R)` and let `a` be an integer.
> Assume `Ext^{-a}(K, M) = 0` for every `R`-module `M`. Then `τ_{≥ a + 1}K` has projective
> amplitude in `[a + 1, b]` for some `b`, and there is a *unique* direct sum decomposition
> `K ≅ τ_{≤ a - 1}K ⊞ τ_{≥ a + 1}K` compatible with the two canonical truncation maps.

```lean
theorem existsUnique_iso_biprod_truncations_of_ext_vanishing
    {R : Type u} [Ring R] (K : DerivedCategory (ModuleCat.{max u v} R)) (a : ℤ)
    (hK : ∃ n : ℤ, K.IsLE n)
    (hExt : ∀ M : ModuleCat.{max u v} R,
      Subsingleton (DerivedCategory.Ext K
        ((DerivedCategory.singleFunctor (ModuleCat.{max u v} R) 0).obj M) (-a))) :
    ∃ b : ℤ,
      HasProjectiveAmplitude
          ((DerivedCategory.TStructure.t.truncGE (a + 1)).obj K) (a + 1) b ∧
        ∃! e : K ≅
            ((DerivedCategory.TStructure.t.truncLE (a - 1)).obj K ⊞
              (DerivedCategory.TStructure.t.truncGE (a + 1)).obj K),
          (DerivedCategory.TStructure.t.truncLEι (a - 1)).app K ≫ e.hom = biprod.inl ∧
            (DerivedCategory.TStructure.t.truncGEπ (a + 1)).app K =
              e.hom ≫ biprod.snd
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.78, Tag 0BCF](https://stacks.math.columbia.edu/tag/0BCF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

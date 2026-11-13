---
declaration: section
origin: cited
lean: MorphismOfTopoi.pushforward_exactness_implications, isLocallySurjective_sheafPushforwardContinuous_map, sheafPushforwardContinuous_reflectsMonomorphisms_of_isCoverDense, sheafPushforwardContinuous_reflectsEpimorphisms_of_isCoverDense, injective_app_of_injective_sheafPushforwardContinuous_map, isLocallySurjective_of_isLocallySurjective_sheafPushforwardContinuous_map
statement: formalized
proof: formalized
---

# 7.41 Exactness properties of pushforward

Section 7.41 of the Stacks Project, [Tag 04D5](https://stacks.math.columbia.edu/tag/04D5). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04D6, a lemma

[Tag 04D6](https://stacks.math.columbia.edu/tag/04D6) in the Stacks Project.

**`MorphismOfTopoi.pushforward_exactness_implications`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PushforwardExactness.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/PushforwardExactness.lean#L65).

> **Stacks 04D6.** Let `f : Sh(C) → Sh(D)` be a morphism of topoi, with pushforward
> `f_* = f.pushforward`, inverse image `f⁻¹ = f.inverseImage` and counit
> `ε : f⁻¹ f_* F ⟶ F`. Consider the properties (on sheaves of sets, where surjections,
> injections and bijections are the epimorphisms, monomorphisms and isomorphisms)
>
> 1. `f_*` is faithful;
> 2. `f_*` is fully faithful;
> 3. `ε : f⁻¹ f_* F ⟶ F` is surjective for all `F`;
> 4. `f_*` transforms surjections into surjections;
> 5. `f_*` commutes with coequalizers;
> 6. `f_*` commutes with pushouts;
> 7. `ε : f⁻¹ f_* F ⟶ F` is an isomorphism for all `F`;
> 8. `f_*` reflects injections;
> 9. `f_*` reflects surjections;
> 10. `f_*` reflects bijections;
> 11. for every surjection `p : F ⟶ f⁻¹ G` there is a surjection `q : G' ⟶ G` such that
>     `f⁻¹ q` factors through `p`.
>
> Then the eight conjuncts below are the implications (a) `(2) ⇒ (1)`, (b) `(3) ⇒ (1)`,
> (c) `(7) ⇒ (1), (2), (3), (8), (9), (10)`, (d) `(3) ⇔ (9)`, (e) `(6) ⇒ (4)` and `(5) ⇒ (4)`,
> (f) `(4) ⇔ (11)`, (g) `(9) ⇒ (8), (10)` and (h) `(2) ⇔ (7)`.
>
> The topos structure enters through balancedness of `Sh(C)` in (g), every epimorphism of
> `Sh(C)` being a coequalizer in (e), and epimorphisms of `Sh(C)` and `Sh(D)` being stable under
> base change in (f).

```lean
theorem pushforward_exactness_implications
    (f : MorphismOfTopoi (Sheaf J (Type max u v)) (Sheaf K (Type max u' v'))) :
    -- (a) (2) ⇒ (1)
    (f.pushforward.Full ∧ f.pushforward.Faithful → f.pushforward.Faithful) ∧
    -- (b) (3) ⇒ (1)
    ((∀ F, Epi (f.adj.counit.app F)) → f.pushforward.Faithful) ∧
    -- (c) (7) ⇒ (1), (2), (3), (8), (9), (10)
    ((∀ F, IsIso (f.adj.counit.app F)) →
      f.pushforward.Faithful ∧ (f.pushforward.Full ∧ f.pushforward.Faithful) ∧
      (∀ F, Epi (f.adj.counit.app F)) ∧ f.pushforward.ReflectsMonomorphisms ∧
      f.pushforward.ReflectsEpimorphisms ∧ f.pushforward.ReflectsIsomorphisms) ∧
    -- (d) (3) ⇔ (9)
    ((∀ F, Epi (f.adj.counit.app F)) ↔ f.pushforward.ReflectsEpimorphisms) ∧
    -- (e) (6) ⇒ (4) and (5) ⇒ (4)
    ((PreservesColimitsOfShape WalkingSpan f.pushforward → f.pushforward.PreservesEpimorphisms) ∧
      (PreservesColimitsOfShape WalkingParallelPair f.pushforward →
        f.pushforward.PreservesEpimorphisms)) ∧
    -- (f) (4) ⇔ (11)
    (f.pushforward.PreservesEpimorphisms ↔
      ∀ (G : Sheaf K (Type max u' v')) (F : Sheaf J (Type max u v))
        (p : F ⟶ f.inverseImage.obj G), Epi p →
        ∃ (G' : Sheaf K (Type max u' v')) (q : G' ⟶ G), Epi q ∧
          ∃ r : f.inverseImage.obj G' ⟶ F, r ≫ p = f.inverseImage.map q) ∧
    -- (g) (9) ⇒ (8), (10)
    (f.pushforward.ReflectsEpimorphisms →
      f.pushforward.ReflectsMonomorphisms ∧ f.pushforward.ReflectsIsomorphisms) ∧
    -- (h) (2) ⇔ (7)
    (f.pushforward.Full ∧ f.pushforward.Faithful ↔ ∀ F, IsIso (f.adj.counit.app F))
```

## Tag 04D7, a lemma

[Tag 04D7](https://stacks.math.columbia.edu/tag/04D7) in the Stacks Project.

**`isLocallySurjective_sheafPushforwardContinuous_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PreservesEpiFactorization.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/PreservesEpiFactorization.lean#L142). The attribute's comment: “Stated for a continuous functor `u`; the exactness of `u_s` making it a morphism of sites is not used. Coverings are families generating a covering sieve, and surjective maps of sheaves are the locally surjective ones.”.

> Let `u : C ⥤ D` be a continuous functor between sites `(C, J)` and
> `(D, K)` (the continuous functor underlying a morphism of sites
> `f : (D, K) → (C, J)`). Assume that for every object `U` of `C` and every
> covering `{V j ⟶ u(U)}` in `D` there is a covering `{W i ⟶ U}` in `C` such
> that `∐ h_{u(W i)}^# → h_{u(U)}^#` factors through `∐ h_{V j}^# → h_{u(U)}^#`
> (`FactorizationCondition`). Then `f_* = u.sheafPushforwardContinuous _ J K`
> transforms surjective maps of sheaves of sets into surjective maps of
> sheaves.

```lean
theorem isLocallySurjective_sheafPushforwardContinuous_map (u : C ⥤ D)
    (J : GrothendieckTopology C) (K : GrothendieckTopology D) [u.IsContinuous J K]
    (h : FactorizationCondition u J K) {F G : Sheaf K (Type (max w₁ w₂))} (a : F ⟶ G)
    [Sheaf.IsLocallySurjective a] :
    Sheaf.IsLocallySurjective ((u.sheafPushforwardContinuous (Type (max w₁ w₂)) J K).map a)
```

## Tag 04D9, a lemma

[Tag 04D9](https://stacks.math.columbia.edu/tag/04D9) in the Stacks Project.

**`sheafPushforwardContinuous_reflectsMonomorphisms_of_isCoverDense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PushforwardEquality.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/PushforwardEquality.lean#L84). The attribute's comment: “f\_* reflects injections (monomorphisms of sheaves)”.

> **Stacks 04D9.** If `u : C ⥤ D` is a continuous functor between sites
> which is also cover dense (i.e. every object of `D` is covered by
> images of objects of `C` under `u`), then the pushforward functor on
> sheaves `f_* : Sheaf K A ⥤ Sheaf J A` reflects monomorphisms. For sheaves of sets these are
> the injections (Stacks 00WN); the componentwise form is
> `injective_app_of_injective_sheafPushforwardContinuous_map`.

```lean
theorem sheafPushforwardContinuous_reflectsMonomorphisms_of_isCoverDense
    [u.IsContinuous J K] [u.IsCoverDense K] :
    (u.sheafPushforwardContinuous A J K).ReflectsMonomorphisms
```

**`sheafPushforwardContinuous_reflectsEpimorphisms_of_isCoverDense`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PushforwardEquality.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/PushforwardEquality.lean#L97). The attribute's comment: “f\_* reflects surjections (epimorphisms of sheaves)”.

> **Stacks 04D9.** If `u : C ⥤ D` is a continuous functor between sites
> which is also cover dense (i.e. every object of `D` is covered by
> images of objects of `C` under `u`), then the pushforward functor on
> sheaves `f_* : Sheaf K A ⥤ Sheaf J A` reflects epimorphisms. For sheaves of sets these are
> the surjections (Stacks 00WN); the local form is
> `isLocallySurjective_of_isLocallySurjective_sheafPushforwardContinuous_map`.

```lean
theorem sheafPushforwardContinuous_reflectsEpimorphisms_of_isCoverDense
    [u.IsContinuous J K] [u.IsCoverDense K] :
    (u.sheafPushforwardContinuous A J K).ReflectsEpimorphisms
```

**`injective_app_of_injective_sheafPushforwardContinuous_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PushforwardReflectsInjSurj.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/PushforwardReflectsInjSurj.lean#L44). The attribute's comment: “f\_* reflects injections, in the sense of Stacks 00WM”.

> **Stacks 04D9, injections.** Let `u : C ⥤ D` be a continuous functor between sites such that
> every object of `D` is covered by images of objects of `C`. If `α : 𝓕 ⟶ 𝓖` is a map of sheaves of
> sets on `D` such that `f_* α` is injective (Stacks 00WM: injective on sections over every object
> of `C`), then `α` is injective on sections over every object of `D`.

```lean
theorem injective_app_of_injective_sheafPushforwardContinuous_map
    [u.IsContinuous J K] [u.IsCoverDense K] {X Y : Sheaf K (Type w)} (α : X ⟶ Y)
    (hα : ∀ U : C, Function.Injective
      (((u.sheafPushforwardContinuous (Type w) J K).map α).hom.app (op U)))
    (V : D) : Function.Injective (α.hom.app (op V))
```

**`isLocallySurjective_of_isLocallySurjective_sheafPushforwardContinuous_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/PushforwardReflectsInjSurj.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/PushforwardReflectsInjSurj.lean#L66). The attribute's comment: “f\_* reflects surjections, in the sense of Stacks 00WM”.

> **Stacks 04D9, surjections.** Let `u : C ⥤ D` be a continuous functor between sites such that
> every object of `D` is covered by images of objects of `C`. If `α : 𝓕 ⟶ 𝓖` is a map of sheaves of
> sets on `D` such that `f_* α` is surjective (Stacks 00WM: every section is locally in the image),
> then `α` is surjective.

```lean
theorem isLocallySurjective_of_isLocallySurjective_sheafPushforwardContinuous_map
    [u.IsContinuous J K] [u.IsCoverDense K] {X Y : Sheaf K (Type w)} (α : X ⟶ Y)
    (hα : Sheaf.IsLocallySurjective ((u.sheafPushforwardContinuous (Type w) J K).map α)) :
    Sheaf.IsLocallySurjective α
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.41, Tag 04D5](https://stacks.math.columbia.edu/tag/04D5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

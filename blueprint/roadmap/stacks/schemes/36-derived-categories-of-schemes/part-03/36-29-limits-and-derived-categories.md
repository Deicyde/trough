---
declaration: section
origin: cited
lean: AlgebraicGeometry.DescentSituation, AlgebraicGeometry.DescentSituation.homProjection_homTransition, AlgebraicGeometry.DescentSituation.homTransition_homTransition, AlgebraicGeometry.DescentSituation.isHomColimit, AlgebraicGeometry.DescentSituation.perfect_isColimit, AlgebraicGeometry.DescentSituation.isPerfect_transition, AlgebraicGeometry.DescentSituation.isPerfect_projection, AlgebraicGeometry.DescentSituation.perfectComparison_coherence
statement: formalized
proof: formalized
---

# 36.29 Limits and derived categories

Section 36.29 of the Stacks Project, [Tag 09RC](https://stacks.math.columbia.edu/tag/09RC). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09RD, a situation

[Tag 09RD](https://stacks.math.columbia.edu/tag/09RD) in the Stacks Project.

**`AlgebraicGeometry.DescentSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/Limits.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/Limits.lean#L41). References: SGA 6 IV (3.2).

> A directed inverse system of quasi-compact and quasi-separated schemes whose transition
> morphisms are affine, equipped with a chosen limit cone and a chosen index.
>
> The index universe `v` is not bounded here, so a large index preorder is admitted, whose
> categorical limit in `Scheme.{u}` need not be the limit of the source's directed set.
> Situation 086P, whose index is a set, is `AlgebraicGeometry.SmallDescentSituation`, which adds
> `Small.{u} I`.

```lean
structure AlgebraicGeometry.DescentSituation (I : Type v) [Preorder I]
    [IsDirected I (· ≤ ·)]
```

## Tag 09RE, a lemma

[Tag 09RE](https://stacks.math.columbia.edu/tag/09RE) in the Stacks Project.

**`AlgebraicGeometry.DescentSituation.homProjection_homTransition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LimitHomDescent.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/LimitHomDescent.lean#L206). The attribute's comment: “the maps to Hom(E, K) are compatible with the transition maps of the directed system, for all E\_0 and K\_0”.

> **The cocone clause of the conclusion of Stacks 09RE.** Pushing a homomorphism from the
> stage `i` to the stage `j` and then to the limit gives the same homomorphism `E ⟶ K` as pushing
> it to the limit directly.
>
> This holds for all `E₀` and `K₀`: it is the coherence of the two comparison
> isomorphisms of derived pullback along the factorisations `f_{ji} ≫ f_{i0} = f_{j0}` and
> `f_j ≫ f_{ji} = f_i`, together with the naturality of the second.

```lean
theorem homProjection_homTransition (i j : D.Stages) (h : i ≤ j)
    (g : stageObj E₀ i ⟶ stageObj K₀ i) :
    homProjection E₀ K₀ j (homTransition E₀ K₀ i j h g) = homProjection E₀ K₀ i g
```

**`AlgebraicGeometry.DescentSituation.homTransition_homTransition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LimitHomDescent.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/LimitHomDescent.lean#L225). The attribute's comment: “the directed system whose colimit the tag takes: its transition maps compose, for all E\_0 and K\_0”.

> **The maps of the directed system of Stacks 09RE compose.** For `i ≤ j ≤ k` among the
> stages, pushing a homomorphism from the stage `i` to the stage `j` and then to the stage `k`
> gives the same homomorphism `E_k ⟶ K_k` as pushing it to the stage `k` directly. Together with
> `AlgebraicGeometry.DescentSituation.homProjection_homTransition` this says that
> `i ↦ Hom_{D(𝒪_{S_i})}(E_i, K_i)` is a system over the stages and that the maps to
> `Hom_{D(𝒪_S)}(E, K)` form a cocone on it, which is what makes the colimit the tag speaks of
> well-posed.
>
> Like the cocone clause, this holds for all `E₀` and `K₀`; it is the cocycle
> identity of the comparisons `Lf_{i0}^* ⋙ Lf_{ji}^* ≅ Lf_{j0}^*`.

```lean
theorem homTransition_homTransition (i j k : D.Stages) (h : i ≤ j) (h' : j ≤ k)
    (g : stageObj E₀ i ⟶ stageObj K₀ i) :
    homTransition E₀ K₀ j k h' (homTransition E₀ K₀ i j h g) =
      homTransition E₀ K₀ i k (h.trans h') g
```

**`AlgebraicGeometry.DescentSituation.isHomColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LimitHomDescent.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/LimitHomDescent.lean#L301).

> **Stacks 09RE.** In Situation 09RD, let `E₀` and `K₀` be objects of `D(𝒪_{S₀})`, put
> `E_i = Lf_{i0}^*E₀`, `K_i = Lf_{i0}^*K₀` for `i ≥ 0` and `E = Lf_0^*E₀`, `K = Lf_0^*K₀`.  If
> either `E₀` is perfect and `K₀` lies in `D_QCoh(𝒪_{S₀})`, or `E₀` is pseudo-coherent and `K₀`
> lies in `D_QCoh(𝒪_{S₀})` and has finite Tor dimension, then
>
> `colim_{i ≥ 0} Hom_{D(𝒪_{S_i})}(E_i, K_i) ⟶ Hom_{D(𝒪_S)}(E, K)`
>
> is an isomorphism.
>
> The index set lies in the universe of the schemes; over a larger index set the statement fails,
> see `AlgebraicGeometry.DescentSituation.exists_not_isHomColimit`.

```lean
theorem isHomColimit
    (hcase :
      (Stacks.Cohomology.PerfectComplexes.IsPerfect
            (X := (D.stage D.base).toRingedSpace) E₀ ∧
          ∀ n : ℤ, SheafOfModules.isQuasicoherent (D.stage D.base).ringCatSheaf
            ((DerivedCategory.homologyFunctor (D.stage D.base).Modules n).obj K₀)) ∨
        (AlgebraicGeometry.RingedSpace.PseudoCoherence.IsPseudoCoherent
            (X := (D.stage D.base).toRingedSpace) E₀ ∧
          (∀ n : ℤ, SheafOfModules.isQuasicoherent (D.stage D.base).ringCatSheaf
            ((DerivedCategory.homologyFunctor (D.stage D.base).Modules n).obj K₀)) ∧
          Stacks.Cohomology.TorAmplitude.HasFiniteTorDimension
            (D.stage D.base).toRingedSpace K₀)) :
    IsHomColimit E₀ K₀
```

## Tag 09RF, a lemma

[Tag 09RF](https://stacks.math.columbia.edu/tag/09RF) in the Stacks Project.

**`AlgebraicGeometry.DescentSituation.perfect_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectCategoryColimit.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectCategoryColimit.lean#L201).

> **[Stacks, Tag 09RF].** In the situation of [Stacks, Tag 09RD], the category of perfect
> objects of `D(𝒪_S)` is the colimit of the categories of perfect objects of `D(𝒪_{S_i})`: the
> comparison functor out of the colimit, induced by derived pullback along the projections, is
>
> 1. essentially surjective — every perfect object of `D(𝒪_S)` is isomorphic to the derived
>    pullback of a perfect object of `D(𝒪_{S_i})` for some `i`; and
> 2. fully faithful — for perfect `E` and `K` on a stage `S_i`, the group
>    `Hom_{D(𝒪_S)}(Lf_i^*E, Lf_i^*K)` is the filtered colimit over `j ≥ i` of the groups
>    `Hom_{D(𝒪_{S_j})}(Lf_{ji}^*E, Lf_{ji}^*K)`.
>
> A morphism of the colimit category between objects living at two stages is a morphism after
> pullback to a common later stage, so the second clause, stated for two objects of one stage, is
> the whole of full faithfulness.

```lean
theorem perfect_isColimit :
    (∀ (E : DerivedCategory D.limitScheme.Modules),
      IsPerfect (X := D.limitScheme.toRingedSpace) E →
      ∃ (i : I) (_ : D.base ≤ i) (Eᵢ : DerivedCategory (D.stage i).Modules),
        IsPerfect (X := (D.stage i).toRingedSpace) Eᵢ ∧
          Nonempty ((derivedPullback (D.projection i).toLRSHom.toShHom).obj Eᵢ ≅ E)) ∧
    (∀ (i : I) (E K : DerivedCategory (D.stage i).Modules),
      IsPerfect (X := (D.stage i).toRingedSpace) E →
      IsPerfect (X := (D.stage i).toRingedSpace) K → IsHomColimit (D := D.atStage i) E K)
```

**`AlgebraicGeometry.DescentSituation.isPerfect_transition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjects.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjects.lean#L135). The attribute's comment: “derived pullback along the transition morphisms of the situation sends perfect objects to perfect objects, so the transition functors of the colimit statement are defined; the colimit property itself is not included”.

> **Derived pullback along a transition morphism of the situation preserves perfectness.**
> This is Stacks 09UA at `f_{ji}`, and it is what makes the transition functor on the categories
> of perfect objects defined.

```lean
theorem isPerfect_transition {i j : I} (h : i ≤ j)
    (E : DerivedCategory (D.stage i).Modules) (hE : IsPerfect (X := (D.stage i).toRingedSpace) E) :
    IsPerfect (X := (D.stage j).toRingedSpace)
      ((derivedPullback (D.transition h).toLRSHom.toShHom).obj E)
```

**`AlgebraicGeometry.DescentSituation.isPerfect_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjects.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjects.lean#L147). The attribute's comment: “derived pullback along the projections of the situation sends perfect objects to perfect objects, so the comparison functors of the colimit statement are defined; the colimit property itself is not included”.

> **Derived pullback along a projection of the situation preserves perfectness.** This is
> Stacks 09UA at `f_i`, and it is what makes the comparison functor from the stage `i` to the limit
> defined.

```lean
theorem isPerfect_projection (i : I)
    (E : DerivedCategory (D.stage i).Modules) (hE : IsPerfect (X := (D.stage i).toRingedSpace) E) :
    IsPerfect (X := D.limitScheme.toRingedSpace)
      ((derivedPullback (D.projection i).toLRSHom.toShHom).obj E)
```

**`AlgebraicGeometry.DescentSituation.perfectComparison_coherence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjects.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjects.lean#L240). The attribute's comment: “the canonical cocone of the colimit statement: the functors between the categories of perfect objects induced by derived pullback along the projections, and their coherence with the transition functors. Neither full faithfulness nor essential surjectivity of the comparison out of the colimit is included”.

> **The cocone coherence on the categories of perfect objects.** For `i ≤ j ≤ k`, comparing
> through the stage `j` and comparing after composing the two transitions give the same
> isomorphism from the functor out of `D_perf(𝒪_{S_i})` through the stage `k` to the functor out
> of `D_perf(𝒪_{S_i})` directly. Together with
> `AlgebraicGeometry.DescentSituation.perfectTransitionComp_coherence` this is the statement that
> the functors `AlgebraicGeometry.DescentSituation.perfectProjection` form a coherent cocone over
> the system of categories of perfect objects.

```lean
theorem perfectComparison_coherence {i j k : I} (h : i ≤ j) (h' : j ≤ k)
    (E : PerfectDerivedCategory (D.stage i)) :
    ((D.perfectComparison h').app ((D.perfectTransition h).obj E)).hom ≫
        ((D.perfectComparison h).app E).hom =
      (D.perfectProjection k).map ((D.perfectTransitionComp h h').app E).hom ≫
        ((D.perfectComparison (h.trans h')).app E).hom
```

**`AlgebraicGeometry.DescentSituation.perfectTransitionComp_coherence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjects.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjects.lean#L280). The attribute's comment: “the system of categories of perfect objects along the transition morphisms: the transition functors, their composition isomorphisms and the cocycle identity those satisfy. Neither full faithfulness nor essential surjectivity of the comparison out of the colimit is included”.

> **The system of transition functors on the categories of perfect objects is coherent.** For
> `i ≤ j ≤ k ≤ l`, the two ways of composing the comparison isomorphisms of the three transitions
> agree.

```lean
theorem perfectTransitionComp_coherence {i j k l : I} (h : i ≤ j) (h' : j ≤ k) (h'' : k ≤ l)
    (E : PerfectDerivedCategory (D.stage i)) :
    ((D.perfectTransitionComp h' h'').app ((D.perfectTransition h).obj E)).hom ≫
        ((D.perfectTransitionComp h (h'.trans h'')).app E).hom =
      (D.perfectTransition h'').map ((D.perfectTransitionComp h h').app E).hom ≫
        ((D.perfectTransitionComp (h.trans h') h'').app E).hom
```

**`AlgebraicGeometry.AffinePerfectLimit.exists_isPerfect_stage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjectsSupplement.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/LimitPerfectObjectsSupplement.lean#L53). The attribute's comment: “essential surjectivity of the comparison out of the colimit, in the affine base case of the source's induction: for a filtered system of rings with colimit R, every perfect object of D(𝒪\_\{Spec R}) is derived pullback of a perfect object at a stage. The induction over the quasi-compact opens of S\_0 that globalises it is not included, and neither is full faithfulness”.

> **Stacks 09RF**, the affine base case of essential surjectivity. Let `i ↦ R_i` be a filtered
> diagram of commutative rings whose colimit is computed on underlying sets, with colimit cocone `c`,
> and write `R = c.pt`, so that `Spec R` is the limit of the affine schemes `Spec R_i`. Then every
> perfect object `E` of `D(𝒪_{Spec R})` is, for some stage `i`, the derived pullback along
> `Spec R ⟶ Spec R_i` of a perfect object of `D(𝒪_{Spec R_i})`.

```lean
theorem exists_isPerfect_stage {J : Type u} [Category.{u} J] [IsFiltered J]
    (A : J ⥤ CommRingCat.{u}) [PreservesColimit A (forget CommRingCat.{u})]
    (c : Cocone A) (hc : IsColimit c) (E : DerivedCategory (Spec c.pt).Modules)
    (hE : IsPerfect (X := (Spec c.pt).toRingedSpace) E) :
    ∃ (j : J) (Ej : DerivedCategory (Spec (A.obj j)).Modules),
      IsPerfect (X := (Spec (A.obj j)).toRingedSpace) Ej ∧
        Nonempty ((derivedPullback (Spec.map (c.ι.app j)).toLRSHom.toShHom).obj Ej ≅ E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.29, Tag 09RC](https://stacks.math.columbia.edu/tag/09RC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

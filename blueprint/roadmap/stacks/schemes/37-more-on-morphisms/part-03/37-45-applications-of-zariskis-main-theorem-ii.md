---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_isAffineOpen_containing_finite_of_locallyQuasiFinite, AlgebraicGeometry.exists_dense_open_isFinite_of_quasiFinite, AlgebraicGeometry.exists_closed_filtration_characterizing_finiteLocallyFree_rank, AlgebraicGeometry.exists_quasiCompact_stratification_of_finiteLocallyFree_rank, AlgebraicGeometry.exists_antitone_opens_iff_fiber_degree_ge, AlgebraicGeometry.exists_open_injective_ideal_sum_with_section, Stacks.MoreMorphisms.exists_isIntegralHom_surjective_zariskiLocallyFactors, Stacks.MoreMorphisms.exists_isFinite_finitePresentation_surjective_zariskiLocallyFactors
statement: formalized
proof: formalized
---

# 37.45 Applications of Zariski's Main Theorem, II

Section 37.45 of the Stacks Project, [Tag 0F2Q](https://stacks.math.columbia.edu/tag/0F2Q). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07S0, a lemma

[Tag 07S0](https://stacks.math.columbia.edu/tag/07S0) in the Stacks Project.

**`AlgebraicGeometry.exists_isAffineOpen_containing_finite_of_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiFinite.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Affine/QuasiAffineQuasiFinite.lean#L168).

> **Stacks Project, Tag 07S0.** Let `f : X ⟶ S` be a separated quasi-finite morphism of
> schemes with affine target. Then every finite set of points of `X` is contained in a single
> affine open of `X`.
>
> Cover the finite set by finitely many affine opens and let `U` be their union. Then `U` is
> quasi-compact, so `U.ι ≫ f` is quasi-compact, and it is still separated and quasi-finite; hence
> it is quasi-affine by Stacks 02LR. Taking the affine open `⊤` of `S` shows that `U` itself is a
> quasi-affine scheme, and Stacks 01ZY part (1) puts the finite set into an affine open of `U`.

```lean
theorem exists_isAffineOpen_containing_finite_of_locallyQuasiFinite [IsSeparated f]
    [LocallyQuasiFinite f] [LocallyOfFiniteType f] [IsAffine S] {E : Set X} (hE : E.Finite) :
    ∃ U : X.Opens, IsAffineOpen U ∧ E ⊆ U
```

## Tag 03I1, a lemma

[Tag 03I1](https://stacks.math.columbia.edu/tag/03I1) in the Stacks Project.

**`AlgebraicGeometry.exists_dense_open_isFinite_of_quasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteOverDenseOpen.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiFinite/FiniteOverDenseOpen.lean#L208).

> **Stacks Project, Tag 03I1.** A quasi-finite morphism of schemes is finite over a dense open
> subscheme of its target. This is also the statement of [Stacks Project, Tag 03HZ], the remark
> offering it as an alternative to [Stacks Project, Tag 02NW] and deferring its proof to here.

```lean
theorem exists_dense_open_isFinite_of_quasiFinite {Y X : Scheme.{u}} (f : Y ⟶ X)
    [LocallyOfFiniteType f] [LocallyQuasiFinite f] [QuasiCompact f] :
    ∃ U : X.Opens, Dense (U : Set X) ∧ IsFinite (f ∣_ U)
```

## Tag 07RY, a lemma

[Tag 07RY](https://stacks.math.columbia.edu/tag/07RY) in the Stacks Project.

**`AlgebraicGeometry.exists_closed_filtration_characterizing_finiteLocallyFree_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/DegreeStratification.lean, line 760](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/DegreeStratification.lean#L760).

> **Stacks Project, Tag 07RY.** A separated, flat, locally finitely presented, locally
> quasi-finite morphism with universally bounded fibres admits a finite closed filtration whose
> strata universally characterize finite locally free base changes of each degree.

```lean
public theorem exists_closed_filtration_characterizing_finiteLocallyFree_rank
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    [IsSeparated f] [LocallyQuasiFinite f] (hbounded : HasUniversallyBoundedFibers f) :
    ∃ (n : ℕ) (Z : Fin (n + 2) → Set S),
      (∀ i, IsClosed (Z i)) ∧
        Z 0 = ∅ ∧
        Z (Fin.last (n + 1)) = Set.univ ∧
        (∀ i : Fin (n + 1), Z i.castSucc ⊆ Z i.succ) ∧
        ∀ (r : Fin (n + 1)) (T : Scheme.{u}) (g : T ⟶ S),
          IsFiniteLocallyFreeOfRank (pullback.snd f g) r.val ↔
            Set.range g.base ⊆ Z r.succ \ Z r.castSucc
```

## Tag 07RZ, a lemma

[Tag 07RZ](https://stacks.math.columbia.edu/tag/07RZ) in the Stacks Project.

**`AlgebraicGeometry.exists_quasiCompact_stratification_of_finiteLocallyFree_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/DegreeStratification.lean, line 1181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/DegreeStratification.lean#L1181).

> **Stacks Project, Tag 07RZ.** A flat, locally finitely presented, separated and quasi-finite
> morphism admits an increasing sequence of closed subsets of its target whose successive
> differences are quasi-compactly immersed and are characterised by the degree of the finite
> locally free base changes of the morphism.

```lean
public theorem exists_quasiCompact_stratification_of_finiteLocallyFree_rank
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f] [IsSeparated f]
    [LocallyQuasiFinite f] [QuasiCompact f] :
    ∃ (Z : ℕ → Set S) (Y : ℕ → Scheme.{u}) (i : (r : ℕ) → Y r ⟶ S),
      (∀ r, IsClosed (Z r)) ∧
        Z 0 = ∅ ∧
        (∀ r, Z r ⊆ Z (r + 1)) ∧
        (⋃ r, Z r) = Set.univ ∧
        (∀ r, IsImmersion (i r)) ∧
        (∀ r, QuasiCompact (i r)) ∧
        (∀ r, Set.range (i r).base = Z (r + 1) \ Z r) ∧
        ∀ (r : ℕ) (T : Scheme.{u}) (g : T ⟶ S),
          IsFiniteLocallyFreeOfRank (pullback.snd f g) r ↔
            Set.range g.base ⊆ Z (r + 1) \ Z r
```

## Tag 086R, a lemma

[Tag 086R](https://stacks.math.columbia.edu/tag/086R) in the Stacks Project.

**`AlgebraicGeometry.exists_antitone_opens_iff_fiber_degree_ge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/DegreeOpenness.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/DegreeOpenness.lean#L443).

> A flat, locally finitely presented, separated and locally quasi-finite morphism of schemes has
> a decreasing sequence of open subschemes of its target through which a field-valued point factors
> exactly when the corresponding fibre has degree at least the index; a fibre which is not finite
> counts as having infinite degree.

```lean
public theorem exists_antitone_opens_iff_fiber_degree_ge {X S : Scheme.{u}} (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] [IsSeparated f] [LocallyQuasiFinite f] :
    ∃ U : ℕ → S.Opens,
      U 0 = ⊤ ∧ Antitone U ∧
        ∀ (d : ℕ) (k : Type u) [Field k] (g : Spec (.of k) ⟶ S),
          (∃ h : Spec (.of k) ⟶ (U d).toScheme, h ≫ (U d).ι = g) ↔
            (¬ IsFinite (pullback.fst g f) ∨
              ∃ r : ℕ, d ≤ r ∧ IsFiniteLocallyFreeOfRank (pullback.fst g f) r)
```

## Tag 082V, a lemma

[Tag 082V](https://stacks.math.columbia.edu/tag/082V) in the Stacks Project.

**`AlgebraicGeometry.exists_open_injective_ideal_sum_with_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/SectionIdealSumCapture.lean, line 1471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/SectionIdealSumCapture.lean#L1471).

> **Stacks 082V.** For `f : X ⟶ S` flat, locally of finite presentation and locally
> quasi-finite and `g` a nonzero global function on `X`, there are opens `V ⊆ f ⁻¹ U` on which `g`
> stays nonzero and a quasi-coherent ideal sheaf `F ⊆ 𝒪_U` such that a finite direct sum of `r > 0`
> copies of `F` injects into `f_* 𝒪_V` with `g|_V` in the image.

```lean
public theorem exists_open_injective_ideal_sum_with_section
    {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [LocallyOfFinitePresentation f] [LocallyQuasiFinite f]
    (g : Γ(X, ⊤)) (hg : g ≠ 0) :
    ∃ (U : S.Opens) (V : X.Opens) (hVU : V ≤ f ⁻¹ᵁ U)
      (F : (SheafOfModules.unit U.toScheme.ringCatSheaf).Submodule),
      F.toSheafOfModules.IsQuasicoherent ∧
      ∃ (r : ℕ) (_hr : 0 < r)
        (φ : (∐ fun _ : Fin r => F.toSheafOfModules) ⟶
          (Scheme.Modules.pushforward (f.resLE U V hVU)).obj (SheafOfModules.unit _)),
        Mono φ ∧
          ∃ t : Γ((∐ fun _ : Fin r => F.toSheafOfModules), ⊤),
            Scheme.Modules.Hom.app φ ⊤ t =
              (show Γ((Scheme.Modules.pushforward (f.resLE U V hVU)).obj
                (SheafOfModules.unit _), ⊤) from (V.ι.appTop).hom g) ∧
          (V.ι.appTop).hom g ≠ 0
```

## Tag 09Z0, a lemma

[Tag 09Z0](https://stacks.math.columbia.edu/tag/09Z0) in the Stacks Project.

**`Stacks.MoreMorphisms.exists_isIntegralHom_surjective_zariskiLocallyFactors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IntegralRefinement.lean, line 907](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IntegralRefinement.lean#L907). The attribute's comment: “the existence assertion: a surjective étale covering of a quasi-compact and quasi-separated scheme is refined by a surjective integral morphism factoring through it Zariski-locally. The closing sentence, that the refinement may be taken finite and of finite presentation, is `Stacks.MoreMorphisms.exists_isFinite_finitePresentation_surjective_zariskiLocallyFactors`”.

> **Stacks, Tag 09Z0: a surjective étale covering is refined by a surjective integral morphism
> which factors through it Zariski-locally.** Let `p : U ⟶ X` be a surjective étale morphism of
> schemes with `X` quasi-compact and quasi-separated. Then there exist a scheme `Y` and a
> surjective integral morphism `f : Y ⟶ X` such that every point of `Y` has an open neighbourhood
> `V` for which `V ⟶ X` factors through `p`.
>
> This is the general case of the tag's existence statement: neither separatedness of `p` nor any
> hypothesis on its fibre degrees is assumed. The source's first reduction, to an affine — hence
> separated — source, is `Stacks.MoreMorphisms.exists_of_isAffine_source`; a natural-number bound
> for the degrees of the fibres over that affine source comes from
> [Stacks, Tag 03JA](https://stacks.math.columbia.edu/tag/03JA); and the induction on that bound is
> `Stacks.MoreMorphisms.exists_isIntegralHom_factorsNear_of_boundsFiberDegrees`.
>
> The tag's closing refinement, that `f` may moreover be taken finite and of finite presentation,
> is `Stacks.MoreMorphisms.exists_isFinite_finitePresentation_surjective_zariskiLocallyFactors`,
> proved by presenting the integral refinement produced here as a limit of morphisms finite and of
> finite presentation.

```lean
public theorem exists_isIntegralHom_surjective_zariskiLocallyFactors (p : U ⟶ X) [Etale p]
    [Surjective p] [CompactSpace X] [QuasiSeparatedSpace X] :
    ∃ (Y : Scheme.{u}) (f : Y ⟶ X), IsIntegralHom f ∧ Surjective f ∧
      ZariskiLocallyFactors f p
```

**`Stacks.MoreMorphisms.exists_isFinite_finitePresentation_surjective_zariskiLocallyFactors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/IntegralRefinementFinite.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/IntegralRefinementFinite.lean#L140). The attribute's comment: “the whole statement: the surjective refinement factoring through the covering Zariski-locally, and the closing sentence that it may be taken finite and of finite presentation”.

> **Stacks, Tag 09Z0: the refinement may be taken finite and of finite presentation.** Let
> `p : U ⟶ X` be a surjective étale morphism of schemes with `X` quasi-compact and quasi-separated.
> Then there exist a scheme `Y` and a surjective morphism `f : Y ⟶ X` which is finite and of finite
> presentation — hence in particular integral — such that every point of `Y` has an open
> neighbourhood `V` for which `V ⟶ X` factors through `p`.
>
> This is the whole of the tag: the first assertion asks only that `f` be integral, which finiteness
> gives, and the closing sentence asks for exactly the finiteness and the finite presentation. No
> hypothesis beyond the source's is used; in particular `p` is not assumed separated and nothing is
> assumed about the degrees of its fibres.
>
> The integral refinement is
> `Stacks.MoreMorphisms.exists_isIntegralHom_surjective_zariskiLocallyFactors`; it is presented as
> a limit of morphisms finite and of finite presentation by
> `Stacks.AlgebraicGeometry.Tag0817PartTwo.nonempty_integralLimitPresentation`, which is
> [Stacks, Tag 09YZ](https://stacks.math.columbia.edu/tag/09YZ) over a quasi-compact and
> quasi-separated base; and one stage of that limit already carries the covering and the
> factorisations, by
> `AlgebraicGeometry.exists_finite_surjective_refinement_of_isLimit`.

```lean
public theorem exists_isFinite_finitePresentation_surjective_zariskiLocallyFactors (p : U ⟶ X)
    [Etale p] [Surjective p] [CompactSpace X] [QuasiSeparatedSpace X] :
    ∃ (Y : Scheme.{u}) (f : Y ⟶ X), IsIntegralHom f ∧ Surjective f ∧ IsFinite f ∧
      LocallyOfFinitePresentation f ∧ QuasiCompact f ∧ QuasiSeparated f ∧
      ZariskiLocallyFactors f p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.45, Tag 0F2Q](https://stacks.math.columbia.edu/tag/0F2Q)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

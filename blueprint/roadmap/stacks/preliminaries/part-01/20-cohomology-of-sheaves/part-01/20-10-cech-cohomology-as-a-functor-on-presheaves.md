---
declaration: section
origin: cited
lean: Stacks.Cohomology.CechExactFunctor.presheafCechComplexFunctor, Stacks.Cohomology.CechExactFunctor.presheafCechComplexFunctor_exact, Stacks.CategoryTheory.CechComplex.shortExact_map_cechComplexFunctor, Stacks.Cohomology.CechDeltaFunctor.presheafCechCohomologyDeltaFunctor, Stacks.CategoryTheory.CechComplex.cechδ, Stacks.CategoryTheory.CechComplex.cech_exact₁, Stacks.CategoryTheory.CechComplex.cech_exact₂, Stacks.CategoryTheory.CechComplex.cech_exact₃
statement: formalized
proof: formalized
---

# 20.10 Čech cohomology as a functor on presheaves

Section 20.10 of the Stacks Project, [Tag 01EH](https://stacks.math.columbia.edu/tag/01EH). 6 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01EI, an equation

[Tag 01EI](https://stacks.math.columbia.edu/tag/01EI) in the Stacks Project.

**`Stacks.Cohomology.CechExactFunctor.presheafCechComplexFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/ComplexFunctorExactness.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/ComplexFunctorExactness.lean#L170). The attribute's comment: “the family is not required to cover `U`, which neither the functor nor its differentials use”.

> **Stacks Project, Tag 01EI.** The Čech complex functor
> `Č^•(U, -) : PMod(R) ⥤ Comp⁺(Mod_{R(U)})` for a family of opens contained in `U`: a
> presheaf of `R`-modules goes to its Čech cochain complex, each term a module over `R(U)`
> and each differential `R(U)`-linear.

```lean
public noncomputable def presheafCechComplexFunctor
    (R : (Opens X)ᵒᵖ ⥤ RingCat.{r}) (U : Opens X) {ι : Type w}
    (obj : ι → Opens X) (le : ∀ i, obj i ≤ U) :
    PresheafOfModules.{max v w} R ⥤
      CochainComplex (ModuleCat.{max v w} (R.obj (op U))) ℕ
```

## Tag 01EJ, a lemma

[Tag 01EJ](https://stacks.math.columbia.edu/tag/01EJ) in the Stacks Project.

**`Stacks.Cohomology.CechExactFunctor.presheafCechComplexFunctor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/ComplexFunctorExactness.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/ComplexFunctorExactness.lean#L263).

> **Stacks Project, Tag 01EJ.** The Čech complex functor on presheaves of
> modules is exact.

```lean
public theorem presheafCechComplexFunctor_exact
    (R : (Opens X)ᵒᵖ ⥤ RingCat.{r}) (U : Opens X) {ι : Type w}
    (obj : ι → Opens X) (le : ∀ i, obj i ≤ U) :
    exactFunctor (PresheafOfModules.{max v w} R)
      (CochainComplex (ModuleCat.{max v w} (R.obj (op U))) ℕ)
      (presheafCechComplexFunctor R U obj le)
```

**`Stacks.CategoryTheory.CechComplex.shortExact_map_cechComplexFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean#L151). The attribute's comment: “exactness of the Čech complex functor into complexes, for Mathlib's cechComplexFunctor, and assuming short exactness of sections only over the intersections that occur in the Čech complex”. References: EGA III (1.2.5), “partial”.

> **The Čech half of [Stacks, Tag 01EJ].** If the sections of a short complex of presheaves are
> short exact over every object `inter U x` appearing in the Čech complex of the family `U`, then the
> Čech complexes form a short exact sequence of cochain complexes. Short exactness in the presheaf
> category, the hypothesis of [Stacks, Tag 01EJ], is the case in which this holds over every object.

```lean
theorem shortExact_map_cechComplexFunctor
    (hS : ∀ (n : ℕ) (x : Fin (n + 1) → ι),
      (S.map ((evaluation Cᵒᵖ A).obj (op (inter U x)))).ShortExact) :
    (S.map (cechComplexFunctor U)).ShortExact
```

## Tag 01EK, a lemma

[Tag 01EK](https://stacks.math.columbia.edu/tag/01EK) in the Stacks Project.

**`Stacks.Cohomology.CechDeltaFunctor.presheafCechCohomologyDeltaFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/DeltaFunctor.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/DeltaFunctor.lean#L282).

> **Stacks Project, Tag 01EK.** The Čech cohomology functors of a family of opens form a
> cohomological delta functor from presheaves of modules over the structure presheaf to
> modules over the ring of sections on the ambient open.

```lean
public noncomputable def presheafCechCohomologyDeltaFunctor
    (R : (Opens X)ᵒᵖ ⥤ RingCat.{uR}) (U : Opens X) {ι : Type w}
    (obj : ι → Opens X) (le : ∀ i, obj i ≤ U) :
    { F : DeltaFunctor (PresheafOfModules.{max v w} R)
        (ModuleCat.{max v w} (R.obj (op U))) //
      ∀ n : ℕ, F.functor n =
        ((PresheafOfModules.pushforward₀ (Over.forget U) R ⋙
          PresheafOfModules.forgetToPresheafModuleCat
            (op (Over.mk (𝟙 U))) (Over.mkIdTerminal.op) :
              PresheafOfModules.{max v w} R ⥤
                (Over U)ᵒᵖ ⥤ ModuleCat.{max v w} (R.obj (op U))) ⋙
          CategoryTheory.cechComplexFunctor
            (fun i ↦ Over.mk (homOfLE (le i)))) ⋙
          HomologicalComplex.homologyFunctor
            (ModuleCat.{max v w} (R.obj (op U))) (ComplexShape.up ℕ) n }
```

**`Stacks.CategoryTheory.CechComplex.cechδ`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean#L178). The attribute's comment: “the connecting maps and the long exact sequence of Čech cohomology”.

> **The connecting map of Čech cohomology.** For a short complex of presheaves whose sections are
> short exact over the objects of the Čech complex of `U`, this is the map
> `Ȟ^n(𝒰, P₃) ⟶ Ȟ^(n+1)(𝒰, P₁)`.

```lean
def cechδ (n : ℕ) :
    ((cechComplexFunctor U).obj S.X₃).homology n ⟶
      ((cechComplexFunctor U).obj S.X₁).homology (n + 1)
```

**`Stacks.CategoryTheory.CechComplex.cech_exact₁`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean#L199). The attribute's comment: “the connecting maps and the long exact sequence of Čech cohomology”.

> **Exactness of `Ȟ^n(𝒰, P₃) ⟶ Ȟ^(n+1)(𝒰, P₁) ⟶ Ȟ^(n+1)(𝒰, P₂)`**, one of the three exactness
> statements making up the long exact sequence of [Stacks, Tag 01EK].

```lean
theorem cech_exact₁ (n : ℕ) :
    (ShortComplex.mk _ _ (cech_δ_comp U S hS n)).Exact
```

**`Stacks.CategoryTheory.CechComplex.cech_exact₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean#L207). The attribute's comment: “the connecting maps and the long exact sequence of Čech cohomology”.

> **Exactness of `Ȟ^n(𝒰, P₁) ⟶ Ȟ^n(𝒰, P₂) ⟶ Ȟ^n(𝒰, P₃)`**, one of the three exactness statements
> making up the long exact sequence of [Stacks, Tag 01EK].

```lean
theorem cech_exact₂ (n : ℕ) :
    (ShortComplex.mk
      (HomologicalComplex.homologyMap ((cechComplexFunctor U).map S.f) n)
      (HomologicalComplex.homologyMap ((cechComplexFunctor U).map S.g) n)
      (by rw [← HomologicalComplex.homologyMap_comp, ← Functor.map_comp, S.zero,
        Functor.map_zero, HomologicalComplex.homologyMap_zero])).Exact
```

**`Stacks.CategoryTheory.CechComplex.cech_exact₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/LongExactSequence.lean#L218). The attribute's comment: “the connecting maps and the long exact sequence of Čech cohomology”.

> **Exactness of `Ȟ^n(𝒰, P₂) ⟶ Ȟ^n(𝒰, P₃) ⟶ Ȟ^(n+1)(𝒰, P₁)`**, one of the three exactness
> statements making up the long exact sequence of [Stacks, Tag 01EK].

```lean
theorem cech_exact₃ (n : ℕ) :
    (ShortComplex.mk _ _ (cech_comp_δ U S hS n)).Exact
```

## Tag 01EL, a lemma

[Tag 01EL](https://stacks.math.columbia.edu/tag/01EL) in the Stacks Project.

**`StacksCechPresheaf.ModPresheaf.main_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/PresheavesOfModulesComplex.lean, line 1231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/PresheavesOfModulesComplex.lean#L1231).

> **Stacks 20.10.3, tag 01EL.** The natural isomorphism of functors
> `Hom_{O_X}(K(U)_•, -) ≅ Č^•(U, -)` itself (the data, not merely its existence), exhibiting the
> isomorphism `Hom_{O_X}(K(U)_•, F) ≅ Č^•(U, F)` as natural in `F`.

```lean
noncomputable def main_iso (U : Cover X I) :
    homComplexFunctor U ≅ cechComplexFunctor U
```

## Tag 01EM, a lemma

[Tag 01EM](https://stacks.math.columbia.edu/tag/01EM) in the Stacks Project.

**`Stacks.Cohomology.CechImagePresheaf.positive_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean#L497). The attribute's comment: “positive-degree homology”.

> The Čech chain complex of an open covering is exact in every positive degree, objectwise on
> opens. Equivalently all its positive-degree homology presheaves vanish.

```lean
public theorem positive_exact (U : Cover X I) (p : ℕ) (W : Opens X.carrier) :
    LinearMap.range ((Kdiff U (p + 1)).app W) =
      LinearMap.ker ((Kdiff U p).app W)
```

**`Stacks.Cohomology.CechImagePresheaf.augmentation_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean, line 516](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean#L516). The attribute's comment: “degree-zero homology”.

> The kernel of the canonical augmentation is the image of the first Čech differential. Thus
> degree-zero homology is canonically the image presheaf of `K(U)₀ → O_X`, with its evident maps on
> restrictions.

```lean
public theorem augmentation_ker (U : Cover X I) (W : Opens X.carrier) :
    LinearMap.ker (augmentationApp U W) =
      LinearMap.range ((Kdiff U 0).app W)
```

**`Stacks.Cohomology.CechImagePresheaf.homologyZeroIsoImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean, line 526](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean#L526). The attribute's comment: “canonical degree-zero identification”.

> The canonical identification of degree-zero homology with the image of the augmentation. Its
> value on a homology class is the augmentation of a representative; this specification determines
> the isomorphism uniquely.

```lean
public noncomputable def homologyZeroIsoImage (U : Cover X I)
    (W : Opens X.carrier) :
    { e : (((Kterm U 0).obj W ⧸ LinearMap.range ((Kdiff U 0).app W)) ≃ₗ[sections X W]
        (imagePresheaf U).obj W) //
      ∀ x : (Kterm U 0).obj W,
        e ((LinearMap.range ((Kdiff U 0).app W)).mkQ x) =
          ⟨augmentationApp U W x, ⟨x, rfl⟩⟩ }
```

**`Stacks.Cohomology.CechImagePresheaf.homologyZeroIsoImage_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean#L546). The attribute's comment: “naturality of degree-zero identification”.

> The canonical degree-zero identification commutes with restrictions; hence it is an isomorphism
> of homology presheaves, not merely a family of isomorphisms.

```lean
public theorem homologyZeroIsoImage_naturality (U : Cover X I)
    {W W' : Opens X.carrier} (h : W ≤ W') (x : (Kterm U 0).obj W') :
    (homologyZeroIsoImage U W).1
        ((LinearMap.range ((Kdiff U 0).app W)).mkQ ((Kterm U 0).res h x)) =
      (imagePresheaf U).res h
        ((homologyZeroIsoImage U W').1
          ((LinearMap.range ((Kdiff U 0).app W')).mkQ x))
```

Declarations registered for the tag:

- [`imagePresheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=imagePresheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechOfPresheavesOfModules/HomologyOfTheAugmentedComplex.lean#L174) (StacksFrontier).

## Tag 01EN, a lemma

[Tag 01EN](https://stacks.math.columbia.edu/tag/01EN) in the Stacks Project.

**`Stacks.Cohomology.CechDelta.cechDeltaFunctorIsoRightDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechDerived/DerivedDeltaFunctor.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechDerived/DerivedDeltaFunctor.lean#L329). The attribute's comment: “the canonical delta-functor isomorphism”.

> **Stacks 01EN, first assertion.** Čech cohomology of the covering `𝒰`, as the cohomological
> δ-functor on presheaves of `R`-modules of Stacks 01EK, is canonically isomorphic to the
> right-derived δ-functor of its degree-zero part. All three inputs of Stacks 01EN are now
> available: enough injectives on presheaves of modules (Stacks 01DV), effaceability of the Čech
> δ-functor (Stacks 01EL and 01EM), and the δ-functor `cechRightDerivedDeltaFunctor` realizing
> the right derived functors. The argument is the one of Stacks 010T and 010U: both δ-functors
> are universal, and universal δ-functors with the same degree-zero part are uniquely
> isomorphic.

```lean
def cechDeltaFunctorIsoRightDerived : cechDeltaFunctor R 𝒰 ≅ cechRightDerivedDeltaFunctor R 𝒰
```

**`Stacks.Cohomology.CechComparisonU.cechDerivedComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechDerivedComparison/Assembled.lean, line 452](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechDerivedComparison/Assembled.lean#L452). The attribute's comment: “construction of the canonical delta-functor isomorphism”.

> **Stacks Project, Tag 01EN, first assertion (construction), at four independent
> universes.** The space, the structure ring, the coefficient modules and the covering index are
> independent; the module universe is `max u r v w`, as the indexed products and injective
> resolutions need. Every field is the four-universe one of
> `Stacks.Cohomology.CechComparisonU`, over the Godement effacement of
> `Stacks.Cohomology.CechComparisonU.effaceable_cechDeltaFunctor` and the `derivedδ_eq` field
> proved above.
>
> This construction carries the first assertion's proof obligation.

```lean
def cechDerivedComparison : CechDerivedComparison.{u, r, v, w} O 𝒰
```

**`Stacks.Cohomology.CechTotalComparison.cechComplexIsoRightDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/QuasiIsoToDerivedCechCohomology.lean, line 1208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/CechTotalComplex/QuasiIsoToDerivedCechCohomology.lean#L1208). The attribute's comment: “the functorial quasi-isomorphism”.

> **Stacks Project, Tag 01EN, moreover assertion.** The functorial quasi-isomorphism from the
> Čech complex functor to the total right-derived functor of degree-zero Čech cohomology,
> together with, for every injective resolution, the two augmentations into the total Čech
> complex that prescribe it.
>
> The isomorphism is built at a resolution chosen for each presheaf; it is natural because the
> two augmentations and the comparison with the total right derived functor are each natural in
> the resolution, and independent of that choice because naturality over the identity says so.

```lean
noncomputable def cechComplexIsoRightDerived : CechComplexIsoRightDerived.{u} O 𝒰
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.10, Tag 01EH](https://stacks.math.columbia.edu/tag/01EH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

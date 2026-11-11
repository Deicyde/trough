---
declaration: section
origin: cited
lean: Stacks.Sites.FibredCategory.FibredCategorySituation.totalRingedTopos, Stacks.Sites.FibredCategory.FibredCategorySituation.ringedProjection, Stacks.Sites.FibredCategory.FibredCategorySituation, Stacks.Sites.FibredCategory.FibredCategorySituation.inducedProjection, Stacks.Sites.FibredCategory.FibredCategorySituation.commRingRingedProjection, Stacks.Sites.FibredCategory.localizedProjectionSection, Stacks.Sites.FibredCategory.MorphismSituation.ringedToposDiagram, Stacks.Sites.FibredCategory.MorphismSituation
statement: formalized
proof: formalized
---

# 21.38 Derived lower shriek for fibred categories

Section 21.38 of the Stacks Project, [Tag 08RV](https://stacks.math.columbia.edu/tag/08RV). 8 tags here are carried by 31 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08P8, a situation

[Tag 08P8](https://stacks.math.columbia.edu/tag/08P8) in the Stacks Project.

**`Stacks.Sites.FibredCategory.FibredCategorySituation.totalRingedTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedProjection.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedProjection.lean#L83). The attribute's comment: “inverse-image structure sheaf”.

> **Stacks 08P8, the inverse-image structure sheaf.** The total ringed topos, with
> `O_C = π⁻¹O_D`.

```lean
def totalRingedTopos : RingedTopos.{vC, uC, max w uD vD uC vC}
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.ringedProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedProjection.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedProjection.lean#L91). The attribute's comment: “morphism of ringed topoi”.

> **Stacks 08P8, the morphism of ringed topoi.** The projection as a morphism of ringed
> topoi; its structure map is the unit of the adjunction `π⁻¹ ⊣ π_*` on sheaves of rings.

```lean
def ringedProjection : RingedToposHom s.totalRingedTopos s.baseRingedTopos
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAFibredCategory.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAFibredCategory.lean#L321). The attribute's comment: “standing data”.

> A ringed site `(D, O_D)` together with a fibred category `p : C ⥤ D` over its underlying
> site.

```lean
structure FibredCategorySituation
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.inducedProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAFibredCategory.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAFibredCategory.lean#L375). The attribute's comment: “associated morphism of topoi”.

> **Stacks 08P8, the associated morphism of topoi.** The morphism of topoi
> `π : Sh(C) ⟶ Sh(D)` canonically associated to the fibred projection: its inverse image is
> restriction along `p.op`, which is left exact because restriction is computed on underlying
> presheaves, where it is precomposition.

```lean
noncomputable def inducedProjection : ProjectionData s
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.commRingRingedProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategoryRingedTopos.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategoryRingedTopos.lean#L75). The attribute's comment: “morphism of ringed topoi”.

> The projection of a fibred category as a morphism of ringed topoi; its structure map is the
> unit of the adjunction `π⁻¹ ⊣ π_*` on sheaves of commutative rings.

```lean
noncomputable def commRingRingedProjection :
    AlgebraicGeometry.RingedToposHom s.totalRingedTopos s.baseRingedTopos
```

Declarations registered for the tag:

- [`Stacks.Sites.FibredCategory.FibredCategorySituation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAFibredCategory.lean#L321), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategoryRingedTopos.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategoryRingedTopos.lean#L51) (StacksFrontier): “standing data”.
- [`Stacks.Sites.FibredCategory.FibredCategorySituation.inducedProjection`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAFibredCategory.lean#L375), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategoryRingedTopos.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategoryRingedTopos.lean#L54) (StacksFrontier): “associated morphism of topoi”.
- [`Stacks.Sites.FibredCategory.FibredCategorySituation.totalRingedTopos`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedProjection.lean#L83), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategoryRingedTopos.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategoryRingedTopos.lean#L57) (StacksFrontier): “inverse-image structure sheaf”.

## Tag 08P9, a lemma

[Tag 08P9](https://stacks.math.columbia.edu/tag/08P9) in the Stacks Project.

**`Stacks.Sites.FibredCategory.localizedProjectionSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategorySection.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/FibredCategorySection.lean#L527).

> The canonical localized projection has a section whose inverse image is its direct image.

```lean
public noncomputable def localizedProjectionSection : LocalizedProjectionSection s U
```

## Tag 08PA, a situation

[Tag 08PA](https://stacks.math.columbia.edu/tag/08PA) in the Stacks Project.

**`Stacks.Sites.FibredCategory.MorphismSituation.ringedToposDiagram`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposDiagram.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposDiagram.lean#L185). The attribute's comment: “canonical commutative triangle of ringed topoi”.

> **Stacks 08PA.** The canonical commutative triangle of ringed topoi associated to a
> 1-morphism of fibred categories over a ringed site: the three morphisms of topoi of Stacks 06NW,
> each pinned by the identification of its inverse image with restriction and of its direct image
> with the right Kan extension, the morphism of ringed topoi `g` whose inverse-image structure map
> is the identification `g⁻¹O_C ≅ O_{C'}`, and the 2-isomorphism `π_* ∘ g_* ≅ (π')_*` exhibited as
> the mate of the comparison of inverse images.

```lean
noncomputable def ringedToposDiagram : S.RingedToposDiagram
```

**`Stacks.Sites.FibredCategory.MorphismSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAMorphism.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedToposOfAMorphism.lean#L136). The attribute's comment: “standing data”.

> **Stacks 08PA, standing data.** A ringed site `(D, O_D)`, two fibred categories over its
> underlying site, and a 1-morphism of fibred categories between them.

```lean
structure MorphismSituation.{a₀, a₁, a₂, b₀, b₁, b₂, c}
```

## Tag 08PB, a lemma

[Tag 08PB](https://stacks.math.columbia.edu/tag/08PB) in the Stacks Project.

**`Stacks.Sites.FibredCategory.MorphismSituation.compatibleLocalizedSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/MorphismOfFibredCategoriesSection.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/LowerShriekAndPerfection/MorphismOfFibredCategoriesSection.lean#L622).

> **Stacks 08PB.** The localized projections of a 1-morphism of fibred categories admit a
> common section: a morphism of topoi `σ' : Sh(D/V) ⟶ Sh(C'/U')` with `π'_{U'} ∘ σ' = id` and
> `(σ')^{-1} = π'_{U',*}`, whose composite `σ = g' ∘ σ'` satisfies `π_U ∘ σ = id` and
> `σ^{-1} = π_{U,*}`.

```lean
def compatibleLocalizedSection : CompatibleLocalizedSection S U'
```

## Tag 08PC, a lemma

[Tag 08PC](https://stacks.math.columbia.edu/tag/08PC) in the Stacks Project.

**`Stacks.Sites.FibredCategory.MorphismSituation.abelianInverseImage_isRightAdjoint`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/AbelianLowerShriek.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/AbelianLowerShriek.lean#L98). The attribute's comment: “part (1), abelian sheaves”.

> **Stacks 08PC, part (1) for abelian sheaves.** The inverse image of abelian sheaves along `g`
> admits a left adjoint `g_!^{Ab}`. The left adjoint is the sheafification of the left Kan extension
> along `u.op`, so the only hypothesis is that abelian groups can be sheafified on the target
> site.

```lean
instance abelianInverseImage_isRightAdjoint
    [HasWeakSheafify S.totalTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂}] :
    S.abelianInverseImage.IsRightAdjoint
```

**`Stacks.Sites.FibredCategory.MorphismSituation.isIso_derivedModuleLowerShriekForgetComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleDerivedLowerShriekForget.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleDerivedLowerShriekForget.lean#L334). The attribute's comment: “part (4): the canonical comparison `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!` is an isomorphism”.

> **Stacks 08PC, part (4).** In Situation 08PA the canonical comparison of Stacks 07AE
>
> `Lg_!^{Ab} ∘ forget ⟶ forget ∘ Lg_!`
>
> of functors `D(O_{C'}) ⥤ D(C)` (`derivedModuleLowerShriekForgetComparison`) is an isomorphism:
> the derived lower shriek on sheaves of modules commutes with forgetting the module structure.
>
> `Lg_!^{Ab} ∘ forget` is a left derived functor of `g_!^{Ab} ∘ forget` on the homotopy category
> of `Mod(O_{C'})` (`isLeftDerivedFunctor_derivedForgetAbelianLowerShriek`), hence of
> `forget ∘ g_!`, the degreewise comparison being invertible by part (2)
> (`isIso_moduleLowerShriekForgetComparison`); and the lift of a comparison between two left derived
> functors of the same functor is an isomorphism.

```lean
theorem isIso_derivedModuleLowerShriekForgetComparison :
    IsIso S.derivedModuleLowerShriekForgetComparison
```

**`Stacks.Sites.FibredCategory.MorphismSituation.moduleDiagramInverseImage_isRightAdjoint`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleInverseImage.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleInverseImage.lean#L212). The attribute's comment: “part (1), modules”.

> **Stacks 08PC, part (1) for sheaves of modules.** The inverse image of sheaves of modules
> along the `g` of a commutative triangle of ringed topoi over the situation admits a left adjoint
> `g_!`. The inverse image is the one of Stacks 03D2 followed by extension of scalars along `g♯`;
> the first factor is a right adjoint because `g⁻¹` is restriction along the continuous functor
> `u`, and the second because `g♯` is an isomorphism, which the triangle records.

```lean
instance moduleDiagramInverseImage_isRightAdjoint (D : S.RingedToposDiagram) :
    (D.gRinged.toModulesHom.pullbackModules).IsRightAdjoint
```

**`Stacks.Sites.FibredCategory.MorphismSituation.moduleDiagramInverseImage_isRightAdjointUnconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleLowerShriekForgetSquare.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleLowerShriekForgetSquare.lean#L138). The attribute's comment: “part (1), modules: `g^*` has a left adjoint `g_!`”.

> **Stacks 08PC, part (1), for sheaves of modules, with no sheafification hypothesis.** The
> inverse image `g^*` of sheaves of modules along the `g` of any commutative triangle of ringed
> topoi over Situation 08PA has a left adjoint `g_!`. This is
> `MorphismSituation.moduleDiagramInverseImage_isRightAdjoint` with its sheafification hypotheses
> discharged: at the situation's universe of sections both inherited sites are essentially
> small.

```lean
theorem moduleDiagramInverseImage_isRightAdjointUnconditional (D : S.RingedToposDiagram) :
    (D.gRinged.toModulesHom.pullbackModules).IsRightAdjoint
```

**`Stacks.Sites.FibredCategory.MorphismSituation.abelianInverseImage_isRightAdjointUnconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleLowerShriekForgetSquare.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleLowerShriekForgetSquare.lean#L147). The attribute's comment: “part (1), abelian sheaves: `g^{-1}` has a left adjoint `g_!^{Ab}`”.

> **Stacks 08PC, part (1), for abelian sheaves, with no sheafification hypothesis.** The
> inverse image `g^{-1}` of abelian sheaves has a left adjoint `g_!^{Ab}`. This is
> `MorphismSituation.abelianInverseImage_isRightAdjoint` with its sheafification hypothesis
> discharged.

```lean
theorem abelianInverseImage_isRightAdjointUnconditional :
    S.abelianInverseImage.IsRightAdjoint
```

**`Stacks.Sites.FibredCategory.MorphismSituation.isIso_moduleLowerShriekForgetComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleLowerShriekForgetSquare.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ModuleLowerShriekForgetSquare.lean#L289). The attribute's comment: “part (2): the canonical comparison `g_!^{Ab} ∘ forget ⟶ forget ∘ g_!` is an isomorphism”.

> **Stacks 08PC, part (2).** In Situation 08PA the canonical comparison of Stacks 0798
>
> `g_!^{Ab} ∘ forget ⟶ forget ∘ g_!`
>
> (`MorphismSituation.moduleLowerShriekForgetComparison`, the transformation adjoint to the
> forgotten unit of `g_! ⊣ g^*`, for the structure sheaf `O_{C'} = (π')^{-1} O_D` of the
> situation) is an isomorphism: lower shriek on sheaves of modules commutes with forgetting the
> module structure.
>
> The comparison is an isomorphism for the structure sheaf `u⁻¹O_C` of `C'`
> (`isIso_lowerShriekForgetComparison_structureMap`, which is where Stacks 08PB enters), and the
> structure sheaf of Situation 08PA is isomorphic to it through the structure map
> `MorphismSituation.moduleStructureMap`, built from the invertible `g♯`; the comparison along an
> isomorphic structure map is the same comparison up to restriction of scalars
> (`Stacks.SheafOfModules.isIso_lowerShriekForgetComparison_of_restrictScalars`).

```lean
theorem isIso_moduleLowerShriekForgetComparison :
    IsIso S.moduleLowerShriekForgetComparison
```

**`Stacks.Sites.FibredCategory.MorphismSituation.derivedAbelianLowerShriekAdjunctionUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/MorphismDerivedAbelianLowerShriek.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/MorphismDerivedAbelianLowerShriek.lean#L50). The attribute's comment: “part (3), abelian sheaves: the adjunction Lg\_!^Ab ⊣ g^-1”.

> **Stacks 08PC part (3) for abelian sheaves, the adjunction.** The unbounded left derived
> lower-shriek functor `Lg_!^{Ab} : D(Ab(C')) ⥤ D(Ab(C))` is left adjoint to `g^{-1}` on the
> unbounded derived categories. This is `MorphismSituation.derivedAbelianLowerShriekAdjunction`
> with its acyclicity input supplied by `abelianLowerShriekAcyclic`.

```lean
def derivedAbelianLowerShriekAdjunctionUnconditional :
    S.derivedAbelianLowerShriek ⊣ S.derivedAbelianInverseImage
```

**`Stacks.Sites.FibredCategory.MorphismSituation.hasPointwiseLeftDerivedModuleLowerShriekUnconditional`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/MorphismModuleLowerShriekAcyclic.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/MorphismModuleLowerShriekAcyclic.lean#L317). The attribute's comment: “part (3), modules: existence of `Lg_! : D(O_{C'}) ⥤ D(O_C)`”.

> **Stacks 08PC part (3) for sheaves of modules, existence.** Degreewise `g_!`, followed by the
> localization of the homotopy category of `Mod(O_C)`, has a pointwise left derived functor along
> the localization of the homotopy category of `Mod(O_{C'})`; that is, `Lg_! : D(O_{C'}) ⥤ D(O_C)`
> exists. This is `MorphismSituation.hasPointwiseLeftDerivedModuleLowerShriek` with the acyclicity
> statement of Stacks 07AC supplied by `moduleLowerShriekAcyclic`.

```lean
instance hasPointwiseLeftDerivedModuleLowerShriekUnconditional :
    (S.moduleLowerShriekOnHomotopy ⋙ DerivedCategory.Qh).HasPointwiseLeftDerivedFunctor
      S.moduleSourceQuasiIso
```

**`Stacks.Sites.FibredCategory.MorphismSituation.derivedModuleLowerShriekAdjunctionUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/MorphismModuleLowerShriekAcyclic.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/MorphismModuleLowerShriekAcyclic.lean#L328). The attribute's comment: “part (3), modules: the adjunction `Lg_! ⊣ g^*`”.

> **Stacks 08PC part (3) for sheaves of modules, the adjunction.** The unbounded left derived
> lower-shriek functor `Lg_! : D(O_{C'}) ⥤ D(O_C)` is left adjoint to `g^* = g^{-1}` on the
> unbounded derived categories. This is `MorphismSituation.derivedModuleLowerShriekAdjunction`
> (Stacks 09T5) with the acyclicity statement of Stacks 07AC supplied by
> `moduleLowerShriekAcyclic`; nothing beyond Situation 08PA is assumed.

```lean
def derivedModuleLowerShriekAdjunctionUnconditional :
    S.derivedModuleLowerShriek ⊣ S.derivedModuleInverseImage
```

Declarations registered for the tag:

- [`Stacks.Sites.FibredCategory.MorphismSituation.hasPointwiseLeftDerivedFunctor_abelianLowerShriekOnHomotopy`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/MorphismLowerShriekAcyclic.lean#L309), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/MorphismDerivedAbelianLowerShriek.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/MorphismDerivedAbelianLowerShriek.lean#L42) (StacksFrontier): “part (3), abelian sheaves: existence of Lg\_!^Ab”.

## Tag 09CY, a remark

[Tag 09CY](https://stacks.math.columbia.edu/tag/09CY) in the Stacks Project.

**`Stacks.Sites.FibredCategory.FibredCategorySituation.toMorphismSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionAsAMorphismOfFibredCategories.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionAsAMorphismOfFibredCategories.lean#L103). The attribute's comment: “the reduction of Situation 08P8 to Situation 08PA, by `C = D` and `u = p`”.

> **Stacks 09CY, the reduction.** The standing data of Stacks 08PA obtained from that of
> Stacks 08P8: the same ringed base site, the target fibred category taken to be the base itself
> fibred over itself by the identity functor, the source fibred category taken to be `C`, and the
> 1-morphism taken to be the structure functor `p`.

```lean
def toMorphismSituation : MorphismSituation.{uD, uD, uC, vD, vD, vC, w}
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.abelianInverseImage_toMorphismSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionAsAMorphismOfFibredCategories.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionAsAMorphismOfFibredCategories.lean#L161). The attribute's comment: “the reduced situation's `g^{-1}` is the `π^{-1}` of Situation 08P8”.

> `g^{-1}` of the reduced situation is `π^{-1}`: both are restriction of abelian sheaves along
> `p` between the same two sites.

```lean
theorem abelianInverseImage_toMorphismSituation :
    HEq s.toMorphismSituation.abelianInverseImage s.abelianInverseImage
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.abelianLowerShriek_toMorphismSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionAsAMorphismOfFibredCategories.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionAsAMorphismOfFibredCategories.lean#L176). The attribute's comment: “the reduced situation's `g_!^{Ab}` is the `π_!^{Ab}` of Situation 08P8”.

> `g_!^{Ab}` of the reduced situation is `π_!^{Ab}`: both are the chosen left adjoint of
> restriction of abelian sheaves along `p` between the same two sites.

```lean
theorem abelianLowerShriek_toMorphismSituation :
    HEq (@MorphismSituation.abelianLowerShriek.{uD, uD, uC, vD, vD, vC, w} s.toMorphismSituation
        s.hasWeakSheafifyToMorphismSituationTotalTopology) s.abelianLowerShriek
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.derivedAbelianLowerShriekAdjunctionUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionLowerShriekAcyclic.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionLowerShriekAcyclic.lean#L339). The attribute's comment: “the derived abelian `Lπ_!^{Ab}` of Situation 08P8 and its adjunction `Lπ_!^{Ab} ⊣ π^{-1}`, with the acyclicity statement of Stacks 07AC discharged”.

> **Stacks 09CY, the derived abelian `Lπ_!^{Ab}` of Situation 08P8.** Remark 09CY reduces
> Situation 08P8 to Situation 08PA and reads off from Lemma 08PC the four functors `π_!`,
> `π_!^{Ab}`, `Lπ_!` and `Lπ_!^{Ab}`. This is the third of them: `Lπ_!^{Ab} : D(Ab(C)) ⥤ D(Ab(D))`
> is left adjoint to derived `π^{-1}`, which is part (3) of Stacks 08PC on abelian sheaves.
>
> It is stated here rather than transported along the reduction because the acyclicity statement
> of Stacks 07AC, which is what part (3) rests on, is discharged for `π` in this file, as
> `abelianLowerShriekAcyclic`; the conditional form `derivedAbelianLowerShriekAdjunction` takes it
> as an argument, and this is that argument supplied, so the adjunction holds under the hypotheses
> of Situation 08P8 alone.

```lean
def derivedAbelianLowerShriekAdjunctionUnconditional :
    s.derivedAbelianLowerShriek ⊣ s.derivedAbelianInverseImage
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.derivedModuleLowerShriekAdjunctionAtBaseModuleRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionModuleDerivedLowerShriek.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionModuleDerivedLowerShriek.lean#L333). The attribute's comment: “the derived `Lπ_!` of Situation 08P8 on sheaves of modules and its adjunction `Lπ_! ⊣ π^*`”.

> **Stacks 09CY, the derived `Lπ_!` on sheaves of modules.** The unbounded left derived functor
> `Lπ_! : D(O_C) ⥤ D(O_D)` of the lower-shriek functor on sheaves of modules exists and is left
> adjoint to `π^* : D(O_D) ⥤ D(O_C)`. This is Stacks 08PC part (3) for modules in the situation of
> the remark; the acyclicity statement of Stacks 07AC it rests on is `moduleLowerShriekAcyclic`.

```lean
def derivedModuleLowerShriekAdjunctionAtBaseModuleRing :
    s.derivedModuleLowerShriekAtBaseModuleRing ⊣ s.derivedModuleRestriction
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.isIso_derivedModuleLowerShriekForgetComparison`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionModuleDerivedLowerShriek.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionModuleDerivedLowerShriek.lean#L354). The attribute's comment: “`forget ∘ Lπ_! = Lπ_!^{Ab} ∘ forget`: the canonical comparison of Stacks 07AE is an isomorphism”.

> **Stacks 09CY, `forget ∘ Lπ_! = Lπ_!^{Ab} ∘ forget`.** The canonical comparison
> `Lπ_!^{Ab} ∘ forget ⟶ forget ∘ Lπ_!` of Stacks 07AE is an isomorphism. This is Stacks 08PC
> part (4) in the situation of the remark.

```lean
instance isIso_derivedModuleLowerShriekForgetComparison :
    IsIso s.derivedModuleLowerShriekForgetComparison
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.moduleLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionModuleLowerShriek.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionModuleLowerShriek.lean#L164). The attribute's comment: “the module-level `π_!` of Situation 08P8 and its adjunction `π_! ⊣ π^*`”.

> **Stacks 09CY, the module-level `π_!`.** The lower-shriek functor `π_!` on sheaves of modules
> is left adjoint to `π^* = π⁻¹`, restriction of sheaves of modules along `p`.

```lean
def moduleLowerShriekAdjunction : s.moduleLowerShriek ⊣ s.sheafModuleRestriction
```

**`Stacks.Sites.FibredCategory.FibredCategorySituation.isIso_moduleLowerShriekForgetComparison`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionModuleLowerShriek.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/ProjectionModuleLowerShriek.lean#L204). The attribute's comment: “`forget ∘ π_! = π_!^{Ab} ∘ forget`: the canonical comparison of Stacks 0798 is an isomorphism”.

> **Stacks 09CY, `forget ∘ π_! = π_!^{Ab} ∘ forget`.** The canonical comparison
> `π_!^{Ab} ∘ forget ⟶ forget ∘ π_!` of Stacks 0798 between lower shriek of abelian sheaves and
> lower shriek of sheaves of modules, for the projection of a fibred category, is an isomorphism.
>
> By the criterion of Stacks 0798 this reduces to the canonical maps
> `(π_U)_!^{Ab} O_U ⟶ O_{p(U)}`, which are isomorphisms by
> `isIso_localizedStructureSheafComparison_baseModuleRing`. This is Stacks 08PC part (2) in the
> situation of the remark.

```lean
instance isIso_moduleLowerShriekForgetComparison :
    IsIso s.moduleLowerShriekForgetComparison
```

## Tag 08PD, a remark

[Tag 08PD](https://stacks.math.columbia.edu/tag/08PD) in the Stacks Project.

**`Stacks.Sites.FibredCategory.MorphismSituation.derivedAbelianLowerShriekCompIso'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/CanonicalDerivedLowerShriekMap.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/CanonicalDerivedLowerShriekMap.lean#L92). The attribute's comment: “the identification Lπ'\_! = Lπ\_! ∘ Lg\_!”.

> **Stacks 08PD, the identification `Lπ'_! = Lπ_! ∘ Lg_!`**, for every situation of
> Stacks 08PA. The three derived lower-shriek functors are left adjoint to the three derived
> restrictions, by Stacks 07AC at the three discharged acyclicity statements, and restriction to the
> source fibred category is restriction to the target followed by restriction along the
> 1-morphism; so this is uniqueness of left adjoints applied to
> `derivedAbelianInverseImageCompIso`.

```lean
def derivedAbelianLowerShriekCompIso' :
    S.derivedAbelianLowerShriek ⋙ S.derivedTotalAbelianLowerShriek ≅
      S.derivedSourceAbelianLowerShriek
```

**`Stacks.Sites.FibredCategory.MorphismSituation.canonicalDerivedLowerShriekMap'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/CanonicalDerivedLowerShriekMap.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/CanonicalDerivedLowerShriekMap.lean#L118). The attribute's comment: “canonical map”.

> **Stacks 08PD, the canonical map**, for every situation of Stacks 08PA. Let `F` be an abelian
> sheaf on `C`, let `F'` be an abelian sheaf on `C'` and let `t : F' ⟶ g⁻¹F` be a map of abelian
> sheaves. The canonical map `Lπ'_!(F') ⟶ Lπ_!(F)` is the identification `Lπ'_! = Lπ_! ∘ Lg_!`
> followed by `Lπ_!` applied to the composite of the comparison `Lg_!(F') ⟶ g_!F'` with the adjoint
> `g_!F' ⟶ F` of `t`.

```lean
def canonicalDerivedLowerShriekMap'
    (F : Sheaf S.totalTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂})
    (F' : Sheaf S.sourceTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂})
    (t : F' ⟶ S.abelianInverseImage.obj F) :
    S.derivedSourceAbelianLowerShriek.obj ((DerivedCategory.singleFunctor
        (Sheaf S.sourceTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂}) 0).obj F') ⟶
      S.derivedTotalAbelianLowerShriek.obj ((DerivedCategory.singleFunctor
        (Sheaf S.totalTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂}) 0).obj F)
```

**`Stacks.Sites.FibredCategory.MorphismSituation.derivedAbelianLowerShriekCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/DerivedLowerShriekFunctoriality.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/DerivedLowerShriekFunctoriality.lean#L476). The attribute's comment: “the identification Lπ'\_! = Lπ\_! ∘ Lg\_!”.

> **The identification `Lπ'_! = Lπ_! ∘ Lg_!`**, the isomorphism of left adjoints induced by
> `derivedAbelianInverseImageCompIso`.

```lean
def derivedAbelianLowerShriekCompIso (h : S.AbelianLowerShriekAcyclic)
    (hp : S.TotalAbelianLowerShriekAcyclic) (hp' : S.SourceAbelianLowerShriekAcyclic) :
    S.derivedAbelianLowerShriek ⋙ S.derivedTotalAbelianLowerShriek ≅
      S.derivedSourceAbelianLowerShriek
```

**`Stacks.Sites.FibredCategory.MorphismSituation.canonicalDerivedLowerShriekMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/DerivedLowerShriekFunctoriality.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/DerivedLowerShriekFunctoriality.lean#L524). The attribute's comment: “canonical map”.

> **The canonical map.** Let `F` be an abelian sheaf on `C`, let `F'` be an abelian sheaf on `C'`
> and let `t : F' ⟶ g⁻¹F` be a map of abelian sheaves. The canonical map `Lπ'_!(F') ⟶ Lπ_!(F)` is the
> identification `Lπ'_! = Lπ_! ∘ Lg_!` followed by `Lπ_!` applied to the composite of the comparison
> `Lg_!(F') ⟶ g_!F'` with the adjoint `g_!F' ⟶ F` of `t`.

```lean
def canonicalDerivedLowerShriekMap (h : S.AbelianLowerShriekAcyclic)
    (hp : S.TotalAbelianLowerShriekAcyclic) (hp' : S.SourceAbelianLowerShriekAcyclic)
    (F : Sheaf S.totalTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂})
    (F' : Sheaf S.sourceTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂})
    (t : F' ⟶ S.abelianInverseImage.obj F) :
    S.derivedSourceAbelianLowerShriek.obj ((DerivedCategory.singleFunctor
        (Sheaf S.sourceTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂}) 0).obj F') ⟶
      S.derivedTotalAbelianLowerShriek.obj ((DerivedCategory.singleFunctor
        (Sheaf S.totalTopology AddCommGrpCat.{max w u₀ u₁ u₂ v₀ v₁ v₂}) 0).obj F)
```

## Tag 08PE, a lemma

[Tag 08PE](https://stacks.math.columbia.edu/tag/08PE) in the Stacks Project.

**`Stacks.Sites.FibredCategory.fiberwiseColimitFormula`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/LowerShriekAsAFibrewiseColimit.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/LowerShriekAsAFibrewiseColimit.lean#L333).

> **Stacks 08PE.** The lower shriek of an abelian sheaf along the projection of a fibred
> category is the sheaf associated to the presheaf of fibrewise colimits, with restriction maps
> induced by the chosen cartesian lifts.

```lean
def fiberwiseColimitFormula
    [HasWeakSheafify s.base.J AddCommGrpCat.{max w uD vD uC vC}] :
    FiberwiseColimitFormula s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.38, Tag 08RV](https://stacks.math.columbia.edu/tag/08RV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isCoherentOnSomeFlatSpaceChart_of_isCoherentOnNoetherianSpaceCharts, AlgebraicGeometry.Stack.isQuasicoherentFiniteTypeModule_of_isFinitePresentationOnSite, AlgebraicGeometry.Stack.tfae_coherenceConditions, AlgebraicGeometry.Stack.IsCoherent, AlgebraicGeometry.Stack.coherentModules, AlgebraicGeometry.Stack.isCoherentModule_unit, AlgebraicGeometry.Stack.isCoherentModule_of_isFiniteLocallyFreeOnSite, AlgebraicGeometry.Stack.isCoherentModule_of_isInvertible
statement: formalized
proof: formalized
---

# 103.17 Coherent sheaves on locally Noetherian stacks

Section 103.17 of the Stacks Project, [Tag 0GR4](https://stacks.math.columbia.edu/tag/0GR4). 9 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GR5, a lemma

[Tag 0GR5](https://stacks.math.columbia.edu/tag/0GR5) in the Stacks Project.

**`AlgebraicGeometry.Stack.isCoherentOnSomeFlatSpaceChart_of_isCoherentOnNoetherianSpaceCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherenceChartConditions.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherenceChartConditions.lean#L167). The attribute's comment: “condition (3) implies condition (4)”.

> **Stacks 0GR5, the implication (3) ⟹ (4).**  Let `𝒳` be a locally Noetherian algebraic stack
> and `ℱ` a module on its big fppf site which is quasi-coherent and whose restriction to the small
> étale site of every locally Noetherian algebraic-space chart is coherent.  Then there is one
> chart which is locally of finite type, flat and surjective and on which the restriction is
> coherent.
>
> The chart is produced by **Stacks 04YF**: local Noetherianity of `𝒳` in the form of
> `AlgebraicGeometry.Stack.HasPropertyOnSomeSchemeAtlas` gives, by
> `AlgebraicGeometry.Stack.exists_scheme_atlas_iff_exists_space_atlas`, a smooth surjective
> 1-morphism from the algebraic stack of an algebraic space with the étale-local property of local
> Noetherianity.  A smooth 1-morphism of algebraic stacks is flat by
> `AlgebraicGeometry.Stack.AlgebraicStacks.isFlat_of_isSmooth` and locally of finite type by
> `AlgebraicGeometry.Stack.AlgebraicStacks.isLocallyOfFiniteType_of_isSmooth`, so that chart is of
> the kind condition (4) asks for, and condition (3) applied to it supplies the coherence.

```lean
theorem isCoherentOnSomeFlatSpaceChart_of_isCoherentOnNoetherianSpaceCharts
    (𝒳 : AlgebraicStacks.{u, t} B S hS)
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    (M : SheafOfModules.{m} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl))
    (hM : IsCoherentOnNoetherianSpaceCharts.{u, m, t} B S hS 𝒳 M) :
    IsCoherentOnSomeFlatSpaceChart.{u, m, t} B S hS 𝒳 M
```

**`AlgebraicGeometry.Stack.isQuasicoherentFiniteTypeModule_of_isFinitePresentationOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherenceConditions.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherenceConditions.lean#L64). The attribute's comment: “condition (2) implies condition (1)”.

> On a locally Noetherian algebraic stack a module of finite presentation on the big fppf site is
> quasi-coherent and of finite type.

```lean
theorem isQuasicoherentFiniteTypeModule_of_isFinitePresentationOnSite
    (𝒳 : AlgebraicStacks.{u, t} B S hS)
    (_h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    (M : SheafOfModules.{m} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl))
    (hM : M.IsFinitePresentationOnSite) :
    IsQuasicoherentFiniteTypeModule B S hS 𝒳 M
```

**`AlgebraicGeometry.Stack.tfae_coherenceConditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherenceConditionsEquivalence.lean, line 439](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherenceConditionsEquivalence.lean#L439).

> **Stacks 0GR5.**  Let `𝒳` be a locally Noetherian algebraic stack and `ℱ` an `𝒪_𝒳`-module.
> The following are equivalent:
>
> 1. `ℱ` is a quasi-coherent, finite type `𝒪_𝒳`-module;
> 2. `ℱ` is an `𝒪_𝒳`-module of finite presentation;
> 3. `ℱ` is quasi-coherent and for any morphism `f : U ⟶ 𝒳` where `U` is a locally Noetherian
>    algebraic space, the pullback `f^*ℱ|_{U_étale}` is coherent;
> 4. `ℱ` is quasi-coherent and there exists an algebraic space `U` and a morphism `f : U ⟶ 𝒳` which
>    is locally of finite type, flat, and surjective, such that the pullback `f^*ℱ|_{U_étale}` is
>    coherent.
>
> Local Noetherianity of `𝒳` is the smooth scheme atlas criterion of Stacks 04YG.

```lean
theorem tfae_coherenceConditions (𝒳 : AlgebraicStacks.{u, t} B S hS)
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    (M : SheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl)) :
    [IsQuasicoherentFiniteTypeModule B S hS 𝒳 M, M.IsFinitePresentationOnSite,
      IsCoherentOnNoetherianSpaceCharts.{u, u, t} B S hS 𝒳 M,
      IsCoherentOnSomeFlatSpaceChart.{u, u, t} B S hS 𝒳 M].TFAE
```

## Tag 0GR6, a definition

[Tag 0GR6](https://stacks.math.columbia.edu/tag/0GR6) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentModules.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentModules.lean#L98). The attribute's comment: “coherence, as conditions (1) and (2) of Stacks 0GR5 jointly”.

> **Stacks 0GR6.**  A module on the big fppf site of an algebraic stack `𝒳` is *coherent* when
> it satisfies the conditions of Stacks 0GR5: it is quasi-coherent of finite type, condition (1),
> and of finite presentation, condition (2).

```lean
def IsCoherent (𝒳 : AlgebraicStacks.{u, t} B S hS)
    (M : SheafOfModules.{m} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl)) : Prop
```

**`AlgebraicGeometry.Stack.coherentModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentModules.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentModules.lean#L138). The attribute's comment: “the category Coh(O\_X) of coherent modules”.

> **Stacks 0GR6.**  The category `Coh(𝒪_𝒳)` of coherent modules on an algebraic stack `𝒳`: the
> full subcategory of the `𝒪_𝒳`-modules on the big fppf site of `𝒳` cut out by
> `AlgebraicGeometry.Stack.IsCoherent`.

```lean
def coherentModules (𝒳 : AlgebraicStacks.{u, t} B S hS) :
    ObjectProperty (SheafOfModules.{m} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl))
```

## Tag 0GR7, a lemma

[Tag 0GR7](https://stacks.math.columbia.edu/tag/0GR7) in the Stacks Project.

**`AlgebraicGeometry.Stack.isCoherentModule_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentLocallyNoetherian.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentLocallyNoetherian.lean#L327). The attribute's comment: “the structure sheaf of the stack is coherent”.

> **Stacks 0GR7, the structure-sheaf clause.**  On a locally Noetherian algebraic stack the
> module `𝒪_𝒳` is coherent: on any site the structure sheaf viewed as a module over itself is the
> coproduct of one copy of itself, hence of finite presentation.
>
> Local Noetherianity is the hypothesis of the source and is not used; see the module
> documentation.

```lean
theorem isCoherentModule_unit (𝒳 : AlgebraicStacks.{u, t} B S hS)
    (_h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳) :
    IsCoherentModule B S hS 𝒳 (SheafOfModules.unit _)
```

**`AlgebraicGeometry.Stack.isCoherentModule_of_isFiniteLocallyFreeOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentLocallyNoetherian.lean, line 339](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentLocallyNoetherian.lean#L339). The attribute's comment: “finite locally free modules on the stack are coherent”.

> **Stacks 0GR7, the finite locally free clause.**  On a locally Noetherian algebraic stack
> every finite locally free `𝒪_𝒳`-module is coherent: the covering witnessing finite local freeness
> already carries a finite global presentation on each of its members.
>
> Local Noetherianity is the hypothesis of the source and is not used.

```lean
theorem isCoherentModule_of_isFiniteLocallyFreeOnSite (𝒳 : AlgebraicStacks.{u, t} B S hS)
    (_h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    (M : SheafOfModules.{m} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl))
    (hM : M.IsFiniteLocallyFreeOnSite) :
    IsCoherentModule B S hS 𝒳 M
```

**`AlgebraicGeometry.Stack.isCoherentModule_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/InvertibleCoherent.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/InvertibleCoherent.lean#L148). The attribute's comment: “invertible modules on the stack are coherent”.

> On a locally Noetherian algebraic stack every invertible `𝒪_𝒳`-module is coherent.

```lean
theorem isCoherentModule_of_isInvertible (𝒳 : AlgebraicStacks.{u, t} B S hS)
    (_h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    (M : SheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl))
    (hM : Stacks.SheafOfModules.IsInvertible
      (structureSheaf B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids B.topology le_rfl).obj
      (ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
        B.topology le_rfl).property M) :
    IsCoherentModule B S hS 𝒳 M
```

## Tag 0GR8, a lemma

[Tag 0GR8](https://stacks.math.columbia.edu/tag/0GR8) in the Stacks Project.

**`AlgebraicGeometry.Stack.isCoherent_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentModules.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentModules.lean#L188).

> **Stacks 0GR8.**  For a 1-morphism `f : 𝒳 ⟶ 𝒴` of locally Noetherian algebraic stacks, the
> inverse image `f^*` sends coherent modules on `𝒴` to coherent modules on `𝒳`.
>
> Coherence is that of Stacks 0GR6, `AlgebraicGeometry.Stack.IsCoherent`, which on a locally
> Noetherian stack is equivalent to each of the four conditions of Stacks 0GR5.  As in the source,
> the proof goes through finite presentation: a coherent module on `𝒴` is of finite presentation,
> the inverse image along `f` preserves finite presentation
> (`AlgebraicGeometry.Stack.isFinitePresentationOnSite_modulePullback`, the case of Stacks 03DO
> needed here), and on the locally Noetherian stack `𝒳` a module of finite presentation is
> coherent.  Local Noetherianity of `𝒴` is a hypothesis of the source and is not used.
>
> The modules have sections in the universe `max (u + 1) m`, where the inverse image of modules
> along a 1-morphism of algebraic stacks is defined.

```lean
theorem isCoherent_modulePullback (𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS) (f : 𝒳 ⟶ 𝒴)
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    (h𝒴 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒴)
    (M : SheafOfModules.{max (u + 1) m} (ringStructureSheafCore B S hS 𝒴.val.val.p
      𝒴.val.isFiberedInGroupoids B.topology le_rfl))
    (hM : IsCoherent B S hS 𝒴 M) :
    IsCoherent B S hS 𝒳
      ((modulePullback B S hS 𝒳.val.val.p 𝒴.val.val.p 𝒳.val.isFiberedInGroupoids
        𝒴.val.isFiberedInGroupoids f.hom.hom.toFunctor f.hom.hom.w
        B.topology le_rfl).obj M)
```

## Tag 0GR9, a lemma

[Tag 0GR9](https://stacks.math.columbia.edu/tag/0GR9) in the Stacks Project.

**`AlgebraicGeometry.Stack.nonempty_abelian_coh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentAbelianLocallyNoetherian.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentAbelianLocallyNoetherian.lean#L154). The attribute's comment: “the category Coh(O\_X) of coherent modules (Stacks 0GR6) on a locally Noetherian algebraic stack is abelian, with kernels Q(Ker φ) and cokernels computed in Mod(O\_X)”.

> The category of coherent `𝒪_𝒳`-modules is abelian, for a locally Noetherian algebraic stack
> `𝒳`. Its kernels are the `Q(Ker φ)` and its cokernels are computed in
> `Mod(𝒪_𝒳)` (`AlgebraicGeometry.Stack.FlatFppf.relKernelData_coherentModules`).

```lean
theorem nonempty_abelian_coh
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳) :
    Nonempty (Abelian (Coh.{u, u, w} B S hS 𝒳))
```

**`AlgebraicGeometry.Stack.preservesFiniteLimits_preservesFiniteColimits_coh_qcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentAbelianLocallyNoetherian.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentAbelianLocallyNoetherian.lean#L163). The attribute's comment: “the inclusion functor Coh(O\_X) → QCoh(O\_X) is exact”.

> The inclusion `Coh(𝒪_𝒳) → QCoh(𝒪_𝒳)` is exact, for a locally Noetherian algebraic stack `𝒳`:
> it preserves finite limits and finite colimits. Here `QCoh(𝒪_𝒳)` is the full subcategory of
> `Mod(𝒪_𝒳)` of the quasi-coherent modules.

```lean
theorem preservesFiniteLimits_preservesFiniteColimits_coh_qcoh
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳) :
    PreservesFiniteLimits
        (ObjectProperty.ιOfLE (FlatFppf.relKernelData_coherentModules h𝒳).le) ∧
      PreservesFiniteColimits
        (ObjectProperty.ιOfLE (FlatFppf.relKernelData_coherentModules h𝒳).le)
```

**`AlgebraicGeometry.Stack.isCoherent_coherator_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentAbelianLocallyNoetherian.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentAbelianLocallyNoetherian.lean#L226). The attribute's comment: “part (2), corrected reading: the image computed in Mod(O\_X) need not be coherent (exists\_not\_isCoherent\_image\_of\_isCoherent); Q(Im φ) is coherent and is the image of φ in Coh(O\_X)”.

> Let `φ : ℱ ⟶ 𝒢` be a map of coherent modules on a locally Noetherian algebraic stack and
> `Im φ = Ker(𝒢 ⟶ Coker φ)` its image computed in `Mod(𝒪_𝒳)`. Then `Q(Im φ)` is coherent and
> `Q(Im φ) ⟶ Im φ ⟶ 𝒢` is the image of `φ` in `Coh(𝒪_𝒳)`, i.e. a kernel in `Coh(𝒪_𝒳)` of the cokernel
> `𝒢 ⟶ Coker φ`, which is coherent.
>
> `Im φ` itself need not be coherent
> (`AlgebraicGeometry.Stack.exists_not_isCoherent_image_of_isCoherent`).

```lean
theorem isCoherent_coherator_image
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F G : _root_.SheafOfModules.{u} (FlatFppf.ambientRingStructureSheaf B S hS 𝒳)}
    (hF : IsCoherent B S hS 𝒳 F) (hG : IsCoherent B S hS 𝒳 G) (φ : F ⟶ G) :
    ∃ (hC : IsCoherent B S hS 𝒳 (cokernel φ))
      (hK : IsCoherent B S hS 𝒳 ((FlatFppf.lowerShriekInverseImageCoherator B S hS 𝒳).obj
        (kernel (cokernel.π φ)))),
      Nonempty (IsLimit (KernelFork.ofι
        (f := ((coherentModules.{u, u, w} B S hS 𝒳).homMk (cokernel.π φ) :
          (⟨G, hG⟩ : Coh B S hS 𝒳) ⟶ ⟨cokernel φ, hC⟩))
        ((coherentModules.{u, u, w} B S hS 𝒳).homMk
          ((FlatFppf.coheratorCounit B S hS 𝒳).app (kernel (cokernel.π φ)) ≫
            kernel.ι (cokernel.π φ)) : (⟨_, hK⟩ : Coh B S hS 𝒳) ⟶ ⟨G, hG⟩)
        (by ext1; exact (FlatFppf.isRelKernel_coherator_kernel B S hS 𝒳 (cokernel.π φ)).1)))
```

**`AlgebraicGeometry.Stack.isCoherent_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentCokernelLocallyNoetherian.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentCokernelLocallyNoetherian.lean#L135). The attribute's comment: “part (1): the cokernel computed in Mod(O\_X) of a map of coherent modules (Stacks 0GR6) is coherent”.

> **Stacks 0GR9, part (1).**  Let `𝒳` be a locally Noetherian algebraic stack and `φ : ℱ ⟶ 𝒢` a
> map of coherent `𝒪_𝒳`-modules.  The cokernel of `φ` computed in `Mod(𝒪_𝒳)` is a coherent
> `𝒪_𝒳`-module.
>
> Coherence is `AlgebraicGeometry.Stack.IsCoherent`, the reading of Stacks 0GR6 as the conjunction
> of the conditions (1) and (2) of Stacks 0GR5 this library states.  On a locally Noetherian
> algebraic stack that conjunction is condition (2) alone, by
> `AlgebraicGeometry.Stack.isCoherent_iff_isCoherentModule`, so the clause is
> `AlgebraicGeometry.Stack.isCoherentModule_cokernel`; local Noetherianity is used, in that
> reduction.

```lean
theorem isCoherent_cokernel
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F G : SheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl)}
    (hF : IsCoherent B S hS 𝒳 F) (hG : IsCoherent B S hS 𝒳 G) (φ : F ⟶ G) :
    IsCoherent B S hS 𝒳 (cokernel φ)
```

**`AlgebraicGeometry.Stack.kernel_mem_lqcohFbc_and_isCoherent_coherator_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentKernelLocallyQuasicoherentFlatBaseChange.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentKernelLocallyQuasicoherentFlatBaseChange.lean#L137). The attribute's comment: “part (3): the kernel Ker(φ) computed in Mod(O\_X) of a map of coherent modules is in LQCoh^fbc(O\_X) -- locally quasi-coherent and with the flat base change property, the latter read with the inverse image of sheaves of modules as in the source -- and Q(Ker φ) is coherent and is the kernel of φ in Coh(O\_X)”.

> Let `𝒳` be a locally Noetherian algebraic stack and `φ : ℱ ⟶ 𝒢` a map of coherent
> `𝒪_𝒳`-modules, and let `Ker φ` be its kernel computed in `Mod(𝒪_𝒳)`. Then
>
> * `Ker φ` is in `LQCoh^fbc(𝒪_𝒳)`: read as an étale sheaf of modules, it is locally
>   quasi-coherent (Stacks 06WJ) and has the flat base change property (Stacks 0762, with the
>   inverse image of sheaves of modules on the small étale sites); and
> * `Q(Ker φ)` is coherent and `Q(Ker φ) ⟶ Ker φ ⟶ ℱ` is a kernel of `φ` in `Coh(𝒪_𝒳)`.
>
> Here `Q = g_!g^{-1}` with its counit is the coherator: composing with `Q(K) ⟶ K` is a bijection on
> maps out of quasi-coherent modules
> (`AlgebraicGeometry.Stack.FlatFppf.bijective_comp_coheratorCounit`). The source's remark that
> `Ker φ` may not be coherent is not part of the assertion. The small étale sites are those of a
> big étale site `E` with the same cutoff as the big fppf site `B`.

```lean
theorem kernel_mem_lqcohFbc_and_isCoherent_coherator_kernel
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F G : _root_.SheafOfModules.{u} (FlatFppf.ambientRingStructureSheaf B S hS 𝒳)}
    (hF : IsCoherent B S hS 𝒳 F) (hG : IsCoherent B S hS 𝒳 G) (φ : F ⟶ G) :
    (IsLocallyQuasicoherent B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids (kernel φ).val ∧
      HasFlatBaseChangePropertySheafUnivLE.{u, u + 1, u, u} B E h S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids
        (etaleModuleOfFppf B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids (kernel φ))) ∧
    ∃ hK : IsCoherent B S hS 𝒳
        ((FlatFppf.lowerShriekInverseImageCoherator B S hS 𝒳).obj (kernel φ)),
      Nonempty (IsLimit (KernelFork.ofι
        (f := ((coherentModules.{u, u, w} B S hS 𝒳).homMk φ : (⟨F, hF⟩ : Coh B S hS 𝒳) ⟶ ⟨G, hG⟩))
        ((coherentModules.{u, u, w} B S hS 𝒳).homMk
          ((FlatFppf.coheratorCounit B S hS 𝒳).app (kernel φ) ≫ kernel.ι φ) :
            (⟨_, hK⟩ : Coh B S hS 𝒳) ⟶ ⟨F, hF⟩)
        (by ext1; exact (FlatFppf.isRelKernel_coherator_kernel B S hS 𝒳 φ).1)))
```

## Tag 0GRA, a lemma

[Tag 0GRA](https://stacks.math.columbia.edu/tag/0GRA) in the Stacks Project.

**`AlgebraicGeometry.Stack.isCoherent_X₂_of_kernel_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentExtensionLocallyNoetherian.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentExtensionLocallyNoetherian.lean#L154). The attribute's comment: “extensions of coherent modules, exactness as a kernel fork and a cokernel cofork”.

> **Stacks 0GRA.**  Let `𝒳` be a locally Noetherian algebraic stack, let `φ : ℱ₁ ⟶ ℱ₂` be a
> kernel of `ψ : ℱ₂ ⟶ ℱ₃` and let `ℱ₃` be a cokernel of `φ` along `ψ`.  If `ℱ₁` and `ℱ₃` are
> coherent then so is `ℱ₂`.
>
> Coherence is `AlgebraicGeometry.Stack.IsCoherent`, the notion of Stacks 0GR6.  On a locally
> Noetherian algebraic stack it is finite presentation on the big fppf site, condition (2) of
> Stacks 0GR5, by `AlgebraicGeometry.Stack.isCoherent_iff_isCoherentModule`, which is where local
> Noetherianity of `𝒳` enters; the content is then that finite presentation on a ringed site is
> closed under extensions.  The exactness is given as a kernel fork and a cokernel cofork, so
> nothing is assumed about the category of `𝒪_𝒳`-modules.

```lean
public theorem isCoherent_X₂_of_kernel_cokernel
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F₁ F₂ F₃ : SheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl)}
    {φ : F₁ ⟶ F₂} {ψ : F₂ ⟶ F₃} (hz : φ ≫ ψ = 0)
    (hφ : IsLimit (KernelFork.ofι φ hz)) (hψ : IsColimit (CokernelCofork.ofπ ψ hz))
    (h₁ : IsCoherent B S hS 𝒳 F₁) (h₃ : IsCoherent B S hS 𝒳 F₃) :
    IsCoherent B S hS 𝒳 F₂
```

## Tag 0GRB, a lemma

[Tag 0GRB](https://stacks.math.columbia.edu/tag/0GRB) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasicoherentFiniteTypeModule_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryLocallyNoetherian.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryLocallyNoetherian.lean#L260). The attribute's comment: “part (1): a quotient of a coherent module by a surjection of quasi-coherent modules is coherent”.

> **Stacks 0GRB, part (1).**  Let `𝒳` be a locally Noetherian algebraic stack and let
> `φ : ℱ ⟶ 𝒢` be a surjective map of quasi-coherent `𝒪_𝒳`-modules.  If `ℱ` is coherent then so
> is `𝒢`.
>
> Coherence is condition (1) of Stacks 0GR5, that the module be quasi-coherent and of finite type;
> see the module documentation.  Quasi-coherence of `𝒢` is the hypothesis of the source, which
> takes `φ` to be a map of quasi-coherent modules, and what is proved is that `𝒢` is of finite
> type: the condition 03DL(5) is inherited by quotients over an arbitrary ringed site.
> Surjectivity is `CategoryTheory.Epi`, which for a morphism of sheaves of modules is local
> surjectivity, by `Stacks.SheafOfModules.EpiMono.epi_iff_isLocallySurjective`.  Local
> Noetherianity is the hypothesis of the source and is not used.

```lean
theorem isQuasicoherentFiniteTypeModule_of_epi
    (_h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS
      (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F G : SheafOfModules.{m} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl)}
    (φ : F ⟶ G) [Epi φ]
    (hF : IsQuasicoherentFiniteTypeModule B S hS 𝒳 F)
    (hG : G.IsQuasicoherentOnSite) :
    IsQuasicoherentFiniteTypeModule B S hS 𝒳 G
```

**`AlgebraicGeometry.Stack.FlatFppf.isCoherent_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean#L465). The attribute's comment: “part (1): if F is coherent and φ : F → G is a surjection of quasi-coherent modules then G is coherent”.

> **Stacks 0GRB, part (1).** Let `𝒳` be a locally Noetherian algebraic stack and
> `φ : ℱ ⟶ 𝒢` a surjective map of quasi-coherent `𝒪_𝒳`-modules. If `ℱ` is coherent, so is `𝒢`.
>
> Surjectivity is `CategoryTheory.Epi` in `Mod(𝒪_𝒳)`, i.e. local surjectivity; an epimorphism of
> `QCoh(𝒪_𝒳)` is one of `Mod(𝒪_𝒳)` (`AlgebraicGeometry.Stack.FlatFppf.epi_hom_of_epi_qcoh`), so
> this is also the statement for surjections in `QCoh(𝒪_𝒳)`. Coherence is
> `AlgebraicGeometry.Stack.IsCoherent` (Stacks 0GR6). Finite type passes to quotients and, on a
> locally Noetherian stack, a quasi-coherent module of finite type is coherent (Stacks 0GR5).

```lean
theorem isCoherent_of_epi
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F G : _root_.SheafOfModules.{u} (ambientRingStructureSheaf B S hS 𝒳)} (φ : F ⟶ G) [Epi φ]
    (hF : IsCoherent B S hS 𝒳 F) (hG : G.IsQuasicoherentOnSite) :
    IsCoherent B S hS 𝒳 G
```

**`AlgebraicGeometry.Stack.isSerreClass_coh_qcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean, line 556](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean#L556). The attribute's comment: “Coh(O\_X) is a Serre subcategory of QCoh(O\_X)”.

> **Stacks 0GRB: `Coh(𝒪_𝒳)` is a Serre subcategory of `QCoh(𝒪_𝒳)`**, for a locally
> Noetherian algebraic stack `𝒳`. Here `QCoh(𝒪_𝒳)` is the full subcategory of the quasi-coherent
> `𝒪_𝒳`-modules on the big fppf site, with the abelian structure
> `AlgebraicGeometry.Stack.FlatFppf.abelianQCoh` (its kernels are the `Q(Ker φ)`, its cokernels are
> computed in `Mod(𝒪_𝒳)`), and `Coh(𝒪_𝒳)` is cut out by `AlgebraicGeometry.Stack.IsCoherent`
> (Stacks 0GR6). `CategoryTheory.ObjectProperty.IsSerreClass` is the Serre-subcategory condition:
> a coherent zero object, and closure under subobjects, quotients and extensions in `QCoh(𝒪_𝒳)`.

```lean
theorem isSerreClass_coh_qcoh
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳) :
    letI := FlatFppf.abelianQCoh 𝒳
    (FlatFppf.cohInQCoh 𝒳).IsSerreClass
```

**`AlgebraicGeometry.Stack.isCoherent_image_qcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean#L580). The attribute's comment: “part (2): if F is coherent then the image of φ : F → G in QCoh(O\_X) is coherent; the image computed in Mod(O\_X) need not be quasi-coherent (exists\_not\_isCoherent\_image\_of\_isCoherent)”.

> **Stacks 0GRB, part (2).** Let `𝒳` be a locally Noetherian algebraic stack and
> `φ : ℱ ⟶ 𝒢` a map of quasi-coherent `𝒪_𝒳`-modules with `ℱ` coherent. Then the image of `φ` is
> coherent.
>
> The image is the image of `φ` in the abelian category `QCoh(𝒪_𝒳)`
> (`AlgebraicGeometry.Stack.FlatFppf.abelianQCoh`), which is the reading of Stacks 0GQL (2) the
> source's Remark sets up; it is a quotient of `ℱ` in `QCoh(𝒪_𝒳)`. The image computed in
> `Mod(𝒪_𝒳)` need not be quasi-coherent, already for `2 : 𝒪 ⟶ 𝒪` on `Spec ℤ`
> (`AlgebraicGeometry.Stack.exists_not_isCoherent_image_of_isCoherent`), so it is not the object of
> the clause.

```lean
theorem isCoherent_image_qcoh
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F G : (FlatFppf.qcohModules 𝒳).FullSubcategory} (φ : F ⟶ G)
    (hF : IsCoherent B S hS 𝒳 F.obj) :
    letI := FlatFppf.abelianQCoh 𝒳
    IsCoherent B S hS 𝒳 (Limits.image φ).obj
```

**`AlgebraicGeometry.Stack.isCoherent_of_isParasitic_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean, line 601](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean#L601). The attribute's comment: “part (3): if G is coherent and Ker(φ), computed in Mod(O\_X), is parasitic, then F is coherent”.

> **Stacks 0GRB, part (3).** Let `𝒳` be a locally Noetherian algebraic stack and
> `φ : ℱ ⟶ 𝒢` a map of quasi-coherent `𝒪_𝒳`-modules. If `𝒢` is coherent and `Ker(φ)` is parasitic
> (Stacks 0773), then `ℱ` is coherent.
>
> Here `Ker(φ)` is the kernel computed in `Mod(𝒪_𝒳)`, as in Stacks 0GR9 and 0GQL. The variant with
> the kernel taken in `QCoh(𝒪_𝒳)` is `AlgebraicGeometry.Stack.isCoherent_of_isParasitic_kernel_qcoh`.
> On sections over a flat object the map `φ` is injective, its kernel there vanishing; so over a
> flat object lying over a Noetherian affine scheme the sections of `ℱ` form a submodule of a finite
> module, which suffices on a locally Noetherian stack
> (`AlgebraicGeometry.Stack.FlatFppf.isCoherent_of_moduleFinite_sections`).

```lean
theorem isCoherent_of_isParasitic_kernel
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F G : _root_.SheafOfModules.{u} (FlatFppf.ambientRingStructureSheaf B S hS 𝒳)}
    (hF : F.IsQuasicoherentOnSite) (φ : F ⟶ G) (hG : IsCoherent B S hS 𝒳 G)
    (hK : IsParasitic B S hS 𝒳 .fppf (kernel φ).val) :
    IsCoherent B S hS 𝒳 F
```

**`AlgebraicGeometry.Stack.isCoherent_of_isParasitic_kernel_qcoh`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean, line 621](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentSerreSubcategoryQuasicoherent.lean#L621). The attribute's comment: “part (3), the kernel read in QCoh(O\_X): if G is coherent and the kernel of φ in QCoh(O\_X) is parasitic, then F is coherent”.

> **Stacks 0GRB, part (3), with the kernel taken in `QCoh(𝒪_𝒳)`.** Let `𝒳` be a locally
> Noetherian algebraic stack and `φ : ℱ ⟶ 𝒢` a map of quasi-coherent `𝒪_𝒳`-modules. If `𝒢` is
> coherent and the kernel of `φ` in the abelian category `QCoh(𝒪_𝒳)`
> (`AlgebraicGeometry.Stack.FlatFppf.abelianQCoh`, kernel `Q(Ker φ)`) is parasitic, then `ℱ` is
> coherent.

```lean
theorem isCoherent_of_isParasitic_kernel_qcoh
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F G : (FlatFppf.qcohModules 𝒳).FullSubcategory} (φ : F ⟶ G)
    (hG : IsCoherent B S hS 𝒳 G.obj) :
    letI := FlatFppf.abelianQCoh 𝒳
    IsParasitic B S hS 𝒳 .fppf (kernel φ).obj.val → IsCoherent B S hS 𝒳 F.obj
```

## Tag 0GRC, a lemma

[Tag 0GRC](https://stacks.math.columbia.edu/tag/0GRC) in the Stacks Project.

**`AlgebraicGeometry.Stack.SelfIntersection.coherentFlatPresentationEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/CoherentFlatPresentationEquivalence.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/CoherentFlatPresentationEquivalence.lean#L245).

> **Stacks 0GRC.** Let `𝒳` be a locally Noetherian algebraic stack, let `U` be an algebraic
> space and let `f : U → 𝒳` be surjective, locally of finite presentation and flat.  Let
> `(U, R, s, t, c)` be the groupoid in algebraic spaces of Stacks 04T4, `R` representing
> `U ×_𝒳 U`.  Then the equivalence `QCoh(𝒪_𝒳) ≅ QCoh(𝒪_{[U/R]}) ≅ QCoh(U, R, s, t, c)` of Sheaves
> on Stacks, Section 06WU, and Stacks 06WT
> (`AlgebraicGeometry.Stack.SelfIntersection.quasicoherentFlatPresentationEquivalence`) sends
> coherent modules to coherent modules and vice versa, i.e. induces an equivalence
> `Coh(𝒪_𝒳) ≅ Coh(U, R, s, t, c)`.
>
> `Coh(𝒪_𝒳)` is the category of coherent modules of Stacks 0GR6 and `Coh(U, R, s, t, c)` that of
> Groupoids in Spaces, Section 0GPN.  The equivalence is the restriction of
> `quasicoherentFlatPresentationEquivalence` to these full subcategories, by
> `AlgebraicGeometry.Stack.coherentPresentationEquivalence`.

```lean
noncomputable def coherentFlatPresentationEquivalence
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    (hlfp : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f)
    (hflat : AlgebraicStacks.IsFlat B S hS f) (hsurj : IsSurjective B S hS f) :
    Coh.{u, u, t} B S hS 𝒳 ≌
      Space.QuasicoherentModule.Coh B S hS (flatPresentationGroupoid B S hS 𝒳 F hF f)
```

## Tag 0GRD, a lemma

[Tag 0GRD](https://stacks.math.columbia.edu/tag/0GRD) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.isCoherent_coheratorInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorInternalHomCoherent.lean, line 521](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorInternalHomCoherent.lean#L521). The attribute's comment: “for a locally Noetherian algebraic stack and coherent F, G, the module hom(F, G) = Q(Hom(F, G)) of Stacks 0GQN is coherent”.

> Let `𝒳` be a locally Noetherian algebraic stack and `ℱ`, `𝒢` coherent `𝒪_𝒳`-modules. Then the
> internal hom `hom(ℱ, 𝒢) = Q(𝓗om_{𝒪_𝒳}(ℱ, 𝒢))` is a coherent `𝒪_𝒳`-module.

```lean
theorem isCoherent_coheratorInternalHom
    (h𝒳 : HasPropertyOnSomeSchemeAtlas B S hS (fun T : Scheme.{u} ↦ IsLocallyNoetherian T) 𝒳)
    {F G : _root_.SheafOfModules.{u} (ambientRingStructureSheaf B S hS 𝒳)}
    (hF : IsCoherent B S hS 𝒳 F) (hG : IsCoherent B S hS 𝒳 G) :
    IsCoherent B S hS 𝒳 (coheratorInternalHom B S hS 𝒳 F G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.17, Tag 0GR4](https://stacks.math.columbia.edu/tag/0GR4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

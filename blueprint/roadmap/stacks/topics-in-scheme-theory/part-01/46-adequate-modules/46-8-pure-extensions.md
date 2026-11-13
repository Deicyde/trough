---
declaration: section
origin: cited
lean: Module.PureInjective, Module.PureProjective, Module.pureProjective_iff_directSum_finitelyPresented_retract, Module.exists_pureProjective_universallyExact_presentation, Module.characterModule_pureInjective, Module.pureInjective_iff_evalₗ_splits, Module.exists_pureInjective_universallyExact_extension, Module.universallyInjective_range_subtype
statement: formalized
proof: formalized
---

# 46.8 Pure extensions

Section 46.8 of the Stacks Project, [Tag 06ZX](https://stacks.math.columbia.edu/tag/06ZX). 9 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06ZY, a definition

[Tag 06ZY](https://stacks.math.columbia.edu/tag/06ZY) in the Stacks Project.

**`Module.PureInjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Defs.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Defs.lean#L29). The attribute's comment: “pure\_injective”.

> An `A`-module `I` is *pure injective* if applying `Hom_A(-, I)` to every
> universally exact short exact sequence of `A`-modules gives a short exact
> sequence.

```lean
public abbrev PureInjective (A : Type u) [CommRing A] (I : Type v)
    [AddCommGroup I] [Module A I] : Prop
```

**`Module.PureProjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Defs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Defs.lean#L51). The attribute's comment: “pure\_projective”.

> An `A`-module `P` is *pure projective* if applying `Hom_A(P, -)` to every
> universally exact short exact sequence of `A`-modules gives a short exact
> sequence.

```lean
public abbrev PureProjective (A : Type u) [CommRing A] (P : Type v)
    [AddCommGroup P] [Module A P] : Prop
```

## Tag 06ZZ, a lemma

[Tag 06ZZ](https://stacks.math.columbia.edu/tag/06ZZ) in the Stacks Project.

**`Module.pureProjective_iff_directSum_finitelyPresented_retract`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Projective.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Projective.lean#L246). The attribute's comment: “pure\_projective\_characterization”.

> An `A`-module is pure projective if and only if it is a retract of a direct
> sum of finitely presented `A`-modules.

```lean
public theorem pureProjective_iff_directSum_finitelyPresented_retract
    (A : Type u) [CommRing A] (M : Type v) [AddCommGroup M] [Module A M] :
    Module.PureProjective A M ↔
      ∃ (ι : Type (max u v)) (Q : ι → Type (max u v))
        (_ : (i : ι) → AddCommGroup (Q i))
        (_ : (i : ι) → Module A (Q i)),
        (∀ i, Module.FinitePresentation A (Q i)) ∧
          ∃ (s : M →ₗ[A] ⨁ i, Q i) (r : (⨁ i, Q i) →ₗ[A] M),
            r.comp s = LinearMap.id
```

**`Module.exists_pureProjective_universallyExact_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Projective.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Projective.lean#L296). The attribute's comment: “pure\_projective\_presentation”.

> Every module is the quotient of a pure projective module in a universally exact short
> exact sequence.

```lean
public theorem exists_pureProjective_universallyExact_presentation
    (A : Type u) [CommRing A] (M : Type v) [AddCommGroup M] [Module A M] :
    ∃ (N P : Type (max u v))
      (_ : AddCommGroup N) (_ : Module A N)
      (_ : AddCommGroup P) (_ : Module A P)
      (f : N →ₗ[A] P) (g : P →ₗ[A] M),
      Function.Injective f ∧
        Function.Surjective g ∧
          LinearMap.range f = LinearMap.ker g ∧
            UniversallyInjective f ∧
              Module.PureProjective A P
```

## Tag 0700, a lemma

[Tag 0700](https://stacks.math.columbia.edu/tag/0700) in the Stacks Project.

**`Module.characterModule_pureInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Injective.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Injective.lean#L75). The attribute's comment: “character\_module\_pure\_injective”.

> The character module `Hom_ℤ(M, ℚ/ℤ)` of any module `M` over a commutative ring is pure
> injective.

```lean
public theorem characterModule_pureInjective (A : Type u) [CommRing A]
    (M : Type v) [AddCommGroup M] [Module A M] :
    Module.PureInjective A (CharacterModule M)
```

**`Module.pureInjective_iff_evalₗ_splits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Injective.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Injective.lean#L130). The attribute's comment: “pure\_injective\_iff\_double\_dual\_splits”.

> A module is pure injective if and only if evaluation into its double character
> module has a linear retraction.

```lean
public theorem pureInjective_iff_evalₗ_splits (A : Type u) [CommRing A]
    (I : Type v) [AddCommGroup I] [Module A I] :
    Module.PureInjective A I ↔
      ∃ r : CharacterModule (CharacterModule I) →ₗ[A] I,
        r.comp (CharacterModule.evalₗ A I) = LinearMap.id
```

**`Module.exists_pureInjective_universallyExact_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Injective.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Injective.lean#L153). The attribute's comment: “exists\_pure\_injective\_universally\_exact\_extension”.

> Every module embeds universally injectively into a pure injective module, with a
> surjective cokernel map making the resulting sequence exact.

```lean
public theorem exists_pureInjective_universallyExact_extension
    (A : Type u) [CommRing A] (M : Type v) [AddCommGroup M] [Module A M] :
    ∃ (I N : Type v)
      (_ : AddCommGroup I) (_ : Module A I)
      (_ : AddCommGroup N) (_ : Module A N)
      (f : M →ₗ[A] I) (g : I →ₗ[A] N),
      Function.Injective f ∧
        Function.Surjective g ∧
          LinearMap.range f = LinearMap.ker g ∧
            UniversallyInjective f ∧ Module.PureInjective A I
```

## Tag 0701, a lemma

[Tag 0701](https://stacks.math.columbia.edu/tag/0701) in the Stacks Project.

**`Module.universallyInjective_range_subtype`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Injective.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Injective.lean#L200). The attribute's comment: “part (1)”.

> If `L → M → N` is exact and remains exact after every tensor product, then the
> inclusion of the image of `M → N` in `N` is universally injective.

```lean
theorem universallyInjective_range_subtype
    {L M N : Type v} [AddCommGroup L] [AddCommGroup M] [AddCommGroup N]
    [Module A L] [Module A M] [Module A N]
    (f : L →ₗ[A] M) (g : M →ₗ[A] N)
    (hexact : Function.Exact f g)
    (h : ∀ (Q : Type v) [AddCommGroup Q] [Module A Q],
      Function.Exact (f.rTensor Q) (g.rTensor Q)) :
    UniversallyInjective (LinearMap.range g).subtype
```

**`Module.kernel_universallyExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Injective.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Injective.lean#L215). The attribute's comment: “part (2)”.

> The kernel-to-term-to-next-kernel sequences of a universally exact complex are
> universally exact short exact sequences.

```lean
theorem kernel_universallyExact
    {M : ℤ → Type u} [∀ i, AddCommGroup (M i)] [∀ i, Module A (M i)]
    (d : ∀ i, M i →ₗ[A] M (i + 1)) (h : UniversallyExactComplex M d) (i : ℤ) :
    UniversallyExact (LinearMap.ker (d i)).subtype (toNextKernel d h i)
```

## Tag 0702, a definition

[Tag 0702](https://stacks.math.columbia.edu/tag/0702) in the Stacks Project.

**`Module.PureInjectiveResolution.IsPureInjectiveResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/InjectiveResolution.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/InjectiveResolution.lean#L37). The attribute's comment: “pure\_injective\_resolution”.

> An augmentation `M ⟶ I⁰` of a cochain complex is a *pure injective resolution* if
> `0 ⟶ M ⟶ I⁰ ⟶ I¹ ⟶ ⋯` is universally exact and every `Iⁱ` is pure injective.

```lean
public structure IsPureInjectiveResolution
    {M : Type v} [AddCommGroup M] [Module A M]
    (I : CochainComplex (ModuleCat.{v} A) ℕ) (augmentation : M →ₗ[A] I.X 0) : Prop
```

**`Module.PureProjectiveResolution.IsPureProjectiveResolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/ProjectiveResolution.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/ProjectiveResolution.lean#L38). The attribute's comment: “pure\_projective\_resolution”.

> An augmentation `P₀ ⟶ M` of a chain complex is a *pure projective resolution* if
> `⋯ ⟶ P₁ ⟶ P₀ ⟶ M ⟶ 0` is universally exact and every `Pᵢ` is pure projective.

```lean
public structure IsPureProjectiveResolution
    {M : Type v} [AddCommGroup M] [Module A M]
    (P : ChainComplex (ModuleCat.{w} A) ℕ) (augmentation : P.X 0 →ₗ[A] M) : Prop
```

## Tag 0703, a lemma

[Tag 0703](https://stacks.math.columbia.edu/tag/0703) in the Stacks Project.

**`Module.PureProjectiveResolution.exists_comparison_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/ProjectiveResolution.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/ProjectiveResolution.lean#L265). The attribute's comment: “comparison\_map”.

> A module map extends from a pure projective resolution to any universally
> exact resolution.

```lean
public theorem exists_comparison_map
    {M N : Type v} [AddCommGroup M] [Module A M] [AddCommGroup N] [Module A N]
    (f : M →ₗ[A] N)
    (P C : ChainComplex (ModuleCat.{v} A) ℕ)
    (aP : P.X 0 →ₗ[A] M) (aC : C.X 0 →ₗ[A] N)
    (hP : Module.PureProjectiveResolution.IsPureProjectiveResolution P aP)
    (hC : IsUniversallyExactResolution C aC) :
    ∃ F : P ⟶ C, aC.comp (F.f 0).hom = f.comp aP
```

**`Module.PureProjectiveResolution.homotopy_of_same_augmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/ProjectiveResolution.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/ProjectiveResolution.lean#L333). The attribute's comment: “homotopy\_uniqueness”.

> Two maps of resolutions inducing the same map of resolved modules are homotopic.

```lean
public theorem homotopy_of_same_augmentation
    {M N : Type v} [AddCommGroup M] [Module A M] [AddCommGroup N] [Module A N]
    (P C : ChainComplex (ModuleCat.{v} A) ℕ)
    (augmentationP : P.X 0 →ₗ[A] M) (augmentationC : C.X 0 →ₗ[A] N)
    (hP : Module.PureProjectiveResolution.IsPureProjectiveResolution P augmentationP)
    (hC : Module.PureProjectiveResolution.IsUniversallyExactResolution C augmentationC)
    (f : M →ₗ[A] N) (α β : P ⟶ C)
    (hα : augmentationC.comp (α.f 0).hom = f.comp augmentationP)
    (hβ : augmentationC.comp (β.f 0).hom = f.comp augmentationP) :
    Nonempty (Homotopy α β)
```

**`Module.PureProjectiveResolution.exists_isPureProjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/ResolutionExistence.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/ResolutionExistence.lean#L169). The attribute's comment: “existence”.

> Every module admits a pure projective resolution.

```lean
public theorem exists_isPureProjectiveResolution :
    ∃ (P : ChainComplex (ModuleCat.{max u v} A) ℕ) (augmentation : P.X 0 →ₗ[A] M),
      IsPureProjectiveResolution P augmentation
```

## Tag 0704, a lemma

[Tag 0704](https://stacks.math.columbia.edu/tag/0704) in the Stacks Project.

**`Module.PureInjectiveResolution.exists_comparison_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/InjectiveResolution.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/InjectiveResolution.lean#L225). The attribute's comment: “comparison\_map”.

> A map `M → N` extends to a map from any universally exact resolution of `M`
> to any pure injective resolution of `N`.

```lean
public theorem exists_comparison_map
    {M N : Type v} [AddCommGroup M] [Module A M] [AddCommGroup N] [Module A N]
    (f : M →ₗ[A] N)
    (C I : CochainComplex (ModuleCat.{v} A) ℕ)
    (aC : M →ₗ[A] C.X 0) (aI : N →ₗ[A] I.X 0)
    (hC : IsUniversallyExactResolution C aC)
    (hI : Module.PureInjectiveResolution.IsPureInjectiveResolution I aI) :
    ∃ F : C ⟶ I, (F.f 0).hom.comp aC = aI.comp f
```

**`Module.PureInjectiveResolution.homotopy_of_same_augmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/InjectiveResolution.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/InjectiveResolution.lean#L332). The attribute's comment: “comparison\_homotopy”.

> Comparison maps extending the same map between resolved modules are homotopic.

```lean
public theorem homotopy_of_same_augmentation
    {M N : Type v} [AddCommGroup M] [Module A M] [AddCommGroup N] [Module A N]
    (C I : CochainComplex (ModuleCat.{v} A) ℕ)
    (augmentationC : M →ₗ[A] C.X 0) (augmentationI : N →ₗ[A] I.X 0)
    (hC : Module.PureInjectiveResolution.IsUniversallyExactResolution C augmentationC)
    (hI : Module.PureInjectiveResolution.IsPureInjectiveResolution I augmentationI)
    (f : M →ₗ[A] N) (α β : C ⟶ I)
    (hα : (α.f 0).hom.comp augmentationC = augmentationI.comp f)
    (hβ : (β.f 0).hom.comp augmentationC = augmentationI.comp f) :
    Nonempty (Homotopy α β)
```

**`Module.PureInjectiveResolution.exists_pureInjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/InjectiveResolution.lean, line 447](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/InjectiveResolution.lean#L447). The attribute's comment: “existence”.

> Every module admits an augmented, universally exact cochain complex of pure injectives.

```lean
public theorem exists_pureInjectiveResolution
    (A : Type u) [CommRing A] (M : Type v) [AddCommGroup M] [Module A M] :
    ∃ (I : CochainComplex (ModuleCat.{v} A) ℕ) (augmentation : M →ₗ[A] I.X 0),
      Module.PureInjectiveResolution.IsPureInjectiveResolution I augmentation
```

## Tag 0705, a definition

[Tag 0705](https://stacks.math.columbia.edu/tag/0705) in the Stacks Project.

**`Module.pureExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Ext.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Ext.lean#L60).

> The `i`th pure extension module of `M` by `N`.

```lean
public noncomputable def pureExt (M N : Type v) [AddCommGroup M] [Module A M]
    [AddCommGroup N] [Module A N] (i : ℕ) : ModuleCat.{v} A
```

## Tag 0706, a lemma

[Tag 0706](https://stacks.math.columbia.edu/tag/0706) in the Stacks Project.

**`Module.pureExt_isZero_of_pureInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Ext.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Ext.lean#L381). The attribute's comment: “pure\_injective\_vanishing”.

> Positive-degree pure extensions into a pure injective module vanish.

```lean
public theorem pureExt_isZero_of_pureInjective
    (M N : Type v) [AddCommGroup M] [Module A M]
    [AddCommGroup N] [Module A N]
    (hN : Module.PureInjective A N)
    (i : ℕ) (hi : 0 < i) :
    CategoryTheory.Limits.IsZero (Module.pureExt (A := A) M N i)
```

**`Module.pureExt_isZero_of_pureProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Ext.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Ext.lean#L463). The attribute's comment: “pure\_projective\_vanishing”.

> Positive-degree pure extensions out of a pure projective module vanish.

```lean
public theorem pureExt_isZero_of_pureProjective
    (M N : Type (max u v)) [AddCommGroup M] [Module A M]
    [AddCommGroup N] [Module A N]
    (hM : Module.PureProjective A M)
    (i : ℕ) (hi : 0 < i) :
    CategoryTheory.Limits.IsZero (Module.pureExt (A := A) M N i)
```

**`Module.pureExt_isZero_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/Ext.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/Ext.lean#L477). The attribute's comment: “finite\_presentation\_vanishing”.

> Positive-degree pure extensions out of a module of finite presentation vanish.

```lean
public theorem pureExt_isZero_of_finitePresentation
    (M N : Type (max u v)) [AddCommGroup M] [Module A M]
    [AddCommGroup N] [Module A N] [Module.FinitePresentation A M]
    (i : ℕ) (hi : 0 < i) :
    CategoryTheory.Limits.IsZero (Module.pureExt (A := A) M N i)
```

**`Module.pureExtIsoHomologyOfPureProjectiveResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Pure/ExtResolution.lean, line 664](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Pure/ExtResolution.lean#L664). The attribute's comment: “pure\_projective\_resolution”.

> **Pure extensions are computed by a pure projective resolution of the first variable**:
> `Pext^i_A(M, N)` is the `i`th cohomology module of `Hom_A(Pᐧ, N)` for every pure projective
> resolution `Pᐧ ⟶ M`.

```lean
public noncomputable def pureExtIsoHomologyOfPureProjectiveResolution
    (M N : Type (max u v)) [AddCommGroup M] [Module A M] [AddCommGroup N] [Module A N]
    {P : ChainComplex (ModuleCat.{max u v} A) ℕ} {ε : P.X 0 →ₗ[A] M}
    (hP : Module.PureProjectiveResolution.IsPureProjectiveResolution P ε) (i : ℕ) :
    Module.pureExt (A := A) M N i ≅ (Module.homComplexOfChain P N).homology i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 46.8, Tag 06ZX](https://stacks.math.columbia.edu/tag/06ZX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

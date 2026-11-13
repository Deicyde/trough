---
declaration: section
origin: cited
lean: AlgebraicGeometry.isProperOver_iff_exists_isProper, AlgebraicGeometry.exists_isProper_iff_forall_isProper, AlgebraicGeometry.IsProperOver, AlgebraicGeometry.isProperOver_of_le, AlgebraicGeometry.isProperOver_preimage_baseChange, AlgebraicGeometry.isClosed_image_of_isProperOver, AlgebraicGeometry.isProperOver_image, AlgebraicGeometry.isProperOver_preimage
statement: formalized
proof: formalized
---

# 30.26 Being proper over a base

Section 30.26 of the Stacks Project, [Tag 0CYK](https://stacks.math.columbia.edu/tag/0CYK). 11 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CYL, a lemma

[Tag 0CYL](https://stacks.math.columbia.edu/tag/0CYL) in the Stacks Project.

**`AlgebraicGeometry.isProperOver_iff_exists_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean#L136). The attribute's comment: “parts (1) and (2)”. References: EGA II (5.4.10), “indep. of subscheme”.

> **Stacks 0CYL, parts (1) and (2).** The reduced closed subscheme on `Z` is proper over `S`
> exactly when some closed subscheme structure on `Z` is proper over `S`.

```lean
public theorem isProperOver_iff_exists_isProper :
    IsProperOver f Z ↔ ∃ I : X.IdealSheafData, I.support = Z ∧ IsProper (I.subschemeι ≫ f)
```

**`AlgebraicGeometry.exists_isProper_iff_forall_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean#L148). The attribute's comment: “parts (2) and (3)”. References: EGA II (5.4.10), “indep. of subscheme”.

> **Stacks 0CYL, parts (2) and (3).** If one closed subscheme structure on `Z` is proper over
> `S`, then every closed subscheme structure on `Z` is proper over `S`.

```lean
public theorem exists_isProper_iff_forall_isProper :
    (∃ I : X.IdealSheafData, I.support = Z ∧ IsProper (I.subschemeι ≫ f)) ↔
      ∀ I : X.IdealSheafData, I.support = Z → IsProper (I.subschemeι ≫ f)
```

## Tag 0CYM, a definition

[Tag 0CYM](https://stacks.math.columbia.edu/tag/0CYM) in the Stacks Project.

**`AlgebraicGeometry.IsProperOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean#L82).

> **Stacks 0CYM.** A closed subset `Z` of `X` is proper over `S` if its reduced induced closed
> subscheme is proper over `S`.

```lean
public abbrev IsProperOver {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (Z : Closeds X) : Prop
```

## Tag 0CYN, a lemma

[Tag 0CYN](https://stacks.math.columbia.edu/tag/0CYN) in the Stacks Project.

**`AlgebraicGeometry.isProperOver_of_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean#L159).

> **Stacks 0CYN.** A closed subset of a closed subset proper over the base is proper over the
> base.

```lean
public theorem isProperOver_of_le {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    {Y Z : Closeds X} (hYZ : Y ≤ Z) (hZ : IsProperOver f Z) : IsProperOver f Y
```

## Tag 0CYP, a lemma

[Tag 0CYP](https://stacks.math.columbia.edu/tag/0CYP) in the Stacks Project.

**`AlgebraicGeometry.isProperOver_preimage_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean#L168).

> **Stacks 0CYP.** A closed subset proper over the base remains proper after base change.

```lean
public theorem isProperOver_preimage_baseChange {X' X S' S : Scheme.{u}}
    (g' : X' ⟶ X) (f' : X' ⟶ S') (f : X ⟶ S) (g : S' ⟶ S)
    (h : IsPullback g' f' f g) [LocallyOfFiniteType f]
    (Z : Closeds X) (hZ : IsProperOver f Z) :
    haveI : LocallyOfFiniteType f' := MorphismProperty.of_isPullback h inferInstance
    IsProperOver f' (Z.preimage g'.continuous)
```

## Tag 0CYQ, a lemma

[Tag 0CYQ](https://stacks.math.columbia.edu/tag/0CYQ) in the Stacks Project.

**`AlgebraicGeometry.isClosed_image_of_isProperOver`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/Functoriality.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/Functoriality.lean#L74). The attribute's comment: “image\_separated”. References: SGA 4 XVII (6.1.1), “Clause (i)”.

> The image of a closed subset proper over the base is closed in a separated
> scheme locally of finite type over that base.

```lean
lemma isClosed_image_of_isProperOver {X Y S : Scheme.{u}}
    (p : X ⟶ S) (g : Y ⟶ S) (f : X ⟶ Y) (hfg : f ≫ g = p)
    [LocallyOfFiniteType p] [LocallyOfFiniteType g] [IsSeparated g]
    (Z : Closeds X) (hZ : IsProperOver p Z) :
    IsClosed (f.base '' (Z : Set X))
```

**`AlgebraicGeometry.isProperOver_image`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/Functoriality.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/Functoriality.lean#L87). The attribute's comment: “image\_separated”. References: EGA II (5.4.10), “more general”.

> The image of a closed subset proper over the base is itself proper over the
> base, when the target is separated and locally of finite type.

```lean
lemma isProperOver_image {X Y S : Scheme.{u}}
    (p : X ⟶ S) (g : Y ⟶ S) (f : X ⟶ Y) (hfg : f ≫ g = p)
    [LocallyOfFiniteType p] [LocallyOfFiniteType g] [IsSeparated g]
    (Z : Closeds X) (hZ : IsProperOver p Z) :
    IsProperOver g
      ⟨f.base '' (Z : Set X), isClosed_image_of_isProperOver p g f hfg Z hZ⟩
```

**`AlgebraicGeometry.isProperOver_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/Functoriality.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/Functoriality.lean#L106). The attribute's comment: “preimage\_proper”.

> The inverse image of a closed subset proper over the base along a proper
> morphism is proper over the base.

```lean
theorem isProperOver_preimage {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [IsProper f] [LocallyOfFiniteType g] (Z : Closeds Y)
    (hZ : IsProperOver g Z) :
    IsProperOver (f ≫ g) (Z.preimage f.continuous)
```

**`AlgebraicGeometry.Scheme.Hom.closedImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean#L200). The attribute's comment: “image\_universally\_closed”.

> **Stacks 0CYQ.** The image of a closed subset under a universally closed morphism, as a
> closed subset.

```lean
public def Scheme.Hom.closedImage {X Y : Scheme.{u}} (f : X ⟶ Y) [UniversallyClosed f]
    (Z : Closeds X) : Closeds Y
```

**`AlgebraicGeometry.isProperOver_closedImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean#L207). The attribute's comment: “image\_universally\_closed”.

> **Stacks 0CYQ.** The closed image of a closed subset proper over the base is proper over the
> base.

```lean
public theorem isProperOver_closedImage {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [UniversallyClosed f] [LocallyOfFiniteType (f ≫ g)] [LocallyOfFiniteType g]
    (Z : Closeds X) (hZ : IsProperOver (f ≫ g) Z) :
    IsProperOver g (f.closedImage Z)
```

## Tag 0CYR, a lemma

[Tag 0CYR](https://stacks.math.columbia.edu/tag/0CYR) in the Stacks Project.

**`AlgebraicGeometry.isProperOver_sup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean#L261).

> **Stacks 0CYR.** The union of two closed subsets proper over the base is proper over the
> base.

```lean
public theorem isProperOver_sup {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (Z W : Closeds X) (hZ : IsProperOver f Z) (hW : IsProperOver f W) :
    IsProperOver f (Z ⊔ W)
```

**`AlgebraicGeometry.isProperOver_iSup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperClosedSubset.lean#L312).

> **Stacks 0CYR.** A finite union of closed subsets proper over the base is proper over the
> base.

```lean
public theorem isProperOver_iSup {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    {ι : Type v} [Finite ι] (Z : ι → Closeds X) (hZ : ∀ i, IsProperOver f (Z i)) :
    IsProperOver f (iSup Z)
```

## Tag 0CYS, a lemma

[Tag 0CYS](https://stacks.math.columbia.edu/tag/0CYS) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isProperOver_supp_iff_isProper_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperSupport.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperSupport.lean#L62). The attribute's comment: “conditions (1) and (2)”.

> The support of a quasi-coherent module of finite type is proper over the base if and only if
> its scheme-theoretic support is proper over the base.

```lean
public theorem isProperOver_supp_iff_isProper_schemeTheoreticSupport :
    IsProperOver f ⟨SheafOfModules.supp F, SheafOfModules.isClosed_supp F⟩ ↔
      IsProper ((schemeTheoreticSupport F).subschemeι ≫ f)
```

**`AlgebraicGeometry.Scheme.Modules.isProper_schemeTheoreticSupport_iff_exists_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperSupport.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/ProperSupport.lean#L76). The attribute's comment: “conditions (2) and (3)”.

> The scheme-theoretic support of a quasi-coherent module `F` of finite type is proper over the
> base if and only if there is a closed subscheme of `X` proper over the base carrying a
> quasi-coherent module of finite type whose direct image is `F`.

```lean
public theorem isProper_schemeTheoreticSupport_iff_exists_pushforward :
    IsProper ((schemeTheoreticSupport F).subschemeι ≫ f) ↔
      ∃ (J : X.IdealSheafData) (G : J.subscheme.Modules),
        G.IsFiniteType ∧ G.IsQuasicoherent ∧ IsProper (J.subschemeι ≫ f) ∧
          Nonempty ((Scheme.Modules.pushforward J.subschemeι).obj G ≅ F)
```

## Tag 0CYT, a lemma

[Tag 0CYT](https://stacks.math.columbia.edu/tag/0CYT) in the Stacks Project.

**`AlgebraicGeometry.isProperOver_supp_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportPullback/BaseChange.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/SupportPullback/BaseChange.lean#L47).

> In a cartesian square, base change preserves properness of the support
> of a finite type module over the base.

```lean
theorem isProperOver_supp_pullback {X' X S' S : Scheme.{u}}
    (g' : X' ⟶ X) (f' : X' ⟶ S') (f : X ⟶ S) (g : S' ⟶ S)
    (h : IsPullback g' f' f g) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsFiniteType]
    (hF : IsProperOver f ⟨SheafOfModules.supp F, SheafOfModules.isClosed_supp F⟩) :
    letI : LocallyOfFiniteType f' := MorphismProperty.of_isPullback h inferInstance
    letI : ((Scheme.Modules.pullback g').obj F).IsFiniteType :=
      SheafOfModules.pullback_isFiniteType g'.toLRSHom.toShHom F
    IsProperOver f'
      ⟨SheafOfModules.supp ((Scheme.Modules.pullback g').obj F),
        SheafOfModules.isClosed_supp _⟩
```

## Tag 0CYU, a lemma

[Tag 0CYU](https://stacks.math.columbia.edu/tag/0CYU) in the Stacks Project.

**`AlgebraicGeometry.isSerreClass_hasProperSupport_coherentModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/CoherentSerreClass.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/CoherentSerreClass.lean#L68). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0CYU, part (2).** For `f : X ⟶ S` locally of finite type with `S`
> locally Noetherian, the coherent `𝒪_X`-modules whose support is proper over `S` form a Serre
> subcategory of the abelian category of coherent `𝒪_X`-modules.
>
> The zero module has empty support, which is proper over `S`; and the support of the middle term
> of an exact sequence of coherent modules is contained in the union of the supports of the outer
> two, a union of two closed subsets proper over `S` being proper over `S`.

```lean
theorem isSerreClass_hasProperSupport_coherentModules [IsLocallyNoetherian S] :
    ObjectProperty.IsSerreClass
      (C := SheafOfModules.CoherentModules X.ringCatSheaf)
      (fun F => Stacks.Algebraization.HasProperSupport f F.obj)
```

**`AlgebraicGeometry.isProperOver_biprod_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean#L190). The attribute's comment: “sheaf\_operations”.

> The direct sum of two sheaves with proper support
> has proper support.

```lean
theorem isProperOver_biprod_support {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F G : X.Modules)
    (b : BinaryBicone F G) (hb : b.IsBilimit)
    (hF : ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp F ∧
      IsProperOver f Z))
    (hG : ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp G ∧
      IsProperOver f Z)) :
    ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp b.pt ∧
      IsProperOver f Z)
```

**`AlgebraicGeometry.isProperOver_extension_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean#L209). The attribute's comment: “sheaf\_operations”.

> A short exact extension of sheaves with proper
> support has proper support.

```lean
theorem isProperOver_extension_support {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (E : ShortComplex X.Modules) (hE : E.ShortExact)
    (hF : ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp E.X₁ ∧
      IsProperOver f Z))
    (hG : ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp E.X₃ ∧
      IsProperOver f Z)) :
    ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp E.X₂ ∧
      IsProperOver f Z)
```

**`AlgebraicGeometry.isProperOver_image_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean#L222). The attribute's comment: “sheaf\_operations”.

> The image of a morphism from a finite type sheaf with proper
> support to an arbitrary sheaf of modules has proper support.

```lean
theorem isProperOver_image_support {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F G : X.Modules)
    [F.IsFiniteType]
    (u : F ⟶ G)
    (hF : ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp F ∧
      IsProperOver f Z)) :
    ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp (Abelian.image u) ∧
      IsProperOver f Z)
```

**`AlgebraicGeometry.isProperOver_cokernel_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean#L236). The attribute's comment: “sheaf\_operations”.

> The cokernel of a morphism from an arbitrary sheaf of modules to a finite type
> sheaf with proper support has proper support.

```lean
theorem isProperOver_cokernel_support {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F G : X.Modules)
    [G.IsFiniteType]
    (u : F ⟶ G)
    (hG : ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp G ∧
      IsProperOver f Z)) :
    ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp (cokernel u) ∧
      IsProperOver f Z)
```

**`AlgebraicGeometry.isProperOver_quotient_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Cohomology/ProperOverBase/ModuleSupport.lean#L249). The attribute's comment: “sheaf\_operations”.

> A quotient of a finite type sheaf with proper
> support has proper support.

```lean
theorem isProperOver_quotient_support {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (F Q : X.Modules)
    [F.IsFiniteType]
    (q : F ⟶ Q) [Epi q]
    (hF : ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp F ∧
      IsProperOver f Z)) :
    ∃ Z : Closeds X, ((Z : Set X) = SheafOfModules.supp Q ∧
      IsProperOver f Z)
```

## Tag 08DS, a lemma

[Tag 08DS](https://stacks.math.columbia.edu/tag/08DS) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProperSupportCoherent.isCoherent_higherDirectImage_of_properSupp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/Unconditional.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperSupportCoherent/Unconditional.lean#L60).

> Let `S` be locally Noetherian, let `f : X ⟶ S` be locally of finite type and let `F` be a
> quasi-coherent `𝒪_X`-module of finite type whose support is proper over `S`. Then the higher
> direct image `R ᵖ f_* F` is a coherent `𝒪_S`-module in every degree.

```lean
theorem isCoherent_higherDirectImage_of_properSupp
    (hF : IsProperOver f ⟨SheafOfModules.supp F, SheafOfModules.isClosed_supp F⟩) (p : ℤ) :
    (((Scheme.Modules.pushforward f).rightDerivedPlus p).obj F).IsCoherent
```

## Tag 0CYV, a lemma

[Tag 0CYV](https://stacks.math.columbia.edu/tag/0CYV) in the Stacks Project.

**`Stacks.Coherent.isSerreClass_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/ProperSerreClass.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/ProperSerreClass.lean#L421). The attribute's comment: “proper support”.

> **[Stacks, Tag 0CYV], part (1).** The coherent adic systems along `ℐ` whose first term has
> support proper over `S` form a Serre subcategory of `Coh(X, ℐ)`.
>
> All terms of a coherent adic system have the same support, and the support of the middle term of a
> short exact sequence is the union of the supports of the outer two, which is proper over `S`
> because a finite union of closed subsets proper over the base is proper over the base.

```lean
public theorem isSerreClass_hasProperSupport {X S : Scheme.{u}} [IsNoetherian S] (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (I : X.IdealSheafData) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    letI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    letI : IsNoetherian X := AlgebraicGeometry.IsNoetherian.mk
    ObjectProperty.IsSerreClass (C := CoherentAdicSystems I)
      (fun F => Stacks.Algebraization.HasProperSupport f (F.obj.obj (op 0)))
```

**`Stacks.Coherent.isSerreClass_hasProperAnnihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/ProperSerreClass.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalGeometry/ProperSerreClass.lean#L471). The attribute's comment: “common proper annihilator”.

> **[Stacks, Tag 0CYV], part (2).** The coherent adic systems along `ℐ` admitting a closed
> subscheme of `X` proper over `S` whose ideal sheaf annihilates every term form a Serre subcategory
> of `Coh(X, ℐ)`.
>
> An ideal sheaf annihilating every term of a system annihilates every term of a subobject and of a
> quotient; for an extension the product of the two ideal sheaves works, and the closed subset it
> cuts out is the union of the two, which is again proper over `S`.

```lean
public theorem isSerreClass_hasProperAnnihilator {X S : Scheme.{u}} [IsNoetherian S] (f : X ⟶ S)
    [LocallyOfFiniteType f] [QuasiCompact f] (I : X.IdealSheafData) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian f
    letI : CompactSpace X := QuasiCompact.compactSpace_of_compactSpace f
    letI : IsNoetherian X := AlgebraicGeometry.IsNoetherian.mk
    (HasProperAnnihilator f I).IsSerreClass
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 30.26, Tag 0CYK](https://stacks.math.columbia.edu/tag/0CYK)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

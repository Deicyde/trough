---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.flatBaseChangeQuasicoherator, AlgebraicGeometry.Stack.flatBaseChangeQuasicoheratorAdjunction, AlgebraicGeometry.Stack.flatBaseChangeQuasicoheratorCompInclusionIsoId, AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoherator, AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoheratorAdjunction, AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoheratorCompIso, AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoheratorAdjunctionAndCompIso, AlgebraicGeometry.Stack.AlgebraicStacks.isZero_coherator_obj_iff_isParasitic
statement: formalized
proof: formalized
---

# 103.10 Quasi-coherent modules

Section 103.10 of the Stacks Project, [Tag 0777](https://stacks.math.columbia.edu/tag/0777). 9 tags here are carried by 54 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0778, a lemma

[Tag 0778](https://stacks.math.columbia.edu/tag/0778) in the Stacks Project.

**`AlgebraicGeometry.Stack.flatBaseChangeQuasicoherator`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean#L257). The attribute's comment: “the right adjoint Q : LQCoh^fbc(𝒪\_𝒳) ⥤ QCoh(𝒪\_𝒳)”.

> **The coherator on `LQCoh^fbc(𝒪_𝒳)`.** The right adjoint of the inclusion
> `i : QCoh(𝒪_𝒳) → LQCoh^fbc(𝒪_𝒳)`: it sends a locally quasi-coherent module with the flat base
> change property to the terminal quasi-coherent module equipped with a map to it.

```lean
def flatBaseChangeQuasicoherator
    (hinc : ∀ F : FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp,
      IsLocallyQuasicoherentWithFlatBaseChange B E h S hS p hp
        ((FibredSite.toSiteModules.{u, u + 1, u, u} B S hS p hp .etale).obj F).val)
    (hclosed : SheafOfModules.ClosedUnderColimitsOfSize.{u, u + 1, u, u, u}
      (FibredSite.ringStructureSheafCore B S hS p hp .fppf))
    (hpres : PreservesColimitsOfSize.{u, u} (quasicoherentToFlatBaseChange B E h S hS p hp hinc))
    (hls : LocallySmall.{u} (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hlsD : LocallySmall.{u}
      (locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS p hp))
    (hwp : WellPowered.{u} (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp)ᵒᵖ)
    (hsep : HasSeparator (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp)) :
    locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS p hp ⥤
      FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp
```

**`AlgebraicGeometry.Stack.flatBaseChangeQuasicoheratorAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean#L279). The attribute's comment: “the adjunction between the inclusion and the right adjoint”.

> **The coherator on `LQCoh^fbc(𝒪_𝒳)` is right adjoint to the inclusion.** The adjunction is
> the universal property of the terminal objects the coherator is built from.

```lean
def flatBaseChangeQuasicoheratorAdjunction
    (hinc : ∀ F : FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp,
      IsLocallyQuasicoherentWithFlatBaseChange B E h S hS p hp
        ((FibredSite.toSiteModules.{u, u + 1, u, u} B S hS p hp .etale).obj F).val)
    (hclosed : SheafOfModules.ClosedUnderColimitsOfSize.{u, u + 1, u, u, u}
      (FibredSite.ringStructureSheafCore B S hS p hp .fppf))
    (hpres : PreservesColimitsOfSize.{u, u} (quasicoherentToFlatBaseChange B E h S hS p hp hinc))
    (hls : LocallySmall.{u} (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hlsD : LocallySmall.{u}
      (locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS p hp))
    (hwp : WellPowered.{u} (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp)ᵒᵖ)
    (hsep : HasSeparator (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp)) :
    quasicoherentToFlatBaseChange B E h S hS p hp hinc ⊣
      flatBaseChangeQuasicoherator B E h S hS p hp hinc hclosed hpres hls hlsD hwp hsep
```

**`AlgebraicGeometry.Stack.flatBaseChangeQuasicoheratorCompInclusionIsoId`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/Coherator.lean#L301). The attribute's comment: “the composite of the right adjoint with the inclusion is the identity functor”.

> **`Q ∘ i` is the identity functor** of `QCoh(𝒪_𝒳)`, for the coherator `Q` on
> `LQCoh^fbc(𝒪_𝒳)` and the inclusion `i`.

```lean
def flatBaseChangeQuasicoheratorCompInclusionIsoId
    (hinc : ∀ F : FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp,
      IsLocallyQuasicoherentWithFlatBaseChange B E h S hS p hp
        ((FibredSite.toSiteModules.{u, u + 1, u, u} B S hS p hp .etale).obj F).val)
    (hclosed : SheafOfModules.ClosedUnderColimitsOfSize.{u, u + 1, u, u, u}
      (FibredSite.ringStructureSheafCore B S hS p hp .fppf))
    (hpres : PreservesColimitsOfSize.{u, u} (quasicoherentToFlatBaseChange B E h S hS p hp hinc))
    (hls : LocallySmall.{u} (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp))
    (hlsD : LocallySmall.{u}
      (locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS p hp))
    (hwp : WellPowered.{u} (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp)ᵒᵖ)
    (hsep : HasSeparator (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp)) :
    quasicoherentToFlatBaseChange B E h S hS p hp hinc ⋙
        flatBaseChangeQuasicoherator B E h S hS p hp hinc hclosed hpres hls hlsD hwp hsep ≅
      𝟭 (FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoherator`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeCoherator.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeCoherator.lean#L68). The attribute's comment: “the right adjoint Q : LQCoh^fbc(𝒪\_𝒳) ⥤ QCoh(𝒪\_𝒳) of the inclusion”.

> **Stacks 0778: the right adjoint `Q : LQCoh^fbc(𝒪_𝒳) ⥤ QCoh(𝒪_𝒳)`.**

```lean
abbrev lqcohFbcCoherator :
    (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).FullSubcategory ⥤
      quasicoherentModules B S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoheratorAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeCoherator.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeCoherator.lean#L75). The attribute's comment: “the inclusion QCoh(𝒪\_𝒳) → LQCoh^fbc(𝒪\_𝒳) is left adjoint to Q”.

> **Stacks 0778: `Q` is right adjoint to the inclusion `i`.**

```lean
def lqcohFbcCoheratorAdjunction :
    quasicoherentToLqcohFbc B E h S hS 𝒳 ⊣ lqcohFbcCoherator B E h S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoheratorCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeCoherator.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeCoherator.lean#L81). The attribute's comment: “Q ∘ i is the identity functor”.

> **Stacks 0778: `Q ∘ i` is the identity functor of `QCoh(𝒪_𝒳)`.**

```lean
def lqcohFbcCoheratorCompIso :
    quasicoherentToLqcohFbc B E h S hS 𝒳 ⋙ lqcohFbcCoherator B E h S hS 𝒳 ≅
      𝟭 (quasicoherentModules B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoheratorAdjunctionAndCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeCoherator.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeCoherator.lean#L90). The attribute's comment: “the whole statement: i has a right adjoint Q, and Q ∘ i is the identity”.

> **Stacks 0778, the whole statement.**  For an algebraic stack `𝒳`, the inclusion
> `i : QCoh(𝒪_𝒳) ⥤ LQCoh^fbc(𝒪_𝒳)` has the right adjoint `Q`, and `Q ∘ i` is the identity functor
> of `QCoh(𝒪_𝒳)`.

```lean
def lqcohFbcCoheratorAdjunctionAndCompIso :
    (quasicoherentToLqcohFbc B E h S hS 𝒳 ⊣ lqcohFbcCoherator B E h S hS 𝒳) ×
      (quasicoherentToLqcohFbc B E h S hS 𝒳 ⋙ lqcohFbcCoherator B E h S hS 𝒳 ≅
        𝟭 (quasicoherentModules B S hS 𝒳))
```

## Tag 0779, a lemma

[Tag 0779](https://stacks.math.columbia.edu/tag/0779) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isZero_coherator_obj_iff_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L94). The attribute's comment: “part (1): the kernel of Q on LQCoh^fbc(𝒪\_𝒳) is exactly its parasitic objects”.

> **Stacks 0779** (1). An object of `LQCoh^fbc(𝒪_𝒳)` is killed by the coherator
> `Q : Mod(𝒪_𝒳) → QCoh(𝒪_𝒳)` of **Stacks 0778** exactly when it is parasitic: the kernel of `Q` on
> `LQCoh^fbc(𝒪_𝒳)` is exactly the collection of its parasitic objects.

```lean
theorem isZero_coherator_obj_iff_isParasitic (F : Stack.fppfModules B S hS 𝒳)
    (hF : lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 F) :
    IsZero ((coherator B S hS 𝒳).obj F) ↔ IsParasitic B S hS 𝒳 .fppf F.val
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isParasitic_kernel_and_cokernel_coheratorAdjunction_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L103). The attribute's comment: “part (2): the kernel and the cokernel of the adjunction map Q(F) → F are parasitic, for F in LQCoh^fbc(𝒪\_𝒳)”.

> **Stacks 0779** (2). For `𝓕` in `LQCoh^fbc(𝒪_𝒳)` both the kernel and the cokernel of the
> adjunction map `Q(𝓕) ⟶ 𝓕` are parasitic.

```lean
theorem isParasitic_kernel_and_cokernel_coheratorAdjunction_counit
    (F : Stack.fppfModules B S hS 𝒳) (hF : lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 F) :
    IsParasitic B S hS 𝒳 .fppf (kernel ((coheratorAdjunction B S hS 𝒳).counit.app F)).val ∧
      IsParasitic B S hS 𝒳 .fppf
        (cokernel ((coheratorAdjunction B S hS 𝒳).counit.app F)).val
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.preservesLimitsOfSize_lqcohSheafFbc_ι_comp_coherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L148). The attribute's comment: “part (3): Q on LQCoh^fbc(𝒪\_𝒳) commutes with all limits”.

> **Stacks 0779** (3), limits: the coherator `Q : LQCoh^fbc(𝒪_𝒳) → QCoh(𝒪_𝒳)` commutes with all
> limits, being right adjoint to the inclusion `QCoh(𝒪_𝒳) → LQCoh^fbc(𝒪_𝒳)`.

```lean
theorem preservesLimitsOfSize_lqcohSheafFbc_ι_comp_coherator :
    PreservesLimitsOfSize.{u, u}
      ((lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι ⋙ coherator B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.preservesColimitsOfShape_lqcohSheafFbc_ι_comp_coherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L156). The attribute's comment: “part (3): Q on LQCoh^fbc(𝒪\_𝒳) commutes with all colimits”.

> **Stacks 0779** (3), colimits: the coherator `Q : LQCoh^fbc(𝒪_𝒳) → QCoh(𝒪_𝒳)` commutes with
> all colimits of `u`-small shapes, which are computed in `Mod(𝒪_𝒳)`.

```lean
theorem preservesColimitsOfShape_lqcohSheafFbc_ι_comp_coherator (J : Type u) [Category.{u} J] :
    PreservesColimitsOfShape J
      ((lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι ⋙ coherator B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.preservesFiniteLimits_and_preservesFiniteColimits_lqcohSheafFbc_ι_comp_coherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L164). The attribute's comment: “part (3): Q is exact on LQCoh^fbc(𝒪\_𝒳)”.

> **Stacks 0779** (3), exactness: the coherator `Q : LQCoh^fbc(𝒪_𝒳) → QCoh(𝒪_𝒳)` is exact, it
> preserves finite limits and finite colimits.

```lean
theorem preservesFiniteLimits_and_preservesFiniteColimits_lqcohSheafFbc_ι_comp_coherator :
    PreservesFiniteLimits
        ((lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι ⋙ coherator B S hS 𝒳) ∧
      PreservesFiniteColimits
        ((lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι ⋙ coherator B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.preservesLimitsOfSize_flatBaseChangeQuasicoherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean#L231). The attribute's comment: “part (3): Q commutes with all limits”.

> **Stacks 0779, part (3): the coherator commutes with all limits.**  This is the one
> assertion of **Stacks 0779** which needs nothing beyond the adjunction of **Stacks 0778**: `Q`
> is a right adjoint, and a right adjoint preserves all limits.

```lean
theorem preservesLimitsOfSize_flatBaseChangeQuasicoherator :
    PreservesLimitsOfSize.{vJ, uJ}
      (flatBaseChangeQuasicoherator B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
        hinc hclosed hpres hls hlsD hwp hsep)
```

**`AlgebraicGeometry.Stack.isZero_flatBaseChangeQuasicoherator_iff_isParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean#L279). The attribute's comment: “part (1): the kernel of Q is exactly the parasitic objects, in both directions, over the chart data of the construction of Stacks 0778”.

> **Stacks 0779, part (1).**  An object `𝓕` of `LQCoh^fbc(𝒪_𝒳)` is in the kernel of the
> coherator `Q` of **Stacks 0778** if and only if it is parasitic (**Stacks 0773**).  Both
> directions are proved: the statement is an equality of the two collections.
>
> The counit of the adjunction identifies `r (i (Q 𝓕))` with `r 𝓕`, and `i ⋙ r` is an
> equivalence and so reflects zero objects; so `Q 𝓕 = 0` if and only if `r 𝓕 = 0`, which by
> `hrpar` is the parasitic condition.  Here `r` stands for the restriction `𝓕 ↦ 𝓕|_{U_étale}`
> along a smooth surjective chart `f : U → 𝒳`, through which the source computes `Q`; see the
> module documentation for the three hypotheses it carries and for **Stacks 06WT**, which
> `hreq` names.

```lean
theorem isZero_flatBaseChangeQuasicoherator_iff_isParasitic
    (F : locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids) :
    IsZero ((flatBaseChangeQuasicoherator B E h S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids hinc hclosed hpres hls hlsD hwp hsep).obj F) ↔
      IsParasitic.{u, w, u} B S hS 𝒳 .etale F.obj.val
```

**`AlgebraicGeometry.Stack.preservesColimitsOfSize_flatBaseChangeQuasicoherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean#L301). The attribute's comment: “part (3): Q commutes with all colimits, over the chart data of the construction of Stacks 0778”.

> **Stacks 0779, part (3): the coherator commutes with all colimits.**  The source does
> *not* get this from adjointness — a right adjoint need not preserve colimits.  It gets it from
> the explicit construction: by exactness it suffices to treat direct sums (**Stacks 002P**), and
> restriction to `U_étale` commutes with direct sums.
>
> Here that is the hypothesis `hrcolim` on `r`, carried through the identification
> `Q ≅ r ⋙ (i ⋙ r)⁻¹` which the counit and `hreq` supply; the inverse of an equivalence
> preserves all colimits.

```lean
theorem preservesColimitsOfSize_flatBaseChangeQuasicoherator
    (hrcolim : PreservesColimitsOfSize.{vJ, uJ} r) :
    PreservesColimitsOfSize.{vJ, uJ}
      (flatBaseChangeQuasicoherator B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
        hinc hclosed hpres hls hlsD hwp hsep)
```

**`AlgebraicGeometry.Stack.exact_flatBaseChangeQuasicoherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean#L338). The attribute's comment: “part (3): Q is exact, over the chart data of the construction of Stacks 0778”.

> **Stacks 0779, part (3): the coherator is exact.**  Exactness of an additive functor
> between abelian categories is the preservation of finite limits and of finite colimits.  The
> first half is `AlgebraicGeometry.Stack.preservesFiniteLimits_flatBaseChangeQuasicoherator`,
> which holds because `Q` is a right adjoint; the second is
> `AlgebraicGeometry.Stack.preservesFiniteColimits_flatBaseChangeQuasicoherator`, which needs the
> chart data.

```lean
theorem exact_flatBaseChangeQuasicoherator (hrfincolim : PreservesFiniteColimits r) :
    PreservesFiniteLimits
        (flatBaseChangeQuasicoherator B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
          hinc hclosed hpres hls hlsD hwp hsep) ∧
      PreservesFiniteColimits
        (flatBaseChangeQuasicoherator B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
          hinc hclosed hpres hls hlsD hwp hsep)
```

**`AlgebraicGeometry.Stack.isParasitic_of_isLimit_kernelFork_flatBaseChangeQuasicoherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean#L360). The attribute's comment: “part (2), the kernel: the kernel of the adjunction map Q(F) ⟶ F is parasitic”.

> **Stacks 0779, part (2), the kernel.**  The kernel of the adjunction map `Q 𝓕 ⟶ 𝓕` is
> parasitic.
>
> The left adjoint `i` is fully faithful, so `Q` applied to the counit is invertible, in
> particular a monomorphism; `Q` preserves the kernel fork, being a right adjoint; so the kernel
> is in the kernel of `Q` and therefore parasitic by part (1).  The kernel is taken as an
> arbitrary limit kernel fork, so that nothing is assumed about `LQCoh^fbc(𝒪_𝒳)` having kernels
> (**Stacks 0771** part (2)).

```lean
theorem isParasitic_of_isLimit_kernelFork_flatBaseChangeQuasicoherator
    {F : locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids}
    {c : KernelFork ((flatBaseChangeQuasicoheratorAdjunction B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids hinc hclosed hpres hls hlsD hwp hsep).counit.app F)}
    (hc : IsLimit c) : IsParasitic.{u, w, u} B S hS 𝒳 .etale c.pt.obj.val
```

**`AlgebraicGeometry.Stack.isParasitic_of_isColimit_cokernelCofork_flatBaseChangeQuasicoherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorParasiticKernel.lean#L385). The attribute's comment: “part (2), the cokernel: the cokernel of the adjunction map Q(F) ⟶ F is parasitic”.

> **Stacks 0779, part (2), the cokernel.**  The cokernel of the adjunction map `Q 𝓕 ⟶ 𝓕` is
> parasitic.
>
> `Q` applied to the counit is invertible, in particular an epimorphism; `Q` is right exact by
> part (3) and so preserves the cokernel cofork; so the cokernel is in the kernel of `Q` and
> therefore parasitic by part (1).  As for the kernel, the cokernel is taken as an arbitrary
> colimit cokernel cofork.

```lean
theorem isParasitic_of_isColimit_cokernelCofork_flatBaseChangeQuasicoherator
    (hrfincolim : PreservesFiniteColimits r)
    {F : locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids}
    {c : CokernelCofork ((flatBaseChangeQuasicoheratorAdjunction B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids hinc hclosed hpres hls hlsD hwp hsep).counit.app F)}
    (hc : IsColimit c) : IsParasitic.{u, w, u} B S hS 𝒳 .etale c.pt.obj.val
```

## Tag 0GQJ, a lemma

[Tag 0GQJ](https://stacks.math.columbia.edu/tag/0GQJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isIso_lqcohFbcCoheratorPullbackComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorFlatPullback.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorFlatPullback.lean#L142). The attribute's comment: “the canonical comparison f^* ∘ Q\_𝒴 ⟶ Q\_𝒳 ∘ f^*, the mate of i ∘ f^* = f^* ∘ i under the adjunctions of Stacks 0778, is an isomorphism”.

> **Stacks 0GQJ.** Let `f : 𝒳 ⟶ 𝒴` be a flat morphism of algebraic stacks.  Then
> `Q_𝒳 ∘ f^* = f^* ∘ Q_𝒴`, with `Q_𝒳` and `Q_𝒴` the coherators of **Stacks 0778**: the canonical
> comparison `f^* Q_𝒴(𝓕) ⟶ Q_𝒳(f^*𝓕)` is an isomorphism for every `𝓕` in `LQCoh^fbc(𝒪_𝒴)`.

```lean
theorem isIso_lqcohFbcCoheratorPullbackComparison (hf : AlgebraicStacks.IsFlat B S hS f) :
    IsIso (lqcohFbcCoheratorPullbackComparison B E h S hS f)
```

## Tag 0GQK, a lemma

[Tag 0GQK](https://stacks.math.columbia.edu/tag/0GQK) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isIso_restrict_coheratorAdjunction_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorFlatObjectIso.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorFlatObjectIso.lean#L52). The attribute's comment: “Q(F)|\_\{U\_ét} = F|\_\{U\_ét} for x : U → 𝒳 flat and F in LQCoh^fbc(𝒪\_𝒳): the restriction of the adjunction map Q(F) → F to U\_ét is an isomorphism”.

> **Stacks 0GQK.** Let `x` be an object of an algebraic stack `𝒳` lying over a scheme `U` such
> that `x : U → 𝒳` is flat, and let `𝓕` be in `LQCoh^fbc(𝒪_𝒳)`.  Then `Q(𝓕)|_{U_ét} = 𝓕|_{U_ét}`:
> the restriction to the small étale site of `U` of the adjunction map `Q(𝓕) ⟶ 𝓕` of the coherator
> of **Stacks 0778** is an isomorphism.

```lean
theorem isIso_restrict_coheratorAdjunction_counit (F : Stack.fppfModules B S hS 𝒳)
    (hF : lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 F)
    (x : 𝒳.val.val.obj) (hx : flatObject B S hS 𝒳.val x) :
    IsIso ((restrictModuleFunctorToSmallEtale B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids x (etaleTopology B) (etaleTopology_le_topology B)).map
        ((coheratorAdjunction B S hS 𝒳).counit.app F).val)
```

## Tag 0GQL, a remark

[Tag 0GQL](https://stacks.math.columbia.edu/tag/0GQL) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLimitKernelForkCoherator`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L81). The attribute's comment: “part (3), the second half: Q(Ker φ), with its map to 𝓕, is the kernel of φ in QCoh(𝒪\_𝒳), for the coherator Q of Stacks 0778”.

> **Stacks 0GQL, part (3), the kernel in `QCoh(𝒪_𝒳)`.** For a map `φ : 𝓕 ⟶ 𝓖` of
> quasi-coherent modules on an algebraic stack, `Q(Ker(i φ))`, the coherator of the kernel computed
> in `Mod(𝒪_𝒳)`, with its map to `𝓕`, is the kernel of `φ` in `QCoh(𝒪_𝒳)`.

```lean
def isLimitKernelForkCoherator {F G : quasicoherentModules B S hS 𝒳} (φ : F ⟶ G) :
    IsLimit (KernelFork.ofι (Abelian.coreflectorKernelι (coheratorAdjunction B S hS 𝒳) φ)
      (Abelian.coreflectorKernelι_comp (coheratorAdjunction B S hS 𝒳) φ))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohSheafFbc_kernel_quasicoherentInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L350). The attribute's comment: “part (3), the first half: the kernel computed in Mod(𝒪\_𝒳) of a map of quasi-coherent modules lies in LQCoh^fbc(𝒪\_𝒳)”.

> **Stacks 0GQL, part (3), the kernel in `Mod(𝒪_𝒳)`.** For a map `φ : 𝓕 ⟶ 𝓖` of quasi-coherent
> modules on an algebraic stack, the kernel of `φ` computed in `Mod(𝒪_𝒳)` lies in
> `LQCoh^fbc(𝒪_𝒳)`, `LQCoh^fbc(𝒪_𝒳)` being a weak Serre subcategory containing `QCoh(𝒪_𝒳)`
> (**Stacks 0771** (2)). Its coherator is the kernel of `φ` in `QCoh(𝒪_𝒳)`
> (`AlgebraicGeometry.Stack.AlgebraicStacks.isLimitKernelForkCoherator`).

```lean
theorem lqcohSheafFbc_kernel_quasicoherentInclusion {F G : quasicoherentModules B S hS 𝒳}
    (φ : F ⟶ G) :
    lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳
      (kernel ((quasicoherentInclusion B S hS 𝒳).map φ))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohSheafFbc_image_quasicoherentInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L363). The attribute's comment: “part (2), corrected, the first half: the image computed in Mod(𝒪\_𝒳) of a map of quasi-coherent modules lies in LQCoh^fbc(𝒪\_𝒳); it need not be quasi-coherent”.

> **Stacks 0GQL, part (2), corrected, the image in `Mod(𝒪_𝒳)`.** For a map `φ : 𝓕 ⟶ 𝓖` of
> quasi-coherent modules on an algebraic stack, the image of `φ` computed in `Mod(𝒪_𝒳)` lies in
> `LQCoh^fbc(𝒪_𝒳)`: it is the kernel of `𝓖 ⟶ Coker(φ)`. It need not be quasi-coherent: part (2)
> as printed is refuted by
> `AlgebraicGeometry.Stack.ImageCounterexample.not_forall_isQuasicoherentOnSite_image`.

```lean
theorem lqcohSheafFbc_image_quasicoherentInclusion {F G : quasicoherentModules B S hS 𝒳}
    (φ : F ⟶ G) :
    lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳
      (Abelian.image ((quasicoherentInclusion B S hS 𝒳).map φ))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.coheratorImageIsImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L377). The attribute's comment: “part (2), corrected, the second half: Q(Im φ) is the image of φ in QCoh(𝒪\_𝒳), for the coherator Q of Stacks 0778”.

> **Stacks 0GQL, part (2), corrected, the image in `QCoh(𝒪_𝒳)`.** For a map `φ : 𝓕 ⟶ 𝓖` of
> quasi-coherent modules on an algebraic stack, `Q(Im φ)`, the coherator of the image computed in
> `Mod(𝒪_𝒳)`, is the image of `φ` in `QCoh(𝒪_𝒳)`: the epimorphism `𝓕 ⟶ Im φ` lies in
> `LQCoh^fbc(𝒪_𝒳)`, where `Q` is right exact (**Stacks 0779** (3)), and `Q` keeps
> `Im φ ⟶ 𝓖` a monomorphism. Part (2) as printed, with `Im φ` itself quasi-coherent, is refuted by
> `AlgebraicGeometry.Stack.ImageCounterexample.not_forall_isQuasicoherentOnSite_image`.

```lean
def coheratorImageIsImage {F G : quasicoherentModules B S hS 𝒳} (φ : F ⟶ G) :
    IsImage (Abelian.coreflectorImageMonoFactorisation (coheratorAdjunction B S hS 𝒳) φ)
```

**`AlgebraicGeometry.Stack.ImageCounterexample.not_forall_isQuasicoherentOnSite_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentImageCounterexample.lean, line 330](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentImageCounterexample.lean#L330). The attribute's comment: “part (2) as printed is false, and the inclusion QCoh(𝒪\_𝒳) → Mod(𝒪\_𝒳) is not exact in general: for multiplication by 2 on 𝒪 over Spec ℤ the image computed in Mod(𝒪\_𝒳) is not quasi-coherent (it vanishes on Spec 𝔽₂ while its would-be module 2ℤ ⊗ 𝔽₂ does not); the corrected part (2) is lqcohSheafFbc\_image\_quasicoherentInclusion and coheratorImageIsImage”.

> **Stacks 0GQL, part (2), fails as written.** It is not true that for every map `φ` of
> quasi-coherent modules on an algebraic stack the image of `φ` computed in `Mod(𝒪_𝒳)` is
> quasi-coherent: multiplication by `2` on `𝒪` over `Spec ℤ` is a counterexample. The corrected
> part (2) is `AlgebraicGeometry.Stack.AlgebraicStacks.lqcohSheafFbc_image_quasicoherentInclusion`
> (the image lies in `LQCoh^fbc(𝒪_𝒳)`) together with
> `AlgebraicGeometry.Stack.AlgebraicStacks.coheratorImageIsImage` (its coherator is the image in
> `QCoh(𝒪_𝒳)`).

```lean
theorem not_forall_isQuasicoherentOnSite_image :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
      (𝒳 : AlgebraicStacks.{u, w} B S hS) (F G : AlgebraicStacks.quasicoherentModules B S hS 𝒳)
      (φ : F ⟶ G),
      (Abelian.image
        ((AlgebraicStacks.quasicoherentInclusion B S hS 𝒳).map φ)).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.FibredSite.isColimitCokernelCoforkMapQuasicoherentInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelCokernel.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelCokernel.lean#L114). The attribute's comment: “part (1): the cokernel of a map of quasi-coherent modules computed in Mod(𝒪\_𝒳) is the inclusion of the cokernel computed in QCoh(𝒪\_𝒳), over the closure of quasi-coherence under colimits”.

> **Stacks 0GQL, part (1).**  Let `φ : 𝓕 → 𝓖` be a map of quasi-coherent `𝒪_𝒳`-modules.  The
> cokernel of `φ` in `QCoh(𝒪_𝒳)`, included into `Mod(𝒪_𝒳)` together with its projection, is a
> cokernel of `φ` in `Mod(𝒪_𝒳)`.
>
> So the cokernel computed in `Mod(𝒪_𝒳)` is the image of a quasi-coherent module — which is the
> quasi-coherence half of the clause, recorded separately as
> `AlgebraicGeometry.FibredSite.isQuasicoherent_cokernel_quasicoherentInclusion` — and it is the
> cokernel in `QCoh(𝒪_𝒳)`.  The proof is the right exactness of the inclusion, which is how the
> source gets the clause.

```lean
def isColimitCokernelCoforkMapQuasicoherentInclusion
    {F G : quasicoherentModules.{u, u + 1, u, u} B S hS p hp} (φ : F ⟶ G) :
    IsColimit (Cofork.ofπ
      ((SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          (ringStructureSheafCore B S hS p hp .fppf)).ι.map (cokernel.π φ))
      (by simp only [← Functor.map_comp, cokernel.condition, zero_comp, Functor.map_zero]) :
      Cofork ((SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringStructureSheafCore B S hS p hp .fppf)).ι.map φ) 0)
```

**`AlgebraicGeometry.FibredSite.isQuasicoherent_cokernel_quasicoherentInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelCokernel.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelCokernel.lean#L130). The attribute's comment: “part (1), the quasi-coherence half: the cokernel computed in Mod(𝒪\_𝒳) of a map of quasi-coherent modules is quasi-coherent, over the closure of quasi-coherence under colimits”.

> **Stacks 0GQL, part (1), the quasi-coherence half.**  The cokernel of a map of quasi-coherent
> `𝒪_𝒳`-modules computed in `Mod(𝒪_𝒳)` is quasi-coherent, because it is isomorphic to the
> inclusion of the cokernel computed in `QCoh(𝒪_𝒳)`.

```lean
theorem isQuasicoherent_cokernel_quasicoherentInclusion
    {F G : quasicoherentModules.{u, u + 1, u, u} B S hS p hp} (φ : F ⟶ G) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringStructureSheafCore B S hS p hp .fppf))
      (cokernel ((SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (ringStructureSheafCore B S hS p hp .fppf)).ι.map φ))
```

**`AlgebraicGeometry.Stack.isLimitKernelForkFlatBaseChangeQuasicoherator`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelCokernel.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelCokernel.lean#L240). The attribute's comment: “part (3), second half: Q(Ker φ) is the kernel of φ in QCoh(𝒪\_𝒳), over the existence of Ker φ inside LQCoh^fbc(𝒪\_𝒳) — the first half of the clause, which is Stacks 0771 part (2) and is not available”.

> **Stacks 0GQL, part (3), second half.**  Let `φ : 𝓕 → 𝓖` be a map of quasi-coherent
> `𝒪_𝒳`-modules and let `Ker(i φ)` be its kernel inside `LQCoh^fbc(𝒪_𝒳)`.  Then `Q(Ker(i φ))`,
> with the map `AlgebraicGeometry.Stack.quasicoheratorKernelι` to `𝓕`, is a kernel of `φ` in
> `QCoh(𝒪_𝒳)`.
>
> The proof is formal: `Q` is a right adjoint, so it preserves the kernel, and `Q ∘ i` is the
> identity because the inclusion is fully faithful; transporting the kernel of `Q(i φ)` along that
> identification gives the kernel of `φ`.
>
> That `Ker(φ)` computed in `Mod(𝒪_𝒳)` lies in `LQCoh^fbc(𝒪_𝒳)` is the first half of the clause and
> is **Stacks 0771** part (2); it is not available, and it enters here only as the instance
> hypothesis that the kernel exists in `LQCoh^fbc(𝒪_𝒳)`.

```lean
def isLimitKernelForkFlatBaseChangeQuasicoherator
    {F G : FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS p hp} (φ : F ⟶ G)
    [HasKernel ((quasicoherentToFlatBaseChange B E h S hS p hp hinc).map φ)] :
    IsLimit (KernelFork.ofι
      (quasicoheratorKernelι B E h S hS p hp hinc hclosed hpres hls hlsD hwp hsep φ)
      (quasicoheratorKernelι_comp B E h S hS p hp hinc hclosed hpres hls hlsD hwp hsep φ))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.preservesFiniteColimits_quasicoherentInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelImageCokernel.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelImageCokernel.lean#L78). The attribute's comment: “the inclusion QCoh(𝒪\_𝒳) → Mod(𝒪\_𝒳) is right exact”.

> **Stacks 0GQL, the right exactness of the inclusion.** The inclusion
> `QCoh(𝒪_𝒳) → Mod(𝒪_𝒳)` of the quasi-coherent modules on an algebraic stack is right exact.

```lean
theorem preservesFiniteColimits_quasicoherentInclusion :
    PreservesFiniteColimits (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
      (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids .fppf)).ι
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isColimitCokernelCoforkQuasicoherentInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelImageCokernel.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelImageCokernel.lean#L111). The attribute's comment: “part (1): the cokernel computed in Mod(𝒪\_𝒳) of a map of quasi-coherent modules is the cokernel computed in QCoh(𝒪\_𝒳)”.

> **Stacks 0GQL, part (1).** Let `φ : 𝓕 → 𝓖` be a map of quasi-coherent modules on an algebraic
> stack `𝒳`. The cokernel of `φ` in `QCoh(𝒪_𝒳)`, included into `Mod(𝒪_𝒳)` with its projection, is a
> cokernel of `φ` in `Mod(𝒪_𝒳)`: the cokernel computed in `Mod(𝒪_𝒳)` is the cokernel in
> `QCoh(𝒪_𝒳)`.

```lean
def isColimitCokernelCoforkQuasicoherentInclusion
    {F G : FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids} (φ : F ⟶ G) :
    IsColimit (Cofork.ofπ
      ((SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
          (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
            .fppf)).ι.map (cokernel.π φ))
      (by simp only [← Functor.map_comp, cokernel.condition, zero_comp, Functor.map_zero]) :
      Cofork ((SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
          .fppf)).ι.map φ) 0)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasicoherent_cokernel_quasicoherentInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelImageCokernel.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelImageCokernel.lean#L128). The attribute's comment: “part (1), the quasi-coherence half: the cokernel computed in Mod(𝒪\_𝒳) of a map of quasi-coherent modules is quasi-coherent”.

> **Stacks 0GQL, part (1), the quasi-coherence half.** The cokernel computed in `Mod(𝒪_𝒳)` of a
> map of quasi-coherent modules on an algebraic stack is quasi-coherent.

```lean
theorem isQuasicoherent_cokernel_quasicoherentInclusion
    {F G : FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids} (φ : F ⟶ G) :
    (SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids .fppf))
      (cokernel ((SheafOfModules.isQuasicoherentOnSite.{u + 1, u, u, u}
        (FibredSite.ringStructureSheafCore B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
          .fppf)).ι.map φ))
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.instAbelianQuasicoherentModules`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentModulesAbelian.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentModulesAbelian.lean#L70). The attribute's comment: “the category QCoh(𝒪\_𝒳) is abelian, for every algebraic stack 𝒳”.

> **Stacks 0GQL**: `QCoh(𝒪_𝒳)` is abelian, for every algebraic stack `𝒳` (also **Stacks 06WV**
> part (2)). It is coreflective in the weak Serre subcategory `LQCoh^fbc(𝒪_𝒳)` of `Mod(𝒪_𝒳)`, with
> the coherator, right exact there, as coreflector.

```lean
instance instAbelianQuasicoherentModules : Abelian (quasicoherentModules B S hS 𝒳)
```

Declarations registered for the tag:

- [`preservesFiniteColimits_quasicoherentInclusion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=preservesFiniteColimits_quasicoherentInclusion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelCokernel.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentKernelCokernel.lean#L90) (StacksFrontier): “the inclusion QCoh(𝒪\_𝒳) → Mod(𝒪\_𝒳) is right exact, over the closure of quasi-coherence under colimits”.

## Tag 0GQM, a remark

[Tag 0GQM](https://stacks.math.columbia.edu/tag/0GQM) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.isMonoidal_lqcohSheafFbc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L207). The attribute's comment: “(ii): LQCoh^fbc(𝒪\_𝒳) is closed under the tensor product, a monoidal subcategory of Mod(𝒪\_𝒳)”.

> **Stacks 0GQM, (ii).** `LQCoh^fbc(𝒪_𝒳)` is closed under the tensor product of `𝒪_𝒳`-modules
> (**Stacks 0771** (6)) and contains `𝒪_𝒳`: it is a monoidal subcategory of `Mod(𝒪_𝒳)`.

```lean
theorem isMonoidal_lqcohSheafFbc :
    (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).IsMonoidal
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohSheafFbcInclusionBraided`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L222). The attribute's comment: “(iii): the inclusion LQCoh^fbc(𝒪\_𝒳) → Mod(𝒪\_𝒳) is a functor of symmetric monoidal categories”.

> **Stacks 0GQM, (iii), the inclusion `LQCoh^fbc(𝒪_𝒳) → Mod(𝒪_𝒳)`**: a functor of symmetric
> monoidal categories, for the tensor product of `𝒪_𝒳`-modules and the structure it induces on
> `LQCoh^fbc(𝒪_𝒳)`.

```lean
def lqcohSheafFbcInclusionBraided :
    letI := isMonoidal_lqcohSheafFbc B S hS 𝒳 E h
    (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι.Braided
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentToLqcohSheafFbcBraided`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L232). The attribute's comment: “(iii): the inclusion QCoh(𝒪\_𝒳) → LQCoh^fbc(𝒪\_𝒳) is a functor of symmetric monoidal categories”.

> **Stacks 0GQM, (iii), the inclusion `QCoh(𝒪_𝒳) → LQCoh^fbc(𝒪_𝒳)`**: a functor of symmetric
> monoidal categories, for the structures both inherit from `Mod(𝒪_𝒳)`.

```lean
def quasicoherentToLqcohSheafFbcBraided :
    letI := isMonoidal_lqcohSheafFbc B S hS 𝒳 E h
    (ObjectProperty.ιOfLE (isQuasicoherentOnSite_le_lqcohSheafFbc B S hS 𝒳 E h)).Braided
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.coheratorBraided`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L288). The attribute's comment: “(iv): the coherator Q : LQCoh^fbc(𝒪\_𝒳) → QCoh(𝒪\_𝒳) is a functor of symmetric monoidal categories”.

> **Stacks 0GQM, (iv).** The coherator `Q : LQCoh^fbc(𝒪_𝒳) → QCoh(𝒪_𝒳)` is a functor of
> symmetric monoidal categories. Its comparison `Q(𝓕) ⊗ Q(𝓖) → Q(𝓕 ⊗ 𝓖)` is the adjoint transpose
> of the tensor product `Q(𝓕) ⊗ Q(𝓖) → 𝓕 ⊗ 𝓖` of the two counits, the south-west arrow of the
> triangle of the source, and it is invertible because `Q` inverts that tensor product of counits
> (`AlgebraicGeometry.Stack.AlgebraicStacks.isIso_coherator_map_tensorHom_counit`).

```lean
def coheratorBraided :
    letI := isMonoidal_lqcohSheafFbc B S hS 𝒳 E h
    ((lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι ⋙ coherator B S hS 𝒳).Braided
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isIso_coheratorTensorComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L299). The attribute's comment: “(iv): the canonical map Q(F) ⊗ Q(G) → Q(F ⊗ G) is an isomorphism”.

> **Stacks 0GQM, (iv), the tensor comparison.** For `𝓕, 𝓖` in `LQCoh^fbc(𝒪_𝒳)` the canonical
> map `Q(𝓕) ⊗ Q(𝓖) → Q(𝓕 ⊗ 𝓖)`, the adjoint transpose of the tensor product of the two counits,
> is an isomorphism.

```lean
theorem isIso_coheratorTensorComparison
    (F G : (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).FullSubcategory) :
    letI := isMonoidal_lqcohSheafFbc B S hS 𝒳 E h
    letI := (lqcohSheafFbcCoheratorAdjunction B S hS 𝒳 E h).rightAdjointLaxMonoidal
    IsIso (Functor.LaxMonoidal.μ
      ((lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι ⋙ coherator B S hS 𝒳) F G)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.coheratorTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorCanonical.lean#L313). The attribute's comment: “(iv): the isomorphism Q(F) ⊗ Q(G) ≅ Q(F ⊗ G)”.

> **Stacks 0GQM, (iv), the isomorphism `Q(𝓕) ⊗ Q(𝓖) ≅ Q(𝓕 ⊗ 𝓖)`** of the symmetric monoidal
> functor `AlgebraicGeometry.Stack.AlgebraicStacks.coheratorBraided`; its forward map is the
> canonical comparison (`AlgebraicGeometry.Stack.AlgebraicStacks.coheratorTensorIso_hom`).

```lean
def coheratorTensorIso
    (F G : (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).FullSubcategory) :
    letI := isMonoidal_lqcohSheafFbc B S hS 𝒳 E h
    (coherator B S hS 𝒳).obj F.obj ⊗ (coherator B S hS 𝒳).obj G.obj ≅
      (coherator B S hS 𝒳).obj (F ⊗ G).obj
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isQuasicoherentOnSite_sheafTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorMonoidal.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorMonoidal.lean#L121). The attribute's comment: “(i): the tensor product of two quasi-coherent modules on an algebraic stack is quasi-coherent”.

> **Stacks 0GQM, (i).** The tensor product `𝓕 ⊗_{𝒪_𝒳} 𝓖` of two quasi-coherent modules on an
> algebraic stack is quasi-coherent (**Stacks 06WV** part (5)). The tensor product is the tensor
> product sheaf, the sheafification of the objectwise tensor product, on the fppf site of `𝒳`.
>
> This is `AlgebraicGeometry.FibredSite.isQuasicoherentOnSite_tensorSheaf` at the fppf site of the
> algebraic stack, which is essentially small.

```lean
theorem isQuasicoherentOnSite_sheafTensor (F G : Stack.fppfModules B S hS 𝒳)
    (hF : F.IsQuasicoherentOnSite) (hG : G.IsQuasicoherentOnSite) :
    (((Stacks.SheafOfModules.Tensor.sheafTensor (FibredSite.structureSheaf B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids .fppf)).obj F).obj G).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentInclusionBraided`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorMonoidal.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorMonoidal.lean#L147). The attribute's comment: “(iii): the inclusion QCoh(𝒪\_𝒳) → Mod(𝒪\_𝒳) is a functor of symmetric monoidal categories”.

> **Stacks 0GQM, (iii), the first inclusion into `Mod(𝒪_𝒳)`.** `QCoh(𝒪_𝒳)` is a symmetric
> monoidal category for the tensor product of `𝒪_𝒳`-modules, and the inclusion
> `QCoh(𝒪_𝒳) → Mod(𝒪_𝒳)` is a functor of symmetric monoidal categories.

```lean
def quasicoherentInclusionBraided : (quasicoherentInclusion B S hS 𝒳).Braided
```

**`Stacks.SheafOfModules.TensorProduct.isQuasicoherent_tensorSheaf'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorProduct/Quasicoherent.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorProduct/Quasicoherent.lean#L303). The attribute's comment: “tensor products of quasi-coherent modules are quasi-coherent”. References: EGA I (9.1.1), “more general”.

> **Stacks 0GQM.** The tensor product of two quasi-coherent sheaves of modules on a site is
> quasi-coherent.
>
> Each factor is presented on some family covering the final object. The two families are refined
> by the objects carrying a morphism into a member of each, which again covers the final object:
> given an object, the first family covers it, each member of that cover is covered by the second
> family, and every object of the resulting cover maps to a member of both. On such an object the
> two presentations restrict, their tensor product presents the tensor product of the restrictions
> by `Stacks.SheafOfModules.TensorProduct.tensorPresentation`, and that is the restriction of
> `F ⊗_𝒪 G` by `Stacks.SheafOfModules.TensorProduct.tensorSheafificationOverIso`.

```lean
theorem isQuasicoherent_tensorSheaf'
    (F G : SheafOfModules.{w} (structureSheaf 𝒪 h𝒪))
    [F.IsQuasicoherent] [G.IsQuasicoherent] :
    ((((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨𝒪, Presheaf.isSheaf_of_isSheaf_comp _ (𝒪) (forget₂ CommRingCat RingCat)
          (h𝒪)⟩).obj (F)).obj (G))).IsQuasicoherent
```

## Tag 07B2, a remark

[Tag 07B2](https://stacks.math.columbia.edu/tag/07B2) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocalization_flatBaseChangeQuasicoherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorSerreQuotient.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorSerreQuotient.lean#L316). The attribute's comment: “the displayed identification QCoh(𝒪\_𝒳) = LQCoh^fbc(𝒪\_𝒳) / Parasitic(𝒪\_𝒳) ∩ LQCoh^fbc(𝒪\_𝒳): the coherator Q of 0778 is a localization functor for the Serre class of parasitic objects; over the hypotheses of 0778 and 0779 and the abelian structures of 06WV (2) and 0771 (2)”.

> **Stacks 07B2**, the displayed identification
>
> `QCoh(𝒪_𝒳) = LQCoh^fbc(𝒪_𝒳) / Parasitic(𝒪_𝒳) ∩ LQCoh^fbc(𝒪_𝒳)`.
>
> The coherator `Q : LQCoh^fbc(𝒪_𝒳) ⥤ QCoh(𝒪_𝒳)` of **Stacks 0778** is a localization functor for
> the class of morphisms whose kernel and cokernel are parasitic, that is, it exhibits
> `QCoh(𝒪_𝒳)` as the quotient of `LQCoh^fbc(𝒪_𝒳)` by the Serre subcategory of parasitic objects
> (**Stacks 02MS**).
>
> The inclusion `i` is fully faithful and `Q` is its right adjoint (**Stacks 0778**), so `Q` is a
> localization functor for the class of morphisms it inverts; by
> `AlgebraicGeometry.Stack.parasiticIsoModSerre_eq_inverseImage_isomorphisms` that class is the
> one attached to the parasitic part.

```lean
theorem isLocalization_flatBaseChangeQuasicoherator :
    (flatBaseChangeQuasicoherator B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
        hinc hclosed hpres hls hlsD hwp hsep).IsLocalization
      (parasiticIsoModSerre B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp hsep r hrpar
        hrcounit hreq hrfincolim)
```

**`AlgebraicGeometry.Stack.serreQuotientEquivalenceQuasicoherentModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorSerreQuotient.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorSerreQuotient.lean#L339). The attribute's comment: “the displayed identification read as an equivalence of categories between the Serre quotient of LQCoh^fbc(𝒪\_𝒳) by Parasitic(𝒪\_𝒳) ∩ LQCoh^fbc(𝒪\_𝒳) and QCoh(𝒪\_𝒳); over the hypotheses of 0778 and 0779 and the abelian structures of 06WV (2) and 0771 (2)”.

> **Stacks 07B2**, the displayed identification as an equivalence of categories.  The Serre
> quotient `LQCoh^fbc(𝒪_𝒳) / Parasitic(𝒪_𝒳) ∩ LQCoh^fbc(𝒪_𝒳)`, built as the localization of
> `LQCoh^fbc(𝒪_𝒳)` at the morphisms with parasitic kernel and cokernel, is equivalent to
> `QCoh(𝒪_𝒳)`, the equivalence being the one through which the coherator of **Stacks 0778**
> factors.

```lean
def serreQuotientEquivalenceQuasicoherentModules :
    (parasiticIsoModSerre B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp hsep r hrpar hrcounit
        hreq hrfincolim).Localization ≌
      FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids
```

**`AlgebraicGeometry.Stack.serreQuotientAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorSerreQuotient.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/CoheratorSerreQuotient.lean#L364). The attribute's comment: “the key feature: the inclusion i : QCoh(𝒪\_𝒳) ⥤ LQCoh^fbc(𝒪\_𝒳) is left adjoint to the quotient functor LQCoh^fbc(𝒪\_𝒳) ⥤ LQCoh^fbc(𝒪\_𝒳) / Parasitic(𝒪\_𝒳) ∩ LQCoh^fbc(𝒪\_𝒳); over the hypotheses of 0778 and 0779 and the abelian structures of 06WV (2) and 0771 (2)”.

> **Stacks 07B2**, the key feature: the inclusion
> `i : QCoh(𝒪_𝒳) ⥤ LQCoh^fbc(𝒪_𝒳)` is left adjoint to the quotient functor.
>
> Read with `QCoh(𝒪_𝒳)` identified with the Serre quotient by
> `AlgebraicGeometry.Stack.serreQuotientEquivalenceQuasicoherentModules`, this is an adjunction
> between `i` and the canonical quotient functor
> `LQCoh^fbc(𝒪_𝒳) ⥤ LQCoh^fbc(𝒪_𝒳) / Parasitic(𝒪_𝒳) ∩ LQCoh^fbc(𝒪_𝒳)`.  It is the adjunction of
> **Stacks 0778** composed with the adjoint equivalence, transported along the isomorphism which
> identifies the quotient functor with the coherator followed by that equivalence.

```lean
def serreQuotientAdjunction :
    (serreQuotientEquivalenceQuasicoherentModules B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp
          hsep r hrpar hrcounit hreq hrfincolim).functor ⋙
        quasicoherentToFlatBaseChange B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids hinc ⊣
      (parasiticIsoModSerre B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp hsep r hrpar hrcounit
        hreq hrfincolim).Q
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isLocalization_lqcohFbcCoherator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSerreQuotient.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSerreQuotient.lean#L142). The attribute's comment: “the displayed identification QCoh(𝒪\_𝒳) = LQCoh^fbc(𝒪\_𝒳) / Parasitic(𝒪\_𝒳) ∩ LQCoh^fbc(𝒪\_𝒳): the coherator Q of 0778 is a localization functor for the Serre class of parasitic objects”.

> **Stacks 07B2**, the displayed identification
> `QCoh(𝒪_𝒳) = LQCoh^fbc(𝒪_𝒳) / Parasitic(𝒪_𝒳) ∩ LQCoh^fbc(𝒪_𝒳)`: for an algebraic stack `𝒳`, the
> coherator `Q : LQCoh^fbc(𝒪_𝒳) ⥤ QCoh(𝒪_𝒳)` of **Stacks 0778** is a localization functor for the
> morphisms whose kernel and cokernel are parasitic, i.e. it exhibits `QCoh(𝒪_𝒳)` as the Serre
> quotient (**Stacks 02MS**) of `LQCoh^fbc(𝒪_𝒳)` by its parasitic objects.

```lean
theorem isLocalization_lqcohFbcCoherator :
    (lqcohFbcCoherator B E h S hS 𝒳).IsLocalization
      (parasiticLqcohFbc B E h S hS 𝒳).isoModSerre
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcSerreQuotientEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSerreQuotient.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSerreQuotient.lean#L154). The attribute's comment: “the displayed identification read as an equivalence of categories between the Serre quotient of LQCoh^fbc(𝒪\_𝒳) by Parasitic(𝒪\_𝒳) ∩ LQCoh^fbc(𝒪\_𝒳) and QCoh(𝒪\_𝒳)”.

> **Stacks 07B2**, the displayed identification as an equivalence of categories between the
> Serre quotient `LQCoh^fbc(𝒪_𝒳) / Parasitic(𝒪_𝒳) ∩ LQCoh^fbc(𝒪_𝒳)` (the localization at the
> morphisms with parasitic kernel and cokernel) and `QCoh(𝒪_𝒳)`, the one through which the
> coherator of **Stacks 0778** factors.

```lean
def lqcohFbcSerreQuotientEquivalence :
    (parasiticLqcohFbc B E h S hS 𝒳).isoModSerre.Localization ≌ quasicoherentModules B S hS 𝒳
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcSerreQuotientAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSerreQuotient.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSerreQuotient.lean#L165). The attribute's comment: “the key feature: the inclusion i : QCoh(𝒪\_𝒳) ⥤ LQCoh^fbc(𝒪\_𝒳) is left adjoint to the quotient functor LQCoh^fbc(𝒪\_𝒳) ⥤ LQCoh^fbc(𝒪\_𝒳) / Parasitic(𝒪\_𝒳) ∩ LQCoh^fbc(𝒪\_𝒳)”.

> **Stacks 07B2**, the key feature: the inclusion `i : QCoh(𝒪_𝒳) ⥤ LQCoh^fbc(𝒪_𝒳)`, read on the
> Serre quotient through `lqcohFbcSerreQuotientEquivalence`, is left adjoint to the quotient
> functor `LQCoh^fbc(𝒪_𝒳) ⥤ LQCoh^fbc(𝒪_𝒳) / Parasitic(𝒪_𝒳) ∩ LQCoh^fbc(𝒪_𝒳)`.

```lean
def lqcohFbcSerreQuotientAdjunction :
    (lqcohFbcSerreQuotientEquivalence B E h S hS 𝒳).functor ⋙
        quasicoherentToLqcohFbc B E h S hS 𝒳 ⊣
      (parasiticLqcohFbc B E h S hS 𝒳).isoModSerre.Q
```

## Tag 0GQN, a lemma

[Tag 0GQN](https://stacks.math.columbia.edu/tag/0GQN) in the Stacks Project.

**`AlgebraicGeometry.FibredSite.internalHomSheaf_restrictSiteModules_val`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHomSiteAgreement.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHomSiteAgreement.lean#L107). The attribute's comment: “the two internal Homs have the same presheaf of modules”.

> **Stacks 0GQN**, the first assertion, on underlying presheaves of modules.  The internal
> Hom of two sheaves of modules on the associated fppf site of a category fibred in groupoids has
> the same underlying presheaf of modules whether it is computed on the associated fppf site or
> on any of the five associated sites; the source's case is the étale one.
>
> The internal Hom of Stacks 03EM is built from the presheaves of modules underlying its two
> arguments and from the presheaf of rings underlying the structure sheaf, and none of the three
> depends on the topology, so the two presheaves of modules are equal on the nose.

```lean
public theorem internalHomSheaf_restrictSiteModules_val (τ : SiteKind)
    (F G : SheafOfModules.{m} (ringStructureSheafCore B S hS p hp .fppf)) :
    ((ringedSite B S hS p hp τ).internalHomSheaf
        (restrictSiteModules.{u, v, w, m} B S hS p hp τ F)
        (restrictSiteModules.{u, v, w, m} B S hS p hp τ G)).val =
      ((ringedSite B S hS p hp .fppf).internalHomSheaf F G).val
```

**`AlgebraicGeometry.FibredSite.isSheaf_internalHomSheaf_restrictSiteModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHomSiteAgreement.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHomSiteAgreement.lean#L123). The attribute's comment: “the common value is a sheaf for the fppf topology”.

> **Stacks 0GQN**, the first assertion, on the sheaf condition.  The internal Hom computed on
> one of the five associated sites of a category fibred in groupoids is a sheaf for the
> associated *fppf* topology, so it is an object of `Mod(𝒪_𝒳)` and not merely of
> `Mod(𝒳_étale, 𝒪_𝒳)`.
>
> By Stacks 03EM the internal Hom is a sheaf for any topology for which its target is one, and
> the target here is a sheaf for the associated fppf topology.

```lean
public theorem isSheaf_internalHomSheaf_restrictSiteModules (τ : SiteKind)
    (F G : SheafOfModules.{m} (ringStructureSheafCore B S hS p hp .fppf)) :
    Presheaf.IsSheaf (BigFppfOver.associatedTopology B S hS p .fppf)
      ((ringedSite B S hS p hp τ).internalHomSheaf
        (restrictSiteModules.{u, v, w, m} B S hS p hp τ F)
        (restrictSiteModules.{u, v, w, m} B S hS p hp τ G)).val.presheaf
```

**`AlgebraicGeometry.FibredSite.internalHomSheaf_restrictSiteModules_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHomSiteAgreement.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/InternalHomSiteAgreement.lean#L139). The attribute's comment: “the two internal Homs agree as objects of Mod(𝒪\_𝒳)”.

> **Stacks 0GQN**, the first assertion.  The internal Hom of two sheaves of modules on the
> associated fppf site of a category fibred in groupoids, computed on one of the five associated
> sites, agrees as an object of `Mod(𝒪_𝒳)` with the one computed on the associated fppf site; the
> source's case is the étale one.
>
> This is the conjunction of the two statements above: the underlying presheaves of modules are
> equal, and the common presheaf is a sheaf for the associated fppf topology.

```lean
public theorem internalHomSheaf_restrictSiteModules_eq (τ : SiteKind)
    (F G : SheafOfModules.{m} (ringStructureSheafCore B S hS p hp .fppf)) :
    (⟨((ringedSite B S hS p hp τ).internalHomSheaf
          (restrictSiteModules.{u, v, w, m} B S hS p hp τ F)
          (restrictSiteModules.{u, v, w, m} B S hS p hp τ G)).val,
        isSheaf_internalHomSheaf_restrictSiteModules.{u, v, w, m} B S hS p hp τ F G⟩ :
        SheafOfModules.{max v w m} (ringStructureSheafCore B S hS p hp .fppf)) =
      (ringedSite B S hS p hp .fppf).internalHomSheaf F G
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.fppfInternalHom_presheaf_eq_etaleInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentInternalHom.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentInternalHom.lean#L107). The attribute's comment: “the agreement of the internal Homs of Mod(𝒳\_étale, 𝒪\_𝒳) and Mod(𝒪\_𝒳), for arbitrary F and G”.

> **Stacks 0GQN**, the agreement of the two internal Homs at module universe `u`.  The internal
> Hom `SheafHom_{𝒪_𝒳}(F, G)` computed in `Mod(𝒳_étale, 𝒪_𝒳)` and the one computed in `Mod(𝒪_𝒳)`
> have the same underlying presheaf of abelian groups, for arbitrary modules `F` and `G` on the fppf
> site; the source states it for `F` of finite presentation and `G` quasi-coherent.
>
> Both are the internal Hom of Stacks 03EM read in the universe `u` of the module sections, and
> that construction depends only on the underlying presheaves of `F`, `G` and of the structure
> sheaf, none of which changes with the topology.

```lean
theorem fppfInternalHom_presheaf_eq_etaleInternalHom (F G : Stack.fppfModules B S hS 𝒳) :
    (fppfInternalHom B S hS 𝒳 F G).val.presheaf =
      (etaleInternalHom B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
        (FibredSite.restrictSiteModules B S hS _ _ .etale F)
        (FibredSite.restrictSiteModules B S hS _ _ .etale G)).val.presheaf
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentInternalHom.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentInternalHom.lean#L148). The attribute's comment: “the universal property of hom(F, G) = Q(SheafHom(F, G)), for arbitrary F and G”.

> **The universal property of `hom(F, G)`** (Stacks 0GQN): for `H` quasi-coherent,
> `Hom_𝒳(H, hom(F, G)) = Hom_𝒳(H ⊗_{𝒪_𝒳} F, G)`.  This is
> `AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHomOfEquiv` at the coherator; it holds for
> arbitrary `F` and `G`.

```lean
def quasicoherentHomEquiv (F G : Stack.fppfModules B S hS 𝒳)
    (H : quasicoherentModules B S hS 𝒳) :
    (H ⟶ quasicoherentHom B S hS 𝒳 F G) ≃
      (fppfTensor B S hS 𝒳 ((quasicoherentInclusion B S hS 𝒳).obj H) F ⟶ G)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohSheafFbcFppfModules_fppfInternalHom_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeInternalHom.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeInternalHom.lean#L100). The attribute's comment: “the common value SheafHom(F, G) is an object of LQCoh^fbc(𝒪\_𝒳), for F of finite presentation and G quasi-coherent”.

> **Stacks 0GQN**, the membership clause: for `F` an `𝒪_𝒳`-module of finite presentation and `G`
> a quasi-coherent `𝒪_𝒳`-module on an algebraic stack, the internal Hom `SheafHom_{𝒪_𝒳}(F, G)`,
> whose two computations agree by
> `AlgebraicGeometry.Stack.AlgebraicStacks.fppfInternalHom_presheaf_eq_etaleInternalHom`, is an
> object of `LQCoh^fbc(𝒪_𝒳)`.  It is Stacks 0771 (7) applied to `G ∈ QCoh(𝒪_𝒳) ⊆ LQCoh^fbc(𝒪_𝒳)`.

```lean
theorem lqcohSheafFbcFppfModules_fppfInternalHom_of_isQuasicoherentOnSite
    (F G : Stack.fppfModules B S hS 𝒳) [F.IsFinitePresentationOnSite]
    (hG : G.IsQuasicoherentOnSite) :
    lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 (fppfInternalHom B S hS 𝒳 F G)
```

## Tag 0GQP, a lemma

[Tag 0GQP](https://stacks.math.columbia.edu/tag/0GQP) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.quasicoherentHomFlatPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHomFlatPullback.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentHomFlatPullback.lean#L76).

> **Stacks 0GQP.** Let `f : 𝒳 ⟶ 𝒴` be a flat morphism of algebraic stacks, `F` an
> `𝒪_𝒴`-module of finite presentation and `G` a quasi-coherent `𝒪_𝒴`-module. Then
> `f^* hom(F, G) = hom(f^* F, f^* G)`, with `hom` the quasi-coherent internal Hom
> `hom(F, G) = Q(SheafHom_{𝒪_𝒴}(F, G))` of Stacks 0GQN.
>
> The isomorphism is the composite of `f^* Q_𝒴 = Q_𝒳 f^*` (Stacks 0GQJ, at
> `SheafHom_{𝒪_𝒴}(F, G)`, which lies in `LQCoh^fbc(𝒪_𝒴)` by Stacks 0GQN) with `Q_𝒳` of
> `f^* SheafHom_{𝒪_𝒴}(F, G) = SheafHom_{𝒪_𝒳}(f^* F, f^* G)`.

```lean
def quasicoherentHomFlatPullbackIso (hf : AlgebraicStacks.IsFlat B S hS f)
    (F G : Stack.fppfModules B S hS 𝒴) [F.IsFinitePresentationOnSite]
    (hG : G.IsQuasicoherentOnSite) :
    (quasicoherentPullback B S hS f).obj (quasicoherentHom B S hS 𝒴 F G) ≅
      quasicoherentHom B S hS 𝒳 ((fppfModulesPullback B S hS f).obj F)
        ((fppfModulesPullback B S hS f).obj G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.10, Tag 0777](https://stacks.math.columbia.edu/tag/0777)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

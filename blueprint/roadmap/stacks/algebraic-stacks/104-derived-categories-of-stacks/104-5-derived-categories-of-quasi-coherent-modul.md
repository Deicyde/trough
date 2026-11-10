---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.derivedCategoryQuasicoherent, AlgebraicGeometry.Stack.toDerivedCategoryQuasicoherent, AlgebraicGeometry.Stack.derivedCategoryQuasicoherentSheaf, AlgebraicGeometry.Stack.toDerivedCategoryQuasicoherentSheaf, AlgebraicGeometry.Stack.cohomologyDerivedCategoryQuasicoherent, AlgebraicGeometry.Stack.cohomologyDerivedCategoryQuasicoherentFac, AlgebraicGeometry.Stack.cohomologyDerivedCategoryQuasicoherentSheaf, AlgebraicGeometry.Stack.cohomologyDerivedCategoryQuasicoherentSheafFac
statement: formalized
proof: formalized
---

# 104.5 Derived categories of quasi-coherent modules

Section 104.5 of the Stacks Project, [Tag 07B5](https://stacks.math.columbia.edu/tag/07B5). 6 tags here are carried by 49 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07B6, a definition

[Tag 07B6](https://stacks.math.columbia.edu/tag/07B6) in the Stacks Project.

**`AlgebraicGeometry.Stack.derivedCategoryQuasicoherent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherent.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherent.lean#L152). The attribute's comment: “the Verdier quotient D_QCoh(𝒪_𝒳) = D_LQCoh^fbc(𝒪_𝒳) / D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳)”.

> **Stacks 07B6.** The *derived category of `𝒪_𝒳`-modules with quasi-coherent cohomology
> sheaves* of an algebraic stack `𝒳`, that is the Verdier quotient
>
> `D_QCoh(𝒪_𝒳) = D_{LQCoh^fbc}(𝒪_𝒳) / D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`,
>
> realized as the localization of `D_{LQCoh^fbc}(𝒪_𝒳)` at the morphisms whose cone lies in
> `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`.

```lean
abbrev derivedCategoryQuasicoherent
```

**`AlgebraicGeometry.Stack.toDerivedCategoryQuasicoherent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherent.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherent.lean#L157). The attribute's comment: “the quotient functor onto D_QCoh(𝒪_𝒳)”.

> **Stacks 07B6**, the quotient functor `D_{LQCoh^fbc}(𝒪_𝒳) ⟶ D_QCoh(𝒪_𝒳)` of the Verdier
> quotient.

```lean
abbrev toDerivedCategoryQuasicoherent :
    (derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳).FullSubcategory ⥤
      derivedCategoryQuasicoherent B E h S hS 𝒳
```

**`AlgebraicGeometry.Stack.derivedCategoryQuasicoherentSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean#L265). The attribute's comment: “the Verdier quotient D_QCoh(𝒪_𝒳) = D_LQCoh^fbc(𝒪_𝒳) / D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳), with the flat base change property of LQCoh^fbc read on sheaves of modules as in the source”.

> **Stacks 07B6**, at the source's `LQCoh^fbc(𝒪_𝒳)`: the derived category with
> quasi-coherent cohomology `D_QCoh(𝒪_𝒳) = D_{LQCoh^fbc}(𝒪_𝒳) / D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`,
> the Verdier quotient of the triangulated subcategory of complexes of `𝒪_𝒳`-modules with
> cohomology in `LQCoh^fbc(𝒪_𝒳)` (a weak Serre subcategory, Stacks 0771) by the one with
> cohomology in the parasitic modules of `LQCoh^fbc(𝒪_𝒳)`.

```lean
abbrev derivedCategoryQuasicoherentSheaf
```

**`AlgebraicGeometry.Stack.toDerivedCategoryQuasicoherentSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean#L272). The attribute's comment: “the quotient functor D_LQCoh^fbc(𝒪_𝒳) ⟶ D_QCoh(𝒪_𝒳), with the flat base change property read on sheaves of modules as in the source”.

> **Stacks 07B6**, at the source's `LQCoh^fbc(𝒪_𝒳)`: the quotient functor.

```lean
abbrev toDerivedCategoryQuasicoherentSheaf :
    (DerivedCategoryB.derivedCategoryB (lqcFbcFppf B S hS 𝒳)).FullSubcategory ⥤
      derivedCategoryQuasicoherentSheaf B S hS 𝒳
```

## Tag 07B7, an equation

[Tag 07B7](https://stacks.math.columbia.edu/tag/07B7) in the Stacks Project.

**`AlgebraicGeometry.Stack.cohomologyDerivedCategoryQuasicoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomology.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomology.lean#L327). The attribute's comment: “the cohomology functor H^i : D_QCoh(𝒪_𝒳) ⟶ QCoh(𝒪_𝒳)”.

> **Stacks 07B7.** The cohomology functor
>
> `H^i : D_QCoh(𝒪_𝒳) ⟶ QCoh(𝒪_𝒳)`
>
> on the derived category of `𝒪_𝒳`-modules with quasi-coherent cohomology sheaves of an algebraic
> stack `𝒳`.  It is the descent through the Verdier quotient of **Stacks 07B6** of the functor
> `Q ∘ H^i` on `D_{LQCoh^fbc}(𝒪_𝒳)`, which is possible because that functor inverts the morphisms
> the quotient inverts.

```lean
def cohomologyDerivedCategoryQuasicoherent (i : ℤ)
    (hhom : (cohomologyQuasicoherent B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp hsep
      i).IsHomological)
    (hQker : ∀ F : locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS
        𝒳.val.val.p 𝒳.val.isFiberedInGroupoids,
      IsZero ((quasicoheratorOfStack B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp hsep).obj F) ↔
        IsParasitic B S hS 𝒳 .etale F.obj.val) :
    derivedCategoryQuasicoherent B E h S hS 𝒳 ⥤
      FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids
```

**`AlgebraicGeometry.Stack.cohomologyDerivedCategoryQuasicoherentFac`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomology.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomology.lean#L346). The attribute's comment: “the identity H^i ∘ (quotient functor) = Q ∘ H^i defining the cohomology functor”.

> **Stacks 07B7**, the identity defining the cohomology functor: composed with the quotient
> functor `D_{LQCoh^fbc}(𝒪_𝒳) ⟶ D_QCoh(𝒪_𝒳)`, the functor `H^i` of **Stacks 07B7** is the functor
> `Q ∘ H^i` it descends.

```lean
def cohomologyDerivedCategoryQuasicoherentFac (i : ℤ)
    (hhom : (cohomologyQuasicoherent B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp hsep
      i).IsHomological)
    (hQker : ∀ F : locallyQuasicoherentFlatBaseChangeModules.{u, u + 1, u} B E h S hS
        𝒳.val.val.p 𝒳.val.isFiberedInGroupoids,
      IsZero ((quasicoheratorOfStack B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp hsep).obj F) ↔
        IsParasitic B S hS 𝒳 .etale F.obj.val) :
    toDerivedCategoryQuasicoherent B E h S hS 𝒳 ⋙
        cohomologyDerivedCategoryQuasicoherent B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp hsep
          i hhom hQker ≅
      cohomologyQuasicoherent B E h S hS 𝒳 hinc hclosed hpres hls hlsD hwp hsep i
```

**`AlgebraicGeometry.Stack.cohomologyDerivedCategoryQuasicoherentSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean#L305). The attribute's comment: “the cohomology functor H^i : D_QCoh(𝒪_𝒳) ⟶ QCoh(𝒪_𝒳), descended from Q ∘ H^i with Q the coherator of 0778”.

> **Stacks 07B7**: the cohomological functor `H^i : D_QCoh(𝒪_𝒳) ⟶ QCoh(𝒪_𝒳)`, the functor
> `Q ∘ H^i : D_{LQCoh^fbc}(𝒪_𝒳) ⟶ QCoh(𝒪_𝒳)` descended to the Verdier quotient (Stacks 05RJ),
> `Q` being the coherator of Stacks 0778, which annihilates
> `Parasitic(𝒪_𝒳) ∩ LQCoh^fbc(𝒪_𝒳)` (Stacks 0779).

```lean
def cohomologyDerivedCategoryQuasicoherentSheaf (i : ℤ) :
    derivedCategoryQuasicoherentSheaf B S hS 𝒳 ⥤
      FibredSite.quasicoherentModules.{u, u + 1, u, u} B S hS 𝒳.val.val.p
        𝒳.val.isFiberedInGroupoids
```

**`AlgebraicGeometry.Stack.cohomologyDerivedCategoryQuasicoherentSheafFac`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean#L314). The attribute's comment: “the identity H^i ∘ (quotient functor) = Q ∘ H^i defining the cohomology functor”.

> **Stacks 07B7**: the defining identity `H^i ∘ (quotient functor) ≅ Q ∘ H^i`.

```lean
def cohomologyDerivedCategoryQuasicoherentSheafFac (i : ℤ) :
    toDerivedCategoryQuasicoherentSheaf B S hS 𝒳 ⋙
        cohomologyDerivedCategoryQuasicoherentSheaf B S hS 𝒳 i ≅
      DerivedCategoryB.cohomologyComp (lqcFbcFppf B S hS 𝒳)
        (flatGroupoidPresentation 𝒳).flatBaseChangeCoherator i
```

**`AlgebraicGeometry.Stack.isHomological_cohomologyDerivedCategoryQuasicoherentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean#L324). The attribute's comment: “the descended H^i : D_QCoh(𝒪_𝒳) ⟶ QCoh(𝒪_𝒳) is a cohomological functor”.

> **Stacks 07B7**: `H^i : D_QCoh(𝒪_𝒳) ⟶ QCoh(𝒪_𝒳)` is a cohomological functor.

```lean
theorem isHomological_cohomologyDerivedCategoryQuasicoherentSheaf (i : ℤ) :
    (cohomologyDerivedCategoryQuasicoherentSheaf B S hS 𝒳 i).IsHomological
```

**`AlgebraicGeometry.Stack.isZero_iff_forall_isZero_cohomologyDerivedCategoryQuasicoherentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentCohomologySheaf.lean#L332). The attribute's comment: “E is zero in D_QCoh(𝒪_𝒳) if and only if H^i(E) = 0 for every i”.

> **Stacks 07B7**: an object `E` of `D_QCoh(𝒪_𝒳)` is zero exactly when `H^i(E) = 0` for all
> `i`, the kernel of `Q` being exactly `Parasitic(𝒪_𝒳) ∩ LQCoh^fbc(𝒪_𝒳)` (Stacks 0779 (1)).

```lean
theorem isZero_iff_forall_isZero_cohomologyDerivedCategoryQuasicoherentSheaf
    (X : derivedCategoryQuasicoherentSheaf B S hS 𝒳) :
    IsZero X ↔ ∀ i : ℤ,
      IsZero ((cohomologyDerivedCategoryQuasicoherentSheaf B S hS 𝒳 i).obj X)
```

## Tag 07B8, a lemma

[Tag 07B8](https://stacks.math.columbia.edu/tag/07B8) in the Stacks Project.

**`AlgebraicGeometry.Stack.epsilonPullbackDerived`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean#L328). The attribute's comment: “the right-hand vertical arrow ε^* : D(𝒳_étale, 𝒪_𝒳) ⥤ D(𝒪_𝒳) of the diagram”.

> **The right-hand vertical arrow of the diagram of Stacks 07B8**, the triangulated functor
> `ε^* : D(𝒳_étale, 𝒪_𝒳) ⥤ D(𝒪_𝒳)` induced by the exact functor `ε^*` on modules.

```lean
def epsilonPullbackDerived :
    DerivedCategory (etaleModules B S hS 𝒳) ⥤ DerivedCategory (fppfModules B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.epsilonPullbackDerivedLocallyQuasicoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean#L400). The attribute's comment: “the middle vertical arrow ε^* : D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) ⥤ D_{LQCoh^fbc}(𝒪_𝒳) of the diagram”.

> **Stacks 07B8, the middle vertical arrow of the diagram.**  The functor
>
> `ε^* : D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) ⥤ D_{LQCoh^fbc}(𝒪_𝒳)`,
>
> the corestriction to `D_{LQCoh^fbc}(𝒪_𝒳)` of `ε^*` on the ambient derived categories.

```lean
def epsilonPullbackDerivedLocallyQuasicoherent :
    (derivedLocallyQuasicoherentFlatBaseChangeEtale B E h S hS 𝒳).FullSubcategory ⥤
      (derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳).FullSubcategory
```

**`AlgebraicGeometry.Stack.epsilonPullbackDerivedParasitic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean#L417). The attribute's comment: “the left vertical arrow ε^* : D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ⥤ D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳) of the diagram”.

> **Stacks 07B8, the left vertical arrow of the diagram.**  The functor
>
> `ε^* : D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ⥤ D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`,
>
> the corestriction to `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` of `ε^*` on the ambient derived
> categories.

```lean
def epsilonPullbackDerivedParasitic :
    (derivedParasiticLocallyQuasicoherentFlatBaseChangeEtale B E h S hS 𝒳).FullSubcategory ⥤
      (derivedParasiticLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳).FullSubcategory
```

**`AlgebraicGeometry.Stack.epsilonPullbackDerived_rightSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean#L436). The attribute's comment: “the right-hand square of the diagram: the inclusion D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) ⊆ D(𝒳_étale, 𝒪_𝒳) followed by ε^* is ε^* followed by the inclusion D_{LQCoh^fbc}(𝒪_𝒳) ⊆ D(𝒪_𝒳)”.

> **Stacks 07B8, the right-hand square of the diagram commutes.**  Going along the bottom row
> from `D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳)` into `D(𝒳_étale, 𝒪_𝒳)` and then up by `ε^*` is going up by
> `ε^*` into `D_{LQCoh^fbc}(𝒪_𝒳)` and then along the top row into `D(𝒪_𝒳)`.
>
> This is an equality of functors, not merely an isomorphism: the middle vertical arrow is by
> construction the corestriction of `ε^*`.

```lean
theorem epsilonPullbackDerived_rightSquare :
    (derivedLocallyQuasicoherentFlatBaseChangeEtale B E h S hS 𝒳).ι ⋙
        epsilonPullbackDerived B S hS 𝒳 =
      epsilonPullbackDerivedLocallyQuasicoherent B E h S hS 𝒳 hfppfSheaf ⋙
        (derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳).ι
```

**`AlgebraicGeometry.Stack.epsilonPullbackDerived_leftSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean#L450). The attribute's comment: “the left-hand square of the diagram: the inclusion D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ⊆ D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) followed by ε^* is ε^* followed by the inclusion D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳) ⊆ D_{LQCoh^fbc}(𝒪_𝒳)”.

> **Stacks 07B8, the left-hand square of the diagram commutes.**  Going along the bottom row
> from `D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳)` into `D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳)` and then up by `ε^*` is going up
> by `ε^*` into `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` and then along the top row into
> `D_{LQCoh^fbc}(𝒪_𝒳)`.

```lean
theorem epsilonPullbackDerived_leftSquare :
    ObjectProperty.ιOfLE
          (derivedParasiticLocallyQuasicoherentFlatBaseChangeEtale_le B E h S hS 𝒳) ⋙
        epsilonPullbackDerivedLocallyQuasicoherent B E h S hS 𝒳 hfppfSheaf =
      epsilonPullbackDerivedParasitic B E h S hS 𝒳 hfppfSheaf ⋙
        ObjectProperty.ιOfLE
          (derivedParasiticLocallyQuasicoherentFlatBaseChange_le B E h S hS 𝒳)
```

**`AlgebraicGeometry.Stack.epsilonPullbackDerived_outerRectangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean#L462). The attribute's comment: “the outer rectangle of the diagram, the composite of its two squares”.

> **Stacks 07B8, the outer rectangle of the diagram commutes**: the composite of the two
> squares, read from `D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳)` to `D(𝒪_𝒳)`.

```lean
theorem epsilonPullbackDerived_outerRectangle :
    (derivedParasiticLocallyQuasicoherentFlatBaseChangeEtale B E h S hS 𝒳).ι ⋙
        epsilonPullbackDerived B S hS 𝒳 =
      epsilonPullbackDerivedParasitic B E h S hS 𝒳 hfppfSheaf ⋙
        (derivedParasiticLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳).ι
```

**`AlgebraicGeometry.Stack.derivedCategoryQuasicoherentEtaleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentEtaleComparison.lean#L524). The attribute's comment: “the last assertion: the induced equivalence D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) / D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ⟶ D_QCoh(𝒪_𝒳), given that the middle vertical arrow is an equivalence matching the two inverted classes”.

> **Stacks 07B8, the last assertion.**  If the middle vertical arrow
>
> `ε^* : D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) ⥤ D_{LQCoh^fbc}(𝒪_𝒳)`
>
> is an equivalence of triangulated categories and matches the two classes of morphisms the
> Verdier quotients invert, then it descends to an equivalence
>
> `D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) / D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ≌ D_QCoh(𝒪_𝒳)`.
>
> The two hypotheses are the source's own "moreover": `hG` is "the middle vertical arrow is an
> equivalence of triangulated categories", which the source gets from **Stacks 07A8** together
> with **Stacks 0D7W** — both of which the library has, but only for a site whose objects and
> morphisms share a universe; see the module docstring — and
> `hW` is the matching of the inverted classes, which comes from the compatibility of `ε^*` with
> the left vertical arrow, the verification the source explicitly omits.
>
> Given them the descent is formal: `ε^*` followed by the quotient functor of **Stacks 07B6** is
> again a localization at the étale class, by transport of a localization along an equivalence of
> the source category, and two localizations at one and the same class of morphisms are
> canonically equivalent.

```lean
def derivedCategoryQuasicoherentEtaleEquivalence
    (hG : (epsilonPullbackDerivedLocallyQuasicoherent B E h S hS 𝒳 hfppfSheaf).IsEquivalence)
    (hW : derivedQuasicoherentWEtale B E h S hS 𝒳 =
      (derivedQuasicoherentW B E h S hS 𝒳).inverseImage
        (epsilonPullbackDerivedLocallyQuasicoherent B E h S hS 𝒳 hfppfSheaf)) :
    derivedCategoryQuasicoherentEtale B E h S hS 𝒳 ≌
      derivedCategoryQuasicoherent B E h S hS 𝒳
```

**`AlgebraicGeometry.Stack.epsilonPullbackDerivedSheafFlatBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean#L169). The attribute's comment: “the middle vertical arrow ε^* : D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) ⥤ D_{LQCoh^fbc}(𝒪_𝒳) of the diagram, for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves”.

> **Stacks 07B8, the middle vertical arrow of the diagram**,
>
> `ε^* : D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) ⥤ D_{LQCoh^fbc}(𝒪_𝒳)`,
>
> with `LQCoh^fbc` read with the flat base change property of Stacks 0762 for the pullback of
> sheaves: the corestriction of `ε^*` on the ambient derived categories.

```lean
abbrev epsilonPullbackDerivedSheafFlatBaseChange :
    (DerivedCategoryB.derivedCategoryB
        (locallyQuasicoherentSheafFlatBaseChangeEtaleModules B E h S hS 𝒳)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryB
        (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)).FullSubcategory
```

**`AlgebraicGeometry.Stack.epsilonPullbackDerivedParasiticSheafFlatBaseChange`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean#L188). The attribute's comment: “the left vertical arrow ε^* : D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ⥤ D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳) of the diagram, for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves”.

> **Stacks 07B8, the left vertical arrow of the diagram**,
>
> `ε^* : D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ⥤ D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`,
>
> with `LQCoh^fbc` read with the flat base change property of Stacks 0762 for the pullback of
> sheaves: the corestriction of `ε^*` on the ambient derived categories.

```lean
abbrev epsilonPullbackDerivedParasiticSheafFlatBaseChange :
    (derivedInter (parasiticModules.{u, w, u} B S hS 𝒳 .etale)
        (locallyQuasicoherentSheafFlatBaseChangeEtaleModules B E h S hS 𝒳)).FullSubcategory ⥤
      (derivedInter (parasiticModules.{u, w, u} B S hS 𝒳 .fppf)
        (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)).FullSubcategory
```

**`AlgebraicGeometry.Stack.epsilonPullbackDerivedSheafFlatBaseChange_rightSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean#L206). The attribute's comment: “the right-hand square of the diagram, for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves”.

> **Stacks 07B8, the right-hand square of the diagram commutes**: the inclusion
> `D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) ⊆ D(𝒳_étale, 𝒪_𝒳)` followed by `ε^*` is `ε^*` followed by the
> inclusion `D_{LQCoh^fbc}(𝒪_𝒳) ⊆ D(𝒪_𝒳)`, as an equality of functors.

```lean
theorem epsilonPullbackDerivedSheafFlatBaseChange_rightSquare :
    (DerivedCategoryB.derivedCategoryB
        (locallyQuasicoherentSheafFlatBaseChangeEtaleModules B E h S hS 𝒳)).ι ⋙
        epsilonPullbackDerived B S hS 𝒳 =
      epsilonPullbackDerivedSheafFlatBaseChange B E h S hS 𝒳 ⋙
        (DerivedCategoryB.derivedCategoryB
          (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)).ι
```

**`AlgebraicGeometry.Stack.epsilonPullbackDerivedSheafFlatBaseChange_leftSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean#L241). The attribute's comment: “the left-hand square of the diagram, for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves”.

> **Stacks 07B8, the left-hand square of the diagram commutes**: the inclusion
> `D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ⊆ D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳)` followed by `ε^*` is `ε^*` followed by
> the inclusion `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳) ⊆ D_{LQCoh^fbc}(𝒪_𝒳)`, as an equality of
> functors.

```lean
theorem epsilonPullbackDerivedSheafFlatBaseChange_leftSquare :
    ObjectProperty.ιOfLE (derivedParasiticSheafFlatBaseChangeEtale_le B E h S hS 𝒳) ⋙
        epsilonPullbackDerivedSheafFlatBaseChange B E h S hS 𝒳 =
      epsilonPullbackDerivedParasiticSheafFlatBaseChange B E h S hS 𝒳 ⋙
        ObjectProperty.ιOfLE (derivedParasiticSheafFlatBaseChange_le B E h S hS 𝒳)
```

**`AlgebraicGeometry.Stack.isEquivalence_epsilonPullbackDerivedSheafFlatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean#L296). The attribute's comment: “the middle vertical arrow is an equivalence of triangulated categories, for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves”.

> **Stacks 07B8, the middle vertical arrow is an equivalence of triangulated categories**:
>
> `ε^* : D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) ⥤ D_{LQCoh^fbc}(𝒪_𝒳)`
>
> is an equivalence, and it is a triangulated functor for the triangulated structures of the two
> strictly full triangulated subcategories, `LQCoh^fbc` being a weak Serre subcategory on both
> sites.

```lean
theorem isEquivalence_epsilonPullbackDerivedSheafFlatBaseChange :
    (epsilonPullbackDerivedSheafFlatBaseChange B E h S hS 𝒳).IsEquivalence ∧
      (epsilonPullbackDerivedSheafFlatBaseChange B E h S hS 𝒳).IsTriangulated
```

**`AlgebraicGeometry.Stack.isEquivalence_epsilonPullbackDerivedParasiticSheafFlatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean#L345). The attribute's comment: “the left vertical arrow is an equivalence of triangulated categories, for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves”.

> **Stacks 07B8, the left vertical arrow is an equivalence of triangulated categories**:
>
> `ε^* : D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ⥤ D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`
>
> is an equivalence, and it is a triangulated functor, `Parasitic ∩ LQCoh^fbc` being a weak Serre
> subcategory on both sites. This includes the verification the source omits, that the
> equivalence of the middle arrow matches the complexes with parasitic cohomology sheaves.

```lean
theorem isEquivalence_epsilonPullbackDerivedParasiticSheafFlatBaseChange :
    (epsilonPullbackDerivedParasiticSheafFlatBaseChange B E h S hS 𝒳).IsEquivalence ∧
      (epsilonPullbackDerivedParasiticSheafFlatBaseChange B E h S hS 𝒳).IsTriangulated
```

**`AlgebraicGeometry.Stack.derivedCategoryQuasicoherentEtaleSheafFlatBaseChangeEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeEtaleFppfDerivedEquivalence.lean#L364). The attribute's comment: “the last assertion: the induced equivalence D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) / D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ≌ D_QCoh(𝒪_𝒳), for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves”.

> **Stacks 07B8, the last assertion**: the equivalence
>
> `D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) / D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳) ≌ D_QCoh(𝒪_𝒳)`
>
> induced by `ε^*`, where `D_QCoh(𝒪_𝒳)` is the Verdier quotient
> `D_{LQCoh^fbc}(𝒪_𝒳) / D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` of **Stacks 07B6**,
> `AlgebraicGeometry.Stack.ParasiticQuotient.quotient`. The middle vertical arrow is an equivalence
> matching the classes of morphisms the two Verdier quotients invert, because it matches the
> complexes with parasitic cohomology; see
> `DerivedCategory.KernelColocalization.quotientEquivalenceOfExactFunctor`. That it is induced by
> `ε^*` is `toQuotientCompDerivedCategoryQuasicoherentEtaleSheafFlatBaseChangeEquivalenceIso`.

```lean
def derivedCategoryQuasicoherentEtaleSheafFlatBaseChangeEquivalence :
    quotient (parasiticModules.{u, w, u} B S hS 𝒳 .etale)
        (locallyQuasicoherentSheafFlatBaseChangeEtaleModules B E h S hS 𝒳) ≌
      ParasiticQuotient.quotient B S hS 𝒳
        (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)
```

## Tag 07B9, a lemma

[Tag 07B9](https://stacks.math.columbia.edu/tag/07B9) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.isZero_derivedModuleRestriction_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedFlatFppfRestriction.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedFlatFppfRestriction.lean#L288). The attribute's comment: “part (2)(b), the kernel of g^* on D_LQCoh^fbc(𝒪_𝒳): g^*K = 0 exactly when K lies in D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳), with g^* restriction to the flat-fppf site”.

> **Stacks 07B9** (2)(b).  Let `𝒳` be an algebraic stack and set
> `𝒫_𝒳 = Parasitic(𝒪_𝒳) ∩ LQCoh^fbc(𝒪_𝒳)`.  For a complex `K` of `𝒪_𝒳`-modules lying in
> `D_{LQCoh^fbc}(𝒪_𝒳)`, the restriction `g^*K` to the flat-fppf site of **Stacks 0787** vanishes
> exactly when `K` lies in `D_{𝒫_𝒳}(𝒪_𝒳)`.
>
> Here `g^*` is restriction along the inclusion of the flat objects, which is pullback along the
> morphism of ringed topoi of **Stacks 0788** (2) by **Stacks 0788**, `flat_ringed`, and which needs
> no derivation because it is exact.  `D_{𝒫_𝒳}(𝒪_𝒳)` is
> `AlgebraicGeometry.Stack.derivedParasiticLocallyQuasicoherentFlatBaseChange`, the subcategory the
> Verdier quotient of **Stacks 07B6** divides by.
>
> The local quasi-coherence and flat base change half of the right-hand side is free given the
> hypothesis on `K`; the content is the parasitic half, which is
> `AlgebraicGeometry.Stack.FlatFppf.isZero_derivedModuleRestriction_iff_forall_isParasitic`.

```lean
theorem isZero_derivedModuleRestriction_iff {E : BigEtaleSite.{u}} {h : E.cutoff = B.cutoff}
    (K : DerivedCategory (fppfModules B S hS 𝒳))
    (hK : derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳 K) :
    IsZero ((derivedModuleRestriction B S hS 𝒳).obj K) ↔
      derivedParasiticLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳 K
```

**`AlgebraicGeometry.Stack.FlatFppf.toDerivedCategoryQuasicoherentCompRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedFlatFppfRestriction.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedFlatFppfRestriction.lean#L337). The attribute's comment: “part (2)(d), the functor c : D_QCoh(𝒪_𝒳) ⥤ D(𝒪_{𝒳_flat,fppf}) that g^* induces on the Verdier quotient of 07B6, together with its factorization through the quotient functor; the mutual inverseness of c with Lg_! is not covered”.

> **Stacks 07B9** (2)(d), the commutativity the functor `c` is characterized by: composing the
> quotient functor `D_{LQCoh^fbc}(𝒪_𝒳) ⟶ D_QCoh(𝒪_𝒳)` of **Stacks 07B6** with `c` gives back
> restriction to the flat-fppf site.  This is what pins `c` down; it is the "inner triangle
> commutes" of the source's proof.

```lean
def toDerivedCategoryQuasicoherentCompRestriction :
    toDerivedCategoryQuasicoherent B E h S hS 𝒳 ⋙
        derivedQuasicoherentModuleRestriction B S hS 𝒳 E h ≅
      (derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳).ι ⋙
        derivedModuleRestriction B S hS 𝒳
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedCategoryB_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedQuasicoherentLowerShriek.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedQuasicoherentLowerShriek.lean#L68). The attribute's comment: “part (2)(c): Lg_! carries D_QCoh(𝒪_{𝒳_flat,fppf}) into D_LQCoh^fbc(𝒪_𝒳), for the derived lower shriek of Stacks 07AS (4) and LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves, at module universe u, at the standard models of the derived categories”.

> **Stacks 07B9** (2)(c).  `Lg_!` carries `D_QCoh(𝒪_{𝒳_{flat,fppf}})` into `D_{LQCoh^fbc}(𝒪_𝒳)`,
> the flat base change property of Stacks 0762 being read with the pullback of sheaves.
>
> This is the dévissage of the source
> (`AlgebraicGeometry.Stack.FlatFppf.derivedCategoryB_derivedModuleLowerShriek_of_single`): `Lg_!` is
> triangulated, right t-exact and commutes with direct sums, `LQCoh^fbc(𝒪_𝒳)` is weak Serre and
> closed under colimits of sequences (Stacks 0771 (2), (5)), and on a quasi-coherent module in
> degree `0` it is Stacks 07B3 (2).

```lean
theorem derivedCategoryB_derivedModuleLowerShriek :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    letI := HasDerivedCategory.standard (flatFppfModules B S hS 𝒳)
    ∀ H : DerivedCategory (flatFppfModules B S hS 𝒳),
      DerivedCategoryB.derivedCategoryB (flatQuasicoherentModules B S hS 𝒳) H →
        DerivedCategoryB.derivedCategoryB
          (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)
          ((derivedModuleLowerShriek B S hS 𝒳).obj H)
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedQuasicoherentLowerShriek.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedQuasicoherentLowerShriek.lean#L109). The attribute's comment: “part (2)(d): g^* and Lg_! define mutually inverse equivalences between D_QCoh(𝒪_𝒳), the Verdier quotient of Stacks 07B6, and D_QCoh(𝒪_{𝒳_flat,fppf}): the functor is induced by g^*, the inverse is q ∘ Lg_!; for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves, at module universe u, at the standard models of the derived categories”.

> **Stacks 07B9** (2)(d).  Restriction `g^*` to the flat-fppf site and `Lg_!` define mutually
> inverse equivalences between `D_QCoh(𝒪_𝒳)` — the Verdier quotient
> `D_{LQCoh^fbc}(𝒪_𝒳) / D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` of Stacks 07B6 — and
> `D_QCoh(𝒪_{𝒳_{flat,fppf}})`, the flat base change property of Stacks 0762 being read with the
> pullback of sheaves.  The functor is the functor `c` induced by `g^*` (Stacks 07B9 (2)(a), (2)(b)),
> the inverse is `q ∘ Lg_!` (Stacks 07B9 (2)(c));
> see `AlgebraicGeometry.Stack.FlatFppf.derivedQuasicoherentEquivalenceOfSingle`.

```lean
def derivedQuasicoherentEquivalence :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    letI := HasDerivedCategory.standard (flatFppfModules B S hS 𝒳)
    ParasiticQuotient.quotient B S hS 𝒳
        (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) ≌
      (DerivedCategoryB.derivedCategoryB (flatQuasicoherentModules B S hS 𝒳)).FullSubcategory
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedCategoryB_derivedModuleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedQuasicoherentRestriction.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedQuasicoherentRestriction.lean#L104). The attribute's comment: “part (2)(a): for K in D_LQCoh^fbc(𝒪_𝒳) the restriction g^*K to the flat-fppf site lies in D_QCoh(𝒪_{𝒳_flat,fppf}), for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves, at module universe u, for any models of the derived categories”.

> **Stacks 07B9** (2)(a).  For `K` in `D_{LQCoh^fbc}(𝒪_𝒳)` (with the flat base change property
> of Stacks 0762 read with the pullback of sheaves), the restriction `g^*K` to the flat-fppf site
> lies in `D_QCoh(𝒪_{𝒳_{flat,fppf}})`: `g^*` is exact, so `H^n(g^*K) = g^*H^n(K)`, which is
> quasi-coherent by Stacks 07B1 (2)(b).

```lean
theorem derivedCategoryB_derivedModuleRestriction (K : DerivedCategory (fppfModules B S hS 𝒳))
    (hK : DerivedCategoryB.derivedCategoryB
      (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) K) :
    DerivedCategoryB.derivedCategoryB (flatQuasicoherentModules B S hS 𝒳)
      ((derivedModuleRestriction B S hS 𝒳).obj K)
```

**`AlgebraicGeometry.Stack.FlatFppf.isZero_derivedModuleRestriction_iff_derivedParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedQuasicoherentRestriction.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfDerivedQuasicoherentRestriction.lean#L122). The attribute's comment: “part (2)(b): for K in D_LQCoh^fbc(𝒪_𝒳), g^*K = 0 if and only if K lies in D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳), for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves, at module universe u, for any models of the derived categories”.

> For `K` in `D_{LQCoh^fbc}(𝒪_𝒳)` (with the flat base change property of Stacks 0762 read with
> the pullback of sheaves), `g^*K = 0` exactly when `K` lies in `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`:
> `g^*K = 0` exactly when every cohomology module of `K` is parasitic
> (`isZero_derivedModuleRestriction_iff_forall_isParasitic`, Stacks 07AR), and the `LQCoh^fbc` half
> is the hypothesis on `K`.

```lean
theorem isZero_derivedModuleRestriction_iff_derivedParasitic
    (K : DerivedCategory (fppfModules B S hS 𝒳))
    (hK : DerivedCategoryB.derivedCategoryB
      (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) K) :
    IsZero ((derivedModuleRestriction B S hS 𝒳).obj K) ↔
      ParasiticQuotient.derivedParasitic B S hS 𝒳
        (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) K
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedQuasicoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedQuasicoherentEquivalence.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedQuasicoherentEquivalence.lean#L122). The attribute's comment: “part (1)(d): g^* and Lg_! define mutually inverse equivalences between D_QCoh(𝒪_𝒳), the Verdier quotient of Stacks 07B6, and D_QCoh(𝒪_{𝒳_lisse,étale}), through the equivalence of Stacks 07B8; the inverse is q ∘ ε^* ∘ Lg_! (derivedQuasicoherentEquivalenceInverseIso); for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves, at module universe u, at the standard models of the derived categories”.

> **Stacks 07B9** (1)(d).  Restriction `g^*` to the lisse-étale site and `Lg_!` define mutually
> inverse equivalences between `D_QCoh(𝒪_𝒳)` — the Verdier quotient
> `D_{LQCoh^fbc}(𝒪_𝒳) / D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` of Stacks 07B6 — and
> `D_QCoh(𝒪_{𝒳_{lisse,étale}})`, the flat base change property of Stacks 0762 being read with the
> pullback of sheaves.
>
> As in the source, `D_QCoh(𝒪_𝒳)` is identified with
> `D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳) / D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳)` by Stacks 07B8
> (`AlgebraicGeometry.Stack.derivedCategoryQuasicoherentEtaleSheafFlatBaseChangeEquivalence`, induced
> by `ε^*`), and on that quotient `g^*` and `q ∘ Lg_!` are mutually inverse
> (`AlgebraicGeometry.Stack.LisseEtale.etaleQuotientDerivedQuasicoherentEquivalence`).  Stated at the
> standard models of the derived categories, where Stacks 07B3 (1) is.

```lean
def derivedQuasicoherentEquivalence :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    letI := HasDerivedCategory.standard (SheafOfModules.{u} (lisseEtaleModuleRing B S hS 𝒳))
    ParasiticQuotient.quotient B S hS 𝒳
        (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) ≌
      (DerivedCategoryB.derivedCategoryB (lisseQuasicoherentModules B S hS 𝒳)).FullSubcategory
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedCategoryB_derivedModuleRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedQuasicoherentRestriction.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedQuasicoherentRestriction.lean#L200). The attribute's comment: “part (1)(a): for F in D_LQCoh^fbc(𝒳_étale, 𝒪_𝒳) the restriction g^*F to the lisse-étale site lies in D_QCoh(𝒪_{𝒳_lisse,étale}), for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves, at module universe u, for any models of the derived categories”.

> **Stacks 07B9** (1)(a).  For `K` in `D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳)` (with the flat base change
> property of Stacks 0762 read with the pullback of sheaves), `g^*K` lies in
> `D_QCoh(𝒪_{𝒳_{lisse,étale}})`: `H^n(g^*K) = g^*H^n(K)` is quasi-coherent by Stacks 07B1 (1)(b).

```lean
theorem derivedCategoryB_derivedModuleRestriction
    (K : DerivedCategory (etaleModules B S hS 𝒳))
    (hK : DerivedCategoryB.derivedCategoryB
      (locallyQuasicoherentSheafFlatBaseChangeEtaleModules B E h S hS 𝒳) K) :
    DerivedCategoryB.derivedCategoryB (lisseQuasicoherentModules B S hS 𝒳)
      ((derivedModuleRestriction B S hS 𝒳).obj K)
```

**`AlgebraicGeometry.Stack.LisseEtale.isZero_derivedModuleRestriction_iff_derivedParasitic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedQuasicoherentRestriction.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedQuasicoherentRestriction.lean#L216). The attribute's comment: “part (1)(b): for F in D_LQCoh^fbc(𝒳_étale, 𝒪_𝒳), g^*F = 0 if and only if F lies in D_{𝒫_𝒳}(𝒳_étale, 𝒪_𝒳), 𝒫_𝒳 = Parasitic ∩ LQCoh^fbc, for LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves, at module universe u, for any models of the derived categories”.

> **Stacks 07B9** (1)(b).  For `K` in `D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳)`, `g^*K = 0` exactly when
> `K` lies in `D_{Parasitic ∩ LQCoh^fbc}(𝒳_étale, 𝒪_𝒳)`.

```lean
theorem isZero_derivedModuleRestriction_iff_derivedParasitic
    (K : DerivedCategory (etaleModules B S hS 𝒳))
    (hK : DerivedCategoryB.derivedCategoryB
      (locallyQuasicoherentSheafFlatBaseChangeEtaleModules B E h S hS 𝒳) K) :
    IsZero ((derivedModuleRestriction B S hS 𝒳).obj K) ↔
      DerivedCategory.KernelColocalization.derivedInter (parasiticModules.{u, w, u} B S hS 𝒳 .etale)
        (locallyQuasicoherentSheafFlatBaseChangeEtaleModules B E h S hS 𝒳) K
```

**`AlgebraicGeometry.Stack.LisseEtale.derivedCategoryB_derivedModuleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedQuasicoherentRestriction.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleDerivedQuasicoherentRestriction.lean#L280). The attribute's comment: “part (1)(c): Lg_! carries D_QCoh(𝒪_{𝒳_lisse,étale}) into D_LQCoh^fbc(𝒳_étale, 𝒪_𝒳), for the derived lower shriek of Stacks 07AS (2) and LQCoh^fbc with the flat base change property of Stacks 0762 read with the pullback of sheaves, at module universe u, at the standard models of the derived categories”.

> **Stacks 07B9** (1)(c).  `Lg_!` carries `D_QCoh(𝒪_{𝒳_{lisse,étale}})` into
> `D_{LQCoh^fbc}(𝒳_étale, 𝒪_𝒳)`, the flat base change property of Stacks 0762 being read with the
> pullback of sheaves.
>
> This is the dévissage of the source (`DerivedCategory.derivedCategoryB_obj_of_isLE_obj`): `Lg_!`
> is triangulated, right t-exact (its right adjoint `g^*` is exact) and commutes with direct sums;
> `LQCoh^fbc` is a weak Serre subcategory closed under colimits of sequences (Stacks 0771 (2), (5));
> and on a quasi-coherent module in degree `0` it is Stacks 07B3 (1)
> (`isLocallyQuasicoherentWithSheafFlatBaseChange_homology_derivedModuleLowerShriek`). It is
> stated at the standard models of the derived categories, where Stacks 07B3 (1) is.

```lean
theorem derivedCategoryB_derivedModuleLowerShriek :
    letI := HasDerivedCategory.standard (SheafOfModules.{u} (lisseEtaleModuleRing B S hS 𝒳))
    letI := HasDerivedCategory.standard (SheafOfModules.{u} (lisseAmbientRing B S hS 𝒳))
    ∀ H : DerivedCategory (SheafOfModules.{u} (lisseEtaleModuleRing B S hS 𝒳)),
      DerivedCategoryB.derivedCategoryB (lisseQuasicoherentModules B S hS 𝒳) H →
        DerivedCategoryB.derivedCategoryB
          (fun F : SheafOfModules.{u} (lisseAmbientRing B S hS 𝒳) =>
            IsLocallyQuasicoherentWithSheafFlatBaseChange.{u, u + 1, u, u} B E h S hS
              𝒳.val.val.p 𝒳.val.isFiberedInGroupoids F.val)
          ((derivedModuleLowerShriek B S hS 𝒳).obj H)
```

## Tag 07BA, a lemma

[Tag 07BA](https://stacks.math.columbia.edu/tag/07BA) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.leftOrthogonal_parasiticFreePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticColocalizationTriangle.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticColocalizationTriangle.lean#L199). The attribute's comment: “the orthogonality: Hom_D(𝒪_𝒳)(E', P') = 0 for every P' in D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳), at E' = Lg_! g^* E; conditional on the derived module-level Lg_! of 07AS (4), carried as the hypotheses Lsh and adj”.

> **Stacks 07BA**, the orthogonality of the first term.  Every morphism from
> `K' = Lg_! g^* K` to an object `P'` of `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` vanishes, i.e. `K'` lies
> in the left orthogonal of `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`.
>
> Indeed `Hom(Lg_! g^* K, P') = Hom(g^* K, g^* P')` by the adjunction, and `g^* P' = 0` by
> **Stacks 07B9** (2)(b), so the right-hand group vanishes.

```lean
theorem leftOrthogonal_parasiticFreePart (K : DerivedCategory (fppfModules B S hS 𝒳)) :
    (derivedParasiticLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳).leftOrthogonal
      (parasiticFreePart B S hS 𝒳 Lsh K)
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedParasitic_obj₃_of_distTriang_parasiticFreePartHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticColocalizationTriangle.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticColocalizationTriangle.lean#L225). The attribute's comment: “the cone: for E' = Lg_! g^* E and E' ⟶ E the counit, every distinguished triangle E' ⟶ E ⟶ P ⟶ E'[1] has P in D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳), and all three terms in D_LQCoh^fbc(𝒪_𝒳); conditional on the derived module-level Lg_! of 07AS (4) and on 07B9 (2)(a), (2)(c), carried as the hypotheses Lsh, adj, hunit and hK'”.

> **Stacks 07BA**, the third term of the triangle.  Let `K` be an object of
> `D_{LQCoh^fbc}(𝒪_𝒳)` whose parasitic-free part `K' = Lg_! g^* K` again lies in
> `D_{LQCoh^fbc}(𝒪_𝒳)` — that is **Stacks 07B9** (2)(a) followed by (2)(c), carried as the
> hypothesis `hK'`.  Then every cone `P` on the canonical morphism `ε_K : K' ⟶ K` lies in
> `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`.
>
> Local quasi-coherence with flat base change is two out of three in the triangle.  For the
> parasitic half, `g^*` is exact hence triangulated, and it inverts `ε_K`, so the third term of the
> image triangle vanishes: `g^* P = 0`, which is the parasitic condition by
> **Stacks 07B9** (2)(b).

```lean
theorem derivedParasitic_obj₃_of_distTriang_parasiticFreePartHom (hunit : IsIso adj.unit)
    (K : DerivedCategory (fppfModules B S hS 𝒳))
    (hK : derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳 K)
    (hK' : derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳
      (parasiticFreePart B S hS 𝒳 Lsh K))
    (P : DerivedCategory (fppfModules B S hS 𝒳)) (b : K ⟶ P)
    (c : P ⟶ (parasiticFreePart B S hS 𝒳 Lsh K)⟦(1 : ℤ)⟧)
    (hT : Triangle.mk (parasiticFreePartHom B S hS 𝒳 Lsh adj K) b c ∈
      distTriang (DerivedCategory (fppfModules B S hS 𝒳))) :
    derivedParasiticLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳 P
```

**`AlgebraicGeometry.Stack.FlatFppf.extensionProduct_parasiticFreePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticColocalizationTriangle.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ParasiticColocalizationTriangle.lean#L260). The attribute's comment: “the existence of the triangle: every E in D_LQCoh^fbc(𝒪_𝒳) is an extension of an object of D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳) by an object of D_LQCoh^fbc(𝒪_𝒳) left orthogonal to it, the extension being the canonical one on Lg_! g^* E ⟶ E; conditional on the derived module-level Lg_! of 07AS (4) and on 07B9 (2)(a), (2)(c)”.

> **Stacks 07BA**, in the shape the source states it.  Every object `K` of
> `D_{LQCoh^fbc}(𝒪_𝒳)` whose parasitic-free part lies in `D_{LQCoh^fbc}(𝒪_𝒳)` fits in a
> distinguished triangle
>
> `K' ⟶ K ⟶ P ⟶ K'[1]`
>
> with `P` in `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` and `K'` in `D_{LQCoh^fbc}(𝒪_𝒳)` and left
> orthogonal to `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`.
>
> This is the existential reading of the two statements above, obtained by completing the
> canonical morphism `ε_K` to a distinguished triangle; `K'` and `ε_K` themselves are the
> `AlgebraicGeometry.Stack.FlatFppf.parasiticFreePart` and
> `AlgebraicGeometry.Stack.FlatFppf.parasiticFreePartHom` of the canonical triangle.

```lean
theorem extensionProduct_parasiticFreePart (hunit : IsIso adj.unit)
    (K : DerivedCategory (fppfModules B S hS 𝒳))
    (hK : derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳 K)
    (hK' : derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳
      (parasiticFreePart B S hS 𝒳 Lsh K)) :
    (((derivedParasiticLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳).leftOrthogonal ⊓
        derivedLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳).extensionProduct
      (derivedParasiticLocallyQuasicoherentFlatBaseChange B E h S hS 𝒳)) K
```

**`AlgebraicGeometry.Stack.FlatFppf.leftOrthogonal_sheafParasiticFreePart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean#L108). The attribute's comment: “the orthogonality: Hom_D(𝒪_𝒳)(E', P') = 0 for every P' in D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳), at E' = Lg_! g^* E, for the faithful class LQCoh^fbc of Stacks 0762 (flat base change read with the pullback of sheaves), the actual derived lower shriek Lg_! of Stacks 07AS (4) and any models of the derived categories, with no hypothesis”.

> **Stacks 07BA**, the orthogonality: `Hom(Lg_! g^* E, P') = Hom(g^* E, g^* P') = 0` for every
> `P'` in `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`.

```lean
theorem leftOrthogonal_sheafParasiticFreePart (K : DerivedCategory (fppfModules B S hS 𝒳)) :
    (ParasiticQuotient.derivedParasitic B S hS 𝒳
      (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)).leftOrthogonal
      (sheafParasiticFreePart B S hS 𝒳 K)
```

**`AlgebraicGeometry.Stack.FlatFppf.exists_iso_sheafParasiticColocalizationTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean#L197). The attribute's comment: “the canonicity of the triangle: a distinguished triangle E'' ⟶ E ⟶ P'' ⟶ E''[1] with E'' left orthogonal to D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳) and P'' in it is isomorphic to the triangle on Lg_! g^* E ⟶ E by an isomorphism which is the identity on E (Stacks 0CQP), for the faithful class LQCoh^fbc, any models of the derived categories, with no hypothesis”.

> **Stacks 07BA, canonicity** ([Stacks, Tag 0CQP]): a distinguished triangle
> `E'' ⟶ E ⟶ P'' ⟶ E''[1]` with `E''` left orthogonal to `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` and
> `P''` in it is isomorphic to any distinguished triangle on the canonical morphism
> `Lg_! g^* E ⟶ E` whose third term lies in `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`, by an isomorphism of
> triangles which is the identity on `E`.

```lean
theorem exists_iso_sheafParasiticColocalizationTriangle
    (K : DerivedCategory (fppfModules B S hS 𝒳))
    (P : DerivedCategory (fppfModules B S hS 𝒳)) (b : K ⟶ P)
    (c : P ⟶ (sheafParasiticFreePart B S hS 𝒳 K)⟦(1 : ℤ)⟧)
    (hT : Triangle.mk (sheafParasiticFreePartHom B S hS 𝒳 K) b c ∈
      distTriang (DerivedCategory (fppfModules B S hS 𝒳)))
    (hP : ParasiticQuotient.derivedParasitic B S hS 𝒳
      (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) P)
    {E'' P'' : DerivedCategory (fppfModules B S hS 𝒳)} (f'' : E'' ⟶ K) (g'' : K ⟶ P'')
    (h'' : P'' ⟶ E''⟦(1 : ℤ)⟧)
    (hT'' : Triangle.mk f'' g'' h'' ∈ distTriang (DerivedCategory (fppfModules B S hS 𝒳)))
    (hE'' : (ParasiticQuotient.derivedParasitic B S hS 𝒳
      (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)).leftOrthogonal E'')
    (hP'' : ParasiticQuotient.derivedParasitic B S hS 𝒳
      (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) P'') :
    ∃ e : Triangle.mk (sheafParasiticFreePartHom B S hS 𝒳 K) b c ≅ Triangle.mk f'' g'' h'',
      e.hom.hom₂ = 𝟙 K
```

**`AlgebraicGeometry.Stack.FlatFppf.derivedParasitic_obj₃_of_distTriang_sheafParasiticFreePartHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean#L235). The attribute's comment: “the cone: for E' = Lg_! g^* E and E' ⟶ E the counit of Lg_! ⊣ g^*, every distinguished triangle E' ⟶ E ⟶ P ⟶ E'[1] with E in D_LQCoh^fbc(𝒪_𝒳) has P in D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳), for the faithful class LQCoh^fbc of Stacks 0762 and the actual derived lower shriek of Stacks 07AS (4) at the standard models of the derived categories, with no hypothesis (Stacks 07B9 (2)(a), (2)(c) and 07B3 (2) are proved, not assumed)”.

> **Stacks 07BA**, the cone: for `E` in `D_{LQCoh^fbc}(𝒪_𝒳)`, every cone `P` on the canonical
> morphism `Lg_! g^* E ⟶ E` lies in `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`.

```lean
theorem derivedParasitic_obj₃_of_distTriang_sheafParasiticFreePartHom :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    letI := HasDerivedCategory.standard (flatFppfModules B S hS 𝒳)
    ∀ (K : DerivedCategory (fppfModules B S hS 𝒳)),
      DerivedCategoryB.derivedCategoryB
        (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) K →
      ∀ (P : DerivedCategory (fppfModules B S hS 𝒳)) (b : K ⟶ P)
        (c : P ⟶ (sheafParasiticFreePart B S hS 𝒳 K)⟦(1 : ℤ)⟧),
        Triangle.mk (sheafParasiticFreePartHom B S hS 𝒳 K) b c ∈
          distTriang (DerivedCategory (fppfModules B S hS 𝒳)) →
        ParasiticQuotient.derivedParasitic B S hS 𝒳
          (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) P
```

**`AlgebraicGeometry.Stack.FlatFppf.exists_sheafParasiticColocalizationTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean#L262). The attribute's comment: “the existence of the triangle: every E in D_LQCoh^fbc(𝒪_𝒳) sits in a distinguished triangle E' ⟶ E ⟶ P ⟶ E'[1] with E' = Lg_! g^* E and E' ⟶ E the counit, E' and P in D_LQCoh^fbc(𝒪_𝒳), P in D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳) and Hom(E', P') = 0 for every P' in D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳), for the faithful class LQCoh^fbc of Stacks 0762 and the actual derived lower shriek of Stacks 07AS (4) at the standard models of the derived categories, with no hypothesis”.

> **Stacks 07BA**: every `E` in `D_{LQCoh^fbc}(𝒪_𝒳)` sits in a distinguished triangle
> `E' ⟶ E ⟶ P ⟶ E'[1]` of `D_{LQCoh^fbc}(𝒪_𝒳)`, `E' ⟶ E` the canonical morphism
> `Lg_! g^* E ⟶ E`, with `P` in `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` and `E'` left orthogonal to
> `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)`.

```lean
theorem exists_sheafParasiticColocalizationTriangle :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    letI := HasDerivedCategory.standard (flatFppfModules B S hS 𝒳)
    ∀ (K : DerivedCategory (fppfModules B S hS 𝒳)),
      DerivedCategoryB.derivedCategoryB
        (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) K →
      ∃ (P : DerivedCategory (fppfModules B S hS 𝒳)) (b : K ⟶ P)
        (c : P ⟶ (sheafParasiticFreePart B S hS 𝒳 K)⟦(1 : ℤ)⟧),
        Triangle.mk (sheafParasiticFreePartHom B S hS 𝒳 K) b c ∈
            distTriang (DerivedCategory (fppfModules B S hS 𝒳)) ∧
          DerivedCategoryB.derivedCategoryB
            (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)
            (sheafParasiticFreePart B S hS 𝒳 K) ∧
          DerivedCategoryB.derivedCategoryB
            (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) P ∧
          ParasiticQuotient.derivedParasitic B S hS 𝒳
            (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳) P ∧
          (ParasiticQuotient.derivedParasitic B S hS 𝒳
            (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)).leftOrthogonal
            (sheafParasiticFreePart B S hS 𝒳 K)
```

**`AlgebraicGeometry.Stack.FlatFppf.hasColocalizations_locallyQuasicoherentSheafFlatBaseChangeFppfModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeParasiticColocalization.lean#L294). The attribute's comment: “the triangle as the colocalization of D_LQCoh^fbc(𝒪_𝒳) by D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳): every object receives Lg_! g^* E ⟶ E, a morphism with cone in D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳) out of an object left orthogonal to it, for the faithful class LQCoh^fbc and the actual Lg_! at the standard models of the derived categories, with no hypothesis”.

> **Stacks 07BA**, in the form of the colocalization hypothesis of the Verdier quotient
> `D_{LQCoh^fbc}(𝒪_𝒳) / D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` (`D_QCoh(𝒪_𝒳)` of **Stacks 07B6**).

```lean
theorem hasColocalizations_locallyQuasicoherentSheafFlatBaseChangeFppfModules :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    DerivedCategoryB.HasColocalizations
      (lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)
      (ParasiticQuotient.parasitic B S hS 𝒳 ⊓
        lqcohSheafFbcFppfModules.{u, _, u} B E h S hS 𝒳)
```

## Tag 0H11, a remark

[Tag 0H11](https://stacks.math.columbia.edu/tag/0H11) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSaturated_derivedParasiticFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentAdmissibility.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedQuasicoherentAdmissibility.lean#L343). The attribute's comment: “the last assertion for D(𝒳_fppf, 𝒪_𝒳): 𝒜, hence D_QCoh(𝒪_𝒳), read inside D(𝒳_fppf, 𝒪_𝒳) is a strictly full saturated triangulated subcategory there”.

> **Stacks 0H11**, last assertion, inside `D(𝒳_{fppf}, 𝒪_𝒳)`.  The subcategory `𝒜` read in
> `D(𝒳_{fppf}, 𝒪_𝒳)`, that is the locally quasi-coherent complexes with flat base change which are
> left orthogonal to the parasitic ones, is a strictly full, saturated ([Stacks, Tag 05RB]),
> triangulated subcategory of `D(𝒳_{fppf}, 𝒪_𝒳)`.
>
> Strict fullness and triangulatedness are those of a left orthogonal ([Stacks, Tag 0FXC] and
> [Stacks, Tag 0CQR]) intersected with `D_{LQCoh^fbc}(𝒪_𝒳)`, and saturation is stability under
> retracts of a left orthogonal, again [Stacks, Tag 0FXC], intersected with the carried stability
> under retracts of `D_{LQCoh^fbc}(𝒪_𝒳)`.

```lean
theorem isSaturated_derivedParasiticFree :
    (derivedParasiticFree B E h S hS 𝒳).IsClosedUnderIsomorphisms ∧
      (derivedParasiticFree B E h S hS 𝒳).IsSaturated ∧
      (derivedParasiticFree B E h S hS 𝒳).IsTriangulated
```

**`AlgebraicGeometry.Stack.parasiticInLQCoh_isLeftAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean#L143). The attribute's comment: “the first assertion: D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳) ⊂ D_LQCoh^fbc(𝒪_𝒳) is a left admissible subcategory”.

> **Stacks 0H11**, first assertion. The subcategory
> `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳) ⊂ D_{LQCoh^fbc}(𝒪_𝒳)` is left admissible: a strictly full
> triangulated subcategory whose inclusion has a left adjoint.

```lean
theorem parasiticInLQCoh_isLeftAdmissible :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    (ParasiticQuotient.parasiticIn B S hS 𝒳
      (𝓛 B E h S hS 𝒳)).IsLeftAdmissible
```

**`AlgebraicGeometry.Stack.parasiticFreeInLQCoh_isRightAdmissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean#L154). The attribute's comment: “the second assertion: the left orthogonal 𝒜 of D_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳) is right admissible in D_LQCoh^fbc(𝒪_𝒳)”.

> **Stacks 0H11**, second assertion. The left orthogonal `𝒜` of
> `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` in `D_{LQCoh^fbc}(𝒪_𝒳)` is right admissible: a strictly full
> triangulated subcategory whose inclusion has a right adjoint.

```lean
theorem parasiticFreeInLQCoh_isRightAdmissible :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    (ParasiticQuotient.parasiticFreeIn B S hS 𝒳
      (𝓛 B E h S hS 𝒳)).IsRightAdmissible
```

**`AlgebraicGeometry.Stack.parasiticFreeInLQCoh_ι_comp_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean#L177). The attribute's comment: “the third assertion: the composition 𝒜 ⟶ D_LQCoh^fbc(𝒪_𝒳) ⟶ D_QCoh(𝒪_𝒳) of the inclusion with the Verdier quotient functor of 07B6 is an equivalence”.

> **Stacks 0H11**, third assertion. The composition
>
> `𝒜 ⟶ D_{LQCoh^fbc}(𝒪_𝒳) ⟶ D_QCoh(𝒪_𝒳)`
>
> of the inclusion of the left orthogonal `𝒜` with the Verdier quotient functor of **Stacks 07B6**
> is an equivalence of categories.

```lean
theorem parasiticFreeInLQCoh_ι_comp_isEquivalence :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    ((ParasiticQuotient.parasiticFreeIn B S hS 𝒳
        (𝓛 B E h S hS 𝒳)).ι ⋙
      ParasiticQuotient.toQuotient B S hS 𝒳
        (𝓛 B E h S hS 𝒳)).IsEquivalence
```

**`AlgebraicGeometry.Stack.parasiticFreeInLQCoh_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean#L191). The attribute's comment: “the last assertion for D_LQCoh^fbc(𝒪_𝒳): 𝒜, hence D_QCoh(𝒪_𝒳), is a strictly full saturated triangulated subcategory of D_LQCoh^fbc(𝒪_𝒳)”.

> **Stacks 0H11**, last assertion, inside `D_{LQCoh^fbc}(𝒪_𝒳)`. The left orthogonal `𝒜`, which
> `AlgebraicGeometry.Stack.parasiticFreeInLQCoh_ι_comp_isEquivalence` identifies with
> `D_QCoh(𝒪_𝒳)`, is a strictly full, saturated ([Stacks, Tag 05RB]), triangulated subcategory of
> `D_{LQCoh^fbc}(𝒪_𝒳)`.

```lean
theorem parasiticFreeInLQCoh_isSaturated :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    (ParasiticQuotient.parasiticFreeIn B S hS 𝒳
        (𝓛 B E h S hS 𝒳)).IsClosedUnderIsomorphisms ∧
      (ParasiticQuotient.parasiticFreeIn B S hS 𝒳
        (𝓛 B E h S hS 𝒳)).IsSaturated ∧
      (ParasiticQuotient.parasiticFreeIn B S hS 𝒳
        (𝓛 B E h S hS 𝒳)).IsTriangulated
```

**`AlgebraicGeometry.Stack.parasiticFreeInDerivedFppf_isSaturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean#L211). The attribute's comment: “the last assertion for D(𝒳_fppf, 𝒪_𝒳): 𝒜, hence D_QCoh(𝒪_𝒳), read inside D(𝒳_fppf, 𝒪_𝒳) is a strictly full saturated triangulated subcategory there”.

> **Stacks 0H11**, last assertion, inside `D(𝒳_{fppf}, 𝒪_𝒳)`. The subcategory `𝒜` read in
> `D(𝒳_{fppf}, 𝒪_𝒳)` — the complexes with cohomology in `LQCoh^fbc(𝒪_𝒳)` admitting no nonzero
> morphism to `D_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` — is a strictly full, saturated, triangulated
> subcategory of `D(𝒳_{fppf}, 𝒪_𝒳)`.

```lean
theorem parasiticFreeInDerivedFppf_isSaturated [HasDerivedCategory (fppfModules B S hS 𝒳)] :
    (ParasiticQuotient.parasiticFree B S hS 𝒳
        (𝓛 B E h S hS 𝒳)).IsClosedUnderIsomorphisms ∧
      (ParasiticQuotient.parasiticFree B S hS 𝒳
        (𝓛 B E h S hS 𝒳)).IsSaturated ∧
      (ParasiticQuotient.parasiticFree B S hS 𝒳
        (𝓛 B E h S hS 𝒳)).IsTriangulated
```

**`AlgebraicGeometry.Stack.parasiticFreeToLQCoh_comp_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentSemiorthogonalDecomposition.lean#L226). The attribute's comment: “the embedding into D(𝒳_fppf, 𝒪_𝒳): the composition of the inclusion of 𝒜, presented as a subcategory of D(𝒳_fppf, 𝒪_𝒳), with the Verdier quotient functor of 07B6 is an equivalence”.

> **Stacks 0H11**, the realization of `D_QCoh(𝒪_𝒳)` inside `D(𝒳_{fppf}, 𝒪_𝒳)`: the inclusion
> of `𝒜`, presented as a subcategory of `D(𝒳_{fppf}, 𝒪_𝒳)`, followed by the Verdier quotient
> functor of **Stacks 07B6** is an equivalence.

```lean
theorem parasiticFreeToLQCoh_comp_isEquivalence :
    letI := HasDerivedCategory.standard (fppfModules B S hS 𝒳)
    (ParasiticQuotient.parasiticFreeToClass B S hS 𝒳
        (𝓛 B E h S hS 𝒳) ⋙
      ParasiticQuotient.toQuotient B S hS 𝒳
        (𝓛 B E h S hS 𝒳)).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 104.5, Tag 07B5](https://stacks.math.columbia.edu/tag/07B5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

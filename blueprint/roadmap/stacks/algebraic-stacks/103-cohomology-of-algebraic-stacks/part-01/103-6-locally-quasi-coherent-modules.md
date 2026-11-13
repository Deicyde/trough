---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isLocallyQuasicoherent_of_isSmooth_jointlySurjective, AlgebraicGeometry.Stack.isLocallyQuasicoherent_stackModuleHigherDirectImage, AlgebraicGeometry.Stack.exists_fppfCovering_isQuasicoherentOnSite_restrictModuleToSmallEtale, AlgebraicGeometry.Stack.isLocallyQuasicoherent_of_isFlat_isLfp_jointlySurjective
statement: formalized
proof: formalized
---

# 103.6 Locally quasi-coherent modules

Section 103.6 of the Stacks Project, [Tag 075X](https://stacks.math.columbia.edu/tag/075X). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 075Y, a lemma

[Tag 075Y](https://stacks.math.columbia.edu/tag/075Y) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentSmoothDescent.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentSmoothDescent.lean#L154).

> Let `f j : 𝒵 j ⟶ 𝒳` be a family of smooth 1-morphisms of algebraic stacks over `S` with
> `|𝒳| = ⋃ j, |f j|(|𝒵 j|)`, and let `F` be a sheaf of `𝒪_𝒳`-modules on `𝒳_étale`. If every inverse
> image `f j^{-1} F` is locally quasi-coherent, then so is `F`.

```lean
theorem isLocallyQuasicoherent_of_isSmooth_jointlySurjective
    {J : Type v} {𝒵 : J → AlgebraicStacks.{u, w} B S hS} {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒵 j ⟶ 𝒳)
    (hsmooth : ∀ j, AlgebraicStacks.IsSmooth B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒳)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (F : PresheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (etaleTopology B) (etaleTopology_le_topology B)).obj)
    (hF : Presheaf.IsSheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)) F.presheaf)
    (hlqc : ∀ j, IsLocallyQuasicoherent B E h S hS
      (CatFiberedInGroupoids.homFunctor (f j).hom ⋙ 𝒳.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS (f j).hom)
      ((stackModulePresheafPullback.{u, w, u} B S hS (f j)).obj F)) :
    IsLocallyQuasicoherent B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids F
```

## Tag 075Z, a lemma

[Tag 075Z](https://stacks.math.columbia.edu/tag/075Z) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_stackModuleHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentHigherDirectImage.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentHigherDirectImage.lean#L128). The attribute's comment: “the whole statement, for every degree i, with the source's hypotheses: f quasi-compact and quasi-separated, ℱ a locally quasi-coherent 𝒪\_𝒳-module on 𝒳\_étale; modules have sections in the universe of the structure sheaf, and Sch\_étale is the big étale site E on the underlying category of Sch\_fppf (E.cutoff = B.cutoff), as in the source”.

> Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and quasi-separated 1-morphism of algebraic stacks and
> `ℱ` a locally quasi-coherent `𝒪_𝒳`-module on `𝒳_étale`. Then every higher direct image `Rⁱf_*ℱ`,
> computed in the étale topology, is locally quasi-coherent on `𝒴_étale`.
>
> Modules have sections in the universe `u` of the schemes, the universe of the structure sheaf
> `𝒪_𝒳`, and `Rⁱf_*` is the right derived functor of the direct image right adjoint to the inverse
> image (`AlgebraicGeometry.Stack.stackModuleHigherDirectImage`). The small étale sites `U_étale` in
> the definition of local quasi-coherence (**Stacks 06WJ**) are those of the big étale site `E`
> whose underlying category is that of the big fppf site `B` (`E.cutoff = B.cutoff`), which is the
> convention of the source: `Sch_étale` is the big étale site on the underlying category `Sch_α`
> of `Sch_fppf`.

```lean
theorem isLocallyQuasicoherent_stackModuleHigherDirectImage
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : IsQuasiCompactMorphism B S hS f) (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (F : StackModules B S hS .etale 𝒳)
    (hF : IsLocallyQuasicoherent B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids F.val)
    (i : ℕ) :
    IsLocallyQuasicoherent B E h S hS 𝒴.val.val.p 𝒴.val.isFiberedInGroupoids
      ((stackModuleHigherDirectImage B S hS f .etale i).obj F).val
```

## Tag 07AP, a lemma

[Tag 07AP](https://stacks.math.columbia.edu/tag/07AP) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_fppfCovering_isQuasicoherentOnSite_restrictModuleToSmallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatDescent.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatDescent.lean#L156). The attribute's comment: “the fppf-local half: every object acquires a jointly surjective family of flat, locally finitely presented arrows at whose sources the small étale restriction of the module is quasi-coherent, via the fppf-local factorisation of Stacks 07AN”.

> **Stacks 07AP, its fppf-local half.** Let `f j : 𝒵 j ⟶ 𝒳` be a family of flat, locally
> finitely presented 1-morphisms of algebraic stacks over `S` with `|𝒳| = ⋃ j, |f j|(|𝒵 j|)`, let
> `F` be a sheaf of `𝒪_𝒳`-modules on `𝒳_étale` and suppose every inverse image `f j^{-1} F` is
> locally quasi-coherent. Then every object `x` of `𝒳` admits a family of arrows `φ i : y i ⟶ x`
> lying over flat, locally finitely presented and jointly surjective morphisms of schemes, at every
> member of which the restriction of `F` to the small étale site is quasi-coherent.

```lean
theorem exists_fppfCovering_isQuasicoherentOnSite_restrictModuleToSmallEtale {J : Type v}
    {𝒵 : J → AlgebraicStacks.{u, w} B S hS} {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒵 j ⟶ 𝒳)
    (hflat : ∀ j, AlgebraicStacks.IsFlat B S hS (f j))
    (hlfp : ∀ j, AlgebraicStacks.IsLocallyOfFinitePresentation B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒳)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (F : PresheafOfModules.{m} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (etaleTopology B) (etaleTopology_le_topology B)).obj)
    (hF : Presheaf.IsSheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)) F.presheaf)
    (hlqc : ∀ j, IsLocallyQuasicoherent B E h S hS
      (CatFiberedInGroupoids.homFunctor (f j).hom ⋙ 𝒳.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS (f j).hom)
      ((stackModulePresheafPullback.{u, w, m} B S hS (f j)).obj F))
    (x : 𝒳.val.val.obj) :
    ∃ (I : Type (u + 1)) (y : I → 𝒳.val.val.obj) (φ : ∀ i, y i ⟶ x),
      (∀ i, Flat (B.inclusion.map (𝒳.val.val.p.map (φ i)).left)) ∧
        (∀ i, LocallyOfFinitePresentation (B.inclusion.map (𝒳.val.val.p.map (φ i)).left)) ∧
          (∀ t : B.inclusion.obj (𝒳.val.val.p.obj x).left,
            ∃ i, t ∈ Set.range (B.inclusion.map (𝒳.val.val.p.map (φ i)).left)) ∧
            ∀ i, (⟨restrictModuleToSmallEtale B E h S hS 𝒳.val.val.p
                  𝒳.val.isFiberedInGroupoids (y i) (etaleTopology B)
                  (etaleTopology_le_topology B) F,
                restrictModuleToSmallEtale_isSheaf B E h S hS 𝒳.val.val.p
                  𝒳.val.isFiberedInGroupoids (y i) F hF⟩ :
              SheafOfModules.{m} (SmallEtale.structureSheaf E
                (𝒳.val.val.p.obj (y i)).left.1
                (contains_base B E h S hS 𝒳.val.val.p (y i)))).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_of_isFlat_isLfp_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFppfDescent.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFppfDescent.lean#L385).

> **Stacks 07AP.** Let `f j : 𝒵 j ⟶ 𝒳` be a family of flat (**Stacks 06PW**) and locally
> finitely presented (**Stacks 06Q2**) 1-morphisms of algebraic stacks over `S` with
> `|𝒳| = ⋃ j, |f j|(|𝒵 j|)` (**Stacks 04XG**), and let `F` be a sheaf of `𝒪_𝒳`-modules on
> `𝒳_fppf`. If every inverse image `f j^{-1} F` is locally quasi-coherent (**Stacks 06WJ**), then
> so is `F`.
>
> The étale sheaf condition follows from the fppf one. At an object `x` lying over `U`, the
> restriction `x^*F|_{U_étale}` is quasi-coherent because it is cartesian between affine objects
> (Descent, Proposition 03DX), which through the index functor of **Stacks 06W1** is the cartesian
> condition for `F` along arrows lying over étale morphisms of affine schemes, proved by
> `AlgebraicGeometry.Stack.isIso_restrictionBaseChange_of_isFlat_isLfp_jointlySurjective`.

```lean
theorem isLocallyQuasicoherent_of_isFlat_isLfp_jointlySurjective {J : Type v}
    {𝒵 : J → AlgebraicStacks.{u, w} B S hS} {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒵 j ⟶ 𝒳)
    (hflat : ∀ j, AlgebraicStacks.IsFlat B S hS (f j))
    (hlfp : ∀ j, AlgebraicStacks.IsLocallyOfFinitePresentation B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒳)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (F : PresheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (etaleTopology B) (etaleTopology_le_topology B)).obj)
    (hF : Presheaf.IsSheaf (associatedTopology B S hS 𝒳.val.val.p B.topology) F.presheaf)
    (hlqc : ∀ j, IsLocallyQuasicoherent B E h S hS
      (CatFiberedInGroupoids.homFunctor (f j).hom ⋙ 𝒳.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS (f j).hom)
      ((stackModulePresheafPullback.{u, w, u} B S hS (f j)).obj F)) :
    IsLocallyQuasicoherent B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.6, Tag 075X](https://stacks.math.columbia.edu/tag/075X)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

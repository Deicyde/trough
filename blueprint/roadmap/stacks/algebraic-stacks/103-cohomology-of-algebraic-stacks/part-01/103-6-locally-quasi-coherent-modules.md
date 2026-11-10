---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isLocallyQuasicoherent_of_isSmooth_jointlySurjective, AlgebraicGeometry.Stack.isLocallyQuasicoherent_moduleSheafHigherDirectImage, AlgebraicGeometry.Stack.isLocallyQuasicoherent_stackModuleHigherDirectImage, AlgebraicGeometry.Stack.exists_fppfCovering_isQuasicoherentOnSite_restrictModuleToSmallEtale, AlgebraicGeometry.Stack.isLocallyQuasicoherent_of_isFlat_isLfp_jointlySurjective
statement: formalized
proof: formalized
---

# 103.6 Locally quasi-coherent modules

Section 103.6 of the Stacks Project, [Tag 075X](https://stacks.math.columbia.edu/tag/075X). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 075Y, a lemma

[Tag 075Y](https://stacks.math.columbia.edu/tag/075Y) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentSmoothDescent.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentSmoothDescent.lean#L154).

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

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_moduleSheafHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageSmoothLocalCriterion.lean, line 537](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/HigherDirectImageSmoothLocalCriterion.lean#L537). The attribute's comment: “the whole statement, in every degree and with the source's hypotheses unweakened, granted four named hypotheses: the criterion of Stacks 076Z quantified over every rule, the weak Serre condition of Stacks 06WM parts (1)-(3), the converse half of the smooth-local criterion Stacks 075Y at section universe u+1, and the affine case (Stacks 075P and Stacks 0720). Hypothesis (2) of the criterion, Stacks 06WL, is proved rather than assumed”.

> **Stacks 075Z.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact (**Stacks 050U**) and quasi-separated
> (**Stacks 04YW**) 1-morphism of algebraic stacks over `S` and let `ℱ` be a locally quasi-coherent
> `𝒪_𝒳`-module on `𝒳_étale` (**Stacks 06WJ**). Then the higher direct image `Rⁱf_*ℱ`, computed in
> the étale topology, is locally quasi-coherent on `𝒴_étale`, in every degree `i`.
>
> The conclusion is `AlgebraicGeometry.Stack.IsLocallyQuasicoherentHigherDirectImage`, the
> library's statement of the assertion of the source, unchanged and for every degree.
>
> Three hypotheses are carried, each a clause of the criterion of **Stacks 076Z** at the rule of
> local quasi-coherence and each one a result of the source this library does not have:
>
> * `hcrit` is **Stacks 076Z**, quantified over every rule. Its proof runs the first-quadrant
>   spectral sequence of **Stacks 072G**, which is not formalized here.
> * `hserre` is hypothesis (1), the weak Serre condition, which is parts (1) to (3) of
>   **Stacks 06WM**, proved at section universe `u` in
>   `StacksFrontier.AlgebraicGeometry.Stacks.Quasicoherent.LocallyQuasicoherentClosure`; here it is
>   read at section universe `u + 1`.
> * `hconv` is the converse half of hypothesis (3), which is **Stacks 075Y**. That tag is proved, at
>   section universe `u` only, and the higher direct images produce modules with sections in
>   `u + 1`; closing this gap is a universe generalization of **Stacks 03DN**, not a new theorem of
>   the source.
> * `haffine` is hypothesis (4), the case of stacks representable by affine schemes, which the
>   source proves from **Stacks 075P** and **Stacks 0720**; the cohomological content of
>   **Stacks 075P** and all of **Stacks 0720** are absent.
>
> Hypothesis (2) is not carried: it is **Stacks 06WL** and is supplied by
> `AlgebraicGeometry.Stack.isStableUnderSmoothPullback_locallyQuasicoherentRule`, which also supplies
> the forward half of hypothesis (3).

```lean
theorem isLocallyQuasicoherent_moduleSheafHigherDirectImage
    (hcrit : SmoothLocalHigherDirectImageCriterion.{u, t, s} B S hS)
    (hserre : StackEtaleModuleRule.IsWeakSerre.{u, t} B S hS (locallyQuasicoherentRule B E h S hS))
    (hconv : StackEtaleModuleRule.IsSmoothLocalConverse.{u, t, s} B S hS
      (locallyQuasicoherentRule B E h S hS))
    (haffine : StackEtaleModuleRule.PreservesHigherDirectImagesOfAffine.{u, t} B S hS
      (locallyQuasicoherentRule B E h S hS))
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : IsQuasiCompactMorphism B S hS f)
    (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f) (i : ℕ) :
    IsLocallyQuasicoherentHigherDirectImage B E h S hS f i
```

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_stackModuleHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentHigherDirectImage.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentHigherDirectImage.lean#L124). The attribute's comment: “the whole statement, with modules and higher direct images at the module universe u of the schemes; local quasi-coherence read against an auxiliary big étale site E with E.cutoff = B.cutoff”.

> Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and quasi-separated 1-morphism of algebraic stacks and
> `ℱ` a locally quasi-coherent `𝒪_𝒳`-module on `𝒳_étale`. Then every higher direct image `Rⁱf_*ℱ`,
> computed in the étale topology, is locally quasi-coherent on `𝒴_étale`.
>
> Modules have sections in the universe `u` of the schemes, and `Rⁱf_*` is the right derived
> functor of the direct image right adjoint to the inverse image
> (`AlgebraicGeometry.Stack.stackModuleHigherDirectImage`). Local quasi-coherence is stated against
> an auxiliary big étale site `E` with the cutoff of `B`.

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

**`AlgebraicGeometry.Stack.exists_fppfCovering_isQuasicoherentOnSite_restrictModuleToSmallEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatDescent.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatDescent.lean#L156). The attribute's comment: “the fppf-local half: every object acquires a jointly surjective family of flat, locally finitely presented arrows at whose sources the small étale restriction of the module is quasi-coherent, via the fppf-local factorisation of Stacks 07AN”.

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

**`AlgebraicGeometry.Stack.isLocallyQuasicoherent_of_isFlat_isLfp_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFppfDescent.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFppfDescent.lean#L385).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

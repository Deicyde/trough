---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChange_fppfModulesPullback, AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChange_stackModulePresheafPullback, AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherentWithSheafFlatBaseChange, AlgebraicGeometry.Stack.fppfModuleOfLqcohSheafFbc, AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherentWithFlatBaseChange, AlgebraicGeometry.Stack.fppfModuleOfLocallyQuasicoherentWithFlatBaseChange, AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChangeUnivLE_moduleSheafHigherDirectImage, AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_fppfModulesHigherDirectImage
statement: formalized
proof: formalized
---

# 103.8 Locally quasi-coherent modules with the flat base change property

Section 103.8 of the Stacks Project, [Tag 0GQG](https://stacks.math.columbia.edu/tag/0GQG). 4 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0771, a proposition

[Tag 0771](https://stacks.math.columbia.edu/tag/0771) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChange_fppfModulesPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeFppfPullback.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeFppfPullback.lean#L85). The attribute's comment: “part (3): the inverse image along a 1-morphism of algebraic stacks of a module in LQCoh^fbc lies in LQCoh^fbc, with the ambient category the modules on the fppf site, which is the source's own”.

> **Stacks 0771, part (3), in the source's ambient category.**  Let `f : 𝒳 ⟶ 𝒴` be a
> 1-morphism of algebraic stacks and let `F` be a module on the fppf site of `𝒴` lying in
> `LQCoh^fbc(𝒪_𝒴)`.  Then the inverse image `f^*F` lies in `LQCoh^fbc(𝒪_𝒳)`.
>
> `AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChange_stackInverseImage` is
> this statement for the inverse image of *presheaves* of modules, stated at the structure functor
> `f ⋙ 𝒪_𝒴` of the composite presentation; the structure functor of the source is a parameter `p`
> here, together with the identification `e`, so that substituting `e` puts the goal at the
> composite presentation where that statement applies.  See the implementation notes.

```lean
theorem isLocallyQuasicoherentWithFlatBaseChange_fppfModulesPullback
    {p : 𝒳.val.val.obj ⥤ BigFppfOver B S hS}
    (e : CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p = p)
    (hp : p.IsFiberedInGroupoids) (F : fppfModules B S hS 𝒴)
    (hF : locallyQuasicoherentFlatBaseChangeFppfModules B E hE S hS 𝒴 F) :
    IsLocallyQuasicoherentWithFlatBaseChange B E hE S hS p hp
      ((modulePullback.{u, u + 1, u, u, u + 1, u} B S hS p 𝒴.val.val.p hp
        𝒴.val.isFiberedInGroupoids (CatFiberedInGroupoids.homFunctor f.hom) e
        B.topology le_rfl).obj F).val
```

**`AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChange_stackModulePresheafPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangePullback.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangePullback.lean#L100). The attribute's comment: “part (3), the local quasi-coherence half: the inverse image along a 1-morphism of algebraic stacks of a module in LQCoh^fbc lies in LQCoh^fbc, with the flat base change property of the inverse image assumed (Stacks 0764 part (1))”.

> **Stacks 0771, part (3), the local quasi-coherence half.** Let `g : 𝒵 ⟶ 𝒳` be a 1-morphism
> of algebraic stacks over `S` and let `F` lie in `LQCoh^fbc(𝒪_𝒳)`. Then the inverse image
> `g^{-1}F` lies in `LQCoh^fbc(𝒪_𝒵)`.
>
> Local quasi-coherence of `g^{-1}F` is **Stacks 06WL**, which holds for every 1-morphism of
> categories fibred in groupoids. The flat base change property of `g^{-1}F` is the hypothesis
> `hfbc`: the source deduces it from **Stacks 0764** part (1), whose module-level ingredient — the
> form of **Stacks 075D** part (4) for presheaves of modules — is not available; see the
> implementation notes of this file.

```lean
theorem isLocallyQuasicoherentWithFlatBaseChange_stackModulePresheafPullback
    {𝒵 𝒳 : AlgebraicStacks.{u, w} B S hS} (g : 𝒵 ⟶ 𝒳)
    (F : PresheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (etaleTopology B) (etaleTopology_le_topology B)).obj)
    (hF : IsLocallyQuasicoherentWithFlatBaseChange B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids F)
    (hfbc : HasFlatBaseChangeProperty B E h S hS
      (CatFiberedInGroupoids.homFunctor g.hom ⋙ 𝒳.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS g.hom) (etaleTopology B)
      (etaleTopology_le_topology B)
      ((stackModulePresheafPullback.{u, w, u} B S hS g).obj F)) :
    IsLocallyQuasicoherentWithFlatBaseChange B E h S hS
      (CatFiberedInGroupoids.homFunctor g.hom ⋙ 𝒳.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS g.hom)
      ((stackModulePresheafPullback.{u, w, u} B S hS g).obj F)
```

**`AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherentWithSheafFlatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFromSheafFlatBaseChange.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFromSheafFlatBaseChange.lean#L399). The attribute's comment: “part (1): a member of LQCoh^fbc (with the flat base change property of 0762 read on sheaves) is a sheaf for the fppf topology; for every category fibred in groupoids”.

> **Stacks 0771, part (1).** A presheaf of modules over the structure sheaf of a category
> fibred in groupoids over the big fppf site which lies in `LQCoh^fbc(𝒪_𝒳)` — locally
> quasi-coherent (**Stacks 06WJ**) with the flat base change property of **Stacks 0762** — is a
> sheaf for the fppf topology of **Stacks 06TP**.
>
> This is **Stacks 076T**,
> `AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherent_of_sheafFlatLfpBaseChange`, whose
> hypothesis (b) asks the flat base change property of fewer arrows. The module sections are in the
> universe of the schemes; the statement holds for every category fibred in groupoids, which
> generalizes the source's algebraic stack.

```lean
theorem isSheaf_fppf_of_isLocallyQuasicoherentWithSheafFlatBaseChange
    (hF : IsLocallyQuasicoherentWithSheafFlatBaseChange B E h S hS p hp F) :
    Presheaf.IsSheaf (associatedTopology B S hS p B.topology) F.presheaf
```

**`AlgebraicGeometry.Stack.fppfModuleOfLqcohSheafFbc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFromSheafFlatBaseChange.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFromSheafFlatBaseChange.lean#L410). The attribute's comment: “part (1), the clause `i.e. it is an object of Mod(𝒪_𝒳)`: the fppf module a member of LQCoh^fbc is, again in LQCoh^fbc”.

> **Stacks 0771, part (1)**, the clause "it is an object of `Mod(𝒪_𝒳)`": a member of
> `LQCoh^fbc(𝒪_𝒳) ⊆ Mod(𝒳_ét, 𝒪_𝒳)` on an algebraic stack is a module on the fppf site, with the
> same underlying presheaf of modules, and it lies in `LQCoh^fbc(𝒪_𝒳) ⊆ Mod(𝒪_𝒳)`.

```lean
noncomputable def fppfModuleOfLqcohSheafFbc (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (G : SheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (etaleTopology B) (etaleTopology_le_topology B)))
    (hG : lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒳 G) :
    (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).FullSubcategory
```

**`AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherentWithFlatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatBaseChangeSummary.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatBaseChangeSummary.lean#L164). The attribute's comment: “part (1): a member of LQCoh^fbc is a sheaf for the fppf topology of Stacks 06TP; stated for every category fibred in groupoids, which generalizes the source's algebraic stack”.

> **Stacks 0771, part (1).** A presheaf of modules over the structure sheaf of a category
> fibred in groupoids over the big fppf site which is locally quasi-coherent (**Stacks 06WJ**) and
> has the flat base change property (**Stacks 0762**) — that is, a member of `LQCoh^fbc(𝒪_𝒳)` — is
> a sheaf for the fppf topology of **Stacks 06TP**.
>
> Membership in `LQCoh^fbc` asks the comparison map `c_φ` of **Stacks 06WC** to be an isomorphism
> along every arrow lying over a flat morphism of schemes, which is more than the hypothesis of
> **Stacks 076T**, where only the arrows lying over a flat morphism locally of finite presentation
> are looked at. So part (1) is **Stacks 076T** after
> `AlgebraicGeometry.Stack.hasFlatLfpBaseChangeProperty_of_hasFlatBaseChangeProperty`.

```lean
theorem isSheaf_fppf_of_isLocallyQuasicoherentWithFlatBaseChange
    (F : PresheafOfModules.{u} (ringStructureSheafCore B S hS p hp (etaleTopology B)
      (etaleTopology_le_topology B)).obj)
    (hF : IsLocallyQuasicoherentWithFlatBaseChange B E h S hS p hp F) :
    Presheaf.IsSheaf (associatedTopology B S hS p B.topology) F.presheaf
```

**`AlgebraicGeometry.Stack.fppfModuleOfLocallyQuasicoherentWithFlatBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatBaseChangeSummary.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatBaseChangeSummary.lean#L190). The attribute's comment: “part (1), the clause `hence lies in Mod(𝒪_𝒳)`: the module on the fppf site of an algebraic stack that a member of LQCoh^fbc is”.

> **Stacks 0771, part (1)**, the object of `Mod(𝒪_𝒳)` the source's clause ends with: a member
> of `LQCoh^fbc(𝒪_𝒳)`, being a sheaf for the fppf topology by
> `AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherentWithFlatBaseChange`, is a module
> on the fppf site of the algebraic stack.
>
> No transport is involved. The presheaf of rings underlying the structure sheaf of **Stacks 06TV**
> is `p.op ⋙ (BigFppfOver.structureSheaf B S hS).obj` whichever of the five topologies of
> **Stacks 06TP** it is read at, so the presheaf of modules is already a presheaf of modules over
> the fppf structure sheaf, and only its sheaf condition has to be improved.

```lean
def fppfModuleOfLocallyQuasicoherentWithFlatBaseChange
    (F : PresheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (etaleTopology B) (etaleTopology_le_topology B)).obj)
    (hF : IsLocallyQuasicoherentWithFlatBaseChange B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids F) :
    fppfModules B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChangeUnivLE_moduleSheafHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatBaseChangeSummary.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LocallyQuasicoherentFlatBaseChangeSummary.lean#L259). The attribute's comment: “part (4)(b), in every degree, over the six hypotheses Stacks 0765 carries (Stacks 076Z; Stacks 06WM (1)-(3) with 0764 (2); 0764 (1) and (3); 075Y at u+1; 075P and 073K). THIS IS THE ETALE READING AND NOT THE TAG'S DEFAULT FPPF ONE: part (4)(a), the agreement of the two, is not asserted here”.

> **Stacks 0771, part (4)(b).** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact (**Stacks 050U**) and
> quasi-separated (**Stacks 04YW**) 1-morphism of algebraic stacks over `S` and let `ℱ` be a sheaf
> of `𝒪_𝒳`-modules on `𝒳_étale` which is locally quasi-coherent (**Stacks 06WJ**) and has the flat
> base change property (**Stacks 0762**). Then the higher direct image `Rⁱf_*ℱ` of **Stacks 06WE**,
> computed in the étale topology, is again locally quasi-coherent *and* has the flat base change
> property, in every degree `i`: that is, `Rⁱf_*` carries `LQCoh^fbc(𝒪_𝒳)` into
> `LQCoh^fbc(𝒪_𝒴)`.
>
> The flat base change property is read at section universe `u + 1`, where the higher direct images
> of module sheaves live, by `AlgebraicGeometry.Stack.HasFlatBaseChangePropertyUnivLE`.
>
> This is the conclusion of the criterion of **Stacks 076Z** at the rule `LQCoh^fbc`, so it is
> obtained from exactly the six hypotheses
> `AlgebraicGeometry.Stack.hasFlatBaseChangePropertyUnivLE_moduleSheafHigherDirectImage`
> (**Stacks 0765**) carries, each a result of the source this library does not have: `hcrit` is
> **Stacks 076Z** quantified over every rule, `hserre` is parts (1) to (3) of **Stacks 06WM** with
> part (2) of **Stacks 0764**, `hfbcPull` is part (1) of **Stacks 0764**, `hconvLqc` and `hconvFbc`
> are **Stacks 075Y** at section universe `u + 1` and part (3) of **Stacks 0764**, and `haffine` is
> the affine case, from **Stacks 075P** and **Stacks 073K**. **Stacks 0765** is the same criterion
> with only the flat base change conjunct of its conclusion kept, and **Stacks 075Z** is the
> criterion at the rule of local quasi-coherence alone; neither of them states the conjunction, and
> the conjunction is what part (4)(b) asserts.
>
> Hypothesis (2) of the criterion for local quasi-coherence is **Stacks 06WL** and is not carried:
> it is supplied by
> `AlgebraicGeometry.Stack.isStableUnderSmoothPullback_locallyQuasicoherentRule`, which also
> supplies the forward half of hypothesis (3).

```lean
theorem isLocallyQuasicoherentWithFlatBaseChangeUnivLE_moduleSheafHigherDirectImage
    (hcrit : SmoothLocalHigherDirectImageCriterion.{u, t, s} B S hS)
    (hserre : StackEtaleModuleRule.IsWeakSerre.{u, t} B S hS
      (locallyQuasicoherentFlatBaseChangeRule B E h S hS))
    (hfbcPull : StackEtaleModuleRule.IsStableUnderSmoothPullback.{u, t} B S hS
      (flatBaseChangePropertyRule B E h S hS))
    (hconvLqc : StackEtaleModuleRule.IsSmoothLocalConverse.{u, t, s} B S hS
      (locallyQuasicoherentRule B E h S hS))
    (hconvFbc : StackEtaleModuleRule.IsSmoothLocalConverse.{u, t, s} B S hS
      (flatBaseChangePropertyRule B E h S hS))
    (haffine : StackEtaleModuleRule.PreservesHigherDirectImagesOfAffine.{u, t} B S hS
      (locallyQuasicoherentFlatBaseChangeRule B E h S hS))
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : IsQuasiCompactMorphism B S hS f)
    (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f) (i : ℕ) :
    letI := hasSheafify_associatedTopology_of_category_succ B S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
    letI := wEqualsLocallyBijective_associatedTopology_of_category_succ B S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
    letI := hasSheafify_associatedTopology_of_category_succ B S hS 𝒴.val.val.p
    letI := wEqualsLocallyBijective_associatedTopology_of_category_succ B S hS 𝒴.val.val.p
    ∀ ℱ : SheafOfModules.{u + 1} (ringStructureSheafCore B S hS
        (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
        (isFiberedInGroupoids_homFunctor_comp B S hS f.hom)
        (etaleTopology B) (etaleTopology_le_topology B)),
      IsLocallyQuasicoherent B E h S hS
          (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
          (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) ℱ.val →
        HasFlatBaseChangePropertyUnivLE B E h S hS
            (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
            (isFiberedInGroupoids_homFunctor_comp B S hS f.hom)
            (etaleTopology B) (etaleTopology_le_topology B) ℱ.val →
          IsLocallyQuasicoherent B E h S hS 𝒴.val.val.p 𝒴.val.isFiberedInGroupoids
              ((moduleSheafHigherDirectImage.{u, u + 1, u, u + 1, u} B S hS
                (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p) 𝒴.val.val.p
                (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) 𝒴.val.isFiberedInGroupoids
                (CatFiberedInGroupoids.homFunctor f.hom) rfl (etaleTopology B)
                (etaleTopology_le_topology B) i).obj ℱ).val ∧
            HasFlatBaseChangePropertyUnivLE B E h S hS 𝒴.val.val.p
              𝒴.val.isFiberedInGroupoids (etaleTopology B) (etaleTopology_le_topology B)
              ((moduleSheafHigherDirectImage.{u, u + 1, u, u + 1, u} B S hS
                (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p) 𝒴.val.val.p
                (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) 𝒴.val.isFiberedInGroupoids
                (CatFiberedInGroupoids.homFunctor f.hom) rfl (etaleTopology B)
                (etaleTopology_le_topology B) i).obj ℱ).val
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_fppfModulesHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFppfHigherDirectImage.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFppfHigherDirectImage.lean#L101). The attribute's comment: “part (4)(b), in Mod(O_Y): the higher direct images computed in the fppf topology, modules at the module universe u of the schemes”.

> **Stacks 0771, part (4)(b)**, in `Mod(𝒪_𝒴)`. Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and
> quasi-separated 1-morphism of algebraic stacks and `F` an object of `LQCoh^fbc(𝒪_𝒳)`. Then each
> higher direct image `Rⁱf_*F`, computed in the fppf topology, is an object of `LQCoh^fbc(𝒪_𝒴)`.
>
> Modules have sections in the universe `u` of the schemes; local quasi-coherence is read against
> an auxiliary big étale site `E` with `E.cutoff = B.cutoff`, and the flat base change property is
> the sheaf-level one of **Stacks 0762**.

```lean
theorem lqcohSheafFbcFppfModules_fppfModulesHigherDirectImage
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : IsQuasiCompactMorphism B S hS f) (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (F : StackModules B S hS .fppf 𝒳) (hF : lqcohSheafFbcFppfModules.{u, t, u} B E h S hS 𝒳 F)
    (i : ℕ) :
    lqcohSheafFbcFppfModules.{u, t, u} B E h S hS 𝒴
      ((fppfModulesHigherDirectImage B S hS f i).obj F)
```

**`AlgebraicGeometry.Stack.nonempty_etaleComparison_fppfModulesHigherDirectImage_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFppfHigherDirectImage.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFppfHigherDirectImage.lean#L125). The attribute's comment: “part (4)(a), for the higher direct images R^i f_* (not the total direct image Rf_*), modules at the module universe u of the schemes”.

> **Stacks 0771, part (4)(a)**, for the higher direct images. Let `f : 𝒳 ⟶ 𝒴` be a
> quasi-compact and quasi-separated 1-morphism of algebraic stacks and `F` an object of
> `LQCoh^fbc(𝒪_𝒳)`. Then `Rⁱf_*F` is the same whether computed in the étale or in the fppf
> topology: `ε_*(Rⁱf_{fppf,*}F) ≅ Rⁱf_{ét,*}(ε_*F)`, where `ε_*` reads an fppf module on the étale
> site.
>
> Modules have sections in the universe `u` of the schemes. The assertion of the source about the
> total direct image `Rf_*` is not included: there is no derived direct image at that universe on
> the sites of algebraic stacks in the library.

```lean
theorem nonempty_etaleComparison_fppfModulesHigherDirectImage_iso
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : IsQuasiCompactMorphism B S hS f) (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (F : StackModules B S hS .fppf 𝒳) (hF : lqcohSheafFbcFppfModules.{u, t, u} B E h S hS 𝒳 F)
    (i : ℕ) :
    Nonempty ((stackModulesEtaleComparison B S hS 𝒴).obj
        ((fppfModulesHigherDirectImage B S hS f i).obj F) ≅
      (stackModuleHigherDirectImage B S hS f .etale i).obj
        ((stackModulesEtaleComparison B S hS 𝒳).obj F))
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcModuleRule_stackModuleHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcHigherDirectImage.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcHigherDirectImage.lean#L59). The attribute's comment: “part (4)(b), with the higher direct images computed in the étale topology, modules at the module universe u of the schemes”.

> **Stacks 0771, part (4)(b), in the étale topology.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact and
> quasi-separated 1-morphism of algebraic stacks and `F` an object of `LQCoh^fbc(𝒪_𝒳)`, a module on
> `𝒳_étale` which is locally quasi-coherent with the flat base change property. Then each higher
> direct image `Rⁱf_*F`, computed in the étale topology, is an object of `LQCoh^fbc(𝒪_𝒴)`.
>
> Modules have sections in the universe `u` of the schemes, local quasi-coherence is read against an
> auxiliary big étale site `E` with `E.cutoff = B.cutoff`, and the flat base change property is the
> sheaf-level one of **Stacks 0762** (`AlgebraicGeometry.Stack.HasSheafFlatBaseChangeProperty`).

```lean
theorem lqcohSheafFbcModuleRule_stackModuleHigherDirectImage
    {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hqc : IsQuasiCompactMorphism B S hS f) (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (F : StackModules B S hS .etale 𝒳)
    (hF : IsLocallyQuasicoherentWithSheafFlatBaseChange B E h S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids F.val) (i : ℕ) :
    IsLocallyQuasicoherentWithSheafFlatBaseChange B E h S hS 𝒴.val.val.p
      𝒴.val.isFiberedInGroupoids ((stackModuleHigherDirectImage B S hS f .etale i).obj F).val
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcEtaleModules_stackModuleInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcPullback.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcPullback.lean#L374). The attribute's comment: “part (3), on Mod(𝒳_ét, 𝒪_𝒳), with the flat base change property of 0762 read on sheaves; the module sections in the universe of the schemes”.

> **Stacks 0771, part (3)**, on `Mod(𝒳_ét, 𝒪_𝒳)`: the inverse image along a 1-morphism of
> algebraic stacks of the étale sites carries `LQCoh^fbc(𝒪_𝒴)` into `LQCoh^fbc(𝒪_𝒳)`.

```lean
theorem lqcohSheafFbcEtaleModules_stackModuleInverseImage (F : StackModules B S hS .etale 𝒴)
    (hF : lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒴 F) :
    lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒳
      ((stackModuleInverseImage B S hS .etale f).obj F)
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_fppfModulesPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcPullback.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcPullback.lean#L387). The attribute's comment: “part (3), on Mod(𝒪_𝒳), with the flat base change property of 0762 read on sheaves; the module sections in the universe of the schemes”.

> **Stacks 0771, part (3)**, on `Mod(𝒪_𝒳)`: the inverse image along a 1-morphism of algebraic
> stacks of the fppf sites carries `LQCoh^fbc(𝒪_𝒴)` into `LQCoh^fbc(𝒪_𝒳)`.

```lean
theorem lqcohSheafFbcFppfModules_fppfModulesPullback (F : fppfModules B S hS 𝒴)
    (hF : lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒴 F) :
    lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 ((fppfModulesPullback B S hS f).obj F)
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcTotalDirectImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcTotalDirectImage.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcTotalDirectImage.lean#L115). The attribute's comment: “part (4)(a), total direct image Rf_*: Rf_{ét,*}(ε_*F) ≅ Rε_*(Rf_{fppf,*}F) in D⁺(𝒴_ét), for F in LQCoh^fbc and every 1-morphism f, modules at the module universe u of the schemes”.

> **Stacks 0771, part (4)(a), for the total direct image.** Let `f : 𝒳 ⟶ 𝒴` be a 1-morphism of
> algebraic stacks and `F` an object of `LQCoh^fbc(𝒪_𝒳) ⊆ Mod(𝒪_𝒳)`. The total direct image of `F`
> computed in the étale topology is the one computed in the fppf topology, read on the étale site:
> `Rf_{ét,*}(ε_*F) ≅ Rε_*(Rf_{fppf,*}F)` in `D⁺(Mod(𝒴_ét, 𝒪_𝒴))`.
>
> Here `ε_* : Mod(𝒪_𝒴) ⥤ Mod(𝒴_ét, 𝒪_𝒴)` is only left exact, so the fppf result is compared through
> its right derived functor `Rε_*`. The isomorphism is
> `AlgebraicGeometry.Stack.totalDirectImageEtaleComparisonIso` together with `Rε_*F ≅ ε_*F`, which
> is **Stacks 075R** (1),
> `AlgebraicGeometry.Stack.isZero_rightDerived_etaleComparisonPushforward_of_lqcohSheafFbc`.
> No quasi-compactness or quasi-separatedness of `f` is needed for this form. When `f` is
> quasi-compact and quasi-separated, part (4)(b) and **Stacks 075R** (1) make the cohomology
> sheaves `Rⁱf_{fppf,*}F` of `Rf_{fppf,*}F` themselves `ε_*`-acyclic, so that `Rε_*` there is
> `ε_*` applied to the cohomology sheaves: that is the form of part (4)(a) for the higher direct
> images, `AlgebraicGeometry.Stack.nonempty_etaleComparison_fppfModulesHigherDirectImage_iso`, and
> `AlgebraicGeometry.Stack.nonempty_homology_etaleComparison_totalDirectImage_iso` below.

```lean
noncomputable def lqcohSheafFbcTotalDirectImageIso (f : 𝒳 ⟶ 𝒴) (F : StackModules B S hS .fppf 𝒳)
    (hF : lqcohSheafFbcFppfModules.{u, t, u} B E h S hS 𝒳 F) :
    (stackModuleDirectImage B S hS f .etale).rightDerivedFunctorPlus.obj
        ((DerivedCategory.Plus.singleFunctor _ 0).obj
          ((stackModulesEtaleComparison B S hS 𝒳).obj F)) ≅
      (stackModulesEtaleComparison B S hS 𝒴).rightDerivedFunctorPlus.obj
        ((stackModuleDirectImage B S hS f .fppf).rightDerivedFunctorPlus.obj
          ((DerivedCategory.Plus.singleFunctor _ 0).obj F))
```

**`AlgebraicGeometry.Stack.lqcohSheafFbc_hasColimits_and_agree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeColimits.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeColimits.lean#L261). The attribute's comment: “part (5): LQCoh^fbc(𝒪_𝒳) has small colimits, agreeing with those of Mod(𝒪_𝒳) and of Mod(𝒳_étale, 𝒪_𝒳)”.

> **Stacks 0771, part (5).**  The category `LQCoh^fbc(𝒪_𝒳)` has colimits, and they agree with
> colimits in `Mod(𝒳_étale, 𝒪_𝒳)` as well as in `Mod(𝒪_𝒳)`.
>
> In order: `LQCoh^fbc(𝒪_𝒳)`, read inside `Mod(𝒪_𝒳)`, has small colimits and its inclusion
> preserves them; read inside `Mod(𝒳_étale, 𝒪_𝒳)` the same holds; and restricting a colimit
> cocone in `Mod(𝒪_𝒳)` of objects of `LQCoh^fbc(𝒪_𝒳)` to the étale site gives a colimit cocone in
> `Mod(𝒳_étale, 𝒪_𝒳)`, so the two readings compute the same colimits.

```lean
theorem lqcohSheafFbc_hasColimits_and_agree :
    HasColimitsOfSize.{u, u} (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).FullSubcategory ∧
      PreservesColimitsOfSize.{u, u} (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι ∧
      (HasColimitsOfSize.{u, u}
          (lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒳).FullSubcategory ∧
        PreservesColimitsOfSize.{u, u} (lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒳).ι) ∧
      ∀ {K : Type u} [Category.{u} K] {D : K ⥤ fppfModules B S hS 𝒳},
        (∀ k, lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 (D.obj k)) →
          ∀ {c : Cocone D}, IsColimit c →
            Nonempty (IsColimit ((fppfToEtaleModules B S hS 𝒳).mapCocone c))
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_fppfInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeInternalHom.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeInternalHom.lean#L66). The attribute's comment: “part (7): LQCoh^fbc is closed under SheafHom(F, -) of Mod(𝒪_𝒳) for F of finite presentation in Mod(𝒪_𝒳)”.

> **Stacks 0771, part (7).** For `F` an `𝒪_𝒳`-module of finite presentation and `G` in
> `LQCoh^fbc(𝒪_𝒳)` on an algebraic stack, the internal Hom `SheafHom_{𝒪_𝒳}(F, G)` of `Mod(𝒪_𝒳)`
> is in `LQCoh^fbc(𝒪_𝒳)`.
>
> `G` is cartesian along the flat arrows between objects over affine schemes (step R2 of
> Stacks 0779), hence so is `SheafHom_{𝒪_𝒳}(F, G)`, `F` being of finite presentation; a module
> cartesian along those arrows is locally quasi-coherent and has the flat base change property.

```lean
theorem lqcohSheafFbcFppfModules_fppfInternalHom (F G : fppfModules B S hS 𝒳)
    [F.IsFinitePresentationOnSite]
    (hG : lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 G) :
    lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳
      (AlgebraicStacks.fppfInternalHom B S hS 𝒳 F G)
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_sheafTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeTensor.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeTensor.lean#L67). The attribute's comment: “part (6): LQCoh^fbc is closed under the tensor product of Mod(𝒪_𝒳)”.

> **Stacks 0771, part (6).** For `F` and `G` in `LQCoh^fbc(𝒪_𝒳)` on an algebraic stack, the
> tensor product `F ⊗_{𝒪_𝒳} G` computed in `Mod(𝒪_𝒳)` is again in `LQCoh^fbc(𝒪_𝒳)`.
>
> Both factors are cartesian along the flat arrows between objects over affine schemes (step R2 of
> Stacks 0779), hence so is their tensor product, whose sections over an affine object are the tensor
> product of the sections; a module cartesian along those arrows is locally quasi-coherent and has
> the flat base change property.

```lean
theorem lqcohSheafFbcFppfModules_sheafTensor (F G : fppfModules B S hS 𝒳)
    (hF : lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 F)
    (hG : lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 G) :
    lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳
      (((Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
        (FlatFppf.fppfRingedTopos B S hS 𝒳).O).obj
        F).obj G)
```

**`AlgebraicGeometry.Stack.isWeakSerreClass_lqcohSheafFbcEtaleModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeWeakSerre.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeWeakSerre.lean#L500). The attribute's comment: “part (2), the étale half: LQCoh^fbc is a weak Serre subcategory of Mod(𝒳_ét, 𝒪_𝒳), with the flat base change property of 0762 read on sheaves”.

> **Stacks 0771, part (2), the étale half: `LQCoh^fbc(𝒪_𝒳)` is a weak Serre subcategory of
> `Mod(𝒳_ét, 𝒪_𝒳)`**, for an algebraic stack `𝒳`, at module universe `u`, with the abelian
> structure coming from the sheafification of abelian presheaves on the associated étale site
> (`AlgebraicGeometry.Stack.hasSheafify_etaleAssociatedTopology`).

```lean
theorem isWeakSerreClass_lqcohSheafFbcEtaleModules (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    letI := hasSheafify_etaleAssociatedTopology B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
    letI := wEqualsLocallyBijective_etaleAssociatedTopology B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids
    (lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒳).IsWeakSerreClass
```

**`AlgebraicGeometry.Stack.isWeakSerreClass_lqcohSheafFbcFppfModules`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeWeakSerreFppf.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeWeakSerreFppf.lean#L291). The attribute's comment: “part (2), fppf half: LQCoh^fbc is a weak Serre subcategory of Mod(𝒪_𝒳)”.

> **Stacks 0771, part (2), the fppf half: `LQCoh^fbc(𝒪_𝒳)` is a weak Serre subcategory of
> `Mod(𝒪_𝒳)`**, for an algebraic stack `𝒳`, at module universe `u`, with the abelian structure
> coming from the sheafification of abelian presheaves on the fppf site
> (`AlgebraicGeometry.Stack.FlatFppf.hasSheafify_fppf_addCommGrpCat`): it contains `0` and is
> closed under isomorphisms, kernels, cokernels and extensions (**Stacks 0754**).

```lean
instance isWeakSerreClass_lqcohSheafFbcFppfModules :
    (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).IsWeakSerreClass
```

## Tag 07AQ, a lemma

[Tag 07AQ](https://stacks.math.columbia.edu/tag/07AQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChange_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSmoothLocal.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSmoothLocal.lean#L154). The attribute's comment: “part (1), the local quasi-coherence half: the criterion along a jointly surjective family of smooth morphisms, with the flat base change property of the source assumed (Stacks 0764 part (3))”.

> **Stacks 07AQ, part (1), the local quasi-coherence half.** Let `f j : 𝒵 j ⟶ 𝒳` be a family
> of smooth 1-morphisms of algebraic stacks over `S` with `|𝒳| = ⋃ j, |f j|(|𝒵 j|)`, and let `F`
> be a sheaf of `𝒪_𝒳`-modules on `𝒳_étale`. If every inverse image `f j^{-1} F` lies in
> `LQCoh^fbc(𝒪_{𝒵 j})` and `F` has the flat base change property, then `F` lies in
> `LQCoh^fbc(𝒪_𝒳)`.
>
> Local quasi-coherence of `F` is **Stacks 075Y**, applied to the local quasi-coherence of the
> inverse images. The flat base change property of `F` is the hypothesis `hfbc`: the source deduces
> it from **Stacks 0764** part (3), whose argument is not available for the presheaf-level inverse
> image that the flat base change property is formulated with here; see the implementation notes of
> this file.

```lean
theorem isLocallyQuasicoherentWithFlatBaseChange_of_isSmooth_jointlySurjective
    {J : Type v} {𝒵 : J → AlgebraicStacks.{u, w} B S hS} {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒵 j ⟶ 𝒳)
    (hsmooth : ∀ j, AlgebraicStacks.IsSmooth B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒳)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (F : PresheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (etaleTopology B) (etaleTopology_le_topology B)).obj)
    (hF : Presheaf.IsSheaf (associatedTopology B S hS 𝒳.val.val.p (etaleTopology B)) F.presheaf)
    (hfbc : HasFlatBaseChangeProperty B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
      (etaleTopology B) (etaleTopology_le_topology B) F)
    (hlqc : ∀ j, IsLocallyQuasicoherentWithFlatBaseChange B E h S hS
      (CatFiberedInGroupoids.homFunctor (f j).hom ⋙ 𝒳.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS (f j).hom)
      ((stackModulePresheafPullback.{u, w, u} B S hS (f j)).obj F)) :
    IsLocallyQuasicoherentWithFlatBaseChange B E h S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
      F
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcEtaleModules_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFlatDescent.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFlatDescent.lean#L98). The attribute's comment: “part (1), on Mod(𝒳_ét, 𝒪_𝒳), with the flat base change property of 0762 read on sheaves; the module sections in the universe of the schemes”.

> **Stacks 07AQ**, part (1). Let `f j : 𝒵 j ⟶ 𝒳` be a family of smooth 1-morphisms of
> algebraic stacks with `|𝒳| = ⋃ |f j|(|𝒵 j|)`, and `F` a sheaf of `𝒪_𝒳`-modules on `𝒳_ét`. If
> every `f j^{-1} F` is in `LQCoh^fbc(𝒪_{𝒵 j})`, then `F` is in `LQCoh^fbc(𝒪_𝒳)`.
>
> The source's hypothesis reads `LQCoh^{fpc}`, a misprint for `LQCoh^{fbc}`. `LQCoh^fbc` is the
> sheaf-level one (`AlgebraicGeometry.Stack.lqcohSheafFbcEtaleModules`), with the flat base change
> property of **Stacks 0762**; the module sections are in the universe of the schemes.

```lean
theorem lqcohSheafFbcEtaleModules_of_isSmooth_jointlySurjective
    {J : Type v} {𝒵 : J → AlgebraicStacks.{u, w} B S hS} {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒵 j ⟶ 𝒳) (hsmooth : ∀ j, AlgebraicStacks.IsSmooth B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒳)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (F : StackModules B S hS .etale 𝒳)
    (hF : ∀ j, lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS (𝒵 j)
      ((stackModuleInverseImage B S hS .etale (f j)).obj F)) :
    lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒳 F
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_of_isFlat_isLocallyOfFinitePresentation_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFlatDescent.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFlatDescent.lean#L203). The attribute's comment: “part (2), on Mod(𝒪_𝒳) (fppf), with the flat base change property of 0762 read on sheaves; the module sections in the universe of the schemes”.

> **Stacks 07AQ**, part (2). Let `f j : 𝒵 j ⟶ 𝒳` be a family of flat and locally finitely
> presented 1-morphisms of algebraic stacks with `|𝒳| = ⋃ |f j|(|𝒵 j|)`, and `F` a sheaf of
> `𝒪_𝒳`-modules on `𝒳_fppf`. If every `f j^{-1} F` is in `LQCoh^fbc(𝒪_{𝒵 j})`, then `F` is in
> `LQCoh^fbc(𝒪_𝒳)`.
>
> `LQCoh^fbc` is the sheaf-level one (`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules`), with the
> flat base change property of **Stacks 0762**; the module sections are in the universe of the
> schemes. The proof is the source's ("analogous to the proof of 07AP"), carried out for a general
> module rule in
> `AlgebraicGeometry.Stack.mem_of_isFlat_isLocallyOfFinitePresentation_jointlySurjective`.

```lean
theorem lqcohSheafFbcFppfModules_of_isFlat_isLocallyOfFinitePresentation_jointlySurjective
    {J : Type v} {𝒵 : J → AlgebraicStacks.{u, w} B S hS} {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : ∀ j, 𝒵 j ⟶ 𝒳) (hflat : ∀ j, AlgebraicStacks.IsFlat B S hS (f j))
    (hlfp : ∀ j, AlgebraicStacks.IsLocallyOfFinitePresentation B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒳)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (F : fppfModules B S hS 𝒳)
    (hF : ∀ j, lqcohSheafFbcFppfModules.{u, w, u} B E h S hS (𝒵 j)
      ((fppfModulesPullback B S hS (f j)).obj F)) :
    lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 F
```

## Tag 0GQH, a lemma

[Tag 0GQH](https://stacks.math.columbia.edu/tag/0GQH) in the Stacks Project.

**`AlgebraicGeometry.Stack.restrictedFppfModulesHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/RestrictedFppfHigherDirectImage.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/RestrictedFppfHigherDirectImage.lean#L69). The attribute's comment: “the whole lemma, at the module universe u of the schemes: for f : X -> Y quasi-compact, quasi-separated and representable by algebraic spaces, F in LQCoh^fbc(O_X) (the flat base change property read on sheaves, Stacks 0762) and an object y : V -> Y over a scheme V, the 2-fibre product U = V x_Y X is an algebraic space, and for every presentation of it and every i, (R^i f_* F)|_{V_etale} = R^i f'_{small,*}(F|_{U_etale}), with R^i f_* the fppf higher direct image of Mod(O_X)”.

> **Stacks 0GQH.** Let `f : 𝒳 ⟶ 𝒴` be a quasi-compact (`hqc`), quasi-separated (`hqs`)
> 1-morphism of algebraic stacks which is representable by algebraic spaces (`hrep`). Let `ℱ` be in
> `LQCoh^{fbc}(𝒪_𝒳)` (`hF`), and let `y : V ⟶ 𝒴` be an object of `𝒴` over a scheme `V`. Then:
>
> * the 2-fibre product `U = V ×_𝒴 𝒳` is represented by an algebraic space;
> * for every such presentation `eU` of `U` by an algebraic space, with `f' : U ⟶ V` the base
>   change of `f` (`AlgebraicGeometry.Stack.baseChangeSpacesHom`), and for every `i`,
>   `(Rⁱf_*ℱ)|_{V_étale} ≅ Rⁱf'_{small,*}(ℱ|_{U_étale})`.
>
> Here `Rⁱf_*` is the higher direct image of `Mod(𝒪_𝒳)`, in the fppf topology. `(-)|_{V_étale}` reads
> an fppf module on the étale site (`stackModulesEtaleComparison`), pulls it back along `y` and
> restricts it to the small étale site of `V` (`π_{V,*}`, Stacks 073M). `(-)|_{U_étale}` does the
> same along the projection `U ⟶ 𝒳`. `f'_{small,*}` is the direct image of the small étale sites
> of the algebraic spaces `U` and `V`.

```lean
theorem restrictedFppfModulesHigherDirectImage {𝒳 𝒴 : AlgebraicStacks.{u, t} B S hS}
    (f : 𝒳 ⟶ 𝒴) (hqc : IsQuasiCompactMorphism B S hS f)
    (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (hrep : IsRepresentableByAlgebraicSpaces B S hS f.hom.hom)
    (F : StackModules B S hS .fppf 𝒳) (hF : lqcohSheafFbcFppfModules.{u, t, u} B E h S hS 𝒳 F)
    {V : BigFppfOver B S hS} (y : schemeStack.{u, t} B S hS V ⟶ 𝒴) :
    (∃ U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u, IsAlgebraicSpace B S hS U ∧
      Nonempty (StacksRepresentableCFG.EquivalenceOver
        (twoFibreProductSquareAlgebraicStacks B S hS f y).pt.val.val.p
        (presheafOfCategories (U ⋙ typeToCat)).p)) ∧
    ∀ (U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hU : IsAlgebraicSpace B S hS U)
      (eU : StacksRepresentableCFG.EquivalenceOver
        (twoFibreProductSquareAlgebraicStacks B S hS f y).pt.val.val.p
        (presheafOfCategories (U ⋙ typeToCat)).p) (i : ℕ),
      Nonempty ((AlgebraicGeometry.RingedToposHom.pushforwardModules
          (Space.projectionRingedToposHom B S hS (yoneda.obj V)
            (schemeStack.{u, t} B S hS V).val.val.p
            (schemeStack.{u, t} B S hS V).val.isFiberedInGroupoids
            (isAlgebraicSpace_yoneda B S hS V) (schemeStackEquivalenceOver B S hS))).obj
          ((stackModuleInverseImage B S hS .etale y).obj
            ((stackModulesEtaleComparison B S hS 𝒴).obj
              ((fppfModulesHigherDirectImage B S hS f i).obj F))) ≅
        (Space.smallEtaleHigherDirectImage
            (baseChangeSpacesHom B S hS f y (yoneda.obj V) (isAlgebraicSpace_yoneda B S hS V)
              (schemeStackEquivalenceOver B S hS) U hU eU) i).obj
          ((AlgebraicGeometry.RingedToposHom.pushforwardModules
            (Space.projectionRingedToposHom B S hS U
              (twoFibreProductSquareAlgebraicStacks B S hS f y).pt.val.val.p
              (twoFibreProductSquareAlgebraicStacks B S hS f y).pt.val.isFiberedInGroupoids
              hU eU)).obj
            ((stackModuleInverseImage B S hS .etale
              (twoFibreProductSquareAlgebraicStacks B S hS f y).fst).obj
              ((stackModulesEtaleComparison B S hS 𝒳).obj F))))
```

**`AlgebraicGeometry.Space.restrictedHigherDirectImageChartIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RestrictedHigherDirectImage.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/RestrictedHigherDirectImage.lean#L331). The attribute's comment: “(R^i f_*F)|_{V_etale} = R^i f'_{small,*}(F|_{U_etale}) for the base change f' of f along an object y : V -> Y of Y, with U = V x_Y X an ALGEBRAIC SPACE (f is representable by algebraic spaces, so U need not be a scheme) and f'_{small,*} the direct image of the small etale sites of algebraic spaces; stated for every i and naturally in the complex of O_X-modules, with R^i the i-th cohomology of the total right derived direct image, which is what composes with Tag 075N. PROVED here from four inputs, two of which are themselves assumed, and all named: (1) `bc`, the BASE CHANGE isomorphism of the 2-cartesian square in derived form, which is Tag 075H -- carried in this library only for ABELIAN sheaves (`abelianHigherDirectImageBaseChangeIso`), the module-coefficient statement `nonempty_moduleHigherDirectImageBaseChangeIso` being itself conditional on a linearity hypothesis that is 075H's own module-coefficient assertion, so the module case is ASSUMED; (2) `hDg`, that the derived inverse image along the chart is computed degreewise, which is exactness of the inverse image of sheaves of modules; (3) Tag 075N, via `restrictedDerivedDirectImageIso`, which is now UNCONDITIONAL -- four inputs that carrier used to ask for are gone: Tag 073N itself, the 2-isomorphism of the two legs of the square, is PROVED, as `AlgebraicGeometry.Space.restrictionRingedSquareInducedAlgebraicSpaces`, out of invertibility of the comparison map of equation 075M (`AlgebraicGeometry.Space.isIso_restrictedDirectImageComparison`) and its structure-sheaf compatibility; exactness of the module-level restrictions pi_{U,*}, pi_{V,*} is PROVED, as `AlgebraicGeometry.Space.exactFunctor_pushforwardModules_projectionRingedToposHom`; Tag 093Y for degreewise f_* is no longer needed, the unit of the exact pi_{V,*} being invertible; and the condition the composition criterion consumes at the leg f_small . pi_U is PROVED, as `AlgebraicGeometry.Space.pushforwardComputesDerived_smallEtaleRingedToposHom`, out of the unconditional Tag 0D6E for a morphism of ringed topoi; and (4) the commutation of H^i with an exact direct image, which IS proved here (`derivedPushforwardOfExactCompHomologyFunctorIso`). The source's remaining hypotheses are consumed rather than restated: representability of f by algebraic spaces is `hF`,`eF`,`hG`,`eG`, the presentations that make the right-hand side exist; quasi-compactness and quasi-separatedness enter only through `hf`; and F in LQCoh^fbc, whose role (Tag 0771 part (4)(a)) is to license computing R^i f_* in the etale topology, is built into the statement, every site here being the etale one, so the conclusion is stated for an arbitrary complex of O_X-modules and contains that case. The reduction of Tag 0771 part (3) is not needed and not used”.

> **Stacks 0GQH.** For an object `y : V ⟶ 𝒴` of `𝒴`, with `𝒱` the category fibred in
> groupoids of that object, `𝒰 = 𝒱 ×_𝒴 𝒳` the 2-fibre product — presented by the *algebraic
> space* `F = U`, because `f` is representable by algebraic spaces — and `f' : 𝒰 ⥤ 𝒱` the base
> change of `f`, inducing a morphism `U ⟶ V` on presenting algebraic spaces
> (`AlgebraicGeometry.Space.inducedAlgebraicSpacesHom`):
>
> ```text
> (R^i f_* ℱ)|_{V_étale} ≅ R^i f'_{small,*}(ℱ|_{U_étale}),
> ```
>
> naturally in the complex `ℱ` of `𝒪_𝒳`-modules. On the left, `R^i f_* ℱ` is `H^i` of the total
> right derived direct image `RfStack`, and `(-)|_{V_étale}` is inverse image along `𝒱 ⥤ 𝒴`
> followed by the restriction `π_{V,*}` of Stacks 073M. On the right, `(-)|_{U_étale}` is derived
> inverse image along `𝒰 ⥤ 𝒳` followed by `π_{U,*}`, and `R^i f'_{small,*}` is `H^i` of the total
> right derived direct image `RfSpace` of the small étale sites of the algebraic spaces `U`
> and `V`.
>
> The chain is the source's: `hDg` and `bc` are its reduction to the representable case, and
> `AlgebraicGeometry.Space.restrictedDerivedDirectImageIso` together with
> `AlgebraicGeometry.RingedToposHom.derivedPushforwardOfExactCompHomologyFunctorIso` are its
> appeal to Stacks 075N. See the implementation notes of this file for what each hypothesis is
> and where the source's hypotheses on `f` and on `ℱ` are consumed.

```lean
noncomputable def restrictedHigherDirectImageChartIso
    (Dy : DerivedCategory
        (FibredSite.associatedRingedTopos B S hS p𝒴 h𝒴 .etale).Modules ⥤
      DerivedCategory (FibredSite.associatedRingedTopos B S hS q hq .etale).Modules)
    (Dy' : DerivedCategory
        (FibredSite.associatedRingedTopos B S hS p𝒳 h𝒳 .etale).Modules ⥤
      DerivedCategory (FibredSite.associatedRingedTopos B S hS p hp .etale).Modules)
    (i : ℤ)
    (hDy : Dy ⋙ DerivedCategory.homologyFunctor
          (FibredSite.associatedRingedTopos B S hS q hq .etale).Modules i ≅
        DerivedCategory.homologyFunctor
            (FibredSite.associatedRingedTopos B S hS p𝒴 h𝒴 .etale).Modules i ⋙
          Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules
            (FibredSite.ringedToposMorphism B S hS q p𝒴 hq h𝒴 y hy .etale).toModulesHom)
    (bc : RfStack ⋙ Dy ≅ Dy' ⋙ Rf) :
    RfStack ⋙ DerivedCategory.homologyFunctor
          (FibredSite.associatedRingedTopos B S hS p𝒴 h𝒴 .etale).Modules i ⋙
        Stacks.Sheaves.RingedToposModules.RingedToposHom.pullbackModules
            (FibredSite.ringedToposMorphism B S hS q p𝒴 hq h𝒴 y hy .etale).toModulesHom ⋙
          RingedToposHom.pushforwardModules
            (projectionRingedToposHom B S hS G q hq hG eG) ≅
      Dy' ⋙ RingedToposHom.derivedPushforwardOfExact
            (projectionRingedToposHom B S hS F p hp hF eF) ⋙
        RfSpace ⋙ DerivedCategory.homologyFunctor
          (smallEtaleRingedTopos B S hS ⟨G, hG⟩).Modules i
```

## Tag 0GQI, a lemma

[Tag 0GQI](https://stacks.math.columbia.edu/tag/0GQI) in the Stacks Project.

**`AlgebraicGeometry.Stack.stacks0GQI`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AffineDirectImageFppfVanishing.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AffineDirectImageFppfVanishing.lean#L431). The attribute's comment: “all three assertions, unconditionally, for an affine 1-morphism f, on the fppf sites at module universe u: f_* restricts to LQCoh^fbc(O_X) -> LQCoh^fbc(O_Y); (1) it is exact (short exact sequences of LQCoh^fbc, read in Mod, go to short exact sequences); (2) it commutes with direct sums; (3) R^i f_* F = 0 for i > 0 and F in LQCoh^fbc(O_X)”.

> **Stacks 0GQI.** Let `f : 𝒳 ⟶ 𝒴` be an affine 1-morphism of algebraic stacks over `S`.  The
> direct image restricts to a functor `f_* : LQCoh^fbc(𝒪_𝒳) ⥤ LQCoh^fbc(𝒪_𝒴)`
> (`AlgebraicGeometry.Stack.affineLqcohSheafFbcPushforward`, which is
> `AlgebraicGeometry.Stack.fppfModulesPushforward` on objects and morphisms by
> `AlgebraicGeometry.Stack.affineLqcohSheafFbcPushforwardCompιIso`), and
>
> 1. `f_*` is exact: a sequence of `LQCoh^fbc(𝒪_𝒳)` which is short exact in `Mod(𝒪_𝒳)` goes to a
>    sequence short exact in `Mod(𝒪_𝒴)`;
> 2. `f_*` commutes with direct sums (indexed by any `ι : Type u`);
> 3. `Rⁱf_* F = 0` for every `i > 0` and `F` in `LQCoh^fbc(𝒪_𝒳)`.
>
> Modules are on the fppf sites at the module universe `u` of the schemes; `LQCoh^fbc` is
> `AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules`.

```lean
theorem stacks0GQI :
    (∀ Sq : ShortComplex (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).FullSubcategory,
        (Sq.map (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι).ShortExact →
        (Sq.map (affineLqcohSheafFbcPushforward B E h S hS f hf ⋙
          (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒴).ι)).ShortExact) ∧
      (∀ ι : Type u, PreservesColimitsOfShape (Discrete ι)
        (affineLqcohSheafFbcPushforward B E h S hS f hf)) ∧
      (∀ (i : ℕ), 0 < i → ∀ F : fppfModules B S hS 𝒳,
        lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 F →
          IsZero ((fppfModulesHigherDirectImage B S hS f i).obj F))
```

**`AlgebraicGeometry.Stack.shortExact_map_etaleModuleDirectImage_of_isZero_higherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AffineDirectImageLocallyQuasicoherent.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AffineDirectImageLocallyQuasicoherent.lean#L324). The attribute's comment: “ASSERTION (1) ONLY, exactness of f_*, on the ETALE reading of LQCoh^fbc (Tag 0771 part (4)(a), the agreement with the source's default fppf reading, is absent here). It is DEDUCED from assertion (3) exactly as the source deduces it, through Tag 015D, and that deduction is the content of this declaration; the positive-degree vanishing is the hypothesis hvan and is NOT proved anywhere in this repository. Assertion (2), commutation with direct sums, and assertion (3) itself are NOT delivered by this file: see the module's implementation notes, and note that `stacks0GQI_of_objectwise_of_preservesDirectSums` deliberately carries NO attribute because its direct-sums conjunct is returned verbatim from its own hypothesis. Stated as preservation of short exact sequences rather than as an exact functor between the subcategories because Tag 0771 part (2) is absent, so LQCoh^fbc is not known to be a weak Serre subcategory and hence not known abelian; only the OUTER terms are required to lie in LQCoh^fbc, which is weaker than the source's hypothesis. AFFINENESS IS THE BINDER `_hf` AND IS CONSUMED NOWHERE: given the vanishing, this implication holds for an arbitrary 1-morphism, so it is a generalisation of the tag's assertion (1), not a weakening. The blocking input for the rest is Tag 03DW, the etale-site analogue of Tag 01XC, which is absent from the whole repository and also blocks Tags 073H and 03M9”.

> **Assertion (1) of Stacks 0GQI from assertion (3)**, which is the source's own deduction.
>
> Let `f : 𝒳 ⟶ 𝒴` be an affine 1-morphism of algebraic stacks over `S` and suppose the higher
> direct images `Rⁱf_*` vanish in positive degrees on `LQCoh^fbc(𝒪_𝒳)`.  Then `f_*` carries a
> short exact sequence of `𝒪_𝒳`-modules on `𝒳_étale` whose outer terms lie in `LQCoh^fbc(𝒪_𝒳)` to
> a short exact sequence of `𝒪_𝒴`-modules on `𝒴_étale`; that is, `f_*` is exact on
> `LQCoh^fbc(𝒪_𝒳)`.
>
> The vanishing in positive degrees is right acyclicity for `f_*`, by **Stacks 015C** and left
> exactness of the right adjoint `f_*`, and **Stacks 015D** part (1) turns right acyclicity of the
> outer terms into short exactness of the image.  Affineness is what discharges `hvan` and is
> consumed nowhere in the deduction, which is why the binder is written `_hf`.

```lean
theorem shortExact_map_etaleModuleDirectImage_of_isZero_higherDirectImage (f : 𝒳 ⟶ 𝒴)
    (_hf : AlgebraicStacks.IsAffineHom B S hS f)
    (hvan : ∀ (i : ℕ), 0 < i → ∀ ℱ : etaleModulesOfHomSource B S hS f,
      IsLocallyQuasicoherentWithFlatBaseChangeUnivLE B E h S hS
          (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
          (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) ℱ.val →
        IsZero ((etaleModuleHigherDirectImage B S hS f i).obj ℱ))
    (Sq : ShortComplex (etaleModulesOfHomSource B S hS f)) (hSq : Sq.ShortExact)
    (h₁ : IsLocallyQuasicoherentWithFlatBaseChangeUnivLE B E h S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) Sq.X₁.val)
    (h₃ : IsLocallyQuasicoherentWithFlatBaseChangeUnivLE B E h S hS
      (CatFiberedInGroupoids.homFunctor f.hom ⋙ 𝒴.val.val.p)
      (isFiberedInGroupoids_homFunctor_comp B S hS f.hom) Sq.X₃.val) :
    (Sq.map (etaleModuleDirectImage B S hS f)).ShortExact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.8, Tag 0GQG](https://stacks.math.columbia.edu/tag/0GQG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

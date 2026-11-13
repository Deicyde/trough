---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherentWithSheafFlatBaseChange, AlgebraicGeometry.Stack.fppfModuleOfLqcohSheafFbc, AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_fppfModulesHigherDirectImage, AlgebraicGeometry.Stack.nonempty_etaleComparison_fppfModulesHigherDirectImage_iso, AlgebraicGeometry.Stack.lqcohSheafFbcModuleRule_stackModuleHigherDirectImage, AlgebraicGeometry.Stack.lqcohSheafFbcEtaleModules_stackModuleInverseImage, AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_fppfModulesPullback, AlgebraicGeometry.Stack.lqcohSheafFbcTotalDirectImageIso
statement: formalized
proof: formalized
---

# 103.8 Locally quasi-coherent modules with the flat base change property

Section 103.8 of the Stacks Project, [Tag 0GQG](https://stacks.math.columbia.edu/tag/0GQG). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0771, a proposition

[Tag 0771](https://stacks.math.columbia.edu/tag/0771) in the Stacks Project.

**`AlgebraicGeometry.Stack.isSheaf_fppf_of_isLocallyQuasicoherentWithSheafFlatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFromSheafFlatBaseChange.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFromSheafFlatBaseChange.lean#L400). The attribute's comment: “part (1): a member of LQCoh^fbc (with the flat base change property of 0762 read on sheaves) is a sheaf for the fppf topology; for every category fibred in groupoids”.

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

**`AlgebraicGeometry.Stack.fppfModuleOfLqcohSheafFbc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFromSheafFlatBaseChange.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FppfSheafFromSheafFlatBaseChange.lean#L412). The attribute's comment: “part (1), the clause `i.e. it is an object of Mod(𝒪_𝒳)`: a member of LQCoh^fbc on the étale site of an algebraic stack, as an object of LQCoh^fbc(𝒪\_𝒳) ⊆ Mod(𝒪\_𝒳) with the same underlying presheaf of modules”.

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

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_fppfModulesHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFppfHigherDirectImage.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFppfHigherDirectImage.lean#L102). The attribute's comment: “part (4)(b), in Mod(𝒪\_𝒴): for f quasi-compact and quasi-separated, each R^i f\_*F computed in the fppf topology lies in LQCoh^fbc(𝒪\_𝒴), with the flat base change property of 0762 read on sheaves; modules at the module universe u of the schemes”.

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

**`AlgebraicGeometry.Stack.nonempty_etaleComparison_fppfModulesHigherDirectImage_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFppfHigherDirectImage.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFppfHigherDirectImage.lean#L127). The attribute's comment: “part (4)(a), for the higher direct images: ε\_*(R^i f\_\{fppf,*}F) ≅ R^i f\_\{ét,*}(ε\_*F) for f quasi-compact and quasi-separated and F in LQCoh^fbc, modules at the module universe u of the schemes; the total direct image Rf\_* is lqcohSheafFbcTotalDirectImageIso”.

> **Stacks 0771, part (4)(a)**, for the higher direct images. Let `f : 𝒳 ⟶ 𝒴` be a
> quasi-compact and quasi-separated 1-morphism of algebraic stacks and `F` an object of
> `LQCoh^fbc(𝒪_𝒳)`. Then `Rⁱf_*F` is the same whether computed in the étale or in the fppf
> topology: `ε_*(Rⁱf_{fppf,*}F) ≅ Rⁱf_{ét,*}(ε_*F)`, where `ε_*` reads an fppf module on the étale
> site.
>
> Modules have sections in the universe `u` of the schemes. The assertion of the source about the
> total direct image `Rf_*` is `AlgebraicGeometry.Stack.lqcohSheafFbcTotalDirectImageIso`.

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

**`AlgebraicGeometry.Stack.lqcohSheafFbcModuleRule_stackModuleHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcHigherDirectImage.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcHigherDirectImage.lean#L60). The attribute's comment: “part (4)(b), étale topology: for f quasi-compact and quasi-separated, each R^i f\_*F computed in the étale topology lies in LQCoh^fbc(𝒪\_𝒴), with the flat base change property of 0762 read on sheaves; modules at the module universe u of the schemes”.

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

**`AlgebraicGeometry.Stack.lqcohSheafFbcEtaleModules_stackModuleInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcPullback.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcPullback.lean#L376). The attribute's comment: “part (3), on Mod(𝒳\_ét, 𝒪\_𝒳): f^* carries LQCoh^fbc(𝒪\_𝒴) into LQCoh^fbc(𝒪\_𝒳) for every 1-morphism f of algebraic stacks, with the flat base change property of 0762 read on sheaves; the module sections in the universe of the schemes. The induced functor is lqcohSheafFbcEtaleModulesPullback”.

> **Stacks 0771, part (3)**, on `Mod(𝒳_ét, 𝒪_𝒳)`: the inverse image along a 1-morphism of
> algebraic stacks of the étale sites carries `LQCoh^fbc(𝒪_𝒴)` into `LQCoh^fbc(𝒪_𝒳)`.

```lean
theorem lqcohSheafFbcEtaleModules_stackModuleInverseImage (F : StackModules B S hS .etale 𝒴)
    (hF : lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒴 F) :
    lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒳
      ((stackModuleInverseImage B S hS .etale f).obj F)
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_fppfModulesPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcPullback.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcPullback.lean#L391). The attribute's comment: “part (3), on Mod(𝒪\_𝒳): f^* carries LQCoh^fbc(𝒪\_𝒴) into LQCoh^fbc(𝒪\_𝒳) for every 1-morphism f of algebraic stacks, with the flat base change property of 0762 read on sheaves; the module sections in the universe of the schemes. The induced functor is lqcohSheafFbcFppfModulesPullback”.

> **Stacks 0771, part (3)**, on `Mod(𝒪_𝒳)`: the inverse image along a 1-morphism of algebraic
> stacks of the fppf sites carries `LQCoh^fbc(𝒪_𝒴)` into `LQCoh^fbc(𝒪_𝒳)`.

```lean
theorem lqcohSheafFbcFppfModules_fppfModulesPullback (F : fppfModules B S hS 𝒴)
    (hF : lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒴 F) :
    lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 ((fppfModulesPullback B S hS f).obj F)
```

**`AlgebraicGeometry.Stack.lqcohSheafFbcTotalDirectImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcTotalDirectImage.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcTotalDirectImage.lean#L117). The attribute's comment: “part (4)(a), total direct image Rf\_*: Rf\_\{ét,*}(ε\_*F) ≅ Rε\_*(Rf\_\{fppf,*}F) in D⁺(𝒴\_ét), for F in LQCoh^fbc (flat base change property of 0762 read on sheaves) and every 1-morphism f, so the source's quasi-compact and quasi-separated f is a special case; modules at the module universe u of the schemes. The higher direct images R^i f\_* are nonempty\_etaleComparison\_fppfModulesHigherDirectImage\_iso”.

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

**`AlgebraicGeometry.Stack.lqcohSheafFbc_hasColimits_and_agree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeColimits.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeColimits.lean#L262). The attribute's comment: “part (5): LQCoh^fbc(𝒪\_𝒳) has u-small colimits, preserved by its inclusions into Mod(𝒪\_𝒳) and into Mod(𝒳\_étale, 𝒪\_𝒳), and a colimit in Mod(𝒪\_𝒳) of members restricts to a colimit in Mod(𝒳\_étale, 𝒪\_𝒳); flat base change property of 0762 read on sheaves”.

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

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_fppfInternalHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeInternalHom.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeInternalHom.lean#L67). The attribute's comment: “part (7): SheafHom(F, G) of Mod(𝒪\_𝒳) lies in LQCoh^fbc(𝒪\_𝒳) for F of finite presentation in Mod(𝒪\_𝒳) and G in LQCoh^fbc(𝒪\_𝒳), with the flat base change property of 0762 read on sheaves; modules at the module universe u of the schemes”.

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

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_sheafTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeTensor.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeTensor.lean#L69). The attribute's comment: “part (6): F ⊗\_\{𝒪\_𝒳} G of Mod(𝒪\_𝒳) lies in LQCoh^fbc(𝒪\_𝒳) for F and G in LQCoh^fbc(𝒪\_𝒳), with the flat base change property of 0762 read on sheaves; modules at the module universe u of the schemes”.

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

**`AlgebraicGeometry.Stack.isWeakSerreClass_lqcohSheafFbcEtaleModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeWeakSerre.lean, line 506](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeWeakSerre.lean#L506). The attribute's comment: “part (2), the étale half: LQCoh^fbc is a weak Serre subcategory of Mod(𝒳\_ét, 𝒪\_𝒳), with the flat base change property of 0762 read on sheaves; modules at the module universe u”.

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

**`AlgebraicGeometry.Stack.isWeakSerreClass_lqcohSheafFbcFppfModules`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeWeakSerreFppf.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafFlatBaseChangeWeakSerreFppf.lean#L292). The attribute's comment: “part (2), fppf half: LQCoh^fbc is a weak Serre subcategory of Mod(𝒪\_𝒳), with the flat base change property of 0762 read on sheaves; modules at the module universe u”.

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

**`AlgebraicGeometry.Stack.isLocallyQuasicoherentWithFlatBaseChange_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSmoothLocal.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatBaseChangeSmoothLocal.lean#L154). The attribute's comment: “part (1), the local quasi-coherence half: the criterion along a jointly surjective family of smooth morphisms, with the flat base change property of the source assumed (Stacks 0764 part (3))”.

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

**`AlgebraicGeometry.Stack.lqcohSheafFbcEtaleModules_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFlatDescent.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFlatDescent.lean#L98). The attribute's comment: “part (1), on Mod(𝒳\_ét, 𝒪\_𝒳), with the flat base change property of 0762 read on sheaves; the module sections in the universe of the schemes”.

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

**`AlgebraicGeometry.Stack.lqcohSheafFbcFppfModules_of_isFlat_isLocallyOfFinitePresentation_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFlatDescent.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LqcohSheafFbcFlatDescent.lean#L203). The attribute's comment: “part (2), on Mod(𝒪\_𝒳) (fppf), with the flat base change property of 0762 read on sheaves; the module sections in the universe of the schemes”.

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

**`AlgebraicGeometry.Stack.restrictedFppfModulesHigherDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/RestrictedFppfHigherDirectImage.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/RestrictedFppfHigherDirectImage.lean#L80). The attribute's comment: “the whole lemma, with Mod(O\_X) the sheaves of modules at the universe u of the schemes (the source's setting): for f : X -> Y quasi-compact, quasi-separated and representable by algebraic spaces, F in LQCoh^fbc(O\_X) (the flat base change property read on sheaves, Stacks 0762) and an object y : V -> Y over a scheme V, the 2-fibre product U = V x\_Y X is an algebraic space, and for every presentation of it and every i, (R^i f\_* F)|\_\{V\_etale} = R^i f'\_\{small,*}(F|\_\{U\_etale}), with R^i f\_* the fppf higher direct image of Mod(O\_X)”.

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

## Tag 0GQI, a lemma

[Tag 0GQI](https://stacks.math.columbia.edu/tag/0GQI) in the Stacks Project.

**`AlgebraicGeometry.Stack.stacks0GQI`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AffineDirectImageFppfVanishing.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/AffineDirectImageFppfVanishing.lean#L433). The attribute's comment: “all three assertions, for an affine 1-morphism f, on the fppf sites at module universe u: f\_* restricts to LQCoh^fbc(O\_X) -> LQCoh^fbc(O\_Y); (1) it is exact (short exact sequences of LQCoh^fbc, read in Mod, go to short exact sequences); (2) it commutes with direct sums; (3) R^i f\_* F = 0 for i > 0 and F in LQCoh^fbc(O\_X)”.

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

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.8, Tag 0GQG](https://stacks.math.columbia.edu/tag/0GQG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isQuasicoherentOnSite_of_isSmooth_jointlySurjective, AlgebraicGeometry.Stack.isQuasicoherentOnSite_of_isFlat_isLfp_jointlySurjective, AlgebraicGeometry.Stack.LisseEtale.isQuasicoherentClause_fppf_moduleLowerShriek, AlgebraicGeometry.Stack.FlatFppf.isQuasicoherentOnSite_moduleLowerShriek_of_isQuasicoherentOnSite, AlgebraicGeometry.Stack.LisseEtale.isQuasicoherentOnSite_moduleLowerShriek, AlgebraicGeometry.Stack.FlatFppf.isQuasicoherentOnSite_moduleLowerShriek, AlgebraicGeometry.Stack.FlatFppf.quasicoherentEquivalence, AlgebraicGeometry.Stack.FlatFppf.isQuasicoherentOnSite_modulePullback_of_lqcohSheafFbc
statement: formalized
proof: formalized
---

# 103.16 Quasi-coherent modules and the lisse-étale and flat-fppf sites

Section 103.16 of the Stacks Project, [Tag 07AY](https://stacks.math.columbia.edu/tag/07AY). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07AZ, a lemma

[Tag 07AZ](https://stacks.math.columbia.edu/tag/07AZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasicoherentOnSite_of_isSmooth_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/JointlySurjectiveDescent.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/JointlySurjectiveDescent.lean#L317). The attribute's comment: “part (1): the smooth family on the étale site”.

> **Stacks 07AZ, part (1).**  Let `f j : 𝒵 j ⟶ 𝒳` be a family of smooth 1-morphisms of
> algebraic stacks over `S` which is jointly surjective, that is `|𝒳| = ⋃ j, |f j|(|𝒵 j|)` for the
> points of **Stacks 04XG**, and let `M` be a sheaf of `𝒪_𝒳`-modules on `𝒳_étale`.  If every
> inverse image `f j^{-1} M` is quasi-coherent, then so is `M`.
>
> Joint surjectivity turns every object of `𝒳` into one covered, étale-locally, by images of
> objects of the members of the family; quasi-coherence of the inverse images presents `M` globally
> on a covering of each of those images, and quasi-coherence is local.

```lean
theorem isQuasicoherentOnSite_of_isSmooth_jointlySurjective
    (hsmooth : ∀ j, AlgebraicStacks.IsSmooth B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒳)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (M : SheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids (B.baseTopology .etale)
      (B.baseTopology_le_topology .etale)))
    (hM : ∀ j, ((familyModulePullback B S hS 𝒵 f (B.baseTopology .etale)
      (B.baseTopology_le_topology .etale) j).obj M).IsQuasicoherentOnSite) :
    M.IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Stack.isQuasicoherentOnSite_of_isFlat_isLfp_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/JointlySurjectiveDescent.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/JointlySurjectiveDescent.lean#L341). The attribute's comment: “part (2): the flat, locally finitely presented family on the fppf site”.

> **Stacks 07AZ, part (2).**  Let `f j : 𝒵 j ⟶ 𝒳` be a family of 1-morphisms of algebraic
> stacks over `S` which are each flat and locally of finite presentation and which is jointly
> surjective, that is `|𝒳| = ⋃ j, |f j|(|𝒵 j|)`, and let `M` be a sheaf of `𝒪_𝒳`-modules on
> `𝒳_fppf`.  If every inverse image `f j^{-1} M` is quasi-coherent, then so is `M`.
>
> This is the argument of part (1) with "smooth" replaced by "flat and locally of finite
> presentation" and the étale covering of **Stacks 06XH** by the fppf covering of
> **Stacks 07AN**.

```lean
theorem isQuasicoherentOnSite_of_isFlat_isLfp_jointlySurjective
    (hflat : ∀ j, AlgebraicStacks.IsFlat B S hS (f j))
    (hlfp : ∀ j, AlgebraicStacks.IsLocallyOfFinitePresentation B S hS (f j))
    (hjs : (Set.univ : Set (AlgebraicStacks.points B S hS 𝒳)) =
      ⋃ j, Set.range (AlgebraicStacks.pointsMap B S hS (f j)))
    (M : SheafOfModules.{u} (ringStructureSheafCore B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl))
    (hM : ∀ j, ((familyModulePullback B S hS 𝒵 f B.topology le_rfl j).obj
      M).IsQuasicoherentOnSite) :
    M.IsQuasicoherentOnSite
```

## Tag 07B0, a lemma

[Tag 07B0](https://stacks.math.columbia.edu/tag/07B0) in the Stacks Project.

**`AlgebraicGeometry.Stack.LisseEtale.isQuasicoherentClause_fppf_moduleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LowerShriekQuasicoherent.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LowerShriekQuasicoherent.lean#L215). The attribute's comment: “part (1): for every quasi-coherent module `H` on the lisse-étale site of an algebraic stack `𝒳`, `g_!H` is a quasi-coherent module on `𝒳` — an fppf sheaf, quasi-coherent on `(𝒳_fppf, O_𝒳)` (the 06WG notion, read through the fppf clause of 0EM8)”.

> Let `𝒳` be an algebraic stack and let `H` be a quasi-coherent
> `O_{𝒳_{lisse,étale}}`-module on the lisse-étale site of `𝒳`. Then `g_!H` is a quasi-coherent
> module on `𝒳`, where `g_!` is the lower shriek on sheaves of modules of **Stacks 0789** (1).
>
> A quasi-coherent module on `𝒳` is one in the sense of **Stacks 06WG**: a sheaf for the fppf
> topology which is quasi-coherent on `(𝒳_fppf, O_𝒳)`. The conclusion is this property of the
> underlying presheaf of modules of the sheaf `g_!H` on `𝒳_étale`, in the form of
> `AlgebraicGeometry.FibredSite.IsQuasicoherentClause` at `.fppf` (**Stacks 0EM8**).

```lean
theorem isQuasicoherentClause_fppf_moduleLowerShriek
    (H : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (ringedTopos.{u, t} B S hS 𝒳
      (closedUnderSmoothMorphisms.{u, t} B S hS 𝒳)).O))
    (hH : H.IsQuasicoherentOnSite) :
    FibredSite.IsQuasicoherentClause B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids .fppf
      ((moduleLowerShriek.{u, t} B S hS 𝒳).obj H).val
```

**`AlgebraicGeometry.Stack.FlatFppf.isQuasicoherentOnSite_moduleLowerShriek_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LowerShriekQuasicoherent.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LowerShriekQuasicoherent.lean#L309). The attribute's comment: “part (2): for every quasi-coherent module `H` on the flat-fppf site of an algebraic stack `𝒳`, `g_!H` is a quasi-coherent module on `𝒳`, i.e. quasi-coherent on `(𝒳_fppf, O_𝒳)` (06WG)”.

> Let `𝒳` be an algebraic stack and let `H` be a quasi-coherent
> `O_{𝒳_{flat,fppf}}`-module on the flat-fppf site of `𝒳`. Then `g_!H` is a quasi-coherent module
> on `𝒳`, where `g_!` is the lower shriek on sheaves of modules of **Stacks 0789** (2): it is
> quasi-coherent on `(𝒳_fppf, O_𝒳)`, the ambient site being `𝒳_fppf` itself, which is
> quasi-coherence of a module on `𝒳` in the sense of **Stacks 06WG**.

```lean
theorem isQuasicoherentOnSite_moduleLowerShriek_of_isQuasicoherentOnSite
    (H : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (subsiteRingedTopos B S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids B.topology le_rfl (objectProperty B S hS 𝒳)).O))
    (hH : H.IsQuasicoherentOnSite) :
    ((moduleLowerShriek B S hS 𝒳).obj H).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Stack.LisseEtale.isQuasicoherentOnSite_moduleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SubsiteLowerShriekQuasicoherent.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SubsiteLowerShriekQuasicoherent.lean#L228). The attribute's comment: “the lisse-étale clause, for an `H` that has a global presentation, with conclusion quasi-coherence on `𝒳_étale`. Three conditions: (a) `H` has a global presentation rather than being quasi-coherent — the source's reduction to this case, through 07AT, 07AZ and the base-change isomorphism for `g_!` on sheaves of modules, is not in the library; (b) 078A, `g_!O = O_𝒳`, as a hypothesis, which this library proves only from a localisation hypothesis with no producer; (c) essential smallness of the category underlying the stack. Passing from `𝒳_étale` to `𝒳_fppf`, the source's last sentence, is 0EM8 over an input left open there”.

> **Stacks 07B0 (1) for an `H` with a global presentation**: if `H` is an
> `O_{𝒳_{lisse,étale}}`-module with a global presentation, then `g_!H` is quasi-coherent on
> `(𝒳_étale, O_𝒳)`.
>
> The three conditions are the ones named in the tag; see the module documentation for where each
> comes from and what is missing without it.

```lean
theorem isQuasicoherentOnSite_moduleLowerShriek
    (hO : IsIso (unitLowerShriekMap.{u, t} B S hS 𝒳))
    (H : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (ringedTopos.{u, t} B S hS 𝒳
      (closedUnderSmoothMorphisms.{u, t} B S hS 𝒳)).O))
    (hH : H.IsPresentedByGlobalSections) :
    ((moduleLowerShriek.{u, t} B S hS 𝒳).obj H).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Stack.FlatFppf.isQuasicoherentOnSite_moduleLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SubsiteLowerShriekQuasicoherent.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SubsiteLowerShriekQuasicoherent.lean#L261). The attribute's comment: “the flat-fppf clause, for an `H` that has a global presentation. Three conditions: (a) `H` has a global presentation rather than being quasi-coherent — the source's reduction to this case, through 07AT, 07AZ and the base-change isomorphism for `g_!` on sheaves of modules, is not in the library; (b) 078A, `g_!O = O_𝒳`, as a hypothesis, which this library proves only from a localisation hypothesis with no producer; (c) essential smallness of the category underlying the stack. The conclusion is the clause's own: quasi-coherence on `𝒳_fppf`, i.e. of a module on `𝒳` in the sense of 06WG”.

> **Stacks 07B0 (2) for an `H` with a global presentation**: if `H` is an
> `O_{𝒳_{flat,fppf}}`-module with a global presentation, then `g_!H` is a quasi-coherent module on
> `𝒳`, that is, quasi-coherent on `(𝒳_fppf, O_𝒳)`.
>
> Here the ambient site is `𝒳_fppf` already, so the conclusion is quasi-coherence of a module on
> `𝒳` in the sense of **Stacks 06WG** and nothing further is needed — the source's "In case (2) we
> are done". The three conditions are the ones named in the tag.

```lean
theorem isQuasicoherentOnSite_moduleLowerShriek
    (hO : IsIso (unitLowerShriekMap B S hS 𝒳))
    (H : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf (subsiteRingedTopos B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids B.topology le_rfl (objectProperty B S hS 𝒳)).O))
    (hH : H.IsPresentedByGlobalSections) :
    ((moduleLowerShriek B S hS 𝒳).obj H).IsQuasicoherentOnSite
```

## Tag 07B1, a lemma

[Tag 07B1](https://stacks.math.columbia.edu/tag/07B1) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.quasicoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfQuasicoherentEquivalence.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfQuasicoherentEquivalence.lean#L125). The attribute's comment: “part (2)(a): g^\{-1} and g\_! are mutually inverse functors between QCoh(𝒪\_𝒳) and QCoh(𝒳\_\{flat,fppf}, 𝒪\_\{𝒳\_\{flat,fppf}})”.

> For an algebraic stack `𝒳`, the functors `g^{-1}` and `g_!` are mutually inverse equivalences
> between `QCoh(𝒪_𝒳)` and `QCoh(𝒳_{flat,fppf}, 𝒪_{𝒳_{flat,fppf}})`. The functor of the equivalence
> is `g^{-1}` and its inverse is `g_!`, both on the nose (`quasicoherentEquivalence_functor_comp_ι`,
> `quasicoherentEquivalence_inverse_comp_ι`); the unit is the inverse of the counit
> `g_!g^{-1}𝓖 ⟶ 𝓖` of `g_! ⊣ g^{-1}`, an isomorphism on quasi-coherent modules, and the counit is
> the inverse of its unit `ℋ ⟶ g^{-1}g_!ℋ`.

```lean
def quasicoherentEquivalence :
    AlgebraicStacks.quasicoherentModules B S hS 𝒳 ≌ quasicoherentSubsiteModules B S hS 𝒳
```

**`AlgebraicGeometry.Stack.FlatFppf.isQuasicoherentOnSite_modulePullback_of_lqcohSheafFbc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfQuasicoherentEquivalence.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfQuasicoherentEquivalence.lean#L147). The attribute's comment: “part (2)(b): for F in LQCoh^fbc(𝒪\_𝒳), g^\{-1}F is in QCoh(𝒪\_\{𝒳\_\{flat,fppf}})”.

> For `𝓕` in `LQCoh^fbc(𝒪_𝒳)`, the module `g^{-1}𝓕` on the flat-fppf site is quasi-coherent.

```lean
theorem isQuasicoherentOnSite_modulePullback_of_lqcohSheafFbc (F : fppfModules B S hS 𝒳)
    (hF : lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳 F) :
    ((modulePullback B S hS 𝒳).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Stack.FlatFppf.coheratorIsoLowerShriekModulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfQuasicoherentEquivalence.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfQuasicoherentEquivalence.lean#L200). The attribute's comment: “part (2)(c): Q(F) = g\_! g^\{-1} F for F in LQCoh^fbc(𝒪\_𝒳), Q the coherator of 0778”.

> For `𝓕` in `LQCoh^fbc(𝒪_𝒳)`, `Q(𝓕) = g_!g^{-1}𝓕`, naturally in `𝓕`, where
> `Q : LQCoh^fbc(𝒪_𝒳) ⥤ QCoh(𝒪_𝒳)` is the coherator of **Stacks 0778**
> (`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoherator`). The isomorphism at `𝓕` is
> `g_!g^{-1}` of the adjunction map `Q(𝓕) ⟶ 𝓕`, preceded by the inverse of the counit
> `g_!g^{-1}Q(𝓕) ⟶ Q(𝓕)`.

```lean
def coheratorIsoLowerShriekModulePullback :
    AlgebraicStacks.lqcohFbcCoherator B E h S hS 𝒳 ⋙
        AlgebraicStacks.quasicoherentInclusion B S hS 𝒳 ≅
      (lqcohSheafFbcFppfModules.{u, w, u} B E h S hS 𝒳).ι ⋙ modulePullback B S hS 𝒳 ⋙
        moduleLowerShriek B S hS 𝒳
```

**`AlgebraicGeometry.Stack.LisseEtale.quasicoherentEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleQuasicoherentEquivalence.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleQuasicoherentEquivalence.lean#L193). The attribute's comment: “part (1)(a): g^\{-1} and g\_! are mutually inverse functors between QCoh(𝒪\_𝒳) and QCoh(𝒳\_\{lisse,étale}, 𝒪\_\{𝒳\_\{lisse,étale}})”.

> **Stacks 07B1 (1)(a).** For an algebraic stack `𝒳`, the functors `g^{-1}` and `g_!` are
> mutually inverse equivalences between `QCoh(𝒪_𝒳)` and
> `QCoh(𝒳_{lisse,étale}, 𝒪_{𝒳_{lisse,étale}})`. The functor of the equivalence is `g^{-1}` and its
> inverse is `g_!`, both on the nose (`quasicoherentEquivalence_functor_comp_ι`,
> `quasicoherentEquivalence_inverse_comp_ι`, `fppfModuleLowerShriek_obj_val`); the unit is the
> inverse of the counit `g_!g^{-1}𝓖 ⟶ 𝓖` of `g_! ⊣ g^{-1}`, an isomorphism on quasi-coherent
> modules, and the counit is the inverse of its unit `ℋ ⟶ g^{-1}g_!ℋ`.

```lean
def quasicoherentEquivalence :
    AlgebraicStacks.quasicoherentModules B S hS 𝒳 ≌ quasicoherentSubsiteModules.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.LisseEtale.isQuasicoherentOnSite_modulePullback_of_lqcohSheafFbc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleQuasicoherentEquivalence.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleQuasicoherentEquivalence.lean#L250). The attribute's comment: “part (1)(b): for F in LQCoh^fbc(𝒪\_𝒳), g^\{-1}F is in QCoh(𝒪\_\{𝒳\_\{lisse,étale}})”.

> **Stacks 07B1 (1)(b).** For `𝓕` in `LQCoh^fbc(𝒪_𝒳) ⊆ Mod(𝒳_étale, 𝒪_𝒳)`, the module
> `g^{-1}𝓕` on the lisse-étale site is quasi-coherent.

```lean
theorem isQuasicoherentOnSite_modulePullback_of_lqcohSheafFbc
    (F : etaleTopologyModules B S hS 𝒳) (hF : lqcohSheafFbcEtaleModules.{u, w, u} B E h S hS 𝒳 F) :
    ((modulePullback.{u, w} B S hS 𝒳).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Stack.LisseEtale.coheratorIsoLowerShriekModulePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleQuasicoherentEquivalence.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleQuasicoherentEquivalence.lean#L293). The attribute's comment: “part (1)(c): Q(F) = g\_! g^\{-1} F for F in LQCoh^fbc(𝒪\_𝒳), Q the coherator of 0778”.

> **Stacks 07B1 (1)(c).** For `𝓕` in `LQCoh^fbc(𝒪_𝒳)`, `Q(𝓕) = g_!g^{-1}𝓕`, naturally in `𝓕`,
> as objects of `QCoh(𝒪_𝒳)`, where `Q : LQCoh^fbc(𝒪_𝒳) ⥤ QCoh(𝒪_𝒳)` is the coherator of
> **Stacks 0778** (`AlgebraicGeometry.Stack.AlgebraicStacks.lqcohFbcCoherator`), `g^{-1}𝓕` is
> quasi-coherent by (1)(b) and `g_!` is the inverse equivalence of (1)(a). The isomorphism at `𝓕` is
> the unit `Q(𝓕) ≅ g_!g^{-1}Q(𝓕)` of (1)(a) followed by `g_!g^{-1}` of the adjunction map
> `Q(𝓕) ⟶ 𝓕`.

```lean
def coheratorIsoLowerShriekModulePullback :
    AlgebraicStacks.lqcohFbcCoherator B E h S hS 𝒳 ≅
      lqcohFbcModulePullback B S hS 𝒳 E h ⋙ quasicoherentModuleLowerShriek B S hS 𝒳
```

## Tag 07B4, a lemma

[Tag 07B4](https://stacks.math.columbia.edu/tag/07B4) in the Stacks Project.

**`AlgebraicGeometry.Stack.FlatFppf.isWeakSerreClass_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfWeakSerre.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FlatFppfWeakSerre.lean#L242). The attribute's comment: “part (2): QCoh(O\_\{X\_\{flat,fppf}}) is a weak Serre subcategory of Mod(O\_\{X\_\{flat,fppf}})”.

> **Stacks 07B4 (2).** For an algebraic stack `𝒳`, the quasi-coherent modules on the flat-fppf
> site `𝒳_{flat,fppf}`, ringed by `𝒪_{𝒳_{flat,fppf}}`, form a weak Serre subcategory of
> `Mod(𝒪_{𝒳_{flat,fppf}})`.
>
> The flat objects over affine schemes are a cover-dense subsite of `𝒳_{flat,fppf}` which, with the
> arrows over flat, locally finitely presented morphisms, has fibre products along its coverings,
> finite covers refining its covering sieves, and flat factorizations of its arrows; so
> `Stacks.FlatAffineSite.isWeakSerreClass_isQuasicoherentOnSite_of_affineSubsite` applies.

```lean
theorem isWeakSerreClass_isQuasicoherentOnSite :
    (SheafOfModules.isQuasicoherentOnSite (Stacks.SheafOfModules.Tensor.ringSheaf
      (subsiteRingedTopos B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids B.topology le_rfl
        (objectProperty B S hS 𝒳)).O) :
      ObjectProperty (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf
        (subsiteRingedTopos B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids B.topology le_rfl
          (objectProperty B S hS 𝒳)).O))).IsWeakSerreClass
```

**`AlgebraicGeometry.Stack.LisseEtale.isWeakSerreClass_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleWeakSerre.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/LisseEtaleWeakSerre.lean#L249). The attribute's comment: “part (1)”.

> For every algebraic stack `𝒳`, the quasi-coherent modules on the lisse-étale site
> `𝒳_{lisse,étale}`, ringed by `𝒪_{𝒳_{lisse,étale}}` (the restriction of the structure sheaf,
> `AlgebraicGeometry.Stack.LisseEtale.ringedTopos'`), form a weak Serre subcategory of
> `Mod(𝒪_{𝒳_{lisse,étale}})`.

```lean
theorem isWeakSerreClass_isQuasicoherentOnSite :
    (SheafOfModules.isQuasicoherentOnSite
        (Stacks.SheafOfModules.Tensor.ringSheaf (ringedTopos'.{u, t} B S hS 𝒳).O) :
      ObjectProperty (SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (ringedTopos'.{u, t} B S hS 𝒳).O))).IsWeakSerreClass
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 103.16, Tag 07AY](https://stacks.math.columbia.edu/tag/07AY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

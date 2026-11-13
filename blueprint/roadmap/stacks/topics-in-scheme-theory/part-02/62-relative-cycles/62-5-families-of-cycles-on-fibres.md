---
declaration: section
origin: cited
lean: Stacks.Chow.baseChangeFamilyOfIsPullback, Stacks.Chow.FamilyOfCycles, Stacks.Chow.properPushforwardFamily, Stacks.Chow.flatPullbackFamily, Stacks.Chow.restrictedFamily, Stacks.Chow.baseChangeFamily_baseChangeFamily_comp, Stacks.Chow.restrictedFamily_eq_flatPullbackFamily_baseChangeFamily, Stacks.Chow.baseChangeFamily_flatPullbackFamily
statement: formalized
proof: formalized
---

# 62.5 Families of cycles on fibres

Section 62.5 of the Stacks Project, [Tag 0H4N](https://stacks.math.columbia.edu/tag/0H4N). 11 tags here are carried by 38 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H4N, the section

[Tag 0H4N](https://stacks.math.columbia.edu/tag/0H4N) in the Stacks Project.

**`Stacks.Chow.baseChangeFamilyOfIsPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeSquare.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeSquare.lean#L80). The attribute's comment: “base change of a family of cycles on fibres through a cartesian square”.

> **The base change of a family of cycles through a cartesian square.** For a cartesian square
> with right-hand column `f : X ⟶ S`, bottom edge `g : T ⟶ S` and left-hand column `p : P ⟶ T`,
> the base change `g^*α`, read on the fibres of `p` through the canonical isomorphism
> `P ≅ X ×_S T` over `T`.

```lean
def baseChangeFamilyOfIsPullback (α : FamilyOfCycles f r) : FamilyOfCycles p r
```

**`Stacks.Chow.FamilyOfCycles`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Basic.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Basic.lean#L84). The attribute's comment: “a family of `r`-cycles on the fibres of `X/S`”.

> A family of `r`-cycles on the fibres of `f`: an `r`-cycle on the scheme-theoretic fibre
> over each point of the base.

```lean
abbrev FamilyOfCycles {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] (r : ℕ) : Type u
```

**`Stacks.Chow.properPushforwardFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedImmersion.lean#L129). The attribute's comment: “proper pushforward of a family of cycles on fibres”.

> **The pushforward `f_*α` of a family of cycles on fibres.** The member over `s` is the proper
> pushforward of the member of `α` over `s` along the morphism `f_s : X_s ⟶ Y_s` induced on the
> fibres.

```lean
def properPushforwardFamily (r : ℕ) (α : FamilyOfCycles sX r) : FamilyOfCycles sY r
```

**`Stacks.Chow.flatPullbackFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatPullbackFamily.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatPullbackFamily.lean#L162). The attribute's comment: “flat pullback of a family of cycles on fibres”.

> **Stacks Project, Section 0H4N.** The flat pullback `j^*α` of a family `α` of `r`-cycles on
> the fibres of `X/S` along a flat morphism `j : U ⟶ X` of schemes over `S`, locally of finite type
> and of relative dimension `e`: the family of `(r+e)`-cycles on the fibres of `U/S` whose member
> over `s` is the flat pullback of `α_s` along `U_s ⟶ X_s`.

```lean
def flatPullbackFamily {X S U : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] (fU : U ⟶ S)
    [LocallyOfFiniteType fU] (j : U ⟶ X) [LocallyOfFiniteType j] [Flat j] (h : j ≫ f = fU)
    (e : ℕ) (he : AlgebraicGeometry.RelativeDimension j e) (r : ℕ) (α : FamilyOfCycles f r) :
    FamilyOfCycles fU (r + e)
```

**`Stacks.Chow.restrictedFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Restriction.lean, line 306](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Restriction.lean#L306). The attribute's comment: “restriction of a family of cycles on fibres to open subschemes”.

> The restriction of a family of cycles to the fibres of an open subscheme, specified by
> restriction of the coefficients along the canonical fibre map.

```lean
def restrictedFamily {X S U V : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (fU : U ⟶ V) [LocallyOfFiniteType fU]
    (j : U ⟶ X) [IsOpenImmersion j] (i : V ⟶ S) [IsOpenImmersion i]
    (h : j ≫ f = fU ≫ i) (r : ℕ) (α : FamilyOfCycles f r) :
    {β : FamilyOfCycles fU r //
      ∀ (t : V) (x : fU.fiber t),
        (β t : AlgebraicCycle (fU.fiber t) ℤ) x =
          (α (i t) : AlgebraicCycle (f.fiber (i t)) ℤ)
            (restrictedFiberMap f fU j i h t x)}
```

## Tag 0H4P, a lemma

[Tag 0H4P](https://stacks.math.columbia.edu/tag/0H4P) in the Stacks Project.

**`Stacks.Chow.baseChangeFamily_baseChangeFamily_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean#L98). The attribute's comment: “part (1): base change is functorial”.

> **Stacks Project, Tag 0H4P, part (1).** Base change of families of cycles on fibres is
> functorial: base changing a family `α` of `r`-cycles on the fibres of `X/S` along `g : S' ⟶ S`
> and then along `h : S'' ⟶ S'` is base changing it along `h ≫ g`, the two families being
> identified through the canonical isomorphism `(X ×_S S') ×_{S'} S'' ≅ X ×_S S''`.

```lean
theorem baseChangeFamily_baseChangeFamily_comp {X S S' S'' : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (g : S' ⟶ S) (h : S'' ⟶ S') (r : ℕ) (α : FamilyOfCycles f r) :
    baseChangeFamily (pullback.snd f g) h r (baseChangeFamily f g r α) =
      fun u => fiberCycleRestrict (pullback.snd f (h ≫ g)) (pullback.snd (pullback.snd f g) h)
        (pullbackLeftPullbackSndIso f g h).hom (pullbackLeftPullbackSndIso_hom_snd f g h) u r
        (baseChangeFamily f (h ≫ g) r α u)
```

**`Stacks.Chow.restrictedFamily_eq_flatPullbackFamily_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean#L150). The attribute's comment: “part (2): restriction is base change followed by flat pullback”.

> **Stacks Project, Tag 0H4P, part (2).** Restriction of families of cycles on fibres is a
> combination of base change and flat pullback: for open subschemes `U ⊆ X` and `V ⊆ S` with
> `f(U) ⊆ V`, the restriction `α|_U` of a family `α` of `r`-cycles on the fibres of `X/S` is the
> flat pullback, along the open immersion `U ⟶ X ×_S V` (flat of relative dimension zero), of the
> base change of `α` along `V ⟶ S`.

```lean
theorem restrictedFamily_eq_flatPullbackFamily_baseChangeFamily (r : ℕ)
    (α : FamilyOfCycles f r) :
    (restrictedFamily f fU j i h r α).1 =
      flatPullbackFamily (pullback.snd f i) fU (pullback.lift j fU h) (pullback.lift_snd _ _ _) 0
        (relativeDimension_of_isOpenImmersion _) r (baseChangeFamily f i r α)
```

**`Stacks.Chow.baseChangeFamily_flatPullbackFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean#L183). The attribute's comment: “part (3): flat pullback commutes with base change”.

> **Stacks Project, Tag 0H4P, part (3).** Flat pullback of families of cycles on fibres commutes
> with base change: for a flat morphism `j : U ⟶ X` over `S`, locally of finite type and of
> relative dimension `e`, and a morphism `g : T ⟶ S`, the base change of `j^*α` along `g` is the
> flat pullback of `g^*α` along the base change `U ×_S T ⟶ X ×_S T` of `j`.

```lean
theorem baseChangeFamily_flatPullbackFamily {X S U T : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (fU : U ⟶ S) [LocallyOfFiniteType fU] (j : U ⟶ X)
    [LocallyOfFiniteType j] [Flat j] (h : j ≫ f = fU) (e : ℕ)
    (he : AlgebraicGeometry.RelativeDimension j e) (g : T ⟶ S) (r : ℕ)
    (α : FamilyOfCycles f r) :
    baseChangeFamily fU g (r + e) (flatPullbackFamily f fU j h e he r α) =
      flatPullbackFamily (pullback.snd f g) (pullback.snd fU g) (pullbackRestrict f fU j h g)
        (pullbackRestrict_snd f fU j h g) e (relativeDimension_pullbackRestrict f fU j h g he) r
        (baseChangeFamily f g r α)
```

**`Stacks.Chow.flatPullbackFamily_flatPullbackFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean#L258). The attribute's comment: “part (4): flat pullback is functorial”.

> **Stacks Project, Tag 0H4P, part (4).** Flat pullback of families of cycles on fibres is
> functorial: for flat morphisms `j : U ⟶ X` and `k : V ⟶ U` over `S`, locally of finite type and
> of relative dimensions `e` and `e'`, pulling a family `α` of `r`-cycles on the fibres of `X/S`
> back along `j` and then along `k` is pulling it back along `k ≫ j`, which has relative dimension
> `e' + e`.
>
> The two families are families of cycles of the dimensions `(r + e) + e'` and `r + (e' + e)`,
> which are equal but not definitionally so; the statement is the equality of the underlying
> cycles on every fibre of `V/S`.

```lean
theorem flatPullbackFamily_flatPullbackFamily {X S U V : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (fU : U ⟶ S) [LocallyOfFiniteType fU] (fV : V ⟶ S)
    [LocallyOfFiniteType fV] (j : U ⟶ X) [LocallyOfFiniteType j] [Flat j] (k : V ⟶ U)
    [LocallyOfFiniteType k] [Flat k] (h : j ≫ f = fU) (hk : k ≫ fU = fV) (e e' : ℕ)
    (he : AlgebraicGeometry.RelativeDimension j e)
    (he' : AlgebraicGeometry.RelativeDimension k e') (r : ℕ) (α : FamilyOfCycles f r) (s : S) :
    (flatPullbackFamily fU fV k hk e' he' (r + e) (flatPullbackFamily f fU j h e he r α) s :
        AlgebraicCycle (fV.fiber s) ℤ) =
      (flatPullbackFamily f fV (k ≫ j) (by rw [Category.assoc, h, hk]) (e' + e)
        (AlgebraicGeometry.RelativeDimension.comp_of_flat k j he' he) r α s :
          AlgebraicCycle (fV.fiber s) ℤ)
```

**`Stacks.Chow.baseChangeFamily_properPushforwardFamily_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean#L326). The attribute's comment: “part (5): proper pushforward commutes with base change”.

> **Stacks Project, Tag 0H4P, part (5).** Proper pushforward of families of cycles on fibres
> commutes with base change: for a proper morphism `f : X ⟶ Y` of schemes locally of finite type
> over `S` and a morphism `g : S' ⟶ S`, the base change of `f_*α` along `g` is the pushforward of
> `g^*α` along the base change `X ×_S S' ⟶ Y ×_S S'` of `f`.

```lean
theorem baseChangeFamily_properPushforwardFamily_of_isProper (r : ℕ) (α : FamilyOfCycles sX r) :
    baseChangeFamily sY g r (properPushforwardFamily sX sY f hf r α) =
      properPushforwardFamily (pullback.snd sX g) (pullback.snd sY g)
        (baseChangeMap sX sY f hf g) (baseChangeMap_snd sX sY f hf g) r
        (baseChangeFamily sX g r α)
```

**`Stacks.Chow.properPushforwardFamily_properPushforwardFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean#L391). The attribute's comment: “part (6): proper pushforward is functorial”.

> **Stacks Project, Tag 0H4P, part (6).** Proper pushforward of families of cycles on fibres is
> functorial: for proper morphisms `f₁ : X ⟶ Y` and `f₂ : Y ⟶ Z` of schemes locally of finite type
> over `S`, pushing a family of `r`-cycles on the fibres of `X/S` forward along `f₁` and then along
> `f₂` is pushing it forward along `f₁ ≫ f₂`.

```lean
theorem properPushforwardFamily_properPushforwardFamily {S X Y Z : Scheme.{u}} (sX : X ⟶ S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ S) [LocallyOfFiniteType sY] (sZ : Z ⟶ S)
    [LocallyOfFiniteType sZ] (f₁ : X ⟶ Y) [IsProper f₁] (f₂ : Y ⟶ Z) [IsProper f₂]
    (hf₁ : f₁ ≫ sY = sX) (hf₂ : f₂ ≫ sZ = sY) (r : ℕ) (α : FamilyOfCycles sX r) :
    properPushforwardFamily sY sZ f₂ hf₂ r (properPushforwardFamily sX sY f₁ hf₁ r α) =
      properPushforwardFamily sX sZ (f₁ ≫ f₂) (by rw [Category.assoc, hf₂, hf₁]) r α
```

**`Stacks.Chow.flatPullbackFamily_properPushforwardFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean, line 447](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Compatibilities.lean#L447). The attribute's comment: “part (7): proper pushforward commutes with flat pullback”.

> **Stacks Project, Tag 0H4P, part (7).** Proper pushforward of families of cycles on fibres
> commutes with flat pullback: for a proper morphism `f : X ⟶ Y` and a flat morphism `g : Y' ⟶ Y`
> of relative dimension `e` of schemes locally of finite type over `S`, with base changes
> `f' : X ×_Y Y' ⟶ Y'` and `g' : X ×_Y Y' ⟶ X`, one has `g^*(f_*α) = f'_*((g')^*α)` for every
> family `α` of `r`-cycles on the fibres of `X/S`.

```lean
theorem flatPullbackFamily_properPushforwardFamily (e : ℕ)
    (he : AlgebraicGeometry.RelativeDimension g e) (r : ℕ) (α : FamilyOfCycles sX r) :
    flatPullbackFamily sY sY' g hg e he r (properPushforwardFamily sX sY f hf r α) =
      properPushforwardFamily (pullback.fst f g ≫ sX) sY' (pullback.snd f g)
        (pullback_snd_comp_eq_fst_comp sX sY sY' f hf g hg) (r + e)
        (flatPullbackFamily sX (pullback.fst f g ≫ sX) (pullback.fst f g) rfl e
          (AlgebraicGeometry.RelativeDimension.of_isPullback (IsPullback.of_hasPullback f g).flip
            he) r α)
```

## Tag 0H4Q, an example

[Tag 0H4Q](https://stacks.math.columbia.edu/tag/0H4Q) in the Stacks Project.

**`Stacks.Chow.familyAssociatedToModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleFamily.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleFamily.lean#L161). The attribute's comment: “the associated family”.

> **Stacks 0H4Q.** The family `[F/X/S]_r` of `r`-cycles on the fibres of `f` attached to a
> quasi-coherent module `F` of finite type whose support on every fibre has dimension at most
> `r`: its member over `s` is the cycle `[F_s]_r` associated to the pullback of `F` to the fibre
> over `s`.

```lean
def familyAssociatedToModule (f : X ⟶ S) [LocallyOfFiniteType f] (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤
        (r : WithBot ℕ∞)) :
    FamilyOfCycles f r
```

**`Stacks.Chow.familyAssociatedToModule_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleFamily.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleFamily.lean#L175). The attribute's comment: “fibrewise formula”.

> **Stacks 0H4Q.** The member of `[F/X/S]_r` over a point `s` of the base is the cycle
> `[F_s]_r` associated to the pullback of `F` to the fibre over `s`.

```lean
theorem familyAssociatedToModule_apply (f : X ⟶ S) [LocallyOfFiniteType f] (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤
        (r : WithBot ℕ∞)) (s : S) :
    familyAssociatedToModule f F r hdim s =
      cycleAssociatedToCoherentSheaf (fieldChowSituation (S.residueField s))
        (f.fiberToSpecResidueField s) ((Scheme.Modules.pullback (f.fiberι s)).obj F) (r : ℤ)
        (fiberModule_schemeDeltaDimension_le f F r hdim s)
```

## Tag 0H4R, a lemma

[Tag 0H4R](https://stacks.math.columbia.edu/tag/0H4R) in the Stacks Project.

**`Stacks.Chow.supportDimension_le_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleBaseChange.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleBaseChange.lean#L126). The attribute's comment: “module\_base\_change, residue-field-isomorphism case: dimension bound”.

> **Stacks Project, Tag 0H4R.** The dimension bound on the fibrewise supports of a
> quasi-coherent module of finite type survives base change along a morphism that induces an
> isomorphism on every residue field: the support on the fibre over `t` is the inverse image of the
> support on the fibre over `g t` along an isomorphism of fibres.

```lean
theorem supportDimension_le_of_baseChange (f : X ⟶ S) [LocallyOfFiniteType f] (g : S' ⟶ S)
    (hres : ∀ t : S', IsIso (g.residueFieldMap t)) (F : X.Modules) [F.IsFiniteType] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤ (r : WithBot ℕ∞)) :
    ∀ t : S', topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback ((pullback.snd f g).fiberι t)).obj
        ((Scheme.Modules.pullback (pullback.fst f g)).obj F))) ≤ (r : WithBot ℕ∞)
```

**`Stacks.Chow.familyAssociatedToModule_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleBaseChange.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleBaseChange.lean#L148). The attribute's comment: “module\_base\_change, residue-field-isomorphism case”.

> **Stacks Project, Tag 0H4R.** Base change along a morphism `g` that induces an isomorphism on
> every residue field carries the family of cycles associated to a quasi-coherent module of finite
> type to the family associated to the base-changed module. Coefficientwise: the base change
> preserves the multiplicity of the module and the relative dimension of a point of the fibre, and
> the support of the base-changed module on a fibre over `t` is the inverse image of the support of
> the original one on the fibre over `g t`.

```lean
theorem familyAssociatedToModule_baseChange (f : X ⟶ S) [LocallyOfFiniteType f] (g : S' ⟶ S)
    (hres : ∀ t : S', IsIso (g.residueFieldMap t)) (F : X.Modules) [F.IsFiniteType]
    [F.IsQuasicoherent] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤ (r : WithBot ℕ∞)) :
    baseChangeFamilyOfResidueIso f g hres r (familyAssociatedToModule f F r hdim) =
      familyAssociatedToModule (pullback.snd f g)
        ((Scheme.Modules.pullback (pullback.fst f g)).obj F) r
        (supportDimension_le_of_baseChange f g hres F r hdim)
```

**`Stacks.Chow.supportDimension_le_of_flatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleFlatPullback.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleFlatPullback.lean#L93). The attribute's comment: “module\_flat\_pullback: dimension bound”.

> **Stacks Project, Tag 0H4R.** The fibrewise support dimension bound on a quasi-coherent
> module of finite type passes to its pullback along a flat morphism `j : U ⟶ X` of schemes over
> `S`, locally of finite type and of relative dimension `e`, with `r` replaced by `r + e`: on the
> fibre over `s` this is the support dimension bound of Stacks 02RE, part (2), for the induced
> morphism `U_s ⟶ X_s`, which is again flat of relative dimension `e`.

```lean
theorem supportDimension_le_of_flatPullback (f : X ⟶ S) [LocallyOfFiniteType f] (fU : U ⟶ S)
    [LocallyOfFiniteType fU] (j : U ⟶ X) [LocallyOfFiniteType j] [Flat j] (h : j ≫ f = fU)
    (e : ℕ) (he : AlgebraicGeometry.RelativeDimension j e) (F : X.Modules) [F.IsFiniteType]
    [F.IsQuasicoherent] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤
        (r : WithBot ℕ∞)) :
    ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (fU.fiberι s)).obj
        ((Scheme.Modules.pullback j).obj F))) ≤ ((r + e : ℕ) : WithBot ℕ∞)
```

**`Stacks.Chow.familyAssociatedToModule_flatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleFlatPullback.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleFlatPullback.lean#L137). The attribute's comment: “module\_flat\_pullback”.

> **Stacks Project, Tag 0H4R.** The flat pullback of the family `[F/X/S]_r` of cycles
> associated to a quasi-coherent module of finite type, along a flat morphism `j : U ⟶ X` of
> schemes over `S` which is locally of finite type and of relative dimension `e`, is the family
> `[j^*F/U/S]_{r+e}` associated to the pulled-back module.
>
> On the fibre over `s` the morphism `U_s ⟶ X_s` induced by `j` is flat, locally of finite type and
> of relative dimension `e`, so Stacks 02RE, part (2), identifies the flat pullback of the cycle
> `[F_s]_r` with the cycle of the pullback of `F_s`; that pullback is the restriction of `j^*F` to
> the fibre of `f_U`, the two orders of pulling `F` back being compared by the
> pullback-composition isomorphism.

```lean
theorem familyAssociatedToModule_flatPullback (f : X ⟶ S) [LocallyOfFiniteType f] (fU : U ⟶ S)
    [LocallyOfFiniteType fU] (j : U ⟶ X) [LocallyOfFiniteType j] [Flat j] (h : j ≫ f = fU)
    (e : ℕ) (he : AlgebraicGeometry.RelativeDimension j e) (F : X.Modules) [F.IsFiniteType]
    [F.IsQuasicoherent] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤
        (r : WithBot ℕ∞)) :
    flatPullbackFamily f fU j h e he r (familyAssociatedToModule f F r hdim) =
      familyAssociatedToModule fU ((Scheme.Modules.pullback j).obj F) (r + e)
        (supportDimension_le_of_flatPullback f fU j h e he F r hdim)
```

**`Stacks.Chow.supportDimension_le_of_baseChange_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleGeneralBaseChange.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleGeneralBaseChange.lean#L102). The attribute's comment: “module\_base\_change, arbitrary morphism of bases: dimension bound”.

> **Stacks Project, Tag 0H4R.** The fibrewise support dimension bound on a quasi-coherent
> module of finite type survives base change along an arbitrary morphism of bases: the fibre of
> `X ×_S S' ⟶ S'` over `t` is the base change of the fibre of `f` over `g t` along the residue
> field extension `κ(t)/κ(g t)`, the support of the pulled-back module on it is the inverse image
> of the support on the fibre over `g t`, and no point of the former has larger delta-dimension
> than its image.

```lean
theorem supportDimension_le_of_baseChange_general (f : X ⟶ S) [LocallyOfFiniteType f]
    (g : S' ⟶ S) (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤
        (r : WithBot ℕ∞)) :
    ∀ t : S', topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback ((pullback.snd f g).fiberι t)).obj
        ((Scheme.Modules.pullback (pullback.fst f g)).obj F))) ≤ (r : WithBot ℕ∞)
```

**`Stacks.Chow.familyAssociatedToModule_baseChange_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleGeneralBaseChange.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleGeneralBaseChange.lean#L138). The attribute's comment: “module\_base\_change, arbitrary morphism of bases”.

> **Stacks Project, Tag 0H4R.** Base change of the family `[F/X/S]_r` of cycles associated to a
> quasi-coherent module of finite type along an *arbitrary* morphism `g : S' ⟶ S` of bases is the
> family associated to the pulled-back module.
>
> The fibre of `X ×_S S' ⟶ S'` over a point `t` is the base change of the fibre of `f` over `g t`
> along the residue field extension `κ(t)/κ(g t)`. That extension is flat and the dimension shift
> of the associated base change of Chow situations vanishes, so Stacks 0FVI part (2) applies and
> identifies the base change of the cycle `[F_{g t}]_r` with the cycle of the base-changed module;
> transporting the result along the canonical isomorphism of fibres, which is an open immersion,
> changes neither multiplicities nor relative dimensions.

```lean
theorem familyAssociatedToModule_baseChange_general (f : X ⟶ S) [LocallyOfFiniteType f]
    (g : S' ⟶ S) (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤
        (r : WithBot ℕ∞)) :
    baseChangeFamily f g r (familyAssociatedToModule f F r hdim) =
      familyAssociatedToModule (pullback.snd f g)
        ((Scheme.Modules.pullback (pullback.fst f g)).obj F) r
        (supportDimension_le_of_baseChange_general f g F r hdim)
```

**`Stacks.Chow.supportDimension_le_of_openRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleRestriction.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleRestriction.lean#L187). The attribute's comment: “module\_restriction: dimension bound”.

> **Stacks Project, Tag 0H4R.** The dimension bound on the fibrewise supports of a
> quasi-coherent module of finite type survives restriction of both the source and the base to
> compatible open subschemes: the support on the fibre of `fU` over `t` is the inverse image of
> the support on the fibre of `f` over `i t` along an open immersion of fibres.

```lean
theorem supportDimension_le_of_openRestriction {X S U V : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (fU : U ⟶ V) [LocallyOfFiniteType fU] (j : U ⟶ X)
    [IsOpenImmersion j] (i : V ⟶ S) [IsOpenImmersion i] (h : j ≫ f = fU ≫ i) (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤ (r : WithBot ℕ∞)) :
    ∀ t : V, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (fU.fiberι t)).obj
        ((Scheme.Modules.pullback j).obj F))) ≤ (r : WithBot ℕ∞)
```

**`Stacks.Chow.familyAssociatedToModule_openRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleRestriction.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleRestriction.lean#L207). The attribute's comment: “module\_restriction”.

> **Stacks Project, Tag 0H4R.** The restriction to `U/V` of the family of cycles associated to
> a quasi-coherent module of finite type is the family associated to the module restricted to `U`.
> Coefficientwise: restriction preserves the multiplicity of the module and the relative dimension
> of a point of the fibre, and the support of the restricted module on a fibre of `fU` is the
> inverse image of the support of the original one.

```lean
theorem familyAssociatedToModule_openRestriction {X S U V : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (fU : U ⟶ V) [LocallyOfFiniteType fU] (j : U ⟶ X)
    [IsOpenImmersion j] (i : V ⟶ S) [IsOpenImmersion i] (h : j ≫ f = fU ≫ i) (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent] (r : ℕ)
    (hdim : ∀ s : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤ (r : WithBot ℕ∞)) :
    (restrictedFamily f fU j i h r (familyAssociatedToModule f F r hdim)).1 =
      familyAssociatedToModule fU ((Scheme.Modules.pullback j).obj F) r
        (supportDimension_le_of_openRestriction f fU j i h F r hdim)
```

## Tag 0H4S, an example

[Tag 0H4S](https://stacks.math.columbia.edu/tag/0H4S) in the Stacks Project.

**`Stacks.Chow.familyAssociatedToClosedSubscheme`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeFamily.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeFamily.lean#L113). The attribute's comment: “the associated family”.

> The family `[Z/X/S]_r` of `r`-cycles on the fibres of `f` attached to a
> closed subscheme `i : Z ⟶ X` whose fibres have dimension at most `r`: its member over `s` is the
> cycle `[Z_s]_r` of the inverse image of `Z` in the fibre over `s`.

```lean
def familyAssociatedToClosedSubscheme (f : X ⟶ S) [LocallyOfFiniteType f] {Z : Scheme.{u}}
    (i : Z ⟶ X) [IsClosedImmersion i] (r : ℕ) : FamilyOfCycles f r
```

**`Stacks.Chow.familyAssociatedToClosedSubscheme_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeFamily.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeFamily.lean#L121). The attribute's comment: “fibrewise formula”.

> The member of `[Z/X/S]_r` over a point `s` of the base is the cycle
> `[Z_s]_r` of the inverse image of `Z` in the fibre over `s`.

```lean
theorem familyAssociatedToClosedSubscheme_apply (f : X ⟶ S) [LocallyOfFiniteType f]
    {Z : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i] (r : ℕ) (s : S) :
    familyAssociatedToClosedSubscheme f i r s =
      cycleAssociatedToClosedSubscheme (fieldChowSituation (S.residueField s))
        (f.fiberToSpecResidueField s) (fiberClosedImmersion f i s) (r : ℤ)
```

## Tag 0H4T, a lemma

[Tag 0H4T](https://stacks.math.columbia.edu/tag/0H4T) in the Stacks Project.

**`Stacks.Chow.familyAssociatedToClosedSubscheme_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeBaseChange.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeBaseChange.lean#L100). The attribute's comment: “base change”.

> **Stacks Project, Tag 0H4T (base change).** The construction of Example 0H4S is compatible
> with base change: let `f : X ⟶ S` be locally of finite type, let `i : Z ⟶ X` be a closed
> subscheme with `dim(Z_s) ≤ r` for every `s ∈ S`, and let `g : S' ⟶ S` be an arbitrary morphism of
> schemes. Then the base change of the family `[Z/X/S]_r` along `g` is the family attached to the
> inverse image `Z ×_X (X ×_S S')` of `Z` in `X ×_S S'`.
>
> With `F = i_* 𝒪_Z` the family `[Z/X/S]_r` is `[F/X/S]_r` by Chow Homology, Lemma 02QY, read on
> each fibre, so this is the base-change clause of Lemma 0H4R applied to `F`, together with the
> identification of the inverse image of `F` with the direct image of the structure sheaf of the
> base change of `Z`.

```lean
theorem familyAssociatedToClosedSubscheme_baseChange (f : X ⟶ S) [LocallyOfFiniteType f]
    (g : S' ⟶ S) (i : Z ⟶ X) [IsClosedImmersion i] (r : ℕ)
    (hZ : ∀ s : S, topologicalKrullDim (pullback i (f.fiberι s) : Scheme.{u}) ≤
      (r : WithBot ℕ∞)) :
    baseChangeFamily f g r (familyAssociatedToClosedSubscheme f i r) =
      familyAssociatedToClosedSubscheme (pullback.snd f g)
        (pullback.snd i (pullback.fst f g)) r
```

**`Stacks.Chow.familyAssociatedToClosedSubscheme_flatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeFlatPullback.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeFlatPullback.lean#L79). The attribute's comment: “flat pullback”.

> The construction of Example 0H4S is compatible with flat pullback: let `f : X ⟶ S` be locally
> of finite type, let `i : Z ⟶ X` be a closed subscheme with `dim(Z_s) ≤ r` for every `s ∈ S`, and
> let `j : U ⟶ X` be flat, locally of finite type and of relative dimension `e`, a morphism of
> schemes over `S` through `j ≫ f = f_U`. Then the flat pullback of the family `[Z/X/S]_r` along `j`
> is the family `[Z ×_X U / U / S]_{r+e}` attached to the scheme-theoretic inverse image of `Z` in
> `U`.

```lean
theorem familyAssociatedToClosedSubscheme_flatPullback (f : X ⟶ S) [LocallyOfFiniteType f]
    (fU : U ⟶ S) [LocallyOfFiniteType fU] (j : U ⟶ X) [LocallyOfFiniteType j] [Flat j]
    (h : j ≫ f = fU) (e : ℕ) (he : AlgebraicGeometry.RelativeDimension j e) (i : Z ⟶ X)
    [IsClosedImmersion i] (r : ℕ)
    (hZ : ∀ s : S, topologicalKrullDim (pullback i (f.fiberι s) : Scheme.{u}) ≤
      (r : WithBot ℕ∞)) :
    flatPullbackFamily f fU j h e he r (familyAssociatedToClosedSubscheme f i r) =
      familyAssociatedToClosedSubscheme fU (pullback.snd i j) (r + e)
```

**`Stacks.Chow.familyAssociatedToClosedSubscheme_openRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeRestriction.lean, line 347](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeRestriction.lean#L347). The attribute's comment: “restriction”.

> **Stacks Project, Tag 0H4T (restriction).** The construction of Example 0H4S is compatible
> with restriction: let `f : X ⟶ S` be locally of finite type, let `i : Z ⟶ X` be a closed
> subscheme with `dim(Z_s) ≤ r` for every `s ∈ S`, and let `j : U ⟶ X` and `i' : V ⟶ S` be open
> subschemes with `fU : U ⟶ V` making the square commute. Then the restriction of the family
> `[Z/X/S]_r` to the fibres of `U/V` is the family `[Z ∩ U / U / V]_r` attached to the closed
> subscheme `Z ∩ U = Z ×_X U` of `U`.
>
> Coefficientwise: restriction preserves the multiplicity of a component of a fibre of `Z` and
> the relative dimension of a point of a fibre, and a component of `Z_{i' t}` contributes to the
> restricted family exactly when it meets `U_t`. The comparison over a single point `t` of `V`
> needs the dimension bound only over `i' t`; that is
> `Stacks.Chow.familyAssociatedToClosedSubscheme_openRestriction_apply`.

```lean
theorem familyAssociatedToClosedSubscheme_openRestriction (f : X ⟶ S) [LocallyOfFiniteType f]
    (fU : U ⟶ V) [LocallyOfFiniteType fU] (j : U ⟶ X) [IsOpenImmersion j] (i' : V ⟶ S)
    [IsOpenImmersion i'] (h : j ≫ f = fU ≫ i') (i : Z ⟶ X) [IsClosedImmersion i] (r : ℕ)
    (hdim : ∀ s : S,
      topologicalKrullDim ↥(pullback i (f.fiberι s)) ≤ (r : WithBot ℕ∞)) :
    (restrictedFamily f fU j i' h r (familyAssociatedToClosedSubscheme f i r)).1 =
      familyAssociatedToClosedSubscheme fU (pullback.fst j i) r
```

## Tag 0H4U, a remark

[Tag 0H4U](https://stacks.math.columbia.edu/tag/0H4U) in the Stacks Project.

**`Stacks.Chow.supportOfFamily`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Basic.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Basic.lean#L90). The attribute's comment: “support\_of\_a\_family\_of\_cycles”.

> The support of a family of cycles on the fibres of `f`: the union in `X` of the images of the
> supports of its members.

```lean
def supportOfFamily {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] {r : ℕ}
    (α : FamilyOfCycles f r) : Set X
```

**`Stacks.Chow.exists_family_support_not_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NonclosedSupport.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/NonclosedSupport.lean#L77).

> **Stacks Project, Tag 0H4U.** The support of a family of cycles on fibres need not be
> closed in the total space.

```lean
theorem exists_family_support_not_closed :
    ∃ (X S : Scheme.{u}) (f : X ⟶ S) (h : LocallyOfFiniteType f),
      letI : LocallyOfFiniteType f := h
      ∃ (r : ℕ) (α : FamilyOfCycles f r), ¬ IsClosed (supportOfFamily f α)
```

## Tag 0H4V, a lemma

[Tag 0H4V](https://stacks.math.columbia.edu/tag/0H4V) in the Stacks Project.

**`Stacks.Chow.supportOfFamily_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeSupport.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChangeSupport.lean#L204). The attribute's comment: “base change”.

> **Stacks Project, Tag 0H4V, the base-change clause.** Taking the support of a family of
> cycles on the fibres is compatible with base change: the support of `g^*α` is the inverse image
> of the support of `α` along the projection `X ×_S S' ⟶ X`.

```lean
theorem supportOfFamily_baseChangeFamily {X S S' : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (g : S' ⟶ S) (r : ℕ) (α : FamilyOfCycles f r) :
    supportOfFamily (pullback.snd f g) (baseChangeFamily f g r α) =
      pullback.fst f g ⁻¹' supportOfFamily f α
```

**`Stacks.Chow.supportOfFamily_flatPullbackFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatPullbackSupport.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/FlatPullbackSupport.lean#L160). The attribute's comment: “flat pullback”.

> **Stacks Project, Tag 0H4V, the flat pullback clause.** Taking the support of a family of
> cycles on the fibres is compatible with flat pullback: the support of `j^*α` is the inverse
> image of the support of `α` along `j`.

```lean
theorem supportOfFamily_flatPullbackFamily {X S U : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (fU : U ⟶ S) (j : U ⟶ X) [LocallyOfFiniteType j] [Flat j]
    (hj : j ≫ f = fU) (e : ℕ) (he : AlgebraicGeometry.RelativeDimension j e) (r : ℕ)
    (α : FamilyOfCycles f r) :
    letI : LocallyOfFiniteType fU := hj ▸ (inferInstance : LocallyOfFiniteType (j ≫ f))
    supportOfFamily fU (flatPullbackFamily f fU j hj e he r α) = j ⁻¹' supportOfFamily f α
```

**`Stacks.Chow.image_supportOfFamily_restrictedFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/RestrictionSupport.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/RestrictionSupport.lean#L47). The attribute's comment: “support\_restriction”.

> The support of a restricted family of cycles, mapped back into the original total space, is
> the intersection of the original support with the open subscheme.

```lean
theorem image_supportOfFamily_restrictedFamily
    {X S U V : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] (fU : U ⟶ V)
    (j : U ⟶ X) [IsOpenImmersion j] (i : V ⟶ S) [IsOpenImmersion i]
    (h : j ≫ f = fU ≫ i) (r : ℕ) (α : FamilyOfCycles f r) :
    letI : LocallyOfFiniteType fU := by
      let : LocallyOfFiniteType (fU ≫ i) := h ▸ inferInstance
      exact locallyOfFiniteType_of_comp fU i
    j '' (supportOfFamily fU (restrictedFamily f fU j i h r α).1) =
      Set.range j ∩ supportOfFamily f α
```

## Tag 0H4W, a lemma

[Tag 0H4W](https://stacks.math.columbia.edu/tag/0H4W) in the Stacks Project.

**`AlgebraicGeometry.exists_preimage_preserving_residueField_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/TrdegLift.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/TrdegLift.lean#L98). The attribute's comment: “part (1)”. References: SGA 2 XIV (2.1.1), “special case”.

> Let `f : X ⟶ S` be locally of finite type, let
> `g : S' ⟶ S` be surjective and let `f' : X' ⟶ S'` be the base change of `f`. A point `x : X`
> whose residue field has transcendence degree `r` over the residue field of `f x` has a preimage
> in `X'` whose residue field has transcendence degree `r` over the residue field of its image in
> `S'`.

```lean
public theorem exists_preimage_preserving_residueField_trdeg {p : X' ⟶ X} {f' : X' ⟶ S'}
    {f : X ⟶ S} {g : S' ⟶ S} (hpb : IsPullback p f' f g) [LocallyOfFiniteType f] [Surjective g]
    (r : ℕ) (x : X)
    (hr : letI := (f.residueFieldMap x).hom.toAlgebra
      Algebra.trdeg ↥(S.residueField (f x)) ↥(X.residueField x) = r) :
    ∃ (x' : X') (_hx : p x' = x),
      letI := (f'.residueFieldMap x').hom.toAlgebra
      Algebra.trdeg ↥(S'.residueField (f' x')) ↥(X'.residueField x') = r
```

**`AlgebraicGeometry.exists_common_preimage_preserving_residueField_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/TrdegLift.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FibreDimensionBaseChange/TrdegLift.lean#L260). The attribute's comment: “part (2)”.

> In the situation of `AlgebraicGeometry.exists_preimage_preserving_residueField_trdeg`, let
> `S''` be the self-intersection `S' ×_S S'` of the base change, with projections `q₁` and `q₂`,
> and let `f'' : X'' ⟶ S''` be the base change of `f` to `S''`, with projections `p₁` and `p₂` to
> `X'` exhibiting `X''` as `X' ×_X X'`. Two preimages `x₁'` and `x₂'` of `x` of the same relative
> transcendence degree `r` are the two images of a point of `X''` whose residue field again has
> transcendence degree `r` over the residue field of its image in `S''`.

```lean
public theorem exists_common_preimage_preserving_residueField_trdeg {p : X' ⟶ X} {f' : X' ⟶ S'}
    {f : X ⟶ S} {g : S' ⟶ S} {q₁ q₂ : S'' ⟶ S'} {p₁ p₂ : X'' ⟶ X'} {f'' : X'' ⟶ S''}
    (hX' : IsPullback p f' f g) (hS'' : IsPullback q₁ q₂ g g)
    (hX''₁ : IsPullback p₁ f'' f' q₁) (hX''₂ : IsPullback p₂ f'' f' q₂)
    (hXX : IsPullback p₁ p₂ p p) [LocallyOfFiniteType f] (r : ℕ) (x : X) (x₁' x₂' : X')
    (hr : letI := (f.residueFieldMap x).hom.toAlgebra
      Algebra.trdeg ↥(S.residueField (f x)) ↥(X.residueField x) = r)
    (hx₁ : p x₁' = x) (hx₂ : p x₂' = x)
    (hr₁ : letI := (f'.residueFieldMap x₁').hom.toAlgebra
      Algebra.trdeg ↥(S'.residueField (f' x₁')) ↥(X'.residueField x₁') = r)
    (hr₂ : letI := (f'.residueFieldMap x₂').hom.toAlgebra
      Algebra.trdeg ↥(S'.residueField (f' x₂')) ↥(X'.residueField x₂') = r) :
    ∃ x'' : X'', p₁ x'' = x₁' ∧ p₂ x'' = x₂' ∧
      (letI := (f''.residueFieldMap x'').hom.toAlgebra
       Algebra.trdeg ↥(S''.residueField (f'' x'')) ↥(X''.residueField x'') = r)
```

## Tag 0H4X, a lemma

[Tag 0H4X](https://stacks.math.columbia.edu/tag/0H4X) in the Stacks Project.

**`Stacks.Chow.baseChangeFamily_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChange.lean, line 729](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChange.lean#L729). The attribute's comment: “injectivity of base change on families of cycles on fibres”.

> Base change of families of `r`-cycles on the fibres of `X / S` along a surjective morphism
> `g : S' ⟶ S` is injective: if `g^*α₁ = g^*α₂` then `α₁ = α₂`.

```lean
theorem baseChangeFamily_injective (f : X ⟶ S) [LocallyOfFiniteType f] (g : S' ⟶ S)
    [Surjective g] (r : ℕ) (α₁ α₂ : FamilyOfCycles f r)
    (h : baseChangeFamily f g r α₁ = baseChangeFamily f g r α₂) :
    α₁ = α₂
```

**`Stacks.Chow.existsUnique_familyOfCycles_baseChangeFamily_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Descent.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Descent.lean#L485). The attribute's comment: “descent of a family of cycles on fibres along a morphism with separable residue field extensions”.

> **Stacks Project, Tag 0H4X (2).** Let `f : X ⟶ S` be locally of finite type, let `r ≥ 0`, let
> `g : S' ⟶ S` be a morphism such that every point of `S` has a preimage in `S'` whose residue
> field extension is separable, and let `X' = X ×_S S'`. Given a family `α'` of `r`-cycles on the
> fibres of `X' / S'` whose two pullbacks to the double overlap `S'' = S' ×_S S'` agree as families
> of `r`-cycles on the fibres of `S'' ×_S X / S''`, there is a unique family `α` of `r`-cycles on
> the fibres of `X / S` with `g^*α = α'`.

```lean
theorem existsUnique_familyOfCycles_baseChangeFamily_eq (f : X ⟶ S) [LocallyOfFiniteType f]
    (g : S' ⟶ S) (hg : HasSeparableResidueFieldPoints g) (r : ℕ)
    (α' : FamilyOfCycles (pullback.snd f g) r)
    (hα' : ∀ (t : (pullback g g : Scheme.{u}))
      (x : (pullback.snd (pullback.snd f g) (pullback.fst g g)).fiber t),
      (baseChangeFamily (pullback.snd f g) (pullback.fst g g) r α' t :
          AlgebraicCycle ((pullback.snd (pullback.snd f g) (pullback.fst g g)).fiber t) ℤ) x =
        (baseChangeFamily (pullback.snd f g) (pullback.snd g g) r α' t :
            AlgebraicCycle ((pullback.snd (pullback.snd f g) (pullback.snd g g)).fiber t) ℤ)
          ((overlapFiberComparison f g t).hom x)) :
    ∃! α : FamilyOfCycles f r, baseChangeFamily f g r α = α'
```

## Tag 0H4Y, a lemma

[Tag 0H4Y](https://stacks.math.columbia.edu/tag/0H4Y) in the Stacks Project.

**`Stacks.Chow.baseChangeFamilyOfCyclesAddEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChange.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChange.lean#L291). The attribute's comment: “the additive equivalence”.

> Base change along a morphism that is bijective on points and
> induces isomorphisms of residue fields identifies the groups of families of cycles on the
> fibres.

```lean
def baseChangeFamilyOfCyclesAddEquiv
    {X S S' : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (g : S' ⟶ S) (hg : Function.Bijective g)
    (hres : ∀ t : S', IsIso (g.residueFieldMap t)) (r : ℕ) :
    FamilyOfCycles f r ≃+ FamilyOfCycles (pullback.snd f g) r
```

**`Stacks.Chow.baseChangeFamilyOfCyclesAddEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChange.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/BaseChange.lean#L302). The attribute's comment: “the coefficient formula”.

> The base-changed family has, on each fibre, the coefficients
> of the original family transported along the canonical map of fibres.

```lean
theorem baseChangeFamilyOfCyclesAddEquiv_apply
    {X S S' : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (g : S' ⟶ S) (hg : Function.Bijective g)
    (hres : ∀ t : S', IsIso (g.residueFieldMap t)) (r : ℕ)
    (α : FamilyOfCycles f r) (t : S') (x : (pullback.snd f g).fiber t) :
    ((baseChangeFamilyOfCyclesAddEquiv f g hg hres r α) t :
      AlgebraicCycle ((pullback.snd f g).fiber t) ℤ) x =
        (α (g t) : AlgebraicCycle (f.fiber (g t)) ℤ)
          (restrictedFiberMap f (pullback.snd f g) (pullback.fst f g) g
            pullback.condition t x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.5, Tag 0H4N](https://stacks.math.columbia.edu/tag/0H4N)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

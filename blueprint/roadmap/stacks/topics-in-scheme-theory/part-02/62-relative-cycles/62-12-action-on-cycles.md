---
declaration: section
origin: cited
lean: Stacks.Chow.cap_add_left, Stacks.Chow.cap_add_right, Stacks.Chow.cycleGroupRestrict_cap, Stacks.Chow.cap_flatPullback, Stacks.Chow.cap_baseChange, Stacks.Chow.cap_familyAssociatedToModule, Stacks.Chow.cap_familyAssociatedToClosedSubscheme, Stacks.Chow.properPushforward_cap_baseChangeFamily
statement: formalized
proof: formalized
---

# 62.12 Action on cycles

Section 62.12 of the Stacks Project, [Tag 0H65](https://stacks.math.columbia.edu/tag/0H65). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H66, a lemma

[Tag 0H66](https://stacks.math.columbia.edu/tag/0H66) in the Stacks Project.

**`Stacks.Chow.cap_add_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionOnCycles.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionOnCycles.lean#L450). The attribute's comment: “additivity in the family of fibre cycles”.

> The action is additive in the family of fibre cycles.

```lean
theorem cap_add_left (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (s : Y ⟶ C.S) [LocallyOfFiniteType s]
    (f : X ⟶ Y) [LocallyOfFiniteType f] {r : ℕ}
    (α₁ α₂ : FamilyOfCycles f r)
    {e : ℤ} (β : CycleGroup C s e) :
    letI : LocallyOfFiniteType (f ≫ s) := inferInstance
    cap C s f (α₁ + α₂) β = cap C s f α₁ β + cap C s f α₂ β
```

**`Stacks.Chow.cap_add_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionOnCycles.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionOnCycles.lean#L462). The attribute's comment: “additivity in the cycle on the base”.

> The action is additive in the cycle on the base.

```lean
theorem cap_add_right (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (s : Y ⟶ C.S) [LocallyOfFiniteType s]
    (f : X ⟶ Y) [LocallyOfFiniteType f] {r : ℕ}
    (α : FamilyOfCycles f r)
    {e : ℤ} (β₁ β₂ : CycleGroup C s e) :
    letI : LocallyOfFiniteType (f ≫ s) := inferInstance
    cap C s f α (β₁ + β₂) = cap C s f α β₁ + cap C s f α β₂
```

## Tag 0H67, a lemma

[Tag 0H67](https://stacks.math.columbia.edu/tag/0H67) in the Stacks Project.

**`Stacks.Chow.cycleGroupRestrict_cap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/RestrictionAction.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/RestrictionAction.lean#L98).

> **Stacks Project, Tag 0H67.** If `U ⊆ X` and `V ⊆ Y` are open and `f(U) ⊆ V`, then the
> restriction to `U` of the cycle `α ∩ β` is `α|_U ∩ β|_V`, the cycle obtained by letting the
> restriction of the family `α` to the fibres of `U/V` act on the restriction of `β` to `V`.

```lean
theorem cycleGroupRestrict_cap (C : ChowSituation.{u}) {X Y U V : Scheme.{u}}
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (sV : V ⟶ C.S) [LocallyOfFiniteType sV]
    (f : X ⟶ Y) [LocallyOfFiniteType f] (fU : U ⟶ V)
    (j : U ⟶ X) [IsOpenImmersion j] (i : V ⟶ Y) [IsOpenImmersion i]
    (hi : i ≫ sY = sV) (h : j ≫ f = fU ≫ i) (r : ℕ) (e : ℤ)
    (α : FamilyOfCycles f r) (β : CycleGroup C sY e) :
    letI : LocallyOfFiniteType fU := by
      let : LocallyOfFiniteType (fU ≫ i) := h ▸ inferInstance
      exact locallyOfFiniteType_of_comp fU i
    letI : LocallyOfFiniteType (f ≫ sY) := inferInstance
    letI : LocallyOfFiniteType (fU ≫ sV) := inferInstance
    cycleGroupRestrict C (f ≫ sY) (fU ≫ sV) j
        (by rw [← Category.assoc, h, Category.assoc, hi]) ((r : ℤ) + e)
        (cap C sY f α β) =
      cap C sV fU (restrictedFamily f fU j i h r α).1
        (cycleGroupRestrict C sY sV i hi e β)
```

## Tag 0H68, a lemma

[Tag 0H68](https://stacks.math.columbia.edu/tag/0H68) in the Stacks Project.

**`Stacks.Chow.cap_flatPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionBaseChange.lean, line 694](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionBaseChange.lean#L694). The attribute's comment: “compatibility with flat pullback”.

> **Stacks Project, Tag 0H68.** Forming `α ∩ β` is compatible with flat pullback: if
> `g : Y' ⟶ Y` is flat, locally of finite type and of relative dimension `c`, if `α'` is the base
> change of the family `α` along `g` and `β'` the flat pullback of `β`, then the cycle `α' ∩ β'` on
> `X ×_Y Y'` is the flat pullback of `α ∩ β` along `X ×_Y Y' ⟶ X`.

```lean
theorem cap_flatPullback (C : ChowSituation.{u}) {X Y Y' : Scheme.{u}}
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y) [LocallyOfFiniteType f]
    (g : Y' ⟶ Y) [LocallyOfFiniteType g] [Flat g] (c : ℕ)
    (hg : AlgebraicGeometry.RelativeDimension g c) (r : ℕ) (e : ℤ)
    (α : FamilyOfCycles f r) (β : CycleGroup C sY e) :
    letI : LocallyOfFiniteType (f ≫ sY) := inferInstance
    letI : LocallyOfFiniteType (g ≫ sY) := inferInstance
    letI : LocallyOfFiniteType (pullback.snd f g ≫ g ≫ sY) := inferInstance
    (cap C (g ≫ sY) (pullback.snd f g) (baseChangeFamily f g r α)
          (flatPullback C (g ≫ sY) sY g rfl c hg e β) :
        AlgebraicCycle (pullback f g : Scheme.{u}) ℤ) =
      (flatPullback C (pullback.snd f g ≫ g ≫ sY) (f ≫ sY) (pullback.fst f g)
          (by rw [← Category.assoc, pullback.condition, Category.assoc]) c
          (AlgebraicGeometry.RelativeDimension.of_isPullback
            ((IsPullback.of_hasPullback f g).flip) hg) ((r : ℤ) + e) (cap C sY f α β) :
        AlgebraicCycle (pullback f g : Scheme.{u}) ℤ)
```

**`Stacks.Chow.cap_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionBaseChange.lean, line 739](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionBaseChange.lean#L739). The attribute's comment: “compatibility with flat base change”.

> **Stacks Project, Tag 0H68.** Forming `α ∩ β` is compatible with flat base change: in the
> situation of Tag 0FVG, with `α'` the base change of the family `α` along `Y' = Y ×_S S' ⟶ Y` and
> `β' = g^*β ∈ Z_{e + c}(Y')` the base change of `β`, the cycle `α' ∩ β'` is the base change of
> `α ∩ β`, read along the canonical isomorphism of `X ×_Y Y'` with `X' = X ×_S S'`.

```lean
theorem cap_baseChange (B : FlatBaseChangeSituation.{u}) {X Y : Scheme.{u}}
    (sY : Y ⟶ B.base.S) [LocallyOfFiniteType sY] (f : X ⟶ Y) [LocallyOfFiniteType f]
    (r : ℕ) (e : ℤ) (α : FamilyOfCycles f r) (β : CycleGroup B.base sY e)
    (w : (pullback f (pullback.fst sY B.g) : Scheme.{u})) :
    letI : LocallyOfFiniteType (f ≫ sY) := inferInstance
    letI : LocallyOfFiniteType (pullback.snd sY B.g) := inferInstance
    letI : LocallyOfFiniteType (pullback.snd f (pullback.fst sY B.g)) := inferInstance
    (cap B.baseChange (pullback.snd sY B.g) (pullback.snd f (pullback.fst sY B.g))
          (baseChangeFamily f (pullback.fst sY B.g) r α)
          (baseChangeCyclePullback B sY e β) :
        AlgebraicCycle (pullback f (pullback.fst sY B.g) : Scheme.{u}) ℤ) w =
      (baseChangeCyclePullback B (f ≫ sY) ((r : ℤ) + e) (cap B.base sY f α β) :
        AlgebraicCycle (pullback (f ≫ sY) B.g : Scheme.{u}) ℤ)
        ((pullbackRightPullbackFstIso sY B.g f).hom.base w)
```

## Tag 0H69, a lemma

[Tag 0H69](https://stacks.math.columbia.edu/tag/0H69) in the Stacks Project.

**`Stacks.Chow.cap_familyAssociatedToModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CapTensorPullback.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CapTensorPullback.lean#L137).

> **Stacks Project, Tag 0H69.** Let `(S, δ)` and `f : X ⟶ Y` be as in Section 0H65, let `F` be
> a coherent `𝒪_X`-module whose support on every fibre of `f` has dimension at most `r` and let `G`
> be a coherent `𝒪_Y`-module whose support has delta-dimension at most `e`. Set `α = [F/X/Y]_r` and
> `β = [G]_e`. If `F` is flat over `Y` then `α ∩ β = [F ⊗_{𝒪_X} f^* G]_{r + e}`.

```lean
theorem cap_familyAssociatedToModule (r : ℕ) (e : ℤ) (F : X.Modules) [F.IsCoherent]
    (hdim : ∀ y : Y, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι y)).obj F)) ≤ (r : WithBot ℕ∞))
    (hflat : IsFlatOver f.toLRSHom.toShHom F) (G : Y.Modules) [G.IsCoherent]
    (hGe : schemeDeltaDimension C ((reducedSupport G).subschemeι ≫ sY) ≤ (e : EInt)) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian (f ≫ sY)
    letI : F.IsFiniteType := isFiniteType_of_isCoherent F
    letI : F.IsQuasicoherent := isQuasicoherent_of_isCoherent F
    cap C sY f (familyAssociatedToModule f F r hdim)
        (cycleAssociatedToCoherentSheaf C sY G e hGe) =
      cycleAssociatedToCoherentSheaf C (f ≫ sY) (tensorPullback f F G) ((r : ℤ) + e)
        (schemeDeltaDimension_tensorPullback_le C sY f r e F hdim G hGe)
```

## Tag 0H6A, a lemma

[Tag 0H6A](https://stacks.math.columbia.edu/tag/0H6A) in the Stacks Project.

**`Stacks.Chow.cap_familyAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CapClosedSubscheme.lean, line 271](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CapClosedSubscheme.lean#L271).

> **Stacks Project, Tag 0H6A.** Let `(S, δ)` and `f : X ⟶ Y` be as in Section 0H65. Let
> `Z ⊆ X` be a closed subscheme of relative dimension at most `r` over `Y`, so that the fibres
> `Z_y = Z ×_X X_y` have dimension at most `r`, and set `α = [Z/X/Y]_r` (Example 0H4S). Let
> `W ⊆ Y` be a closed subscheme of `δ`-dimension at most `e` and set `β = [W]_e` (Chow Homology,
> Definition 02QU). If `Z` is flat over `Y`, then `α ∩ β = [Z ×_Y W]_{r + e}`.
>
> The proof is the special case `F = 𝒪_Z`, `G = 𝒪_W` of Stacks 0H69: the family `α` is the family
> of cycles attached to the coherent module `i_* 𝒪_Z` of Example 0H4Q, by
> `Stacks.Chow.familyAssociatedToModule_pushforwardStructureSheaf`; the cycle of a closed
> subscheme is the cycle of its structure sheaf (Stacks 02QY) on both sides; flatness of `Z` over
> `Y` is flatness of `i_* 𝒪_Z` over `Y` because a closed immersion is affine; and the projection
> formula together with base change identifies `i_* 𝒪_Z ⊗_{𝒪_X} f^* j_* 𝒪_W` with the structure
> sheaf of `Z ×_Y W` pushed forward to `X`.

```lean
theorem cap_familyAssociatedToClosedSubscheme (C : ChowSituation.{u}) {X Y Z W : Scheme.{u}}
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y) [LocallyOfFiniteType f] (r : ℕ) (e : ℤ)
    (i : Z ⟶ X) [IsClosedImmersion i] [Flat (i ≫ f)]
    (hZ : ∀ y : Y, topologicalKrullDim (pullback i (f.fiberι y) : Scheme.{u}) ≤ (r : WithBot ℕ∞))
    (j : W ⟶ Y) [IsClosedImmersion j]
    (hWe : schemeDeltaDimension C (j ≫ sY) ≤ (e : EInt)) :
    cap C sY f (familyAssociatedToClosedSubscheme f i r)
        (cycleAssociatedToClosedSubscheme C sY j e) =
      cycleAssociatedToClosedSubscheme C (f ≫ sY) (pullback.fst (i ≫ f) j ≫ i)
        ((r : ℤ) + e)
```

## Tag 0H6B, a lemma

[Tag 0H6B](https://stacks.math.columbia.edu/tag/0H6B) in the Stacks Project.

**`Stacks.Chow.properPushforward_cap_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionPushPull.lean, line 678](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ActionPushPull.lean#L678).

> **Stacks Project, Tag 0H6B.** Let `(S, δ)` be a Chow situation, let
> ```
> X' --f--> X
> |         |
> v         v
> Y' --g--> Y
> ```
> be a cartesian square of schemes locally of finite type over `S` with `g` proper, realized by
> the fibre product `X' = X ×_Y Y'` with `f = pullback.fst`, let `r ≥ 0` and `e ∈ ℤ`, let `α` be a
> family of `r`-cycles on the fibres of `X/Y` and let `β' ∈ Z_e(Y')`. Then
>
> `f_*(g^*α ∩ β') = α ∩ g_*β'`   in   `Z_{r + e}(X)`,
>
> where `∩` is the action `Stacks.Chow.cap` and `g^*α` is the base change
> `Stacks.Chow.baseChangeFamily` of the family.

```lean
theorem properPushforward_cap_baseChangeFamily (C : ChowSituation.{u}) {X Y Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY'] (p : X ⟶ Y) [LocallyOfFiniteType p]
    (g : Y' ⟶ Y) [IsProper g] (hp : p ≫ sY = sX) (hg : g ≫ sY = sY') (r : ℕ) (e : ℤ)
    (α : FamilyOfCycles p r) (β' : CycleGroup C sY' e) :
    properPushforward C (pullback.snd p g ≫ sY') sX (pullback.fst p g)
        (pullbackFst_comp_eq_of_base g hp hg) ((r : ℤ) + e)
        (cap C sY' (pullback.snd p g) (baseChangeFamily p g r α) β') =
      hp ▸ cap C sY p α (properPushforward C sY' sY g hg e β')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.12, Tag 0H65](https://stacks.math.columbia.edu/tag/0H65)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

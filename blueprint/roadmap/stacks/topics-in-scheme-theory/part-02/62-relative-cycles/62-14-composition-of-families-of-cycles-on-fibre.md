---
declaration: section
origin: cited
lean: Stacks.Chow.compFamily_add_left, Stacks.Chow.compFamily_add_right, Stacks.Chow.restrictedFamily_compFamily, Stacks.Chow.compFamily_baseChangeFamily, Stacks.Chow.compFamily_familyAssociatedToModule, Stacks.Chow.compFamily_familyAssociatedToClosedSubscheme, Stacks.Chow.properPushforwardFamily_compFamily_baseChangeFamily, Stacks.Chow.cap_compFamily
statement: formalized
proof: formalized
---

# 62.14 Composition of families of cycles on fibres

Section 62.14 of the Stacks Project, [Tag 0H6H](https://stacks.math.columbia.edu/tag/0H6H). 7 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H6I, a lemma

[Tag 0H6I](https://stacks.math.columbia.edu/tag/0H6I) in the Stacks Project.

**`Stacks.Chow.compFamily_add_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Composition.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Composition.lean#L260). The attribute's comment: “additivity in the family on X/Y”.

> **Stacks Project, Tag 0H6I.** The composition of families of cycles on fibres is additive in
> the family on `X/Y`: `(α₁ + α₂) ∘ β = α₁ ∘ β + α₂ ∘ β`.

```lean
theorem compFamily_add_left (f : X ⟶ Y) [LocallyOfFiniteType f] (g : Y ⟶ S)
    [LocallyOfFiniteType g] (r e : ℕ) (α₁ α₂ : FamilyOfCycles f r) (β : FamilyOfCycles g e) :
    compFamily f g r e (α₁ + α₂) β = compFamily f g r e α₁ β + compFamily f g r e α₂ β
```

**`Stacks.Chow.compFamily_add_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Composition.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Composition.lean#L272). The attribute's comment: “additivity in the family on Y/S”.

> **Stacks Project, Tag 0H6I.** The composition of families of cycles on fibres is additive in
> the family on `Y/S`: `α ∘ (β₁ + β₂) = α ∘ β₁ + α ∘ β₂`.

```lean
theorem compFamily_add_right (f : X ⟶ Y) [LocallyOfFiniteType f] (g : Y ⟶ S)
    [LocallyOfFiniteType g] (r e : ℕ) (α : FamilyOfCycles f r) (β₁ β₂ : FamilyOfCycles g e) :
    compFamily f g r e α (β₁ + β₂) = compFamily f g r e α β₁ + compFamily f g r e α β₂
```

## Tag 0H6J, a lemma

[Tag 0H6J](https://stacks.math.columbia.edu/tag/0H6J) in the Stacks Project.

**`Stacks.Chow.restrictedFamily_compFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Composition.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Composition.lean#L295).

> **Stacks Project, Tag 0H6J.** If `U ⊆ X`, `V ⊆ Y` and `W ⊆ S` are open with `f(U) ⊆ V` and
> `g(V) ⊆ W`, then the restriction of the composition `α ∘ β` to `U` is the composition of the
> restriction of `α` to the fibres of `U/V` with the restriction of `β` to the fibres of `V/W`.
> The source's statement is the case `W = S`.

```lean
theorem restrictedFamily_compFamily {U V W : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f]
    (g : Y ⟶ S) [LocallyOfFiniteType g] (fU : U ⟶ V) (gV : V ⟶ W) (j : U ⟶ X)
    [IsOpenImmersion j] (i : V ⟶ Y) [IsOpenImmersion i] (k : W ⟶ S) [IsOpenImmersion k]
    (hU : j ≫ f = fU ≫ i) (hV : i ≫ g = gV ≫ k) (r e : ℕ) (α : FamilyOfCycles f r)
    (β : FamilyOfCycles g e) :
    letI : LocallyOfFiniteType fU := by
      let : LocallyOfFiniteType (fU ≫ i) := hU ▸ inferInstance
      exact locallyOfFiniteType_of_comp fU i
    letI : LocallyOfFiniteType gV := by
      let : LocallyOfFiniteType (gV ≫ k) := hV ▸ inferInstance
      exact locallyOfFiniteType_of_comp gV k
    (restrictedFamily (f ≫ g) (fU ≫ gV) j k (comp_restrictionSquare hU hV) (r + e)
        (compFamily f g r e α β)).1 =
      compFamily fU gV r e (restrictedFamily f fU j i hU r α).1
        (restrictedFamily g gV i k hV e β).1
```

## Tag 0H6K, a lemma

[Tag 0H6K](https://stacks.math.columbia.edu/tag/0H6K) in the Stacks Project.

**`Stacks.Chow.compFamily_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CompositionBaseChange.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CompositionBaseChange.lean#L353).

> The formation of the composition `α ∘ β` of a family of `r`-cycles on the fibres of `X/Y` with
> a family of `e`-cycles on the fibres of `Y/S` is compatible with an arbitrary base change
> `h : S' ⟶ S`: the composition of the base change of `α` along `Y ×_S S' ⟶ Y` with the base change
> of `β` along `h` is the base change of `α ∘ β` along `h`, read on the fibre over a point `t` of
> `S'` through the canonical identification of `(X ×_Y (Y ×_S S'))_t` with `(X ×_S S')_t`.

```lean
theorem compFamily_baseChangeFamily (r e : ℕ) (α : FamilyOfCycles f r)
    (β : FamilyOfCycles g e) :
    compFamily (pullback.snd f (pullback.fst g h)) (pullback.snd g h) r e
        (baseChangeFamily f (pullback.fst g h) r α) (baseChangeFamily g h e β) t =
      fiberCycleRestrict (pullback.snd (f ≫ g) h)
        (pullback.snd f (pullback.fst g h) ≫ pullback.snd g h)
        (pullbackRightPullbackFstIso g h f).hom
        (pullbackRightPullbackFstIso_hom_snd g h f) t (r + e)
        (baseChangeFamily (f ≫ g) h (r + e) (compFamily f g r e α β) t)
```

## Tag 0H6L, a lemma

[Tag 0H6L](https://stacks.math.columbia.edu/tag/0H6L) in the Stacks Project.

**`Stacks.Chow.compFamily_familyAssociatedToModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleComposition.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ModuleComposition.lean#L419).

> **Stacks Project, Tag 0H6L.** Let `f : X ⟶ Y` and `g : Y ⟶ S` be morphisms of schemes, both
> locally of finite type, and let `r, e ≥ 0`. Let `F` be a quasi-coherent `𝒪_X`-module of finite
> type whose support on every fibre of `f` has dimension at most `r`, and let `G` be a
> quasi-coherent `𝒪_Y`-module of finite type whose support on every fibre of `g` has dimension at
> most `e`. Set `α = [F/X/Y]_r` and `β = [G/Y/S]_e`. If `F` is flat over `Y` then
> `α ∘ β = [F ⊗_{𝒪_X} f^* G/X/S]_{r + e}`.

```lean
theorem compFamily_familyAssociatedToModule {X Y S : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] (g : Y ⟶ S) [LocallyOfFiniteType g] (r e : ℕ) (F : X.Modules)
    [F.IsFiniteType] [F.IsQuasicoherent]
    (hF : ∀ y : Y, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι y)).obj F)) ≤ (r : WithBot ℕ∞))
    (hflat : IsFlatOver f.toLRSHom.toShHom F) (G : Y.Modules) [G.IsFiniteType]
    [G.IsQuasicoherent]
    (hG : ∀ t : S, topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (g.fiberι t)).obj G)) ≤ (e : WithBot ℕ∞)) :
    compFamily f g r e (familyAssociatedToModule f F r hF)
        (familyAssociatedToModule g G e hG) =
      familyAssociatedToModule (f ≫ g) (tensorPullback f F G) (r + e)
        (fibreDim_tensorPullback_le f g r e F hF G hG)
```

## Tag 0H6M, a lemma

[Tag 0H6M](https://stacks.math.columbia.edu/tag/0H6M) in the Stacks Project.

**`Stacks.Chow.compFamily_familyAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeComposition.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeComposition.lean#L182).

> **Stacks Project, Tag 0H6M.** Let `f : X ⟶ Y` and `g : Y ⟶ S` be morphisms of schemes, both
> locally of finite type, and let `r, e ≥ 0`. Let `Z ⊆ X` be a closed subscheme of relative
> dimension at most `r` over `Y`, so that the fibres `Z_y = Z ×_X X_y` have dimension at most `r`,
> and let `W ⊆ Y` be a closed subscheme of relative dimension at most `e` over `S`. Set
> `α = [Z/X/Y]_r` and `β = [W/Y/S]_e` (Example 0H4S). If `Z` is flat over `Y` then
> `α ∘ β = [Z ×_Y W/X/S]_{r + e}`.

```lean
theorem compFamily_familyAssociatedToClosedSubscheme {X Y S Z W : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] (g : Y ⟶ S) [LocallyOfFiniteType g] (r e : ℕ) (i : Z ⟶ X)
    [IsClosedImmersion i] [Flat (i ≫ f)]
    (hZ : ∀ y : Y, topologicalKrullDim (pullback i (f.fiberι y) : Scheme.{u}) ≤ (r : WithBot ℕ∞))
    (j : W ⟶ Y) [IsClosedImmersion j]
    (hW : ∀ t : S,
      topologicalKrullDim (pullback j (g.fiberι t) : Scheme.{u}) ≤ (e : WithBot ℕ∞)) :
    compFamily f g r e (familyAssociatedToClosedSubscheme f i r)
        (familyAssociatedToClosedSubscheme g j e) =
      familyAssociatedToClosedSubscheme (f ≫ g) (pullback.fst (i ≫ f) j ≫ i) (r + e)
```

## Tag 0H6N, a lemma

[Tag 0H6N](https://stacks.math.columbia.edu/tag/0H6N) in the Stacks Project.

**`Stacks.Chow.properPushforwardFamily_compFamily_baseChangeFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CompositionPushPull.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CompositionPushPull.lean#L294).

> **Stacks Project, Tag 0H6N.** Let `S` be a scheme, let
> ```
> X' --f--> X
> |         |
> v         v
> Y' --g--> Y
> ```
> be a cartesian square of schemes locally of finite type over `S` with `g` proper, realized by
> the fibre product `X' = X ×_Y Y'` with `f = pullback.fst`, let `r, e ≥ 0`, let `α` be a family
> of `r`-cycles on the fibres of `X/Y` and let `β'` be a family of `e`-cycles on the fibres of
> `Y'/S`. Then
>
> `f_*(g^*α ∘ β') = α ∘ g_*β'`
>
> as families of `(r + e)`-cycles on the fibres of `X/S`, where `∘` is the composition
> `Stacks.Chow.compFamily`, `g^*` is `Stacks.Chow.baseChangeFamily` and `f_*`, `g_*` are
> `Stacks.Chow.properPushforwardFamily`.

```lean
theorem properPushforwardFamily_compFamily_baseChangeFamily {X Y Y' S : Scheme.{u}}
    (sY : Y ⟶ S) [LocallyOfFiniteType sY] (sY' : Y' ⟶ S) [LocallyOfFiniteType sY']
    (p : X ⟶ Y) [LocallyOfFiniteType p] (g : Y' ⟶ Y) [IsProper g] (hg : g ≫ sY = sY')
    (r e : ℕ) (α : FamilyOfCycles p r) (β' : FamilyOfCycles sY' e) :
    properPushforwardFamily (pullback.snd p g ≫ sY') (p ≫ sY) (pullback.fst p g)
        (pullbackFst_comp_eq_of_base g rfl hg) (r + e)
        (compFamily (pullback.snd p g) sY' r e (baseChangeFamily p g r α) β') =
      compFamily p sY r e α (properPushforwardFamily sY' sY g hg e β')
```

## Tag 0H6P, a lemma

[Tag 0H6P](https://stacks.math.columbia.edu/tag/0H6P) in the Stacks Project.

**`Stacks.Chow.cap_compFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Composition.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Composition.lean#L378).

> **Stacks Project, Tag 0H6P.** Associativity of the action of families of cycles on fibres:
> for `α` a family of `r`-cycles on the fibres of `X/Y`, `β` a family of `e`-cycles on the fibres
> of `Y/S` and `γ` a `d`-cycle on `S`, we have `(α ∘ β) ∩ γ = α ∩ (β ∩ γ)` in `Z_{r + e + d}(X)`.
> Each side carries its δ-dimension in its own type, so the relation is stated between the
> underlying cycles on `X`.

```lean
theorem cap_compFamily (C : ChowSituation.{u}) (sS : S ⟶ C.S) [LocallyOfFiniteType sS]
    (f : X ⟶ Y) [LocallyOfFiniteType f] (g : Y ⟶ S) [LocallyOfFiniteType g] (r e : ℕ) {d : ℤ}
    (α : FamilyOfCycles f r) (β : FamilyOfCycles g e) (γ : CycleGroup C sS d) :
    (cap C sS (f ≫ g) (compFamily f g r e α β) γ : AlgebraicCycle X ℤ) =
      (cap C (g ≫ sS) f α (cap C sS g β γ) : AlgebraicCycle X ℤ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.14, Tag 0H6H](https://stacks.math.columbia.edu/tag/0H6H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

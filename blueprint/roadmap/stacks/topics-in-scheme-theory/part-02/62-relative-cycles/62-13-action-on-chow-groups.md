---
declaration: section
origin: cited
lean: Stacks.Chow.properPushforward_gysinCycleMap, Stacks.Chow.cap_baseChangeFamily_gysinCycleMap, Stacks.Chow.exists_bivariantClass_cap_mk_eq_relativeCycleCap, Stacks.Chow.CompatibleCycleCapRule.exists_relativeCycle
statement: formalized
proof: formalized
---

# 62.13 Action on chow groups

Section 62.13 of the Stacks Project, [Tag 0H6C](https://stacks.math.columbia.edu/tag/0H6C). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H6D, a lemma

[Tag 0H6D](https://stacks.math.columbia.edu/tag/0H6D) in the Stacks Project.

**`Stacks.Chow.properPushforward_gysinCycleMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestrictionPushforward.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/GysinTrivialRestrictionPushforward.lean#L368).

> **Stacks 0H6D.** The Gysin map on cycles of Stacks 0B6Z commutes with proper pushforward:
> in the cartesian square of Stacks 0B6Y
>
>   `D' --i'--> X'`
>   `|g          |f`
>   `D  --i-->  X`
>
> attached to a triple `(L, s, i : D ⟶ X)` whose invertible module restricts trivially to the zero
> scheme `D = Z(s)`, one has `i^* f_* α' = g_* (i')^* α'` in `Z_k(D)` for every `α' ∈ Z_{k+1}(X')`.
>
> The triviality of `L'|_{D'}` that the Gysin map on `X'` needs is not a hypothesis: it follows from
> the triviality of `L|_D`, by
> `Stacks.Divisors.isTrivial_pullback_zeroScheme_pullbackGlobalSections`.

```lean
theorem properPushforward_gysinCycleMap
    (htriv : AlgebraicGeometry.SheafOfModules.IsTrivial (zeroScheme X L s).subscheme.sheaf.obj
      (zeroScheme X L s).subscheme.ringCatSheaf.property
      ((Scheme.Modules.pullback (zeroScheme X L s).subschemeι).obj L))
    (α : CycleGroup C p' (k + 1)) :
    gysinCycleMap C p k L s htriv (properPushforward C p' p f hf (k + 1) α) =
      properPushforward C ((pullbackZeroScheme f L s).subschemeι ≫ p')
        ((zeroScheme X L s).subschemeι ≫ p) (zeroSchemePullbackMap f L s)
        (zeroSchemePullbackMap_comp_structureMorphism f L s p p' hf) k
        (gysinCycleMap C p' k ((Scheme.Modules.pullback f).obj L)
          (AlgebraicGeometry.pullbackGlobalSections f L s)
          (isTrivial_pullback_zeroScheme_pullbackGlobalSections f L s htriv) α)
```

## Tag 0H6E, a lemma

[Tag 0H6E](https://stacks.math.columbia.edu/tag/0H6E) in the Stacks Project.

**`Stacks.Chow.cap_baseChangeFamily_gysinCycleMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/GysinAction.lean, line 582](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/GysinAction.lean#L582).

> **Stacks Project, Tag 0H6E.** Let `(S, δ)` be as in Section 0H65, let `p : X ⟶ Y` be a
> morphism of schemes locally of finite type over `S`, let `r ≥ 0` and let `α ∈ z(X/Y, r)` be a
> relative `r`-cycle on `X/Y`. Let `(L, s, i : D ⟶ Y)` be as in Chow Homology, Definition 02T8:
> `L` an invertible module on `Y`, `s` a global section and `i` the closed immersion of its zero
> scheme `D`. Form the cartesian square of Chow Homology, Remark 0B6Y,
> ```
> E = X ×_Y D --j--> X
>      |             |
>      v             v
>      D    --i-->   Y
> ```
> so that `j` presents `E` as the zero scheme of the pulled-back section `p^* s` of `p^* L`. If
> `L|_D ≅ 𝒪_D`, then for every `e ∈ ℤ` and every `β ∈ Z_{e+1}(Y)`
> `i^*α ∩ i^*β = j^*(α ∩ β)` in `Z_{r+e}(E)`,
> where `∩` is the action of Section 0H65, `i^*α` the base change of `α` along `i`, and
> `i^* : Z_{e+1}(Y) ⟶ Z_e(D)` and `j^* : Z_{r+e+1}(X) ⟶ Z_{r+e}(E)` the Gysin maps on cycles of
> Chow Homology, Remark 0B6Z, the latter read along the presentation `j` of the zero scheme of
> `p^* s` (`Stacks.Chow.gysinCycleMapAlong`). The triviality of `(p^* L)|_E` that `j^*` needs is
> not a hypothesis: it follows from that of `L|_D`.

```lean
theorem cap_baseChangeFamily_gysinCycleMap (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (p : X ⟶ Y) [LocallyOfFiniteType p] (r : ℕ) (e : ℤ)
    (α : FamilyOfCycles p r)
    (hα : letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
      IsRelativeCycle p r α)
    (L : Y.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible Y.sheaf.obj Y.ringCatSheaf.property L]
    (s : Γ(L, ⊤))
    (htriv : AlgebraicGeometry.SheafOfModules.IsTrivial
      (Stacks.Divisors.zeroScheme Y L s).subscheme.sheaf.obj
      (Stacks.Divisors.zeroScheme Y L s).subscheme.ringCatSheaf.property
      ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme Y L s).subschemeι).obj L))
    (β : CycleGroup C sY (e + 1)) :
    cap C ((Stacks.Divisors.zeroScheme Y L s).subschemeι ≫ sY)
        (pullback.snd p (Stacks.Divisors.zeroScheme Y L s).subschemeι)
        (baseChangeFamily p (Stacks.Divisors.zeroScheme Y L s).subschemeι r α)
        (gysinCycleMap C sY e L s htriv β) =
      gysinCycleMapAlong C (p ≫ sY)
        (pullback.snd p (Stacks.Divisors.zeroScheme Y L s).subschemeι ≫
          (Stacks.Divisors.zeroScheme Y L s).subschemeι ≫ sY) ((r : ℤ) + e)
        ((Scheme.Modules.pullback p).obj L) (pullbackGlobalSections p L s)
        (pullback.fst p (Stacks.Divisors.zeroScheme Y L s).subschemeι)
        (Stacks.Divisors.isTrivial_pullback_zeroScheme_pullbackGlobalSections p L s htriv)
        (by rw [← Category.assoc, pullback.condition, Category.assoc])
        (Stacks.Divisors.zeroScheme_pullback p L s).symm
        (cycleGroupCongr C (p ≫ sY) (by ring) (cap C sY p α β))
```

## Tag 0H6F, a proposition

[Tag 0H6F](https://stacks.math.columbia.edu/tag/0H6F) in the Stacks Project.

**`Stacks.Chow.exists_bivariantClass_cap_mk_eq_relativeCycleCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/RelativeCycleGysin.lean, line 649](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/RelativeCycleGysin.lean#L649).

> **Stacks Project, Proposition 0H6F.** Let `(S, δ)` be as in Section 0H65, let `p : X ⟶ Y` be
> a morphism of schemes locally of finite type over `S`, let `r ≥ 0` and let `α ∈ z(X/Y, r)` be a
> relative `r`-cycle on `X/Y`. The rule that to every morphism `g : Y' ⟶ Y` locally of finite type
> and every `k ∈ ℤ` associates the operation `g^*α ∩ - : Z_k(Y') ⟶ Z_{r + k}(X')`,
> `X' = Y' ×_Y X` (`Stacks.Chow.relativeCycleCap`), factors through rational equivalence to define
> a bivariant class `c(α) ∈ A^{-r}(X ⟶ Y)`: there is a bivariant class of degree `-r` for `p`
> whose cap operation on every test scheme sends the class of a cycle `β` to the class of
> `g^*α ∩ β`. The class is `Stacks.Chow.relativeCycleBivariantClass`.

```lean
theorem exists_bivariantClass_cap_mk_eq_relativeCycleCap :
    ∃ c : BivariantClass C (gysinSystemOfInvertible C) (p ≫ sY) sY p rfl (-(r : ℤ)),
      ∀ {T : Scheme.{u}} (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ)
        (β : CycleGroup C (g ≫ sY) k),
        c.cap g k (QuotientAddGroup.mk' (rationalEquivalences C (g ≫ sY) k) β) =
          QuotientAddGroup.mk' (rationalEquivalences C (pullback.fst p g ≫ p ≫ sY) (k - -(r : ℤ)))
            (cycleGroupCongr C _ (by ring) (relativeCycleCap C sY p r α g k β))
```

## Tag 0H6G, a remark

[Tag 0H6G](https://stacks.math.columbia.edu/tag/0H6G) in the Stacks Project.

**`Stacks.Chow.CompatibleCycleCapRule.exists_relativeCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CycleCapRuleRelative.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CycleCapRuleRelative.lean#L185).

> **Stacks Project, Tag 0H6G.** Let `(S, δ)` be as in Section 0H65, let `p : X ⟶ Y` be a morphism
> of schemes locally of finite type over `S` and let `r ≥ 0`. Let `c` be a rule that to every
> morphism `g : Y' ⟶ Y` locally of finite type and every `e ∈ ℤ` associates an operation
> `c ∩ - : Z_e(Y') ⟶ Z_{r+e}(X')`, `X' = Y' ×_Y X`, compatible with proper pushforward, flat
> pullback, and Gysin maps as in Lemma 0H6E (`Stacks.Chow.CompatibleCycleCapRule`). Then there is a
> relative `r`-cycle `α` on `X/Y` such that `c ∩ - = g^*α ∩ -` for every such `g`, where `g^*α ∩ -`
> is `Stacks.Chow.relativeCycleCap`.

```lean
theorem CompatibleCycleCapRule.exists_relativeCycle (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (p : X ⟶ Y) [LocallyOfFiniteType p] (r : ℕ)
    (c : CompatibleCycleCapRule C sY p r) :
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    ∃ α ∈ relativeCycles p r, ∀ {Y' : Scheme.{u}} (g : Y' ⟶ Y) [LocallyOfFiniteType g] (e : ℤ),
      c.cap g e = relativeCycleCap C sY p r α g e
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.13, Tag 0H6C](https://stacks.math.columbia.edu/tag/0H6C)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

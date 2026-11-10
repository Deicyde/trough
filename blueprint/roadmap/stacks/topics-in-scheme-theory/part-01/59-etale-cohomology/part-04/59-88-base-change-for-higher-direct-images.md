---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.higherBaseChangeMapAb, Stacks.EtaleCohomology.BaseChangeHolds, Stacks.EtaleCohomology.mono_cokernelDesc_higherBaseChangeMapAb_app_of_injective, Stacks.EtaleCohomology.mono_higherBaseChangeMapAb_app_of_annihilated, Stacks.EtaleCohomology.mono_cokernelMap_higherBaseChangeMapAb_app_of_annihilated, Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_isIso_integralSurjective, Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_integralSurjective, Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_iff_of_isIntegralHom
statement: formalized
proof: formalized
---

# 59.88 Base change for higher direct images

Section 59.88 of the Stacks Project, [Tag 0F01](https://stacks.math.columbia.edu/tag/0F01). 7 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0F02, a remark

[Tag 0F02](https://stacks.math.columbia.edu/tag/0F02) in the Stacks Project.

**`Stacks.EtaleCohomology.higherBaseChangeMapAb`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/BaseChangeCondition.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/BaseChangeCondition.lean#L277). The attribute's comment: “bc”.

> **The base change map on higher direct images**, `(f')⁻¹ R^q g_* ⟶ R^q h_* e⁻¹`, for abelian
> sheaves on the small étale sites of a commutative square. It is the degree-`q` cohomology of the
> canonical derived base change comparison `smallEtaleDerivedBaseChangeAb`, transported along the
> canonical identifications `baseChangeSourceIso` and `baseChangeTargetIso` of the two sides with
> cohomology of the bounded below derived composites.

```lean
public def higherBaseChangeMapAb (q : ℕ) :
    (smallEtalePushforwardAb g).rightDerived q ⋙ smallEtalePullbackAb f' ⟶
      smallEtalePullbackAb e ⋙ (smallEtalePushforwardAb h).rightDerived q
```

**`Stacks.EtaleCohomology.BaseChangeHolds`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/BaseChangeCondition.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/BaseChangeCondition.lean#L352).

> **The condition `BC(f, n, q₀)` of Stacks 0F02.** For `f : X ⟶ S` a morphism of schemes and
> `n` an integer, `BC(f, n, q₀)` holds if for every commutative diagram
>
> ```
> X  ←--  X'  ←-h-  Y
> |f      |f'       |e
> S  ←--  S'  ←-g-  T
> ```
>
> in which `X' = X ×_S S'` and `Y = X' ×_{S'} T` and `g` is quasi-compact and quasi-separated,
> and every abelian sheaf `F` on the small étale site of `T` annihilated by `n`, the base change
> map `(f')⁻¹ R^q g_* F ⟶ R^q h_* e⁻¹ F` is an isomorphism for every `q ≤ q₀`.
>
> The two cartesian squares are the hypotheses `IsPullback p f' f s` and `IsPullback h e f' g`;
> the map whose invertibility is asserted is `higherBaseChangeMapAb`, the base change map on
> higher direct images. Annihilation by `n` is imposed on every section of `F`, which is the same
> as annihilation of `F` itself.

```lean
public abbrev BaseChangeHolds {X S : Scheme.{u}} (f : X ⟶ S) (n q₀ : ℤ) : Prop
```

## Tag 0F03, a lemma

[Tag 0F03](https://stacks.math.columbia.edu/tag/0F03) in the Stacks Project.

**`Stacks.EtaleCohomology.mono_cokernelDesc_higherBaseChangeMapAb_app_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/TorsionSheafEmbedding.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/TorsionSheafEmbedding.lean#L281). The attribute's comment: “part (3), the cokernel inside R^q h_* e⁻¹ of an injective ℤ/nℤ-module sheaf”.

> **Part (3) of [Stacks, Tag 0F03].** In the situation of
> `mono_higherBaseChangeMapAb_app_of_injective`, with `F` annihilated by `n` contained in the
> underlying abelian sheaf of an injective sheaf `I` of `ℤ/nℤ`-modules,
>
> `Coker((f')⁻¹R^{q+1} g_* F ⟶ R^{q+1} h_* e⁻¹F) ⊂ R^{q+1} h_* e⁻¹I`,
>
> the inclusion being the canonical map induced by `R^{q+1}h_* e⁻¹(F ⟶ I)`, which is defined
> because `higherBaseChangeMapAb_app_comp_map_eq_zero_of_injective` vanishes. This is
> `mono_cokernelDesc_higherBaseChangeMapAb_app_of_shortExact` with its short exact sequence
> constructed from `F ⊂ I`.

```lean
public theorem mono_cokernelDesc_higherBaseChangeMapAb_app_of_injective
    (hbc : BaseChangeHolds f n (q : ℤ))
    (sq₁ : IsPullback p f' f s) (sq : IsPullback h e f' g)
    [QuasiCompact g] [QuasiSeparated g]
    {F : Sheaf (smallEtaleTopology T) Ab.{u + 1}}
    (hF : ∀ (U : T.Etale) (x : F.obj.obj (op U)), n • x = 0)
    (I : SheafOfModules.{u + 1} (etaleZModRingSheaf T n)) [Injective I]
    (k : F ⟶ (SheafOfModules.toSheaf.{u + 1} (etaleZModRingSheaf T n)).obj I) (hk : Mono k) :
    Mono (cokernel.desc ((higherBaseChangeMapAb f' g h e sq.w (q + 1)).app F)
      ((higherBaseChangeTarget h e (q + 1)).map k)
      (higherBaseChangeMapAb_app_comp_map_eq_zero_of_injective n q f' g h e sq I k hk))
```

**`Stacks.EtaleCohomology.mono_higherBaseChangeMapAb_app_of_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/TorsionSheafEmbedding.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/TorsionSheafEmbedding.lean#L355). The attribute's comment: “part (1), injectivity of the base change map”.

> **Part (1) of [Stacks, Tag 0F03].** With `f : X ⟶ S` and `n` as in [Stacks, Tag 0F02],
> assume `BC(f, n, q)`, let
>
> ```
> X  ←--  X'  ←-h-  Y
> |f      |f'       |e
> S  ←--  S'  ←-g-  T
> ```
>
> be a commutative diagram with `X' = X ×_S S'` and `Y = X' ×_{S'} T` and `g` quasi-compact and
> quasi-separated, and let `F` be an abelian sheaf on the small étale site of `T` annihilated
> by `n`. Then the base change map `(f')⁻¹R^{q+1} g_* F ⟶ R^{q+1} h_* e⁻¹F` is injective.
>
> This is `mono_higherBaseChangeMapAb_app_of_injective` at the embedding
> `torsionEtaleInjectiveEmbedding` of `F` into an injective sheaf of `ℤ/nℤ`-modules.

```lean
public theorem mono_higherBaseChangeMapAb_app_of_annihilated
    (hbc : BaseChangeHolds f n (q : ℤ))
    (sq₁ : IsPullback p f' f s) (sq : IsPullback h e f' g)
    [QuasiCompact g] [QuasiSeparated g]
    {F : Sheaf (smallEtaleTopology T) Ab.{u + 1}}
    (hF : ∀ (U : T.Etale) (x : F.obj.obj (op U)), n • x = 0) :
    Mono ((higherBaseChangeMapAb f' g h e sq.w (q + 1)).app F)
```

**`Stacks.EtaleCohomology.mono_cokernelMap_higherBaseChangeMapAb_app_of_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/TorsionSheafEmbedding.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/TorsionSheafEmbedding.lean#L377). The attribute's comment: “part (2), the cokernel inclusion under F ⊂ G”.

> **Part (2) of [Stacks, Tag 0F03].** In the situation of
> `mono_higherBaseChangeMapAb_app_of_annihilated`, if `F ⊂ G` where `G` on the small étale site
> of `T` is annihilated by `n`, then
>
> `Coker((f')⁻¹R^{q+1}g_* F → R^{q+1}h_* e⁻¹F) ⊂ Coker((f')⁻¹R^{q+1}g_* G → R^{q+1}h_* e⁻¹G)`,
>
> the inclusion being the map induced on cokernels by the naturality square of the base change
> map. This is `mono_cokernelMap_higherBaseChangeMapAb_app_of_injective` at the embedding
> `torsionEtaleInjectiveEmbedding` of `G` into an injective sheaf of `ℤ/nℤ`-modules, which
> realises the choice `F ⊂ G ⊂ I` of the source.

```lean
public theorem mono_cokernelMap_higherBaseChangeMapAb_app_of_annihilated
    (hbc : BaseChangeHolds f n (q : ℤ))
    (sq₁ : IsPullback p f' f s) (sq : IsPullback h e f' g)
    [QuasiCompact g] [QuasiSeparated g]
    {F G : Sheaf (smallEtaleTopology T) Ab.{u + 1}} (i : F ⟶ G) (hi : Mono i)
    (hF : ∀ (U : T.Etale) (x : F.obj.obj (op U)), n • x = 0)
    (hG : ∀ (U : T.Etale) (x : G.obj.obj (op U)), n • x = 0) :
    Mono (cokernel.map ((higherBaseChangeMapAb f' g h e sq.w (q + 1)).app F)
      ((higherBaseChangeMapAb f' g h e sq.w (q + 1)).app G)
      ((higherBaseChangeSource f' g (q + 1)).map i)
      ((higherBaseChangeTarget h e (q + 1)).map i)
      ((higherBaseChangeMapAb f' g h e sq.w (q + 1)).naturality i).symm)
```

## Tag 0F04, a lemma

[Tag 0F04](https://stacks.math.columbia.edu/tag/0F04) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_isIso_integralSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/IntegralDirectImagePasting.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/IntegralDirectImagePasting.lean#L235).

> **Stacks Project, Tag 0F04.** With `f : X ⟶ S` and `n` as in [Stacks, Tag 0F02], assume
> `BC(f, n, q)`. Consider the commutative diagrams
>
> ```
> X  ←--  X'  ←-h-  Y  ←-π'-  Y'            X'  ←----h' = π' ≫ h----  Y'
> |f      |f'       |e        |e'    and    |f'                       |e'
> S  ←--  S'  ←-g-  T  ←-π-   T'            S'  ←----g' = π ≫ g-----  T'
> ```
>
> with all squares cartesian, `g` quasi-compact and quasi-separated and `π` integral surjective,
> and let `F` be an abelian sheaf on the small étale site of `T` annihilated by `n`, with
> `F' = π⁻¹F`. If the base change map
> `(f')⁻¹ R^{q+1} g'_* F' ⟶ R^{q+1} h'_* (e')⁻¹ F'` of the pasted diagram is an isomorphism, then
> so is the base change map `(f')⁻¹ R^{q+1} g_* F ⟶ R^{q+1} h_* e⁻¹ F` of the middle square.
>
> The index convention is that of [Stacks, Tag 0F03] in this library: the source's `q ≥ 1` with
> `BC(f, n, q - 1)` is read as degree `q + 1` with `BC(f, n, q)`.
>
> The unit `F ⟶ π_*π⁻¹F` is a monomorphism because `π` is surjective
> (`Stacks.EtaleCohomology.mono_smallEtaleUnitAb_of_surjective`) and `π_*π⁻¹F` is annihilated by
> `n` (`Stacks.EtaleCohomology.zsmul_eq_zero_of_additive`), so by parts (1) and (2) of
> [Stacks, Tag 0F03] it suffices that the base change map of the middle square at `π_*π⁻¹F` is an
> isomorphism. That is the hypothesis, read through
> `Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_pushforward_iff`, which is where
> [Stacks, Tag 0EYP], [Stacks, Tag 04C2] and the relative Leray identification `Rπ_* = π_*` enter.

```lean
public theorem isIso_higherBaseChangeMapAb_app_of_isIso_integralSurjective
    {X S S' X' T Y T' Y' : Scheme.{u}} (f : X ⟶ S) (n : ℤ) (q : ℕ)
    (hbc : BaseChangeHolds f n (q : ℤ))
    (s : S' ⟶ S) (p : X' ⟶ X) (f' : X' ⟶ S') (sq₁ : IsPullback p f' f s)
    (g : T ⟶ S') (h : Y ⟶ X') (e : Y ⟶ T) (sq₂ : IsPullback h e f' g)
    [QuasiCompact g] [QuasiSeparated g]
    (π : T' ⟶ T) (π' : Y' ⟶ Y) (e' : Y' ⟶ T') (sq₃ : IsPullback π' e' e π)
    [IsIntegralHom π] [Surjective π]
    (F : Sheaf (smallEtaleTopology T) Ab.{u + 1})
    (hF : ∀ (U : T.Etale) (y : F.obj.obj (op U)), n • y = 0)
    (hpaste : IsIso ((higherBaseChangeMapAb f' (π ≫ g) (π' ≫ h) e'
      (sq₃.paste_horiz sq₂).w (q + 1)).app ((smallEtalePullbackAb π).obj F))) :
    IsIso ((higherBaseChangeMapAb f' g h e sq₂.w (q + 1)).app F)
```

**`Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_integralSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/IntegralSurjectiveCoverCriterion.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/IntegralSurjectiveCoverCriterion.lean#L145).

> **Stacks Project, Tag 0F04.** With `f : X ⟶ S` and `n` as in [Stacks, Tag 0F02], assume
> `BC(f, n, q)`. Consider the commutative diagrams
>
> ```
> X  ←--  X'  ←-h-  Y  ←-π'-  Y'            X'  ←----h' = π' ≫ h----  Y'
> |f      |f'       |e        |e'    and    |f'                       |e'
> S  ←--  S'  ←-g-  T  ←-π-   T'            S'  ←----g' = π ≫ g-----  T'
> ```
>
> with all squares cartesian, `g` quasi-compact and quasi-separated and `π` integral surjective,
> and let `F` be an abelian sheaf on the small étale site of `T` annihilated by `n`, with
> `F' = π⁻¹F`. If the base change map `(f')⁻¹ R^{q+1} g'_* F' ⟶ R^{q+1} h'_* (e')⁻¹ F'` of the
> pasted diagram is an isomorphism, then so is the base change map
> `(f')⁻¹ R^{q+1} g_* F ⟶ R^{q+1} h_* e⁻¹ F` of the middle square.
>
> The index convention is that of [Stacks, Tag 0F03] in this library: the source's `q ≥ 1` with
> `BC(f, n, q - 1)` is read as degree `q + 1` with `BC(f, n, q)`.
>
> Both base change maps are decided by the criterion
> `isIso_higherBaseChangeMapAb_app_iff_map_eq_zero` of [Stacks, Tag 0F03]. Embed `F'` into an
> injective sheaf `J'` of `ℤ/nℤ`-modules by `k'`; the hypothesis says `R^{q+1}h'_*(e')⁻¹k' = 0`.
> The sheaf `π_*J'` is annihilated by `n` and receives `F` by the monomorphism
> `F ⟶ π_*π⁻¹F ⟶ π_*J'`, the unit being injective because `π` is surjective; embedding `π_*J'`
> into an injective sheaf of `ℤ/nℤ`-modules gives an embedding of `F` factoring through it. And
> `R^{q+1}h_* e⁻¹(π_*k')` vanishes: through the base change transformation
> `e⁻¹π_* ⟶ π'_*(e')⁻¹` of `exists_baseChange_isIso_of_baseChangeHolds`, invertible at `J'`, it is
> carried to `R^{q+1}h_*(π'_*(e')⁻¹k')`, which is `R^{q+1}h'_*(e')⁻¹k'` read through
> `integralCompRightDerivedIso π' h`, `π'` being integral.

```lean
public theorem isIso_higherBaseChangeMapAb_app_of_integralSurjective
    {X S S' X' T Y T' Y' : Scheme.{u}} (f : X ⟶ S) (n : ℤ) (q : ℕ)
    (hbc : BaseChangeHolds f n (q : ℤ))
    (s : S' ⟶ S) (p : X' ⟶ X) (f' : X' ⟶ S') (sq₁ : IsPullback p f' f s)
    (g : T ⟶ S') (h : Y ⟶ X') (e : Y ⟶ T) (sq₂ : IsPullback h e f' g)
    [QuasiCompact g] [QuasiSeparated g]
    (π : T' ⟶ T) (π' : Y' ⟶ Y) (e' : Y' ⟶ T') (sq₃ : IsPullback π' e' e π)
    [IsIntegralHom π] [Surjective π]
    (F : Sheaf (smallEtaleTopology T) Ab.{u + 1})
    (hF : ∀ (U : T.Etale) (y : F.obj.obj (op U)), n • y = 0)
    (hcollapse : IsIso ((higherBaseChangeMapAb f' (π ≫ g) (π' ≫ h) e'
      (sq₃.paste_horiz sq₂).w (q + 1)).app ((smallEtalePullbackAb π).obj F))) :
    IsIso ((higherBaseChangeMapAb f' g h e sq₂.w (q + 1)).app F)
```

## Tag 0F05, a lemma

[Tag 0F05](https://stacks.math.columbia.edu/tag/0F05) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_iff_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/IntegralBaseCriterion.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/IntegralBaseCriterion.lean#L98). The attribute's comment: “as an equivalence; the source's statement is the forward implication”.

> **Stacks Project, Tag 0F05.** With `f : X ⟶ S` and `n` as in [Stacks, Tag 0F02], let
> `q ≥ 1` and assume `BC(f, n, q - 1)`. Consider the commutative diagrams
>
> ```
> X  ←--  X'  ←-π'-  X''  ←-h'-  Y                X'  ←------h------  Y
> |f      |f'        |f''        |e       and     |f'                 |e
> S  ←--  S'  ←-π-   S''  ←-g'-  T                S'  ←------g------  T
> ```
>
> with all squares cartesian, `g'` quasi-compact and quasi-separated, `π` integral,
> `h = h' ≫ π'` and `g = g' ≫ π`, and let `F` be an abelian sheaf on the small étale site of `T`
> annihilated by `n`. Then the base change map `(f')⁻¹ R^q g_* F ⟶ R^q h_* e⁻¹ F` of the
> collapsed diagram is an isomorphism if and only if the base change map
> `(f'')⁻¹ R^q g'_* F ⟶ R^q h'_* e⁻¹ F` of the right-hand square is. The source's statement is the
> forward implication.
>
> Both are decided by the criterion `isIso_higherBaseChangeMapAb_app_iff_map_eq_zero` at one
> embedding `F ⊂ I` into an injective sheaf of `ℤ/nℤ`-modules, and the two morphisms it asks to
> vanish correspond under `rightDerivedCompIntegralIso h' π'`, the faithful functor `π'_*`
> carrying one to the other.

```lean
public theorem isIso_higherBaseChangeMapAb_app_iff_of_isIntegralHom
    {X S X' S' X'' S'' Y T : Scheme.{u}} (f : X ⟶ S) (n : ℤ) (q : ℕ) (hq : 1 ≤ q)
    (hbc : BaseChangeHolds f n ((q : ℤ) - 1)) (s : S' ⟶ S) (p : X' ⟶ X) (f' : X' ⟶ S')
    (sq₁ : IsPullback p f' f s) (π : S'' ⟶ S') (π' : X'' ⟶ X') (f'' : X'' ⟶ S'')
    (sq₂ : IsPullback π' f'' f' π) (g' : T ⟶ S'') (h' : Y ⟶ X'') (e : Y ⟶ T)
    (sq₃ : IsPullback h' e f'' g') [QuasiCompact g'] [QuasiSeparated g'] [IsIntegralHom π]
    (F : Sheaf (smallEtaleTopology T) Ab.{u + 1})
    (hF : ∀ (U : T.Etale) (x : F.obj.obj (Opposite.op U)), n • x = 0) :
    IsIso ((higherBaseChangeMapAb f' (g' ≫ π) (h' ≫ π') e (sq₃.paste_horiz sq₂).w q).app F) ↔
      IsIso ((higherBaseChangeMapAb f'' g' h' e sq₃.w q).app F)
```

**`Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_isIso_collapsed_of_bc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/IntegralBaseLeray.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/IntegralBaseLeray.lean#L192).

> **Stacks Project, Tag 0F05.** With `f : X ⟶ S` and `n` as in [Stacks, Tag 0F02], let
> `q ≥ 1` and assume `BC(f, n, q - 1)`. Consider the commutative diagrams
>
> ```
> X  ←--  X'  ←-π'-  X''  ←-h'-  Y                X'  ←------h------  Y
> |f      |f'        |f''        |e       and     |f'                 |e
> S  ←--  S'  ←-π-   S''  ←-g'-  T                S'  ←------g------  T
> ```
>
> with all squares cartesian, `g'` quasi-compact and quasi-separated, `π` integral,
> `h = h' ≫ π'` and `g = g' ≫ π`, and let `F` be an abelian sheaf on the small étale site of `T`
> annihilated by `n`. If the base change map `(f')⁻¹ R^q g_* F ⟶ R^q h_* e⁻¹ F` of the collapsed
> diagram is an isomorphism, then so is the base change map
> `(f'')⁻¹ R^q g'_* F ⟶ R^q h'_* e⁻¹ F` of the right-hand square.
>
> The two relative Leray identifications the source's proof uses are supplied, not assumed: they
> are `Stacks.EtaleCohomology.integralLerayIso` for `g = g' ≫ π` and for `h = h' ≫ π'`, the
> second along the base change `π'` of `π`, whose integrality is
> `Stacks.EtaleCohomology.isIntegralHom_of_isPullback`.
>
> The remaining identification, [Stacks, Tag 0EYP] for the middle square, is not assumed either:
> it is needed only at the cohomology sheaves of `Rg'_* F`, which are annihilated by `n` because
> `F` is, and there it is the source's own `BC(f, n, q - 1)` read in degree zero, which is
> `Stacks.EtaleCohomology.isIso_smallEtaleBaseChangeAb_app_of_annihilated`. That only the
> cohomology sheaves matter is
> `Stacks.Cohomology.BaseChange.isIso_derived_app_iff_homology`, both legs of the middle square's
> direct image being exact.
>
> The pasting compatibility the source elides is *not* assumed: it is
> `Stacks.EtaleCohomology.smallEtaleDerivedBaseChangeAb_eq_derivedVPaste_app`, the pasting law for
> the derived base change comparison along the direct image legs, whose two leg comparisons
> `Rg'_* ⋙ Rπ_* ≅ R(g' ≫ π)_*` and `Rh'_* ⋙ Rπ'_* ≅ R(h' ≫ π')_*` are the derived form of the
> relative Leray identification for an integral morphism. Of the four factors of that pasting,
> two are isomorphisms outright, the third is one by the preceding paragraph, and the fourth is
> the direct image
> along `π'` of the base change map of the right-hand square; the conclusion is then
> `isIso_pushforward_higherBaseChangeMapAb_app_iff` in the form carried by
> `Stacks.EtaleCohomology.isIso_smallEtalePushforwardAb_map_iff_of_isIntegralHom`.

```lean
public theorem isIso_higherBaseChangeMapAb_app_of_isIso_collapsed_of_bc
    {X S X' S' X'' S'' Y T : Scheme.{u}} (f : X ⟶ S) (n : ℤ) (q : ℕ) (hq : 1 ≤ q)
    (hbc : BaseChangeHolds f n ((q : ℤ) - 1)) (s : S' ⟶ S) (p : X' ⟶ X) (f' : X' ⟶ S')
    (sq₁ : IsPullback p f' f s) (π : S'' ⟶ S') (π' : X'' ⟶ X') (f'' : X'' ⟶ S'')
    (sq₂ : IsPullback π' f'' f' π) (g' : T ⟶ S'') (h' : Y ⟶ X'') (e : Y ⟶ T)
    (sq₃ : IsPullback h' e f'' g') [QuasiCompact g'] [QuasiSeparated g'] [IsIntegralHom π]
    (F : Sheaf (smallEtaleTopology T) Ab.{u + 1})
    (hF : ∀ (U : T.Etale) (x : F.obj.obj (Opposite.op U)), n • x = 0)
    (hcollapse : IsIso
      ((higherBaseChangeMapAb f' (g' ≫ π) (h' ≫ π') e (sq₃.paste_horiz sq₂).w q).app F)) :
    IsIso ((higherBaseChangeMapAb f'' g' h' e sq₃.w q).app F)
```

## Tag 0F06, a lemma

[Tag 0F06](https://stacks.math.columbia.edu/tag/0F06) in the Stacks Project.

**`AlgebraicGeometry.exists_field_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FieldPoint.lean, line 559](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FieldPoint.lean#L559).

> **Stacks Project, Tag 0F06.** A property of quasi-compact, quasi-separated schemes
> over a nonempty base, invariant under thickenings and stable under affine-transition
> inverse limits and passage to a closed subscheme or its quasi-compact open complement,
> holds at some field-valued point.
>
> The `[Nonempty T]` hypothesis is deliberate and necessary rather than a weakening. Without it the
> statement is false: `T = Spec PUnit` is empty and affine, hence quasi-compact and quasi-separated,
> and for `P = fun _ _ ↦ True` all four remaining hypotheses hold, while the conclusion would supply
> a morphism into `T` from the nonempty scheme `Spec K`. The Stacks statement leaves the condition
> implicit; the proof below needs it to put `⊥` into the family of closed subschemes that are
> nonempty and carry `P`, which is where Zorn's lemma is applied.

```lean
public theorem exists_field_point {T : Scheme.{u}} [Nonempty T] [CompactSpace T]
    [QuasiSeparatedSpace T] (P : ∀ X : Scheme.{u}, (X ⟶ T) → Prop)
    (hThickening : ∀ {X X' : Scheme.{u}} [CompactSpace X] [QuasiSeparatedSpace X]
      [CompactSpace X'] [QuasiSeparatedSpace X'] (i : X ⟶ X') (f : X' ⟶ T),
      IsThickening i → (P X (i ≫ f) ↔ P X' f))
    (hLimit : ∀ {I : Type u} [Category.{u} I] [IsCofiltered I]
      (D : I ⥤ Scheme.{u})
      [∀ {i j : I} (a : i ⟶ j), IsAffineHom (D.map a)]
      [∀ i, CompactSpace (D.obj i)] [∀ i, QuasiSeparatedSpace (D.obj i)]
      (c : Cone D) (_ : IsLimit c)
      [CompactSpace c.pt] [QuasiSeparatedSpace c.pt]
      (f : c.pt ⟶ T) (fi : ∀ i, D.obj i ⟶ T),
      (∀ {i j : I} (a : i ⟶ j), D.map a ≫ fi j = fi i) →
      (∀ i, c.π.app i ≫ fi i = f) →
      (∀ i, P (D.obj i) (fi i)) → P c.pt f)
    (hClosedOrOpen : ∀ {X : Scheme.{u}} [CompactSpace X]
      [QuasiSeparatedSpace X] (f : X ⟶ T) (J : X.IdealSheafData)
      [CompactSpace J.subscheme] [QuasiSeparatedSpace J.subscheme]
      (V : X.Opens) (_hV : (V : Set X) = (J.support : Set X)ᶜ)
      [CompactSpace V.toScheme] [QuasiSeparatedSpace V.toScheme],
      P X f → (P V.toScheme (V.ι ≫ f) ∨
        P J.subscheme (J.subschemeι ≫ f)))
    (hP : P T (𝟙 T)) :
    ∃ (K : Type u) (_ : Field K) (g : Spec (.of K) ⟶ T),
      P (Spec (.of K)) g
```

**`AlgebraicGeometry.exists_field_point_of_isDirected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FieldPointDirected.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FieldPointDirected.lean#L108). The attribute's comment: “the limit hypothesis for directed inverse systems, as in the source”.

> **Stacks Project, Tag 0F06.** Let `T` be a nonempty quasi-compact quasi-separated scheme and
> `P` a property of quasi-compact quasi-separated schemes over `T` such that
>
> 1. `P` is invariant under thickenings;
> 2. if `T'` is the limit of a directed inverse system of quasi-compact quasi-separated schemes
>    `Tᵢ` over `T` with affine transition morphisms and `P(Tᵢ)` holds for all `i`, then `P(T')`
>    holds;
> 3. if `P(T')` holds, `Z ⊂ T'` is a closed subscheme and its complement `U` is quasi-compact, then
>    `P(U)` or `P(Z)` holds;
>
> and such that `P(T)` holds. Then there are a field `K` and a morphism `Spec K ⟶ T` with
> `P(Spec K)`.
>
> The limit hypothesis is the source's, for directed inverse systems; it is reduced to the one of
> `AlgebraicGeometry.exists_field_point`, for small cofiltered diagrams, by
> `AlgebraicGeometry.limit_property_of_isCofiltered`. The `[Nonempty T]` hypothesis is necessary,
> as recorded at `AlgebraicGeometry.exists_field_point`.

```lean
public theorem exists_field_point_of_isDirected {T : Scheme.{u}} [Nonempty T] [CompactSpace T]
    [QuasiSeparatedSpace T] (P : ∀ X : Scheme.{u}, (X ⟶ T) → Prop)
    (hThickening : ∀ {X X' : Scheme.{u}} [CompactSpace X] [QuasiSeparatedSpace X]
      [CompactSpace X'] [QuasiSeparatedSpace X'] (i : X ⟶ X') (f : X' ⟶ T),
      IsThickening i → (P X (i ≫ f) ↔ P X' f))
    (hLimit : ∀ {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)] [Nonempty I]
      (D : Iᵒᵖ ⥤ Scheme.{u})
      [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (D.map a)]
      [∀ i, CompactSpace (D.obj i)] [∀ i, QuasiSeparatedSpace (D.obj i)]
      (c : Cone D) (_ : IsLimit c)
      [CompactSpace c.pt] [QuasiSeparatedSpace c.pt]
      (f : c.pt ⟶ T) (fi : ∀ i, D.obj i ⟶ T),
      (∀ {i j : Iᵒᵖ} (a : i ⟶ j), D.map a ≫ fi j = fi i) →
      (∀ i, c.π.app i ≫ fi i = f) →
      (∀ i, P (D.obj i) (fi i)) → P c.pt f)
    (hClosedOrOpen : ∀ {X : Scheme.{u}} [CompactSpace X]
      [QuasiSeparatedSpace X] (f : X ⟶ T) (J : X.IdealSheafData)
      [CompactSpace J.subscheme] [QuasiSeparatedSpace J.subscheme]
      (V : X.Opens) (_hV : (V : Set X) = (J.support : Set X)ᶜ)
      [CompactSpace V.toScheme] [QuasiSeparatedSpace V.toScheme],
      P X f → (P V.toScheme (V.ι ≫ f) ∨
        P J.subscheme (J.subschemeι ≫ f)))
    (hP : P T (𝟙 T)) :
    ∃ (K : Type u) (_ : Field K) (g : Spec (.of K) ⟶ T),
      P (Spec (.of K)) g
```

## Tag 0F07, a lemma

[Tag 0F07](https://stacks.math.columbia.edu/tag/0F07) in the Stacks Project.

**`Stacks.EtaleCohomology.exists_affine_field_not_isIso_higherBaseChangeMapAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FirstFailureFieldObstruction.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FirstFailureFieldObstruction.lean#L238).

> **Stacks Project, Tag 0F07.** With `f : X ⟶ S` and `n` as in [Stacks, Tag 0F02], assume
> `BC(f, n, q)` holds and `BC(f, n, q + 1)` does not. Then there are a commutative diagram
>
> ```
> X  ←--  X'  ←-h-  Y
> |f      |f'       |e
> S  ←--  S'  ←-g-  Spec K
> ```
>
> with `X' = X ×_S S'`, `Y = X' ×_{S'} Spec K`, `S'` affine and `K` a field, and an abelian sheaf
> `F` on the small étale site of `Spec K` annihilated by `n`, such that
> `(f')⁻¹ R^{q+1} g_* F ⟶ R^{q+1} h_* e⁻¹ F` is not an isomorphism.
>
> The source's *"we may and do replace `S'` by an affine open of `S'`"* is
> `Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_forall_isAffine`. The dévissage
> `AlgebraicGeometry.exists_field_point_of_isDirected` of [Stacks, Tag 0F06] is applied to the
> source's property `P`, which is `Stacks.EtaleCohomology.ObstructionSurvives`; its three
> hypotheses are `Stacks.EtaleCohomology.obstructionSurvives_iff_of_isThickening`,
> `Stacks.EtaleCohomology.obstructionSurvives_of_isLimit` and
> `Stacks.EtaleCohomology.obstructionSurvives_open_or_closed`.
>
> Proved here: that the failure of `BC(f, n, q + 1)` under `BC(f, n, q)` is a failure in degree
> exactly `q + 1`, that the shrunk base is quasi-compact and quasi-separated, the choice of the
> obstruction class and that `P` holds at the base, that `P` at a field-valued point is a failure
> of base change, and that the sheaf the dévissage returns is annihilated by `n`.

```lean
public theorem exists_affine_field_not_isIso_higherBaseChangeMapAb {X S : Scheme.{u}} (f : X ⟶ S)
    (n : ℤ) (q : ℕ) (hprev : BaseChangeHolds f n (q : ℤ))
    (hfail : ¬ BaseChangeHolds f n ((q : ℤ) + 1)) :
    ∃ (S' X' Y : Scheme.{u}) (_ : IsAffine S') (s : S' ⟶ S) (p : X' ⟶ X) (f' : X' ⟶ S')
      (_hp : IsPullback p f' f s) (K : Type u) (_ : Field K) (g : Spec (.of K) ⟶ S')
      (h : Y ⟶ X') (e : Y ⟶ Spec (.of K)) (sq : IsPullback h e f' g)
      (F : Sheaf (smallEtaleTopology (Spec (.of K))) Ab.{u + 1}),
      (∀ (U : (Spec (.of K)).Etale) (x : F.obj.obj (op U)), n • x = 0) ∧
        ¬ IsIso ((higherBaseChangeMapAb f' g h e sq.w (q + 1)).app F)
```

## Tag 0F08, a lemma

[Tag 0F08](https://stacks.math.columbia.edu/tag/0F08) in the Stacks Project.

**`Stacks.EtaleCohomology.FirstFailureDiagram.normalFailureDiagram_of_not_baseChangeHolds`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FirstFailureDiagram.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FirstFailureDiagram.lean#L412). The attribute's comment: “the base change condition BC(f, n, q) of 0F02 and its failure in degree q + 1, indexed as the source's BC(f, n, q - 1) and BC(f, n, q)”.

> **Stacks Project, Tag 0F08.** With `f : X ⟶ S` and `n` as in [Stacks, Tag 0F02], assume
> `BC(f, n, q)` holds and `BC(f, n, q + 1)` does not (the source's `BC(f, n, q - 1)` and
> `BC(f, n, q)` for `q ≥ 1`, indexed from `q + 1`). Then there are a commutative diagram
>
> ```
> X  ←--  X'  ←-h-  Y
> |f      |f'       |e
> S  ←--  S'  ←-g-  Spec K
> ```
>
> with both squares cartesian, in which `S'` is affine, integral and normal with algebraically
> closed function field, `K` is algebraically closed and `g : Spec K ⟶ S'` is dominant, and an
> integer `d ∣ n` for which `R^{q+1} h_*(ℤ/dℤ)` is nonzero; this is `NormalFailureDiagram`,
> the sheaf `ℤ/dℤ` on `Y` being the inverse image along `e` of `constantZMod (Spec K) d`, the
> constant sheaf `ℤ/dℤ` on `Spec K`. `BaseChangeHolds` is the condition `BC(f, n, q₀)` of
> [Stacks, Tag 0F02].
>
> The failure is first realised over the spectrum of a field `K` with `S'` affine by
> [Stacks, Tag 0F07] (`Stacks.EtaleCohomology.exists_affine_field_not_isIso_higherBaseChangeMapAb`).
> The field is replaced by an algebraic closure `K̄` by
> [Stacks, Tag 0F04] (`Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_integralSurjective`)
> applied to the integral surjective `Spec K̄ ⟶ Spec K`, and the diagram is then normalized by
> `normalFailureDiagram_of_isAlgClosed`.

```lean
public theorem normalFailureDiagram_of_not_baseChangeHolds {X S : Scheme.{u}} (f : X ⟶ S)
    (n : ℤ) (q : ℕ) (hprev : BaseChangeHolds f n (q : ℤ))
    (hfail : ¬ BaseChangeHolds f n ((q : ℤ) + 1)) :
    NormalFailureDiagram f n (q + 1)
```

**`Stacks.EtaleCohomology.FirstFailureDiagram.normalFailureDiagram_of_firstFailure`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FirstFailureDiagramNormalization.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/FirstFailureDiagramNormalization.lean#L128).

> With `f : X ⟶ S` and `n` as in [Stacks, Tag 0F02], assume `BC(f, n, q)` holds and
> `BC(f, n, q + 1)` does not. Then there is a diagram
>
> ```
> X  ←--  X'  ←-h-  Y
> |f      |         |
> S  ←--  S'  ←---  Spec K
> ```
>
> with both squares cartesian, `S'` affine, integral and normal with algebraically closed function
> field, `K` algebraically closed with `Spec K ⟶ S'` dominant, and an integer `d ∣ n` with
> `R^{q+1} h_* (ℤ/dℤ)` nonzero, `ℤ/dℤ` on `Y` being the inverse image of the constant sheaf on
> `Spec K` (`Stacks.EtaleCohomology.FirstFailureDiagram.NormalFailureDiagram`). This is another
> name for
> `Stacks.EtaleCohomology.FirstFailureDiagram.normalFailureDiagram_of_not_baseChangeHolds`.

```lean
public alias normalFailureDiagram_of_firstFailure
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.88, Tag 0F01](https://stacks.math.columbia.edu/tag/0F01)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

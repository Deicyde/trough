---
declaration: section
origin: cited
lean: Stacks.Chow.properPushforwardFlatPullbackBaseChange, Stacks.Chow.flatPullback_properPushforward_comap, Stacks.Chow.flatPullback_properPushforward_of_isIso, Stacks.Chow.flatPullbackChow_chowPushforwardOfIso, Stacks.Chow.flatPullback_properPushforward_cycleAssociatedToCoherentSheaf, Stacks.Chow.flatPullback_properPushforward_cycleAssociatedToClosedSubscheme, Stacks.Chow.flatPullback_properPushforward_of_finite_support, Stacks.Chow.flatPullback_properPushforward
statement: formalized
proof: formalized
---

# 42.15 Push and pull

Section 42.15 of the Stacks Project, [Tag 02RF](https://stacks.math.columbia.edu/tag/02RF). 2 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02RG, a lemma

[Tag 02RG](https://stacks.math.columbia.edu/tag/02RG) in the Stacks Project.

**`Stacks.Chow.properPushforwardFlatPullbackBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackProperPushforward.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FlatPullbackProperPushforward.lean#L58). The attribute's comment: “the identity ON CHOW GROUPS in the four-corner form of the source -- a cartesian square with two proper legs and two flat legs of a common relative dimension r -- for an arbitrary class, with NOTHING ASSUMED: the two descents (Stacks 02S1, 02S2) are theorems here, coherence of the two direct images is Stacks 02O5 and the flat base change isomorphism is part (1) of Stacks 02KH at i = 0, which is the only degree the comparison of ordinary direct images needs”.

> In a cartesian square of schemes locally of finite type over the base of chapter 42 whose
> horizontal legs `u₀ : A₀ ⟶ B₀`, `u₁ : A₁ ⟶ B₁` are proper and whose vertical legs `d : A₁ ⟶ A₀`,
> `v : B₁ ⟶ B₀` are flat of relative dimension `r`, flat pullback of Chow classes commutes with
> proper pushforward: `v^* u₀_* α = u₁_* d^* α`.

```lean
theorem properPushforwardFlatPullbackBaseChange (C : ChowSituation.{u}) :
    ProperPushforwardFlatPullbackBaseChange C
```

**`Stacks.Chow.flatPullback_properPushforward_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ClosedImmersionBaseChange.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ClosedImmersionBaseChange.lean#L253). The attribute's comment: “the case of a closed immersion base change, on cycles”.

> **Stacks 02RG for a closed immersion base change, on cycles.** For `f : X' ⟶ X` flat of
> relative dimension `r` and `W ⊆ X` a closed subscheme, flat pullback along `f` carries the
> pushforward of a `k`-cycle on `W` to the pushforward of its flat pullback along the restriction
> `g : f^{-1}(W) ⟶ W`:
>
>   `f^*(i_* γ) = i'_*(g^* γ)`  in  `Z_{k+r}(X')`.
>
> Read at a point of `X'` in the inverse image both sides are the coefficient of `γ` at the image
> point times a flat pullback multiplicity, and the two multiplicities agree by
> `Stacks.Chow.flatPullbackWeight_comapRestrict`; off the inverse image both sides vanish, the left
> one because the support of `i_* γ` misses the image of the point.

```lean
theorem flatPullback_properPushforward_comap (C : ChowSituation.{u}) {X' X : Scheme.{u}}
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (f : X' ⟶ X) [LocallyOfFiniteType f] [Flat f] (hbase : f ≫ sX = sX') (r : ℕ)
    (hf : AlgebraicGeometry.RelativeDimension f r) (k : ℤ) (W : X.IdealSheafData)
    (γ : CycleGroup C (W.subschemeι ≫ sX) k) :
    letI := locallyOfFiniteType_comapRestrict W f
    letI := flat_comapRestrict W f
    flatPullback C sX' sX f hbase r hf k
        (properPushforward C (W.subschemeι ≫ sX) sX W.subschemeι rfl k γ) =
      properPushforward C ((W.comap f).subschemeι ≫ sX') sX' (W.comap f).subschemeι rfl
        (k + (r : ℤ))
        (flatPullback C ((W.comap f).subschemeι ≫ sX') (W.subschemeι ≫ sX) (comapRestrict W f)
          (comapRestrict_comp_base C sX' sX f hbase W) r
          (relativeDimension_comapRestrict W f hf) k γ)
```

**`Stacks.Chow.flatPullback_properPushforward_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/IsomorphismBaseChange.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/IsomorphismBaseChange.lean#L216). The attribute's comment: “the case of two isomorphism legs, on cycles”.

> **Flat pullback commutes with pushforward along two isomorphism legs, on cycles.** In a
> square
>
>   `A₁ --u₁--> B₁`
>   `|d          |v`
>   `A₀ --u₀--> B₀`
>
> over the base, with `u₀` and `u₁` isomorphisms and `d`, `v` flat of relative dimension `r`, flat
> pullback commutes with pushforward along the isomorphisms.

```lean
theorem flatPullback_properPushforward_of_isIso (C : ChowSituation.{u})
    {A₀ A₁ B₀ B₁ : Scheme.{u}} (sA₀ : A₀ ⟶ C.S) [LocallyOfFiniteType sA₀]
    (sA₁ : A₁ ⟶ C.S) [LocallyOfFiniteType sA₁] (sB₀ : B₀ ⟶ C.S) [LocallyOfFiniteType sB₀]
    (sB₁ : B₁ ⟶ C.S) [LocallyOfFiniteType sB₁]
    (u₀ : A₀ ⟶ B₀) [IsIso u₀] (hu₀ : u₀ ≫ sB₀ = sA₀)
    (u₁ : A₁ ⟶ B₁) [IsIso u₁] (hu₁ : u₁ ≫ sB₁ = sA₁)
    (d : A₁ ⟶ A₀) [LocallyOfFiniteType d] [Flat d] (hd : d ≫ sA₀ = sA₁)
    (v : B₁ ⟶ B₀) [LocallyOfFiniteType v] [Flat v] (hv : v ≫ sB₀ = sB₁)
    (hsq : d ≫ u₀ = u₁ ≫ v) (r : ℕ)
    (hdr : AlgebraicGeometry.RelativeDimension d r)
    (hvr : AlgebraicGeometry.RelativeDimension v r) (k : ℤ) (z : CycleGroup C sA₀ k) :
    flatPullback C sB₁ sB₀ v hv r hvr k (properPushforward C sA₀ sB₀ u₀ hu₀ k z) =
      properPushforward C sA₁ sB₁ u₁ hu₁ (k + (r : ℤ))
        (flatPullback C sA₁ sA₀ d hd r hdr k z)
```

**`Stacks.Chow.flatPullbackChow_chowPushforwardOfIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/IsomorphismBaseChange.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/IsomorphismBaseChange.lean#L242). The attribute's comment: “the case of two isomorphism legs”.

> **Flat pullback commutes with pushforward along two isomorphism legs, on Chow groups.** In a
> square over the base whose two horizontal legs are isomorphisms — hence automatically cartesian —
> flat pullback commutes with pushforward along the isomorphisms, on Chow groups.

```lean
theorem flatPullbackChow_chowPushforwardOfIso (C : ChowSituation.{u})
    {A₀ A₁ B₀ B₁ : Scheme.{u}} (sA₀ : A₀ ⟶ C.S) [LocallyOfFiniteType sA₀]
    (sA₁ : A₁ ⟶ C.S) [LocallyOfFiniteType sA₁] (sB₀ : B₀ ⟶ C.S) [LocallyOfFiniteType sB₀]
    (sB₁ : B₁ ⟶ C.S) [LocallyOfFiniteType sB₁]
    (u₀ : A₀ ⟶ B₀) [IsIso u₀] (hu₀ : u₀ ≫ sB₀ = sA₀)
    (u₁ : A₁ ⟶ B₁) [IsIso u₁] (hu₁ : u₁ ≫ sB₁ = sA₁)
    (d : A₁ ⟶ A₀) [LocallyOfFiniteType d] [Flat d] (hd : d ≫ sA₀ = sA₁)
    (v : B₁ ⟶ B₀) [LocallyOfFiniteType v] [Flat v] (hv : v ≫ sB₀ = sB₁)
    (hsq : d ≫ u₀ = u₁ ≫ v) (r : ℕ)
    (hdr : AlgebraicGeometry.RelativeDimension d r)
    (hvr : AlgebraicGeometry.RelativeDimension v r) (k : ℤ)
    (hfacd : FlatPullbackFactorsThroughRationalEquivalence C sA₁ sA₀ d hd r hdr k)
    (hfacv : FlatPullbackFactorsThroughRationalEquivalence C sB₁ sB₀ v hv r hvr k)
    (α : chowGroup C sA₀ k) :
    flatPullbackChow C sB₁ sB₀ v hv r hvr k hfacv
        (chowPushforwardOfIso C sA₀ sB₀ u₀ hu₀ k α) =
      chowPushforwardOfIso C sA₁ sB₁ u₁ hu₁ (k + (r : ℤ))
        (flatPullbackChow C sA₁ sA₀ d hd r hdr k hfacd α)
```

**`Stacks.Chow.flatPullback_properPushforward_cycleAssociatedToCoherentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean#L186). The attribute's comment: “the cycle identity for the cycle of a coherent sheaf; the flat base change isomorphism g^* f\_* F ≅ f'\_* (g')^* F (Stacks 02KH) is a HYPOTHESIS and is not proved here, and coherence of the two direct images (Stacks 02O5) is assumed as an instance”.

> **Stacks 02RG for the cycle of a coherent sheaf, granted flat base change for that sheaf.**
> In a fibre product diagram
>
>       X' --g'--> X
>       |          |
>       f'         f
>       v          v
>       Y' --g-->  Y
>
> of schemes locally of finite type over the base of chapter 42, with `f` proper and `g` flat of
> relative dimension `r`, let `F` be a coherent `𝒪_X`-module whose support has delta-dimension at
> most `k`. If the canonical comparison morphism `g^* f_* F ⟶ f'_* (g')^* F` is an isomorphism —
> flat base change in degree zero, Stacks 02KH, which is assumed here and not proved — then
>
> `g^* f_* [F]_k = f'_* (g')^* [F]_k`.
>
> Indeed `f_* [F]_k = [f_* F]_k` and `f'_* [(g')^* F]_{k+r} = [f'_* (g')^* F]_{k+r}` by Stacks
> 02R6, while `g^* [f_* F]_k = [g^* f_* F]_{k+r}` and `(g')^* [F]_k = [(g')^* F]_{k+r}` by Stacks
> 02RE; the two resulting cycles are the cycles of isomorphic sheaves.

```lean
theorem flatPullback_properPushforward_cycleAssociatedToCoherentSheaf
    (C : ChowSituation.{u}) {X Y X' Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r)
    (F : X.Modules) [F.IsCoherent]
    [((Scheme.Modules.pushforward f).obj F).IsCoherent]
    [((Scheme.Modules.pushforward f').obj ((Scheme.Modules.pullback g').obj F)).IsCoherent]
    (k : ℤ) (hFk : schemeDeltaDimension C ((reducedSupport F).subschemeι ≫ sX) ≤ (k : EInt))
    (hbc : IsIso ((Stacks.AlgebraicGeometry.AffinePushforward.baseChangeNatTrans
      hsq.w).app F)) :
    letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
    letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    letI : Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    flatPullback C sY' sY g hg r hgr k
        (properPushforward C sX sY f hf k (cycleAssociatedToCoherentSheaf C sX F k hFk)) =
      properPushforward C sX' sY' f'
        (by rw [← hg, ← Category.assoc, ← hsq.w, Category.assoc, hf, hg']) (k + (r : ℤ))
        (flatPullback C sX' sX g' hg' r
          (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k
          (cycleAssociatedToCoherentSheaf C sX F k hFk))
```

**`Stacks.Chow.flatPullback_properPushforward_cycleAssociatedToClosedSubscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean#L252). The attribute's comment: “steps (4) and (5) of the source proof: the cycle identity for the cycle [W] of a closed subscheme W of X, under NO integrality hypothesis on W beyond dim\_δ(W) ≤ k; the flat base change isomorphism for i\_* O\_W (Stacks 02KH) is a HYPOTHESIS and is not proved here, as is coherence of the two direct images (Stacks 02O5)”.

> **Stacks 02RG for the cycle of a closed subscheme, granted flat base change for its
> structure sheaf.** In the fibre product diagram of
> `Stacks.Chow.flatPullback_properPushforward_cycleAssociatedToCoherentSheaf`, let `i : W ⟶ X` be
> a closed subscheme with `dim_δ(W) ≤ k`. If the canonical comparison morphism
> `g^* f_* (i_* 𝒪_W) ⟶ f'_* (g')^* (i_* 𝒪_W)` is an isomorphism — Stacks 02KH, assumed and not
> proved — then
>
> `g^* f_* [W] = f'_* (g')^* [W]`  in  `Z_{k+r}(Y')`.
>
> This is step (4) of the source proof: `[W] = [𝒪_W]_k` by Stacks 02QY, so the identity is the one
> for the cycle of the coherent sheaf `i_* 𝒪_W`.

```lean
theorem flatPullback_properPushforward_cycleAssociatedToClosedSubscheme
    (C : ChowSituation.{u}) {X Y X' Y' W : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r)
    (i : W ⟶ X) [IsClosedImmersion i] (k : ℤ)
    (hW : schemeDeltaDimension C (i ≫ sX) ≤ (k : EInt))
    (hbc : IsIso ((Stacks.AlgebraicGeometry.AffinePushforward.baseChangeNatTrans hsq.w).app
      ((Scheme.Modules.pushforward i).obj (Ample.unitModule W)))) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
    letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    letI : Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    ∀ [((Scheme.Modules.pushforward f).obj
        ((Scheme.Modules.pushforward i).obj (Ample.unitModule W))).IsCoherent]
      [((Scheme.Modules.pushforward f').obj ((Scheme.Modules.pullback g').obj
        ((Scheme.Modules.pushforward i).obj (Ample.unitModule W)))).IsCoherent],
    flatPullback C sY' sY g hg r hgr k
        (properPushforward C sX sY f hf k (cycleAssociatedToClosedSubscheme C sX i k)) =
      properPushforward C sX' sY' f'
        (by rw [← hg, ← Category.assoc, ← hsq.w, Category.assoc, hf, hg']) (k + (r : ℤ))
        (flatPullback C sX' sX g' hg' r
          (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k
          (cycleAssociatedToClosedSubscheme C sX i k))
```

**`Stacks.Chow.flatPullback_properPushforward_of_finite_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean#L310). The attribute's comment: “steps (3)-(5) of the source proof for an arbitrary FINITELY SUPPORTED k-cycle (the cycle groups of chapter 42 are locally finitely supported, so this is an explicit restriction on alpha and the general case is not proved here); the flat base change isomorphisms (Stacks 02KH) and the coherence of the direct images (Stacks 02O5) are HYPOTHESES quantified over the integral closed subschemes of X, and neither is proved here”.

> **Stacks 02RG for a finitely supported cycle, granted flat base change.** In the fibre
> product diagram of
> `Stacks.Chow.flatPullback_properPushforward_cycleAssociatedToCoherentSheaf`, let `α` be a
> `k`-cycle on `X` whose support is finite. Granted, for the structure sheaf of each integral
> closed subscheme `W_x ⊆ X` with generic point `x`, coherence of the two direct images
> (Stacks 02O5) and the flat base change isomorphism (Stacks 02KH), one has
>
> `g^* f_* α = f'_* (g')^* α`  in  `Z_{k+r}(Y')`.
>
> This is steps (3) to (5) of the source proof, carried out by linearity: a finitely supported
> cycle is the finite sum `∑ n_x [W_x]` of
> `Stacks.Chow.eq_finsetSum_cycleAssociatedToIntegralComponentAt`, both sides of the identity are
> homomorphisms of abelian groups, and on each summand the identity is
> `Stacks.Chow.flatPullback_properPushforward_cycleAssociatedToClosedSubscheme`.

```lean
theorem flatPullback_properPushforward_of_finite_support
    (C : ChowSituation.{u}) {X Y X' Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r)
    (k : ℤ) (α : CycleGroup C sX k)
    (hfin : (Function.support (α.1 : X → ℤ)).Finite) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
    letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    letI : Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    (∀ x : X, ((Scheme.Modules.pushforward f).obj
        ((Scheme.Modules.pushforward (integralComponentAt x).subschemeι).obj
          (Ample.unitModule (integralComponentAt x).subscheme))).IsCoherent) →
    (∀ x : X, ((Scheme.Modules.pushforward f').obj ((Scheme.Modules.pullback g').obj
        ((Scheme.Modules.pushforward (integralComponentAt x).subschemeι).obj
          (Ample.unitModule (integralComponentAt x).subscheme)))).IsCoherent) →
    (∀ x : X, IsIso ((Stacks.AlgebraicGeometry.AffinePushforward.baseChangeNatTrans hsq.w).app
        ((Scheme.Modules.pushforward (integralComponentAt x).subschemeι).obj
          (Ample.unitModule (integralComponentAt x).subscheme)))) →
    flatPullback C sY' sY g hg r hgr k (properPushforward C sX sY f hf k α) =
      properPushforward C sX' sY' f'
        (by rw [← hg, ← Category.assoc, ← hsq.w, Category.assoc, hf, hg']) (k + (r : ℤ))
        (flatPullback C sX' sX g' hg' r
          (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k α)
```

**`Stacks.Chow.flatPullback_properPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean#L396). The attribute's comment: “steps (3)-(5) of the source proof for an ARBITRARY k-cycle alpha, with no support hypothesis on alpha: properness of f makes each fibre of f meet the support of alpha in a finite set, and the coefficient of either side at a point y of Y' depends on alpha only through the fibre over g(y), which reduces the identity to the finitely supported case; the flat base change isomorphisms (Stacks 02KH) and the coherence of the direct images (Stacks 02O5) remain HYPOTHESES quantified over the integral closed subschemes of X, and neither is proved here”.

> **Stacks 02RG for an arbitrary cycle, granted flat base change.** In the fibre product
> diagram of `Stacks.Chow.flatPullback_properPushforward_cycleAssociatedToCoherentSheaf`, let `α`
> be any `k`-cycle on `X`. Granted, for the structure sheaf of each integral closed subscheme
> `W_x ⊆ X` with generic point `x`, coherence of the two direct images (Stacks 02O5) and the flat
> base change isomorphism (Stacks 02KH), one has
>
> `g^* f_* α = f'_* (g')^* α`  in  `Z_{k+r}(Y')`.
>
> Both sides are compared coefficient by coefficient. At a point `y` of `Y'` the coefficient of the
> left-hand side is the coefficient of `f_* α` at `g(y)`, a locally finite sum over the fibre
> `f⁻¹(g(y))`, times the flat pullback weight; the coefficient of the right-hand side is a locally
> finite sum over `f'⁻¹(y)`, whose points are carried by `g'` into that same fibre because the
> square commutes. So both coefficients at `y` depend on `α` only through its values on
> `f⁻¹(g(y))`. Properness of `f` makes that fibre compact, hence makes its intersection with the
> locally finite support of `α` finite, and `Stacks.Chow.cycleRestrict` to that intersection is a
> finitely supported `k`-cycle agreeing with `α` on the fibre. The identity at `y` is therefore the
> one already proved for a finitely supported cycle,
> `Stacks.Chow.flatPullback_properPushforward_of_finite_support`.

```lean
theorem flatPullback_properPushforward
    (C : ChowSituation.{u}) {X Y X' Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r)
    (k : ℤ) (α : CycleGroup C sX k) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
    letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    letI : Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    (∀ x : X, ((Scheme.Modules.pushforward f).obj
        ((Scheme.Modules.pushforward (integralComponentAt x).subschemeι).obj
          (Ample.unitModule (integralComponentAt x).subscheme))).IsCoherent) →
    (∀ x : X, ((Scheme.Modules.pushforward f').obj ((Scheme.Modules.pullback g').obj
        ((Scheme.Modules.pushforward (integralComponentAt x).subschemeι).obj
          (Ample.unitModule (integralComponentAt x).subscheme)))).IsCoherent) →
    (∀ x : X, IsIso ((Stacks.AlgebraicGeometry.AffinePushforward.baseChangeNatTrans hsq.w).app
        ((Scheme.Modules.pushforward (integralComponentAt x).subschemeι).obj
          (Ample.unitModule (integralComponentAt x).subscheme)))) →
    flatPullback C sY' sY g hg r hgr k (properPushforward C sX sY f hf k α) =
      properPushforward C sX' sY' f'
        (by rw [← hg, ← Category.assoc, ← hsq.w, Category.assoc, hf, hg']) (k + (r : ℤ))
        (flatPullback C sX' sX g' hg' r
          (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k α)
```

**`Stacks.Chow.flatPullback_properPushforward_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChangeUnconditional.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChangeUnconditional.lean#L164).

> **Stacks 02RG, third assertion, on cycles.** Let `(S, δ)` be as in Situation 02QL, let
> ```
> X' --g'--> X
> |f'        |f
> Y' --g-->  Y
> ```
> be a fibre product diagram of schemes locally of finite type over `S`, let `f` be proper and let
> `g` be flat of relative dimension `r`. Then for every `k`-cycle `α` on `X`,
>
>   `g^* f_* α = f'_* (g')^* α`  in  `Z_{k + r}(Y')`.
>
> That `f'` is proper and `g'` flat of relative dimension `r` — the first two assertions of the tag
> — is what makes the right hand side meaningful, and is supplied by the instances the statement
> elaborates with.
>
> This is `Stacks.Chow.flatPullback_properPushforward` with its three hypotheses discharged: the
> two coherence hypotheses by Stacks 02O5 and Stacks 0EBF, the base-change isomorphism by
> `Stacks.Chow.isIso_baseChange_app_of_isProper`.

```lean
theorem flatPullback_properPushforward_of_isProper
    (C : ChowSituation.{u}) {X Y X' Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [AlgebraicGeometry.Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : CategoryTheory.IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r)
    (k : ℤ) (α : CycleGroup C sX k) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
    letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    letI : AlgebraicGeometry.Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    flatPullback C sY' sY g hg r hgr k (properPushforward C sX sY f hf k α) =
      properPushforward C sX' sY' f'
        (by rw [← hg, ← Category.assoc, ← hsq.w, Category.assoc, hf, hg']) (k + (r : ℤ))
        (flatPullback C sX' sX g' hg' r
          (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k α)
```

**`Stacks.Chow.flatPullbackChow_properChowPushforward_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChangeUnconditional.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChangeUnconditional.lean#L207).

> **Stacks 02RG on Chow groups.** In the fibre product diagram above, with `f` proper and `g`
> flat of relative dimension `r`, the flat pullback of the proper pushforward of a class agrees
> with the proper pushforward of its flat pullback:
>
>   `g^* f_* c = f'_* (g')^* c`  in  `A_{k + r}(Y')`  for every  `c ∈ A_k(X)`.
>
> This is `Stacks.Chow.flatPullbackChow_properChowPushforward` with all five of its hypotheses
> discharged: the two descent bundles by `Stacks.Chow.flatPullbackDescends` (Stacks 02S1) and
> `Stacks.Chow.properPushforwardDescends` (Stacks 02S2), and the coherence and base-change
> hypotheses exactly as for the cycle-level statement above.

```lean
theorem flatPullbackChow_properChowPushforward_of_isProper
    (C : ChowSituation.{u}) {X Y X' Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [AlgebraicGeometry.Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : CategoryTheory.IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r)
    (k : ℤ) (c : chowGroup C sX k) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
    letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    letI : AlgebraicGeometry.Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    flatPullbackChow C sY' sY g hg r hgr k (flatPullbackDescends C sY' sY g hg r hgr k)
        (properChowPushforward C sX sY f hf k (properPushforwardDescends C sX sY f hf k) c) =
      properChowPushforward C sX' sY' f'
        (comp_structureMorphism_of_isPullback sX sY sX' sY' f g g' f' hsq hf hg hg')
        (k + (r : ℤ))
        (properPushforwardDescends C sX' sY' f'
          (comp_structureMorphism_of_isPullback sX sY sX' sY' f g g' f' hsq hf hg hg')
          (k + (r : ℤ)))
        (flatPullbackChow C sX' sX g' hg' r
          (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k
          (flatPullbackDescends C sX' sX g' hg' r
            (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k) c)
```

**`Stacks.Chow.flatPullbackChow_properChowPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardChowBaseChange.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardChowBaseChange.lean#L95). The attribute's comment: “the identity ON CHOW GROUPS, for an ARBITRARY class and an ARBITRARY cartesian square, descended from the cycle identity; unlike the sibling carrier keyed to two isomorphism legs it restricts neither leg, but the 02S1/02S2 descents remain bundled HYPOTHESES, as do the flat base change isomorphisms (Stacks 02KH) and coherence of the direct images (Stacks 02O5)”.

> **Flat pullback commutes with proper pushforward on Chow groups.** In a fibre product diagram
>
>       X' --g'--> X
>       |          |
>       f'         f
>       v          v
>       Y' --g-->  Y
>
> of schemes locally of finite type over the base of chapter 42, with `f` proper and `g` flat of
> relative dimension `r`, let `c ∈ A_k(X)` be a Chow class. Assume the descents
> `Stacks.Chow.FlatPullbackDescends` and `Stacks.Chow.ProperPushforwardDescends`, and, for the
> structure sheaf of each integral closed subscheme of `X`, that its direct image along `f` and the
> direct image along `f'` of its pullback along `g'` are coherent and that the base change comparison
> `Stacks.AlgebraicGeometry.AffinePushforward.baseChangeNatTrans` is an isomorphism at it. Then
>
> `g^* f_* c = f'_* (g')^* c`  in  `A_{k+r}(Y')`.

```lean
theorem flatPullbackChow_properChowPushforward
    (C : ChowSituation.{u}) {X Y X' Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r)
    (hS1 : FlatPullbackDescends C) (hS2 : ProperPushforwardDescends C)
    (k : ℤ) (c : chowGroup C sX k) :
    letI : IsLocallyNoetherian X := LocallyOfFiniteType.isLocallyNoetherian sX
    letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
    letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    letI : Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    (∀ x : X, ((Scheme.Modules.pushforward f).obj
        ((Scheme.Modules.pushforward (integralComponentAt x).subschemeι).obj
          (Ample.unitModule (integralComponentAt x).subscheme))).IsCoherent) →
    (∀ x : X, ((Scheme.Modules.pushforward f').obj ((Scheme.Modules.pullback g').obj
        ((Scheme.Modules.pushforward (integralComponentAt x).subschemeι).obj
          (Ample.unitModule (integralComponentAt x).subscheme)))).IsCoherent) →
    (∀ x : X, IsIso ((Stacks.AlgebraicGeometry.AffinePushforward.baseChangeNatTrans hsq.w).app
        ((Scheme.Modules.pushforward (integralComponentAt x).subschemeι).obj
          (Ample.unitModule (integralComponentAt x).subscheme)))) →
    flatPullbackChow C sY' sY g hg r hgr k (hS1 sY' sY g hg r hgr k)
        (properChowPushforward C sX sY f hf k (hS2 sX sY f hf k) c) =
      properChowPushforward C sX' sY' f'
        (comp_structureMorphism_of_isPullback sX sY sX' sY' f g g' f' hsq hf hg hg')
        (k + (r : ℤ))
        (hS2 sX' sY' f'
          (comp_structureMorphism_of_isPullback sX sY sX' sY' f g g' f' hsq hf hg hg')
          (k + (r : ℤ)))
        (flatPullbackChow C sX' sX g' hg' r
          (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k
          (hS1 sX' sX g' hg' r
            (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k) c)
```

**`Stacks.Chow.flatPullback_properPushforward_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardChowBaseChangeGenuine.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardChowBaseChangeGenuine.lean#L116). The attribute's comment: “the third assertion, g^* f\_* alpha = f'\_* (g')^* alpha in Z\_\{k+r}(Y'), ON CYCLES for an ARBITRARY k-cycle alpha and an arbitrary cartesian square, with NOTHING ASSUMED: coherence of the two direct images is the proper mapping theorem Stacks 02O5 and the flat base change isomorphism is part (1) of Stacks 02KH at i = 0, both theorems of this repository; the first two assertions are registered on the base-change stability declarations”.

> **Proper pushforward commutes with flat pullback on cycles.** For a cartesian square
>
>       X' --g'--> X
>       |          |
>       f'         f
>       v          v
>       Y' --g-->  Y
>
> of schemes locally of finite type over the base of chapter 42, with `f` proper and `g` flat of
> relative dimension `r`, `g^* f_* α = f'_* (g')^* α` in `Z_{k+r}(Y')` for every `α ∈ Z_k(X)`.

```lean
theorem flatPullback_properPushforward_unconditional
    (C : ChowSituation.{u}) {X Y X' Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r)
    (k : ℤ) (α : CycleGroup C sX k) :
    letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
    letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    letI : Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    flatPullback C sY' sY g hg r hgr k (properPushforward C sX sY f hf k α) =
      properPushforward C sX' sY' f'
        (comp_structureMorphism_of_isPullback sX sY sX' sY' f g g' f' hsq hf hg hg')
        (k + (r : ℤ))
        (flatPullback C sX' sX g' hg' r
          (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k α)
```

**`Stacks.Chow.flatPullbackChow_comp_properChowPushforward_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardChowBaseChangeUnconditional.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardChowBaseChangeUnconditional.lean#L138). The attribute's comment: “the identity ON CHOW GROUPS as an equality of the two composite homomorphisms, with EVERY side condition discharged”.

> Across a cartesian square with `f` proper and `g` flat of relative dimension `r`, the
> composite of proper pushforward along `f` and flat pullback along `g` equals the composite of flat
> pullback along `g'` and proper pushforward along `f'`, as homomorphisms
> `A_k(X) ⟶ A_{k+r}(Y')`.

```lean
theorem flatPullbackChow_comp_properChowPushforward_of_isPullback
    (C : ChowSituation.{u}) {X Y X' Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r) (k : ℤ) :
    letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
    letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    letI : Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
    (flatPullbackChow C sY' sY g hg r hgr k
          (flatPullbackDescends C sY' sY g hg r hgr k)).comp
        (properChowPushforward C sX sY f hf k (properPushforwardDescends C sX sY f hf k)) =
      (properChowPushforward C sX' sY' f'
        (comp_structureMorphism_of_isPullback sX sY sX' sY' f g g' f' hsq hf hg hg')
        (k + (r : ℤ))
        (properPushforwardDescends C sX' sY' f'
          (comp_structureMorphism_of_isPullback sX sY sX' sY' f g g' f' hsq hf hg hg')
          (k + (r : ℤ)))).comp
        (flatPullbackChow C sX' sX g' hg' r
          (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k
          (flatPullbackDescends C sX' sX g' hg' r
            (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsProper.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsProper.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean#L109) (StacksFrontier): “first assertion: the base change of a proper morphism is proper”. References: EGA II (5.4.2), “more general”; EGA III (4.3.4), “more general”; EGA IV (2.7.1), “implication”; SGA 1 IX (2.4), “partial”; SGA 1 VIII (4.8), “partial”; SGA 3 VIB (10.1), “partial”; SGA 6 X (7.5), “partial”.
- [`AlgebraicGeometry.Flat.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean#L118) (StacksFrontier): “second assertion, flatness: the base change of a flat morphism is flat”. References: EGA III (7.7.2), “special case”; EGA III (7.9.7), “special case”; EGA IV (11.5.4), “necessity”; EGA IV (2.1.4); EGA IV (2.2.13), “(i)”; EGA IV (2.5.1), “special case”; EGA IV (20.6.9), “flatness of X' over S'”; EGA IV (21.15.9), “partial”; EGA IV (7.3.5), “partial”; SGA 3 III (0.13), “partial”; SGA 3 VIB (10.1), “partial”; SGA 3 VIB (11.1); SGA 3 VIB (2.1.2), “partial”; SGA 3 VIB (3.11), “fiber-flatness”; SGA 3 VIIB (1.3.3), “(iii), special case”; SGA 3 XIX (2.1); SGA 4 Vbis (3.3), “special case”; SGA 6 0 (2.9), “special case”; SGA 6 XII (2.3), “(a)”; SGA 6 XII (4.1), “(1)”; SGA 7 VII (1.3.8), “partial”.
- [`AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFiniteType_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean#L141) (StacksFrontier): “second assertion, local finite type of the base change”. References: EGA I (10.13.5), “(ii)”; EGA I (6.3.4), “clause (iv)”; EGA I (6.6.6); EGA II (3.5.5), “partial”; EGA IV (1.3.4); EGA IV (2.7.1), “(iii)”; SGA 3 VIB (2.1.2), “partial”.
- [`AlgebraicGeometry.RelativeDimension.of_isPullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FibreDimension/BaseChange.lean#L74), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardBaseChange.lean#L150) (StacksFrontier): “second assertion, relative dimension: the base change of a morphism of relative dimension r again has relative dimension r”.

## Tag 02RH, a lemma

[Tag 02RH](https://stacks.math.columbia.edu/tag/02RH) in the Stacks Project.

**`Stacks.Chow.properPushforward_flatPullback_of_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFreeFibreDegree.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFreeFibreDegree.lean#L141). The attribute's comment: “push-pull formula”.

> **Stacks 02RH, the second assertion.** For `f : X ⟶ Y` finite locally free of degree `d` over
> the base,
>
>   `f_* f^* α = d α`   in `Z_k(Y)`.
>
> The statement transports the left hand side along the equality `k + 0 = k` of delta-dimensions,
> which is the degree that pullback and pushforward along `f` produce; that equality is taken as a
> hypothesis so that the statement typechecks, exactly as in
> `Stacks.Chow.properPushforward_flatPullback`.
>
> This is `Stacks.Chow.properPushforward_flatPullback` with its fibre-degree hypothesis discharged
> by `Stacks.Chow.fibreDegreeIsRank_of_isFiniteLocallyFreeOfRank`.

```lean
theorem properPushforward_flatPullback_of_isFiniteLocallyFreeOfRank (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) (d : ℕ)
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank f d] (hbase : f ≫ sY = sX) (k : ℤ)
    (hcast : k + ((0 : ℕ) : ℤ) = k) (α : CycleGroup C sY k) :
    letI : LocallyOfFiniteType f :=
      Stacks.Morphisms.locallyOfFiniteType_of_isFiniteLocallyFreeOfRank f d
    letI : Flat f := Stacks.Morphisms.flat_of_isFiniteLocallyFreeOfRank f d
    letI : IsProper f := Stacks.Morphisms.isProper_of_isFiniteLocallyFreeOfRank f d
    (hcast ▸ properPushforward C sX sY f hbase (k + ((0 : ℕ) : ℤ))
          (flatPullback C sX sY f hbase 0
            (Stacks.Morphisms.relativeDimension_zero_of_isFiniteLocallyFreeOfRank f d) k α) :
        CycleGroup C sY k) = (d : ℤ) • α
```

Declarations registered for the tag:

- [`Stacks.Morphisms.isProper_of_isFiniteLocallyFreeOfRank`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeProper.lean#L84), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean#L126) (StacksFrontier): “properness”.
- [`Stacks.Morphisms.flat_of_isFiniteLocallyFreeOfRank`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeProper.lean#L91), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean#L127) (StacksFrontier): “flatness”.
- [`Stacks.Morphisms.relativeDimension_zero_of_isFiniteLocallyFreeOfRank`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeProper.lean#L98), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean#L128) (StacksFrontier): “relative dimension zero”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.15, Tag 02RF](https://stacks.math.columbia.edu/tag/02RF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

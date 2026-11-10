---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.etaleLocalBaseChange, Stacks.EtaleCohomology.smallEtaleSetsBaseChange, Stacks.EtaleCohomology.isIso_smallEtaleSetsBaseChange_of_isIso_local, Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_paste, Stacks.EtaleCohomology.etaleAbelianDerivedBaseChange_isIso_of_comp, Stacks.EtaleCohomology.LimitBaseChange.isPullback_limitSquare, Stacks.EtaleCohomology.LimitBaseChange.isIso_higherBaseChangeMapAb_limit, Stacks.EtaleCohomology.LimitBaseChange.isIso_higherBaseChangeMapAb_limit_of_isLimit
statement: formalized
proof: formalized
---

# 59.86 Preliminaries on base change

Section 59.86 of the Stacks Project, [Tag 0EZQ](https://stacks.math.columbia.edu/tag/0EZQ). 6 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EZR, a lemma

[Tag 0EZR](https://stacks.math.columbia.edu/tag/0EZR) in the Stacks Project.

**`Stacks.EtaleCohomology.etaleLocalBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/EtaleLocalBaseChangeThreeParts.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/EtaleLocalBaseChangeThreeParts.lean#L156). The attribute's comment: “parts (1), (2) and (3), as the conjunction of the three implications”.

> **Stacks 0EZR.**  Let
>
> ```
> X <--h-- Y
> |f       |e
> S <--g-- T
> ```
>
> be a cartesian square of schemes, let `{Uᵢ → X}` be an étale covering of `X` such that each
> composite `Uᵢ → X → S` factors as `Uᵢ → Vᵢ → S` with `Vᵢ → S` étale, and let
>
> ```
> Uᵢ <--hᵢ-- Yᵢ
> |fᵢ        |eᵢ
> Vᵢ <--gᵢ-- Tᵢ
> ```
>
> be the induced cartesian squares, with `Yᵢ = Uᵢ ×_X Y` and `Tᵢ = Vᵢ ×_S T`.  Let `F` be a sheaf
> of sets on the small étale site of `T`, let `𝓖` be an abelian sheaf on it, let `K` be an object of
> its unbounded derived category, and write `F|ᵢ`, `𝓖|ᵢ` and `K|ᵢ` for the inverse images along
> `Tᵢ ⟶ T`.  Then:
>
> 1. if `fᵢ^{-1} g_{i,*} F|ᵢ ⟶ h_{i,*} eᵢ^{-1} F|ᵢ` is an isomorphism for every `i`, so is
>    `f^{-1} g_* F ⟶ h_* e^{-1} F`;
> 2. if `fᵢ^{-1} Rg_{i,*} K|ᵢ ⟶ Rh_{i,*} eᵢ^{-1} K|ᵢ` is an isomorphism for every `i`, so is
>    `f^{-1} Rg_* K ⟶ Rh_* e^{-1} K`;
> 3. for every degree `q`, if `fᵢ^{-1} R^q g_{i,*} 𝓖|ᵢ ⟶ R^q h_{i,*} eᵢ^{-1} 𝓖|ᵢ` is an
>    isomorphism for every `i`, so is `f^{-1} R^q g_* 𝓖 ⟶ R^q h_* e^{-1} 𝓖`.
>
> The hypotheses are exactly the source's: the square is cartesian, the family `{Uᵢ → X}` is an
> étale covering, each `Uᵢ → S` factors through an étale `Vᵢ → S`, and the two families of induced
> squares are cartesian.  Nothing is assumed of `f`, `g`, `h`, `e` beyond that, and the coefficients
> are arbitrary sheaves of sets, arbitrary abelian sheaves and arbitrary objects of the unbounded
> derived category.
>
> The three parts are proved in
> `Stacks.EtaleCohomology.isIso_smallEtaleSetsBaseChange_app_of_isIso_local`,
> `Stacks.EtaleCohomology.isIso_etaleAbelianDerivedBaseChange_app_of_isIso_local` and
> `Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_isIso_local`; each of them restricts
> the base change map of the outer square to `Uᵢ`, compares it there with the base change map of
> the `i`-th local square through the two decompositions of the rectangle `Uᵢ ⟶ X ⟶ S`, and
> concludes by the locality of invertibility on the small étale site.

```lean
theorem etaleLocalBaseChange
    (D : EtaleLocalBaseChangeData.{u, z, _, _} (Type (max (u + 1) v)))
    (𝓖 : Sheaf D.T.smallEtaleTopology Ab.{u + 1})
    (K : DerivedCategory (Sheaf D.T.smallEtaleTopology Ab.{u + 1})) :
    ((∀ i : D.I, IsIso ((smallEtaleSetsBaseChange.{u, v} (D.e_i i) (D.h_i i) (D.g_i i)
          (D.f_i i) (D.local_cartesian i).w.symm).app
            ((smallEtaleInverseImage.{u, v} (D.toT_i i)).obj D.F))) →
        IsIso ((smallEtaleSetsBaseChange.{u, v} D.e D.h D.g D.f
          D.cartesian.w.symm).app D.F)) ∧
      ((∀ i : D.I, IsIso ((etaleAbelianDerivedBaseChange.{u, 0} (D.g_i i) (D.f_i i) (D.e_i i)
            (D.h_i i) (D.local_cartesian i).w.symm).app
              ((etaleAbelianDerivedInverseImage.{u, 0} (D.toT_i i)).obj K))) →
          IsIso ((etaleAbelianDerivedBaseChange.{u, 0} D.g D.f D.e D.h
            D.cartesian.w.symm).app K)) ∧
        ∀ q : ℕ, (∀ i : D.I, IsIso ((higherBaseChangeMapAb (D.f_i i) (D.g_i i) (D.h_i i)
            (D.e_i i) (D.local_cartesian i).w q).app
              ((smallEtalePullbackAb (D.toT_i i)).obj 𝓖))) →
          IsIso ((higherBaseChangeMapAb D.f D.g D.h D.e D.cartesian.w q).app 𝓖)
```

**`Stacks.EtaleCohomology.smallEtaleSetsBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/OrdinaryLocality.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/OrdinaryLocality.lean#L283). The attribute's comment: “the set-valued base change map and the locality calculus only: the map g^{-1} f_* to f'_* (g')^{-1} for sheaves of SETS, which the library previously had only for abelian coefficients, together with the hypothesis bundle and the option-free mate calculus the locality argument runs on. NONE of the tag's three clauses is proved here. Clause (1) is blocked at rightSquare_app by a kernel defeq the elaborator cannot reduce because getLimitCone is not exposed by the module system; clause (3) sits on top of it; clause (2) has no proof content anywhere in the repository.”.

> **The base change map `g^{-1} f_* ⟶ f'_* (g')^{-1}` for sheaves of sets** on the small étale
> sites of a commutative square `g' ≫ f = f' ≫ g` of schemes: the mate, under the two
> inverse-image/direct-image adjunctions, of the identification of the two composite direct images
> around the square.

```lean
public def smallEtaleSetsBaseChange {X' X Y' Y : Scheme.{u}}
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (f : X ⟶ Y) (g : Y' ⟶ Y)
    (w : g' ≫ f = f' ≫ g) :
    smallEtaleDirectImage.{u, v} f ⋙ smallEtaleInverseImage.{u, v} g ⟶
      smallEtaleInverseImage.{u, v} g' ⋙ smallEtaleDirectImage.{u, v} f'
```

**`Stacks.EtaleCohomology.isIso_smallEtaleSetsBaseChange_of_isIso_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/OrdinaryLocalityCriterion.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/OrdinaryLocalityCriterion.lean#L317). The attribute's comment: “clause (1), for sheaves of SETS, which is the generality in which the source states it: the étale-local criterion for the ordinary base change map. Clause (2), the analogue for an object of the unbounded derived category, and clause (3), the analogue for the higher direct images, are not proved here.”.

> **Stacks 0EZR, part (1): the base change map of sheaves of sets may be checked étale-locally
> on `X`.**  Let
>
> ```
> X <--h-- Y
> |f       |e
> S <--g-- T
> ```
>
> be a cartesian square of schemes, let `{Uᵢ → X}` be an étale covering such that each `Uᵢ → S`
> factors as `Uᵢ → Vᵢ → S` with `Vᵢ → S` étale, and form the induced cartesian squares with
> `Yᵢ = Uᵢ ×_X Y` and `Tᵢ = Vᵢ ×_S T`.  If for every `i` the base change map
> `fᵢ^{-1} g_{i,*} Fᵢ ⟶ h_{i,*} e_i^{-1} Fᵢ` of the `i`-th local square is an isomorphism, where
> `Fᵢ` is the inverse image of `F` on `Tᵢ`, then the base change map
> `f^{-1} g_* F ⟶ h_* e^{-1} F` of the outer square is an isomorphism.

```lean
public theorem isIso_smallEtaleSetsBaseChange_of_isIso_local
    (D : EtaleLocalBaseChangeData.{u, z, max (u + 1) v, (max (u + 1) v) + 1}
      (Type (max (u + 1) v)))
    (hlocal : ∀ i : D.I,
      IsIso ((smallEtaleSetsBaseChange.{u, v} (D.e_i i) (D.h_i i) (D.g_i i) (D.f_i i)
        (D.local_cartesian i).w.symm).app
        ((smallEtaleInverseImage.{u, v} (D.toT_i i)).obj D.F))) :
    IsIso ((smallEtaleSetsBaseChange.{u, v} D.e D.h D.g D.f D.cartesian.w.symm).app D.F)
```

## Tag 0EZS, a lemma

[Tag 0EZS](https://stacks.math.columbia.edu/tag/0EZS) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_of_paste`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/SmallEtaleHigherBaseChangePasting.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/SmallEtaleHigherBaseChangePasting.lean#L524). The attribute's comment: “the abelian half: for an abelian sheaf F on T_étale and a degree q, if f⁻¹R^qg_*F → R^qh_*e⁻¹F and i⁻¹R^qh_*e⁻¹F → R^qj_*k⁻¹e⁻¹F are isomorphisms then (f∘i)⁻¹R^qg_*F → R^qj_*(e∘k)⁻¹F is an isomorphism; the derived statement of the same tag is `etaleAbelianDerivedBaseChange_isIso_of_comp`”.

> **Base change maps of a rectangle of squares.** Consider a tower of two commutative squares
> of schemes
> ```
> X₂ --v₂--> X₁ --v₁--> X₀
> |g₂         |g₁        |g₀
> v           v          v
> S₂ --u₂--> S₁ --u₁--> S₀
> ```
> written in the notation of the Stacks Project by `u₁ = f`, `v₁ = e`, `g₀ = g`, `g₁ = h`,
> `u₂ = i`, `v₂ = k`, `g₂ = j`, let `F` be an abelian sheaf on the small étale site of `X₀` and let
> `q` be a degree.
> If the degree-`q` base change maps `f⁻¹ R^q g_* F ⟶ R^q h_* e⁻¹ F` of the lower square and
> `i⁻¹ R^q h_* (e⁻¹ F) ⟶ R^q j_* k⁻¹ (e⁻¹ F)` of the upper square are isomorphisms, then so is the
> degree-`q` base change map `(i ≫ f)⁻¹ R^q g_* F ⟶ R^q j_* (k ≫ e)⁻¹ F` of the outer rectangle.
> Nothing is assumed of the squares beyond commutativity: neither need be cartesian, and the
> degree `q` is arbitrary — each degree is a separate statement, with the same degree in the
> hypotheses and in the conclusion.

```lean
public theorem isIso_higherBaseChangeMapAb_app_of_paste (g₀ : X₀ ⟶ S₀) (g₁ : X₁ ⟶ S₁)
    (g₂ : X₂ ⟶ S₂) (u₁ : S₁ ⟶ S₀) (u₂ : S₂ ⟶ S₁) (v₁ : X₁ ⟶ X₀) (v₂ : X₂ ⟶ X₁)
    (w₁ : g₁ ≫ u₁ = v₁ ≫ g₀) (w₂ : g₂ ≫ u₂ = v₂ ≫ g₁) (q : ℕ)
    (F : Sheaf (smallEtaleTopology X₀) Ab.{u + 1})
    (h₁ : IsIso ((higherBaseChangeMapAb u₁ g₀ g₁ v₁ w₁ q).app F))
    (h₂ : IsIso ((higherBaseChangeMapAb u₂ g₁ g₂ v₂ w₂ q).app
      ((smallEtalePullbackAb v₁).obj F))) :
    IsIso ((higherBaseChangeMapAb (u₂ ≫ u₁) g₀ g₂ (v₂ ≫ v₁)
      (smallEtaleRectangle_comm g₀ g₁ g₂ u₁ u₂ v₁ v₂ w₁ w₂) q).app F)
```

**`Stacks.EtaleCohomology.etaleAbelianDerivedBaseChange_isIso_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/BaseChangeMate.lean, line 902](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/BaseChangeMate.lean#L902). The attribute's comment: “the derived half: for K in D(T_étale), if f⁻¹Rg_*K → Rh_*e⁻¹K and i⁻¹Rh_*e⁻¹K → Rj_*k⁻¹e⁻¹K are isomorphisms then (f∘i)⁻¹Rg_*K → Rj_*(e∘k)⁻¹K is an isomorphism; the R^q statement of the same tag is not covered here”.

> Consider a tower of two commutative squares of schemes
> ```
> W <--j-- Z
> |i       |k
> X <--h-- Y
> |f       |e
> S <--g-- T
> ```
> and `K` in `D(T_étale)`.  If the base change maps `f⁻¹ Rg_* K ⟶ Rh_* e⁻¹ K` and
> `i⁻¹ Rh_* e⁻¹ K ⟶ Rj_* k⁻¹ e⁻¹ K` of the two squares are isomorphisms, then so is the base change
> map `(i ≫ f)⁻¹ Rg_* K ⟶ Rj_* (k ≫ e)⁻¹ K` of the outer rectangle.

```lean
public theorem etaleAbelianDerivedBaseChange_isIso_of_comp (f : X ⟶ S) (g : T ⟶ S) (h : Y ⟶ X)
    (e : Y ⟶ T) (i : W ⟶ X) (j : Z ⟶ W) (k : Z ⟶ Y)
    (sq₁ : e ≫ g = h ≫ f) (sq₂ : k ≫ h = j ≫ i)
    (a : W ⟶ S) (ha : a = i ≫ f) (b : Z ⟶ T) (hb : b = k ≫ e) (hyp : b ≫ g = j ≫ a)
    (K : DerivedCategory (Sheaf T.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}))
    (h₁ : IsIso ((etaleAbelianDerivedBaseChange.{u, v} g f e h sq₁).app K))
    (h₂ : IsIso ((etaleAbelianDerivedBaseChange.{u, v} h i k j sq₂).app
      ((etaleAbelianDerivedInverseImage.{u, v} e).obj K))) :
    IsIso ((etaleAbelianDerivedBaseChange.{u, v} g a b j hyp).app K)
```

## Tag 0EZT, a lemma

[Tag 0EZT](https://stacks.math.columbia.edu/tag/0EZT) in the Stacks Project.

**`Stacks.EtaleCohomology.LimitBaseChange.isPullback_limitSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChange.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChange.lean#L138). The attribute's comment: “the square on the limits of an inverse system of cartesian squares is cartesian”.

> **The square on the limits is cartesian**, the assertion of the setup of Stacks 0EZT. A
> morphism to `X` and a morphism to `T` agreeing over `S` induce, level by level, a morphism to
> `Y_i` through the cartesian square at `i`; these are compatible with the transitions because the
> two legs of the square at a larger index determine a morphism, so they define a morphism to
> `Y = lim Y_i`, and the same two uniqueness statements make it the unique one.

```lean
theorem isPullback_limitSquare (hcX : IsLimit cX) (hcS : IsLimit cS) (hcT : IsLimit cT)
    (hcY : IsLimit cY)
    (hfL : ∀ i : Iᵒᵖ, fL ≫ cS.π.app i = cX.π.app i ≫ f.app i)
    (hgL : ∀ i : Iᵒᵖ, gL ≫ cS.π.app i = cT.π.app i ≫ g.app i)
    (hhL : ∀ i : Iᵒᵖ, hL ≫ cX.π.app i = cY.π.app i ≫ h.app i)
    (heL : ∀ i : Iᵒᵖ, eL ≫ cT.π.app i = cY.π.app i ≫ e.app i)
    (hsq : ∀ i : Iᵒᵖ, IsPullback (h.app i) (e.app i) (f.app i) (g.app i)) :
    IsPullback hL eL fL gL
```

**`Stacks.EtaleCohomology.LimitBaseChange.isIso_higherBaseChangeMapAb_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChange.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChange.lean#L306). The attribute's comment: “conclusion (2): base change for the higher direct images passes to the limit”.

> **Conclusion (2) of Stacks 0EZT.** Let `(ℱ_i, φ_{i'i})` be a system of abelian sheaves on
> `(T_i)` and let `ℱ` on `T` be a sheaf whose higher direct images along the limit are presented,
> as in Stacks 0EYM, as the colimits of the `s_i^{-1}R^q g_{i,*}ℱ_i` and of the
> `r_i^{-1}R^q h_{i,*}e_i^{-1}ℱ_i`, compatibly with the levelwise base change maps. If the base
> change map of every level is an isomorphism, so is the base change map of the limit square.

```lean
theorem isIso_higherBaseChangeMapAb_limit
    (w : ∀ i : Iᵒᵖ, h.app i ≫ f.app i = e.app i ≫ g.app i) (wL : hL ≫ fL = eL ≫ gL)
    (hfL : ∀ i : Iᵒᵖ, fL ≫ cS.π.app i = cX.π.app i ≫ f.app i)
    (𝓕 : Sheaf (smallEtaleTopology cT.pt) Ab.{u + 1})
    (Kg : I ⥤ Sheaf (smallEtaleTopology cS.pt) Ab.{u + 1})
    (ρg : ∀ i : I, Kg.obj i ≅ sourceTerm g cS F q (Opposite.op i))
    (κg : Kg ⟶ (Functor.const I).obj
      (((smallEtalePushforwardAb gL).rightDerived q).obj 𝓕))
    (hκg : IsColimit (Cocone.mk _ κg))
    (Kh : I ⥤ Sheaf (smallEtaleTopology cX.pt) Ab.{u + 1})
    (ρh : ∀ i : I, Kh.obj i ≅ targetTerm h e cX F q (Opposite.op i))
    (κh : Kh ⟶ (Functor.const I).obj
      (((smallEtalePushforwardAb hL).rightDerived q).obj ((smallEtalePullbackAb eL).obj 𝓕)))
    (hκh : IsColimit (Cocone.mk _ κh))
    (α : Kg ⋙ smallEtalePullbackAb fL ⟶ Kh)
    (hα : ∀ i : I, (smallEtalePullbackAb fL).map (ρg i).hom ≫
      stageComparison f g h e cX cS fL F q w hfL (Opposite.op i) = α.app i ≫ (ρh i).hom)
    (hκ : ∀ i : I, (smallEtalePullbackAb fL).map (κg.app i) ≫
      (higherBaseChangeMapAb fL gL hL eL wL q).app 𝓕 = α.app i ≫ κh.app i)
    (hstage : ∀ i : Iᵒᵖ,
      IsIso ((higherBaseChangeMapAb (f.app i) (g.app i) (h.app i) (e.app i) (w i) q).app
        (F.obj i))) :
    IsIso ((higherBaseChangeMapAb fL gL hL eL wL q).app 𝓕)
```

**`Stacks.EtaleCohomology.LimitBaseChange.isIso_higherBaseChangeMapAb_limit_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeColimit.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeColimit.lean#L525). The attribute's comment: “conclusion (2): if base change for `R^q` holds at every level of the system of cartesian squares, it holds for the limit square”.

> **Conclusion (2) of Stacks 0EZT.** Let `I` be a directed set and let
> `(X_i, Y_i, S_i, T_i, f_i, h_i, e_i, g_i)` be an inverse system of cartesian squares of schemes
> with affine transition morphisms and with `g_i` quasi-compact and quasi-separated, with limit
> square `(X, Y, S, T, f, h, e, g)`. Let `(ℱ_i, φ_{i'i})` be a system of abelian sheaves on
> `(T_i)` and `ℱ = colim p_i⁻¹ℱ_i`. If the base change map
> `f_i⁻¹R^q g_{i, *}ℱ_i ⟶ R^q h_{i, *}e_i⁻¹ℱ_i` is an isomorphism for every `i`, then so is
> `f⁻¹R^q g_*ℱ ⟶ R^q h_*e⁻¹ℱ`.
>
> The limit morphisms are any morphisms `f`, `g`, `h`, `e` satisfying the equations of the
> projection squares, and `ℱ = colim p_i⁻¹ℱ_i` is given by maps `ι_i : p_i⁻¹ℱ_i ⟶ ℱ` compatible with
> the transition maps and enjoying the universal property of the colimit.

```lean
theorem isIso_higherBaseChangeMapAb_limit_of_isLimit [IsDirected I (· ≤ ·)] [Nonempty I]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DX.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DS.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DT.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DY.map a)]
    [∀ i, QuasiCompact (g.app i)] [∀ i, QuasiSeparated (g.app i)]
    (hsq : ∀ i : Iᵒᵖ, IsPullback (h.app i) (e.app i) (f.app i) (g.app i))
    (hcX : IsLimit cX) (hcS : IsLimit cS) (hcT : IsLimit cT) (hcY : IsLimit cY)
    (gL : cT.pt ⟶ cS.pt) (hL : cY.pt ⟶ cX.pt)
    (hgL : ∀ i : Iᵒᵖ, gL ≫ cS.π.app i = cT.π.app i ≫ g.app i)
    (hhL : ∀ i : Iᵒᵖ, hL ≫ cX.π.app i = cY.π.app i ≫ h.app i)
    (𝓕 : Sheaf (smallEtaleTopology cT.pt) Ab.{u + 1})
    (ι : ∀ i : Iᵒᵖ, (smallEtalePullbackAb (cT.π.app i)).obj (F.obj i) ⟶ 𝓕)
    (hι : IsPullbackCocone cT F ι) (hpres : IsPullbackColimitPresentation cT 𝓕 F ι)
    (hstage : ∀ i : Iᵒᵖ, IsIso ((higherBaseChangeMapAb (f.app i) (g.app i) (h.app i) (e.app i)
      (hsq i).w q).app (F.obj i))) :
    IsIso ((higherBaseChangeMapAb fL gL hL eL
      (limitSquare_comm f g h e cX cS cT cY fL gL hL eL hcS hfL hgL hhL heL fun i => (hsq i).w)
        q).app 𝓕)
```

**`Stacks.EtaleCohomology.LimitSetBaseChange.isIso_smallEtaleSetBaseChange_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeDirectImageSet.lean, line 588](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeDirectImageSet.lean#L588). The attribute's comment: “conclusion (1), at the source's hypotheses: for an inverse system over a directed set of cartesian squares of schemes with affine transition morphisms and quasi-compact quasi-separated `g_i`, with limit square `(f, g, h, e)`, and a system of sheaves of sets `ℱ_i` on the `T_i` (Tag 0EZL) with `ℱ = colim p_i^{-1}ℱ_i`, if every base change map `f_i^{-1}g_{i,*}ℱ_i ⟶ h_{i,*}e_i^{-1}ℱ_i` of sheaves of sets (`Stacks.EtaleCohomology.smallEtaleSetBaseChange`) is an isomorphism then so is `f^{-1}g_*ℱ ⟶ h_*e^{-1}ℱ`. Together with `Stacks.EtaleCohomology.LimitBaseChange.isIso_higherBaseChangeMapAb_of_isLimit`, conclusion (2), this covers the tag.”.

> **[Stacks, Tag 0EZT] (1): base change for the direct images of sheaves of sets passes to the
> limit.** Let `I` be a directed set and let `(X_i ← Y_i, S_i ← T_i)` be an inverse system over `I`
> of cartesian squares of schemes `h_i ≫ f_i = e_i ≫ g_i`, with affine transition morphisms and with
> every `g_i` quasi-compact and quasi-separated. Let `X, S, T, Y` be the limits, with the limit
> morphisms `f, g, h, e` characterised by `f ≫ s_i = r_i ≫ f_i`, `g ≫ s_i = p_i ≫ g_i`,
> `h ≫ r_i = q_i ≫ h_i` and `e ≫ p_i = q_i ≫ e_i`. Let `(ℱ_i, φ_{i'i})` be a system of sheaves of
> sets on `(T_i)` (Stacks 0EZL) and let `ℱ = colim p_i^{-1}ℱ_i` on `T`, presented by legs
> `ι_i : p_i^{-1}ℱ_i ⟶ ℱ`. If for every `i` the base change map
> `f_i^{-1}g_{i,*}ℱ_i ⟶ h_{i,*}e_i^{-1}ℱ_i` of sheaves of sets is an isomorphism, then so is the base
> change map `f^{-1}g_*ℱ ⟶ h_*e^{-1}ℱ` of the limit square.

```lean
theorem isIso_smallEtaleSetBaseChange_of_isLimit
    (hsq : ∀ i : Iᵒᵖ, IsPullback (h.app i) (e.app i) (f.app i) (g.app i))
    (hcX : IsLimit cX) (hcS : IsLimit cS) (hcT : IsLimit cT) (hcY : IsLimit cY)
    (hfL : ∀ i : Iᵒᵖ, fL ≫ cS.π.app i = cX.π.app i ≫ f.app i)
    (hgL : ∀ i : Iᵒᵖ, gL ≫ cS.π.app i = cT.π.app i ≫ g.app i)
    (hhL : ∀ i : Iᵒᵖ, hL ≫ cX.π.app i = cY.π.app i ≫ h.app i)
    (heL : ∀ i : Iᵒᵖ, eL ≫ cT.π.app i = cY.π.app i ≫ e.app i)
    (𝓕 : Sheaf (smallEtaleTopology cT.pt) (Type (u + 1)))
    (F : EtaleSheafSystem DT (Type (u + 1)))
    (ι : ∀ i : Iᵒᵖ, (etalePullback (cT.π.app i) (Type (u + 1))).obj (F.obj i) ⟶ 𝓕)
    (hι : ∀ ⦃i j : Iᵒᵖ⦄ (a : i ⟶ j),
      (Adjunction.leftAdjointCompIso (systemAdjunction DT (Type (u + 1)) a)
          (etaleAdjunction (cT.π.app i) (Type (u + 1)))
          (etaleAdjunction (cT.π.app j) (Type (u + 1)))
          (coneProjectionComp (Type (u + 1)) cT a)).inv.app (F.obj j) ≫
        (etalePullback (cT.π.app i) (Type (u + 1))).map (F.map a) ≫ ι i = ι j)
    (hpres : IsSetPullbackColimitPresentation cT F 𝓕 ι)
    (hstage : ∀ i : Iᵒᵖ,
      IsIso ((smallEtaleSetBaseChange.{u, 0} (e.app i) (h.app i) (g.app i) (f.app i)
        (hsq i).w.symm).app (F.obj i))) :
    IsIso ((smallEtaleSetBaseChange.{u, 0} eL hL gL fL
      (LimitBaseChange.limitSquare_comm f g h e cX cS cT cY fL gL hL eL hcS hfL hgL hhL heL
        fun i => (hsq i).w).symm).app 𝓕)
```

**`Stacks.EtaleCohomology.LimitBaseChange.isIso_higherBaseChangeMapAb_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeHigherDirectImage.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeHigherDirectImage.lean#L339). The attribute's comment: “conclusion (2), at the source's hypotheses: for an inverse system over a directed set of cartesian squares of schemes with affine transition morphisms and quasi-compact quasi-separated `g_i`, with limit square `(f, g, h, e)`, and a system of abelian sheaves `ℱ_i` on the `T_i` with `ℱ = colim p_i^{-1}ℱ_i`, if every base change map `f_i^{-1}R^q g_{i,*}ℱ_i ⟶ R^q h_{i,*}e_i^{-1}ℱ_i` is an isomorphism then so is `f^{-1}R^q g_*ℱ ⟶ R^q h_*e^{-1}ℱ`. Together with `Stacks.EtaleCohomology.LimitSetBaseChange.isIso_smallEtaleSetBaseChange_of_isLimit`, conclusion (1), this covers the tag.”.

> **[Stacks, Tag 0EZT] (2): base change for the higher direct images passes to the limit.**
> Let `I` be a directed set and let `(X_i ← Y_i, S_i ← T_i)` be an inverse system over `I` of
> cartesian squares of schemes `h_i ≫ f_i = e_i ≫ g_i`, with affine transition morphisms and with
> every `g_i` quasi-compact and quasi-separated. Let `X, S, T, Y` be the limits, with the limit
> morphisms `f, g, h, e` characterised by `f ≫ s_i = r_i ≫ f_i`, `g ≫ s_i = p_i ≫ g_i`,
> `h ≫ r_i = q_i ≫ h_i` and `e ≫ p_i = q_i ≫ e_i`. Let `(ℱ_i, φ_{i'i})` be a system of abelian
> sheaves on `(T_i)` (Stacks 0EZL) and let `ℱ = colim p_i^{-1}ℱ_i` on `T`, presented by legs
> `ι_i : p_i^{-1}ℱ_i ⟶ ℱ`. If for every `i` the base change map
> `f_i^{-1}R^q g_{i,*}ℱ_i ⟶ R^q h_{i,*}e_i^{-1}ℱ_i` is an isomorphism, then so is the base change
> map `f^{-1}R^q g_*ℱ ⟶ R^q h_*e^{-1}ℱ` of the limit square.

```lean
theorem isIso_higherBaseChangeMapAb_of_isLimit
    (hsq : ∀ i : Iᵒᵖ, IsPullback (h.app i) (e.app i) (f.app i) (g.app i))
    (hcX : IsLimit cX) (hcS : IsLimit cS) (hcT : IsLimit cT) (hcY : IsLimit cY)
    (hfL : ∀ i : Iᵒᵖ, fL ≫ cS.π.app i = cX.π.app i ≫ f.app i)
    (hgL : ∀ i : Iᵒᵖ, gL ≫ cS.π.app i = cT.π.app i ≫ g.app i)
    (hhL : ∀ i : Iᵒᵖ, hL ≫ cX.π.app i = cY.π.app i ≫ h.app i)
    (heL : ∀ i : Iᵒᵖ, eL ≫ cT.π.app i = cY.π.app i ≫ e.app i) (q : ℕ)
    (𝓕 : Sheaf (smallEtaleTopology cT.pt) Ab.{u + 1})
    (F : EtaleSheafSystem DT Ab.{u + 1})
    (ι : ∀ i : Iᵒᵖ, (smallEtalePullbackAb (cT.π.app i)).obj (F.obj i) ⟶ 𝓕)
    (hι : ∀ {i j : Iᵒᵖ} (a : i ⟶ j),
      (conePullbackComp cT a).inv.app (F.obj j) ≫
        (smallEtalePullbackAb (cT.π.app i)).map (F.map a) ≫ ι i = ι j)
    (hpres : IsPullbackColimitPresentation cT 𝓕 F ι)
    (hstage : ∀ i : Iᵒᵖ,
      IsIso ((higherBaseChangeMapAb (f.app i) (g.app i) (h.app i) (e.app i) (hsq i).w q).app
        (F.obj i))) :
    IsIso ((higherBaseChangeMapAb fL gL hL eL
      (limitSquare_comm f g h e cX cS cT cY fL gL hL eL hcS hfL hgL hhL heL fun i => (hsq i).w)
      q).app 𝓕)
```

**`Stacks.EtaleCohomology.LimitBaseChange.isIso_smallEtaleSheafBaseChange_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeSetsColimit.lean, line 408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeSetsColimit.lean#L408). The attribute's comment: “conclusion (1): if base change for sheaves of sets holds at every level of the system of cartesian squares, it holds for the limit square”.

> **Conclusion (1) of Stacks 0EZT.** Let `I` be a directed set and let
> `(X_i, Y_i, S_i, T_i, f_i, h_i, e_i, g_i)` be an inverse system of cartesian squares of schemes
> with affine transition morphisms and with `g_i` quasi-compact and quasi-separated, with limit
> square `(X, Y, S, T, f, h, e, g)`. Let `(ℱ_i, φ_{i'i})` be a system of sheaves of sets on `(T_i)`
> and `ℱ = colim p_i⁻¹ℱ_i`. If the base change map `f_i⁻¹g_{i, *}ℱ_i ⟶ h_{i, *}e_i⁻¹ℱ_i` is an
> isomorphism for every `i`, then so is `f⁻¹g_*ℱ ⟶ h_*e⁻¹ℱ`.
>
> The limit morphisms are any morphisms `f`, `g`, `h`, `e` satisfying the equations of the
> projection squares, and `ℱ = colim p_i⁻¹ℱ_i` is given by maps `ι_i : p_i⁻¹ℱ_i ⟶ ℱ` compatible with
> the transition maps and enjoying the universal property of the colimit.

```lean
theorem isIso_smallEtaleSheafBaseChange_limit {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)]
    [Nonempty I] {DX DS DT DY : Iᵒᵖ ⥤ Scheme.{u}}
    (f : DX ⟶ DS) (g : DT ⟶ DS) (h : DY ⟶ DX) (e : DY ⟶ DT)
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DX.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DS.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DT.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DY.map a)]
    [∀ i, QuasiCompact (g.app i)] [∀ i, QuasiSeparated (g.app i)]
    (hsq : ∀ i : Iᵒᵖ, IsPullback (h.app i) (e.app i) (f.app i) (g.app i))
    {cX : Cone DX} {cS : Cone DS} {cT : Cone DT} {cY : Cone DY}
    (hcX : IsLimit cX) (hcS : IsLimit cS) (hcT : IsLimit cT) (hcY : IsLimit cY)
    (fL : cX.pt ⟶ cS.pt) (gL : cT.pt ⟶ cS.pt) (hL : cY.pt ⟶ cX.pt) (eL : cY.pt ⟶ cT.pt)
    (hfL : ∀ i : Iᵒᵖ, fL ≫ cS.π.app i = cX.π.app i ≫ f.app i)
    (hgL : ∀ i : Iᵒᵖ, gL ≫ cS.π.app i = cT.π.app i ≫ g.app i)
    (hhL : ∀ i : Iᵒᵖ, hL ≫ cX.π.app i = cY.π.app i ≫ h.app i)
    (heL : ∀ i : Iᵒᵖ, eL ≫ cT.π.app i = cY.π.app i ≫ e.app i)
    (F : EtaleSheafSystem DT (Type (u + 1))) (𝓕 : Sheaf (smallEtaleTopology cT.pt) (Type (u + 1)))
    (ι : ∀ i : Iᵒᵖ, (smallEtaleSheafPullback (Type (u + 1)) (X := cT.pt) (cT.π.app i)).obj
      (F.obj i) ⟶ 𝓕)
    (hι : F.IsSheafPullbackCocone cT ι) (hpres : F.IsSheafPullbackColimitPresentation cT 𝓕 ι)
    (hstage : ∀ i : Iᵒᵖ, IsIso ((smallEtaleSheafBaseChange (Type (u + 1)) (f.app i) (g.app i)
      (h.app i) (e.app i) (hsq i).w).app (F.obj i))) :
    IsIso ((smallEtaleSheafBaseChange (Type (u + 1)) fL gL hL eL
      (limitSquare_comm f g h e cX cS cT cY fL gL hL eL hcS hfL hgL hhL heL
        fun i => (hsq i).w)).app 𝓕)
```

**`Stacks.EtaleCohomology.LimitSetBaseChange.isIso_smallEtaleSetBaseChange_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeGeneral.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/PushforwardBaseChangeGeneral.lean#L287). The attribute's comment: “conclusion (1): base change for the direct images of sheaves of sets passes to the limit. The two colimit presentations `g_*ℱ = colim_i s_i^{-1}g_{i,*}ℱ_i` and `h_*e^{-1}ℱ = colim_i r_i^{-1}h_{i,*}e_i^{-1}ℱ_i` are the two instances of Stacks 0EYM that the source's proof cites; this repository does not prove Stacks 0EYM -- `Stacks.EtaleCohomology.LimitHigherDirectImage` constructs only its comparison maps and says so in its own clause strings -- and the compatibility of the two with the legs is the pasting of base change maps of Stacks 0E47. All three are carried as declared hypotheses (`Kg`/`ρg`/`κg`/`hκg`, `Kh`/`ρh`/`κh`/`hκh`, `α`/`hα`/`hκ`), exactly as for conclusion (2) in `Stacks.EtaleCohomology.LimitBaseChange.isIso_higherBaseChangeMapAb_limit`. What is proved is the source's own argument from those inputs: inverse image is a left adjoint, so it carries the first presentation to a colimit presentation of `f^{-1}g_*ℱ`, and a map of colimit cocones that is invertible on every term is invertible. Since the two presentations are hypotheses, the proof uses nothing of the inverse systems but the schemes and the morphisms, and the levels are accordingly carried as bare families rather than as functors out of `Iᵒᵖ`: no functoriality, no limit property of the cones and no cartesianness of the squares is assumed.”.

> **Conclusion (1) of Stacks 0EZT.** Let `(ℱ_i)` be a family of sheaves of sets on the `T_i`
> and let `ℱ` on `T` be a sheaf whose direct images along the limit are presented, as in Stacks
> 0EYM, as the colimits of the `s_i^{-1}g_{i,*}ℱ_i` and of the `r_i^{-1}h_{i,*}e_i^{-1}ℱ_i`,
> compatibly with the levelwise base change maps. If the base change map of every level is an
> isomorphism, so is the base change map of the limit square.

```lean
theorem isIso_smallEtaleSetBaseChange_limit (w : ∀ i, h i ≫ f i = e i ≫ g i)
    (wL : hL ≫ fL = eL ≫ gL) (hfL : ∀ i, fL ≫ s i = r i ≫ f i)
    (𝓕 : Sheaf (smallEtaleTopology T) (Type (max (u + 1) v)))
    (Kg : I ⥤ Sheaf (smallEtaleTopology S) (Type (max (u + 1) v)))
    (ρg : ∀ i, Kg.obj i ≅ sourceTerm.{u, v} g s F i)
    (κg : Kg ⟶ (Functor.const I).obj
      ((smallEtalePushforward gL (Type (max (u + 1) v))).obj 𝓕))
    (hκg : IsColimit (Cocone.mk
      ((smallEtalePushforward gL (Type (max (u + 1) v))).obj 𝓕) κg))
    (Kh : I ⥤ Sheaf (smallEtaleTopology X) (Type (max (u + 1) v)))
    (ρh : ∀ i, Kh.obj i ≅ targetTerm.{u, v} h e r F i)
    (κh : Kh ⟶ (Functor.const I).obj
      ((smallEtalePushforward hL (Type (max (u + 1) v))).obj
        ((smallEtaleInverseImage.{u, v} eL).obj 𝓕)))
    (hκh : IsColimit (Cocone.mk
      ((smallEtalePushforward hL (Type (max (u + 1) v))).obj
        ((smallEtaleInverseImage.{u, v} eL).obj 𝓕)) κh))
    (α : Kg ⋙ smallEtaleInverseImage.{u, v} fL ⟶ Kh)
    (hα : ∀ i, (smallEtaleInverseImage.{u, v} fL).map (ρg i).hom ≫
      stageComparison.{u, v} f g h e r s fL F w hfL i = α.app i ≫ (ρh i).hom)
    (hκ : ∀ i, (smallEtaleInverseImage.{u, v} fL).map (κg.app i) ≫
      setBaseChangeApp.{u, v} eL hL gL fL wL.symm 𝓕 = α.app i ≫ κh.app i)
    (hstage : ∀ i, IsIso ((smallEtaleSetBaseChange.{u, v} (e i) (h i) (g i) (f i)
      (w i).symm).app (F i))) :
    IsIso ((smallEtaleSetBaseChange.{u, v} eL hL gL fL wL.symm).app 𝓕)
```

## Tag 0GJL, a lemma

[Tag 0GJL](https://stacks.math.columbia.edu/tag/0GJL) in the Stacks Project.

**`Stacks.EtaleCohomology.LimitBaseChangeDerived.isIso_smallEtaleDerivedBaseChangeAb_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeDerived.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeDerived.lean#L322). The attribute's comment: “if the derived base change map of the `i`-th square is an isomorphism at `K_i` for all `i ≥ 0`, then the derived base change map of the limit square is an isomorphism at `K`, with `K_i` and `K` the derived inverse images of `K_0 ∈ D^+(T_{0, étale})` to `T_i` and to `T`. Both steps of the source's proof are carried out: the reduction to cohomology sheaves is `isIso_of_forall_isIso_derivedLimitComparison` and the colimit argument of Stacks 0EZT, with the reference to Stacks 0EYM replaced by one to Stacks 0GIU, is `isIso_derivedLimitComparison`. EXTRA HYPOTHESIS: the single bundled hypothesis `P` grants, in each degree `p`, the two instances of the colimit assertion of Stacks 0GIU that the source's proof cites — `H^p(Rg_*K) = colim_{i ≥ 0} s_i^{-1}H^p(Rg_{i, *}K_i)` and `H^p(Rh_*Re^{-1}K) = colim_{i ≥ 0} r_i^{-1}H^p(Rh_{i, *}Re_i^{-1}K_i)` — presented as in `Stacks.EtaleCohomology.LimitBaseChange.isIso_higherBaseChangeMapAb_limit`, namely a diagram with terms identified with `derivedSourceTerm` resp. `derivedTargetTerm` and a colimit cocone with the stated vertex, together with the comparison of the two diagrams and its compatibility with terms and legs, which is the pasting of base change maps of Stacks 0E47. That colimit assertion is NOT available in this repository: `Stacks.EtaleCohomology.LimitHigherDirectImage.pullbackProjectionMap`, the carrier of Stacks 0GIU, states in its own clause string that it is not proved and that the colimit cannot even be formed, both because the colimit assertion of Stacks 0EYM is unproved and because the cocycle compatibility of Stacks 0E47 is unavailable for the bounded below derived base change map. The hypothesis does not restate the goal: it says nothing about any base change map being invertible, only that the two sides are the asserted colimits and that the comparison maps assemble.”.

> **Stacks 0GJL.** Let `(X_i, Y_i, S_i, T_i, f_i, h_i, e_i, g_i)` be an inverse system of
> squares as in the setup of Stacks 0EZT, with limit square `(X, Y, S, T, f, h, e, g)`. Let
> `0 ∈ I`, let `K_0` be an object of `D^+(T_{0, étale})`, let `K_i` be the pullback of `K_0` to
> `T_i` for `i ≥ 0` and `K` the pullback of `K_0` to `T`. If `f_i^{-1}Rg_{i, *}K_i =
> Rh_{i, *}e_i^{-1}K_i` for all `i ≥ 0`, then `f^{-1}Rg_*K = Rh_*e^{-1}K`.

```lean
theorem isIso_smallEtaleDerivedBaseChangeAb_limit
    (w : ∀ i : Iᵒᵖ, h.app i ≫ f.app i = e.app i ≫ g.app i) (wL : hL ≫ fL = eL ≫ gL)
    (hfL : ∀ i : Iᵒᵖ, fL ≫ cS.π.app i = cX.π.app i ≫ f.app i)
    {i₀ : Iᵒᵖ} (K₀ : PlusAb (DT.obj i₀)) (J : Type w₁) [Category.{w₂} J] (σ : J → Iᵒᵖ)
    (τ : ∀ j : J, σ j ⟶ i₀)
    (P : ∀ p : ℤ,
      ColimitPresentation f g h e cX cS cT cY fL gL hL eL w wL hfL K₀ J σ τ p)
    (hstage : ∀ (i : Iᵒᵖ) (a : i ⟶ i₀),
      IsIso ((smallEtaleDerivedBaseChangeAb (f.app i) (g.app i) (h.app i) (e.app i) (w i)).app
        (stageObj K₀ a))) :
    IsIso ((smallEtaleDerivedBaseChangeAb fL gL hL eL wL).app (limitObj cT K₀))
```

**`Stacks.EtaleCohomology.LimitBaseChangeDerived.isIso_smallEtaleDerivedBaseChangeAb_limit_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeDerivedColimit.lean, line 807](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Colimits/LimitBaseChangeDerivedColimit.lean#L807).

> Let `I` be a directed set and let `(X_i, Y_i, S_i, T_i, f_i, h_i, e_i, g_i)` be an inverse
> system of cartesian squares of schemes with affine transition morphisms and with `g_i`
> quasi-compact and quasi-separated, with limit square `(X, Y, S, T, f, h, e, g)`. Let `0 = i₀ ∈ I`,
> let `K_0 ∈ D^+(T_{0, étale})`, let `K_i` be the pullback of `K_0` to `T_i` for `i ≥ 0` and `K` the
> pullback of `K_0` to `T`. If the derived base change map
> `f_i^{-1}Rg_{i, *}K_i ⟶ Rh_{i, *}e_i^{-1}K_i` is an isomorphism for all `i ≥ 0`, then so is
> `f^{-1}Rg_*K ⟶ Rh_*e^{-1}K`.
>
> The limit morphisms are any morphisms `f`, `g`, `h`, `e` satisfying the equations of the
> projection squares.

```lean
theorem isIso_smallEtaleDerivedBaseChangeAb_limit_of_isLimit [IsDirected I (· ≤ ·)] [Nonempty I]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DX.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DS.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DT.map a)]
    [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (DY.map a)]
    [∀ i, QuasiCompact (g.app i)] [∀ i, QuasiSeparated (g.app i)]
    (hsq : ∀ i : Iᵒᵖ, IsPullback (h.app i) (e.app i) (f.app i) (g.app i))
    (hcX : IsLimit cX) (hcS : IsLimit cS) (hcT : IsLimit cT) (hcY : IsLimit cY)
    (fL : cX.pt ⟶ cS.pt) (gL : cT.pt ⟶ cS.pt) (hL : cY.pt ⟶ cX.pt) (eL : cY.pt ⟶ cT.pt)
    (hfL : ∀ i : Iᵒᵖ, fL ≫ cS.π.app i = cX.π.app i ≫ f.app i)
    (hgL : ∀ i : Iᵒᵖ, gL ≫ cS.π.app i = cT.π.app i ≫ g.app i)
    (hhL : ∀ i : Iᵒᵖ, hL ≫ cX.π.app i = cY.π.app i ≫ h.app i)
    (heL : ∀ i : Iᵒᵖ, eL ≫ cT.π.app i = cY.π.app i ≫ e.app i)
    (i₀ : I) (K₀ : PlusAb (DT.obj (op i₀)))
    (hstage : ∀ (i : Iᵒᵖ) (a : i ⟶ op i₀),
      IsIso ((smallEtaleDerivedBaseChangeAb (f.app i) (g.app i) (h.app i) (e.app i)
        (hsq i).w).app (stageObj K₀ a))) :
    IsIso ((smallEtaleDerivedBaseChangeAb fL gL hL eL
      (LimitBaseChange.limitSquare_comm f g h e cX cS cT cY fL gL hL eL hcS hfL hgL hhL heL
        fun i => (hsq i).w)).app (limitObj cT K₀))
```

## Tag 0EZU, a lemma

[Tag 0EZU](https://stacks.math.columbia.edu/tag/0EZU) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_iff_forall_isIso_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/StalkwiseCriterion.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/StalkwiseCriterion.lean#L212). The attribute's comment: “base change on higher direct images is an isomorphism iff it is on every stalk”.

> **Stacks 0EZU.** Consider a cartesian diagram of schemes
> ```
> X  ←-h-  Y
> |f       |e
> S  ←-g-  T
> ```
> with `g : T ⟶ S` quasi-compact and quasi-separated, let `F` be an abelian sheaf on the small
> étale site of `T`, and let `q ≥ 0`. Then the base change map on higher direct images
> `f⁻¹ R^q g_* F ⟶ R^q h_* e⁻¹ F` is an isomorphism if and only if its map on the stalk at every
> geometric point of `X` is an isomorphism.

```lean
public theorem isIso_higherBaseChangeMapAb_app_iff_forall_isIso_stalk
    {X Y S T : Scheme.{u}} (f : X ⟶ S) (h : Y ⟶ X) (e : Y ⟶ T) (g : T ⟶ S)
    (sq : IsPullback h e f g) [QuasiCompact g] [QuasiSeparated g]
    (F : Sheaf (smallEtaleTopology T) Ab.{u + 1}) (q : ℕ) :
    (∀ x : GeometricPoint X,
        IsIso ((smallEtaleStalkAb x.hom).map ((higherBaseChangeMapAb f g h e sq.w q).app F))) ↔
      IsIso ((higherBaseChangeMapAb f g h e sq.w q).app F)
```

**`Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_iff_forall_isIso_stalkMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/StalkwiseCriterion.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/StalkwiseCriterion.lean#L232). The attribute's comment: “the condition at a geometric point, as a map out of the stalk at its image”.

> **Stacks 0EZU**, with the condition at a geometric point `x̄` of `X` phrased as invertibility
> of the canonical map `(R^q g_* F)_{s̄} ⟶ (R^q h_* e⁻¹ F)_{x̄}` out of the stalk at the image
> geometric point `s̄ = f(x̄)`. In the situation of
> `Stacks.EtaleCohomology.isIso_higherBaseChangeMapAb_app_iff_forall_isIso_stalk`, the base change
> map `f⁻¹ R^q g_* F ⟶ R^q h_* e⁻¹ F` is an isomorphism if and only if that map is an isomorphism
> for every geometric point `x̄` of `X`.
>
> This is the source's equivalence with each of its two cohomology groups replaced by the stalk
> which it computes; the identification of the stalks with cohomology over the fibre products
> `Spec(𝒪^{sh}_{S,s̄}) ×_S T` and `Spec(𝒪^{sh}_{X,x̄}) ×_S T` is not available in the library.

```lean
public theorem isIso_higherBaseChangeMapAb_app_iff_forall_isIso_stalkMap
    {X Y S T : Scheme.{u}} (f : X ⟶ S) (h : Y ⟶ X) (e : Y ⟶ T) (g : T ⟶ S)
    (sq : IsPullback h e f g) [QuasiCompact g] [QuasiSeparated g]
    (F : Sheaf (smallEtaleTopology T) Ab.{u + 1}) (q : ℕ) :
    (∀ x : GeometricPoint X,
        IsIso (higherBaseChangeMapAbStalk f g h e sq.w q F x)) ↔
      IsIso ((higherBaseChangeMapAb f g h e sq.w q).app F)
```

**`AlgebraicGeometry.isIso_higherBaseChangeMapAb_app_iff_forall_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/StrictHenselizationCriterion.lean, line 630](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/BaseChangeHigher/StrictHenselizationCriterion.lean#L630).

> Consider a cartesian square of schemes
> ```
> X  ←-h-  Y
> |f       |e
> S  ←-g-  T
> ```
> with `g : T ⟶ S` quasi-compact and quasi-separated, let `F` be an abelian sheaf on `T_étale` and
> let `q ≥ 0`. The following are equivalent:
>
> 1. for every geometric point `x̄` of `X` with image `s̄ = f(x̄)`, the restriction map
>    `H^q(T ×_S Spec(𝒪^{sh}_{S,s̄}), F) ⟶ H^q(T ×_S Spec(𝒪^{sh}_{X,x̄}), F)` along the canonical
>    morphism `AlgebraicGeometry.strictHenselizationBaseChangeMap` is bijective;
> 2. the base change map `f⁻¹ R^q g_* F ⟶ R^q h_* e⁻¹ F` is an isomorphism.
>
> Here the cohomology groups are those of the inverse images of `F` along the projections to `T`, and
> the restriction map is pull back along the canonical morphism together with the comparison of
> the iterated inverse image with the inverse image along the composite.

```lean
theorem isIso_higherBaseChangeMapAb_app_iff_forall_bijective
    (F : Sheaf (smallEtaleTopology T) Ab.{u + 1}) (q : ℕ) :
    (∀ x : GeometricPoint X, Function.Bijective
      (etaleCohomologyPullback (strictHenselizationBaseChangeMap B hX hS f g x)
        ((smallEtalePullbackAbComp' _ _ _
          (strictHenselizationBaseChangeMap_fst B hX hS f g x)).hom.app
          F) q)) ↔
      IsIso ((higherBaseChangeMapAb f g h e sq.w q).app F)
```

## Tag 0EZV, a lemma

[Tag 0EZV](https://stacks.math.columbia.edu/tag/0EZV) in the Stacks Project.

**`Stacks.EtaleCohomology.bijective_strictHenselizationFiberRestriction_iff_of_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationSeparablyClosedFiber.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationSeparablyClosedFiber.lean#L560). The attribute's comment: “the equivalence of the tag's two conditions. What is carried as the explicit datum `Stacks.EtaleCohomology.SepClosedFiberLocallyConstantPresentation`, rather than constructed, is exactly the COHOMOLOGICAL identification of the source's proof: that the two cohomology groups over `Spec(O^sh_{S,s̄}) ×_S Spec K` are locally constant functions on the limit index space with values in the two groups over `Spec K`, compatibly with restriction. The geometric input it rests on is proved here, not assumed -- the fibre product is affine (`isAffine_strictHenselizationBaseFiber`), is `Spec` of a ring ind-étale over `K` (`indEtale_strictHenselizationBaseFiberRing`, from `indEtale_etaleLocalRing` and Stacks 0BSH), and each étale `K`-algebra of such a presentation has `Spec` a finite coproduct of copies of `Spec K` (`specIsoSigmaOfIsSepClosed`). Three things block constructing the datum: Theorem 09YQ is available only as the right-derived `sheafSections` of the small AFFINE étale site and its transport to the `Sheaf.H` of the small étale site, which is what `Stacks.EtaleCohomology.etaleCohomologyRestrictionMap` is stated for, needs a general-degree comparison `Sheaf.H = rightDerived sheafSections` that exists nowhere at these universes; the passage from `StacksDraft.IndEtale` to an explicit cofiltered limit of schemes is unavailable; and the source's identification of the base change along the morphism of strict henselizations of the different copies of `Spec K` in a stage -- distinct `K`-points of `Spec(O^sh_{S,s̄})`, Galois twists of one another -- is suppressed in the source and not available either. The datum asserts only the cohomological identification, not the equivalence, which is proved here”.

> **Stacks Project, Tag 0EZV.** Let `f : X ⟶ S` be a morphism of schemes, let `x̄` be a
> geometric point of `X` with image `s̄` in `S`, let `Spec K ⟶ Spec(𝒪^{sh}_{S,s̄})` be a morphism
> with `K` a separably closed field, let `ℱ` be an abelian sheaf on the small étale site of
> `Spec K` and let `q ≥ 0`. Then
> `H^q(Spec(𝒪^{sh}_{X,x̄}) ×_S Spec K, ℱ) = H^q(Spec(𝒪^{sh}_{S,s̄}) ×_S Spec K, ℱ)` holds if and
> only if `H^q(Spec(𝒪^{sh}_{X,x̄}) ×_{Spec(𝒪^{sh}_{S,s̄})} Spec K, ℱ) = H^q(Spec K, ℱ)` does, each
> equality read as bijectivity of the canonical restriction map.
>
> The limit presentation of the two cohomology groups over `Spec(𝒪^{sh}_{S,s̄}) ×_S Spec K` as
> locally constant functions on a nonempty space is carried as the explicit datum
> `Stacks.EtaleCohomology.SepClosedFiberLocallyConstantPresentation`; what is proved here is the
> equivalence, which comes down to post-composition with a map being bijective on locally constant
> functions on a nonempty space exactly when the map is.

```lean
public theorem bijective_strictHenselizationFiberRestriction_iff_of_presentation
    [IsSepClosed K] (A : Type u) [TopologicalSpace A]
    (F : Sheaf (Spec (CommRingCat.of K)).smallEtaleTopology AddCommGrpCat.{max (u + 1) v})
    (q : ℕ)
    (P : SepClosedFiberLocallyConstantPresentation.{u, v, w} B hX hS f x k A F q) :
    Function.Bijective (strictHenselizationFiberRestriction.{u, v, w} B hX hS f x k F q) ↔
      Function.Bijective (strictHenselizationPointRestriction.{u, v, w} B hX hS f x k F q)
```

**`Stacks.EtaleCohomology.bijective_strictHenselizationFiberCohomologyPullback_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationSeparablyClosedFiberCohomology.lean, line 695](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationSeparablyClosedFiberCohomology.lean#L695). The attribute's comment: “corrected: condition (1) is equivalent to condition (2) at every lift `k'` of `Spec K ⟶ S` to the strict henselization, not only at the given point; that (2) at the given point does not imply (1) is `Stacks.EtaleCohomology.exists_bijective_pointRestriction_and_not_bijective_fiberRestriction`”.

> **[Stacks, Tag 0EZV], corrected.** Let `f : X ⟶ S` be a morphism of schemes, `x̄` a geometric
> point of `X` with image `s̄`, `k : Spec K ⟶ Spec(𝒪^{sh}_{S,s̄})` with `K` separably closed, `ℱ` an
> abelian sheaf on `Spec K` and `q ≥ 0`. Then
> `H^q(Spec(𝒪^{sh}_{X,x̄}) ×_S Spec K, ℱ) = H^q(Spec(𝒪^{sh}_{S,s̄}) ×_S Spec K, ℱ)` if and only if
> `H^q(Spec(𝒪^{sh}_{X,x̄}) ×_{Spec(𝒪^{sh}_{S,s̄}), k'} Spec K, ℱ) = H^q(Spec K, ℱ)` for every lift
> `k'` of the composite `Spec K ⟶ S` to the strict henselization, each equality read as
> bijectivity of the restriction map.

```lean
public theorem bijective_strictHenselizationFiberCohomologyPullback_iff
    (F : Sheaf (Spec (CommRingCat.of K)).smallEtaleTopology Ab.{u + 1}) (q : ℕ) :
    Function.Bijective (strictHenselizationFiberCohomologyPullback B hX hS f x k F q) ↔
      ∀ k' : Spec (CommRingCat.of K) ⟶ strictHenselization B S hS (x.map f),
        k' ≫ strictHenselizationToBase B S hS (x.map f) =
            k ≫ strictHenselizationToBase B S hS (x.map f) →
          Function.Bijective (strictHenselizationPointCohomologyPullback B hX hS f x k' F q)
```

**`Stacks.EtaleCohomology.exists_bijective_pointRestriction_and_not_bijective_fiberRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationSeparablyClosedFiberCohomology.lean, line 857](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationSeparablyClosedFiberCohomology.lean#L857). The attribute's comment: “the statement as given fails: condition (2) at the given point does not imply condition (1). Condition (1) is equivalent to condition (2) at every lift of `Spec K ⟶ S` to the strict henselization.”.

> **Tag 0EZV fails as stated: condition (2) at the given point does not imply condition (1).**
> Let `S` be the nodal cubic over an algebraically closed field of characteristic zero, `s̄` its
> geometric point at the node, and `X = Spec(𝒪^{sh}_{S,s̄}/(e))` for the branch
> `e = y - x √(1 + x)` of the node in the strict henselization, with `x̄` its geometric point over
> `s̄`. For two `K`-points `κ`, `τ` of `Spec(𝒪^{sh}_{S,s̄})` over the same point of `S`, with `κ` on
> the branch and `τ` off it, take the point `κ` and `q = 0`, `ℱ = ℤ`. The fibre of `X` over `κ` is
> `Spec K` itself, so condition (2) holds; the fibre over `τ` is empty, so the restriction map of
> condition (1) kills the class of the constant function `1` on a clopen neighbourhood of `τ`, and
> condition (1) fails.

```lean
public theorem exists_bijective_pointRestriction_and_not_bijective_fiberRestriction :
    ∃ (B : BigEtaleSite.{u}) (X S : Scheme.{u}) (hX : B.Contains X) (hS : B.Contains S)
      (f : X ⟶ S) (x : GeometricPoint X) (K : Type u) (_ : Field K) (_ : IsAlgClosed K)
      (k : Spec (CommRingCat.of K) ⟶ strictHenselization B S hS (x.map f)),
      Function.Bijective
          (strictHenselizationPointCohomologyPullback B hX hS f x k
            (constantZ (Spec (CommRingCat.of K))) 0) ∧
        ¬ Function.Bijective
          (strictHenselizationFiberCohomologyPullback B hX hS f x k
            (constantZ (Spec (CommRingCat.of K))) 0)
```

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.not_forall_bijective_strictHenselizationFiberRestriction_iff`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationSeparablyClosedFiberRestriction.lean#L286), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationFiberErratum.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/StrictHenselizationFiberErratum.lean#L68) (StacksFrontier): “erratum: the statement as printed is false; condition (2) at the given point does not imply condition (1). This is the negation of the printed equivalence, for the restriction maps of its statement, at the nodal cubic. The corrected statement, (1) iff (2) for every lift `k'` of `Spec K ⟶ S` to the strict henselization, is `Stacks.EtaleCohomology.bijective_strictHenselizationFiberCohomologyPullback_iff`.”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.86, Tag 0EZQ](https://stacks.math.columbia.edu/tag/0EZQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

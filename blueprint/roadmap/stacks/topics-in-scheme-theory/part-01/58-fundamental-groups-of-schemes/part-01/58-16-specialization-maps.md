---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_isSpecializationMap, AlgebraicGeometry.exists_isSpecializationMap_of_square, AlgebraicGeometry.exists_isSpecializationMap_comm_square, AlgebraicGeometry.isSpecializationMap_comp, AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_strictlyHenselianValuationRing, AlgebraicGeometry.exists_valuationSubring_strictlyHenselian_of_specializes, AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_isDiscreteValuationRing, AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_strictlyHenselianDVR
statement: formalized
proof: formalized
---

# 58.16 Specialization maps

Section 58.16 of the Stacks Project, [Tag 0BUP](https://stacks.math.columbia.edu/tag/0BUP). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BUP, the section

[Tag 0BUP](https://stacks.math.columbia.edu/tag/0BUP) in the Stacks Project.

**`AlgebraicGeometry.exists_isSpecializationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapExistence.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapExistence.lean#L260). The attribute's comment: “the construction of the specialization map, i.e. the existence of a continuous homomorphism satisfying `AlgebraicGeometry.IsSpecializationMap`, granted the one input this library cannot prove, carried as the hypothesis `hclosedFibre`: that base change along the inclusion of the closed geometric fibre `X_s ⟶ X ×_S Spec C` is an equivalence on finite étale covers, for a henselian local ring `C` with separably closed residue field over `S` through whose closed point `s` factors. That is the first of the two equalities in the source's composite `π₁(X_{s̄'}) → π₁(X_A) = π₁(X_{κ(s)^{sep}}) = π₁(X_{s̄})`, namely Stacks 0A48, together with the second, Stacks 0BTW and 0A49; `StacksFrontier.AlgebraicGeometry.FundamentalGroup.ClosedGeometricFibre` reduces it to the essential-surjectivity half of Stacks 0GS2, left open by `StacksFrontier.AlgebraicGeometry.FundamentalGroup.FiniteEtaleProperEquivalence`. It is the same datum that `AlgebraicGeometry.IsSpecializationMap` records and that `AlgebraicGeometry.exists_isSpecializationMap_of_square` (Stacks 0C0K) carries, and it restricts nothing about `f`, the specialization or the geometric points. `AlgebraicGeometry.ProperHenselianFiniteEtaleEquivalence`, Stacks 0A48 alone, would not suffice: the residue field of `A` is only separably closed, so passing to the algebraically closed `κ(s̄)` needs Stacks 0BTW, whose fundamental-group half is absent here. Everything else is proved: the strict henselization `A` of `𝒪_{S,s}`, the factorization of `s̄` through the closed point of `Spec A`, the factorization of `s̄'` through `Spec A` obtained from the specialization by dominating `𝒪_{S,s} → κ(s̄')` by a strictly henselian valuation ring, connectedness of `X_A`, the fibre-functor isomorphism, and the defining equation.”.

> **Stacks Project, Tag 0BUP.** Let `f : X ⟶ S` be a proper morphism with geometrically
> connected fibres, let `s' ⇝ s` be a specialization of points of `S`, let `s̄'` and `s̄` be
> geometric points over `s'` and `s`, and choose geometric base points of the two geometric fibres
> `X_{s̄'}` and `X_{s̄}`. Then there is a specialization map `π₁(X_{s̄'}) ⟶ π₁(X_{s̄})`, that is, a
> continuous homomorphism satisfying `AlgebraicGeometry.IsSpecializationMap`.

```lean
theorem exists_isSpecializationMap (f : X ⟶ S) [IsProper f] [GeometricallyConnected f]
    (s' s : GeometricPoint S)
    (hspec : s'.hom (closedPoint s'.residueField) ⤳ s.hom (closedPoint s.residueField))
    (x' : GeometricPoint (fiberOverGeometricPoint f s'))
    (x : GeometricPoint (fiberOverGeometricPoint f s))
    (hclosedFibre : ∀ (C : Type u) (_ : CommRing C) (_ : HenselianLocalRing C),
      ∀ (_ : IsSepClosed (ResidueField C)) (r : Spec (.of C) ⟶ S)
        (q : s.source ⟶ Spec (.of C)) (hq : q ≫ r = s.hom),
      q (closedPoint s.residueField) = closedPoint C →
      (finiteEtaleBaseChange (fiberOverGeometricPointMap f s r q hq)).IsEquivalence) :
    ∃ sp : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' →ₜ*
        EtaleFundamentalGroup (fiberOverGeometricPoint f s) x,
      IsSpecializationMap f s' s x' x sp
```

## Tag 0C0K, a lemma

[Tag 0C0K](https://stacks.math.columbia.edu/tag/0C0K) in the Stacks Project.

**`AlgebraicGeometry.exists_isSpecializationMap_of_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapFunctoriality.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapFunctoriality.lean#L317). The attribute's comment: “the whole statement — the specialization map on the bottom row and the commutativity of the square of fundamental groups — granted the one input this library cannot prove, carried as the hypothesis `hclosedFibre`: that base change along the inclusion of the closed geometric fibre `X_s ⟶ X ×_S Spec C` is an equivalence on finite étale covers, for a strictly henselian local ring `C` over `S` through whose closed point `s` factors. That is Stacks 0A48 with 0A49 and 0BTW; `StacksFrontier.AlgebraicGeometry.FundamentalGroup.ClosedGeometricFibre` reduces it to the essential-surjectivity half of Stacks 0GS2, left open by `StacksFrontier.AlgebraicGeometry.FundamentalGroup.FiniteEtaleProperEquivalence`. It is an input to the construction of a specialization map (Stacks 0BUP) — the same datum for the upper row is part of `AlgebraicGeometry.IsSpecializationMap` — and it restricts nothing about `a`, `b`, the specialization `t' ⤳ t` or the schemes. Everything else is proved here: the strict henselization `A` of the stalk at the image of `t`, the ring map `A → B` of Stacks 04GU, the factorizations of the two geometric points of `S` through `Spec A`, connectedness of `X_A`, and the base-point bookkeeping.”.

> **Stacks Project, Tag 0C0K.** Consider a commutative square of schemes with `a : Y ⟶ X` on
> top, `g : Y ⟶ T` and `f : X ⟶ S` vertical and `b : T ⟶ S` on the bottom, where `f` and `g` are
> proper with geometrically connected fibres. Let `t'` and `t` be geometric points of `T` and let
> `sp : π₁(Y_{t'}) → π₁(Y_t)` be a specialization map. Then there is a specialization map
> `π₁(X_{s'}) → π₁(X_s)`, where `s'` and `s` are the images of `t'` and `t` in `S`, making the
> square of maps induced by the morphisms `Y_{t'} ⟶ X_{s'}` and `Y_t ⟶ X_s` of geometric fibres
> commute.

```lean
theorem exists_isSpecializationMap_of_square (a : Y ⟶ X) (g : Y ⟶ T) (f : X ⟶ S) (b : T ⟶ S)
    (hab : a ≫ f = g ≫ b) [IsProper f] [GeometricallyConnected f] [IsProper g]
    [GeometricallyConnected g] (t' t : GeometricPoint T)
    (y' : GeometricPoint (fiberOverGeometricPoint g t'))
    (y : GeometricPoint (fiberOverGeometricPoint g t))
    (sp : EtaleFundamentalGroup (fiberOverGeometricPoint g t') y' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint g t) y)
    (hsp : IsSpecializationMap g t' t y' y sp)
    (hclosedFibre : ∀ (C : Type u) (_ : CommRing C) (_ : HenselianLocalRing C),
      ∀ (_ : IsSepClosed (ResidueField C)) (r : Spec (.of C) ⟶ S)
        (p : (t.map b).source ⟶ Spec (.of C)) (hp : p ≫ r = (t.map b).hom),
      p (closedPoint (t.map b).residueField) = closedPoint C →
      (finiteEtaleBaseChange
        (fiberOverGeometricPointMap f (t.map b) r p hp)).IsEquivalence) :
    ∃ sp' : EtaleFundamentalGroup (fiberOverGeometricPoint f (t'.map b))
          (y'.map (fiberOverGeometricPointSquareMap a g f b hab t')) →ₜ*
        EtaleFundamentalGroup (fiberOverGeometricPoint f (t.map b))
          (y.map (fiberOverGeometricPointSquareMap a g f b hab t)),
      IsSpecializationMap f (t'.map b) (t.map b)
          (y'.map (fiberOverGeometricPointSquareMap a g f b hab t'))
          (y.map (fiberOverGeometricPointSquareMap a g f b hab t)) sp' ∧
        ∀ γ, etaleFundamentalGroupMap
              (fiberOverGeometricPointSquareMap a g f b hab t) y (sp γ)
          = sp' (etaleFundamentalGroupMap
              (fiberOverGeometricPointSquareMap a g f b hab t') y' γ)
```

**`AlgebraicGeometry.exists_isSpecializationMap_comm_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapSquare.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapSquare.lean#L58). The attribute's comment: “The whole statement, under the source's hypotheses only.”.

> **Stacks Project, Tag 0C0K.** Consider a commutative square of schemes with `a : Y ⟶ X` on
> top, `g : Y ⟶ T` and `f : X ⟶ S` vertical and `b : T ⟶ S` on the bottom, where `f` and `g` are
> proper with geometrically connected fibres. Let `t'` and `t` be geometric points of `T` and let
> `sp : π₁(Y_{t'}) → π₁(Y_t)` be a specialization map. Then there is a specialization map
> `sp' : π₁(X_{s'}) → π₁(X_s)`, where `s'` and `s` are the images of `t'` and `t` in `S`, such that
> the square formed by `sp`, `sp'` and the maps induced by the morphisms `Y_{t'} ⟶ X_{s'}` and
> `Y_t ⟶ X_s` of geometric fibres commutes.

```lean
theorem exists_isSpecializationMap_comm_square (a : Y ⟶ X) (g : Y ⟶ T) (f : X ⟶ S)
    (b : T ⟶ S) (hab : a ≫ f = g ≫ b) [IsProper f] [GeometricallyConnected f] [IsProper g]
    [GeometricallyConnected g] (t' t : GeometricPoint T)
    (y' : GeometricPoint (fiberOverGeometricPoint g t'))
    (y : GeometricPoint (fiberOverGeometricPoint g t))
    (sp : EtaleFundamentalGroup (fiberOverGeometricPoint g t') y' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint g t) y)
    (hsp : IsSpecializationMap g t' t y' y sp) :
    ∃ sp' : EtaleFundamentalGroup (fiberOverGeometricPoint f (t'.map b))
          (y'.map (fiberOverGeometricPointSquareMap a g f b hab t')) →ₜ*
        EtaleFundamentalGroup (fiberOverGeometricPoint f (t.map b))
          (y.map (fiberOverGeometricPointSquareMap a g f b hab t)),
      IsSpecializationMap f (t'.map b) (t.map b)
          (y'.map (fiberOverGeometricPointSquareMap a g f b hab t'))
          (y.map (fiberOverGeometricPointSquareMap a g f b hab t)) sp' ∧
        ∀ γ, etaleFundamentalGroupMap
              (fiberOverGeometricPointSquareMap a g f b hab t) y (sp γ)
          = sp' (etaleFundamentalGroupMap
              (fiberOverGeometricPointSquareMap a g f b hab t') y' γ)
```

## Tag 0C0L, a lemma

[Tag 0C0L](https://stacks.math.columbia.edu/tag/0C0L) in the Stacks Project.

**`AlgebraicGeometry.isSpecializationMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMap.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMap.lean#L525).

> **Stacks Project, Tag 0C0L.** For a proper morphism with geometrically connected fibres and
> specializations `s'' ⇝ s' ⇝ s`, the composite of a specialization map
> `π₁(X_{s̄''}) → π₁(X_{s̄'})` with a specialization map `π₁(X_{s̄'}) → π₁(X_{s̄})` is again a
> specialization map `π₁(X_{s̄''}) → π₁(X_{s̄})`.

```lean
theorem isSpecializationMap_comp (f : X ⟶ S) [IsProper f] [GeometricallyConnected f]
    (s'' s' s : GeometricPoint S)
    (x'' : GeometricPoint (fiberOverGeometricPoint f s''))
    (x' : GeometricPoint (fiberOverGeometricPoint f s'))
    (x : GeometricPoint (fiberOverGeometricPoint f s))
    (h₁ : EtaleFundamentalGroup (fiberOverGeometricPoint f s'') x'' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint f s') x')
    (h₂ : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint f s) x)
    (hs₁ : IsSpecializationMap f s'' s' x'' x' h₁)
    (hs₂ : IsSpecializationMap f s' s x' x h₂) :
    IsSpecializationMap f s'' s x'' x (h₂.comp h₁)
```

## Tag 0C0M, a lemma

[Tag 0C0M](https://stacks.math.columbia.edu/tag/0C0M) in the Stacks Project.

**`AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_strictlyHenselianValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapValuationRing.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapValuationRing.lean#L297).

> **Stacks Project, Tag 0C0M.** Let `f : X ⟶ S` be a proper morphism with geometrically
> connected fibres, let `s'` and `s` be geometric points of `S` and let
> `sp : π₁(X_{s̄'}) → π₁(X_{s̄})` be a specialization map. Then there are a strictly henselian
> valuation ring `R` with algebraically closed fraction field (and algebraically closed residue
> field) and a morphism `r : Spec R ⟶ S` sending the generic point `η` of `Spec R` to the image of
> `s'` and its closed point `o` to the image of `s`, such that `sp` is isomorphic to the
> specialization map `sp_R : π₁((X_R)_η) → π₁((X_R)_o)` of the base change `X_R ⟶ Spec R`: there
> are isomorphisms of topological groups `π₁(X_{s̄'}) ≅ π₁((X_R)_η)` and `π₁(X_{s̄}) ≅ π₁((X_R)_o)`
> intertwining `sp` and `sp_R`.
>
> The geometric points `η` and `o` of `Spec R` are the generic and closed points themselves: the
> field of `η` is a fraction field of `R`, and `R` maps onto the field of `o`. This is
> `exists_isSpecializationMap_isomorphic_over_valuationRing` with its input Tag 0A48 supplied by
> `properHenselianFiniteEtaleEquivalence`.

```lean
theorem exists_isSpecializationMap_isomorphic_over_strictlyHenselianValuationRing
    {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f] [GeometricallyConnected f]
    (s' s : GeometricPoint S)
    (x' : GeometricPoint (fiberOverGeometricPoint f s'))
    (x : GeometricPoint (fiberOverGeometricPoint f s))
    (sp : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint f s) x)
    (hsp : IsSpecializationMap f s' s x' x sp) :
    ∃ (R : Type u) (_ : CommRing R) (_ : IsDomain R) (_ : ValuationRing R)
      (_ : StrictlyHenselianLocalRing R) (_ : IsAlgClosed (FractionRing R))
      (_ : IsAlgClosed (ResidueField R))
      (r : Spec (.of R) ⟶ S) (η o : GeometricPoint (Spec (.of R)))
      (yη : GeometricPoint (fiberOverGeometricPoint (pullback.snd f r) η))
      (yo : GeometricPoint (fiberOverGeometricPoint (pullback.snd f r) o))
      (spR : EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) η) yη →ₜ*
        EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) o) yo),
      η.hom default = genericPoint (Spec (.of R)) ∧
      o.hom default = closedPoint R ∧
      @IsFractionRing R _ η.residueField _ (Spec.preimage η.hom).hom.toAlgebra ∧
      Function.Surjective (Spec.preimage o.hom).hom ∧
      r (η.hom default) = s'.hom default ∧
      r (o.hom default) = s.hom default ∧
      IsSpecializationMap (pullback.snd f r) η o yη yo spR ∧
      ∃ (eη : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' ≃ₜ*
            EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) η) yη)
        (eo : EtaleFundamentalGroup (fiberOverGeometricPoint f s) x ≃ₜ*
            EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) o) yo),
        ∀ γ, eo (sp γ) = spR (eη γ)
```

**`AlgebraicGeometry.exists_valuationSubring_strictlyHenselian_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationValuationRing.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationValuationRing.lean#L97). The attribute's comment: “the existence of the strictly henselian valuation ring `R` over `S` with algebraically closed fraction field realizing the specialization, which is the only step the Stacks proof argues; the comparison `sp ≅ sp_R` of specialization maps of fundamental groups is not formalized, because the specialization map `sp` cannot be constructed in this library: its construction (Stacks 0BUP) is the composite of the functoriality map with the identifications of Stacks 0A48, 0BTW and 0A49, and none of those three is available here — 0BTW is proper base change over a henselian local ring, i.e. Stacks 0GS2, whose essential-surjectivity half is open (see `StacksFrontier.AlgebraicGeometry.FundamentalGroup.FiniteEtaleProperEquivalence`)”.

> **Stacks Project, Tag 0C0M**, the existence of the valuation ring. Let `φ : Spec K ⟶ S` be a
> geometric point of a scheme `S`, with `K` algebraically closed, and let the image of `φ`
> specialize to `s`. Then there is a strictly henselian valuation subring `A` of `K` — so a
> valuation ring with algebraically closed fraction field `K` and, as it happens, algebraically
> closed residue field — together with a morphism `r : Spec A ⟶ S` over which `φ` is the generic
> point and which carries the closed point of `Spec A` to `s`.

```lean
theorem exists_valuationSubring_strictlyHenselian_of_specializes
    {S : Scheme.{u}} {K : Type u} [Field K] [IsAlgClosed K] (φ : Spec (.of K) ⟶ S) {s : S}
    (h : φ (closedPoint K) ⤳ s) :
    ∃ A : ValuationSubring K, StrictlyHenselianLocalRing A ∧
      IsAlgClosed (IsLocalRing.ResidueField A) ∧
      ∃ r : Spec (.of A) ⟶ S,
        Spec.map (CommRingCat.ofHom (algebraMap A K)) ≫ r = φ ∧ r (closedPoint A) = s
```

## Tag 0C0N, a lemma

[Tag 0C0N](https://stacks.math.columbia.edu/tag/0C0N) in the Stacks Project.

**`AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_isDiscreteValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapDiscreteValuationRing.lean, line 764](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapDiscreteValuationRing.lean#L764). The attribute's comment: “the whole statement, with the same one input this library cannot prove carried as the hypothesis `h0A48`: `ProperHenselianFiniteEtaleEquivalence`, Tag 0A48 for a proper — not merely finite — scheme over a henselian local ring, whose remaining content is Grothendieck existence together with Artin approximation (see `StacksFrontier.AlgebraicGeometry.FundamentalGroup.FiniteEtaleAlgClosedExtension`). It is used exactly twice, for Tag 0A49 through `isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian_of_isAlgClosed` and for the closed geometric fibre of `X_R ⟶ Spec R`; it is the same datum that is already part of `AlgebraicGeometry.IsSpecializationMap`, so it constrains none of the data quantified over. Everything else is proved here: the discrete valuation ring (Tags 00PH, 0ARL and 0AP1), that the strict henselization of the stalk is Noetherian, the two factorizations of the geometric points, and the base-point bookkeeping. `sp_R` is produced as a specialization map in the sense of `AlgebraicGeometry.IsSpecializationMap`, and `R` is strictly henselian in the strong sense that its residue field is algebraically closed.”.

> **Stacks Project, Tag 0C0N.** Let `f : X ⟶ S` be a proper morphism with geometrically
> connected fibres over a Noetherian scheme, let `s'` and `s` be geometric points of `S`, and let
> `sp : π₁(X_{s'}) → π₁(X_s)` be a specialization map. Then there are a complete — in particular
> strictly henselian — discrete valuation ring `R` with algebraically closed residue field, a
> morphism `r : Spec R ⟶ S` carrying the generic point of `Spec R` to the image of `s'` and its
> closed point to the image of `s`, and a specialization map
> `sp_R : π₁((X_R)_{η̄}) → π₁((X_R)_{ō})` of the base change `X_R ⟶ Spec R` from the generic to the
> closed point, such that `sp` and `sp_R` are intertwined by isomorphisms of topological groups on
> the source and on the target.

```lean
theorem exists_isSpecializationMap_isomorphic_over_isDiscreteValuationRing
    {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f] [GeometricallyConnected f] [IsNoetherian S]
    (s' s : GeometricPoint S)
    (x' : GeometricPoint (fiberOverGeometricPoint f s'))
    (x : GeometricPoint (fiberOverGeometricPoint f s))
    (sp : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint f s) x)
    (hsp : IsSpecializationMap f s' s x' x sp)
    (h0A48 : ProperHenselianFiniteEtaleEquivalence.{u}) :
    ∃ (R : Type u) (_ : CommRing R) (_ : IsDomain R) (_ : IsDiscreteValuationRing R)
      (_ : HenselianLocalRing R) (_ : IsAlgClosed (ResidueField R))
      (r : Spec (.of R) ⟶ S) (η o : GeometricPoint (Spec (.of R)))
      (yη : GeometricPoint (fiberOverGeometricPoint (pullback.snd f r) η))
      (yo : GeometricPoint (fiberOverGeometricPoint (pullback.snd f r) o))
      (spR : EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) η) yη →ₜ*
        EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) o) yo),
      η.hom default = genericPoint (Spec (.of R)) ∧
      o.hom default = closedPoint R ∧
      r (η.hom default) = s'.hom default ∧
      r (o.hom default) = s.hom default ∧
      IsSpecializationMap (pullback.snd f r) η o yη yo spR ∧
      ∃ (eη : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' ≃ₜ*
            EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) η) yη)
        (eo : EtaleFundamentalGroup (fiberOverGeometricPoint f s) x ≃ₜ*
            EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) o) yo),
        ∀ γ, eo (sp γ) = spR (eη γ)
```

**`AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_strictlyHenselianDVR`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapStrictlyHenselianDiscreteValuationRing.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapStrictlyHenselianDiscreteValuationRing.lean#L63). The attribute's comment: “The full statement under the source's hypotheses; nothing is granted or assumed.”.

> **Stacks Project, Tag 0C0N.** Let `f : X ⟶ S` be a proper morphism with geometrically
> connected fibres over a Noetherian scheme `S`, let `s'` and `s` be geometric points of `S` and let
> `sp : π₁(X_{s̄'}) → π₁(X_{s̄})` be a specialization map. Then there are a strictly henselian
> discrete valuation ring `R` (whose residue field is even algebraically closed) and a morphism
> `r : Spec R ⟶ S` sending the generic point `η` of `Spec R` to the image of `s'` and its closed
> point `o` to the image of `s`, such that `sp` is isomorphic to the specialization map
> `sp_R : π₁((X_R)_{η̄}) → π₁((X_R)_{ō})` of the base change `X_R ⟶ Spec R`: there are isomorphisms
> of topological groups `π₁(X_{s̄'}) ≅ π₁((X_R)_{η̄})` and `π₁(X_{s̄}) ≅ π₁((X_R)_{ō})` intertwining
> `sp` and `sp_R`.
>
> This is `exists_isSpecializationMap_isomorphic_over_isDiscreteValuationRing` with its input
> Tag 0A48 supplied by `properHenselianFiniteEtaleEquivalence`.

```lean
theorem exists_isSpecializationMap_isomorphic_over_strictlyHenselianDVR
    {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f] [GeometricallyConnected f] [IsNoetherian S]
    (s' s : GeometricPoint S)
    (x' : GeometricPoint (fiberOverGeometricPoint f s'))
    (x : GeometricPoint (fiberOverGeometricPoint f s))
    (sp : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' →ₜ*
      EtaleFundamentalGroup (fiberOverGeometricPoint f s) x)
    (hsp : IsSpecializationMap f s' s x' x sp) :
    ∃ (R : Type u) (_ : CommRing R) (_ : IsDomain R) (_ : IsDiscreteValuationRing R)
      (_ : StrictlyHenselianLocalRing R) (_ : IsAlgClosed (ResidueField R))
      (r : Spec (.of R) ⟶ S) (η o : GeometricPoint (Spec (.of R)))
      (yη : GeometricPoint (fiberOverGeometricPoint (pullback.snd f r) η))
      (yo : GeometricPoint (fiberOverGeometricPoint (pullback.snd f r) o))
      (spR : EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) η) yη →ₜ*
        EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) o) yo),
      η.hom default = genericPoint (Spec (.of R)) ∧
      o.hom default = closedPoint R ∧
      r (η.hom default) = s'.hom default ∧
      r (o.hom default) = s.hom default ∧
      IsSpecializationMap (pullback.snd f r) η o yη yo spR ∧
      ∃ (eη : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' ≃ₜ*
            EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) η) yη)
        (eo : EtaleFundamentalGroup (fiberOverGeometricPoint f s) x ≃ₜ*
            EtaleFundamentalGroup (fiberOverGeometricPoint (pullback.snd f r) o) yo),
        ∀ γ, eo (sp γ) = spR (eη γ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.16, Tag 0BUP](https://stacks.math.columbia.edu/tag/0BUP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

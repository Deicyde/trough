---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_continuousMonoidHom_isSpecializationMap, AlgebraicGeometry.exists_isSpecializationMap_comm_square, AlgebraicGeometry.isSpecializationMap_comp, AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_strictlyHenselianValuationRing, AlgebraicGeometry.exists_valuationSubring_strictlyHenselian_of_specializes, AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_strictlyHenselianDVR
statement: formalized
proof: formalized
---

# 58.16 Specialization maps

Section 58.16 of the Stacks Project, [Tag 0BUP](https://stacks.math.columbia.edu/tag/0BUP). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BUP, the section

[Tag 0BUP](https://stacks.math.columbia.edu/tag/0BUP) in the Stacks Project.

**`AlgebraicGeometry.exists_continuousMonoidHom_isSpecializationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapConstruction.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapConstruction.lean#L62). The attribute's comment: “the construction of the specialization map: for `f` proper with geometrically connected fibres, a specialization `s' ⇝ s` and geometric points `s̄'`, `s̄` over them, a continuous homomorphism `π₁(X_{s̄'}) → π₁(X_{s̄})` which is the composite `π₁(X_{s̄'}) → π₁(X_A) = π₁(X_{κ(s)^{sep}}) = π₁(X_{s̄})` of the source, recorded by `AlgebraicGeometry.IsSpecializationMap`. As in the source the map depends on the choice of the factorization `φ : s̄' → Spec A`, so this is stated as existence. The equality `π₁(X_A) = π₁(X_{s̄})` is proved from Stacks 0A48, 0BTW and 0A49 by `AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_fiberOverGeometricPointMap`.”.

> **Stacks Project, Tag 0BUP.** Let `f : X ⟶ S` be a proper morphism with geometrically
> connected fibres, let `s' ⇝ s` be a specialization of points of `S`, let `s̄'` and `s̄` be
> geometric points over `s'` and `s`, and choose geometric base points of the two geometric fibres
> `X_{s̄'}` and `X_{s̄}`. Then there is a specialization map `π₁(X_{s̄'}) ⟶ π₁(X_{s̄})`, that is, a
> continuous homomorphism satisfying `AlgebraicGeometry.IsSpecializationMap`: it is the composite
> `π₁(X_{s̄'}) → π₁(X_A) ≅ π₁(X_{s̄})` for `A` the strict henselization of `𝒪_{S,s}` and a chosen
> factorization of `s̄'` through `Spec A`.
>
> The closed-fibre equivalence `π₁(X_A) ≅ π₁(X_{s̄})` is
> `isEquivalence_finiteEtaleBaseChange_fiberOverGeometricPointMap` (Stacks 0A48, 0BTW, 0A49).

```lean
theorem exists_continuousMonoidHom_isSpecializationMap (f : X ⟶ S) [IsProper f]
    [GeometricallyConnected f] (s' s : GeometricPoint S)
    (hspec : s'.hom (closedPoint s'.residueField) ⤳ s.hom (closedPoint s.residueField))
    (x' : GeometricPoint (fiberOverGeometricPoint f s'))
    (x : GeometricPoint (fiberOverGeometricPoint f s)) :
    ∃ sp : EtaleFundamentalGroup (fiberOverGeometricPoint f s') x' →ₜ*
        EtaleFundamentalGroup (fiberOverGeometricPoint f s) x,
      IsSpecializationMap f s' s x' x sp
```

## Tag 0C0K, a lemma

[Tag 0C0K](https://stacks.math.columbia.edu/tag/0C0K) in the Stacks Project.

**`AlgebraicGeometry.exists_isSpecializationMap_comm_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapSquare.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapSquare.lean#L58). The attribute's comment: “The whole statement, under exactly the source's hypotheses.”.

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

**`AlgebraicGeometry.isSpecializationMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMap.lean, line 525](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMap.lean#L525).

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

**`AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_strictlyHenselianValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapValuationRing.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapValuationRing.lean#L297).

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

**`AlgebraicGeometry.exists_valuationSubring_strictlyHenselian_of_specializes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationValuationRing.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationValuationRing.lean#L97). The attribute's comment: “the existence of the strictly henselian valuation ring `R` over `S` with algebraically closed fraction field realizing the specialization, which is the only step the Stacks proof argues; the comparison `sp ≅ sp_R` of specialization maps of fundamental groups is not formalized, because the specialization map `sp` cannot be constructed in this library: its construction (Stacks 0BUP) is the composite of the functoriality map with the identifications of Stacks 0A48, 0BTW and 0A49, and none of those three is available here — 0BTW is proper base change over a henselian local ring, i.e. Stacks 0GS2, whose essential-surjectivity half is open (see `StacksFrontier.AlgebraicGeometry.FundamentalGroup.FiniteEtaleProperEquivalence`)”.

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

**`AlgebraicGeometry.exists_isSpecializationMap_isomorphic_over_strictlyHenselianDVR`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapStrictlyHenselianDiscreteValuationRing.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/SpecializationMapStrictlyHenselianDiscreteValuationRing.lean#L69). The attribute's comment: “The full statement under the source's hypotheses, with no extra input: Tag 0A48 is supplied by `properHenselianFiniteEtaleEquivalence`. The source leaves "isomorphic" undefined; it is stated as a commutative square of isomorphisms of topological groups `eη`, `eo` with `eo ∘ sp = sp_R ∘ eη`. The ring `R` produced also has algebraically closed residue field.”.

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
> The proof follows the source: `exists_isSpecializationMap_isomorphic_over_isDiscreteValuationRing`
> builds the discrete valuation ring dominating the strict henselization `A` of `𝒪_{S,s}` (Tags 00PH,
> 0ARL, 0AP1) and the two comparison isomorphisms (Tag 0A49), taking Tag 0A48 for proper schemes
> over henselian local rings as an argument; that argument is the theorem
> `properHenselianFiniteEtaleEquivalence`, supplied here.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

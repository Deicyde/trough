---
declaration: section
origin: cited
lean: Module.Flat.injective_of_injective_mapQ_maximalIdeal_of_valuationRing, Module.Flat.flat_quotient_range_of_injective_mapQ_maximalIdeal_of_valuationRing, Stacks.RelativeAssassin.exists_valuation_base_change_generic_component, Stacks.RelativeAssassin.topologicalKrullDimAt_fiber_eq_fiber_of_flat, Stacks.RelativeAssassin.mem_relativeAssassin_of_isGenericPoint_fibre_closure, Stacks.RelativeAssassin.topologicalKrullDim_supp_fiber_le_of_generic, Stacks.RelativeAssassin.isDominant_closureSubschemeMap, Stacks.RelativeAssassin.relativeDimension_closureSubschemeMap
statement: formalized
proof: formalized
---

# 37.18 Flat modules and relative assassins

Section 37.18 of the Stacks Project, [Tag 0GSF](https://stacks.math.columbia.edu/tag/0GSF). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GSG, a lemma

[Tag 0GSG](https://stacks.math.columbia.edu/tag/0GSG) in the Stacks Project.

**`Module.Flat.injective_of_injective_mapQ_maximalIdeal_of_valuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/InjectiveModMaximalIdealOverValuationRing.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/InjectiveModMaximalIdealOverValuationRing.lean#L187). The attribute's comment: “injectivity”.

> **The injectivity half of Stacks 0GSG.** Let `A` be a valuation ring, let `A → B` be a local
> homomorphism of local rings which is essentially of finite type, and let `u : N → M` be a map of
> finite `B`-modules with `M` flat over `A`. If `ū : N/𝔪_A N → M/𝔪_A M` is injective then `u` is
> injective.

```lean
theorem injective_of_injective_mapQ_maximalIdeal_of_valuationRing
    {A : Type u₁} {B : Type u₂} {N : Type u₃} {M : Type u₄}
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [Algebra A B] [IsLocalRing B] [IsLocalHom (algebraMap A B)]
    [Algebra.EssFiniteType A B]
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N] [Module.Finite B N]
    [AddCommGroup M] [Module A M] [Module B M] [IsScalarTower A B M] [Module.Finite B M]
    [Module.Flat A M]
    (u : N →ₗ[B] M)
    (hu : Function.Injective
      (Submodule.mapQ (maximalIdeal A • (⊤ : Submodule A N))
        (maximalIdeal A • (⊤ : Submodule A M)) (u.restrictScalars A)
        (Submodule.smul_top_le_comap_smul_top (maximalIdeal A) (u.restrictScalars A)))) :
    Function.Injective u
```

**`Module.Flat.flat_quotient_range_of_injective_mapQ_maximalIdeal_of_valuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/InjectiveModMaximalIdealOverValuationRing.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/InjectiveModMaximalIdealOverValuationRing.lean#L208). The attribute's comment: “flatness of the cokernel”.

> **The cokernel half of Stacks 0GSG.** Let `A` be a valuation ring, let `A → B` be a local
> homomorphism of local rings which is essentially of finite type, and let `u : N → M` be a map of
> finite `B`-modules with `M` flat over `A`. If `ū : N/𝔪_A N → M/𝔪_A M` is injective then `M/u(N)`
> is flat over `A`.

```lean
theorem flat_quotient_range_of_injective_mapQ_maximalIdeal_of_valuationRing
    {A : Type u₁} {B : Type u₂} {N : Type u₃} {M : Type u₄}
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [Algebra A B] [IsLocalRing B] [IsLocalHom (algebraMap A B)]
    [Algebra.EssFiniteType A B]
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N] [Module.Finite B N]
    [AddCommGroup M] [Module A M] [Module B M] [IsScalarTower A B M] [Module.Finite B M]
    [Module.Flat A M]
    (u : N →ₗ[B] M)
    (hu : Function.Injective
      (Submodule.mapQ (maximalIdeal A • (⊤ : Submodule A N))
        (maximalIdeal A • (⊤ : Submodule A M)) (u.restrictScalars A)
        (Submodule.smul_top_le_comap_smul_top (maximalIdeal A) (u.restrictScalars A)))) :
    Module.Flat A (M ⧸ LinearMap.range u)
```

## Tag 0GSH, a lemma

[Tag 0GSH](https://stacks.math.columbia.edu/tag/0GSH) in the Stacks Project.

**`Stacks.RelativeAssassin.exists_valuation_base_change_generic_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ValuationBaseChange.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ValuationBaseChange.lean#L191).

> A valuation-ring base change through a prescribed generic point of a component of
> the fibre of the integral closure of a point.

```lean
theorem exists_valuation_base_change_generic_component
    {X S : Scheme.{u}} (f : X ⟶ S) (y : X)
    (Y : X.IdealSheafData)
    (hY : Y = Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({y} : Set X)))
    (s : S) (x : X)
    (ξ : (Y.subschemeι ≫ f).fiber s)
    (hξ : closure ({ξ} : Set ((Y.subschemeι ≫ f).fiber s)) ∈
      irreducibleComponents ((Y.subschemeι ≫ f).fiber s))
    (hx : Y.subschemeι ((Y.subschemeι ≫ f).fiberι s ξ) = x) :
    ∃ (A : Type u) (_ : CommRing A) (_ : IsDomain A) (_ : ValuationRing A)
      (g : Spec (.of A) ⟶ S),
      g (genericPoint (Spec (.of A))) = f y ∧
      g (closedPoint A) = s ∧
      (let X' := (pullback f g : Scheme.{u})
       let p : X' ⟶ X := pullback.fst f g
       let q : X' ⟶ Spec (.of A) := pullback.snd f g
       let Z : X'.IdealSheafData := Y.comap p
       let j : Z.subscheme ⟶ X' := Z.subschemeι
       ∃ η : (j ≫ q).fiber (genericPoint (Spec (.of A))),
         closure ({η} : Set ((j ≫ q).fiber (genericPoint (Spec (.of A))))) ∈
           irreducibleComponents ((j ≫ q).fiber (genericPoint (Spec (.of A)))) ∧
         p (j ((j ≫ q).fiberι (genericPoint (Spec (.of A))) η)) = y ∧
         (let y' : X' := j ((j ≫ q).fiberι (genericPoint (Spec (.of A))) η)
          let Y' : X'.IdealSheafData :=
            Scheme.IdealSheafData.vanishingIdeal (Closeds.closure ({y'} : Set X'))
          IsIntegral Y'.subscheme ∧
          ∃ ξ' : (Y'.subschemeι ≫ q).fiber (closedPoint A),
            closure ({ξ'} : Set ((Y'.subschemeι ≫ q).fiber (closedPoint A))) ∈
              irreducibleComponents ((Y'.subschemeι ≫ q).fiber (closedPoint A)) ∧
            p (Y'.subschemeι ((Y'.subschemeι ≫ q).fiberι (closedPoint A) ξ')) = x))
```

## Tag 0GSI, a lemma

[Tag 0GSI](https://stacks.math.columbia.edu/tag/0GSI) in the Stacks Project.

**`Stacks.RelativeAssassin.topologicalKrullDimAt_fiber_eq_fiber_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FlatFibreDimension.lean, line 894](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FlatFibreDimension.lean#L894). The attribute's comment: “the fibre dimension equality”. References: EGA IV (12.1.1.4), “fibre dimension equality”; EGA IV (12.1.1.5), “dim(Z'_y)=dim(Z'_{y'})”.

> **Fibre dimension at a generic point of the fibre of a closure.** Let `f : X ⟶ S` be locally
> of finite type, `F` a quasi-coherent finite type `𝒪_X`-module and `y` a point of `Ass_{X/S}(F)`.
> Let `Y` be the reduced closed subscheme supported on the closure of `y`. At a generic point `x`
> of an irreducible component of the fibre of `Y` over `s` at whose image `F` is flat over `S`, the
> local dimension of that fibre equals the dimension of the fibre of `Y` over `f y`.

```lean
theorem topologicalKrullDimAt_fiber_eq_fiber_of_flat
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (y : X) (hy : y ∈ Stacks.Divisors.relativeAssassin f F) (s : S) :
    let Y := Scheme.IdealSheafData.vanishingIdeal
      (⟨closure ({y} : Set X), isClosed_closure⟩ : Closeds X)
    let g : Y.subscheme ⟶ S := Y.subschemeι ≫ f
    ∀ x : g.fiber s,
      (∃ Z : irreducibleComponents (g.fiber s), IsGenericPoint x (Z : Set (g.fiber s))) →
      AlgebraicGeometry.IsFlatOverAt f.toLRSHom.toShHom F (Y.subschemeι (g.fiberι s x)) →
      topologicalKrullDimAt (g.fiber s) x = topologicalKrullDim (g.fiber (f y))
```

**`Stacks.RelativeAssassin.mem_relativeAssassin_of_isGenericPoint_fibre_closure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FlatFibreSpecialization.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FlatFibreSpecialization.lean#L228). The attribute's comment: “the relative assassin conclusion”. References: EGA IV (12.1.1.4), “z ∈ Ass(F_y)”; EGA IV (12.1.1.5), “z ∈ Ass(F_y)”.

> **Relative associated points at generic points of the fibres of a closure.** Let
> `f : X ⟶ S` be locally of finite type, `F` a quasi-coherent finite type `𝒪_X`-module and `y` a
> point of `Ass_{X/S}(F)`. Let `Y` be the reduced closed subscheme supported on the closure of `y`
> and let `ξ` be a generic point of an irreducible component of the fibre of `Y` over a point `s`
> of `S`. If `F` is flat over `S` at the image of `ξ` in `X`, that image lies in
> `Ass_{X/S}(F)`.

```lean
theorem mem_relativeAssassin_of_isGenericPoint_fibre_closure
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (y : X) (hy : y ∈ Stacks.Divisors.relativeAssassin f F)
    (Y : X.IdealSheafData)
    (hY : Y = Scheme.IdealSheafData.vanishingIdeal (Closeds.closure ({y} : Set X)))
    (s : S) (ξ : (Y.subschemeι ≫ f).fiber s)
    (hξ : closure ({ξ} : Set ((Y.subschemeι ≫ f).fiber s)) ∈
      irreducibleComponents ((Y.subschemeι ≫ f).fiber s))
    (hflat : IsFlatOverAt f.toLRSHom.toShHom F
      (Y.subschemeι ((Y.subschemeι ≫ f).fiberι s ξ))) :
    Y.subschemeι ((Y.subschemeι ≫ f).fiberι s ξ)
      ∈ Stacks.Divisors.relativeAssassin f F
```

## Tag 0H3X, a lemma

[Tag 0H3X](https://stacks.math.columbia.edu/tag/0H3X) in the Stacks Project.

**`Stacks.RelativeAssassin.topologicalKrullDim_supp_fiber_le_of_generic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FlatFibreSupportDimension.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FlatFibreSupportDimension.lean#L390).

> **Stacks Project, Tag 0H3X.** The dimension of the support of a finite type quasi-coherent
> module flat over an irreducible base does not increase from the generic fibre to any other
> fibre.

```lean
theorem topologicalKrullDim_supp_fiber_le_of_generic
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    (hF : AlgebraicGeometry.IsFlatOver f.toLRSHom.toShHom F)
    [IrreducibleSpace S] (η : S) (hη : IsGenericPoint η Set.univ)
    (r : WithBot ℕ∞)
    (hdim : topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι η)).obj F)) ≤
        r)
    (s : S) :
    topologicalKrullDim
      (SheafOfModules.supp ((Scheme.Modules.pullback (f.fiberι s)).obj F)) ≤
        r
```

## Tag 0GSJ, a lemma

[Tag 0GSJ](https://stacks.math.columbia.edu/tag/0GSJ) in the Stacks Project.

**`Stacks.RelativeAssassin.isDominant_closureSubschemeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ClosureRelativeDimension.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ClosureRelativeDimension.lean#L131). The attribute's comment: “dominance of the canonical map”.

> The canonical map from the reduced closure of a point to the reduced closure
> of its image is dominant.

```lean
theorem isDominant_closureSubschemeMap
    {X S : Scheme.{u}} (f : X ⟶ S) (y : X) :
    let Y := Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({y} : Set X))
    let T := Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({f y} : Set S))
    let h : Y.subscheme ⟶ T.subscheme :=
      Scheme.IdealSheafData.subschemeMap Y T f (by
        rw [Scheme.IdealSheafData.map_vanishingIdeal]
        apply le_of_eq
        apply congrArg Scheme.IdealSheafData.vanishingIdeal
        apply Closeds.ext
        change closure ({f y} : Set S) = closure (f '' closure ({y} : Set X))
        exact ((closure_image_closure f.continuous).trans (by simp)).symm)
    IsDominant h
```

**`Stacks.RelativeAssassin.relativeDimension_closureSubschemeMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ClosureRelativeDimension.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ClosureRelativeDimension.lean#L212). The attribute's comment: “part (2)”. References: EGA IV (12.1.1.4), “equidimensional Z'→Y'”; EGA IV (12.1.1.5), “equidimensionality”.

> If the module is flat at component-generic fibre points, the canonical map
> from the reduced closure of a relative associated point to the reduced closure
> of its image has constant relative dimension.

```lean
theorem relativeDimension_closureSubschemeMap
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (y : X) (hy : y ∈ Stacks.Divisors.relativeAssassin f F) :
    let Y := Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({y} : Set X))
    let T := Scheme.IdealSheafData.vanishingIdeal
      (Closeds.closure ({f y} : Set S))
    let h : Y.subscheme ⟶ T.subscheme :=
      Scheme.IdealSheafData.subschemeMap Y T f (by
        rw [Scheme.IdealSheafData.map_vanishingIdeal]
        apply le_of_eq
        apply congrArg Scheme.IdealSheafData.vanishingIdeal
        apply Closeds.ext
        change closure ({f y} : Set S) = closure (f '' closure ({y} : Set X))
        exact ((closure_image_closure f.continuous).trans (by simp)).symm)
    (∀ t : T.subscheme, ∀ x : h.fiber t,
      (∃ Z : irreducibleComponents (h.fiber t),
        IsGenericPoint x (Z : Set (h.fiber t))) →
      AlgebraicGeometry.IsFlatOverAt f.toLRSHom.toShHom F
        (Y.subschemeι (h.fiberι t x))) →
    let hh : LocallyOfFiniteType h := by
      have : LocallyOfFiniteType (h ≫ T.subschemeι) := by
        rw [Scheme.IdealSheafData.subschemeMap_subschemeι]
        infer_instance
      exact locallyOfFiniteType_of_comp h T.subschemeι
    letI : LocallyOfFiniteType h := hh
    ∃ d : ℕ, RelativeDimension h d
```

Declarations registered for the tag:

- [`Stacks.RelativeAssassin.mem_relativeAssassin_of_isGenericPoint_fibre_closure`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/FlatFibreSpecialization.lean#L228), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ClosureRelativeDimension.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/ClosureRelativeDimension.lean#L125) (StacksFrontier): “part (1)”.

## Tag 0GSK, a remark

[Tag 0GSK](https://stacks.math.columbia.edu/tag/0GSK) in the Stacks Project.

**`Stacks.RelativeAssassin.relativeDimension_of_isGenericPoint_of_trdeg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/RelativeDimensionCriteria.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/RelativeDimensionCriteria.lean#L324). The attribute's comment: “first set of hypotheses”.

> **Stacks Project, Tag 0GSK, first set of hypotheses.** Let `f : X ⟶ S` be locally of finite
> type with `X` integral of generic point `ξ`, and let `F` be a quasi-coherent `𝒪_X`-module of
> finite type whose support is all of `X` and which is flat over `S` at every generic point of
> every fibre. If the transcendence degree of `κ(ξ)` over `κ(f ξ)` is `d`, then `f` has relative
> dimension `d` in the sense of Tag 02NJ.
>
> Only the irreducibility of `X` is used, not its reducedness, and the flatness hypothesis is the
> one the source's last sentence allows; flatness of `F` over `S` everywhere, which the source's
> list asks for, gives it as `fun s z _ => hF _`.

```lean
theorem relativeDimension_of_isGenericPoint_of_trdeg (f : X ⟶ S) [LocallyOfFiniteType f]
    [IsIntegral X] (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hsupp : SheafOfModules.supp F = Set.univ)
    (hflat : ∀ (s : S) (z : f.fiber s), z ∈ genericPoints (f.fiber s) →
      AlgebraicGeometry.IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s z))
    (ξ : X) (hξ : IsGenericPoint ξ (Set.univ : Set X)) (d : ℕ)
    (hd : letI := (f.residueFieldMap ξ).hom.toAlgebra
      Cardinal.toENat (Algebra.trdeg (S.residueField (f ξ)) (X.residueField ξ)) = (d : ℕ∞)) :
    AlgebraicGeometry.RelativeDimension f d
```

**`Stacks.RelativeAssassin.relativeDimension_of_dense_fiber_of_component_dim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/RelativeDimensionCriteria.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/RelativeAssassin/RelativeDimensionCriteria.lean#L442). The attribute's comment: “second set of hypotheses”.

> **Stacks Project, Tag 0GSK, second set of hypotheses.** Let `f : X ⟶ S` be locally of finite
> type and let `F` be a quasi-coherent `𝒪_X`-module of finite type whose support is all of `X` and
> which is flat over `S` at every generic point of every fibre. If the fibre over a point `η` of
> `S` is dense in `X` and every irreducible component of that fibre has dimension `d`, then `f` has
> relative dimension `d` in the sense of Tag 02NJ.
>
> The source asks in addition that `S` be irreducible with `η` its generic point, which is what
> makes the density plausible; the argument uses only the density itself, so that hypothesis is
> dropped here and the source's statement is the case of an irreducible `S` and its generic
> point. The flatness hypothesis is again the weakened one of the source's last sentence.

```lean
theorem relativeDimension_of_dense_fiber_of_component_dim (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType]
    (hsupp : SheafOfModules.supp F = Set.univ)
    (hflat : ∀ (s : S) (z : f.fiber s), z ∈ genericPoints (f.fiber s) →
      AlgebraicGeometry.IsFlatOverAt f.toLRSHom.toShHom F (f.fiberι s z))
    (η : S) (hdense : Dense (f ⁻¹' ({η} : Set S))) (d : ℕ)
    (hdim : ∀ Z ∈ irreducibleComponents (f.fiber η), topologicalKrullDim Z = (d : WithBot ℕ∞)) :
    AlgebraicGeometry.RelativeDimension f d
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.18, Tag 0GSF](https://stacks.math.columbia.edu/tag/0GSF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

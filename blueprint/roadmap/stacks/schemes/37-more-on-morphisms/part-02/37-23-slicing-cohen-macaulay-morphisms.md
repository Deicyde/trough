---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.exists_affineOpen_effectiveCartierDivisor_of_isRegular_fiber, Stacks.AlgebraicGeometry.exists_affineOpen_regularImmersion_flat_of_isRegular_fiber, Stacks.AlgebraicGeometry.exists_affineOpen_effectiveCartierDivisor_of_one_le_depth, Stacks.AlgebraicGeometry.exists_regularImmersion_flat_locallyQuasiFinite_singleton_fiber_of_isCohenMacaulayAt, AlgebraicGeometry.exists_flat_locallyQuasiFinite_factorization_through, AlgebraicGeometry.hasLocallyQuasiFiniteRefinement
statement: formalized
proof: formalized
---

# 37.23 Slicing Cohen-Macaulay morphisms

Section 37.23 of the Stacks Project, [Tag 056X](https://stacks.math.columbia.edu/tag/056X). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 056Y, a lemma

[Tag 056Y](https://stacks.math.columbia.edu/tag/056Y) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_affineOpen_effectiveCartierDivisor_of_isRegular_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/EffectiveCartierSlice.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/EffectiveCartierSlice.lean#L214).

> Let `f : X ⟶ S` be locally of finite presentation and flat at `x : X`, and let `h` be an
> element of the maximal ideal of `𝒪_{X, x}` whose image in the local ring of the fibre `X_{f x}`
> at `x` is a nonzerodivisor.  Then there is an affine open `U ∋ x` and a global section `a` of `U`
> whose germ at `x` is `h`, such that the zero scheme `V(a) ⊆ U` is an effective Cartier divisor
> containing `x` which is flat and locally of finite presentation over `S`.

```lean
theorem exists_affineOpen_effectiveCartierDivisor_of_isRegular_fiber (f : X ⟶ S)
    [LocallyOfFinitePresentation f] (x : X) (h : X.presheaf.stalk x)
    (hh : h ∈ IsLocalRing.maximalIdeal (X.presheaf.stalk x))
    (hflat : IsFlatAt f.toLRSHom.toShHom x)
    (hregular : IsRegular (((f.fiberι (f x)).stalkMap (f.asFiber x)).hom
      ((f.fiberι_asFiber x).symm ▸ h))) :
    ∃ (U : X.affineOpens) (hx : x ∈ U.1) (a : Γ(U.1.toScheme, ⊤)),
      let y : U.1.toScheme := ⟨x, hx⟩
      let I : U.1.toScheme.IdealSheafData :=
        Scheme.IdealSheafData.ofIdealTop (Ideal.span {a})
      (U.1.ι.stalkMap y).hom ((show U.1.ι y = x by rfl).symm ▸ h) =
          U.1.toScheme.presheaf.germ ⊤ y (by trivial) a ∧
        y ∈ I.support ∧
        Stacks.Divisors.IsEffectiveCartierDivisor I ∧
        Flat (I.subschemeι ≫ U.1.ι ≫ f) ∧
        LocallyOfFinitePresentation (I.subschemeι ≫ U.1.ι ≫ f)
```

## Tag 06LI, a lemma

[Tag 06LI](https://stacks.math.columbia.edu/tag/06LI) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_affineOpen_regularImmersion_flat_of_isRegular_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/RegularSliceThroughPoint.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/RegularSliceThroughPoint.lean#L74). References: EGA IV (11.3.8), “c) ⇒ b') for F = O\_X”.

> **Stacks Project, Lemma 37.23.2 (Tag 06LI).**  Let `f : X ⟶ S` be locally of finite
> presentation and flat at `x : X`, and let `h : Fin r → 𝒪_{X, x}` be a family whose image in the
> local ring of the fibre `X_{f x}` at `x` is a regular sequence.  Then there is an affine open `U`
> containing `x` and global sections `a : Fin r → Γ(U, ⊤)` whose germs at `x` are the `h i`, such
> that `x` lies on the zero scheme `V(a)`, the closed immersion of `V(a)` into `U` is a regular
> immersion, `V(a)` is flat and locally of finite presentation over `S`, and the base change of
> the immersion along any `S' ⟶ S` is again a regular immersion.

```lean
theorem exists_affineOpen_regularImmersion_flat_of_isRegular_fiber
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) {r : ℕ}
    (h : Fin r → X.presheaf.stalk x) [LocallyOfFinitePresentation f]
    (hflat : IsFlatAt f.toLRSHom.toShHom x)
    (hregular : RingTheory.Sequence.IsRegular
      ((f.fiber (f x)).presheaf.stalk (f.asFiber x))
      (List.ofFn fun i : Fin r =>
        ((f.fiberι (f x)).stalkMap (f.asFiber x)).hom ((f.fiberι_asFiber x).symm ▸ h i))) :
    ∃ (U : X.affineOpens) (hx : x ∈ U.1) (a : Fin r → Γ(U.1.toScheme, ⊤)),
      let y : U.1.toScheme := ⟨x, hx⟩
      let I : U.1.toScheme.IdealSheafData :=
        Scheme.IdealSheafData.ofIdealTop (Ideal.ofList (List.ofFn a))
      (∀ i : Fin r, (U.1.ι.stalkMap y).hom ((show U.1.ι y = x by rfl).symm ▸ h i) =
          U.1.toScheme.presheaf.germ ⊤ y (by trivial) (a i)) ∧
      y ∈ I.support ∧
      IsRegularImmersion I.subschemeι ∧
      Flat (I.subschemeι ≫ U.1.ι ≫ f) ∧
      LocallyOfFinitePresentation (I.subschemeι ≫ U.1.ι ≫ f) ∧
      ∀ (S' : Scheme.{u}) (g : S' ⟶ S),
        IsRegularImmersion (pullback.snd I.subschemeι (pullback.fst (U.1.ι ≫ f) g))
```

## Tag 056Z, a lemma

[Tag 056Z](https://stacks.math.columbia.edu/tag/056Z) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_affineOpen_effectiveCartierDivisor_of_one_le_depth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/EffectiveCartierSlice.lean, line 367](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/EffectiveCartierSlice.lean#L367). References: EGA IV (19.9.6), “n = 1, F = O\_X”.

> Let `f : X ⟶ S` be locally of finite presentation and flat at `x : X`, and assume the local
> ring of the fibre `X_{f x}` at `x` has depth at least one.  Then some affine open neighbourhood
> of `x` carries an effective Cartier divisor through `x` which is flat and locally of finite
> presentation over `S`.

```lean
theorem exists_affineOpen_effectiveCartierDivisor_of_one_le_depth (f : X ⟶ S)
    [LocallyOfFinitePresentation f] (x : X) (hflat : IsFlatAt f.toLRSHom.toShHom x)
    (hdepth : (1 : ℕ∞) ≤
      Module.depth ((f.fiber (f x)).presheaf.stalk (f.asFiber x))
        (IsLocalRing.maximalIdeal ((f.fiber (f x)).presheaf.stalk (f.asFiber x)))
        ((f.fiber (f x)).presheaf.stalk (f.asFiber x))) :
    ∃ (U : X.affineOpens) (I : U.1.toScheme.IdealSheafData),
      x ∈ Set.range (I.subschemeι ≫ U.1.ι) ∧
        Stacks.Divisors.IsEffectiveCartierDivisor I ∧
        Flat (I.subschemeι ≫ U.1.ι ≫ f) ∧
        LocallyOfFinitePresentation (I.subschemeι ≫ U.1.ι ≫ f)
```

## Tag 0570, a lemma

[Tag 0570](https://stacks.math.columbia.edu/tag/0570) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_regularImmersion_flat_locallyQuasiFinite_singleton_fiber_of_isCohenMacaulayAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/RegularSliceThroughPoint.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/RegularSliceThroughPoint.lean#L110). References: EGA IV (19.2.9), “x closed in fibre”; EGA IV (17.16.1).

> **Stacks Project, Lemma 37.23.4 (Tag 0570).**  Let `f : X ⟶ S` be locally of finite
> presentation, let `x : X` be a point at which `f` is Cohen–Macaulay, and assume `x` is closed in
> its fibre `X_{f x}`.  Then there is a regular immersion `i : Z ⟶ X` through `x` such that `Z` is
> flat, locally of finite presentation and locally quasi-finite over `S`, and such that the fibre
> of `Z` over `f x` is set-theoretically the single point of `Z` above `x`.

```lean
theorem exists_regularImmersion_flat_locallyQuasiFinite_singleton_fiber_of_isCohenMacaulayAt
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f] (x : X)
    (hCM : ∃ hf : ∀ y : S, IsLocallyNoetherian (f.fiber y),
      Scheme.Hom.IsCohenMacaulayAt f hf x)
    (hclosed : IsClosed ({f.asFiber x} : Set (f.fiber (f x)))) :
    ∃ (Z : Scheme.{u}) (i : Z ⟶ X) (z : Z) (hi : IsImmersion i),
      letI := hi
      i z = x ∧ IsRegularImmersion i ∧
        Flat (i ≫ f) ∧ LocallyOfFinitePresentation (i ≫ f) ∧
        LocallyQuasiFinite (i ≫ f) ∧
        {z' : Z | (i ≫ f) z' = f x} = {z}
```

## Tag 0571, a lemma

[Tag 0571](https://stacks.math.columbia.edu/tag/0571) in the Stacks Project.

**`AlgebraicGeometry.exists_flat_locallyQuasiFinite_factorization_through`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/QuasiFiniteSlices.lean, line 559](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/QuasiFiniteSlices.lean#L559).

> A point in the image of a flat morphism `f : X ⟶ S` locally of
> finite presentation lies in the image of some `g : S' ⟶ S` which factors as `h ≫ f` through `f`
> and is flat, locally of finite presentation and locally quasi-finite.

```lean
theorem exists_flat_locallyQuasiFinite_factorization_through
    {X S : Scheme.{u}} (f : X ⟶ S) [Flat f] [LocallyOfFinitePresentation f]
    (s : S) (hs : s ∈ Set.range f) :
    ∃ (S' : Scheme.{u}) (g : S' ⟶ S) (h : S' ⟶ X),
      h ≫ f = g ∧ Flat g ∧ LocallyOfFinitePresentation g ∧
        LocallyOfFiniteType g ∧ LocallyQuasiFinite g ∧ s ∈ Set.range g
```

## Tag 0572, a lemma

[Tag 0572](https://stacks.math.columbia.edu/tag/0572) in the Stacks Project.

**`AlgebraicGeometry.hasLocallyQuasiFiniteRefinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/LocallyQuasiFiniteRefinement.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/LocallyQuasiFiniteRefinement.lean#L126).

> **Stacks Project, Tag 0572.** An fppf covering `𝒰` of a scheme `S` is refined by an fppf
> covering `{T_j ⟶ S}`, indexed by the points of `S`, each member of which is locally
> quasi-finite over `S`.

```lean
theorem hasLocallyQuasiFiniteRefinement {S : Scheme.{u}}
    (𝒰 : S.Cover.{v} Scheme.fppfPrecoverage) :
    HasLocallyQuasiFiniteRefinement 𝒰
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.23, Tag 056X](https://stacks.math.columbia.edu/tag/056X)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

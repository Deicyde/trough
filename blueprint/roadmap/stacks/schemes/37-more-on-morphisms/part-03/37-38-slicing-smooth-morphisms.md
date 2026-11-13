---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.exists_smooth_effectiveCartierDivisor_of_nonzero_differential, Stacks.AlgebraicGeometry.exists_smooth_divisor_of_nonzero_differential_kernel, Stacks.AlgebraicGeometry.not_exists_etale_lift_through_inseparableClosedPoint, Stacks.AlgebraicGeometry.exists_smooth_divisor_of_separable_residueField, Stacks.AlgebraicGeometry.exists_etale_immersion_with_singleton_fiber, AlgebraicGeometry.exists_etaleNeighborhood_lift_of_smooth, AlgebraicGeometry.exists_etale_cover_refining_smooth_cover, AlgebraicGeometry.exists_etaleCover_factors_affine_smooth_section
statement: formalized
proof: formalized
---

# 37.38 Slicing smooth morphisms

Section 37.38 of the Stacks Project, [Tag 055S](https://stacks.math.columbia.edu/tag/055S). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 057C, a lemma

[Tag 057C](https://stacks.math.columbia.edu/tag/057C) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_smooth_effectiveCartierDivisor_of_nonzero_differential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/SmoothSlice/SmoothDivisor.lean, line 693](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/SmoothSlice/SmoothDivisor.lean#L693). References: SGA 1 II (4.12), “dF(x)≠0 ⇒ Y smooth”.

> **Stacks Project, Tag 057C.** A local equation with nonzero relative
> differential cuts out a smooth effective Cartier divisor near the point.

```lean
public theorem exists_smooth_effectiveCartierDivisor_of_nonzero_differential
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X)
    (h : X.presheaf.stalk x)
    (hh : h ∈ IsLocalRing.maximalIdeal (X.presheaf.stalk x))
    (hf : InfinitesimalLifting.SmoothAt f x)
    (hdh : HasNonzeroRelativeDifferential f x h) :
    ∃ (U : X.Opens) (_hU : IsAffineOpen U) (hxU : x ∈ U)
      (a : Γ(X, U)) (I : U.toScheme.IdealSheafData),
      ((TopCat.Presheaf.germ X.presheaf U x hxU).hom a = h) ∧
      (∀ V : U.toScheme.affineOpens,
        I.ideal V = Ideal.span
          {((U.toScheme.presheaf.map (homOfLE le_top).op).hom
            (U.topIso.inv.hom a))}) ∧
      Stacks.Divisors.IsEffectiveCartierDivisor I ∧
      (⟨x, hxU⟩ : U.toScheme) ∈ I.support ∧
      Smooth (I.subschemeι ≫ U.ι ≫ f)
```

## Tag 057D, a lemma

[Tag 057D](https://stacks.math.columbia.edu/tag/057D) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_smooth_divisor_of_nonzero_differential_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/SmoothSliceCriteria.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/SmoothSliceCriteria.lean#L267).

> **Stacks Project, Tag 057D.**  Let `f : X ⟶ S` be smooth at `x`, with image `s = f x`.  If
> the map `Ω_{X_s/s,x} ⊗_{𝒪_{X_s,x}} κ(x) ⟶ Ω_{κ(x)/κ(s)}` has a nonzero kernel, then there is an
> affine open neighbourhood `U` of `x` and an effective Cartier divisor `D ⊆ U` containing `x`
> with `D ⟶ S` smooth.

```lean
public theorem exists_smooth_divisor_of_nonzero_differential_kernel
    (hf : InfinitesimalLifting.SmoothAt f x)
    (hker :
      letI := algebraResidueFiber f x
      letI := algebraFiberResidue f x
      letI := algebraTargetResidueResidueField f x
      letI := isScalarTower_targetResidue_fiberStalk_residueField f x
      ¬ Function.Injective (KaehlerDifferential.mapBaseChange (targetResidue f x)
        (ToType ((f.fiber (f x)).sheaf.presheaf.stalk (fiberPoint f x)))
        (ToType (X.residueField x)))) :
    ∃ (U : X.Opens) (_hU : IsAffineOpen U) (hxU : x ∈ U)
      (I : U.toScheme.IdealSheafData),
      Stacks.Divisors.IsEffectiveCartierDivisor I ∧
      (⟨x, hxU⟩ : U.toScheme) ∈ I.support ∧
      Smooth (I.subschemeι ≫ U.ι ≫ f)
```

## Tag 057E, a remark

[Tag 057E](https://stacks.math.columbia.edu/tag/057E) in the Stacks Project.

**`Stacks.AlgebraicGeometry.not_exists_etale_lift_through_inseparableClosedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/InseparableSliceObstruction.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/InseparableSliceObstruction.lean#L297).

> **No étale lift through an inseparable closed point.**  Let `k` be a field of characteristic
> `p > 0` and let `a ∈ k` not be a `p`-th power, so that `k` is imperfect.  For the closed point `w`
> of `X = 𝐀²_k` given by the maximal ideal `(x, y^p - a)` and the projection `f : X ⟶ S = 𝐀¹_k`,
> there is no commutative diagram `h : S' ⟶ X`, `g : S' ⟶ S` with `h ≫ f = g`, `g` étale, and `w`
> in the image of `h`.

```lean
theorem not_exists_etale_lift_through_inseparableClosedPoint {k : Type u} [Field k] {p : ℕ}
    [Fact p.Prime] [CharP k p] (a : k) (ha : ∀ b : k, b ^ p ≠ a) :
    ¬ ∃ (S' : Scheme.{u}) (g : S' ⟶ affineLine k) (h : S' ⟶ affinePlane k),
        Etale g ∧ h ≫ projection k = g ∧ closedPoint a ha ∈ Set.range h.base
```

## Tag 057F, a lemma

[Tag 057F](https://stacks.math.columbia.edu/tag/057F) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_smooth_divisor_of_separable_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/SmoothSliceCriteria.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/SmoothSliceCriteria.lean#L465).

> **Stacks Project, Tag 057F.**  Let `f : X ⟶ S` be smooth at `x`, with image `s = f x`.  If
> the residue field extension `κ(x)/κ(s)` is separable and `x` is not a generic point of the fibre
> `X_s`, then there is an affine open neighbourhood `U` of `x` and an effective Cartier divisor
> `D ⊆ U` containing `x` with `D ⟶ S` smooth.

```lean
public theorem exists_smooth_divisor_of_separable_residueField
    (hf : InfinitesimalLifting.SmoothAt f x)
    (hsep : letI := (f.residueFieldMap x).hom.toAlgebra
      Algebra.IsSeparableExtension (ToType (S.residueField (f x)))
        (ToType (X.residueField x)))
    (hngen : f.asFiber x ∉ genericPoints (f.fiber (f x))) :
    ∃ (U : X.Opens) (_hU : IsAffineOpen U) (hxU : x ∈ U)
      (I : U.toScheme.IdealSheafData),
      Stacks.Divisors.IsEffectiveCartierDivisor I ∧
      (⟨x, hxU⟩ : U.toScheme) ∈ I.support ∧
      Smooth (I.subschemeι ≫ U.ι ≫ f)
```

## Tag 057G, a lemma

[Tag 057G](https://stacks.math.columbia.edu/tag/057G) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_etale_immersion_with_singleton_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/EtaleSlice.lean, line 504](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/CohenMacaulaySlice/EtaleSlice.lean#L504). References: EGA IV (17.16.3), “Clause (i)”; SGA 3 XI (1.10), “more general”.

> **Stacks Project, Tag 057G.**  Let `f : X ⟶ S` be a morphism of schemes, `x : X` a point with
> image `s = f x`.  If `f` is smooth at `x`, if `x` is a closed point of the fibre `X_s`, and if the
> residue field extension `κ(x)/κ(s)` is separable, then there is an immersion `i : Z ⟶ X` whose
> image contains `x` such that `Z ⟶ S` is étale and `Z_s = {x}` set theoretically.

```lean
public theorem exists_etale_immersion_with_singleton_fiber
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X)
    (hsmooth : InfinitesimalLifting.SmoothAt f x)
    (hclosed : IsClosed ({f.asFiber x} : Set (f.fiber (f x))))
    (hsep : letI := (f.residueFieldMap x).hom.toAlgebra
      Algebra.IsSeparableExtension (S.residueField (f x)) (X.residueField x)) :
    ∃ (Z : Scheme.{u}) (i : Z ⟶ X) (z : Z),
      IsImmersion i ∧ i z = x ∧ Etale (i ≫ f) ∧
        {z' : Z | (i ≫ f) z' = f x} = {z}
```

## Tag 055U, a lemma

[Tag 055U](https://stacks.math.columbia.edu/tag/055U) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_lift_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/EtaleLocalSection.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Smooth/EtaleLocalSection.lean#L241).

> **Stacks Project, Tag 055U.** A smooth morphism admits an étale local section through any
> point of its image.

```lean
theorem exists_etaleNeighborhood_lift_of_smooth {X S : Scheme.{u}}
    (f : X ⟶ S) [Smooth f] (s : S) (hs : s ∈ Set.range f.base) :
    ∃ (W : EtaleNeighborhood S s) (g : W.scheme ⟶ X), g ≫ f = W.toBase
```

## Tag 055V, a lemma

[Tag 055V](https://stacks.math.columbia.edu/tag/055V) in the Stacks Project.

**`AlgebraicGeometry.exists_etale_cover_refining_smooth_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmoothRefinement.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/Etale/SmoothRefinement.lean#L49).

> **Stacks Project, Tag 055V.** Every smooth covering of a scheme is refined by an étale
> covering.

```lean
public theorem exists_etale_cover_refining_smooth_cover {S : Scheme.{u}}
    (𝒰 : S.Cover.{v} (Scheme.precoverage (@Smooth.{u}))) :
    ∃ 𝒱 : S.Cover.{u} (Scheme.precoverage (@Etale.{u})),
      Nonempty (𝒱.toPreZeroHypercover.Hom 𝒰.toPreZeroHypercover)
```

## Tag 0EY4, a lemma

[Tag 0EY4](https://stacks.math.columbia.edu/tag/0EY4) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleCover_factors_affine_smooth_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SlicingSmooth/AffineConnectedCover.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SlicingSmooth/AffineConnectedCover.lean#L176).

> A smooth morphism of schemes admits an étale covering of its source each member of which maps
> to the base through an étale morphism, the first factor being a smooth morphism of affine schemes
> which has a section and has geometrically connected fibres.

```lean
theorem exists_etaleCover_factors_affine_smooth_section {X S : Scheme.{u}} (f : X ⟶ S)
    [Smooth f] :
    ∃ 𝒰 : X.Cover.{u} Scheme.etalePrecoverage, ∀ i : 𝒰.I₀,
      ∃ (Bᵢ : Scheme.{u}) (h : Bᵢ ⟶ S) (g : 𝒰.X i ⟶ Bᵢ) (σ : Bᵢ ⟶ 𝒰.X i),
        Etale h ∧ IsAffine (𝒰.X i) ∧ IsAffine Bᵢ ∧ Smooth g ∧ σ ≫ g = 𝟙 Bᵢ ∧
          GeometricallyConnected g ∧ g ≫ h = 𝒰.f i ≫ f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.38, Tag 055S](https://stacks.math.columbia.edu/tag/055S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_affineOpen_quasiFinite_affineSpace_factorization, AlgebraicGeometry.exists_factorization_finite_fiber, AlgebraicGeometry.exists_isImmersion_specMap_derivativePair_of_unramifiedAt, AlgebraicGeometry.exists_isOpenImmersion_specMap_derivativePair_of_etaleAt, AlgebraicGeometry.finiteDimensional_relativeCotangentSpace, AlgebraicGeometry.finrank_relativeCotangentSpace_eq_fiberRelativeCotangentSpace, AlgebraicGeometry.finrank_relativeCotangentSpace_eq_finrank_dottedTangentArrow, AlgebraicGeometry.exists_factorization_unramifiedAt
statement: formalized
proof: formalized
---

# 33.18 Variants of Noether normalization

Section 33.18 of the Stacks Project, [Tag 0CBG](https://stacks.math.columbia.edu/tag/0CBG). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CBH, a lemma

[Tag 0CBH](https://stacks.math.columbia.edu/tag/0CBH) in the Stacks Project.

**`AlgebraicGeometry.exists_affineOpen_quasiFinite_affineSpace_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean#L155). References: EGA IV (13.3.1.1), “quasi-finite factoriz.”.

> Relative Noether normalization on an affine neighbourhood of a point.

```lean
theorem exists_affineOpen_quasiFinite_affineSpace_factorization
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (x : X) (V : S.affineOpens) (hxV : f x ∈ V.1) (d : ℕ)
    (hd : topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) = (d : WithBot ℕ∞)) :
    ∃ (U : X.affineOpens) (_hxU : x ∈ U.1)
      (_hUV : U.1 ≤ f ⁻¹ᵁ V.1)
      (π : U.1.toScheme ⟶ AffineSpace (ULift.{u} (Fin d)) V.1.toScheme),
      (π ≫ (AffineSpace.over (ULift.{u} (Fin d)) V.1.toScheme).hom ≫ V.1.ι =
        U.1.ι ≫ f) ∧
      ((LocallyOfFiniteType π ∧ QuasiCompact π) ∧ LocallyQuasiFinite π)
```

## Tag 0CBI, a lemma

[Tag 0CBI](https://stacks.math.columbia.edu/tag/0CBI) in the Stacks Project.

**`AlgebraicGeometry.exists_factorization_finite_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean#L407).

> Noether normalization for a finite-type map of affine schemes at a chosen fibre.

```lean
theorem exists_factorization_finite_fiber {X S : Scheme.{u}} (f : X ⟶ S)
    [IsAffine X] [IsAffine S] [LocallyOfFiniteType f] [QuasiCompact f]
    (s : S) (d : ℕ) (hd : topologicalKrullDim (f.fiber s) = d) :
    ∃ π : X ⟶ 𝔸(ULift (Fin d); S),
      (π ≫ 𝔸(ULift (Fin d); S) ↘ S = f) ∧
      ∃ πs : f.fiber s ⟶ (𝔸(ULift (Fin d); S) ↘ S).fiber s,
        (πs ≫ (𝔸(ULift (Fin d); S) ↘ S).fiberι s = f.fiberι s ≫ π) ∧
        (πs ≫ (𝔸(ULift (Fin d); S) ↘ S).fiberToSpecResidueField s =
          f.fiberToSpecResidueField s) ∧
        IsFinite πs
```

## Tag 0CBJ, a lemma

[Tag 0CBJ](https://stacks.math.columbia.edu/tag/0CBJ) in the Stacks Project.

**`AlgebraicGeometry.exists_isImmersion_specMap_derivativePair_of_unramifiedAt`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/LocalStructure.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/LocalStructure.lean#L346). The attribute's comment: “unramified case; the étale case is `AlgebraicGeometry.exists_isOpenImmersion_specMap_derivativePair_of_etaleAt`”.

> **Stacks Project, Tag 0CBJ, unramified case.** A morphism of schemes unramified at `x`
> factors, on an affine open neighbourhood of `x` lying over a prescribed affine open `V` of the
> target, as an immersion into the spectrum of the derivative-localized monic hypersurface
> `Γ(S, V)[t]_{g'}/(g)`, followed by the canonical map to the affine line over `V`.

```lean
public lemma exists_isImmersion_specMap_derivativePair_of_unramifiedAt
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) (V : S.Opens)
    (hV : IsAffineOpen V) (hxV : f x ∈ V) (hf : UnramifiedAt f x) :
    ∃ (U : X.Opens) (_ : IsAffineOpen U) (_ : x ∈ U)
      (hUV : U ≤ f ⁻¹ᵁ V) (P : StandardEtalePair Γ(S, V)),
      P.g = P.f.derivative ∧
        ∃ (j : U.toScheme ⟶ Spec (CommRingCat.of P.Ring)),
          IsImmersion j ∧
            j ≫ Spec.map (CommRingCat.ofHom (aeval P.X).toRingHom) ≫
                Spec.map (CommRingCat.ofHom (Polynomial.C : Γ(S, V) →+* Γ(S, V)[X])) =
              f.resLE V U hUV ≫ hV.isoSpec.hom
```

**`AlgebraicGeometry.exists_isOpenImmersion_specMap_derivativePair_of_etaleAt`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/LocalStructure.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/LocalStructure.lean#L383). The attribute's comment: “étale case; the unramified case”.

> **Stacks Project, Tag 0CBJ, étale case.** At a point where the morphism is étale, the
> immersion of `AlgebraicGeometry.exists_isImmersion_specMap_derivativePair_of_unramifiedAt` may
> be chosen to be an open immersion.

```lean
public lemma exists_isOpenImmersion_specMap_derivativePair_of_etaleAt
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) (V : S.Opens)
    (hV : IsAffineOpen V) (hxV : f x ∈ V) (hf : EtaleAt f x) :
    ∃ (U : X.Opens) (_ : IsAffineOpen U) (_ : x ∈ U)
      (hUV : U ≤ f ⁻¹ᵁ V) (P : StandardEtalePair Γ(S, V)),
      P.g = P.f.derivative ∧
        ∃ (j : U.toScheme ⟶ Spec (CommRingCat.of P.Ring)),
          IsOpenImmersion j ∧
            j ≫ Spec.map (CommRingCat.ofHom (aeval P.X).toRingHom) ≫
                Spec.map (CommRingCat.ofHom (Polynomial.C : Γ(S, V) →+* Γ(S, V)[X])) =
              f.resLE V U hUV ≫ hV.isoSpec.hom
```

## Tag 0CBK, a lemma

[Tag 0CBK](https://stacks.math.columbia.edu/tag/0CBK) in the Stacks Project.

**`AlgebraicGeometry.finiteDimensional_relativeCotangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean, line 762](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean#L762). The attribute's comment: “finiteness of r”.

> **Stacks Project, Tag 0CBK, finiteness of `r`.** For a morphism locally of finite type the
> residue-field fibre at `x` of the stalk of the sheaf of relative differentials is a
> finite-dimensional `κ(x)`-vector space, so the integer `r` of the tag is defined.

```lean
theorem finiteDimensional_relativeCotangentSpace {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (x : X) :
    FiniteDimensional (X.residueField x) (relativeCotangentSpace f x)
```

**`AlgebraicGeometry.finrank_relativeCotangentSpace_eq_fiberRelativeCotangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean, line 774](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean#L774). The attribute's comment: “first equality”.

> **Stacks Project, Tag 0CBK, first equality defining `r`.** The residue-field fibre of the
> stalk of `Ω_{X/S}` at `x` and the corresponding fibre computed on the scheme-theoretic fibre
> through `x` have the same dimension over `κ(x)`:
> `dim_{κ(x)} Ω_{X/S,x} ⊗ κ(x) = dim_{κ(x)} Ω_{X_s/s,x} ⊗ κ(x)`.

```lean
theorem finrank_relativeCotangentSpace_eq_fiberRelativeCotangentSpace
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) :
    Module.finrank (X.residueField x) (relativeCotangentSpace f x) =
      Module.finrank (X.residueField x) (fiberRelativeCotangentSpace f x)
```

**`AlgebraicGeometry.finrank_relativeCotangentSpace_eq_finrank_dottedTangentArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean, line 786](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean#L786). The attribute's comment: “second equality”.

> **Stacks Project, Tag 0CBK, second equality defining `r`.** The residue-field fibre of the
> stalk of `Ω_{X/S}` at `x` and the relative tangent space at `x` have the same dimension over
> `κ(x)`: `dim_{κ(x)} Ω_{X/S,x} ⊗ κ(x) = dim_{κ(x)} T_{X/S,x}`. The tangent space is the
> `𝒪_{X,x}`-linear dual of the stalk, which is the `κ(x)`-linear dual of the fibre.

```lean
theorem finrank_relativeCotangentSpace_eq_finrank_dottedTangentArrow
    {X S : Scheme.{u}} (f : X ⟶ S) (x : X) :
    Module.finrank (X.residueField x) (relativeCotangentSpace f x) =
      Module.finrank (X.residueField x) (DottedTangentArrow f x)
```

**`AlgebraicGeometry.exists_factorization_unramifiedAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean, line 986](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean#L986).

> **Stacks Project, Tag 0CBK.** Let `f : X ⟶ S` be a finite type morphism of affine schemes
> and let `x` be a point of `X`. If `r` is the dimension over `κ(x)` of the residue-field fibre at
> `x` of the stalk of the sheaf of relative differentials, then `f` factors as `X ⟶ 𝐀^r_S ⟶ S`
> with the first morphism unramified at `x`.
>
> The coordinates of the factorization are `r` global sections of `X` whose differentials span
> that fibre.

```lean
theorem exists_factorization_unramifiedAt {X S : Scheme.{u}} (f : X ⟶ S)
    [IsAffine X] [IsAffine S] [LocallyOfFiniteType f] [QuasiCompact f]
    (x : X) (r : ℕ)
    (hr : Module.finrank (X.residueField x) (relativeCotangentSpace f x) = r) :
    ∃ π : X ⟶ 𝔸(ULift.{u} (Fin r); S),
      (π ≫ 𝔸(ULift.{u} (Fin r); S) ↘ S = f) ∧ UnramifiedAt π x
```

## Tag 0CBL, a lemma

[Tag 0CBL](https://stacks.math.columbia.edu/tag/0CBL) in the Stacks Project.

**`AlgebraicGeometry.exists_affineOpen_immersion_into_affineSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean, line 1463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean#L1463). The attribute's comment: “clause (1): the immersion into affine (r+1)-space”.

> **Stacks Project, Tag 0CBL, first clause.** Let `f : X ⟶ S` be locally of finite type, let
> `x` be a point of `X` and let `V` be an affine open neighbourhood of its image. If `r` is the
> dimension over `κ(x)` of the residue-field fibre at `x` of the stalk of the sheaf of relative
> differentials, then `f` restricted to some affine open `U ∋ x` lying over `V` factors as an
> immersion into relative affine `(r+1)`-space over `V` followed by the projection.

```lean
theorem exists_affineOpen_immersion_into_affineSpace {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (x : X) (V : S.affineOpens) (hxV : f x ∈ V.1) (r : ℕ)
    (hr : Module.finrank (X.residueField x) (relativeCotangentSpace f x) = r) :
    ∃ (U : X.affineOpens) (_ : x ∈ U.1) (hUV : U.1 ≤ f ⁻¹ᵁ V.1)
      (j : U.1.toScheme ⟶ 𝔸(ULift.{u} (Fin (r + 1)); V.1.toScheme)),
      IsImmersion j ∧
        j ≫ 𝔸(ULift.{u} (Fin (r + 1)); V.1.toScheme) ↘ V.1.toScheme =
          f.resLE V.1 U.1 hUV
```

**`AlgebraicGeometry.exists_closedImmersion_smoothFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean, line 1481](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Variety/GeometricFieldChange/NoetherNormalization.lean#L1481). The attribute's comment: “clause (2): the closed immersion into a smooth scheme”.

> **Stacks Project, Tag 0CBL, second clause.** In the situation of
> `AlgebraicGeometry.exists_affineOpen_immersion_into_affineSpace`, the affine open `U` may instead
> be taken to be a closed subscheme of a scheme smooth of relative dimension `r` over `V`, through
> which the restriction of `f` factors.

```lean
theorem exists_closedImmersion_smoothFactorization {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFiniteType f] (x : X) (V : S.affineOpens) (hxV : f x ∈ V.1) (r : ℕ)
    (hr : Module.finrank (X.residueField x) (relativeCotangentSpace f x) = r) :
    ∃ (U : X.affineOpens) (_ : x ∈ U.1) (hUV : U.1 ≤ f ⁻¹ᵁ V.1) (D : Scheme.{u})
      (j : U.1.toScheme ⟶ D) (g : D ⟶ V.1.toScheme),
      IsClosedImmersion j ∧ SmoothOfRelativeDimension r g ∧
        j ≫ g = f.resLE V.1 U.1 hUV
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.18, Tag 0CBG](https://stacks.math.columbia.edu/tag/0CBG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

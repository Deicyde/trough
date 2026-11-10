---
declaration: section
origin: cited
lean: Stacks.Divisors.isAffineOpen_puncturedSpectrum_iff_krullDimLE_one, Stacks.Divisors.krullDimLE_one_stalk_at_genericPoint_compl_affineOpenImmersion, Stacks.Divisors.ringKrullDim_stalk_at_genericPoint_compl_affineOpenImmersion_eq_one, Stacks.PuncturedSpectrum.krullDimLE_one_stalk_at_genericPoint_compl_affineOpen, Stacks.PuncturedSpectrum.ringKrullDim_stalk_at_genericPoint_compl_affineOpen_eq_one, AlgebraicGeometry.exists_effectiveCartierDivisor_compl_affineOpen, AlgebraicGeometry.exists_effectiveCartierDivisor_compl_affineOpen_of_isSeparated, AlgebraicGeometry.exists_isAmpleFamily_of_isRegular
statement: formalized
proof: formalized
---

# 31.17 Complements of affine opens

Section 31.17 of the Stacks Project, [Tag 0BCQ](https://stacks.math.columbia.edu/tag/0BCQ). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BCR, a lemma

[Tag 0BCR](https://stacks.math.columbia.edu/tag/0BCR) in the Stacks Project.

**`Stacks.Divisors.isAffineOpen_puncturedSpectrum_iff_krullDimLE_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/PuncturedSpectrumAffineCriterion.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/PuncturedSpectrumAffineCriterion.lean#L358). References: EGA IV (21.12.9), “special case”.

> The punctured spectrum of a Noetherian local ring is affine if and only if the ring has Krull
> dimension at most one.

```lean
theorem isAffineOpen_puncturedSpectrum_iff_krullDimLE_one :
    IsAffineOpen (puncturedSpectrum A) ↔ Ring.KrullDimLE 1 A
```

## Tag 0BCU, a lemma

[Tag 0BCU](https://stacks.math.columbia.edu/tag/0BCU) in the Stacks Project.

**`Stacks.Divisors.krullDimLE_one_stalk_at_genericPoint_compl_affineOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/PuncturedSpectrumAffineCriterion.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/PuncturedSpectrumAffineCriterion.lean#L435). The attribute's comment: “dimension bound”. References: EGA IV (21.12.7), “codimension ≤ 1”; SGA 6 II (2.2.6), “dim ≤ 1 at maximal pts”; SGA 2 V (3.4).

> Let `U` be an open subscheme of a locally Noetherian scheme `X` whose inclusion is affine.  At
> the generic point `ξ` of an irreducible component of `X ∖ U` the local ring has Krull dimension at
> most one.
>
> Pulling `U` back along `Spec 𝒪_{X,ξ} → X` gives the punctured spectrum of `𝒪_{X,ξ}`, which is
> affine because the inclusion of `U` is; so Tag 0BCR applies.

```lean
theorem krullDimLE_one_stalk_at_genericPoint_compl_affineOpenImmersion
    (X : Scheme.{u}) [IsLocallyNoetherian X]
    (U : X.Opens) [IsAffineHom U.ι]
    {Z : Set ↑((U : Set X)ᶜ)} (hZ : Z ∈ irreducibleComponents ↑((U : Set X)ᶜ))
    {ξ : ↑((U : Set X)ᶜ)} (hξ : IsGenericPoint ξ Z) :
    Ring.KrullDimLE 1 (X.presheaf.stalk (ξ : X))
```

**`Stacks.Divisors.ringKrullDim_stalk_at_genericPoint_compl_affineOpenImmersion_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/PuncturedSpectrumAffineCriterion.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/PuncturedSpectrumAffineCriterion.lean#L503). The attribute's comment: “equality in the closure”. References: EGA IV (21.12.7), “codimension = 1 if dense”; SGA 6 II (2.2.6), “dim = 1 case”.

> With the hypotheses of
> `Stacks.Divisors.krullDimLE_one_stalk_at_genericPoint_compl_affineOpenImmersion`, if `U` is dense
> or `ξ` lies in the closure of `U`, then the local ring at `ξ` has dimension exactly one.
>
> Some point of `U` specializes to `ξ`, so it is a point of `Spec 𝒪_{X,ξ}` other than the closed
> point; hence the dimension is positive.

```lean
theorem ringKrullDim_stalk_at_genericPoint_compl_affineOpenImmersion_eq_one
    (X : Scheme.{u}) [IsLocallyNoetherian X]
    (U : X.Opens) [IsAffineHom U.ι]
    {Z : Set ↑((U : Set X)ᶜ)} (hZ : Z ∈ irreducibleComponents ↑((U : Set X)ᶜ))
    {ξ : ↑((U : Set X)ᶜ)} (hξ : IsGenericPoint ξ Z)
    (hξU : Dense (U : Set X) ∨ (ξ : X) ∈ closure (U : Set X)) :
    ringKrullDim (X.presheaf.stalk (ξ : X)) = 1
```

## Tag 0BCV, a lemma

[Tag 0BCV](https://stacks.math.columbia.edu/tag/0BCV) in the Stacks Project.

**`Stacks.PuncturedSpectrum.krullDimLE_one_stalk_at_genericPoint_compl_affineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PuncturedSpectrum/SeparatedComplement.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PuncturedSpectrum/SeparatedComplement.lean#L71). The attribute's comment: “dimension bound”. References: EGA IV (21.12.7), “dim ≤ 1, U affine open”; SGA 2 V (3.4); SGA 6 II (2.2.6), “X sep, U affine; dim≤1”.

> **Stacks Project, Tag 0BCV.** The local ring at the generic point of an irreducible
> component of the complement of an affine open in a separated locally Noetherian scheme has
> Krull dimension at most one.

```lean
theorem krullDimLE_one_stalk_at_genericPoint_compl_affineOpen
    (X : Scheme.{u}) [Scheme.IsSeparated X] [IsLocallyNoetherian X]
    (U : X.Opens) (hU : IsAffineOpen U)
    {Z : Set ↑((U : Set X)ᶜ)} (hZ : Z ∈ irreducibleComponents ↑((U : Set X)ᶜ))
    {ξ : ↑((U : Set X)ᶜ)} (hξ : IsGenericPoint ξ Z) :
    Ring.KrullDimLE 1 (X.presheaf.stalk (ξ : X))
```

**`Stacks.PuncturedSpectrum.ringKrullDim_stalk_at_genericPoint_compl_affineOpen_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/PuncturedSpectrum/SeparatedComplement.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/PuncturedSpectrum/SeparatedComplement.lean#L85). The attribute's comment: “equality in the closure”. References: EGA IV (21.12.7), “dim = 1, U affine open”; SGA 6 II (2.2.6), “X sep, U affine; dim=1”.

> **Stacks Project, Tag 0BCV.** Under the hypotheses of the dimension bound, the local ring
> has dimension one when the affine open is dense or the generic point is in its closure.

```lean
theorem ringKrullDim_stalk_at_genericPoint_compl_affineOpen_eq_one
    (X : Scheme.{u}) [Scheme.IsSeparated X] [IsLocallyNoetherian X]
    (U : X.Opens) (hU : IsAffineOpen U)
    {Z : Set ↑((U : Set X)ᶜ)} (hZ : Z ∈ irreducibleComponents ↑((U : Set X)ᶜ))
    {ξ : ↑((U : Set X)ᶜ)} (hξ : IsGenericPoint ξ Z)
    (hξU : Dense (U : Set X) ∨ (ξ : X) ∈ closure (U : Set X)) :
    ringKrullDim (X.presheaf.stalk (ξ : X)) = 1
```

## Tag 0BCW, a lemma

[Tag 0BCW](https://stacks.math.columbia.edu/tag/0BCW) in the Stacks Project.

**`AlgebraicGeometry.exists_effectiveCartierDivisor_compl_affineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/AffineComplement.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/AffineComplement.lean#L107). The attribute's comment: “the separated case, where the diagonal is affine”.

> **Stacks Project, Tag 0EGJ.** The complement of a dense affine open in a Noetherian
> scheme with affine diagonal is the support of an effective Cartier divisor if its local
> rings along the complement are UFDs.

```lean
theorem exists_effectiveCartierDivisor_compl_affineOpen
    (X : Scheme.{u}) [IsNoetherian X]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    (U : X.Opens) (hU : IsAffineOpen U) (hDense : Dense (U : Set X))
    (hUFD : ∀ x : X, x ∉ U → UniqueFactorizationMonoid (X.presheaf.stalk x)) :
    ∃ I : X.IdealSheafData,
      IsEffectiveCartierDivisor I ∧
        (I.support : Set X) = (U : Set X)ᶜ
```

**`AlgebraicGeometry.exists_effectiveCartierDivisor_compl_affineOpen_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/SeparatedAffineComplement.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/SeparatedAffineComplement.lean#L54).

> **Stacks Project, Tag 0BCW.** Let `X` be a Noetherian separated scheme and `U ⊆ X` a dense
> affine open whose complement meets only points with factorial local rings.  Then there is an
> effective Cartier divisor `D ⊆ X` with `U = X ∖ D`.

```lean
theorem exists_effectiveCartierDivisor_compl_affineOpen_of_isSeparated
    (X : Scheme.{u}) [IsNoetherian X] [Scheme.IsSeparated X]
    (U : X.Opens) (hU : IsAffineOpen U) (hdense : Dense (U : Set X))
    (hUFD : ∀ x : X, x ∉ U → UniqueFactorizationMonoid (X.presheaf.stalk x)) :
    ∃ I : X.IdealSheafData,
      IsEffectiveCartierDivisor I ∧ (U : Set X) = (I.support : Set X)ᶜ
```

## Tag 0EGJ, a lemma

[Tag 0EGJ](https://stacks.math.columbia.edu/tag/0EGJ) in the Stacks Project.

**`AlgebraicGeometry.exists_effectiveCartierDivisor_compl_affineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/AffineComplement.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/AffineComplement.lean#L107).

> **Stacks Project, Tag 0EGJ.** The complement of a dense affine open in a Noetherian
> scheme with affine diagonal is the support of an effective Cartier divisor if its local
> rings along the complement are UFDs.

```lean
theorem exists_effectiveCartierDivisor_compl_affineOpen
    (X : Scheme.{u}) [IsNoetherian X]
    [IsAffineHom (pullback.diagonal (terminal.from X))]
    (U : X.Opens) (hU : IsAffineOpen U) (hDense : Dense (U : Set X))
    (hUFD : ∀ x : X, x ∉ U → UniqueFactorizationMonoid (X.presheaf.stalk x)) :
    ∃ I : X.IdealSheafData,
      IsEffectiveCartierDivisor I ∧
        (I.support : Set X) = (U : Set X)ᶜ
```

## Tag 0GML, a lemma

[Tag 0GML](https://stacks.math.columbia.edu/tag/0GML) in the Stacks Project.

**`AlgebraicGeometry.exists_isAmpleFamily_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/AmpleFamilyRegular.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/AmpleFamilyRegular.lean#L187). References: SGA 6 II (2.2.7.1), “more general”.

> **Stacks Project, Tag 0GML.** A quasi-compact regular scheme whose diagonal is affine has an
> ample family of invertible modules.
>
> The family is `{𝒪_X(D x)}` indexed by the points of `X`, where `D x` is the effective Cartier
> divisor whose support is the complement of a dense affine open around `x`, supplied by Tag 0EGJ;
> the required section of `𝒪_X(D x)` is the canonical section `1_{D x}`, whose nonvanishing locus
> is exactly that affine open.

```lean
theorem exists_isAmpleFamily_of_isRegular (X : Scheme.{u}) [CompactSpace X]
    [IsAffineHom (pullback.diagonal (terminal.from X))] (hX : IsRegular X) :
    ∃ (I : Type u) (L : I → X.Modules), X.IsAmpleFamily L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.17, Tag 0BCQ](https://stacks.math.columbia.edu/tag/0BCQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

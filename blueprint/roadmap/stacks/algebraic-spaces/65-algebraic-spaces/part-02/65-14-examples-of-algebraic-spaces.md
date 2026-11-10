---
declaration: section
origin: cited
lean: AlgebraicGeometry.AffineLineInvolution.affineLine, AlgebraicGeometry.AffineLineInvolution.puncturedAffineLineOpen, AlgebraicGeometry.AffineLineInvolution.puncturedAffineLine, AlgebraicGeometry.AffineLineInvolution.relationScheme, AlgebraicGeometry.AffineLineInvolution.involutionRelation, AlgebraicGeometry.AffineLineInvolution.involutionQuotient, AlgebraicGeometry.AffineLineInvolution.isAbsolutelyQuasiSeparated_involutionQuotient, AlgebraicGeometry.AffineLineInvolution.isEtaleEquivalenceRelation
statement: formalized
proof: formalized
---

# 65.14 Examples of algebraic spaces

Section 65.14 of the Stacks Project, [Tag 02Z0](https://stacks.math.columbia.edu/tag/02Z0). 9 tags here are carried by 75 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02Z1, an example

[Tag 02Z1](https://stacks.math.columbia.edu/tag/02Z1) in the Stacks Project.

**`AlgebraicGeometry.AffineLineInvolution.affineLine`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean#L135). The attribute's comment: “the chart 𝔸¹”.

> The affine line over `Spec k`, the chart of the example.

```lean
noncomputable abbrev affineLine : Over (Spec (.of k))
```

**`AlgebraicGeometry.AffineLineInvolution.puncturedAffineLineOpen`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean#L140). The attribute's comment: “the punctured line, as an open”.

> The basic open of the standard coordinate, the punctured affine line.

```lean
noncomputable abbrev puncturedAffineLineOpen : (affineLine k).left.Opens
```

**`AlgebraicGeometry.AffineLineInvolution.puncturedAffineLine`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean#L145). The attribute's comment: “the punctured line”.

> The punctured affine line as a scheme over `Spec k`.

```lean
noncomputable abbrev puncturedAffineLine : Over (Spec (.of k))
```

**`AlgebraicGeometry.AffineLineInvolution.relationScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean#L192). The attribute's comment: “the relation scheme Δ ⨿ Γ”.

> The relation scheme, the disjoint union of the affine line (carrying the diagonal) and of its
> puncture (carrying the graph of negation).

```lean
noncomputable abbrev relationScheme : Over (Spec (.of k))
```

**`AlgebraicGeometry.AffineLineInvolution.involutionRelation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean#L198). The attribute's comment: “the relation j”.

> The pre-relation `j : R ⟶ U ×_k U` which is the diagonal on the first summand and the graph of
> negation on the second.

```lean
noncomputable def involutionRelation :
    Stacks.Groupoids.PreRelation (relationScheme k) (affineLine k)
```

**`AlgebraicGeometry.AffineLineInvolution.involutionQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolution.lean#L224). The attribute's comment: “the quotient X = U/R”.

> The quotient sheaf of the involution relation on a big fppf site containing `Spec k`.

```lean
noncomputable abbrev involutionQuotient (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    Sheaf (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)
```

**`AlgebraicGeometry.AffineLineInvolution.isAbsolutelyQuasiSeparated_involutionQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionQuasiSeparated.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionQuasiSeparated.lean#L128). The attribute's comment: “quasi\_separated”.

> **Stacks 02Z1, quasi-separatedness.** Away from characteristic two, the quotient of the
> affine line by the punctured graph of negation is a quasi-separated algebraic space.
>
> The chart `𝔸¹_k ⟶ X` is surjective and étale by Stacks 0265, its source is affine and hence
> quasi-separated, and the second projection of its kernel pair is a base change of the target
> map of the relation, which is affine; Stacks 07S4 concludes.
>
> Representability of the diagonal of `X`, from which surjectivity and étaleness of the chart
> both follow, is supplied unconditionally by
> `AlgebraicGeometry.Space.relativelyRepresentable_diag_quotientSheaf` together with
> `AlgebraicGeometry.Space.isEffectiveDescentAlongCoveringSieve_monomorphisms_inf_lft`.

```lean
theorem isAbsolutelyQuasiSeparated_involutionQuotient (hchar : (2 : k) ≠ 0)
    (hZ : B.Contains (⊤_ Scheme.{u})) :
    Space.IsAbsolutelyQuasiSeparated B (Spec (.of k)) hS hZ
      (involutionQuotient k B hS).obj
```

**`AlgebraicGeometry.AffineLineInvolution.isEtaleEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionQuotient.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionQuotient.lean#L472). The attribute's comment: “etale\_relation”.

> **Stacks 02Z1.** Away from characteristic two, the involution relation on the affine
> line is an étale equivalence relation.

```lean
theorem isEtaleEquivalenceRelation [NeZero (2 : k)] :
    Stacks.Groupoids.IsEtaleEquivalenceRelation (involutionRelation k)
```

**`AlgebraicGeometry.AffineLineInvolution.isAlgebraicSpace_involutionQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionQuotient.lean, line 565](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineInvolutionQuotient.lean#L565). The attribute's comment: “algebraic\_space”.

> **Stacks 02Z1.** Away from characteristic two, the quotient of the affine line by the
> punctured graph of negation is an algebraic space over the ground field.
>
> The chart `affineLineChart` is affine, so the two descent hypotheses of Stacks 0265 are
> discharged unconditionally by
> `AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_of_affineBase_unconditional`.

```lean
theorem isAlgebraicSpace_involutionQuotient (hchar : (2 : k) ≠ 0) (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    IsAlgebraicSpace B (Spec (.of k)) hS (involutionQuotient k B hS).obj
```

**`AlgebraicGeometry.AffineLineInvolution.not_isImmersion_involutionRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/AffineLineInvolutionNotLocallySeparated.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/AffineLineInvolutionNotLocallySeparated.lean#L92). The attribute's comment: “the relation j is not an immersion”.

> **Stacks 02Z1.** The pre-relation `j : R ⟶ U ×_k U` of the involution quotient is not an
> immersion.
>
> On the graph summand `j` restricts to the inclusion of the puncture followed by the graph of
> negation; on the diagonal summand it restricts to the diagonal. The generic point of the
> punctured line specializes to the zero section, which negation fixes, so an immersion would
> force a specialization between the images of the two summands that
> `not_specializes_relationScheme` rules out upstairs.

```lean
theorem not_isImmersion_involutionRelation :
    ¬ AlgebraicGeometry.IsImmersion ((involutionRelation k).left)
```

**`AlgebraicGeometry.AffineLineInvolution.not_isAbsolutelyLocallySeparated_involutionQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/AffineLineInvolutionNotLocallySeparated.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/AffineLineInvolutionNotLocallySeparated.lean#L163). The attribute's comment: “not\_locally\_separated”.

> **Stacks 02Z1, not locally separated.** Away from characteristic two, the quotient of the
> affine line by the punctured graph of negation is not a locally separated algebraic space.
>
> The contrapositive of
> `AlgebraicGeometry.Space.isLocallySeparatedOver_of_isAbsolutelyLocallySeparated` (Stacks 04ZI,
> part 2) reduces this to the relative statement `not_isLocallySeparatedOver_quotientSpace`, using
> the algebraicity of the quotient supplied by
> `AlgebraicGeometry.AffineLineInvolution.isAlgebraicSpace_involutionQuotient`.

```lean
theorem not_isAbsolutelyLocallySeparated_involutionQuotient (hchar : (2 : k) ≠ 0)
    (hZ : B.Contains (⊤_ Scheme.{u})) :
    ¬ Space.IsAbsolutelyLocallySeparated B (Spec (.of k)) hS hZ
      (involutionQuotient k B hS).obj
```

## Tag 03FN, an example

[Tag 03FN](https://stacks.math.columbia.edu/tag/03FN) in the Stacks Project.

**`AlgebraicGeometry.TwistedDoubledOrigin.quadraticGaloisTwistedDoubledOrigin`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOrigin.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOrigin.lean#L273). The attribute's comment: “quadratic\_galois\_twisted\_doubled\_origin”.

> The quotient `X = U/R` of the affine line over a quadratic Galois extension by the diagonal
> together with the twisted diagonal away from zero.

```lean
abbrev quadraticGaloisTwistedDoubledOrigin
    [FiniteDimensional k K] [IsGalois k K] (_hdegree : Module.finrank k K = 2)
    (σ : K ≃ₐ[k] K) (_hσ : σ ≠ 1)
    (B : BigFppfSite.{u}) (hS : B.Contains (base k))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    Sheaf (BigFppfOver.topology B (base k) hS) (Type u)
```

**`AlgebraicGeometry.TwistedDoubledOrigin.isAlgebraicSpace_quadraticGaloisTwistedDoubledOrigin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginAlgebraicSpace.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginAlgebraicSpace.lean#L100). The attribute's comment: “X = U/R is an algebraic space”.

> **Stacks 03FN.** The Galois twist of the affine line with zero doubled **is an algebraic
> space**: `R` is an étale equivalence relation on `U` over `S`, and so the quotient `X = U/R` is
> an algebraic space. No descent hypothesis is needed.
>
> The relation is an affine morphism into the self-product of the chart, so
> `AlgebraicGeometry.Space.isAlgebraicSpace_quotientSheaf_of_isAffineHom` applies: Stacks 0265 is
> unconditional for an affine étale equivalence relation.

```lean
theorem isAlgebraicSpace_quadraticGaloisTwistedDoubledOrigin
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1)
    (B : BigFppfSite.{u}) (hS : B.Contains (base k))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    IsAlgebraicSpace B (base k) hS
      (quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj
```

**`AlgebraicGeometry.TwistedDoubledOrigin.isIso_quadraticGaloisTwistedDoubledOrigin_over_puncturedBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginAwayFromZero.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginAwayFromZero.lean#L497). The attribute's comment: “away\_from\_zero”.

> **Stacks 03FN.** The quotient `X = U/R` agrees with the base away from the origin: the
> base change of its structure morphism to the punctured base is an isomorphism.

```lean
theorem isIso_quadraticGaloisTwistedDoubledOrigin_over_puncturedBase
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1) (B : BigFppfSite.{u})
    (hS : B.Contains (base k))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    IsIso (pullback.snd (quotientBaseMap k K hdegree σ hσ B hS)
      ((Over.post (X := B.obj hS) B.inclusion).op.whiskerLeft
        (yoneda.map (puncturedBaseInclusion k))))
```

**`AlgebraicGeometry.TwistedDoubledOrigin.surjective_isFinite_etale_and_baseChange_isScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginBaseChange/Representability.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginBaseChange/Representability.lean#L446). The attribute's comment: “part (6): finite etale cover trivialising X”.

> **Stacks 03FN, part (6).** There is a surjective, finite, étale morphism `S' ⟶ S` such
> that the base change `X' = S' ×_S X` is a scheme: take `S' = U = Spec K[x]`, the chart itself,
> and then `X'` is two copies of `U` glued along the puncture.
>
> The chart is surjective, finite and étale over the base because `K[x]` is the base change of the
> finite separable extension `K/k` along `k → k[x]`. For the base change: pulling the quotient
> `X = U/R` back along `U ⟶ S` presents `X'` as the quotient of the self-product `U ×_S U` by the
> base change of `R`; the self-product is two copies of `U` (`coverFiberProductSplitIso`), and the
> induced relation is exactly the gluing relation of two copies of `U` along the puncture, which is
> `isPullback_doubledRelation` — the base-changed relation is the kernel pair of the map to the
> glued scheme. The representability criterion of Stacks 03C5 then identifies the quotient of the
> base-changed relation with the functor of points of the glued scheme, and `X'` is that same
> quotient.

```lean
theorem surjective_isFinite_etale_and_baseChange_isScheme
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1) :
    (Surjective (coverMap k K) ∧ IsFinite (coverMap k K) ∧ Etale (coverMap k K)) ∧
      ∃ χ : baseChangePresheaf k K B hS hdegree σ hσ ⟶
          (pointsFunctor k B hS).obj (doubledOverBase k K),
        IsIso χ
```

**`AlgebraicGeometry.TwistedDoubledOrigin.isEtale_quotientBaseMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginEtaleOverBase.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginEtaleOverBase.lean#L156). The attribute's comment: “part (2): the morphism X -> S is etale”.

> **Stacks 03FN, part (2).** The structure morphism of the Galois twist of the affine line
> with zero doubled is an étale morphism of algebraic spaces over the base, in the sense of
> Stacks 03FR: every étale morphism from a scheme into the quotient is étale over the base.
>
> The chart `U ⟶ X` is surjective and étale, and `U ⟶ S` is étale; so for an étale morphism
> `T ⟶ X` the fibre product `W = T ×_X U` is étale over `S` and surjective étale over `T`, and
> the étale case of Stacks 02KM makes `T ⟶ S` étale.

```lean
theorem isEtale_quotientBaseMap [FiniteDimensional k K] [IsGalois k K]
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1)
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    Space.IsEtale B (base k) hS (quotientBaseMap k K hdegree σ hσ B hS)
```

**`AlgebraicGeometry.TwistedDoubledOrigin.twistedRelation_isEtaleEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginEtaleRelation.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginEtaleRelation.lean#L243). The attribute's comment: “etale\_relation”.

> **Stacks 03FN.** The diagonal of the chart together with the twisted diagonal away from
> the origin is an étale equivalence relation on the chart over the base.

```lean
theorem twistedRelation_isEtaleEquivalenceRelation [FiniteDimensional k K] [IsGalois k K]
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1) :
    Stacks.Groupoids.IsEtaleEquivalenceRelation (twistedRelation k K σ)
```

**`AlgebraicGeometry.TwistedDoubledOrigin.quadraticGaloisTwistedDoubledOrigin_not_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginNotScheme.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginNotScheme.lean#L127). The attribute's comment: “not\_scheme”.

> **Stacks 03FN.** The quotient `X = U/R` is not represented by a scheme over the base.

```lean
theorem quadraticGaloisTwistedDoubledOrigin_not_representable (k K : Type u) [Field k]
    [Field K] [Algebra k K] [FiniteDimensional k K] [IsGalois k K]
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1) (B : BigFppfSite.{u})
    (hS : B.Contains (base k))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    ¬ ∃ Y : Over (base k),
      Nonempty ((quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj ≅
        Stacks.Groupoids.points (Over.post B.inclusion) Y)
```

**`AlgebraicGeometry.TwistedDoubledOrigin.isLocallySeparatedOver_quadraticGaloisTwistedDoubledOrigin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSeparation.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSeparation.lean#L278). The attribute's comment: “part (5): X is locally separated over S”.

> **Stacks 03FN, part (5).** The Galois twist of the affine line with zero doubled is
> locally separated over the base: its diagonal is an immersion.
>
> The relation `j : R ⟶ U ×_S U` is an open immersion, hence an immersion, and the diagonal of
> the quotient is covered by it.

```lean
theorem isLocallySeparatedOver_quadraticGaloisTwistedDoubledOrigin
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1)
    (B : BigFppfSite.{u}) (hS : B.Contains (base k))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    Space.IsLocallySeparatedOver B (base k) hS
      (quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj
```

**`AlgebraicGeometry.TwistedDoubledOrigin.isQuasiSeparatedOver_quadraticGaloisTwistedDoubledOrigin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSeparation.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSeparation.lean#L305). The attribute's comment: “part (5): X is quasi-separated over S”.

> **Stacks 03FN, part (5).** The Galois twist of the affine line with zero doubled is
> quasi-separated over the base: its diagonal is quasi-compact.
>
> The relation `j : R ⟶ U ×_S U` is an affine morphism, hence quasi-compact, and the diagonal of
> the quotient is covered by it.

```lean
theorem isQuasiSeparatedOver_quadraticGaloisTwistedDoubledOrigin
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1)
    (B : BigFppfSite.{u}) (hS : B.Contains (base k))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    Space.IsQuasiSeparatedOver B (base k) hS
      (quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj
```

**`AlgebraicGeometry.TwistedDoubledOrigin.not_isSeparatedOver_quadraticGaloisTwistedDoubledOrigin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSeparation.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSeparation.lean#L352). The attribute's comment: “part (5): X is not separated over S”.

> **Stacks 03FN, part (5).** The Galois twist of the affine line with zero doubled is *not*
> separated over the base: its diagonal is not a closed immersion.
>
> The relation is a represented base change of the diagonal, so a closed-immersion diagonal
> would make the relation a closed immersion of schemes, which
> `AlgebraicGeometry.TwistedDoubledOrigin.not_isClosedImmersion_twistedRelation_left`
> excludes.

```lean
theorem not_isSeparatedOver_quadraticGaloisTwistedDoubledOrigin
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1)
    (B : BigFppfSite.{u}) (hS : B.Contains (base k))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    ¬ Space.IsSeparatedOver B (base k) hS
      (quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj
```

**`AlgebraicGeometry.TwistedDoubledOrigin.baseChange_specExtension_isScheme_and_not_isScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSpecBase.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSpecBase.lean#L107). The attribute's comment: “part (7): X over Spec k, with X\_\{k'} a scheme but X not a scheme”.

> **Stacks 03FN, part (7).** Read over `Spec k` rather than over `S`, the base change
> `X_{k'} = X ×_{Spec k} Spec k'` of the twisted doubled origin is a scheme — the affine line
> over `k'` with zero doubled — while `X` itself is not a scheme.
>
> The three conjuncts are: the chart `U` is the base change `S ×_{Spec k} Spec k'` of the base,
> so that `X ×_{Spec k} Spec k'` is the presheaf `X ×_S U` of part (6); that presheaf is the
> functor of points of the affine line over `k'` with zero doubled, which is part (6); and `X`
> is not the functor of points of any scheme over the base, which is the `not_scheme` clause.
> Together they say that `X_{k'}` is a scheme and `X` is not.

```lean
theorem baseChange_specExtension_isScheme_and_not_isScheme
    (hdegree : Module.finrank k K = 2) (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1) (B : BigFppfSite.{u})
    (hS : B.Contains (base k))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    IsPullback (coverMap k K) (coverToSpecExtension K) (specBase k) (specExtension k K) ∧
      (∃ χ : baseChangePresheaf k K B hS hdegree σ hσ ⟶
          (pointsFunctor k B hS).obj (doubledOverBase k K), IsIso χ) ∧
      ¬ ∃ Y : Over (base k),
        Nonempty ((quadraticGaloisTwistedDoubledOrigin k K hdegree σ hσ B hS).obj ≅
          Stacks.Groupoids.points (Over.post B.inclusion) Y)
```

**`AlgebraicGeometry.TwistedDoubledOrigin.exists_descentDatum_specExtension_not_isEffective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSpecNotEffective.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginSpecNotEffective.lean#L276). The attribute's comment: “the descent datum relative to \{Spec k' -> Spec k} which is not effective”.

> **Stacks 03FN, the closing claim.** For a degree two Galois extension `k'/k` with nonidentity
> automorphism `σ` there is a descent datum for schemes relative to the one-member covering
> `{Spec k' ⟶ Spec k}` which is not effective.
>
> The datum is the Galois twist of the affine line over `k'` with the origin doubled; were it
> effective, the two origins of that line would have the same image in the descended scheme, which
> `AlgebraicGeometry.TwistedDoubledOrigin.specOrigin_chart_ne` forbids.

```lean
theorem exists_descentDatum_specExtension_not_isEffective (hdegree : Module.finrank k K = 2)
    (σ : K ≃ₐ[k] K) (hσ : σ ≠ 1) :
    ∃ D : DescentDatum (specExtension k K), ¬ DescentData.IsEffective D
```

**`AlgebraicGeometry.TwistedDoubledOrigin.twistedRelationQuotient_zeroFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginZeroFibre.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TwistedDoubledOriginZeroFibre.lean#L386). The attribute's comment: “zero\_fibre”.

> **Stacks 03FN.** Over the origin the punctured twisted diagonal disappears, so the fibre
> of the quotient over the origin of the base is the origin of the chart, `Spec K`.

```lean
theorem twistedRelationQuotient_zeroFibre (σ : K ≃ₐ[k] K) (B : BigFppfSite.{u})
    (hS : B.Contains (base k))
    [HasSheafify (BigFppfOver.topology B (base k) hS) (Type u)] :
    let C := BigFppfOver B (base k) hS
    let F : C ⥤ Over (base k) := Over.post B.inclusion
    let Q : Cᵒᵖ ⥤ Type u :=
      (quotientSheaf (BigFppfOver.topology B (base k) hS) F (twistedRelation k K σ)).obj
    Nonempty ((Q ⨯ points F (zeroBaseOverBase k)) ≅ points F (zeroCoverOverBase k K))
```

## Tag 02Z2, a lemma

[Tag 02Z2](https://stacks.math.columbia.edu/tag/02Z2) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_actionQuotient_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionQuotientAlgebraic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionQuotientAlgebraic.lean#L67). The attribute's comment: “the quotient is an algebraic space”.

> **Stacks 02Z2.** Let a group `G` act on an object `V` of the big fppf site of `S` so that
> no nonidentity element fixes a point of `V` and acts trivially on its residue field. Then the
> quotient `V/R` of `V` by the graph relation `R = ∐_{g ∈ G} V` of the action is an algebraic
> space over `S`.
>
> This is `AlgebraicGeometry.Space.isAlgebraicSpace_actionQuotient` with its descent hypothesis
> discharged by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongCoveringSieve_monomorphisms_inf_lft`.

```lean
theorem isAlgebraicSpace_actionQuotient_unconditional {S : Scheme.{u}} (G : Type v) [Group G]
    [Small.{u} G] (B : BigFppfSite.{u}) (hS : B.Contains S) (V : BigFppfOver B S hS)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    (a : G →* Aut (underlyingOver B hS V))
    (ha : ActsNontriviallyOnFixedResidueFields (underlyingOver B hS V) G a) :
    IsAlgebraicSpace B S hS (actionQuotient G B hS V a)
```

**`AlgebraicGeometry.Space.actionRelationScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean#L86). The attribute's comment: “relation object”.

> The scheme of arrows of the graph relation of a group action: the disjoint union of one
> copy of `U` for each group element.

```lean
abbrev actionRelationScheme : Over S
```

**`AlgebraicGeometry.Space.actionRelation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean#L100). The attribute's comment: “relation”.

> The graph relation of a group action, as a pre-relation on `U`.

```lean
def actionRelation (a : G →* Aut U) :
    PreRelation (actionRelationScheme U G) U
```

**`AlgebraicGeometry.Space.actionRelation_isEtaleEquivalenceRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean#L483). The attribute's comment: “étale equivalence relation”.

> The graph relation of an action whose stabilizers act faithfully on residue fields is an
> étale equivalence relation.

```lean
theorem actionRelation_isEtaleEquivalenceRelation (a : G →* Aut U)
    (ha : ActsNontriviallyOnFixedResidueFields U G a) :
    IsEtaleEquivalenceRelation (actionRelation U G a)
```

**`AlgebraicGeometry.Space.actionQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean#L525). The attribute's comment: “quotient”.

> The quotient of a scheme in a big fppf site by a group action: the quotient sheaf of the
> graph relation of the action.

```lean
abbrev actionQuotient (a : G →* Aut (underlyingOver B hS V))
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)] :
    (BigFppfOver B S hS)ᵒᵖ ⥤ Type u
```

## Tag 02Z3, a definition

[Tag 02Z3](https://stacks.math.columbia.edu/tag/02Z3) in the Stacks Project.

**`AlgebraicGeometry.Space.ActsNontriviallyOnFixedResidueFields`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean#L78). The attribute's comment: “acts freely: the condition (*) of 02Z2 on the action”.

> The action of a group on a scheme over `S` *acts nontrivially on fixed residue fields*
> when every nonidentity element fixing a point acts nontrivially on the residue field at that
> point.

```lean
def ActsNontriviallyOnFixedResidueFields (a : G →* Aut U) : Prop
```

**`AlgebraicGeometry.Space.actionQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/GroupActionRelation.lean#L525). The attribute's comment: “the quotient U/G of a scheme by a group action satisfying (*)”.

> The quotient of a scheme in a big fppf site by a group action: the quotient sheaf of the
> graph relation of the action.

```lean
abbrev actionQuotient (a : G →* Aut (underlyingOver B hS V))
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)] :
    (BigFppfOver B S hS)ᵒᵖ ⥤ Type u
```

## Tag 02Z4, a lemma

[Tag 02Z4](https://stacks.math.columbia.edu/tag/02Z4) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparatedOver_actionQuotient_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientSeparated.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientSeparated.lean#L371). The attribute's comment: “separated”.

> **Stacks 02Z4, part (2).** Let a finite group `G` act on an object `V` of the big fppf site
> over `S` so that no nonidentity element fixes a point of `V` together with its residue field. If
> `V` is separated over `S`, then the quotient `V/G` is separated over `S`.

```lean
theorem isSeparatedOver_actionQuotient_unconditional (G : Type v) [Group G] [Finite G]
    (a : G →* Aut (underlyingOver B hS V))
    (ha : ActsNontriviallyOnFixedResidueFields (underlyingOver B hS V) G a)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    [_root_.AlgebraicGeometry.IsSeparated (underlyingOver B hS V).hom] :
    IsSeparatedOver B S hS (actionQuotient G B hS V a)
```

**`AlgebraicGeometry.Space.isQuasiSeparatedOver_actionQuotient_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientSeparated.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientSeparated.lean#L384). The attribute's comment: “quasi-separated”.

> **Stacks 02Z4, part (1).** Let a finite group `G` act on an object `V` of the big fppf site
> over `S` so that no nonidentity element fixes a point of `V` together with its residue field. If
> `V` is quasi-separated over `S`, then the quotient `V/G` is quasi-separated over `S`.

```lean
theorem isQuasiSeparatedOver_actionQuotient_unconditional (G : Type v) [Group G] [Finite G]
    (a : G →* Aut (underlyingOver B hS V))
    (ha : ActsNontriviallyOnFixedResidueFields (underlyingOver B hS V) G a)
    [HasSheafify (BigFppfOver.topology B S hS) (Type u)]
    [QuasiSeparated (underlyingOver B hS V).hom] :
    IsQuasiSeparatedOver B S hS (actionQuotient G B hS V a)
```

## Tag 02Z5, a lemma

[Tag 02Z5](https://stacks.math.columbia.edu/tag/02Z5) in the Stacks Project.

**`AlgebraicGeometry.Space.quotientPoint_of_galois_equivariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientFieldPoints.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientFieldPoints.lean#L600). The attribute's comment: “converse descent”.

> **Stacks 02Z5, the converse descent.** Galois-equivariant field-valued data descend to a
> point of the action quotient whose pullback is the image of the supplied point upstairs.
>
> Let `L/K` be finite Galois with Galois group identified with a finite subgroup `H` of `G`,
> and let `f : Spec L ⟶ V` be a point over the given point of the base which is equivariant for
> that identification. Then the image of `f` in the quotient is invariant under the Galois
> group, so it descends through the sheaf condition on the étale covering `Spec L ⟶ Spec K` to a
> `K`-valued point of the quotient.

```lean
theorem quotientPoint_of_galois_equivariant (L : Type u) [Field L] [Algebra K L]
    [FiniteDimensional K L] [IsGalois K L] (H : Subgroup G) [Finite H]
    (e : H ≃* (L ≃ₐ[K] L))
    (f : Spec (.of L) ⟶ (underlyingOver B hS V).left)
    (hf : f ≫ (underlyingOver B hS V).hom =
      Spec.map (CommRingCat.ofHom (algebraMap K L)) ≫ b)
    (he : ∀ h : H,
      Spec.map (CommRingCat.ofHom (e h⁻¹).toRingHom) ≫ f = f ≫ (a h.1).asIso.hom.left) :
    ∃ ξ : (actionQuotient G B hS V a).obj (op (fieldObject (hS := hS) K hK b)),
      IsQuotientLift B hS V G a K hK b ξ L f hf
```

**`AlgebraicGeometry.Space.exists_galois_equivariant_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientFieldPointsUnconditional.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientFieldPointsUnconditional.lean#L79). The attribute's comment: “the Galois-equivariant lift of a field-valued point of the quotient”.

> **Stacks 02Z5, the Galois-equivariant lift.** Let a group `G` act on an object `V` of the
> big fppf site over `S` so that no nonidentity element fixes a point of `V` together with its
> residue field. Then every `K`-valued point `ξ` of the quotient `V/G` is the image of an
> equivariant point over a finite Galois extension of `K`: there are a finite Galois extension
> `L/K`, a finite subgroup `H` of `G`, an isomorphism `H ≃* Gal(L/K)` and a morphism
> `Spec L ⟶ V` over the given point of the base which is equivariant for that isomorphism and
> whose image in the quotient is the pullback of `ξ`.
>
> This is `AlgebraicGeometry.Space.exists_galois_equivariant_lift_of_descent` with its descent
> hypothesis discharged by
> `AlgebraicGeometry.Space.isEffectiveDescentAlongCoveringSieve_monomorphisms_inf_lft`.

```lean
theorem exists_galois_equivariant_lift
    (ha : ActsNontriviallyOnFixedResidueFields (underlyingOver B hS V) G a)
    (ξ : (actionQuotient G B hS V a).obj (op (fieldObject (hS := hS) K hK b))) :
    ∃ (L : Type u) (_ : Field L) (_ : Algebra K L) (_ : FiniteDimensional K L)
      (_ : IsGalois K L) (H : Subgroup G) (_ : Finite H) (e : H ≃* (L ≃ₐ[K] L))
      (f : Spec (.of L) ⟶ (underlyingOver B hS V).left)
      (hf : f ≫ (underlyingOver B hS V).hom =
        Spec.map (CommRingCat.ofHom (algebraMap K L)) ≫ b),
      (∀ h : H,
        Spec.map (CommRingCat.ofHom (e h⁻¹).toRingHom) ≫ f = f ≫ (a h.1).asIso.hom.left) ∧
      IsQuotientLift B hS V G a K hK b ξ L f hf
```

**`AlgebraicGeometry.Space.exists_galois_equivariant_lift_and_existsUnique_quotientPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientFieldPointsUnconditional.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/ActionQuotientFieldPointsUnconditional.lean#L106).

> **Stacks 02Z5.** Let a group `G` act on an object `V` of the big fppf site over `S` so
> that condition `(*)` of Stacks 02Z2 holds: no nonidentity element fixes a point of `V`
> together with its residue field. Then for a field `K` with a point `Spec K ⟶ S` of the base:
>
> * every `K`-valued point `ξ` of the quotient `V/G` comes from a finite Galois extension `L/K`,
>   a finite subgroup `H ⊆ G`, an isomorphism `H ≃* Gal(L/K)` and an `H`-equivariant morphism
>   `Spec L ⟶ V` over the base whose image in the quotient is the pullback of `ξ`;
> * conversely, such data determine a `K`-valued point of `V/G`: there is exactly one whose
>   pullback to `Spec L` is the image of the given morphism `Spec L ⟶ V`.
>
> The two halves are `AlgebraicGeometry.Space.exists_galois_equivariant_lift` and
> `AlgebraicGeometry.Space.existsUnique_quotientPoint_of_galois_equivariant`.

```lean
theorem exists_galois_equivariant_lift_and_existsUnique_quotientPoint
    (ha : ActsNontriviallyOnFixedResidueFields (underlyingOver B hS V) G a) :
    (∀ ξ : (actionQuotient G B hS V a).obj (op (fieldObject (hS := hS) K hK b)),
      ∃ (L : Type u) (_ : Field L) (_ : Algebra K L) (_ : FiniteDimensional K L)
        (_ : IsGalois K L) (H : Subgroup G) (_ : Finite H) (e : H ≃* (L ≃ₐ[K] L))
        (f : Spec (.of L) ⟶ (underlyingOver B hS V).left)
        (hf : f ≫ (underlyingOver B hS V).hom =
          Spec.map (CommRingCat.ofHom (algebraMap K L)) ≫ b),
        (∀ h : H,
          Spec.map (CommRingCat.ofHom (e h⁻¹).toRingHom) ≫ f = f ≫ (a h.1).asIso.hom.left) ∧
        IsQuotientLift B hS V G a K hK b ξ L f hf) ∧
    (∀ (L : Type u) [Field L] [Algebra K L] [FiniteDimensional K L] [IsGalois K L]
      (H : Subgroup G) [Finite H] (e : H ≃* (L ≃ₐ[K] L))
      (f : Spec (.of L) ⟶ (underlyingOver B hS V).left)
      (hf : f ≫ (underlyingOver B hS V).hom =
        Spec.map (CommRingCat.ofHom (algebraMap K L)) ≫ b),
      (∀ h : H,
        Spec.map (CommRingCat.ofHom (e h⁻¹).toRingHom) ≫ f = f ≫ (a h.1).asIso.hom.left) →
      ∃! ξ : (actionQuotient G B hS V a).obj (op (fieldObject (hS := hS) K hK b)),
        IsQuotientLift B hS V G a K hK b ξ L f hf)
```

## Tag 02Z6, an example

[Tag 02Z6](https://stacks.math.columbia.edu/tag/02Z6) in the Stacks Project.

**`AlgebraicGeometry.RationalGaloisQuotient.galoisAction_nontrivialOnFixedResidueFields`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotient.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotient.lean#L169). The attribute's comment: “qbar\_quotient\_algebraic\_space”.

> **Stacks 02Z6.** Every nonidentity element of the absolute Galois group of `ℚ` acts
> nontrivially on the residue field at the unique point of `Spec ℚ̄`.

```lean
theorem galoisAction_nontrivialOnFixedResidueFields :
    Space.ActsNontriviallyOnFixedResidueFields
      (Space.underlyingOver B hS (siteCover B hS hU)) galoisGroup (galoisAction B hS hU)
```

**`AlgebraicGeometry.RationalGaloisQuotient.fieldPoint_algEquiv_algebraicClosure_or_real`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotient.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/RationalGaloisQuotient.lean#L227). The attribute's comment: “qbar\_quotient\_field\_points”.

> **Stacks 02Z6.** A field algebraic over `ℚ` carrying a point of the Galois quotient of
> `Spec ℚ̄` is isomorphic over `ℚ` either to `ℚ̄` itself or to the field `algebraicClosure ℚ ℝ`
> of real algebraic numbers.
>
> The point lifts to a morphism `Spec L → Spec ℚ̄` for a finite extension `L` of the field, so
> `L` is algebraic over `ℚ` and receives `ℚ̄`, hence is a copy of `ℚ̄` and is algebraically
> closed; the Artin–Schreier degree bound in characteristic zero then leaves only degree one
> and degree two, and the quadratic case is the real closure.

```lean
theorem fieldPoint_algEquiv_algebraicClosure_or_real
    (K : Type) [Field K] [Algebra ℚ K] [Algebra.IsAlgebraic ℚ K]
    (hK : B.Contains (Spec (.of K))) (b : Spec (.of K) ⟶ base)
    (ξ : (galoisQuotient B hS hU).obj
      (op (Over.mk (ObjectProperty.homMk b : B.obj hK ⟶ B.obj hS)))) :
    Nonempty (K ≃ₐ[ℚ] AlgebraicClosure ℚ) ∨
      Nonempty (K ≃ₐ[ℚ] algebraicClosure ℚ ℝ)
```

## Tag 02Z7, an example

[Tag 02Z7](https://stacks.math.columbia.edu/tag/02Z7) in the Stacks Project.

**`AlgebraicGeometry.AffineLineTranslation.translationAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation.lean#L87). The attribute's comment: “translation\_quotient”.

> **Stacks 02Z7.** The action of the integers on the affine line over `k` by
> translation.

```lean
def translationAction : Multiplicative ℤ →* Aut (affineLine k)
```

**`AlgebraicGeometry.AffineLineTranslation.translationAction_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation.lean#L93). The attribute's comment: “translation\_quotient”.

> **Stacks 02Z7.** The integer `n` acts on the standard coordinate of the affine line by
> `x ↦ x + n`.

```lean
theorem translationAction_apply (n : ℤ) :
    ((translationAction k (Multiplicative.ofAdd n)).asIso.hom.left).appTop
      (AffineSpace.coord (Spec (.of k)) PUnit.unit) =
      AffineSpace.coord (Spec (.of k)) PUnit.unit +
        (n : Γ(AffineSpace PUnit.{u + 1} (Spec (.of k)), ⊤))
```

**`AlgebraicGeometry.AffineLineTranslation.translationQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation.lean#L135). The attribute's comment: “translation\_quotient”.

> **Stacks 02Z7.** The fppf sheaf quotient of the affine line over `k` by integer
> translations.

```lean
abbrev translationQuotient (B : BigFppfSite.{u}) (hS : B.Contains (Spec (.of k)))
    (hU : B.Contains (affineLine k).left)
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    (BigFppfOver B (Spec (.of k)) hS)ᵒᵖ ⥤ Type u
```

**`AlgebraicGeometry.AffineLineTranslation.genericQuotientMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation/GenericPointFibre.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation/GenericPointFibre.lean#L396). The attribute's comment: “the generic point of the quotient”.

> The generic point of the affine line over `k`, as a morphism `γ : Spec k(x) ⟶ X = 𝔸¹_k/ℤ`
> of fppf sheaves over `Spec k`: the generic point of the line followed by the projection onto
> the quotient.

```lean
def genericQuotientMorphism (hU : B.Contains (affineLine k).left) :
    points (siteOver k B hS) (genericPointOver k) ⟶ translationQuotient k B hS hU
```

**`AlgebraicGeometry.AffineLineTranslation.isPullback_genericQuotientMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation/GenericPointFibre.lean, line 447](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation/GenericPointFibre.lean#L447). The attribute's comment: “the self-fibre-product of the generic point”.

> **Stacks 02Z7, the self-fibre-product of the generic point.** The fibre product
> `Spec k(x) ×_{γ, X, γ} Spec k(x)` over `X = 𝔸¹_k/ℤ` is the disjoint union of one copy of
> `Spec k(x)` for every integer: it is the graph relation of the translation action of `ℤ` on
> `Spec k(x)`, whose two projections send the summand indexed by `n` to the translate of the
> generic point by `n` and to the generic point itself.
>
> The kernel pair of the projection `𝔸¹_k ⟶ 𝔸¹_k/ℤ` is the graph relation of the action on the
> line — this is Stacks 0265 in the form
> `Stacks.Groupoids.quotientChart_app_eq_iff_rel` — and that relation restricts along the
> monomorphism `Spec k(x) ⟶ 𝔸¹_k` to the graph relation of the action on `Spec k(x)`.

```lean
theorem isPullback_genericQuotientMorphism [CharZero k]
    (hU : B.Contains (affineLine k).left) :
    IsPullback
      ((siteOver k B hS).op.whiskerLeft (yoneda.map
        (Space.actionRelationTarget (genericPointOver k) (Multiplicative ℤ)
          (genericPointTranslationAction k))))
      ((siteOver k B hS).op.whiskerLeft (yoneda.map
        (Space.actionRelationSource (genericPointOver k) (Multiplicative ℤ))))
      (genericQuotientMorphism k B hS hU) (genericQuotientMorphism k B hS hU)
```

**`AlgebraicGeometry.AffineLineTranslation.not_mono_genericQuotientMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation/GenericPointFibre.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslation/GenericPointFibre.lean#L524). The attribute's comment: “gamma is not a monomorphism”.

> **Stacks 02Z7, part 1.** The generic point `γ : Spec k(x) ⟶ 𝔸¹_k/ℤ` is *not* a
> monomorphism: translating the indeterminate by one is a nonidentity automorphism of
> `Spec k(x)` which `γ` does not separate, because the translation is identified with the
> identity in the quotient. It is the summand indexed by `1` of the self-fibre-product computed
> in `AlgebraicGeometry.AffineLineTranslation.isPullback_genericQuotientMorphism` on which the
> two projections differ.

```lean
theorem not_mono_genericQuotientMorphism [CharZero k]
    (hU : B.Contains (affineLine k).left) (hG : B.Contains (Spec (.of (RatFunc k)))) :
    ¬ Mono (genericQuotientMorphism k B hS hU)
```

**`AlgebraicGeometry.AffineLineTranslation.not_hasMonomorphicFieldRepresentative_genericQuotientPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslationNotDecent.lean, line 631](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslationNotDecent.lean#L631). The attribute's comment: “no monomorphic field-valued representative of the generic point”.

> **Stacks 02Z7, part 3.** The generic point of the quotient `X = 𝔸¹_k/ℤ` has *no*
> monomorphic field-valued representative: no monomorphism `Spec L ⟶ X` from the spectrum of a
> field presents it.
>
> If `p` were one, with field `L`, then `p` would lift to the line over an extension `M` of `L`
> of finite type, hence algebraic, and the coordinate `z` of that lift would agree, up to an
> integer translation, with the indeterminate: so `z` is transcendental over `k`, and `L(z)` has
> two embeddings into a single field differing by one on `z`. Monomorphy of `p` forces those two
> embeddings to agree on `L`, which makes the minimal polynomial of `z` over `L` invariant under
> translating the variable by one. In characteristic zero no nonconstant polynomial is.

```lean
theorem not_hasMonomorphicFieldRepresentative_genericQuotientPoint (k : Type u) [Field k]
    [CharZero k] (B : BigFppfSite.{u}) (hS : B.Contains (Spec (.of k)))
    (hG : B.Contains (Spec (.of (RatFunc k))))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    ¬ Space.HasMonomorphicFieldRepresentative B (Spec (.of k)) hS
      (translationQuotient k B hS (contains_affineLine k B hS))
      ((genericQuotientPoint k B hS hG).class B (Spec (.of k)) hS
        (translationQuotient k B hS (contains_affineLine k B hS)))
```

**`AlgebraicGeometry.AffineLineTranslation.not_exists_mono_factorisation_genericQuotientPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslationNotDecent.lean, line 725](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslationNotDecent.lean#L725). The attribute's comment: “gamma factors through no monomorphism from a field spectrum”.

> The generic point `γ : Spec k(x) ⟶ X = 𝔸¹_k/ℤ` factors through no monomorphism from the
> spectrum of a field: there is no field-valued point `p` of `X` whose presenting morphism
> `Spec L ⟶ X` is a monomorphism and through which `γ` factors.

```lean
theorem not_exists_mono_factorisation_genericQuotientPoint (k : Type u) [Field k] [CharZero k]
    (B : BigFppfSite.{u}) (hS : B.Contains (Spec (.of k)))
    (hG : B.Contains (Spec (.of (RatFunc k))))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    ¬ ∃ (p : Space.FieldValuedPoint B (Spec (.of k)) hS
          (translationQuotient k B hS (contains_affineLine k B hS)))
        (f : (genericQuotientPoint k B hS hG).siteObject B (Spec (.of k)) hS
          (translationQuotient k B hS (contains_affineLine k B hS)) ⟶
            p.siteObject B (Spec (.of k)) hS
              (translationQuotient k B hS (contains_affineLine k B hS))),
        Mono (Space.fieldMorphism B (Spec (.of k)) hS
            (translationQuotient k B hS (contains_affineLine k B hS)) p) ∧
          yoneda.map f ≫ Space.fieldMorphism B (Spec (.of k)) hS
              (translationQuotient k B hS (contains_affineLine k B hS)) p =
            Space.fieldMorphism B (Spec (.of k)) hS
              (translationQuotient k B hS (contains_affineLine k B hS))
              (genericQuotientPoint k B hS hG)
```

## Tag 02Z8, an example

[Tag 02Z8](https://stacks.math.columbia.edu/tag/02Z8) in the Stacks Project.

**`AlgebraicGeometry.Space.InfiniteProduct.pow_card_eq_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L171). The attribute's comment: “residue\_fields\_and\_closed\_points”.

> **Stacks Project, Tag 02Z8.** Every element of the product of copies of a finite field
> satisfies `x ^ q = x`, where `q` is the number of elements of the field.

```lean
theorem pow_card_eq_self (x : productRing K) : x ^ Nat.card K = x
```

**`AlgebraicGeometry.Space.InfiniteProduct.nonempty_algEquiv_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L231). The attribute's comment: “residue\_fields\_and\_closed\_points”.

> **Stacks Project, Tag 02Z8.** The residue field at any prime of the product is
> isomorphic to the factor field, compatibly with its diagonal `K`-algebra structure.

```lean
theorem nonempty_algEquiv_residueField (p : PrimeSpectrum (productRing K)) :
    Nonempty (K ≃ₐ[K] p.asIdeal.ResidueField)
```

**`AlgebraicGeometry.Space.InfiniteProduct.isClosed_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L243). The attribute's comment: “residue\_fields\_and\_closed\_points”.

> **Stacks Project, Tag 02Z8.** Every point of the spectrum of the product of copies of a
> finite field is closed.

```lean
theorem isClosed_singleton (x : space K) : IsClosed ({x} : Set (space K))
```

**`AlgebraicGeometry.Space.InfiniteProduct.dense_coordinatePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L275). The attribute's comment: “coordinate\_points\_dense”.

> **Stacks Project, Tag 02Z8.** The points of the spectrum of `∏ n : ℕ, k` determined by
> the coordinate projections form a dense subset.

```lean
theorem dense_coordinatePoints (K : Type u) [Field K] :
    Dense (Set.range (fun n : ℕ ↦ (coordinate K n).base (default : base K)))
```

**`AlgebraicGeometry.Space.InfiniteProduct.exists_unit_mul_idempotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L303). The attribute's comment: “clopen\_basis”.

> **Stacks Project, Tag 02Z8.** Every element of a product of copies of a field is a unit
> times an idempotent.

```lean
theorem exists_unit_mul_idempotent (x : productRing K) :
    ∃ (u : (productRing K)ˣ) (e : productRing K),
      IsIdempotentElem e ∧ x = (u : productRing K) * e
```

**`AlgebraicGeometry.Space.InfiniteProduct.isTopologicalBasis_isClopen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L321). The attribute's comment: “clopen\_basis”.

> **Stacks Project, Tag 02Z8.** The clopen subsets of the spectrum of `∏ n : ℕ, k` form a
> topological basis.

```lean
theorem isTopologicalBasis_isClopen :
    TopologicalSpace.IsTopologicalBasis {s : Set (space K) | IsClopen s}
```

**`AlgebraicGeometry.Space.InfiniteProduct.instTotallyDisconnectedSpace`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L337). The attribute's comment: “clopen\_basis”.

> **Stacks Project, Tag 02Z8.** The spectrum of `∏ n : ℕ, k` is totally disconnected.

```lean
instance instTotallyDisconnectedSpace : TotallyDisconnectedSpace (space K)
```

**`AlgebraicGeometry.Space.InfiniteProduct.isOpen_singleton_iff_coordinate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L362). The attribute's comment: “coordinate\_and\_other\_points”.

> **Stacks Project, Tag 02Z8.** The open points of the spectrum of `∏ n : ℕ, k` are
> precisely the points coming from the coordinate projections.

```lean
theorem isOpen_singleton_iff_coordinate (x : space K) :
    IsOpen ({x} : Set (space K)) ↔
      ∃ n : ℕ, x = (coordinate K n).base (default : base K)
```

**`AlgebraicGeometry.Space.InfiniteProduct.exists_noncoordinate_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L385). The attribute's comment: “coordinate\_and\_other\_points”.

> **Stacks Project, Tag 02Z8.** The spectrum of `∏ n : ℕ, k` has a point not coming from any
> coordinate projection.

```lean
theorem exists_noncoordinate_point :
    ∃ x : space K, ∀ n : ℕ, x ≠ (coordinate K n).base (default : base K)
```

**`AlgebraicGeometry.Space.InfiniteProduct.not_discreteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProduct.lean#L410). The attribute's comment: “coordinate\_and\_other\_points”.

> **Stacks Project, Tag 02Z8.** The spectrum of `∏ n : ℕ, k` is not discrete.

```lean
theorem not_discreteTopology : ¬ DiscreteTopology (space K)
```

**`AlgebraicGeometry.Space.InfiniteProduct.isEtaleEquivalenceRelation_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean#L136). The attribute's comment: “the charted relation is an étale equivalence relation”.

> **Stacks 02Z8.** The two charted projections form an étale equivalence relation on `U` in
> the big fppf site over `S`.

```lean
theorem isEtaleEquivalenceRelation_chart :
    Stacks.Groupoids.IsEtaleEquivalenceRelation
      (Space.relation B (base k) hS (chartSource k B hS hU hR) (chartTarget k B hS hU hR))
```

**`AlgebraicGeometry.Space.InfiniteProduct.isAlgebraicSpace_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean#L156). The attribute's comment: “the quotient X = U/R is an algebraic space”.

> **Stacks 02Z8.** The quotient `X = U/R` is an algebraic space over `S`. This is Stacks
> 02WW applied to the étale equivalence relation of the example.

```lean
theorem isAlgebraicSpace_quotient :
    IsAlgebraicSpace B (base k) hS (quotient k B hS hU hR)
```

**`AlgebraicGeometry.Space.InfiniteProduct.quotientMap_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean#L165). The attribute's comment: “the quotient map U ⟶ X is surjective”.

> **Stacks 02Z8.** The quotient map `U ⟶ X` is surjective after every representable base
> change: the morphism `|U| → |X|` of the source is surjective.

```lean
theorem quotientMap_surjective :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Surjective.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B (base k) hS)))
      (Space.quotientMap B (base k) hS (chartSource k B hS hU hR)
        (chartTarget k B hS hU hR))
```

**`AlgebraicGeometry.Space.InfiniteProduct.quotientMap_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean#L178). The attribute's comment: “the quotient map U ⟶ X is étale”.

> **Stacks 02Z8.** The quotient map `U ⟶ X` is étale after every representable base
> change.

```lean
theorem quotientMap_etale :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@Etale.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B (base k) hS)))
      (Space.quotientMap B (base k) hS (chartSource k B hS hU hR)
        (chartTarget k B hS hU hR))
```

**`AlgebraicGeometry.Space.InfiniteProduct.presentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean#L191). The attribute's comment: “the presentation of X by U and R”.

> **Stacks 02Z8.** The triple `(U, R, U ⟶ X)` is a presentation of the algebraic space
> `X = U/R`.

```lean
noncomputable def presentation :
    Space.Presentation B (base k) hS (quotient k B hS hU hR)
      (isAlgebraicSpace_quotient k B hS hU hR)
```

**`AlgebraicGeometry.Space.InfiniteProduct.quotientMap_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean#L204). The attribute's comment: “exactly the related points of U are identified in X”.

> **Stacks 02Z8.** The relation `R` is the fibre product `U ×_X U`: the points of `U` that
> become equal in `X` are exactly the ones related by `R`. Together with
> `AlgebraicGeometry.Space.InfiniteProduct.quotientMap_comp_chartCoordinate_eq` this is the
> assertion of the source that the coordinate points of `U` all map to one point of `X` and
> that no other point of `U` gets identified with anything.

```lean
theorem quotientMap_isPullback :
    IsPullback (yoneda.map (chartTarget k B hS hU hR))
      (yoneda.map (chartSource k B hS hU hR))
      (Space.quotientMap B (base k) hS (chartSource k B hS hU hR)
        (chartTarget k B hS hU hR))
      (Space.quotientMap B (base k) hS (chartSource k B hS hU hR)
        (chartTarget k B hS hU hR))
```

**`AlgebraicGeometry.Space.InfiniteProduct.quotientMap_comp_chartCoordinate_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean#L291). The attribute's comment: “all the coordinate points of U map to one point of X”.

> **Stacks 02Z8.** All the coordinate points of `U` have the same image in `X`: the
> composites of the coordinate morphisms `S ⟶ U` with the quotient map agree.

```lean
theorem quotientMap_comp_chartCoordinate_eq (n m : ℕ) :
    yoneda.map (chartCoordinate k B hS hU n) ≫
        Space.quotientMap B (base k) hS (chartSource k B hS hU hR)
          (chartTarget k B hS hU hR) =
      yoneda.map (chartCoordinate k B hS hU m) ≫
        Space.quotientMap B (base k) hS (chartSource k B hS hU hR)
          (chartTarget k B hS hU hR)
```

**`AlgebraicGeometry.Space.InfiniteProduct.coordinatePoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotient.lean#L309). The attribute's comment: “x₀ is the image of a section S ⟶ X”.

> **Stacks 02Z8.** The point `x₀` of `X`: the common image of all the coordinate points of
> `U`. It is a section of the structure morphism of `X`, the base `S` being a terminal object
> of the site by `AlgebraicGeometry.Space.InfiniteProduct.isTerminal_baseChart`.

```lean
noncomputable def coordinatePoint :
    yoneda.obj (baseChart k B hS) ⟶ quotient k B hS hU hR
```

**`AlgebraicGeometry.Space.InfiniteProduct.surjective_pointsMap_quotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotientPoints.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotientPoints.lean#L104). The attribute's comment: “the map |U| → |X| is surjective”.

> **Stacks 02Z8.** The map `|U| → |X|` is surjective.

```lean
theorem surjective_pointsMap_quotientMap :
    Function.Surjective (pointsMap B (base K) hS (yoneda.obj (spaceChart K B hS hU))
      (Space.quotientMap B (base K) hS (chartSource K B hS hU hR)
        (chartTarget K B hS hU hR)))
```

**`AlgebraicGeometry.Space.InfiniteProduct.continuous_pointsMap_quotientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotientPoints.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotientPoints.lean#L112). The attribute's comment: “the map |U| → |X| is continuous”.

> **Stacks 02Z8.** The map `|U| → |X|` is continuous.

```lean
theorem continuous_pointsMap_quotientMap :
    Continuous (pointsMap B (base K) hS (yoneda.obj (spaceChart K B hS hU))
      (Space.quotientMap B (base K) hS (chartSource K B hS hU hR)
        (chartTarget K B hS hU hR)))
```

**`AlgebraicGeometry.Space.InfiniteProduct.pointsMap_quotientMap_coordinatePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotientPoints.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotientPoints.lean#L121). The attribute's comment: “the coordinate points of |U| all map to x₀”.

> **Stacks 02Z8.** The point of `|U|` of the `n`-th coordinate maps to the point `x₀` of
> `|X|`, for every `n`: all the coordinate points of `|U|` are identified in `|X|`.

```lean
theorem pointsMap_quotientMap_coordinatePoint (n : ℕ) :
    pointsMap B (base K) hS (yoneda.obj (spaceChart K B hS hU))
        (Space.quotientMap B (base K) hS (chartSource K B hS hU hR)
          (chartTarget K B hS hU hR))
        ((schemePointsHomeomorph B (base K) hS (spaceChart K B hS hU)).symm
          ((coordinate K n).base (default : base K))) =
      pointsMap B (base K) hS (yoneda.obj (baseChart K B hS))
        (coordinatePoint K B hS hU hR) (basePoint K B hS)
```

**`AlgebraicGeometry.Space.InfiniteProduct.dense_range_pointsMap_coordinatePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotientPoints.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductQuotientPoints.lean#L140). The attribute's comment: “the closure of x₀ is all of |X|”.

> **Stacks 02Z8.** The image of the section `S ⟶ X` is dense in `|X|`: the point `x₀` has
> closure all of `|X|`, so `|X|` is irreducible with generic point `x₀`.
>
> The coordinate points are dense in `|U|` by
> `AlgebraicGeometry.Space.InfiniteProduct.dense_coordinatePoints`, the map `|U| → |X|` is
> continuous and surjective, and it carries every coordinate point to `x₀`.

```lean
theorem dense_range_pointsMap_coordinatePoint :
    Dense (Set.range (pointsMap B (base K) hS (yoneda.obj (baseChart K B hS))
      (coordinatePoint K B hS hU hR)))
```

**`AlgebraicGeometry.Space.InfiniteProduct.isOpenImmersion_coordinate`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean#L88). The attribute's comment: “the coordinate morphisms are open immersions”.

> **Stacks 02Z8.** Each coordinate projection of the product ring defines an open immersion
> `S ⟶ U`: it is the localization of the product at the idempotent supported at `n`.

```lean
instance isOpenImmersion_coordinate (n : ℕ) : IsOpenImmersion (coordinate k n)
```

**`AlgebraicGeometry.Space.InfiniteProduct.isClosedImmersion_coordinate`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean#L95). The attribute's comment: “the coordinate morphisms are closed immersions”.

> **Stacks 02Z8.** Each coordinate projection of the product ring defines a closed immersion
> `S ⟶ U`: the projection is a surjective ring homomorphism.

```lean
instance isClosedImmersion_coordinate (n : ℕ) : IsClosedImmersion (coordinate k n)
```

**`AlgebraicGeometry.Space.InfiniteProduct.isEmpty_of_coordinate_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean#L119). The attribute's comment: “distinct coordinate morphisms are disjoint”.

> **Stacks 02Z8.** Distinct coordinate morphisms are disjoint: a scheme mapping to `S` in
> two ways whose composites with `f_n` and with `f_m` agree is empty when `n ≠ m`.

```lean
theorem isEmpty_of_coordinate_eq {T : Scheme.{u}} {n m : ℕ} (hnm : n ≠ m) (a b : T ⟶ base k)
    (h : a ≫ coordinate k n = b ≫ coordinate k m) : IsEmpty T
```

**`AlgebraicGeometry.Space.InfiniteProduct.etale_relationTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean#L202). The attribute's comment: “the target projection is étale”.

> **Stacks 02Z8.** The target projection of the relation is étale: it is the identity on
> one summand and an open immersion on each of the others.

```lean
theorem etale_relationTarget : Etale (relationTarget k)
```

**`AlgebraicGeometry.Space.InfiniteProduct.etale_relationSource`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean#L211). The attribute's comment: “the source projection is étale”.

> **Stacks 02Z8.** The source projection of the relation is étale: it is the identity on
> one summand and an open immersion on each of the others.

```lean
theorem etale_relationSource : Etale (relationSource k)
```

**`AlgebraicGeometry.Space.InfiniteProduct.isEquivalenceRelation_relation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean#L369). The attribute's comment: “the relation is an equivalence relation”.

> **Stacks 02Z8.** The two projections of `R` are an internal equivalence relation on `U`
> in the category of schemes.

```lean
theorem isEquivalenceRelation_relation :
    IsEquivalenceRelation (relationTarget k) (relationSource k)
```

**`AlgebraicGeometry.Space.InfiniteProduct.isEtaleEquivalenceRelation_preRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/PointsAndCoverings/InfiniteProductRelation.lean#L454). The attribute's comment: “the pre-relation is an étale equivalence relation”.

> **Stacks 02Z8.** The pre-relation of the example is an étale equivalence relation over
> `S`: this is the hypothesis under which Stacks 02WW produces the algebraic space `X = U/R`.

```lean
theorem isEtaleEquivalenceRelation_preRelation :
    Stacks.Groupoids.IsEtaleEquivalenceRelation (preRelation k)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.14, Tag 02Z0](https://stacks.math.columbia.edu/tag/02Z0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

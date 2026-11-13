---
declaration: section
origin: cited
lean: AlgebraicGeometry.isEffectiveCartierDivisor_comap_pullback, Stacks.Divisors.IsRelativeEffectiveCartierDivisor, AlgebraicGeometry.isRelativeEffectiveCartierDivisor_mul, Stacks.Divisors.isRelativeEffectiveCartierDivisor_of_mul_eq, AlgebraicGeometry.isFlatAt_of_relativeEffectiveCartierDivisor, Stacks.AlgebraicGeometry.exists_open_flat_of_isRelativeEffectiveCartierDivisor, AlgebraicGeometry.flat_of_flat_off_relativeEffectiveCartierDivisor, AlgebraicGeometry.NonflatAmbient.not_flat_ambientRing
statement: formalized
proof: formalized
---

# 31.19 Relative effective Cartier divisors

Section 31.19 of the Stacks Project, [Tag 056P](https://stacks.math.columbia.edu/tag/056P). 9 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 056Q, a lemma

[Tag 056Q](https://stacks.math.columbia.edu/tag/056Q) in the Stacks Project.

**`AlgebraicGeometry.isEffectiveCartierDivisor_comap_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/BaseChangeDivisor.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/BaseChangeDivisor.lean#L123). References: EGA IV (21.15.9), “partial”.

> A relative effective Cartier divisor stays effective Cartier under arbitrary base
> change.

```lean
theorem isEffectiveCartierDivisor_comap_pullback {X S S' : Scheme.{u}}
    (f : X ⟶ S) (g : S' ⟶ S) (I : X.IdealSheafData)
    (hI : IsEffectiveCartierDivisor I)
    [Flat (I.subschemeι ≫ f)] :
    IsEffectiveCartierDivisor
      (I.comap (pullback.snd g f))
```

## Tag 062T, a definition

[Tag 062T](https://stacks.math.columbia.edu/tag/062T) in the Stacks Project.

**`Stacks.Divisors.IsRelativeEffectiveCartierDivisor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Picard/RelativeEffectiveCartier.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Picard/RelativeEffectiveCartier.lean#L46).

> **Stacks Project, Tag 062T.** A closed subscheme of `X` is a *relative effective Cartier
> divisor* over `S` when it is an effective Cartier divisor on `X` and its structure morphism to
> `S` is flat.

```lean
abbrev IsRelativeEffectiveCartierDivisor {X S : Scheme.{u}}
    (f : X ⟶ S) (I : X.IdealSheafData) : Prop
```

## Tag 0B8U, a lemma

[Tag 0B8U](https://stacks.math.columbia.edu/tag/0B8U) in the Stacks Project.

**`AlgebraicGeometry.isRelativeEffectiveCartierDivisor_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/RelativeSum.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/RelativeSum.lean#L204).

> **Stacks Project, Tag 0B8U.**  The sum of two relative effective Cartier divisors on `X`
> over `S` is a relative effective Cartier divisor over `S`.

```lean
theorem isRelativeEffectiveCartierDivisor_mul {X S : Scheme.{u}} (f : X ⟶ S)
    (I J : X.IdealSheafData)
    (hI : IsRelativeEffectiveCartierDivisor f I)
    (hJ : IsRelativeEffectiveCartierDivisor f J) :
    IsRelativeEffectiveCartierDivisor f (I * J)
```

## Tag 0B8V, a lemma

[Tag 0B8V](https://stacks.math.columbia.edu/tag/0B8V) in the Stacks Project.

**`Stacks.Divisors.isRelativeEffectiveCartierDivisor_of_mul_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/RelativeDifference.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/EffectiveCartier/RelativeDifference.lean#L288).

> **Stacks Project, Tag 0B8V.** An effective Cartier divisor which is the difference of two
> relative effective Cartier divisors is itself relative.

```lean
theorem isRelativeEffectiveCartierDivisor_of_mul_eq
    {X S : Scheme.{u}} (f : X ⟶ S) (D₁ D₂ E : X.IdealSheafData)
    (hD₁ : IsRelativeEffectiveCartierDivisor f D₁)
    (hD₂ : IsRelativeEffectiveCartierDivisor f D₂)
    (hE : IsEffectiveCartierDivisor E)
    (h : D₂ = D₁ * E) :
    IsRelativeEffectiveCartierDivisor f E
```

## Tag 062U, a lemma

[Tag 062U](https://stacks.math.columbia.edu/tag/062U) in the Stacks Project.

**`AlgebraicGeometry.isFlatAt_of_relativeEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatAtDivisor.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatAtDivisor.lean#L185).

> **Stacks Project, Tag 062U.**  The ambient morphism is flat at a point of a relative
> effective Cartier divisor whose ambient local ring is Noetherian.

```lean
theorem isFlatAt_of_relativeEffectiveCartierDivisor
    {X S : Scheme.{u}} (f : X ⟶ S) (I : X.IdealSheafData)
    (hI : IsRelativeEffectiveCartierDivisor f I)
    (x : X) (hx : x ∈ I.supportSet)
    (hNoetherian : IsNoetherianRing (X.presheaf.stalk x)) :
    IsFlatAt f.toLRSHom.toShHom x
```

## Tag 062V, a lemma

[Tag 062V](https://stacks.math.columbia.edu/tag/062V) in the Stacks Project.

**`Stacks.AlgebraicGeometry.exists_open_flat_of_isRelativeEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatNeighbourhood.lean, line 537](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatNeighbourhood.lean#L537).

> A relative effective Cartier divisor lies in an open subscheme on which the ambient morphism is
> flat, provided that morphism is locally of finite presentation.

```lean
theorem exists_open_flat_of_isRelativeEffectiveCartierDivisor
    {X S : Scheme.{u}} (f : X ⟶ S) (I : X.IdealSheafData)
    (hI : Stacks.Divisors.IsRelativeEffectiveCartierDivisor f I)
    [LocallyOfFinitePresentation f] :
    ∃ U : X.Opens, I.supportSet ⊆ (U : Set X) ∧ Flat (U.ι ≫ f)
```

## Tag 062W, a lemma

[Tag 062W](https://stacks.math.columbia.edu/tag/062W) in the Stacks Project.

**`AlgebraicGeometry.flat_of_flat_off_relativeEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatOffDivisor.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatOffDivisor.lean#L214).

> A morphism flat away from a relative effective Cartier divisor is flat.

```lean
theorem flat_of_flat_off_relativeEffectiveCartierDivisor
    {X S : Scheme.{u}} (f : X ⟶ S) (I : X.IdealSheafData)
    (hI : IsRelativeEffectiveCartierDivisor f I)
    (hf : ∀ x : X, x ∉ I.supportSet →
      IsFlatAt f.toLRSHom.toShHom x) :
    Flat f
```

## Tag 062X, an example

[Tag 062X](https://stacks.math.columbia.edu/tag/062X) in the Stacks Project.

**`AlgebraicGeometry.NonflatAmbient.not_flat_ambientRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean#L149). The attribute's comment: “ambient ring not flat”.

> The ring `B` is not flat over `k[t]`.

```lean
theorem not_flat_ambientRing : ¬ RingHom.Flat (baseMap k)
```

**`AlgebraicGeometry.NonflatAmbient.quotientByX_equiv_polynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean#L436). The attribute's comment: “quotient by x”.

> The quotient `B / xB` is isomorphic to `k[t]` by a ring isomorphism carrying the class of `t`
> to the coordinate and constants to constants.

```lean
theorem quotientByX_equiv_polynomial :
    ∃ e : (ambientRing k ⧸ Ideal.span {x k}) ≃+* Polynomial k,
      e (Ideal.Quotient.mk (Ideal.span {x k}) (t k)) = Polynomial.X ∧
        ∀ a : k,
          e (Ideal.Quotient.mk (Ideal.span {x k})
            (algebraMap k (ambientRing k) a)) = Polynomial.C a
```

**`AlgebraicGeometry.NonflatAmbient.quotientByX_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean, line 508](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean#L508). The attribute's comment: “quotient by x flat”.

> The quotient `B / xB` is flat over `k[t]`.

```lean
theorem quotientByX_flat :
    RingHom.Flat
      ((Ideal.Quotient.mk (Ideal.span {x k})).comp (baseMap k))
```

**`AlgebraicGeometry.NonflatAmbient.x_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean, line 531](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean#L531). The attribute's comment: “x nonzerodivisor”.

> The element `x` is a nonzerodivisor of `B`.

```lean
theorem x_isRegular : IsRegular (x k)
```

**`AlgebraicGeometry.NonflatAmbient.divisor_isRelativeEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean, line 593](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean#L593). The attribute's comment: “relative effective Cartier divisor”.

> The closed subscheme of `Spec B` cut out by `x` is a relative effective Cartier divisor over
> `Spec k[t]`.

```lean
theorem divisor_isRelativeEffectiveCartierDivisor :
    Stacks.Divisors.IsRelativeEffectiveCartierDivisor
      (Spec.map (CommRingCat.ofHom (baseMap k))) (divisor k)
```

**`AlgebraicGeometry.NonflatAmbient.no_flat_neighbourhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean, line 717](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/NonflatAmbientExample.lean#L717). The attribute's comment: “no flat neighbourhood”.

> No open subscheme of `Spec B` containing the divisor is flat over `Spec k[t]`.

```lean
theorem no_flat_neighbourhood
    (U : (Spec (.of (ambientRing k))).Opens)
    (hU : (divisor k).supportSet ⊆ (U : Set (Spec (.of (ambientRing k))))) :
    ¬ Flat (U.ι ≫ Spec.map (CommRingCat.ofHom (baseMap k)))
```

## Tag 062Y, a lemma

[Tag 062Y](https://stacks.math.columbia.edu/tag/062Y) in the Stacks Project.

**`Stacks.Divisors.exists_isRelativeEffectiveCartierDivisor_containing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/ContainingDivisorFibre.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/ContainingDivisorFibre.lean#L313). The attribute's comment: “local\_containing\_divisor”.

> Let `f : X ⟶ S` be flat and locally of finite presentation, let `Z` be a closed subscheme of
> `X` and let `x` be a point of `Z` whose fibre over `f x` is an effective Cartier divisor in a
> neighbourhood of `x`.  Then there is an open neighbourhood `U` of `x` carrying a relative
> effective Cartier divisor `D` over `S` with `Z ∩ U ⊆ D` and `Z_{f x} ∩ U = D_{f x}`.

```lean
theorem exists_isRelativeEffectiveCartierDivisor_containing (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (Z : X.IdealSheafData) (x : X) (hx : x ∈ Z.support)
    (hfib : ∃ N : (f.fiber (f x)).Opens, f.asFiber x ∈ N ∧
      IsEffectiveCartierDivisor ((Z.comap (f.fiberι (f x))).comap N.ι)) :
    ∃ (U : X.Opens) (_ : x ∈ U) (D : U.toScheme.IdealSheafData),
      IsRelativeEffectiveCartierDivisor (U.ι ≫ f) D ∧ D ≤ Z.comap U.ι ∧
        (Z.comap U.ι).comap ((U.ι ≫ f).fiberι (f x)) =
          D.comap ((U.ι ≫ f).fiberι (f x))
```

**`Stacks.Divisors.exists_isRelativeEffectiveCartierDivisor_of_flat_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatCartierFibre.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatCartierFibre.lean#L296). The attribute's comment: “flat\_finitely\_presented\_case”.

> Let `f : X ⟶ S` be flat and locally of finite presentation, let `Z` be a closed subscheme of
> `X` of finite presentation over `X` and let `x` be a point of `Z` at which `Z` is flat over `S` and
> whose fibre over `f x` is an effective Cartier divisor in a neighbourhood of `x`.  Then `Z`
> restricts to a relative effective Cartier divisor over `S` on an affine open neighbourhood of
> `x`.

```lean
theorem exists_isRelativeEffectiveCartierDivisor_of_flat_of_finitePresentation (f : X ⟶ S)
    [Flat f] [LocallyOfFinitePresentation f] (Z : X.IdealSheafData)
    [LocallyOfFinitePresentation Z.subschemeι] (x : X) (hx : x ∈ Z.support)
    (hfib : ∃ V : (f.fiber (f x)).Opens, f.asFiber x ∈ V ∧
      IsEffectiveCartierDivisor ((Z.comap (f.fiberι (f x))).comap V.ι))
    (hflat : ((Z.subschemeι ≫ f).stalkMap (⟨x, hx⟩ : Z.subscheme)).hom.Flat) :
    ∃ V : X.Opens, x ∈ V ∧ IsAffineOpen V ∧
      IsRelativeEffectiveCartierDivisor (V.ι ≫ f) (Z.comap V.ι)
```

**`Stacks.Divisors.isRelativeEffectiveCartierDivisor_of_flat_of_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatCartierFibre.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/FlatCartierFibre.lean#L313). The attribute's comment: “flat\_fibres\_global\_case”. References: EGA IV (21.15.3.3), “converse”.

> A closed subscheme of a scheme flat and locally of finite presentation over `S`, itself flat
> and locally of finite presentation over `S`, all of whose fibres are effective Cartier divisors, is
> a relative effective Cartier divisor over `S`.

```lean
theorem isRelativeEffectiveCartierDivisor_of_flat_of_fibres (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (Z : X.IdealSheafData) [Flat (Z.subschemeι ≫ f)]
    [LocallyOfFinitePresentation (Z.subschemeι ≫ f)]
    (hfib : ∀ s : S, IsEffectiveCartierDivisor (Z.comap (f.fiberι s))) :
    IsRelativeEffectiveCartierDivisor f Z
```

**`Stacks.Divisors.exists_isRelativeEffectiveCartierDivisor_of_ideal_isPrincipal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/LocallyPrincipalFibre.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/LocallyPrincipalFibre.lean#L393). The attribute's comment: “locally\_principal\_case”.

> Let `f : X ⟶ S` be flat and locally of finite presentation, let
> `Z` be a closed subscheme of `X` and let `x` be a point of `Z` whose fibre over `f x` is an
> effective Cartier divisor in a neighbourhood of `x`.  If the ideal of `Z` is principal on some
> affine open neighbourhood of `x`, then `Z` restricts to a relative effective Cartier divisor over
> `S` on an affine open neighbourhood of `x`.

```lean
theorem exists_isRelativeEffectiveCartierDivisor_of_ideal_isPrincipal (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (Z : X.IdealSheafData) (x : X) (hx : x ∈ Z.support)
    (hprin : ∃ U : X.affineOpens, x ∈ (U : X.Opens) ∧ (Z.ideal U).IsPrincipal)
    (hfib : ∃ V : (f.fiber (f x)).Opens, f.asFiber x ∈ V ∧
      IsEffectiveCartierDivisor ((Z.comap (f.fiberι (f x))).comap V.ι)) :
    ∃ V : X.Opens, x ∈ V ∧ IsAffineOpen V ∧
      IsRelativeEffectiveCartierDivisor (V.ι ≫ f) (Z.comap V.ι)
```

**`Stacks.Divisors.isRelativeEffectiveCartierDivisor_of_isLocallyPrincipal_of_fibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/LocallyPrincipalFibre.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/RegularImmersion/LocallyPrincipalFibre.lean#L411). The attribute's comment: “locally\_principal\_global\_case”. References: EGA IV (21.15.3.3), “forward direction”.

> A locally principal closed subscheme of a scheme flat and locally of finite presentation over
> `S`, all of whose fibres are effective Cartier divisors, is a relative effective Cartier divisor
> over `S`.

```lean
theorem isRelativeEffectiveCartierDivisor_of_isLocallyPrincipal_of_fibres (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f] (Z : X.IdealSheafData) (hZ : IsLocallyPrincipal Z)
    (hfib : ∀ s : S, IsEffectiveCartierDivisor (Z.comap (f.fiberι s))) :
    IsRelativeEffectiveCartierDivisor f Z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 31.19, Tag 056P](https://stacks.math.columbia.edu/tag/056P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

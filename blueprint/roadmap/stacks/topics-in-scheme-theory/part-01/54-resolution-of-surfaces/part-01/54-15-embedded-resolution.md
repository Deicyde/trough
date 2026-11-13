---
declaration: section
origin: cited
lean: AlgebraicGeometry.resolveCurve_tfae, AlgebraicGeometry.exists_pointBlowupChain_chainTransform_isRegular, AlgebraicGeometry.IntersectionMultiplicityContext.intersectionMultiplicity_natCast_eq_length, AlgebraicGeometry.strictTransformToCurve_isIso, AlgebraicGeometry.strictTransform_exceptional_unique, AlgebraicGeometry.strictTransform_exceptional_multiplicity_one, AlgebraicGeometry.strictTransform_intersectionMultiplicity_lt, AlgebraicGeometry.exists_pointBlowupChain_familyTransform_isRegular_pairwise_disjoint
statement: formalized
proof: formalized
---

# 54.15 Embedded resolution

Section 54.15 of the Stacks Project, [Tag 0BI3](https://stacks.math.columbia.edu/tag/0BI3). 7 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BI4, a lemma

[Tag 0BI4](https://stacks.math.columbia.edu/tag/0BI4) in the Stacks Project.

**`AlgebraicGeometry.resolveCurve_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveResolution.lean, line 549](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveResolution.lean#L549). References: EGA IV (7.9.1), “more general”.

> **Stacks Project, Tag 0BI4.** For a one-dimensional integral Noetherian scheme `Y` the
> following are equivalent: there is an alteration `X → Y` with `X` regular; there is a resolution
> of singularities of `Y`; there is a finite sequence of blowups in closed points
> `Y_n → … → Y_1 → Y` with `Y_n` regular; and the normalization `Y^ν → Y` is finite.

```lean
theorem resolveCurve_tfae (Y : Scheme.{u}) [IsIntegral Y] [IsNoetherian Y]
    (hYdim : topologicalKrullDim Y = 1) :
    List.TFAE [
      ∃ (X : Scheme.{u}) (f : X ⟶ Y), IsAlteration f ∧ IsRegular X,
      ∃ (X : Scheme.{u}) (f : X ⟶ Y), IsResolution f,
      ∃ (X : Scheme.{u}) (f : X ⟶ Y), PointBlowupChain Y Set.univ X f ∧ IsRegular X,
      IsFinite (Scheme.normalization Y
        finite_irreducibleComponents_isCompactOpen_of_isNoetherian)]
```

## Tag 0BI5, a lemma

[Tag 0BI5](https://stacks.math.columbia.edu/tag/0BI5) in the Stacks Project.

**`AlgebraicGeometry.exists_pointBlowupChain_chainTransform_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/AmbientCurveResolution.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/AmbientCurveResolution.lean#L257).

> Let `X` be a Noetherian scheme and let `Y ⊆ X` be an integral closed subscheme of dimension
> one admitting an alteration by a regular scheme — one of the equivalent conditions of
> [Stacks, Tag 0BI4]. Then there is a finite chain of blowups of `X` at closed points along which
> the strict transform of `Y` becomes a regular curve.

```lean
public theorem exists_pointBlowupChain_chainTransform_isRegular {X : Scheme.{u}}
    [IsNoetherian X] (Y : X.IdealSheafData) [IsIntegral Y.subscheme]
    (hYdim : topologicalKrullDim Y.subscheme = 1)
    (hY : ∃ (Z : Scheme.{u}) (g : Z ⟶ Y.subscheme), IsAlteration g ∧ IsRegular Z) :
    ∃ (W : Scheme.{u}) (f : W ⟶ X) (J : W.IdealSheafData),
      PointBlowupChain X Set.univ W f ∧ ChainTransform Y f J ∧ IsIntegral J.subscheme ∧
        topologicalKrullDim J.subscheme = 1 ∧ IsRegular J.subscheme
```

## Tag 0BI6, an equation

[Tag 0BI6](https://stacks.math.columbia.edu/tag/0BI6) in the Stacks Project.

**`AlgebraicGeometry.IntersectionMultiplicityContext.intersectionMultiplicity_natCast_eq_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/IntersectionMultiplicity.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/IntersectionMultiplicity.lean#L201).

> **Stacks Project, Tag 0BI6.** The intersection multiplicity at `p` is the length of the
> local ring of the scheme-theoretic intersection as an `𝒪_{X,p}`-module.

```lean
theorem intersectionMultiplicity_natCast_eq_length
    (S : IntersectionMultiplicityContext) :
    (S.intersectionMultiplicity : ℕ∞) =
      Module.length (S.X.presheaf.stalk S.p) S.intersectionLocalRing
```

## Tag 0BI7, a lemma

[Tag 0BI7](https://stacks.math.columbia.edu/tag/0BI7) in the Stacks Project.

**`AlgebraicGeometry.strictTransformToCurve_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveStrictTransform.lean, line 654](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveStrictTransform.lean#L654). The attribute's comment: “part (1)”.

> Part (1): a curve regular at the centre is unchanged by strict transform.

```lean
public theorem strictTransformToCurve_isIso
    {X : Scheme.{u}} [IsLocallyNoetherian X] (Y : X.IdealSheafData)
    [IsIntegral Y.subscheme] (hYdim : topologicalKrullDim Y.subscheme = 1)
    (p : X) (hp : IsClosed ({p} : Set X))
    (yPoint : Y.subscheme) (hyPoint : Y.subschemeι yPoint = p)
    (hregular : IsRegularLocalRing (Y.subscheme.presheaf.stalk yPoint)) :
    IsIso (transformToCurve Y p hp)
```

**`AlgebraicGeometry.strictTransform_exceptional_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveStrictTransform.lean, line 726](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveStrictTransform.lean#L726). The attribute's comment: “part (2), unique point”.

> Part (2): the strict transform has exactly one point on the exceptional fibre.

```lean
public theorem strictTransform_exceptional_unique
    {X : Scheme.{u}} [IsLocallyNoetherian X] (Y : X.IdealSheafData)
    [IsIntegral Y.subscheme] (hYdim : topologicalKrullDim Y.subscheme = 1)
    (p : X) (hp : IsClosed ({p} : Set X))
    (yPoint : Y.subscheme) (hyPoint : Y.subschemeι yPoint = p)
    (hregular : IsRegularLocalRing (Y.subscheme.presheaf.stalk yPoint)) :
    ∃! q : (AlgebraicGeometry.blowUp (centerIdeal p hp)),
      q ∈ (transformIdeal Y p hp).support ∧
      q ∈ (AlgebraicGeometry.exceptionalIdeal (centerIdeal p hp)).support
```

**`AlgebraicGeometry.strictTransform_exceptional_multiplicity_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveStrictTransform.lean, line 776](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveStrictTransform.lean#L776). The attribute's comment: “part (2), multiplicity”.

> Part (2): the exceptional intersection has multiplicity one.

```lean
public theorem
    strictTransform_exceptional_multiplicity_one
    {X : Scheme.{u}} [IsLocallyNoetherian X] (Y : X.IdealSheafData)
    [IsIntegral Y.subscheme] (hYdim : topologicalKrullDim Y.subscheme = 1)
    (p : X) (hp : IsClosed ({p} : Set X))
    (yPoint : Y.subscheme) (hyPoint : Y.subschemeι yPoint = p)
    (hregular : IsRegularLocalRing (Y.subscheme.presheaf.stalk yPoint))
    (q : (AlgebraicGeometry.blowUp (centerIdeal p hp)))
    (hq : q ∈ ((transformIdeal Y p hp) ⊔
      AlgebraicGeometry.exceptionalIdeal (centerIdeal p hp)).support) :
    intersectionLength (transformIdeal Y p hp)
      (AlgebraicGeometry.exceptionalIdeal (centerIdeal p hp)) q hq = 1
```

**`AlgebraicGeometry.strictTransform_intersectionMultiplicity_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveStrictTransform.lean, line 1168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveStrictTransform.lean#L1168). The attribute's comment: “part (3)”.

> Part (3): an intersection surviving the blowup has smaller multiplicity.

```lean
public theorem
    strictTransform_intersectionMultiplicity_lt
    (S : AlgebraicGeometry.IntersectionMultiplicityContext.{u})
    (yPoint : S.y.subscheme) (hyPoint : S.y.subschemeι yPoint = S.p)
    (hregular : IsRegularLocalRing (S.y.subscheme.presheaf.stalk yPoint))
    (q : (AlgebraicGeometry.blowUp (centerIdeal S.p S.p_isClosed)))
    (hqExceptional : q ∈
      (AlgebraicGeometry.exceptionalIdeal (centerIdeal S.p S.p_isClosed)).support)
    (hq : q ∈ ((transformIdeal S.y S.p S.p_isClosed) ⊔
      (transformIdeal S.z S.p S.p_isClosed)).support) :
    intersectionLength (transformIdeal S.y S.p S.p_isClosed)
      (transformIdeal S.z S.p S.p_isClosed) q hq <
      S.intersectionMultiplicity
```

## Tag 0BI8, a lemma

[Tag 0BI8](https://stacks.math.columbia.edu/tag/0BI8) in the Stacks Project.

**`AlgebraicGeometry.exists_pointBlowupChain_familyTransform_isRegular_pairwise_disjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveFamilyResolution.lean, line 1195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CurveFamilyResolution.lean#L1195).

> **Stacks Project, Tag 0BI8.** Let `X` be a Noetherian scheme and let
> `Y : Fin n → X.IdealSheafData` be pairwise distinct integral closed subschemes of dimension one,
> each admitting a finite chain of blowups in closed points with regular source — one of the
> equivalent conditions of [Stacks, Tag 0BI4]. Then there is a finite chain of blowups of `X` at
> closed points along which the strict transforms of the `Y i` become pairwise disjoint regular
> curves.

```lean
public theorem exists_pointBlowupChain_familyTransform_isRegular_pairwise_disjoint
    {X : Scheme.{u}} [IsNoetherian X] {n : ℕ} (Y : Fin n → X.IdealSheafData)
    (hYne : Function.Injective Y) (hYint : ∀ i, IsIntegral (Y i).subscheme)
    (hYdim : ∀ i, topologicalKrullDim (Y i).subscheme = 1)
    (hYres : ∀ i, ∃ (V : Scheme.{u}) (g : V ⟶ (Y i).subscheme),
      PointBlowupChain (Y i).subscheme Set.univ V g ∧ IsRegular V) :
    ∃ (W : Scheme.{u}) (f : W ⟶ X) (J : Fin n → W.IdealSheafData),
      PointBlowupChain X Set.univ W f ∧ FamilyTransform Y f J ∧
        (∀ i, IsIntegral (J i).subscheme ∧ topologicalKrullDim (J i).subscheme = 1 ∧
          IsRegular (J i).subscheme) ∧
        Pairwise fun i j : Fin n => Disjoint (J i).support (J j).support
```

## Tag 0BIB, a lemma

[Tag 0BIB](https://stacks.math.columbia.edu/tag/0BIB) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_comap_isEffectiveCartierDivisor_of_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CartierInverseImage.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/CartierInverseImage.lean#L403). The attribute's comment: “a closed subscheme containing no positive-dimensional irreducible component of a regular quasi-compact scheme of dimension at most two becomes an effective Cartier divisor after finitely many blowups at closed points lying over it”.

> **Stacks Project, Tag 0BIB.** Let `X` be a regular scheme of dimension (at most) two which is
> quasi-compact, and let `Z ⊆ X` be a closed subscheme containing no irreducible component of `X` of
> positive dimension: every point in the interior of `Z` is an isolated closed point of `X`. Then
> there is a finite sequence `Xₙ → … → X₁ → X` of blowups at closed points, each lying over a point
> of `Z`, such that the inverse image `Zₙ` of `Z` in `Xₙ` is an effective Cartier divisor.
>
> On a locally Noetherian scheme the condition says exactly that every irreducible component of `X`
> contained in `Z` is a single point; it holds in particular when `Z` contains no irreducible
> component of `X` at all (`IsNowhereDense`). The isolated points of `X` inside `Z` are blown up
> first, which removes them (`isOpenImmersion_blowUpToBase_of_isClopen`); what is left of `Z` then
> contains no irreducible component, and
> `exists_pointBlowupChain_comap_isEffectiveCartierDivisor_of_isNowhereDense` applies.
>
> Both deviations from the literal source are forced. Without quasi-compactness the statement is
> false: `Stacks.ResolutionOfSurfaces.not_forall_isEffectiveCartierDivisor_comap_of_isNowhereDense`
> (countably many copies of `𝔸²_ℚ`, `Z` one closed point in each). "Proper closed subscheme" cannot
> be read literally as `Z ≠ X`, even for Noetherian `X`:
> `Stacks.ResolutionOfSurfaces.not_forall_isEffectiveCartierDivisor_comap_of_ne_bot`
> (`X = 𝔸²_ℚ ⊔ 𝔸²_ℚ`, `Z` one copy, a component of dimension two). On an irreducible `X` the literal
> reading implies the one used here (`isNowhereDense_support_of_ne_bot`). Both counterexamples are in
> the sibling module `CartierInverseImageCounterexamples` (same directory).

```lean
public theorem exists_pointBlowupChain_comap_isEffectiveCartierDivisor_of_isRegular
    (X : Scheme.{u}) [CompactSpace X] (hX : AlgebraicGeometry.IsRegular X)
    (hdim : topologicalKrullDim X ≤ 2) (Z : X.IdealSheafData)
    (hZ : ∀ x ∈ interior (Z.support : Set X), IsClopen ({x} : Set X)) :
    ∃ (Y : Scheme.{u}) (f : Y ⟶ X), PointBlowupChain X (Z.support : Set X) Y f ∧
      Stacks.Divisors.IsEffectiveCartierDivisor (Z.comap f)
```

## Tag 0BIC, a lemma

[Tag 0BIC](https://stacks.math.columbia.edu/tag/0BIC) in the Stacks Project.

**`Stacks.ResolutionOfSurfaces.exists_pointBlowupChain_comap_support_eq_isStrictNormalCrossings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/NormalCrossingsResolution.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/EmbeddedResolution/NormalCrossingsResolution.lean#L156).

> **Stacks Project, Tag 0BIC.** Let `X` be a regular Noetherian scheme of dimension two and let
> `Z ⊆ X` be a closed subscheme containing no irreducible component of `X` — the source's "proper
> closed subscheme" — each of whose one-dimensional irreducible components satisfies the equivalent
> conditions of [Stacks, Tag 0BI4], in the point-blowup form of clause (3) there. Then there is a
> sequence `Xₙ → … → X₁ → X` of blowups at closed points such that the inverse image `Zₙ` of `Z` in
> `Xₙ` is an effective Cartier divisor whose support is the support of a strict normal crossings
> divisor.

```lean
public theorem exists_pointBlowupChain_comap_support_eq_isStrictNormalCrossings
    (X : Scheme.{u}) [IsNoetherian X] (hX : AlgebraicGeometry.IsRegular X)
    (hdim : topologicalKrullDim X = 2) (Z : X.IdealSheafData)
    (hZ : IsNowhereDense (Z.support : Set X))
    (hres : ∀ C : irreducibleComponents Z.subscheme,
      topologicalKrullDim (componentIdeal Z C).subscheme = 1 →
      ∃ (P : Scheme.{u}) (g : P ⟶ (componentIdeal Z C).subscheme),
        PointBlowupChain (componentIdeal Z C).subscheme Set.univ P g ∧
          AlgebraicGeometry.IsRegular P) :
    ∃ (W : Scheme.{u}) (f : W ⟶ X), PointBlowupChain X Set.univ W f ∧
      IsEffectiveCartierDivisor (Z.comap f) ∧
      ∃ (hW : IsLocallyNoetherian W) (D : W.IdealSheafData),
        @IsStrictNormalCrossingsDivisor W hW D ∧
          ((Z.comap f).support : Set W) = (D.support : Set W)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.15, Tag 0BI3](https://stacks.math.columbia.edu/tag/0BI3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

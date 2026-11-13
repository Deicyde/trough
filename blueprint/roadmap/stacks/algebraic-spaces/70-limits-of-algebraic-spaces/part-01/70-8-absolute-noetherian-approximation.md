---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.hasNoetherianApproximation_of_isQuasiCompactSpace, AlgebraicGeometry.isPullback_gluedRelationSource_of_isPullback, AlgebraicGeometry.isPullback_gluedRelationSource
statement: formalized
proof: formalized
---

# 70.8 Absolute Noetherian approximation

Section 70.8 of the Stacks Project, [Tag 07SS](https://stacks.math.columbia.edu/tag/07SS). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07SU, a proposition

[Tag 07SU](https://stacks.math.columbia.edu/tag/07SU) in the Stacks Project.

**`AlgebraicGeometry.Space.hasNoetherianApproximation_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AbsoluteNoetherianApproximation/Main.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AbsoluteNoetherianApproximation/Main.lean#L457).

> Absolute Noetherian approximation. Let `X` be a quasi-compact and quasi-separated algebraic
> space over `Spec ℤ`, the terminal scheme `⊤_ Scheme`, on the big fppf site `B`. Then there are a
> directed set `I` and an inverse system `(X_i)` of algebraic spaces over `I` such that
> (1) the transition morphisms are affine, (2) each `X_i` is quasi-separated and of finite type
> over `ℤ`, and (3) `X = lim X_i`, the limit being taken in presheaves on the site.
>
> The hypotheses are exactly those of the source, and nothing further is assumed: `X` is written
> as a limit by the descending induction over the strata of Stacks 07ST, through
> `AlgebraicGeometry.Space.hasConventionalNoetherianApproximation_of_etaleAtlas`.

```lean
theorem hasNoetherianApproximation_of_isQuasiCompactSpace
    {X : (BigFppfOver B (⊤_ Scheme.{u}) hZ)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (⊤_ Scheme.{u}) hZ X)
    (hqc : IsQuasiCompactSpace B (⊤_ Scheme.{u}) hZ X)
    (hqs : IsAbsolutelyQuasiSeparated B (⊤_ Scheme.{u}) hZ hZ X) :
    HasNoetherianApproximation B (⊤_ Scheme.{u}) hZ hZ X
```

## Tag 07SV, an equation

[Tag 07SV](https://stacks.math.columbia.edu/tag/07SV) in the Stacks Project.

**`AlgebraicGeometry.isPullback_gluedRelationSource_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GluedEtaleRelationTransition.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GluedEtaleRelationTransition.lean#L303). The attribute's comment: “the displayed square is cartesian, for any base-changed fibre square over W”.

> **Stacks Project, Tag 07SV.** The displayed square of the proof of absolute Noetherian
> approximation, in the form in which the proof establishes it.
>
> The data: a morphism `v : V ⟶ V'`, open subschemes `j : W ⟶ V` and `j' : W' ⟶ V'` with `W`
> the inverse image of `W'`, that is with `hj` cartesian; objects `Q`, `Q'` with sections `d`,
> `d'` of projections `p`, `p'` — in the application `Q = W ×_U W`, `Q' = W' ×_{U'} W'`,
> `p` and `p'` are the first projections and `d`, `d'` the diagonals — such that `Q` is the base
> change of `Q'` along `k`, that is with `hQ` cartesian; and the relations `R`, `R'` obtained by
> glueing `V` to `Q` along `W` and `V'` to `Q'` along `W'`, with source maps `s`, `s'` which are
> the identity on the chart `V`, resp. `V'`, and `p`, resp. `p'`, followed by the open immersion
> on the other chart. Then for the morphism `r : R ⟶ R'` induced by `v` and `q` the square
>
> ```
> R  --r-->  R'
> |          |
> s          s'
> v          v
> V  --v-->  V'
> ```
>
> is cartesian. Nothing is assumed about the base over which `Q` and `Q'` are fibre products,
> so this applies verbatim when that base is an algebraic space, as it is in the source.

```lean
theorem isPullback_gluedRelationSource_of_isPullback
    {v : V ⟶ V'} {k : W ⟶ W'} {j : W ⟶ V} {j' : W' ⟶ V'} [IsOpenImmersion j']
    {p : Q ⟶ W} {p' : Q' ⟶ W'} {d : W ⟶ Q} {d' : W' ⟶ Q'} [IsOpenImmersion d']
    {q : Q ⟶ Q'} (hj : IsPullback k j j' v) (hQ : IsPullback q p p' k)
    (hd : d ≫ p = 𝟙 W) (hdq : d ≫ q = k ≫ d')
    {a : V ⟶ R} {b : Q ⟶ R} {a' : V' ⟶ R'} {b' : Q' ⟶ R'}
    (hR : IsPushout j d a b) (hR' : IsPushout j' d' a' b')
    {s : R ⟶ V} (hsa : a ≫ s = 𝟙 V) (hsb : b ≫ s = p ≫ j)
    {s' : R' ⟶ V'} (hsa' : a' ≫ s' = 𝟙 V') (hsb' : b' ≫ s' = p' ≫ j')
    {r : R ⟶ R'} (hra : a ≫ r = v ≫ a') (hrb : b ≫ r = q ≫ b') :
    IsPullback r s s' v
```

**`AlgebraicGeometry.isPullback_gluedRelationSource`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GluedEtaleRelationTransition.lean, line 378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GluedEtaleRelationTransition.lean#L378). The attribute's comment: “the displayed square for R\_i glued from V\_i and W\_i x\_\{U\_i} W\_i is cartesian”.

> **Stacks Project, Tag 07SV.** The displayed square of the proof of absolute Noetherian
> approximation, written out for the construction the source performs. Let `w' : W' ⟶ U'` be
> étale, let `u : U ⟶ U'` be arbitrary, and let `W = W' ×_{U'} U`. Let `j' : W' ⟶ V'` and
> `j : W ⟶ V` be open immersions with `W` the inverse image of `W'`, that is with `hj`
> cartesian. Let `R` be obtained by glueing `V` to `W ×_U W` along the diagonal copy of `W`,
> and `R'` likewise at the primed stage, and let `s`, `s'` be the source maps: the identity on
> the chart `V`, resp. `V'`, and the first projection on the chart `W ×_U W`, resp.
> `W' ×_{U'} W'`. If `r : R ⟶ R'` is the morphism induced by `v` on the glueings, then the
> square formed by `r`, `s`, `s'` and `v` is cartesian.

```lean
theorem isPullback_gluedRelationSource {u : U ⟶ U'} {v : V ⟶ V'} {w' : W' ⟶ U'} [Etale w']
    {j' : W' ⟶ V'} [IsOpenImmersion j'] {j : pullback w' u ⟶ V}
    (hj : IsPullback (pullback.fst w' u) j j' v)
    {a : V ⟶ R} {b : pullback (pullback.snd w' u) (pullback.snd w' u) ⟶ R}
    {a' : V' ⟶ R'} {b' : pullback w' w' ⟶ R'}
    (hR : IsPushout j (pullback.diagonal (pullback.snd w' u)) a b)
    (hR' : IsPushout j' (pullback.diagonal w') a' b')
    {s : R ⟶ V} (hsa : a ≫ s = 𝟙 V)
    (hsb : b ≫ s = pullback.fst (pullback.snd w' u) (pullback.snd w' u) ≫ j)
    {s' : R' ⟶ V'} (hsa' : a' ≫ s' = 𝟙 V') (hsb' : b' ≫ s' = pullback.fst w' w' ≫ j')
    {r : R ⟶ R'} (hra : a ≫ r = v ≫ a')
    (hrb : b ≫ r = etaleRelationTransition w' u ≫ b') :
    IsPullback r s s' v
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.8, Tag 07SS](https://stacks.math.columbia.edu/tag/07SS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

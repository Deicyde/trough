---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.hasNoetherianApproximation_of_isQuasiCompactSpace, AlgebraicGeometry.Space.hasNoetherianApproximation_of_isomorphicPresentation_limit, AlgebraicGeometry.isPullback_gluedRelationSource_of_isPullback, AlgebraicGeometry.isPullback_gluedRelationSource
statement: formalized
proof: formalized
---

# 70.8 Absolute Noetherian approximation

Section 70.8 of the Stacks Project, [Tag 07SS](https://stacks.math.columbia.edu/tag/07SS). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07SU, a proposition

[Tag 07SU](https://stacks.math.columbia.edu/tag/07SU) in the Stacks Project.

**`AlgebraicGeometry.Space.hasNoetherianApproximation_of_isQuasiCompactSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AbsoluteNoetherianApproximation/Main.lean, line 453](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AbsoluteNoetherianApproximation/Main.lean#L453).

> Absolute Noetherian approximation. Let `X` be a quasi-compact and quasi-separated algebraic
> space over `Spec ℤ`, the terminal scheme `⊤_ Scheme`, on the big fppf site `B`. Then there are a
> directed set `I` and an inverse system `(X_i)` of algebraic spaces over `I` such that
> (1) the transition morphisms are affine, (2) each `X_i` is quasi-separated and of finite type
> over `ℤ`, and (3) `X = lim X_i`, the limit being taken in presheaves on the site.

```lean
theorem hasNoetherianApproximation_of_isQuasiCompactSpace
    {X : (BigFppfOver B (⊤_ Scheme.{u}) hZ)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (⊤_ Scheme.{u}) hZ X)
    (hqc : IsQuasiCompactSpace B (⊤_ Scheme.{u}) hZ X)
    (hqs : IsAbsolutelyQuasiSeparated B (⊤_ Scheme.{u}) hZ hZ X) :
    HasNoetherianApproximation B (⊤_ Scheme.{u}) hZ hZ X
```

**`AlgebraicGeometry.Space.hasNoetherianApproximation_of_isomorphicPresentation_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/NoetherianApproximationFromPresentation.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/NoetherianApproximationFromPresentation.lean#L160). The attribute's comment: “granted the Conrad–Lieblich–Olsson construction's output as the general hypothesis hCLO, strengthened by the two cardinality conditions on the index set that make the limit an algebraic space and without which the statement is false”.

> **Stacks 07SU.**  Let `X` be a quasi-compact and quasi-separated algebraic space over `S`.
> Then there are a directed set `I` and an inverse system of algebraic spaces `(X_i, f_{ii'})`
> over `I` whose transition morphisms are affine, whose stages are quasi-separated and of finite
> type over `Spec ℤ`, and whose limit is `X`.
>
> The tag's own hypotheses — `X` an algebraic space, quasi-compact and quasi-separated — are the
> hypotheses here, and the conclusion is the full conclusion of the tag, in the interface
> `AlgebraicGeometry.Space.HasNoetherianApproximation` of
> `StacksFrontier/AlgebraicGeometry/Spaces/NoetherianApproximation.lean`.  What is granted is the
> single general hypothesis `hCLO`, the output of the Conrad–Lieblich–Olsson construction, which
> is quantified over its own algebraic space and does not mention `X`; see the module
> documentation for what it carries and for why it is not this conclusion pre-instantiated.  It
> supplies the two cardinality conditions on the index set that Stacks 07SF, existence needs, and
> which a statement of Stacks 07SU that omits them does not have; that is the correction recorded
> below.
>
> Proved from it: the limit of the system is an algebraic space (Stacks 07SF, existence), it is
> its own Noetherian approximation (`AlgebraicGeometry.Space.noetherianApproximationLimit`), and
> `X` is isomorphic to it, which is the step the source's proof ends with (Stacks 0262, as
> `AlgebraicGeometry.Space.exists_iso_of_isomorphic_presentations`).

```lean
theorem hasNoetherianApproximation_of_isomorphicPresentation_limit
    (hCLO : ∀ Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u, IsAlgebraicSpace B S hS Z →
      IsQuasiCompactSpace B S hS Z → IsAbsolutelyQuasiSeparated B S hS hZ Z →
        ∃ (I : Type u) (inst : Preorder I),
          let _ := inst
          ∃ (_ : Nonempty I) (_ : IsDirected I (· ≤ ·))
            (D : Iᵒᵖ ⥤ (BigFppfOver B S hS)ᵒᵖ ⥤ Type u),
            #I < B.cutoff.ord.cof ∧
            (∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof) ∧
            (∀ j, IsAlgebraicSpace B S hS (D.obj j)) ∧
            (∀ {j j' : Iᵒᵖ} (g : j ⟶ j'), IsAffineHom B S hS (D.map g)) ∧
            (∀ j, IsAbsolutelyQuasiSeparated B S hS hZ (D.obj j)) ∧
            (∀ j, IsFiniteType B (⊤_ Scheme.{u}) hZ
              (terminal.from (viewOverIntegers B S hS hZ (D.obj j)))) ∧
            ∃ (R R' U : BigFppfOver B S hS) (s t : R ⟶ U) (s' t' : R' ⟶ U)
              (a : yoneda.obj U ⟶ Z) (a' : yoneda.obj U ⟶ limit D) (e : R ≅ R'),
              IsPullback (yoneda.map s) (yoneda.map t) a a ∧
              IsPullback (yoneda.map s') (yoneda.map t') a' a' ∧
              e.hom ≫ s' = s ∧ e.hom ≫ t' = t ∧
              (MorphismProperty.presheaf (MorphismProperty.inverseImage
                (@Surjective.{u} : MorphismProperty Scheme.{u})
                (BigFppfOver.toScheme B S hS))) a ∧
              (MorphismProperty.presheaf (MorphismProperty.inverseImage
                (@Etale.{u} : MorphismProperty Scheme.{u})
                (BigFppfOver.toScheme B S hS))) a ∧
              (MorphismProperty.presheaf (MorphismProperty.inverseImage
                (@Surjective.{u} : MorphismProperty Scheme.{u})
                (BigFppfOver.toScheme B S hS))) a' ∧
              (MorphismProperty.presheaf (MorphismProperty.inverseImage
                (@Etale.{u} : MorphismProperty Scheme.{u})
                (BigFppfOver.toScheme B S hS))) a')
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hqc : IsQuasiCompactSpace B S hS X)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X) :
    HasNoetherianApproximation B S hS hZ X
```

## Tag 07SV, an equation

[Tag 07SV](https://stacks.math.columbia.edu/tag/07SV) in the Stacks Project.

**`AlgebraicGeometry.isPullback_gluedRelationSource_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GluedEtaleRelationTransition.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GluedEtaleRelationTransition.lean#L303). The attribute's comment: “the displayed square is cartesian, for any base-changed fibre square over W”.

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

**`AlgebraicGeometry.isPullback_gluedRelationSource`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GluedEtaleRelationTransition.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GluedEtaleRelationTransition.lean#L378). The attribute's comment: “the displayed square for R_i glued from V_i and W_i x_{U_i} W_i is cartesian”.

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: Stacks.Duality.isDerivedSheafHomRightAdjoint_of_fts_closedImmersion, Stacks.Duality.LocallySmall.upperShriek_closedImmersion_of_fts, Stacks.Divisors.isDualizingModule_homologyOne_derivedSheafHomExactSupport, Stacks.Duality.isNormalTensorPullbackRightAdjoint_of_fts, Stacks.Duality.upperShriek_isRightAdjointOnBoundedBelow_of_isProper, Stacks.Duality.isDualizingComplex_upperShriek_of_fts
statement: formalized
proof: formalized
---

# 48.19 A duality theory

Section 48.19 of the Stacks Project, [Tag 0AU3](https://stacks.math.columbia.edu/tag/0AU3). 1 tag here is carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AU3, the section

[Tag 0AU3](https://stacks.math.columbia.edu/tag/0AU3) in the Stacks Project.

**`Stacks.Duality.isDerivedSheafHomRightAdjoint_of_fts_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImage.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImage.lean#L244). The attribute's comment: “clause (5) of Section 48.19: for a closed immersion f^! is derived sheaf Hom out of the structure sheaf, with the conclusion of Tag 0A9X discharged by Stacks.Duality.tag0A9XHypothesis; i^! is the explicit parameter a with its adjunction, the existence statement being Tag 0A9E”.

> **Stacks Project, Tag 0AA2 (Lemma 48.17.4), with nothing about Tag 0A9X assumed.** In
> Situation 48.16.1, let `i : X ⟶ Y` be a morphism of `FTS S` whose underlying morphism of schemes
> is a closed immersion, and let `a` be a right adjoint of
> `Ri_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)`. Then `a`, which is `i^!`, is derived sheaf Hom out of `𝒪_X`:
> `i^!(-) = R𝓗om_{𝒪_Y}(𝒪_X, -)` on bounded-below complexes with quasi-coherent cohomology.
>
> This is `Stacks.Duality.isDerivedSheafHomRightAdjoint_of_fts` with its hypothesis `h0A9X`
> discharged by `Stacks.Duality.tag0A9XHypothesis`, which is the content of [Stacks, Tag 0A9X]
> (`Stacks.Duality.tag0A9X`) read at the canonical restriction of `Ri_*` to the quasi-coherent
> derived categories. Two of the three things the tag's proof needs are therefore not hypotheses:
> the conclusion of [Stacks, Tag 0A9X], and the preservation of quasi-coherent cohomology by `Ri_*`
> (part (1) of [Stacks, Tag 08D5], a closed immersion being affine).
>
> What remains a parameter is `i^!` itself, the functor `a` together with the adjunction `adj`
> characterising it, exactly as in `Stacks.Duality.isDerivedSheafHomRightAdjoint_of_pseudoCoherent`
> ([Stacks, Tag 0A9X]) and in `Stacks.Duality.sheafyTrace`. Its existence is [Stacks, Tag 0A9E],
> which is not proved unconditionally in this tree —
> `Stacks.Duality.DerivedPushforward.isLeftAdjoint_qcqsRestrictedDerivedPushforward` carries
> [Stacks, Tag 08DZ] at the locally small model and [Stacks, Tag 09IS]; a right adjoint being
> unique up to canonical isomorphism, the
> statement about an arbitrary one says the same thing as the statement about the one that tag
> produces.
>
> This declaration is not registered as [Stacks, Tag 0AA2]: the full statement, with `i^!`
> produced for every object of `FTS S` and no affineness or quasi-affineness hypothesis, is
> `Stacks.Duality.LocallySmall.upperShriek_closedImmersion_of_fts` in
> `StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImageQcqs.lean`.

```lean
theorem isDerivedSheafHomRightAdjoint_of_fts_closedImmersion
    {S : Scheme.{u}} [IsNoetherian S] {X Y : FTS S} (i : X ⟶ Y)
    [IsClosedImmersion i.left]
    (a : quasiCoherentDerivedCategory Y.left ⥤ quasiCoherentDerivedCategory X.left)
    (adj : affineHomQuasiCoherentDerivedPushforward i.left ⊣ a) :
    IsDerivedSheafHomRightAdjoint i.left a
```

**`Stacks.Duality.LocallySmall.upperShriek_closedImmersion_of_fts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImageQcqs.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/ClosedImmersionTwistedInverseImageQcqs.lean#L160). The attribute's comment: “clause (5): for a closed immersion f^! = RHom(O\_X, -), at the locally small derived categories”.

> **Stacks Project, Tag 0AA2 (Lemma 48.17.4).** In Situation 48.16.1 — `S` a Noetherian scheme
> and `FTS S` the schemes separated and of finite type over `S` — let `i : X ⟶ Y` be a morphism of
> `FTS S` whose underlying morphism of schemes is a closed immersion. Then
> `i^!(-) = R𝓗om(𝒪_X, -)`:
>
> 1. `Ri_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` has a right adjoint;
> 2. the upper shriek `i^! = j^* ∘ a` of [Stacks, Tag 0A9Y] at the compactification `X̄ = X` that a
>    proper morphism is (`Stacks.Duality.properCompactification`), with its right adjoint `a`
>    *produced* by (1) and its quasi-coherence inputs discharged, agrees with `R𝓗om(𝒪_X, -)` on
>    `D⁺_QCoh(𝒪_Y)`;
> 3. for every right adjoint `a` of `Ri_*` the canonical comparison `a(K) ⟶ R𝓗om(𝒪_X, K)` — the
>    mate of the counit of `a` under [Stacks, Tag 0A76] — is an isomorphism for every `K` in
>    `D⁺_QCoh(𝒪_Y)`.
>
> The existence (1) is
> `Stacks.Duality.LocallySmall.isLeftAdjoint_affineHomQuasiCoherentDerivedPushforward`, which builds
> the right adjoint as `DQ_X ∘ R𝓗om(𝒪_X, -)` from the coherator of [Stacks, Tag 0CR0]; `X` is
> quasi-compact and quasi-separated, being of finite type over a Noetherian scheme. The
> identification (2), (3) is [Stacks, Tag 0A9X] at this model
> (`Stacks.Duality.LocallySmall.isIso_rightAdjointToDerivedSheafHom_app`), whose hypotheses —
> pseudo-coherence of `i` — hold in Situation 48.16.1.

```lean
theorem upperShriek_closedImmersion_of_fts {S : Scheme.{u}} [IsNoetherian S] {X Y : FTS S}
    (i : X ⟶ Y) [IsClosedImmersion i.left] :
    (affineHomQuasiCoherentDerivedPushforward i.left).IsLeftAdjoint ∧
      IsDerivedSheafHomRightAdjoint i.left
        (upperShriek i (properCompactification i)) ∧
      ∀ (a : quasiCoherentDerivedCategory Y.left ⥤ quasiCoherentDerivedCategory X.left)
        (adj : affineHomQuasiCoherentDerivedPushforward i.left ⊣ a)
        (K : (isBoundedBelowQuasiCoherent Y.left).FullSubcategory),
        IsIso ((rightAdjointToDerivedSheafHom i.left
          (isQuasicoherent_homology_derivedPushforward_of_isAffineHom i.left) a adj).app
            K.obj)
```

**`Stacks.Divisors.isDualizingModule_homologyOne_derivedSheafHomExactSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDualizingModule.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/EffectiveCartierDualizingModule.lean#L118). The attribute's comment: “clauses (4)(a) and (7) for the inclusion i : D to X of an effective Cartier divisor into a locally Noetherian scheme, read on a module: clause (7) identifies i^! with Li^*(-) tensor N[-1], so for a module omega the degree-one cohomology of i^!omega is N tensor i^*omega, which is H^1(a(omega)) for a the right adjoint of Tag 0A76; clause (4)(a) is that this is dualizing on D. Nothing is carried: the reduction to affine charts of D lying over affine opens of X on which the ideal of D is principal on a nonzerodivisor is Tag 0A86, the chart-level input is Tag 0AX0 at the surjection Gamma(X,U) to Gamma(D, i^-1 U) whose kernel that nonzerodivisor generates, and the identification of H^1(a(omega)) with the twist is Tag 0AA4 at the level of modules. The general finite-type case of clause (4)(a) is Stacks.Duality.isDualizingComplex\_upperShriek\_of\_fts, stated for an unconstructed f^!”.

> **[Stacks, Tag 0AA3] for the inclusion of an effective Cartier divisor, read on a module.**
> Let `D ⊆ X` be an effective Cartier divisor on a locally Noetherian scheme, with closed immersion
> `i : D ⟶ X`, and let `a(-)` be the right adjoint of derived pushforward along `i` of
> [Stacks, Tag 0A76]. If a quasi-coherent `𝒪_X`-module `ω` placed in some degree is a dualizing
> complex on `X`, then the `𝒪_D`-module `H¹(a(ω))` is a dualizing module on `D`.
>
> Degree one is the degree [Stacks, Remark 0B4R] selects, and
> `Stacks.Divisors.nonempty_homologyOne_derivedSheafHomExactSupport_iso` identifies `H¹(a(ω))` with
> the normal sheaf twist `𝒩 ⊗ i^*ω` of the restriction.

```lean
theorem isDualizingModule_homologyOne_derivedSheafHomExactSupport (ω : X.Modules)
    [ω.IsQuasicoherent] (n : ℤ) (hω : Stacks.Duality.IsDualizingComplex
      ((DerivedCategory.singleFunctor X.Modules n).obj ω)) :
    letI : IsLocallyNoetherian D.subscheme := D.isLocallyNoetherian_subscheme
    Stacks.Duality.IsDualizingModule
      ((DerivedCategory.homologyFunctor D.subscheme.Modules 1).obj
        ((closedQuotient D).derivedSheafHomExactSupport.obj
          ((DerivedCategory.singleFunctor X.Modules 0).obj ω)))
```

**`Stacks.Duality.isNormalTensorPullbackRightAdjoint_of_fts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryDivisor.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryDivisor.lean#L174). The attribute's comment: “clause (7) of Section 48.19: for the inclusion of an effective Cartier divisor into an object of FTS S, f^! is derived pullback tensored with the shifted normal sheaf i^*O\_Y(D)[-1]. Both inputs are proved unconditionally: clause (5) of the same section (Tag 0AA2) as Stacks.Duality.isDerivedSheafHomRightAdjoint\_of\_fts\_closedImmersion, and Tag 0AA4 as Stacks.Divisors.normalTensorDerivedSheafHomIso. As in clause (5), i^! is the explicit parameter a with its adjunction, the existence statement being Tag 0A9E”.

> **Stacks Project, Section 0AU3, clause (7).** Let `S` be a Noetherian scheme, let `Y` be an
> object of `AlgebraicGeometry.FTS S` — a scheme separated and of finite type over `S` — and let
> `D ⊆ Y` be an effective Cartier divisor, with closed immersion `i : D ⟶ Y` and normal sheaf
> `𝒩 = i^*𝒪_Y(D)`. Let `a` be a right adjoint of `Ri_* : D_QCoh(𝒪_D) ⥤ D_QCoh(𝒪_Y)`. Then `a`,
> which is `i^!`, is `Li^*(-) ⊗^L_{𝒪_D} 𝒩[-1]` on bounded-below complexes with quasi-coherent
> cohomology:
>
> `i^!(-) = Li^*(-) ⊗_{𝒪_D} i^*𝒪_Y(D)[-1]`.
>
> The proof is the section's own: clause (5) of the section, which is [Stacks, Tag 0AA2] and is
> formalized as `Stacks.Duality.isDerivedSheafHomRightAdjoint_of_fts_closedImmersion`, identifies
> `i^!` with `R𝓗om_{𝒪_Y}(𝒪_D, -)`; and [Stacks, Tag 0AA4],
> `Stacks.Divisors.normalTensorDerivedSheafHomIso`, identifies that with
> `Li^*(-) ⊗^L_{𝒪_D} 𝒩[-1]`.

```lean
theorem isNormalTensorPullbackRightAdjoint_of_fts
    (a : quasiCoherentDerivedCategory Y.left ⥤ quasiCoherentDerivedCategory D.subscheme)
    (adj : affineHomQuasiCoherentDerivedPushforward D.subschemeι ⊣ a) :
    IsNormalTensorPullbackRightAdjoint D a
```

**`Stacks.Duality.upperShriek_isRightAdjointOnBoundedBelow_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryProper.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/TwistedInverseImage/DualityTheoryProper.lean#L117). The attribute's comment: “clause (2), first assertion: for a proper morphism f^! is a right adjoint of Rf\_* and carries the bounded-below part of D\_QCoh into the bounded-below part, so it is the restriction of that right adjoint to D^+\_QCoh. The f^! is Stacks.Duality.upperShriek at the identity compactification, which is the one the source uses for a proper morphism; independence of the compactification is Tag 0AA0, which in this repository still carries the Tag 0A9L invertibility of Tag 0A9P. The SECOND assertion of clause (2), the duality isomorphism Rf\_* RHom(K, f^! M) = RHom(Rf\_* K, M), is not claimed: its map is Stacks.Duality.sheafyTrace and its invertibility is Tag 0GEW, which is open here”.

> **Stacks Project, Section 0AU3, clause (2), first assertion.** Let `S` be a quasi-compact
> quasi-separated scheme (in the source, a Noetherian one) and let `f : X ⟶ Y` be a morphism of
> `AlgebraicGeometry.FTS S`, the schemes separated and of finite type over `S`, whose underlying
> morphism of schemes is proper. Then `f^!` is the restriction of the right adjoint of
> `Rf_* : D_QCoh(𝒪_X) ⥤ D_QCoh(𝒪_Y)` to `D⁺_QCoh(𝒪_Y)`: the upper shriek functor of
> [Stacks, Tag 0A9Y] is a right adjoint of `Rf_*`, and it carries `D⁺_QCoh(𝒪_Y)` into
> `D⁺_QCoh(𝒪_X)`.
>
> Both conjuncts are needed for the clause: the first says `f^!` *is* the right adjoint, the second
> says the restriction of that right adjoint to the bounded-below parts is defined.

```lean
theorem upperShriek_isRightAdjointOnBoundedBelow_of_isProper :
    Nonempty (DerivedPushforward.qcqsRestrictedDerivedPushforward f.left ⊣
        upperShriek f (properCompactification f)) ∧
      ∀ K : quasiCoherentDerivedCategory Y.left, DerivedCategoryB.IsBoundedBelow K.obj →
        DerivedCategoryB.IsBoundedBelow
          ((upperShriek f (properCompactification f)).obj K).obj
```

**`Stacks.Duality.isDualizingComplex_upperShriek_of_fts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDualizingComplex.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekDualizingComplex.lean#L148). The attribute's comment: “clause (4)(a) of Section 48.19: the normalized complex f^! of a dualizing complex is dualizing, under the same carried hypotheses as the Tag 0AA3 key below”.

> **Stacks Project, Tag 0AA3 (Lemma 48.17.7).** In Situation 48.16.1, let `f : X ⟶ Y` be a
> morphism of `FTS S` and let `f^!` be an exceptional inverse image functor
> `D⁺_QCoh(𝒪_Y) ⥤ D⁺_QCoh(𝒪_X)` for it, in the sense that on affine charts it is the algebraic
> upper shriek of a polynomial presentation of the chart ring map. If `K` is a dualizing complex
> for `Y`, then `f^!K` is a dualizing complex for `X`.

```lean
theorem isDualizingComplex_upperShriek_of_fts {S : Scheme.{u}} [IsNoetherian S] {X Y : FTS S}
    (f : X ⟶ Y)
    (fShriek : quasiCoherentDerivedCategoryPlus Y.left ⥤ quasiCoherentDerivedCategoryPlus X.left)
    (K : quasiCoherentDerivedCategoryPlus Y.left)
    (h0A86 : ∀ L : DerivedCategory X.left.Modules,
      (∀ x : X.left, ∃ (U : X.left.Opens) (hU : IsAffineOpen U),
        x ∈ U ∧ HasDualizingModelOn L U hU) → IsDualizingComplex L)
    (h0AA1 : ∀ (U : X.left.Opens) (hU : IsAffineOpen U) (V : Y.left.Opens)
      (hV : IsAffineOpen V) (hUV : U ≤ f.left ⁻¹ᵁ V)
      (ω : DerivedCategory (ModuleCat.{u} Γ(Y.left, V))),
      IsTildeModelOn K.obj.obj V hV ω →
      ∃ p : Dualizing.PolynomialPresentation (f.left.appLE V U hUV).hom,
        IsTildeModelOn (fShriek.obj K).obj.obj U hU (p.upperShriekFunctor.{u, u}.obj ω))
    (hK : IsDualizingComplex K.obj.obj) :
    IsDualizingComplex (fShriek.obj K).obj.obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.19, Tag 0AU3](https://stacks.math.columbia.edu/tag/0AU3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

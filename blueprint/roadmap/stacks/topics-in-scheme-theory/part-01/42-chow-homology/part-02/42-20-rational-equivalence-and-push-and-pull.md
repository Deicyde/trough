---
declaration: section
origin: cited
lean: Stacks.Chow.flatPullback_principalDivisor_eq_sum_components, Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence_of_isOpenImmersion, Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence_general, Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence_of_opensι, Stacks.Chow.isRationallyEquivalentToZero_of_coe_eq_flatPullback_principalDivisorCycle, Stacks.Chow.properPushforwardFactorsThroughRationalEquivalence_of_isProper, Stacks.Chow.properPushforward_rationallyEquivalent_of_isProper
statement: formalized
proof: formalized
---

# 42.20 Rational equivalence and push and pull

Section 42.20 of the Stacks Project, [Tag 02S0](https://stacks.math.columbia.edu/tag/02S0). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EPH, a lemma

[Tag 0EPH](https://stacks.math.columbia.edu/tag/0EPH) in the Stacks Project.

**`Stacks.Chow.flatPullback_principalDivisor_eq_sum_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackPrincipalDivisor.lean, line 1030](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackPrincipalDivisor.lean#L1030).

> **Stacks 0EPH.** Let `C = (S, δ)` be the base situation of chapter 42, let `X` and `Y` be
> locally of finite type over `S` with `Y` integral of delta-dimension `k`, and let `f : X ⟶ Y` be
> flat of relative dimension `r`. For a nonzero rational function `g` on `Y`,
>
>   `f^* div_Y(g) = ∑_j n_j i_{j,*} div_{X_j}(g ∘ f|_{X_j})`
>
> as `(k + r - 1)`-cycles on `X`, where the sum is over the irreducible components `X_j` of `X`
> with their reduced structure and `n_j` is the multiplicity of `X_j` in the fundamental cycle
> `[X]_{k + r}`. The identity is read coefficientwise at a point `x` of `X`.

```lean
theorem flatPullback_principalDivisor_eq_sum_components (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] [IsIntegral Y] (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f]
    (hbase : f ≫ sY = sX) (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r) {k : ℤ}
    (hY : schemeDeltaDimension C sY = (k : EInt)) (g : Y.functionField) (hg : g ≠ 0) (x : X) :
    (flatPullback C sX sY f hbase r hf (k - 1) (principalDivisorCycle C sY hY g)).1 x =
      ∑ᶠ W : irreducibleComponents X,
        (cycleAssociatedToClosedSubscheme C sX (𝟙 X) (k + (r : ℤ))).1 W.2.1.genericPoint *
          (letI : IsIntegral (integralComponentAt W.2.1.genericPoint).subscheme :=
             isIntegral_integralComponentAt _
           letI := isDominant_subschemeι_integralComponentAt_comp f W
           (properPushforward C ((integralComponentAt W.2.1.genericPoint).subschemeι ≫ sX) sX
             (integralComponentAt W.2.1.genericPoint).subschemeι rfl (k + (r : ℤ) - 1)
             (principalDivisorCycle C _
               (schemeDeltaDimension_integralComponentAt_comp C sX sY f hbase r hf hY W)
               (dominantFunctionFieldMap
                 ((integralComponentAt W.2.1.genericPoint).subschemeι ≫ f) g))).1 x)
```

## Tag 02S1, a lemma

[Tag 02S1](https://stacks.math.columbia.edu/tag/02S1) in the Stacks Project.

**`Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ClopenDecomposition/OpenImmersionPieces.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ClopenDecomposition/OpenImmersionPieces.lean#L163). The attribute's comment: “flat pullback along an arbitrary open immersion preserves rational equivalence”.

> **Stacks 02S1 along an arbitrary open immersion.** Flat pullback along an open immersion over
> the base carries cycles rationally equivalent to zero to cycles rationally equivalent to zero.
>
> Flat pullback along an open immersion in relative dimension zero is restriction of cycles, by
> `Stacks.Chow.cycleGroupRestrict_eq_flatPullback`, up to a transport of the degree from `k + 0` to
> `k`; the statement for restriction is
> `Stacks.Chow.cycleGroupRestrict_mem_rationalEquivalences`.

```lean
theorem flatPullbackFactorsThroughRationalEquivalence_of_isOpenImmersion :
    FlatPullbackFactorsThroughRationalEquivalence C sU sX j hj 0
      (relativeDimension_of_isOpenImmersion j) k
```

**`Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/GeneralRationalEquivalence.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/GeneralRationalEquivalence.lean#L159). The attribute's comment: “the general case: an arbitrary flat morphism of relative dimension r”.

> **Stacks 02S1.** Flat pullback of `k`-cycles along a morphism `f : X' ⟶ X` of schemes locally
> of finite type over the base which is flat and locally of finite type of relative dimension `r`
> carries cycles rationally equivalent to zero to cycles rationally equivalent to zero.
>
> A presentation `∑_j (i_j)_* div_{W_j}(g_j)` of a rational equivalence on `X` by a locally finite
> family of integral closed subschemes `W_j ⊆ X` of delta-dimension `k + 1` is pulled back term by
> term. The closed-immersion case of Stacks 02RG rewrites the pullback of each term as a pushforward
> from the scheme-theoretic inverse image `f^{-1}(W_j)` of a cycle on `f^{-1}(W_j)`, which is
> rationally equivalent to zero there by the case of Stacks 02S1 for a principal divisor on an
> integral target. Those inverse images have as supports the preimages of the supports of the `W_j`,
> so they form a locally finite family by Stacks 02R9, and Stacks 02RZ sums the pushforwards into a
> single rational equivalence.

```lean
theorem flatPullbackFactorsThroughRationalEquivalence_general (C : ChowSituation.{u})
    {X' X : Scheme.{u}} (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (f : X' ⟶ X) [LocallyOfFiniteType f] [Flat f]
    (hbase : f ≫ sX = sX') (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r) (k : ℤ) :
    FlatPullbackFactorsThroughRationalEquivalence C sX' sX f hbase r hf k
```

**`Stacks.Chow.flatPullbackFactorsThroughRationalEquivalence_of_opensι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/OpenImmersionRationalEquivalence.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/OpenImmersionRationalEquivalence.lean#L195). The attribute's comment: “flat pullback along an open immersion preserves rational equivalence”.

> **Stacks 02S1 along the inclusion of an open subscheme.** Flat pullback of `k`-cycles along
> the inclusion of an open subscheme `V ⊆ X` carries cycles rationally equivalent to zero to cycles
> rationally equivalent to zero.
>
> A presentation `∑_j (i_j)_* div(g_j)` of a rational equivalence on `X`, by a locally finite family
> of integral closed subschemes `W_j` of delta-dimension `k + 1`, restricts to the presentation by
> the inverse images `W_j ×_X V` of those members whose generic point lies in `V`, carrying the
> restrictions of the `g_j`. The members whose generic point misses `V` are supported off `V` and
> contribute nothing there; the surviving inverse images are integral by
> `Stacks.Chow.comap_integralComponentAt_of_isOpenImmersion`, keep their delta-dimension by
> `Stacks.Chow.schemeDeltaDimension_eq_of_isOpenImmersion`, form a locally finite family because
> their supports are preimages, and their terms have the right coefficients by
> `Stacks.Chow.principalDivisorPushforward_comap_opensι`.

```lean
theorem flatPullbackFactorsThroughRationalEquivalence_of_opensι (C : ChowSituation.{u})
    {X : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] (V : X.Opens) (k : ℤ) :
    FlatPullbackFactorsThroughRationalEquivalence C (V.ι ≫ f) f V.ι rfl 0
      (relativeDimension_opensι V) k
```

**`Stacks.Chow.isRationallyEquivalentToZero_of_coe_eq_flatPullback_principalDivisorCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackPrincipalDivisorEquivalence.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackPrincipalDivisorEquivalence.lean#L102). The attribute's comment: “the case of a principal divisor on an integral target”.

> **Stacks 02S1 for a principal divisor on an integral target.** Let `X` and `Y` be locally of
> finite type over the base of chapter 42 with `Y` integral of delta-dimension `k`, let
> `f : X ⟶ Y` be flat of relative dimension `r`, and let `g` be a nonzero rational function on `Y`.
> Then the flat pullback `f^* div_Y(g)` of the principal divisor of `g` is rationally equivalent to
> zero, as a `(k + r - 1)`-cycle on `X`.
>
> Stacks 0EPH writes that pullback as the locally finite sum `∑_j n_j (i_j)_* div_{X_j}(g)` over the
> irreducible components `X_j` of `X` taken with their reduced structure. Each `X_j` is integral of
> delta-dimension `k + r`, so `div_{X_j}(g)` is rationally equivalent to zero on `X_j` by Stacks
> 02RW, and the multiplicity `n_j` is absorbed by the subgroup. The components form a locally finite
> family by Stacks 0BE1, so Stacks 02RZ sums the pushforwards into a single rational equivalence
> on `X`.

```lean
theorem isRationallyEquivalentToZero_of_coe_eq_flatPullback_principalDivisorCycle
    (C : ChowSituation.{u}) {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] [IsIntegral Y] (f : X ⟶ Y)
    [LocallyOfFiniteType f] [Flat f] (hbase : f ≫ sY = sX) (r : ℕ)
    (hf : AlgebraicGeometry.RelativeDimension f r) {k j : ℤ}
    (hY : schemeDeltaDimension C sY = (k : EInt)) {g : Y.functionField} (hg : g ≠ 0)
    (hj : j = k + (r : ℤ) - 1) (α : CycleGroup C sX j)
    (hα : ∀ x : X, α.1 x =
      (flatPullback C sX sY f hbase r hf (k - 1) (principalDivisorCycle C sY hY g)).1 x) :
    IsRationallyEquivalentToZero C sX j α
```

## Tag 02S2, a lemma

[Tag 02S2](https://stacks.math.columbia.edu/tag/02S2) in the Stacks Project.

**`Stacks.Chow.properPushforwardFactorsThroughRationalEquivalence_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/GenericFibre.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/GenericFibre.lean#L337). The attribute's comment: “pushforward kills rational equivalence”.

> Proper pushforward of `k`-cycles along a proper morphism over the base carries cycles
> rationally equivalent to zero to cycles rationally equivalent to zero.

```lean
theorem properPushforwardFactorsThroughRationalEquivalence_of_isProper (k : ℤ) :
    ProperPushforwardFactorsThroughRationalEquivalence C sX sY p hp k
```

**`Stacks.Chow.properPushforward_rationallyEquivalent_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/RationalEquivalenceUnconditional.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ProperPushforwardPrincipal/RationalEquivalenceUnconditional.lean#L30).

> Proper pushforward preserves rational equivalence of cycles: if `α` and `β` are rationally
> equivalent `k`-cycles on `X` and `p : X ⟶ Y` is proper over the base, then `p_*α` and `p_*β` are
> rationally equivalent `k`-cycles on `Y`.

```lean
theorem properPushforward_rationallyEquivalent_of_isProper (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (p : X ⟶ Y) [IsProper p] (hp : p ≫ sY = sX) (k : ℤ)
    {α β : CycleGroup C sX k} (h : RationallyEquivalent C sX k α β) :
    RationallyEquivalent C sY k (properPushforward C sX sY p hp k α)
      (properPushforward C sX sY p hp k β)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.20, Tag 02S0](https://stacks.math.columbia.edu/tag/02S0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

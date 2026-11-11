---
declaration: section
origin: cited
lean: Stacks.Chow.flatPullback_meromorphicDivisor_eq_sum_components, Stacks.Chow.flatNaturality_firstChernIdentityCapRule, Stacks.Chow.flatPullback_firstChernCapOfInvertible_rationallyEquivalent, Stacks.Chow.properChowPushforward_firstChernClassCapOfInvertible_fundamentalCycle, Stacks.Chow.properPushforward_meromorphicDivisorCycleOfInvertible, Stacks.Chow.properNaturality_firstChernIdentityCapRule, Stacks.Chow.properChowPushforward_firstChernClassCapOfInvertible_of_isProper', Stacks.Chow.properChowPushforward_firstChernClassCapOfInvertible_of_isProper
statement: formalized
proof: formalized
---

# 42.26 Intersecting with an invertible sheaf and push and pull

Section 42.26 of the Stacks Project, [Tag 0AYA](https://stacks.math.columbia.edu/tag/0AYA). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EPJ, a lemma

[Tag 0EPJ](https://stacks.math.columbia.edu/tag/0EPJ) in the Stacks Project.

**`Stacks.Chow.flatPullback_meromorphicDivisor_eq_sum_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackMeromorphicSection.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackMeromorphicSection.lean#L186).

> **Stacks 0EPJ.** Let `C = (S, δ)` be the base situation of chapter 42, let `X` and `Y` be
> locally of finite type over `S` with `Y` integral of delta-dimension `n`, and let `f : X ⟶ Y` be
> flat of relative dimension `r`. For an invertible module `L` on `Y` and a *nonzero* meromorphic
> section `s` of `L`,
>
>   `f^* div_L(s) = ∑_i n_i i_{i,*} div_{f^*L|_{X_i}}(s_i)`
>
> as `(n + r - 1)`-cycles on `X`. The sum runs over the irreducible components `X_i` of `X` taken
> with their reduced structure — each of these has delta-dimension `n + r` by
> `Stacks.Chow.schemeDeltaDimension_integralComponentAt_comp`, so this is the sum over the
> components of delta-dimension `n + r` that the source writes — `i_i : X_i ⟶ X` is the inclusion,
> `s_i` is the pullback of `s` along `f|_{X_i}`, and `n_i` is the multiplicity of `X_i` in `X`,
> read as the coefficient of `X_i` in the fundamental cycle `[X]_{n + r}`.
>
> The identity is read coefficientwise at a point `x` of `X`, because the irreducible components
> of a locally Noetherian scheme need not form a finite set: neither side is a finite sum of
> cycles, and at a fixed point of `X` only finitely many components contribute.

```lean
theorem flatPullback_meromorphicDivisor_eq_sum_components (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] [IsIntegral Y] (f : X ⟶ Y) [LocallyOfFiniteType f] [Flat f]
    (hbase : f ≫ sY = sX) (r : ℕ) (hf : AlgebraicGeometry.RelativeDimension f r) {n : ℤ}
    (hY : schemeDeltaDimension C sY = (n : EInt)) (L : Y.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.2 L]
    (s : L.presheaf.stalk (genericPoint Y)) (hs : s ≠ 0) (x : X) :
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    (flatPullback C sX sY f hbase r hf (n - 1)
        (meromorphicDivisorCycleOfInvertible C sY hY L s).val).1 x =
      ∑ᶠ W : irreducibleComponents X,
        (cycleAssociatedToClosedSubscheme C sX (𝟙 X) (n + (r : ℤ))).1 W.2.1.genericPoint *
          (letI : IsIntegral (integralComponentAt W.2.1.genericPoint).subscheme :=
             isIntegral_integralComponentAt _
           letI : IsLocallyNoetherian (integralComponentAt W.2.1.genericPoint).subscheme :=
             LocallyOfFiniteType.isLocallyNoetherian
               ((integralComponentAt W.2.1.genericPoint).subschemeι ≫ sX)
           letI := isDominant_subschemeι_integralComponentAt_comp f W
           letI := isInvertible_presheaf_pullback L
             ((integralComponentAt W.2.1.genericPoint).subschemeι ≫ f)
           (properPushforward C ((integralComponentAt W.2.1.genericPoint).subschemeι ≫ sX) sX
             (integralComponentAt W.2.1.genericPoint).subschemeι rfl (n + (r : ℤ) - 1)
             (meromorphicDivisorCycleOfInvertible C
               ((integralComponentAt W.2.1.genericPoint).subschemeι ≫ sX)
               (schemeDeltaDimension_integralComponentAt_comp C sX sY f hbase r hf hY W)
               ((Scheme.Modules.pullback
                 ((integralComponentAt W.2.1.genericPoint).subschemeι ≫ f)).obj L)
               (genericStalkPullback
                 ((integralComponentAt W.2.1.genericPoint).subschemeι ≫ f) L s)).val).1 x)
```

## Tag 02SS, a lemma

[Tag 02SS](https://stacks.math.columbia.edu/tag/02SS) in the Stacks Project.

**`Stacks.Chow.flatNaturality_firstChernIdentityCapRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean#L275). The attribute's comment: “the flat-pullback identity read for the identity cap rule of the canonical first Chern class cap product on the test schemes of X, i.e. the predicate `IdentityCapRule.FlatNaturality` that the bivariant class of Stacks 0B77 takes as its second naturality hypothesis, with no hypothesis of its own”.

> **The flat-pullback identity on the test schemes.** For the canonical first Chern class cap
> product and test morphisms `g : T ⟶ X` and `h : T' ⟶ T` with `h` flat of relative dimension `r`,
>
>   `c₁((h ∘ g)^*ℒ) ∩ h^*α = h^*(c₁(g^*ℒ) ∩ α)`,
>
> the two sides sitting in the degrees `(k + r) - 1` and `(k - 1) + r`. This is
> `Stacks.Chow.IdentityCapRule.FlatNaturality` for `Stacks.Chow.firstChernIdentityCapRule` at the
> canonical cap product.

```lean
theorem flatNaturality_firstChernIdentityCapRule :
    IdentityCapRule.FlatNaturality C sX 1
      (firstChernIdentityCapRule C sX (canonicalFirstChernCapRule C) L)
```

**`Stacks.Chow.flatPullback_firstChernCapOfInvertible_rationallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InvertibleChernCapPullback.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/InvertibleChernCapPullback.lean#L52).

> Intersecting with the first Chern class of an invertible module commutes with flat pullback:
> for `f : X' ⟶ X` flat of relative dimension `r`, an invertible module `L` on `X` and a
> `(k+1)`-cycle `α` on `X`, the cycle representing `c₁(f^*L) ∩ f^*α` and the flat pullback of the
> cycle representing `c₁(L) ∩ α` are rationally equivalent on `X'`.

```lean
theorem flatPullback_firstChernCapOfInvertible_rationallyEquivalent (α : CycleGroup C p (k + 1)) :
    RationallyEquivalent C (f ≫ p) (k + (r : ℤ))
      ((firstChernCapRule C (f ≫ p) (k + (r : ℤ))
          (firstChernComponentCycleRule C (f ≫ p) (k + (r : ℤ))
            ((Scheme.Modules.pullback f).obj L))).extendCycleGroup
        ((show k + 1 + (r : ℤ) = k + (r : ℤ) + 1 by omega) ▸
          flatPullback C (f ≫ p) p f rfl r hf (k + 1) α))
      (flatPullback C (f ≫ p) p f rfl r hf k
        ((firstChernCapRule C p k (firstChernComponentCycleRule C p k L)).extendCycleGroup α))
```

## Tag 02ST, a lemma

[Tag 02ST](https://stacks.math.columbia.edu/tag/02ST) in the Stacks Project.

**`Stacks.Chow.properChowPushforward_firstChernClassCapOfInvertible_fundamentalCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernClassDominantPushforward.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernClassDominantPushforward.lean#L257). The attribute's comment: “second displayed equation”.

> **The second displayed equation of Stacks 02ST.** Let `X` and `Y` be integral and locally of
> finite type over the base with `dim_δ(X) = dim_δ(Y) = n`, let `f : X ⟶ Y` be proper and dominant
> over the base and let `L` be an invertible `𝒪_Y`-module. Then
>
> `f_*(c₁(f^*L) ∩ [X]) = [R(X) : R(Y)] c₁(L) ∩ [Y] = c₁(L) ∩ f_*[X]`
>
> in `CH_{n-1}(Y)`, the two equalities being the two conjuncts below.
>
> The proper pushforward on Chow groups carries no hypothesis: Stacks 02S2 is
> `Stacks.Chow.properPushforwardFactorsThroughRationalEquivalence`. The invertibility of `f^*L` is
> Stacks 0B8L, the instance `Stacks.Divisors.pullback_isInvertible`.

```lean
theorem properChowPushforward_firstChernClassCapOfInvertible_fundamentalCycle
    (C : ChowSituation.{u}) {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] [IsIntegral X] [IsIntegral Y] {n : ℤ}
    (hnX : schemeDeltaDimension C sX = (n : EInt))
    (hnY : schemeDeltaDimension C sY = (n : EInt))
    (f : X ⟶ Y) [IsProper f] [IsDominant f] (hf : f ≫ sY = sX) (L : Y.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible Y.sheaf.obj Y.ringCatSheaf.property L] :
    letI : Algebra Y.functionField X.functionField := (dominantFunctionFieldMap f).toAlgebra
    properChowPushforward C sX sY f hf (n - 1)
          (properPushforwardFactorsThroughRationalEquivalence C sX sY f hf (n - 1))
          (firstChernClassCapOfInvertible C sX (n - 1) ((Scheme.Modules.pullback f).obj L)
            (cycleAssociatedToClosedSubscheme C sX (𝟙 X) (n - 1 + 1))) =
        (Module.finrank Y.functionField X.functionField : ℤ) •
          firstChernClassCapOfInvertible C sY (n - 1) L
            (cycleAssociatedToClosedSubscheme C sY (𝟙 Y) (n - 1 + 1)) ∧
      firstChernClassCapOfInvertible C sY (n - 1) L
          (properPushforward C sX sY f hf (n - 1 + 1)
            (cycleAssociatedToClosedSubscheme C sX (𝟙 X) (n - 1 + 1))) =
        (Module.finrank Y.functionField X.functionField : ℤ) •
          firstChernClassCapOfInvertible C sY (n - 1) L
            (cycleAssociatedToClosedSubscheme C sY (𝟙 Y) (n - 1 + 1))
```

**`Stacks.Chow.properPushforward_meromorphicDivisorCycleOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MeromorphicDivisorPushforward.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/MeromorphicDivisorPushforward.lean#L191). The attribute's comment: “first displayed equation”.

> **The first displayed equation of Stacks 02ST.** For a proper dominant morphism `p : X ⟶ Y`
> of integral schemes locally of finite type over the base with `dim_δ(X) = dim_δ(Y) = n`, an
> invertible `𝒪_Y`-module `L` and a nonzero meromorphic section `s` of `L`, the proper pushforward
> of the divisor cycle of `p^*s` is `[R(X) : R(Y)]` times the divisor cycle of `s`, as cycles.
>
> These are the hypotheses the source states the tag under; the rank-one hypothesis of
> `Stacks.Chow.properPushforward_meromorphicDivisorCycle` is discharged here by
> `Stacks.Divisors.isTrivializedNear_of_isInvertible`. The tag's second displayed equation, the
> first Chern class consequence, is in
> `StacksFrontier.AlgebraicGeometry.Chow.ChernClassDominantPushforward`, so the attribute names this
> clause explicitly; see the module documentation.

```lean
theorem properPushforward_meromorphicDivisorCycleOfInvertible (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] [IsIntegral X] [IsIntegral Y] [IsLocallyNoetherian X]
    [IsLocallyNoetherian Y] {n : ℤ}
    (hnX : schemeDeltaDimension C sX = (n : EInt))
    (hnY : schemeDeltaDimension C sY = (n : EInt))
    (p : X ⟶ Y) [IsProper p] [IsDominant p] (hp : p ≫ sY = sX) (L : Y.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible Y.presheaf Y.ringCatSheaf.2 L]
    (s : L.presheaf.stalk (genericPoint Y)) (hs : s ≠ 0) :
    letI : Algebra Y.functionField X.functionField := (dominantFunctionFieldMap p).toAlgebra
    properPushforward C sX sY p hp (n - 1)
        (meromorphicDivisorCycle C sX hnX
          (fun x => (isTrivializedNear_of_isInvertible L (p.base x)).pullback)
          (genericStalkPullback p L s)).val =
      (Module.finrank Y.functionField X.functionField : ℤ) •
        (meromorphicDivisorCycle C sY hnY (isTrivializedNear_of_isInvertible L) s).val
```

## Tag 02SU, a lemma

[Tag 02SU](https://stacks.math.columbia.edu/tag/02SU) in the Stacks Project.

**`Stacks.Chow.properNaturality_firstChernIdentityCapRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean#L194). The attribute's comment: “the projection formula read for the identity cap rule of the canonical first Chern class cap product on the test schemes of X, i.e. the predicate `IdentityCapRule.ProperNaturality` that the bivariant class of Stacks 0B77 takes as its first naturality hypothesis, with no hypothesis of its own”.

> **The projection formula on the test schemes.** For the canonical first Chern class cap product
> and test morphisms `g : T ⟶ X` and `h : T' ⟶ T` with `h` proper,
>
>   `c₁(g^*ℒ) ∩ h_*α = h_*(c₁((h ∘ g)^*ℒ) ∩ α)`.
>
> This is `Stacks.Chow.IdentityCapRule.ProperNaturality` for
> `Stacks.Chow.firstChernIdentityCapRule` at the canonical cap product.

```lean
theorem properNaturality_firstChernIdentityCapRule :
    IdentityCapRule.ProperNaturality C sX 1
      (firstChernIdentityCapRule C sX (canonicalFirstChernCapRule C) L)
```

**`Stacks.Chow.properChowPushforward_firstChernClassCapOfInvertible_of_isProper'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCapProperPushforward/Invertible.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCapProperPushforward/Invertible.lean#L268).

> **Stacks 02SU.** Let `p : X ⟶ Y` be a proper morphism of schemes locally of finite type over
> the base scheme of chapter 42 and let `ℒ` be an invertible `𝒪_Y`-module. Then for every
> `(k+1)`-cycle `α` on `X`
>
>   `p_*(c₁(p^*ℒ) ∩ α) = c₁(ℒ) ∩ p_*α`  in  `A_k(Y)`.

```lean
theorem properChowPushforward_firstChernClassCapOfInvertible_of_isProper'
    (α : CycleGroup C sX (k + 1)) :
    letI := isInvertible_presheaf_modulePullback L p
    properChowPushforward C sX sY p hp k
        (properPushforwardFactorsThroughRationalEquivalence C sX sY p hp k)
        (firstChernClassCapOfInvertible C sX k ((Scheme.Modules.pullback p).obj L) α) =
      firstChernClassCapOfInvertible C sY k L
        (properPushforward C sX sY p hp (k + 1) α)
```

**`Stacks.Chow.properChowPushforward_firstChernClassCapOfInvertible_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCapPushforward/Proper.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCapPushforward/Proper.lean#L471).

> **Stacks 02SU.** Let `p : X ⟶ Y` be a proper morphism of schemes locally of finite type over
> the base scheme of chapter 42, and let `ℒ` be an invertible `𝒪_Y`-module. Then for every
> `(k+1)`-cycle `α` on `X`
>
>   `p_*(c₁(p^*ℒ) ∩ α) = c₁(ℒ) ∩ p_*α`  in  `A_k(Y)`.
>
> The invertibility of `p^*ℒ` is Stacks 0B8L (`Stacks.Divisors.pullback_isInvertible`), and proper
> pushforward on Chow groups is defined by Stacks 02S2
> (`Stacks.Chow.properPushforwardFactorsThroughRationalEquivalence_of_isProper`).

```lean
theorem properChowPushforward_firstChernClassCapOfInvertible_of_isProper
    (α : CycleGroup C sX (k + 1)) :
    properChowPushforward C sX sY p hp k
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper C sX sY p hp k)
        (firstChernClassCapOfInvertible C sX k ((Scheme.Modules.pullback p).obj L) α) =
      firstChernClassCapOfInvertible C sY k L (properPushforward C sX sY p hp (k + 1) α)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.26, Tag 0AYA](https://stacks.math.columbia.edu/tag/0AYA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: Stacks.Chow.effectiveCartierIntersection_eq_firstChernClassCap_of_keyFormula, Stacks.Chow.gysinHomomorphismOfInvertible_eq_firstChernClassCapOfInvertible_of_keyFormula, Stacks.Chow.gysin_divisorOfMeromorphicSection_eq_firstChernClassCap, Stacks.Chow.gysinOfInvertibleDescends, Stacks.Chow.gysinOfInvertibleFactorsThroughRationalEquivalence_of_components, Stacks.Chow.gysinHomomorphismOnChowOfInvertibleOfComponents, Stacks.Chow.gysinOfInvertibleFactorsThroughRationalEquivalence, Stacks.Chow.gysinChowOfInvertible
statement: formalized
proof: formalized
---

# 42.30 Gysin homomorphisms and rational equivalence

Section 42.30 of the Stacks Project, [Tag 02TK](https://stacks.math.columbia.edu/tag/02TK). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02TM, a lemma

[Tag 02TM](https://stacks.math.columbia.edu/tag/02TM) in the Stacks Project.

**`Stacks.Chow.effectiveCartierIntersection_eq_firstChernClassCap_of_keyFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ChernCapDivisor.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ChernCapDivisor.lean#L151). The attribute's comment: “after pushforward along E ⟶ X, granting the key formula 0AYC”.

> **Stacks 02TM, pushed forward to the ambient scheme.** Let `X` be integral of
> delta-dimension `k + 2`, let `E` be an effective Cartier divisor on `X` and let `N` be an
> invertible module with a nonzero meromorphic section `t`. Then intersecting `div_N(t)` with `E`
> agrees with capping the fundamental cycle `[E]_{k+1}` with the first Chern class of `N`, in
> `A_k(X)`.
>
> This is the identity `i^* div_N(t) = c₁(N|_E) ∩ [E]_{k+1}` of the source after pushing forward
> along the closed immersion `i : E ⟶ X`, the right hand side being read on `X` through Stacks 02SU;
> see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.Gysin42.ChernCapDivisor`.
>
> Intersection with `E` is capping with `c₁(𝒪_X(E))` by Stacks 02T9, and the fundamental cycle
> `[E]_{k+1}` is the divisor cycle of the canonical section `1_E` of `𝒪_X(E)`, presented by the
> family `{Z_i}` of the key formula through `hfundamentalCycle`. So the identity is the
> commutativity of Stacks 02TH for the pair `(𝒪_X(E), N)`.

```lean
theorem effectiveCartierIntersection_eq_firstChernClassCap_of_keyFormula
    (hn : schemeDeltaDimension C p = ((k + 2 : ℤ) : EInt)) (E : X.IdealSheafData)
    [Stacks.Divisors.IsEffectiveCartierDivisor E] (D : KeyFormulaData X)
    (hKey : D.KeyFormula C p) (chernN : FirstChernComponentCycleRule C p k)
    (hchernE : ∀ (i : D.Index) (hW : IsIntegral (D.component i).subscheme)
      (hDim : schemeDeltaDimension C ((D.component i).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt)),
      (firstChernComponentCycleRule C p k (Stacks.Divisors.divisorSheaf E)
        (D.component i) hW hDim).1 = D.restrictedDivisorL i)
    (hchernN : ∀ (i : D.Index) (hW : IsIntegral (D.component i).subscheme)
      (hDim : schemeDeltaDimension C ((D.component i).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt)),
      (chernN (D.component i) hW hDim).1 = D.restrictedDivisorN i)
    (fundamentalCycle divN : CycleGroup C p (k + 1))
    (hfundamentalCycle : ∀ x : X, fundamentalCycle.1 x = ∑ᶠ i, D.orderL i *
      (cycleAssociatedToClosedSubscheme C p (D.component i).subschemeι (k + 1)).1 x)
    (hdivN : ∀ x : X, divN.1 x = ∑ᶠ i, D.orderN i *
      (cycleAssociatedToClosedSubscheme C p (D.component i).subschemeι (k + 1)).1 x) :
    effectiveCartierIntersectionOfInvertible C p k (Stacks.Divisors.divisorSheaf E)
        (Stacks.Divisors.divisorSheafGlobalSection E)
        (isEffectiveCartierDivisor_zeroScheme_divisorSheaf E) divN =
      firstChernClassCap C p k chernN fundamentalCycle
```

**`Stacks.Chow.gysinHomomorphismOfInvertible_eq_firstChernClassCapOfInvertible_of_keyFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ChernCapDivisor.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ChernCapDivisor.lean#L267). The attribute's comment: “the identity i^* div_N(t) = c₁(N|_D) ∩ [D]_{n-1} in A_{n-2}(D), the conclusion of the source, granting the rational equivalence `KeyFormulaRationalEquivalenceOnDivisor` that the key formula 0AYC exhibits on D — the last step of the source's proof — together with the divisor cycle div_N(t) of 02SJ and the fundamental cycle [D]_{n-1} read on D, each with its presentation by a locally finite family of integral closed subschemes of delta-dimension n-1, which is the second step of the source's proof”.

> **Stacks 02TM.** Let `X` be integral of delta-dimension `k + 2`, let `E` be an effective
> Cartier divisor on `X` with closed immersion `i : E ⟶ X`, and let `N` be an invertible module on
> `X` with a nonzero meromorphic section `t`. Then
>
> `i^* div_N(t) = c₁(N|_E) ∩ [E]_{k+1}`  in  `A_k(E)`,
>
> the identity of the source: the left hand side is the Gysin pullback of Stacks 02T8 along `i`,
> which takes its values in the Chow group of `E`, and the right hand side is the cap product of
> Stacks 02SO on `E` with the first Chern class of the restriction `N|_E`, applied to the
> fundamental cycle of `E` read as a cycle on `E`.
>
> The divisor cycle `div_N(t)` of Stacks 02SJ and the fundamental cycle `[E]_{k+1}` are explicit
> parameters, each with the presentation the second step of the source's proof gives it: the first
> by the family `{Z_i}` of prime divisors of the key formula data `D`, with the orders
> `ord_{B_i}(g_i)`, and the second by a locally finite family `{V_j}` of integral closed subschemes
> of `E` of delta-dimension `k + 1`, with multiplicities `m_j`. The remaining input is the rational
> equivalence `Stacks.Chow.KeyFormulaRationalEquivalenceOnDivisor` on `E`, which is the last step
> of the source's proof; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.Gysin42.ChernCapDivisor`.
>
> Given these, the two sides are computed on their presentations by the locally finite component
> formulas of Stacks 02T8 and 02SO, and the rational equivalence identifies the resulting two
> classes.

```lean
theorem gysinHomomorphismOfInvertible_eq_firstChernClassCapOfInvertible_of_keyFormula
    (hn : schemeDeltaDimension C p = ((k + 2 : ℤ) : EInt)) (E : X.IdealSheafData)
    [Stacks.Divisors.IsEffectiveCartierDivisor E] (N : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property N]
    (D : KeyFormulaData X) {J : Type u}
    (V : J → (Stacks.Divisors.zeroScheme X (Stacks.Divisors.divisorSheaf E)
      (Stacks.Divisors.divisorSheafGlobalSection E)).subscheme.IdealSheafData)
    (hV : ∀ j, IsIntegral (V j).subscheme)
    (hVdim : ∀ j, schemeDeltaDimension C ((V j).subschemeι ≫
        (Stacks.Divisors.zeroScheme X (Stacks.Divisors.divisorSheaf E)
          (Stacks.Divisors.divisorSheafGlobalSection E)).subschemeι ≫ p) =
      ((k + 1 : ℤ) : EInt))
    (hVlocal : LocallyFinite fun j ↦ ((V j).support :
      Set (Stacks.Divisors.zeroScheme X (Stacks.Divisors.divisorSheaf E)
        (Stacks.Divisors.divisorSheafGlobalSection E)).subscheme))
    (m : J → ℤ)
    (hKeyOnDivisor : KeyFormulaRationalEquivalenceOnDivisor C p hn E N D V hV hVdim m)
    (divN : CycleGroup C p (k + 1))
    (hdivN : ∀ x : X, divN.1 x = ∑ᶠ i, D.orderN i *
      (cycleAssociatedToClosedSubscheme C p (D.component i).subschemeι (k + 1)).1 x)
    (fundamentalCycle : CycleGroup C ((Stacks.Divisors.zeroScheme X
      (Stacks.Divisors.divisorSheaf E)
      (Stacks.Divisors.divisorSheafGlobalSection E)).subschemeι ≫ p) (k + 1))
    (hfundamentalCycle : ∀ z : (Stacks.Divisors.zeroScheme X
      (Stacks.Divisors.divisorSheaf E)
      (Stacks.Divisors.divisorSheafGlobalSection E)).subscheme,
      fundamentalCycle.1 z = ∑ᶠ j, m j *
        (cycleAssociatedToClosedSubscheme C ((Stacks.Divisors.zeroScheme X
            (Stacks.Divisors.divisorSheaf E)
            (Stacks.Divisors.divisorSheafGlobalSection E)).subschemeι ≫ p)
          (V j).subschemeι (k + 1)).1 z) :
    gysinHomomorphismOfInvertible C p k (Stacks.Divisors.divisorSheaf E)
        (Stacks.Divisors.divisorSheafGlobalSection E) divN =
      firstChernClassCapOfInvertible C ((Stacks.Divisors.zeroScheme X
          (Stacks.Divisors.divisorSheaf E)
          (Stacks.Divisors.divisorSheafGlobalSection E)).subschemeι ≫ p) k
        ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X
          (Stacks.Divisors.divisorSheaf E)
          (Stacks.Divisors.divisorSheafGlobalSection E)).subschemeι).obj N)
        fundamentalCycle
```

**`Stacks.Chow.gysin_divisorOfMeromorphicSection_eq_firstChernClassCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/DivisorChernComparison.lean, line 496](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/DivisorChernComparison.lean#L496).

> **Stacks 02TM.** Let `X` be integral and locally of finite type over the base scheme `S` of
> chapter 42, with `n = dim_δ(X)`, let `i : D ⟶ X` be an effective Cartier divisor, and let `N` be
> an invertible `𝒪_X`-module with a nonzero (that is, regular) meromorphic section `t`. Then
>
>   `i^* div_N(t) = c₁(N|_D) ∩ [D]_{n-1}`  in  `CH_{n-2}(D)`.
>
> Here `i^*` is the Gysin homomorphism of Stacks 02T8 for the pair `(𝒪_X(D), 1_D)`, whose zero
> scheme is `D` (`Stacks.Divisors.zeroScheme_canonicalSection`), so it takes values in the Chow
> group of `D`; `div_N(t)` is the divisor cycle of Stacks 02SJ (1); `N|_D` is the pullback of `N`
> along `i`; and `[D]_{n-1}` is the fundamental cycle of `D`, the cycle of `D` as a closed
> subscheme of itself. Cycles of degree `n - 1` are read in degree `(n - 2) + 1`, the source of
> `i^*` and of the cap product into degree `n - 2`, by `Stacks.Chow.cycleGroupOfEq`.

```lean
theorem gysin_divisorOfMeromorphicSection_eq_firstChernClassCap (n : ℤ)
    (hn : schemeDeltaDimension C p = (n : EInt)) (E : X.IdealSheafData)
    [IsEffectiveCartierDivisor E] (N : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property N]
    (t : AlgebraicGeometry.MeromorphicSection X.sheaf N)
    (ht : AlgebraicGeometry.IsRegularMeromorphicSection X.sheaf N t) :
    gysinHomomorphismOfInvertible C p (n - 2) (divisorSheaf E) (divisorSheafGlobalSection E)
        (cycleGroupOfEq (by ring) (divisorOfMeromorphicSectionCycle C p n hn N t ht)) =
      firstChernClassCapOfInvertible C
        ((Stacks.Divisors.zeroScheme X (divisorSheaf E)
          (divisorSheafGlobalSection E)).subschemeι ≫ p) (n - 2)
        ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X (divisorSheaf E)
          (divisorSheafGlobalSection E)).subschemeι).obj N)
        (cycleGroupOfEq (by ring) (fundamentalCycle C
          ((Stacks.Divisors.zeroScheme X (divisorSheaf E)
            (divisorSheafGlobalSection E)).subschemeι ≫ p) (n - 1)))
```

## Tag 02TO, a lemma

[Tag 02TO](https://stacks.math.columbia.edu/tag/02TO) in the Stacks Project.

**`Stacks.Chow.gysinOfInvertibleDescends`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinSystemOfInvertible.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/GysinSystemOfInvertible.lean#L66). The attribute's comment: “the vanishing for every test datum at once, with no hypothesis: the bundled form of `gysinOfInvertibleFactorsThroughRationalEquivalence`”.

> For every scheme locally of finite type over the base, every invertible module on it, every
> global section of that module and every degree, the Gysin map of the zero scheme of the section
> kills the cycles rationally equivalent to zero.

```lean
theorem gysinOfInvertibleDescends (C : ChowSituation.{u}) : GysinOfInvertibleDescends C
```

**`Stacks.Chow.gysinOfInvertibleFactorsThroughRationalEquivalence_of_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinRationalEquivalenceReduction.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinRationalEquivalenceReduction.lean#L208). The attribute's comment: “the Gysin map factors through rational equivalence, granted the single-component case the source's proof reduces to — the Gysin map kills the pushforward of div_V(f) for one integral V and one rational function f, which the source settles with Stacks 02TM, 02TI and 02SP. The reduction to that case, which the source performs with Stacks 02TA and 02S2, is proved”.

> **Stacks 02TO from its single-component case.** If the Gysin map of the zero scheme of `s`
> kills the pushforward of the principal divisor of a rational function on each single integral
> closed subscheme of delta-dimension `k + 2`, with witnesses over that subscheme, then it kills
> every `(k+1)`-cycle rationally equivalent to zero — which is the vanishing of Stacks 02TO, and
> therefore, by `Stacks.Chow.gysinHomomorphismOnChowOfInvertibleOfComponents`, the descended map
> `i^* : A_{k+1}(X) ⟶ A_k(D)`.

```lean
theorem gysinOfInvertibleFactorsThroughRationalEquivalence_of_components
    (h : GysinOfInvertibleKillsPrincipalDivisorOnComponent C p k L s) :
    GysinOfInvertibleFactorsThroughRationalEquivalence C p k L s
```

**`Stacks.Chow.gysinHomomorphismOnChowOfInvertibleOfComponents`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinRationalEquivalenceReduction.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinRationalEquivalenceReduction.lean#L228). The attribute's comment: “the descended map i^* : A_{k+1}(X) ⟶ A_k(D), granted the single-component case the source's proof reduces to, as in `gysinOfInvertibleFactorsThroughRationalEquivalence_of_components`”.

> **Stacks 02TO.** The Gysin homomorphism of the zero scheme of a global section of an
> invertible module, descended to Chow groups,
>
>   `i^* : A_{k+1}(X) ⟶ A_k(D)`,
>
> granted the single-component datum. This is
> `Stacks.Chow.gysinHomomorphismOnChowOfInvertible` with its vanishing hypothesis supplied by
> `Stacks.Chow.gysinOfInvertibleFactorsThroughRationalEquivalence_of_components`, so it is a
> function of `L`, `s` and that datum alone, and
> `Stacks.Chow.eq_gysinHomomorphismOnChowOfInvertible` says it is the only homomorphism of Chow
> groups agreeing with the Gysin map on cycle representatives.

```lean
def gysinHomomorphismOnChowOfInvertibleOfComponents
    (h : GysinOfInvertibleKillsPrincipalDivisorOnComponent C p k L s) :
    chowGroup C p (k + 1) →+
      chowGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
```

**`Stacks.Chow.gysinOfInvertibleFactorsThroughRationalEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/GysinComponentDischarge.lean, line 837](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/GysinComponentDischarge.lean#L837). The attribute's comment: “the Gysin map factors through rational equivalence, with no hypothesis: the single-component case the source's proof reduces to is proved here, as `gysinOfInvertibleKillsPrincipalDivisorOnComponent`, from the key formula 0AYC”.

> **Stacks 02TO, with no hypothesis.** The Gysin homomorphism of the zero scheme of a global
> section of an invertible module kills every `(k+1)`-cycle rationally equivalent to zero.
>
> The single-component case the source's proof reduces to is
> `Stacks.Chow.gysinOfInvertibleKillsPrincipalDivisorOnComponent`, proved above, and the reduction
> to it is `Stacks.Chow.gysinOfInvertibleFactorsThroughRationalEquivalence_of_components`.

```lean
theorem gysinOfInvertibleFactorsThroughRationalEquivalence :
    GysinOfInvertibleFactorsThroughRationalEquivalence C p k L s
```

**`Stacks.Chow.gysinChowOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/GysinComponentDischarge.lean, line 853](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/KeyFormula/GysinComponentDischarge.lean#L853). The attribute's comment: “the descended map i^* : A_{k+1}(X) ⟶ A_k(D), with no hypothesis: the single-component datum is proved, in `gysinOfInvertibleKillsPrincipalDivisorOnComponent`”.

> **Stacks 02TO, with no hypothesis.** The Gysin homomorphism of the zero scheme `D = Z(s)` of a
> global section of an invertible module, descended to Chow groups,
>
>   `i^* : A_{k+1}(X) ⟶ A_k(D)`.
>
> This is `Stacks.Chow.gysinHomomorphismOnChowOfInvertibleOfComponents` with its single-component
> datum supplied, and `Stacks.Chow.eq_gysinHomomorphismOnChowOfInvertible` says it is the only
> homomorphism of Chow groups agreeing with the Gysin map of Stacks 02T8 on cycle
> representatives.

```lean
def gysinChowOfInvertible : chowGroup C p (k + 1) →+
    chowGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
```

## Tag 0F95, a lemma

[Tag 0F95](https://stacks.math.columbia.edu/tag/0F95) in the Stacks Project.

**`Stacks.Chow.gysinHomomorphismOfInvertible_properPushforward_subschemeι`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersection.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersection.lean#L280). The attribute's comment: “the identity i^* i_* α = c₁(L|_D) ∩ α in A_k(D), with i_* taken on cycles as in the source's proof, with no hypothesis”.

> **Stacks 0F95.** For the Gysin map of the zero scheme of a global section of an invertible
> module `L`, the composite with the pushforward along `i` is intersection with the first Chern
> class of the restriction `L|_D`: `i^* i_* α = c₁(L|_D) ∩ α` in `A_k(D)`.
>
> Both operations are functions of `L` and `s` alone: the Gysin map is
> `Stacks.Chow.gysinHomomorphismOfInvertible` and the right hand side is the cap product
> `Stacks.Chow.firstChernClassCapOfInvertible` of the restricted module, which is invertible by
> Stacks 0B8L. No hypothesis is carried: the two first Chern class component rules agree up to
> rational equivalence on the integral components of `D`. The statement is exactly
> `Stacks.Chow.gysinHomomorphismOfInvertible_properPushforward_zeroSchemeι`, of which this is an
> alias.

```lean
alias gysinHomomorphismOfInvertible_properPushforward_subschemeι
```

**`Stacks.Chow.gysinHomomorphismOnChowOfInvertible_properChowPushforward_subschemeι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersection.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersection.lean#L297). The attribute's comment: “the composite A_{k+1}(D) ⟶ A_k(D) of the descended operations, at any descent data h and hchernD; each is discharged by a theorem of this repository (Stacks 02TO and 02TI), so nothing is assumed”.

> **Stacks 0F95, on Chow groups.** The composite
> `i^* i_* : A_{k+1}(D) ⟶ A_k(D)` of the two descended operations of an invertible module `L` and a
> section `s` is intersection with the first Chern class of `L|_D`.
>
> The descended Gysin map is that of Stacks 02TO and the descended cap product that of Stacks 02TI,
> at descent data `h` and `hchernD`. Both are propositions proved in this repository, as
> `Stacks.Chow.gysinOfInvertibleFactorsThroughRationalEquivalence` and
> `Stacks.Chow.firstChernClassCapFactorsThroughRationalEquivalence_firstChernComponentCycleRule`, so
> the identity holds outright; with those proofs supplied it is
> `Stacks.Chow.gysinChowOfInvertible_properChowPushforward_zeroSchemeι`. The instance of Stacks 02S2
> needed for `i_*` on Chow groups is discharged, `i` being a closed immersion.

```lean
theorem gysinHomomorphismOnChowOfInvertible_properChowPushforward_subschemeι
    (h : GysinOfInvertibleFactorsThroughRationalEquivalence C p k L s)
    (hchernD : FirstChernClassCapFactorsThroughRationalEquivalence C
      ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
      (firstChernComponentCycleRule C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
        ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X L s).subschemeι).obj L)))
    (α : chowGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) (k + 1)) :
    gysinHomomorphismOnChowOfInvertible C p k L s h
        (properChowPushforward C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) p
          (Stacks.Divisors.zeroScheme X L s).subschemeι rfl (k + 1)
          (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
            (Stacks.Divisors.zeroScheme X L s).subschemeι C
            ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) p rfl (k + 1)) α) =
      firstChernClassCapOnChow C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
        (firstChernComponentCycleRule C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
          ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X L s).subschemeι).obj L))
        hchernD α
```

**`Stacks.Chow.gysinChowOfInvertible_comp_properChowPushforward_zeroSchemeι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersectionChow.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersectionChow.lean#L88).

> **Stacks 0F95.** The composite of the proper pushforward along the zero scheme
> `i : D = Z(s) ⟶ X` of a global section of an invertible module with the Gysin map of that zero
> scheme is intersection with the first Chern class of the restriction `L|_D`:
>
>   `i^* i_* α = c₁(L|_D) ∩ α`  in  `\CH_k(D)`,  for `α ∈ \CH_{k+1}(D)`.
>
> All three maps are the operations on Chow groups: `i_*` is Tag 0GU8, whose vanishing hypothesis
> of Tag 02S2 is discharged by
> `Stacks.Chow.properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion`, `i^*` is
> the descended Gysin map `Stacks.Chow.gysinChowOfInvertible` of Tag 02TO and the right hand side
> is the descended cap product `Stacks.Chow.firstChernClassCapChow` of Tag 02TI, both of which are
> unconditional in this repository. No hypothesis is carried.
>
> Every class is the class of a cycle, and on a cycle the identity is
> `Stacks.Chow.gysinHomomorphismOfInvertible_properPushforward_zeroSchemeι`.

```lean
theorem gysinChowOfInvertible_comp_properChowPushforward_zeroSchemeι :
    (gysinChowOfInvertible C p k L s).comp
        (properChowPushforward C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) p
          (Stacks.Divisors.zeroScheme X L s).subschemeι rfl (k + 1)
          (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
            (Stacks.Divisors.zeroScheme X L s).subschemeι C
            ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) p rfl (k + 1))) =
      firstChernClassCapChow C k ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p)
        ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X L s).subschemeι).obj L)
```

**`Stacks.Chow.gysinChowOfInvertible_properChowPushforward_zeroSchemeι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersectionChow.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersectionChow.lean#L106).

> **Stacks 0F95**, read on a class. This is
> `Stacks.Chow.gysinChowOfInvertible_comp_properChowPushforward_zeroSchemeι` evaluated at `α`, the
> source's "sends `α` to `c₁(L|_D) ∩ α`".

```lean
theorem gysinChowOfInvertible_properChowPushforward_zeroSchemeι
    (α : chowGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) (k + 1)) :
    gysinChowOfInvertible C p k L s
        (properChowPushforward C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) p
          (Stacks.Divisors.zeroScheme X L s).subschemeι rfl (k + 1)
          (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
            (Stacks.Divisors.zeroScheme X L s).subschemeι C
            ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) p rfl (k + 1)) α) =
      firstChernClassCapChow C k ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p)
        ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X L s).subschemeι).obj L) α
```

**`Stacks.Chow.gysinHomomorphismOfInvertible_properPushforward_zeroSchemeι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersectionFormula.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/SelfIntersectionFormula.lean#L358). The attribute's comment: “the identity i^* i_* α = c₁(L|_D) ∩ α in A_k(D), with i_* taken on cycles as in the source's proof”. References: SGA 5 VII (9.2), “Codimension d = 1”.

> **The self-intersection formula.** For the Gysin map of the zero scheme `i : D = Z(s) ⟶ X` of
> a global section of an invertible module `L`, the composite with the pushforward along `i` is
> intersection with the first Chern class of the restriction `L|_D`:
>
>   `i^* i_* α = c₁(L|_D) ∩ α`  in  `A_k(D)`,  for `α ∈ Z_{k+1}(D)`.
>
> Both operations are functions of `L` and `s` alone: the Gysin map is
> `Stacks.Chow.gysinHomomorphismOfInvertible` (Tag 02T8) and the right hand side is the cap product
> `Stacks.Chow.firstChernClassCapOfInvertible` (Tag 02SO) of the restricted module, which is
> invertible by Tag 0B8L. No hypothesis is carried; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.Gysin42.SelfIntersectionFormula`.

```lean
theorem gysinHomomorphismOfInvertible_properPushforward_zeroSchemeι
    (α : CycleGroup C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) (k + 1)) :
    gysinHomomorphismOfInvertible C p k L s
        (properPushforward C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) p
          (Stacks.Divisors.zeroScheme X L s).subschemeι rfl (k + 1) α) =
      firstChernClassCapOfInvertible C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
        ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X L s).subschemeι).obj L) α
```

## Tag 0B72, a lemma

[Tag 0B72](https://stacks.math.columbia.edu/tag/0B72) in the Stacks Project.

**`Stacks.Chow.gysinNaturality_firstChernIdentityCapRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/FirstChernClassCanonical.lean#L327). The attribute's comment: “the Gysin identity read for the identity cap rule of the canonical first Chern class cap product on the test schemes of X, i.e. the predicate `IdentityCapRule.GysinNaturality` that the bivariant class of Stacks 0B77 takes as its third naturality hypothesis, with no hypothesis of its own”.

> **The Gysin identity on the test schemes.** For the canonical first Chern class cap product, a
> test morphism `g : T ⟶ X`, and an invertible module `𝒩` on `T` with a global section `s` and zero
> scheme `i : D = Z(s) ⟶ T`,
>
>   `c₁((i ∘ g)^*ℒ) ∩ i^*α = i^*(c₁(g^*ℒ) ∩ α)`.
>
> This is `Stacks.Chow.IdentityCapRule.GysinNaturality` for
> `Stacks.Chow.firstChernIdentityCapRule` at the canonical cap product and the canonical Gysin
> system.

```lean
theorem gysinNaturality_firstChernIdentityCapRule :
    IdentityCapRule.GysinNaturality C sX 1
      (firstChernIdentityCapRule C sX (canonicalFirstChernCapRule C) L)
      (canonicalGysinSystem C)
```

**`Stacks.Chow.GenuineChern.gysinChowOfInvertible_firstChernClassCapChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/GysinFirstChernCap.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GenuineChern/GysinFirstChernCap.lean#L82). The attribute's comment: “the identity i^* (c_1(N) cap a) = c_1(i^* N) cap i^* a on Chow groups, for every class a, stated for the descended operations of Stacks 02TO and 02TI that the library proves outright (`gysinChowOfInvertible`, `firstChernClassCapChow`); nothing about the Gysin map, the cap product or their descent is left over. The source proves the tag with the proof of Stacks 0B73 through Stacks 02TM on the integral components; here it is deduced from Stacks 0B73 itself for the pair `(L, s)` and the zero section of `N`, using Stacks 02T9 to read `j_* j^*` as the cap product and Stacks 02TA for the pushforward along `Z(0) = X ⟶ X`”.

> Let `ℒ` be an invertible module on `X` with a global section `s` and zero scheme
> `i : D = Z(s) ⟶ X`, and let `𝒩` be an invertible module on `X`. Then Gysin pullback along `i`
> commutes with capping with the first Chern class of `𝒩`:
>
>   `i^*(c₁(𝒩) ∩ α) = c₁(i^*𝒩) ∩ i^*α`  in  `A_k(D)`,  for every `α ∈ A_{k+2}(X)`.

```lean
theorem gysinChowOfInvertible_firstChernClassCapChow (α : chowGroup C p (k + 1 + 1)) :
    gysinChowOfInvertible C p k L s (firstChernClassCapChow C (k + 1) p N α) =
      firstChernClassCapChow C k ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p)
        ((Scheme.Modules.pullback (Stacks.Divisors.zeroScheme X L s).subschemeι).obj N)
        (gysinChowOfInvertible C p (k + 1) L s α)
```

**`Stacks.Chow.gysinChowOfInvertible_firstChernClassCapChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ChernCapGysinCommute.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Gysin42/ChernCapGysinCommute.lean#L167). The attribute's comment: “the identity i^*(c_1(N) cap alpha) = c_1(i^* N) cap i^* alpha in A_k(D), for the Gysin map of Stacks 02TO and the cap product of Stacks 02TI, with no hypothesis”.

> **Stacks 0B72, with no hypothesis.** For an invertible module `ℒ` with a global section `s`
> whose zero scheme is `i : D = Z(s) ⟶ X`, and a second invertible module `𝒩` on `X`, Gysin
> pullback along `i` commutes with capping with the first Chern class of `𝒩`:
>
>   `i^*(c₁(𝒩) ∩ α) = c₁(i^*𝒩) ∩ i^*α`  in  `A_k(D)`,  for  `α ∈ A_{k+2}(X)`.
>
> The Gysin map is the one of Stacks 02TO and the cap product the one of Stacks 02TI, both
> constructed in this repository with no hypothesis. Nothing is assumed: the cap product with
> `c₁(𝒩)` is itself the Gysin map of the zero section of `𝒩`, so the identity is Stacks 0B73 for
> the pairs `(ℒ, s)` and `(𝒩, 0)`, read through Stacks 02T9 on `X` and on `D` and Stacks 02TA
> across `Z(0) ⟶ X`. See the implementation notes.

```lean
theorem gysinChowOfInvertible_firstChernClassCapChow (α : chowGroup C p (k + 1 + 1)) :
    gysinChowOfInvertible C p k L s (firstChernClassCapChow C (k + 1) p N α) =
      firstChernClassCapChow C k ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p)
        (zeroSchemeRestrictModule L N s) (gysinChowOfInvertible C p (k + 1) L s α)
```

## Tag 0B73, a lemma

[Tag 0B73](https://stacks.math.columbia.edu/tag/0B73) in the Stacks Project.

**`Stacks.Chow.gysinChowOfInvertible_comm`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/GysinGysinKeyFormula.lean, line 1362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/GysinGysinKeyFormula.lean#L1362).

> Let `(S, δ)` be the base situation of chapter 42 of the Stacks Project, let
> `X` be locally of finite type over `S`, and let `(L, s, i : D → X)` and `(L', s', i' : D' → X)`
> be two triples as in Definition 02T8, so that `D = Z(s)` and `D' = Z(s')` are the zero schemes of
> the two sections. Write `j : D ∩ D' → D` and `j' : D ∩ D' → D'` for the two presentations of the
> scheme-theoretic intersection as a zero scheme — of the restriction of `s'` to `D`, and of the
> restriction of `s` to `D'` — and let `e` be an isomorphism between them over `X`. Then the
> diagram
>
> ```
>   CH_k(X)  --i^*-->  CH_{k-1}(D)
>      |                  |
>   (i')^*               j^*
>      v                  v
>   CH_{k-1}(D') --(j')^*--> CH_{k-2}(D ∩ D')
> ```
>
> commutes, each of the four maps being a Gysin map. The input degree is written `(k + 1) + 1`.

```lean
theorem gysinChowOfInvertible_comm
    (e : (zeroSchemeInter L L' s s').subscheme ≅ (zeroSchemeInter L' L s' s).subscheme)
    (he : e.hom ≫ (zeroSchemeInter L' L s' s).subschemeι ≫
        (Stacks.Divisors.zeroScheme X L' s').subschemeι =
      (zeroSchemeInter L L' s s').subschemeι ≫ (Stacks.Divisors.zeroScheme X L s).subschemeι)
    (α : chowGroup C p (k + 1 + 1)) :
    chowPushforwardOfIso C ((zeroSchemeInter L L' s s').subschemeι ≫
          (Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p)
        ((zeroSchemeInter L' L s' s).subschemeι ≫
          (Stacks.Divisors.zeroScheme X L' s').subschemeι ≫ p)
        e.hom (iso_zeroSchemeInter_comp_structureMorphism C p L L' s s' e he) k
        (gysinChowOfInvertible C ((Stacks.Divisors.zeroScheme X L s).subschemeι ≫ p) k
          (zeroSchemeRestrictModule L L' s) (restrictSectionToZeroScheme L L' s s')
          (gysinChowOfInvertible C p (k + 1) L s α)) =
      gysinChowOfInvertible C ((Stacks.Divisors.zeroScheme X L' s').subschemeι ≫ p) k
        (zeroSchemeRestrictModule L' L s') (restrictSectionToZeroScheme L' L s' s)
        (gysinChowOfInvertible C p (k + 1) L' s' α)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.30, Tag 02TK](https://stacks.math.columbia.edu/tag/02TK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: Stacks.Chow.firstChernClassCapOfInvertible, Stacks.Chow.firstChernClassCapOfInvertible_integral, Stacks.Chow.firstChernClassCapOfInvertible_finsum, Stacks.Chow.firstChernClassCapOfInvertible_tensorObj, Stacks.Chow.firstChernClassCapOfInvertible_unit, Stacks.Chow.zeroCycle_eq_sum_components, Stacks.ChernCap42.firstChernClassCapOfInvertible_closedSubscheme_eq_zeroScheme
statement: formalized
proof: formalized
---

# 42.25 Intersecting with an invertible sheaf

Section 42.25 of the Stacks Project, [Tag 02SN](https://stacks.math.columbia.edu/tag/02SN). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02SO, a definition

[Tag 02SO](https://stacks.math.columbia.edu/tag/02SO) in the Stacks Project.

**`Stacks.Chow.firstChernClassCapOfInvertible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernComponent/ClassRule.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernComponent/ClassRule.lean#L103).

> The first Chern class cap product `Z_{k+1}(X) ⟶ A_k(X)`, `α ↦ c₁(L) ∩ α`, of an invertible
> module: `Stacks.Chow.firstChernClassCap` at the component rule of `L`.

```lean
abbrev firstChernClassCapOfInvertible : CycleGroup C p (k + 1) →+ chowGroup C p k
```

**`Stacks.Chow.firstChernClassCapOfInvertible_integral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean#L110). The attribute's comment: “integral component formula”.

> On the fundamental cycle of a single integral closed subscheme `W ⊆ X` of delta-dimension
> `k + 1`, the cap product of an invertible module is the proper Chow pushforward along `W ⟶ X` of
> the first Chern class of `L|_W`.
>
> This is `Stacks.Chow.firstChernClassCapOfInvertible_integral_cycle` read through
> `Stacks.Chow.properChowPushforward_mk`. The instance of Stacks 02S2 that
> `Stacks.Chow.properChowPushforward` requires is discharged, `W.subschemeι` being a closed
> immersion.

```lean
theorem firstChernClassCapOfInvertible_integral (W : X.IdealSheafData)
    (hW : IsIntegral W.subscheme)
    (hDim : schemeDeltaDimension C (W.subschemeι ≫ p) = ((k + 1 : ℤ) : EInt)) :
    firstChernClassCapOfInvertible C p k L
        (cycleAssociatedToClosedSubscheme C p W.subschemeι (k + 1)) =
      properChowPushforward C (W.subschemeι ≫ p) p W.subschemeι rfl k
        (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion W.subschemeι C
          (W.subschemeι ≫ p) p rfl k)
        (firstChernComponentClass C p k L W hW hDim)
```

**`Stacks.Chow.firstChernClassCapOfInvertible_finsum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/InvertibleChernSpecialization.lean#L125). The attribute's comment: “locally finite component formula”.

> The locally finite component formula for the cap product of an invertible module: on a
> presentation `α = ∑ n_j [W_j]` of a `(k+1)`-cycle, `c₁(L) ∩ α` is the class of
> `∑ n_j c₁(L) ∩ [W_j]`.

```lean
theorem firstChernClassCapOfInvertible_finsum {J : Type u} (W : J → X.IdealSheafData)
    (hW : ∀ j, IsIntegral (W j).subscheme)
    (hDim : ∀ j, schemeDeltaDimension C ((W j).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
    (hLocal : LocallyFinite fun j ↦ ((W j).support : Set X)) (n : J → ℤ)
    (α : CycleGroup C p (k + 1))
    (hα : ∀ x : X, α.1 x = ∑ᶠ j : J, n j *
      (cycleAssociatedToClosedSubscheme C p (W j).subschemeι (k + 1)).1 x) :
    ∃ β : CycleGroup C p k,
      firstChernClassCapOfInvertible C p k L α = QuotientAddGroup.mk β ∧
      ∀ x : X, β.1 x = ∑ᶠ j : J, n j *
        (firstChernComponentCycle C p k (firstChernComponentCycleRule C p k L)
          (W j) (hW j) (hDim j)).1 x
```

## Tag 02SP, a lemma

[Tag 02SP](https://stacks.math.columbia.edu/tag/02SP) in the Stacks Project.

**`Stacks.Chow.firstChernClassCapOfInvertible_tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FirstChernClassTensor.lean, line 498](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FirstChernClassTensor.lean#L498). The attribute's comment: “additivity in the invertible module”.

> **Stacks 02SP.** Let `(S, δ)` be the base situation of chapter 42, let `X` be locally of
> finite type over `S` and let `L`, `N` be invertible `𝒪_X`-modules. Then
>
>   `c₁(L) ∩ α + c₁(N) ∩ α = c₁(L ⊗_{𝒪_X} N) ∩ α`
>
> in `A_k(X)` for every `α ∈ Z_{k+1}(X)`. The companion assertion of the same tag,
> `c₁(𝒪_X) ∩ α = 0`, is `Stacks.Chow.firstChernClassCapOfInvertible_unit`, deduced from this one
> through `𝒪_X ⊗_{𝒪_X} 𝒪_X ≅ 𝒪_X`.
>
> The cap product is the one of `StacksFrontier.AlgebraicGeometry.Chow.ChernComponent.ClassRule`; see
> the module documentation for why no `@[stacks 02SO]` attribute accompanies it.

```lean
theorem firstChernClassCapOfInvertible_tensorObj (α : CycleGroup C p (k + 1)) :
    firstChernClassCapOfInvertible C p k L α + firstChernClassCapOfInvertible C p k N α =
      firstChernClassCapOfInvertible C p k (Scheme.Modules.tensorObj L N) α
```

**`Stacks.Chow.firstChernClassCapOfInvertible_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FirstChernClassTensor.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FirstChernClassTensor.lean#L515). The attribute's comment: “vanishing on the structure sheaf”.

> **Stacks 02SP.** `c₁(𝒪_X) ∩ α = 0` in `A_k(X)` for every `α ∈ Z_{k+1}(X)`.
>
> Additivity applied to `L = N = 𝒪_X` together with `𝒪_X ⊗_{𝒪_X} 𝒪_X ≅ 𝒪_X` gives
> `c₁(𝒪_X) ∩ α + c₁(𝒪_X) ∩ α = c₁(𝒪_X) ∩ α`.
>
> The companion assertion of the same tag is
> `Stacks.Chow.firstChernClassCapOfInvertible_tensorObj`.

```lean
theorem firstChernClassCapOfInvertible_unit (α : CycleGroup C p (k + 1)) :
    firstChernClassCapOfInvertible C p k (SheafOfModules.unit X.ringCatSheaf) α = 0
```

## Tag 0EPI, a lemma

[Tag 0EPI](https://stacks.math.columbia.edu/tag/0EPI) in the Stacks Project.

**`Stacks.Chow.zeroCycle_eq_sum_components`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/IntersectionInvertibleSheaf.lean, line 927](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/IntersectionInvertibleSheaf.lean#L927).

> **Stacks 0EPI.** Let `(S, δ)` be the base situation of chapter 42, let `Y` be locally of
> finite type over `S`, let `L` be an invertible `𝒪_Y`-module and `s` a global section of `L`.
> Assume `dim_δ(Y) ≤ k + 1`, `dim_δ(Z(s)) ≤ k`, and that multiplication by `s` is injective on
> the stalk at the generic point of every component of `Z(s)` of delta-dimension `k`. Then the
> `k`-cycle of `Z(s)` is the sum of the `k`-cycles of the zero schemes of the restrictions of `s`
> to the components of `Y` of delta-dimension `k + 1`, weighted by their multiplicities in the
> fundamental cycle `[Y]_{k + 1}`.

```lean
theorem zeroCycle_eq_sum_components (C : ChowSituation.{u}) {Y : Scheme.{u}}
    (f : Y ⟶ C.S) [LocallyOfFiniteType f] (L : Y.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible Y.sheaf.obj Y.ringCatSheaf.property L]
    (s : L.sections) (k : ℤ)
    (hY : schemeDeltaDimension C f ≤ (k + 1 : EInt))
    (hD : schemeDeltaDimension C
      ((Stacks.Divisors.zeroScheme Y L (s.eval (op ⊤))).subschemeι ≫ f) ≤ (k : EInt))
    (hs : ∀ ξ : genericPoints (Stacks.Divisors.zeroScheme Y L (s.eval (op ⊤))).subscheme,
      relativeDimension C.dimensionFunction f
        ((Stacks.Divisors.zeroScheme Y L (s.eval (op ⊤))).subschemeι ξ.1) = k →
      Function.Injective (ConcreteCategory.hom
        ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u}
          ((Stacks.Divisors.zeroScheme Y L (s.eval (op ⊤))).subschemeι ξ.1)).map
          ((Scheme.Modules.toPresheaf Y).map (L.unitHomEquiv.symm s))))) :
    let D := Stacks.Divisors.zeroScheme Y L (s.eval (op ⊤))
    ∀ x : Y,
      (cycleAssociatedToClosedSubscheme C f D.subschemeι k).1 x =
        ∑ᶠ W : {W : irreducibleComponents Y //
            deltaDimension C f
              ⟨W.1, W.2.1, isClosed_of_mem_irreducibleComponents W.1 W.2⟩ = k + 1},
          (cycleAssociatedToClosedSubscheme C f (𝟙 Y) (k + 1)).1 W.1.2.1.genericPoint *
            (cycleAssociatedToClosedSubscheme C f
              ((Scheme.IdealSheafData.vanishingIdeal
                ⟨W.1.1, isClosed_of_mem_irreducibleComponents W.1.1 W.1.2⟩ ⊔ D).subschemeι)
              k).1 x
```

## Tag 02SQ, a lemma

[Tag 02SQ](https://stacks.math.columbia.edu/tag/02SQ) in the Stacks Project.

**`Stacks.ChernCap42.firstChernClassCapOfInvertible_closedSubscheme_eq_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCap42/ClosedSubschemeZeroCycle.lean, line 862](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChernCap42/ClosedSubschemeZeroCycle.lean#L862).

> **Stacks 02SQ.** Let `(S, δ)` be the base situation of chapter 42 of the Stacks Project, let
> `X` be locally of finite type over `S`, let `L` be an invertible `𝒪_X`-module, let `Y ⊆ X` be a
> closed subscheme and let `s` be a global section of `L|_Y`. Assume `dim_δ(Y) ≤ k + 1`, that
> `dim_δ(Z(s)) ≤ k`, and that multiplication by `s` is injective on the local ring at the generic
> point of every component of `Z(s)` of `δ`-dimension `k`. Then
>
> `c₁(L) ∩ [Y]_{k + 1} = [Z(s)]_k`  in  `A_k(X)`.
>
> The cycle `[Z(s)]_k` is read on `X` through the composite of the closed immersion of `Z(s)` into
> `Y` with that of `Y` into `X`.

```lean
theorem firstChernClassCapOfInvertible_closedSubscheme_eq_zeroScheme
    (s : ((Scheme.Modules.pullback i).obj L).sections)
    (hY : schemeDeltaDimension C (i ≫ p) ≤ (k + 1 : EInt))
    (hD : schemeDeltaDimension C
      ((Stacks.Divisors.zeroScheme Y ((Scheme.Modules.pullback i).obj L)
        (s.eval (op ⊤))).subschemeι ≫ (i ≫ p)) ≤ (k : EInt))
    (hs : ∀ ξ : genericPoints (Stacks.Divisors.zeroScheme Y
        ((Scheme.Modules.pullback i).obj L) (s.eval (op ⊤))).subscheme,
      relativeDimension C.dimensionFunction (i ≫ p)
        ((Stacks.Divisors.zeroScheme Y ((Scheme.Modules.pullback i).obj L)
          (s.eval (op ⊤))).subschemeι ξ.1) = k →
      Function.Injective (ConcreteCategory.hom
        ((TopCat.Presheaf.stalkFunctor AddCommGrpCat.{u}
          ((Stacks.Divisors.zeroScheme Y ((Scheme.Modules.pullback i).obj L)
            (s.eval (op ⊤))).subschemeι ξ.1)).map
          ((Scheme.Modules.toPresheaf Y).map
            (((Scheme.Modules.pullback i).obj L).unitHomEquiv.symm s))))) :
    firstChernClassCapOfInvertible C p k L (cycleAssociatedToClosedSubscheme C p i (k + 1)) =
      QuotientAddGroup.mk (cycleAssociatedToClosedSubscheme C p
        ((Stacks.Divisors.zeroScheme Y ((Scheme.Modules.pullback i).obj L)
          (s.eval (op ⊤))).subschemeι ≫ i) k)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.25, Tag 02SN](https://stacks.math.columbia.edu/tag/02SN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

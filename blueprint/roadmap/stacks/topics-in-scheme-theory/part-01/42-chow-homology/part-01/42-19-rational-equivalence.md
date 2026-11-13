---
declaration: section
origin: cited
lean: Stacks.Chow.exists_principalDivisorFamilySum, Stacks.Chow.IsRationallyEquivalentToZero, Stacks.Chow.rationallyEquivalentToZero_zero, Stacks.Chow.rationallyEquivalentToZero_add, Stacks.Chow.rationallyEquivalentToZero_neg, Stacks.Chow.rationalEquivalences, Stacks.Chow.RationallyEquivalent, Stacks.Chow.chowGroup
statement: formalized
proof: formalized
---

# 42.19 Rational equivalence

Section 42.19 of the Stacks Project, [Tag 02RV](https://stacks.math.columbia.edu/tag/02RV). 5 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02RW, a definition

[Tag 02RW](https://stacks.math.columbia.edu/tag/02RW) in the Stacks Project.

**`Stacks.Chow.exists_principalDivisorFamilySum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DimensionFunction/PrincipalDivisorFamily.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/DimensionFunction/PrincipalDivisorFamily.lean#L110). The attribute's comment: “locally finite sums of principal divisors”.

> **Stacks 02RW.** A locally finite family of integral closed subschemes of `X` of
> delta-dimension `k + 1`, each carrying a nonzero rational function, determines a cycle of
> delta-dimension `k` on `X`, whose coefficients are the locally finite sums of the coefficients
> of the pushed-forward principal divisors.

```lean
theorem exists_principalDivisorFamilySum (C : ChowSituation.{u}) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p] (k : ℤ) {J : Type u} (W : J → X.IdealSheafData)
    (hW : ∀ j, IsIntegral (W j).subscheme)
    (hDim : ∀ j, schemeDeltaDimension C ((W j).subschemeι ≫ p) = ((k + 1 : ℤ) : EInt))
    (hLocal : LocallyFinite fun j ↦ ((W j).support : Set X))
    (g : ∀ j, (rationalFunctions (W j).subscheme)ˣ) :
    ∃ α : CycleGroup C p k,
      ∀ x : X, α.1 x = principalDivisorFamilyCoefficient C p W hW g x
```

**`Stacks.Chow.IsRationallyEquivalentToZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L330). The attribute's comment: “rationally equivalent to zero”.

> **Stacks 02RW.** A `k`-cycle is rationally equivalent to zero when its coefficients are the
> locally finite sum of the pushforwards of the principal divisors of nonzero rational functions
> on a locally finite family of integral closed subschemes of delta-dimension `k + 1`.

```lean
def IsRationallyEquivalentToZero (C : ChowSituation.{u}) {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] (k : ℤ) (α : CycleGroup C p k) : Prop
```

**`Stacks.Chow.rationallyEquivalentToZero_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L352). The attribute's comment: “zero family”.

> **Stacks 02RW.** The zero cycle is rationally equivalent to zero, via the empty family.

```lean
theorem rationallyEquivalentToZero_zero (C : ChowSituation.{u}) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p] (k : ℤ) :
    IsRationallyEquivalentToZero C p k 0
```

**`Stacks.Chow.rationallyEquivalentToZero_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L363). The attribute's comment: “closure under addition”.

> **Stacks 02RW.** The sum of two cycles rationally equivalent to zero is rationally
> equivalent to zero, via the disjoint union of the two families.

```lean
theorem rationallyEquivalentToZero_add (C : ChowSituation.{u}) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p] (k : ℤ) {α β : CycleGroup C p k}
    (hα : IsRationallyEquivalentToZero C p k α)
    (hβ : IsRationallyEquivalentToZero C p k β) :
    IsRationallyEquivalentToZero C p k (α + β)
```

**`Stacks.Chow.rationallyEquivalentToZero_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L386). The attribute's comment: “closure under negation”.

> **Stacks 02RW.** The negative of a cycle rationally equivalent to zero is rationally
> equivalent to zero, via the inverses of the same rational functions.

```lean
theorem rationallyEquivalentToZero_neg (C : ChowSituation.{u}) {X : Scheme.{u}}
    (p : X ⟶ C.S) [LocallyOfFiniteType p] (k : ℤ) {α : CycleGroup C p k}
    (hα : IsRationallyEquivalentToZero C p k α) :
    IsRationallyEquivalentToZero C p k (-α)
```

**`Stacks.Chow.rationalEquivalences`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 402](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L402). The attribute's comment: “cycles rationally equivalent to zero”.

> **Stacks 02RW.** The subgroup of `k`-cycles rationally equivalent to zero.

```lean
def rationalEquivalences (C : ChowSituation.{u}) {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] (k : ℤ) : AddSubgroup (CycleGroup C p k)
```

**`Stacks.Chow.RationallyEquivalent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L419). The attribute's comment: “rational equivalence”.

> **Stacks 02RW.** Two `k`-cycles are rationally equivalent when their difference is a locally
> finite sum of pushforwards of principal divisors.

```lean
abbrev RationallyEquivalent (C : ChowSituation.{u}) {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] (k : ℤ) (α β : CycleGroup C p k) : Prop
```

**`Stacks.Chow.chowGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean, line 425](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalenceDefs.lean#L425). The attribute's comment: “Chow group”. References: SGA 6 XIV (4.1), “partial”.

> **Stacks 02RW.** The Chow group `A_k(X)` of `k`-cycles modulo rational equivalence.

```lean
abbrev chowGroup (C : ChowSituation.{u}) {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] (k : ℤ) : Type u
```

## Tag 0GU3, a remark

[Tag 0GU3](https://stacks.math.columbia.edu/tag/0GU3) in the Stacks Project.

**`Stacks.Chow.pointwiseDivisorDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseDivisor.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseDivisor.lean#L465). The attribute's comment: “pointwise\_divisor\_differential”.

> **Stacks 0GU3.** The divisor differential from pointwise Milnor K₁-chains at the points of
> relative dimension `k + 1` to pointwise Milnor K₀-chains at the points of relative dimension `k`:
> each Milnor K₁-class is read as a nonzero rational function on the closure of its point, and the
> differential is the locally finite sum of the pushed-forward principal divisors, transported to
> the pointwise description of cycles of Stacks 0GU2.

```lean
def pointwiseDivisorDifferential (k : ℤ) :
    PointwiseKOneGroup C p k →+ PointwiseCycleGroup C p k
```

**`Stacks.Chow.pointwiseDivisorDifferential_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseDivisor.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseDivisor.lean#L474). The attribute's comment: “pointwise\_divisor\_differential”.

> **Stacks 0GU3.** The divisor differential satisfies the coordinatewise divisor formula.

```lean
theorem pointwiseDivisorDifferential_spec (k : ℤ) :
    IsPointwiseDivisorDifferential C p k (pointwiseDivisorDifferential C p k)
```

**`Stacks.Chow.exists_pointwiseDivisorDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseDivisor.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwiseDivisor.lean#L487). The attribute's comment: “pointwise\_divisor\_differential”.

> **Stacks 0GU3.** There is a homomorphism from pointwise Milnor K₁-chains to pointwise Milnor
> K₀-chains satisfying the coordinatewise divisor formula.

```lean
theorem exists_pointwiseDivisorDifferential (k : ℤ) :
    ∃ d : PointwiseKOneGroup C p k →+ PointwiseCycleGroup C p k,
      IsPointwiseDivisorDifferential C p k d
```

**`Stacks.Chow.pointwiseChowClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwisePresentation.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwisePresentation.lean#L75). The attribute's comment: “the map from pointwise cycles to the Chow group”.

> **Stacks 0GU3.** The class in the Chow group `A_k(X)` of a locally finite family of
> degree-zero Milnor K-classes at the points of relative dimension `k`: the cycle it names,
> modulo rational equivalence.

```lean
def pointwiseChowClass (k : ℤ) : PointwiseCycleGroup C p k →+ chowGroup C p k
```

**`Stacks.Chow.pointwiseChowClass_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwisePresentation.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwisePresentation.lean#L92). The attribute's comment: “surjectivity of the presentation”.

> **Stacks 0GU3.** Every class in the Chow group `A_k(X)` is the class of a pointwise Milnor
> K₀ chain: the chain attached to any cycle representing it.

```lean
theorem pointwiseChowClass_surjective (k : ℤ) :
    Function.Surjective (pointwiseChowClass C p k)
```

**`Stacks.Chow.pointwiseDivisorDifferential_range_eq_ker_pointwiseChowClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwisePresentation.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/PointwisePresentation.lean#L424). The attribute's comment: “exactness of the presentation”.

> **Stacks 0GU3.** The presentation of the Chow group is exact in the middle: a pointwise
> Milnor K₀-chain is a pointwise divisor exactly when the cycle it names is rationally equivalent
> to zero.

```lean
theorem pointwiseDivisorDifferential_range_eq_ker_pointwiseChowClass (k : ℤ) :
    (pointwiseDivisorDifferential C p k).range = (pointwiseChowClass C p k).ker
```

## Tag 02RX, a lemma

[Tag 02RX](https://stacks.math.columbia.edu/tag/02RX) in the Stacks Project.

**`Stacks.Chow.exists_rationallyEquivalent_properPushforward_of_cycleGroupRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/LocalizationSequence.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/LocalizationSequence.lean#L141). The attribute's comment: “lifting a rational equivalence from an open subscheme”.

> Let `V ⊆ X` be an open subscheme and let `i : Y ⟶ X` be a closed immersion whose image is the
> complement of `V`. If two `k`-cycles on `X` become rationally equivalent after restriction to `V`,
> then they are rationally equivalent on `X` up to the pushforward of a `k`-cycle on `Y`.

```lean
theorem exists_rationallyEquivalent_properPushforward_of_cycleGroupRestrict
    (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (i : Y ⟶ X) [IsClosedImmersion i] (hi : i ≫ sX = sY)
    (V : X.Opens) (hcomplement : Set.range i.base = (Set.range V.ι.base)ᶜ)
    (k : ℤ) (α β : CycleGroup C sX k)
    (h : RationallyEquivalent C (V.ι ≫ sX) k
      (cycleGroupOpensRestrict C sX V k α) (cycleGroupOpensRestrict C sX V k β)) :
    ∃ γ : CycleGroup C sY k,
      RationallyEquivalent C sX k α (β + properPushforward C sY sX i hi k γ)
```

**`Stacks.Chow.surjective_chowGroupOpensRestrictOfIsOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/LocalizationSequence.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/LocalizationSequence.lean#L198). The attribute's comment: “surjectivity onto the Chow group of the open subscheme”.

> The localization sequence of Chow groups is exact at `A_k(V)`: restriction of `k`-cycle
> classes to an open subscheme `V ⊆ X` is surjective.

```lean
theorem surjective_chowGroupOpensRestrictOfIsOpenImmersion (C : ChowSituation.{u})
    {X : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (V : X.Opens) (k : ℤ) :
    Function.Surjective (chowGroupOpensRestrictOfIsOpenImmersion C sX V k)
```

**`Stacks.Chow.exact_chowPushforward_chowGroupOpensRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/LocalizationSequence.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/LocalizationSequence.lean#L212). The attribute's comment: “exactness at the Chow group of the ambient scheme”.

> The localization sequence of Chow groups is exact at `A_k(X)`: for an open subscheme `V ⊆ X`
> and a closed immersion `i : Y ⟶ X` whose image is the complement of `V`, a `k`-cycle class on `X`
> restricts to zero on `V` exactly when it is the pushforward of a `k`-cycle class on `Y`.

```lean
theorem exact_chowPushforward_chowGroupOpensRestrict (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (i : Y ⟶ X) [IsClosedImmersion i] (hi : i ≫ sX = sY)
    (V : X.Opens) (hcomplement : Set.range i.base = (Set.range V.ι.base)ᶜ) (k : ℤ) :
    Function.Exact (chowPushforwardOfIsClosedImmersion C sY sX i hi k)
      (chowGroupOpensRestrictOfIsOpenImmersion C sX V k)
```

## Tag 0F94, a lemma

[Tag 0F94](https://stacks.math.columbia.edu/tag/0F94) in the Stacks Project.

**`Stacks.Chow.exact_intersectionToSummandsChow_summandsToUnionChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/ClosedCoverExactSequence.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/ClosedCoverExactSequence.lean#L423). The attribute's comment: “exactness in the middle”.

> The sequence of Chow groups of a union of two closed subschemes is exact in the middle: a pair
> of classes of `k`-cycles on the two closed subschemes has vanishing sum of pushforwards exactly
> when it comes from a class of `k`-cycles on the scheme-theoretic intersection.

```lean
theorem exact_intersectionToSummandsChow_summandsToUnionChow
    (hcover : I.support ⊔ J.support = ⊤) :
    Function.Exact (intersectionToSummandsChow C sX I J k) (summandsToUnionChow C sX I J k)
```

**`Stacks.Chow.surjective_summandsToUnionChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/ClosedCoverExactSequence.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/ClosedCoverExactSequence.lean#L435). The attribute's comment: “surjectivity”.

> If two closed subschemes cover the ambient scheme set-theoretically, every class of `k`-cycles
> on it is the sum of the classes of the pushforwards of a `k`-cycle on each of them.

```lean
theorem surjective_summandsToUnionChow (hcover : I.support ⊔ J.support = ⊤) :
    Function.Surjective (summandsToUnionChow C sX I J k)
```

**`Stacks.Chow.surjective_chowPushforwardOfIsClosedImmersion_coprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/ClosedImmersionCoverExactSequence.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/ClosedImmersionCoverExactSequence.lean#L134). The attribute's comment: “surjectivity, for two arbitrary closed immersions”.

> **Stacks 0F94, surjectivity, for two closed immersions.** If the images of two closed
> immersions `j₁ : X₁ ⟶ X` and `j₂ : X₂ ⟶ X` cover `X`, every class of `k`-cycles on `X` is the sum
> of the pushforwards of a class on `X₁` and a class on `X₂`.

```lean
theorem surjective_chowPushforwardOfIsClosedImmersion_coprod
    (hcover : Set.range j₁ ∪ Set.range j₂ = Set.univ) :
    Function.Surjective ((chowPushforwardOfIsClosedImmersion C sX₁ sX j₁ hj₁ k).coprod
      (chowPushforwardOfIsClosedImmersion C sX₂ sX j₂ hj₂ k))
```

**`Stacks.Chow.exact_chowPushforwardOfIsClosedImmersion_prod_coprod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/ClosedImmersionCoverExactSequence.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/ClosedImmersionCoverExactSequence.lean#L179). The attribute's comment: “exactness in the middle, for two arbitrary closed immersions”.

> **Stacks 0F94, exactness in the middle, for two closed immersions.** If the images of two
> closed immersions `j₁ : X₁ ⟶ X` and `j₂ : X₂ ⟶ X` cover `X`, a pair of classes of `k`-cycles on
> `X₁` and `X₂` has vanishing sum of pushforwards exactly when it is the pair of pushforwards of a
> class on the fibre product `X₁ ×_X X₂`, the second one negated.

```lean
theorem exact_chowPushforwardOfIsClosedImmersion_prod_coprod
    (hcover : Set.range j₁ ∪ Set.range j₂ = Set.univ) :
    Function.Exact
      ((chowPushforwardOfIsClosedImmersion C (pullback.fst j₁ j₂ ≫ sX₁) sX₁
          (pullback.fst j₁ j₂) rfl k).prod
        (-chowPushforwardOfIsClosedImmersion C (pullback.fst j₁ j₂ ≫ sX₁) sX₂
          (pullback.snd j₁ j₂)
          (pullbackSnd_comp_structureMorphism_eq_fst C sX j₁ j₂ sX₁ sX₂ hj₁ hj₂)
          k))
      ((chowPushforwardOfIsClosedImmersion C sX₁ sX j₁ hj₁ k).coprod
        (chowPushforwardOfIsClosedImmersion C sX₂ sX j₂ hj₂ k))
```

## Tag 02RZ, a remark

[Tag 02RZ](https://stacks.math.columbia.edu/tag/02RZ) in the Stacks Project.

**`Stacks.Chow.rationallyEquivalent_finsum_of_closedSupports`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChowToolkit/ClosedImmersionCarrier.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/ChowToolkit/ClosedImmersionCarrier.lean#L250).

> **Stacks 02RZ, two-sided form.** Rational equivalences on a locally finite family of closed
> subschemes of `X` may be summed: if cycles `a i` and `b i` on the closed subschemes `T i` are
> rationally equivalent for each `i`, and the cycles `α`, `β` on `X` are coefficientwise the locally
> finite sums of the pushforwards of the `a i` and of the `b i`, then `α` and `β` are rationally
> equivalent on `X`.
>
> Both locally finite sums have finite support at each point, because the pushforward of a cycle on
> `T i` is supported on `(T i).support` and the family of those supports is locally finite. So they
> may be subtracted termwise, which exhibits `α - β` as the locally finite sum of the pushforwards of
> the `a i - b i`, each rationally equivalent to zero, and
> `Stacks.Chow.rationallyEquivalentToZero_finsum_of_closedSupports` applies.

```lean
theorem rationallyEquivalent_finsum_of_closedSupports (p : X ⟶ C.S)
    [LocallyOfFiniteType p] (k : ℤ) {I : Type u} (T : I → X.IdealSheafData)
    (hT : LocallyFinite fun i ↦ ((T i).support : Set X))
    (a b : ∀ i, CycleGroup C ((T i).subschemeι ≫ p) k)
    (hab : ∀ i, RationallyEquivalent C ((T i).subschemeι ≫ p) k (a i) (b i))
    {α β : CycleGroup C p k}
    (hα : ∀ x : X, α.1 x = ∑ᶠ i : I,
      (properPushforward C ((T i).subschemeι ≫ p) p (T i).subschemeι rfl k (a i)).1 x)
    (hβ : ∀ x : X, β.1 x = ∑ᶠ i : I,
      (properPushforward C ((T i).subschemeι ≫ p) p (T i).subschemeι rfl k (b i)).1 x) :
    RationallyEquivalent C p k α β
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.19, Tag 02RV](https://stacks.math.columbia.edu/tag/02RV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

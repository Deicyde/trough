---
declaration: section
origin: cited
lean: Stacks.Chow.VeryWeakCapRule.cap_eq_zero_of_isCycleGysinNatural, Stacks.Chow.VeryWeakCapRule.capChowOfCycleGysin, Stacks.Chow.WeakCapRule.toBivariantClass, Stacks.Chow.BivariantClass.eq_zero_iff_capsIntegralFundamentalClassesToZero, Stacks.Chow.BivariantClass.capsIntegralFundamentalClassesToZero_of_hasBirationalModification, Stacks.Chow.BivariantClass.capsIntegralFundamentalClassesToZero_iff_hasBirationalModification, Stacks.Chow.BivariantClass.eq_zero_tfae, Stacks.Chow.BivariantClass.eq_zero_iff_capsIntegral_canonical
statement: formalized
proof: formalized
---

# 42.35 Lemmas on bivariant classes

Section 42.35 of the Stacks Project, [Tag 0FDY](https://stacks.math.columbia.edu/tag/0FDY). 6 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B7A, a lemma

[Tag 0B7A](https://stacks.math.columbia.edu/tag/0B7A) in the Stacks Project.

**`Stacks.Chow.VeryWeakCapRule.cap_eq_zero_of_isCycleGysinNatural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VeryWeakBivariantCriterion.lean, line 792](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VeryWeakBivariantCriterion.lean#L792).

> **Stacks 0B7A, the very weak form of Fulton's Theorem 17.1.** Let `(S, δ)` be as in
> Situation 02QL, let `f : X ⟶ Y` be a morphism of schemes locally of finite type over `S` and let
> `p ∈ ℤ`. A rule assigning to every locally of finite type `g : Y' ⟶ Y` and every `k` a map
>
>   `c ∩ - : Z_k(Y') ⟶ A_{k-p}(X')`,   `X' = Y' ×_Y X`,
>
> which satisfies condition (3) of Definition 0B76 whenever the invertible module restricts
> trivially to the divisor, factors through rational equivalence: it kills every cycle rationally
> equivalent to zero.
>
> A cycle `α` rationally equivalent to zero is the total fibre difference of a locally finite
> family of integral closed subschemes of `Y' ×_S 𝐏¹_S` (Stacks 02S4 part (4)); so `α` is the
> difference of the two section Gysin images of the cycle `β` that family presents
> (`Stacks.Chow.sub_gysinCycleMapAlong_sections_eq_of_familyFibreDifference`), and the two
> sections are effective Cartier divisors with trivial normal bundle, so condition (3) applies at
> both and gives the same value
> (`Stacks.Chow.cap_gysinCycleMapAlong_zeroSection_eq_infinitySection_of_isCycleGysinNatural`).

```lean
theorem VeryWeakCapRule.cap_eq_zero_of_isCycleGysinNatural (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (f : X ⟶ Y) [LocallyOfFiniteType f]
    (hf : f ≫ sY = sX) (p : ℤ) (c : VeryWeakCapRule C sX sY f hf p)
    (hc : c.IsCycleGysinNatural) {T : Scheme.{u}}
    (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ) (α : CycleGroup C (g ≫ sY) k)
    (hα : α ∈ rationalEquivalences C (g ≫ sY) k) :
    c.cap g k α = 0
```

**`Stacks.Chow.VeryWeakCapRule.capChowOfCycleGysin`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VeryWeakBivariantCriterion.lean, line 818](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/VeryWeakBivariantCriterion.lean#L818). The attribute's comment: “the operation descended to Chow groups”.

> **Stacks 0B7A.** The operation `c ∩ -` of a very weak cap rule satisfying condition (3) read
> on cycles, descended to Chow groups: `A_k(Y') ⟶ A_{k-p}(X')`.

```lean
def VeryWeakCapRule.capChowOfCycleGysin (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) [LocallyOfFiniteType f] (hf : f ≫ sY = sX) (p : ℤ)
    (c : VeryWeakCapRule C sX sY f hf p) (hc : c.IsCycleGysinNatural) {T : Scheme.{u}}
    (g : T ⟶ Y) [LocallyOfFiniteType g]
    (k : ℤ) : chowGroup C (g ≫ sY) k →+ chowGroup C (pullback.fst f g ≫ sX) (k - p)
```

## Tag 0F9A, a lemma

[Tag 0F9A](https://stacks.math.columbia.edu/tag/0F9A) in the Stacks Project.

**`Stacks.Chow.WeakCapRule.toBivariantClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/WeakBivariantCriterionProof.lean, line 668](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/WeakBivariantCriterionProof.lean#L668).

> **[Stacks, Tag 0F9A], a weak form of Fulton's Theorem 17.1.** Let `(S, δ)` be as in Situation
> 02QL, let `f : X ⟶ Y` be a morphism of schemes locally of finite type over `S` and let `p ∈ ℤ`.
> A rule assigning to every morphism `Y' ⟶ Y` locally of finite type and every `k` a map
> `c ∩ - : A_k(Y') ⟶ A_{k-p}(Y' ×_Y X)`, satisfying conditions (1) and (2) of Stacks 0B76 and
> condition (3) whenever `ℒ'|_{D'} ≅ 𝒪_{D'}` — a `Stacks.Chow.WeakCapRule` read against the
> canonical Gysin system — is a bivariant class: an element of `A^p(X ⟶ Y)` with the same cap
> operation (`Stacks.Chow.WeakCapRule.toBivariantClass_cap`).

```lean
def WeakCapRule.toBivariantClass (w : WeakCapRule C (canonicalGysinSystem C) sX sY f hf p) :
    CanonicalBivariantClass C sX sY f hf p
```

## Tag 02UC, a lemma

[Tag 02UC](https://stacks.math.columbia.edu/tag/02UC) in the Stacks Project.

**`Stacks.Chow.BivariantClass.eq_zero_iff_capsIntegralFundamentalClassesToZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Vanishing.lean, line 726](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Vanishing.lean#L726). The attribute's comment: “(1) ⇔ (2)”.

> **Stacks 02UC, (1) `⇔` (2).** A bivariant class is zero exactly when its cap product with
> the fundamental class of every integral scheme locally of finite type over `Y` vanishes.

```lean
theorem BivariantClass.eq_zero_iff_capsIntegralFundamentalClassesToZero
    (c : BivariantClass C G sX sY f hf p) :
    c = 0 ↔ c.CapsIntegralFundamentalClassesToZero C G sX sY f hf p
```

**`Stacks.Chow.BivariantClass.capsIntegralFundamentalClassesToZero_of_hasBirationalModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Vanishing.lean, line 739](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Vanishing.lean#L739). The attribute's comment: “(3) ⇒ (2)”.

> **Stacks 02UC, (3) `⇒` (2).** If some proper birational modification of each integral test
> scheme has its fundamental class killed by `c`, then so has the test scheme itself: the
> modification pushes its fundamental class forward to the fundamental class, and capping with a
> bivariant class commutes with proper pushforward.

```lean
theorem BivariantClass.capsIntegralFundamentalClassesToZero_of_hasBirationalModification
    {c : BivariantClass C G sX sY f hf p}
    (hc : c.HasBirationalModificationCappingToZero C G sX sY f hf p) :
    c.CapsIntegralFundamentalClassesToZero C G sX sY f hf p
```

**`Stacks.Chow.BivariantClass.capsIntegralFundamentalClassesToZero_iff_hasBirationalModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Vanishing.lean, line 754](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Vanishing.lean#L754). The attribute's comment: “(2) ⇔ (3)”.

> **Stacks 02UC, (2) `⇔` (3).** A bivariant class kills the fundamental class of every integral
> scheme locally of finite type over `Y` exactly when each such scheme admits a proper birational
> modification whose fundamental class it kills.

```lean
theorem BivariantClass.capsIntegralFundamentalClassesToZero_iff_hasBirationalModification
    (c : BivariantClass C G sX sY f hf p) :
    c.CapsIntegralFundamentalClassesToZero C G sX sY f hf p ↔
      c.HasBirationalModificationCappingToZero C G sX sY f hf p
```

**`Stacks.Chow.BivariantClass.eq_zero_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Vanishing.lean, line 766](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/Vanishing.lean#L766). The attribute's comment: “all three clauses”.

> **Stacks 02UC.** For a bivariant class `c ∈ A^p(X ⟶ Y)` the following are equivalent: `c` is
> zero; `c ∩ [Y'] = 0` for every integral scheme `Y'` locally of finite type over `Y`; and every
> such `Y'` admits a proper birational `Y'' ⟶ Y'` with `c ∩ [Y''] = 0`.

```lean
theorem BivariantClass.eq_zero_tfae (c : BivariantClass C G sX sY f hf p) :
    [c = 0, c.CapsIntegralFundamentalClassesToZero C G sX sY f hf p,
      c.HasBirationalModificationCappingToZero C G sX sY f hf p].TFAE
```

**`Stacks.Chow.BivariantClass.eq_zero_iff_capsIntegral_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VanishingUnconditional.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VanishingUnconditional.lean#L121). The attribute's comment: “(1) ⇔ (2) for A^p(X ⟶ Y) itself: the bivariant group read at the canonical Gysin system `Stacks.Chow.gysinSystemOfInvertible`, which is constructed outright, so no Gysin system is assumed”.

> A bivariant class for the canonical Gysin
> system is zero exactly when its cap product with the fundamental class of every integral scheme
> locally of finite type over `Y` vanishes.

```lean
theorem BivariantClass.eq_zero_iff_capsIntegral_canonical :
    c = 0 ↔
      c.CapsIntegralFundamentalClassesToZero C (gysinSystemOfInvertible C) sX sY f hf p
```

**`Stacks.Chow.BivariantClass.capsIntegral_iff_hasBirationalModification_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VanishingUnconditional.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VanishingUnconditional.lean#L134). The attribute's comment: “(2) ⇔ (3) for A^p(X ⟶ Y) itself: the bivariant group read at the canonical Gysin system `Stacks.Chow.gysinSystemOfInvertible`, which is constructed outright, so no Gysin system is assumed”.

> A bivariant class for the canonical Gysin
> system kills the fundamental class of every integral scheme locally of finite type over `Y`
> exactly when each such scheme admits a proper birational modification whose fundamental class it
> kills.

```lean
theorem BivariantClass.capsIntegral_iff_hasBirationalModification_canonical :
    c.CapsIntegralFundamentalClassesToZero C (gysinSystemOfInvertible C) sX sY f hf p ↔
      c.HasBirationalModificationCappingToZero C (gysinSystemOfInvertible C) sX sY f hf p
```

**`Stacks.Chow.BivariantClass.eq_zero_tfae_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VanishingUnconditional.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/VanishingUnconditional.lean#L146). The attribute's comment: “all three clauses for A^p(X ⟶ Y) itself: the bivariant group read at the canonical Gysin system `Stacks.Chow.gysinSystemOfInvertible`, which is constructed outright, so no Gysin system is assumed”.

> For a bivariant class `c ∈ A^p(X ⟶ Y)` for the canonical Gysin system the following are
> equivalent: `c` is zero; `c ∩ [Y'] = 0` for every integral scheme `Y'` locally of finite type
> over `Y`; and every such `Y'` admits a proper birational `Y'' ⟶ Y'` with `c ∩ [Y''] = 0`.

```lean
theorem BivariantClass.eq_zero_tfae_canonical :
    [c = 0, c.CapsIntegralFundamentalClassesToZero C (gysinSystemOfInvertible C) sX sY f hf p,
      c.HasBirationalModificationCappingToZero C (gysinSystemOfInvertible C)
        sX sY f hf p].TFAE
```

## Tag 0FDZ, a lemma

[Tag 0FDZ](https://stacks.math.columbia.edu/tag/0FDZ) in the Stacks Project.

**`Stacks.Chow.bivariantPieceAssemblyCap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceAssembly/AssembledCap.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceAssembly/AssembledCap.lean#L92). The attribute's comment: “the cap operation assembled from a family of bivariant classes on the pieces”.

> **Stacks 0FDZ.** The cap operation assembled from a family `(c_i)` of bivariant classes of
> degree `p` for the restrictions `f_i : X_i ⟶ Y_{a(i)}`: on a test scheme `g : T ⟶ Y` it sends
> `α ∈ A_k(T)` to the unique class in `A_{k-p}(X ×_Y T)` whose restriction to the `i`-th piece
> `X_i ×_{Y_{a(i)}} T_{a(i)}` is `c_i ∩ α|_{T_{a(i)}}`.
>
> It is well defined because the Chow groups of `X ×_Y T` decompose along those pieces, by
> `Stacks.Chow.chowGroupPullbackPieceEquiv`.

```lean
def bivariantPieceAssemblyCap
    (c : ∀ i, BivariantClass C G ((UX i).ι ≫ sX) ((UY (a i)).ι ≫ sY)
      (pieceMap f UX UY a ha i)
      (pieceMap_comp_pieceStructureMorphism C sX sY f hf UX UY a ha i) p)
    {T : Scheme.{u}} (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ) :
    chowGroup C (g ≫ sY) k →+ chowGroup C (pullback.fst f g ≫ sX) (k - p)
```

**`Stacks.Chow.bivariantPieceRestrictionOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean#L517). The attribute's comment: “the restriction of a bivariant class to a piece, at the Gysin system of the first Chern class rule, with the open-immersion case of Stacks 02TA discharged”.

> **Stacks 0FDZ.** The restriction `c_i` of a bivariant class `c` of degree `p` for `f : X ⟶ Y`
> to the piece `f_i : X_i ⟶ Y_{a(i)}` of a disjoint union decomposition, at the Gysin system of the
> first Chern class rule of an invertible module.
>
> This is `Stacks.Chow.bivariantPieceRestriction` with its Gysin compatibility discharged by
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpenImmersion`, so it assumes nothing.

```lean
def bivariantPieceRestrictionOfInvertible (i : I)
    (c : BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p) :
    BivariantClass C (gysinSystemOfInvertible C) ((UX i).ι ≫ sX) ((UY (a i)).ι ≫ sY)
      (pieceMap f UX UY a ha i)
      (pieceMap_comp_structureMorphism C sX sY f hf UX UY a ha i) p
```

**`Stacks.Chow.bivariantPieceRestrictionHomOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean#L530). The attribute's comment: “the map from A^p(X ⟶ Y) to the product over the pieces, at the Gysin system of the first Chern class rule, with the open-immersion case of Stacks 02TA discharged”.

> **Stacks 0FDZ.** The map `A^p(X ⟶ Y) ⟶ ∏_{i ∈ I} A^p(X_i ⟶ Y_{a(i)})` of the tag at the Gysin
> system of the first Chern class rule of an invertible module, with no Gysin compatibility
> assumed.

```lean
def bivariantPieceRestrictionHomOfInvertible :
    BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p →+
      ∀ i, BivariantClass C (gysinSystemOfInvertible C) ((UX i).ι ≫ sX) ((UY (a i)).ι ≫ sY)
        (pieceMap f UX UY a ha i)
        (pieceMap_comp_structureMorphism C sX sY f hf UX UY a ha i) p
```

**`Stacks.Chow.bivariantPieceEquivOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceGysinSystemOfInvertible.lean#L550). The attribute's comment: “A^p(X ⟶ Y) = ∏_i A^p(X_i ⟶ Y_{a(i)}) at the Gysin system of the first Chern class rule, with all three Gysin compatibilities discharged”.

> **Stacks 0FDZ.** `A^p(X ⟶ Y) = ∏_{i ∈ I} A^p(X_i ⟶ Y_{a(i)})` at the Gysin system of the
> first Chern class rule of an invertible module: a bivariant class of degree `p` for `f : X ⟶ Y`
> is the same thing as a family of bivariant classes of degree `p` for the restrictions
> `f_i : X_i ⟶ Y_{a(i)}`.
>
> This is `Stacks.Chow.bivariantPieceEquiv` with all three of its Gysin compatibilities discharged,
> by `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpenImmersion`,
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpensRestriction` and
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderPullbackComp`. Nothing remains assumed: the
> Gysin system itself carries no hypothesis either.

```lean
def bivariantPieceEquivOfInvertible (hX : IsClopenDecomposition UX) :
    BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p ≃+
      ∀ i, BivariantClass C (gysinSystemOfInvertible C) ((UX i).ι ≫ sX) ((UY (a i)).ι ≫ sY)
        (pieceMap f UX UY a ha i)
        (pieceMap_comp_pieceStructureMorphism C sX sY f hf UX UY a ha i) p
```

**`Stacks.Chow.bivariantPieceRestrictionCap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceRestriction.lean, line 477](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceRestriction.lean#L477). The attribute's comment: “the cap operation of the restriction of a bivariant class to a piece”.

> **Stacks 0FDZ.** The cap operation `c_i ∩ -` of the restriction of a bivariant class `c` of
> degree `p` for `f : X ⟶ Y` to the piece `f_i : X_i ⟶ Y_{a(i)}`: on a test scheme
> `g : T ⟶ Y_{a(i)}` it is the cap operation of `c` at `g ≫ (Y_{a(i)} ⟶ Y)`, restricted along the
> open immersion `X_i ×_{Y_{a(i)}} T ⟶ X ×_Y T`.

```lean
def bivariantPieceRestrictionCap (c : BivariantClass C G sX sY f hf p) {T : Scheme.{u}}
    (g : T ⟶ (UY (a i) : Scheme.{u})) [LocallyOfFiniteType g] (k : ℤ) :
    chowGroup C (g ≫ ((UY (a i)).ι ≫ sY)) k →+
      chowGroup C (pullback.fst (pieceMap f UX UY a ha i) g ≫ ((UX i).ι ≫ sX)) (k - p)
```

**`Stacks.Chow.BivariantClass.eq_of_clopenRestrict_cap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceUniqueness.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantDisjoint/PieceUniqueness.lean#L77). The attribute's comment: “injectivity: a bivariant class is determined by its restrictions to the pieces”.

> **Stacks 0FDZ, injectivity.** Two bivariant classes of degree `p` for `f : X ⟶ Y` are equal as
> soon as, for every test scheme `g : T ⟶ Y` and every `k`, their cap operations agree after
> restriction to each piece `X_i ×_Y T` of `X ×_Y T`.
>
> The pieces of `X ×_Y T` are the preimages of the pieces of `X` under the projection, a
> decomposition into open and closed subschemes by
> `Stacks.Chow.IsClopenDecomposition.preimage`, so restriction to them is jointly injective on
> `CH_{k-p}(X ×_Y T)` by `Stacks.Chow.chowGroupClopenEquiv`.

```lean
theorem BivariantClass.eq_of_clopenRestrict_cap_eq {c d : BivariantClass C G sX sY f hf p}
    (h : ∀ {T : Scheme.{u}} (g : T ⟶ Y) [LocallyOfFiniteType g] (k : ℤ)
      (α : chowGroup C (g ≫ sY) k) (i : I),
      chowGroupRestrict C (pullback.fst f g ≫ sX)
          ((pullback.fst f g ⁻¹ᵁ UX i).ι ≫ (pullback.fst f g ≫ sX))
          (pullback.fst f g ⁻¹ᵁ UX i).ι rfl (k - p) (c.cap g k α) =
        chowGroupRestrict C (pullback.fst f g ≫ sX)
          ((pullback.fst f g ⁻¹ᵁ UX i).ι ≫ (pullback.fst f g ≫ sX))
          (pullback.fst f g ⁻¹ᵁ UX i).ι rfl (k - p) (d.cap g k α)) :
    c = d
```

## Tag 0FE0, a remark

[Tag 0FE0](https://stacks.math.columbia.edu/tag/0FE0) in the Stacks Project.

**`Stacks.Chow.isBivariantClassComposition_bivariantCompositeOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/GysinSystemOfInvertible.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantComposition/GysinSystemOfInvertible.lean#L184). The attribute's comment: “the composite class satisfies the composition formula, at the Gysin system of the first Chern class rule, with both cases of Stacks 02TA discharged”.

> The composite class at the Gysin system of the first Chern class rule is *the* composite: on
> every test scheme its cap operation is cap with `b` followed by cap with `a`, pushed forward along
> the associativity isomorphism of pullbacks.

```lean
theorem isBivariantClassComposition_bivariantCompositeOfInvertible
    (a : BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p)
    (b : BivariantClass C (gysinSystemOfInvertible C) sY sZ g hg q) :
    IsBivariantClassComposition C (gysinSystemOfInvertible C) sX sY sZ f g hf hg
      (properPushforwardDescends C) p q a b
      (bivariantCompositeOfInvertible C sX sY sZ f g hf hg p q a b)
```

**`Stacks.Chow.completedBivariantGroup`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedGroup.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedGroup.lean#L68). The attribute's comment: “completed_bivariant_group”.

> **Stacks 0FE0.** The completed bivariant group `A^*(X ⟶ Y)^∧` of a morphism `f : X ⟶ Y` of
> schemes locally of finite type over the base: the product, over the connected components `X_i`
> of `X`, of the graded groups `A^*(X_i ⟶ Y_{a(i)})` of bivariant classes for the restriction of
> `f` to `X_i` and the connected component of `Y` it lands in. The degree support is finite on
> each component but need not be bounded across components.

```lean
abbrev completedBivariantGroup (C : ChowSituation.{u}) (G : GysinSystem C) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (f : X ⟶ Y) [LocallyOfFiniteType f] (hf : f ≫ sY = sX) : Type (u + 1)
```

**`Stacks.Chow.completedIdentityClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedIdentity.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/CompletedIdentity.lean#L274). The attribute's comment: “the unit 1 of the completed bivariant cohomology ring A^*(X)^∧”.

> The unit `1 ∈ A^*(X)^∧` of the completed bivariant cohomology ring: on the connected
> component `X_i` of `X` it is the restriction of `1 ∈ A^0(X)` to `X_i`, placed in degree `0`. By
> `Stacks.Chow.completedIdentityClass_apply_heq` that restriction is `1 ∈ A^0(X_i)`.

```lean
def completedIdentityClass : completedChowCohomology C (gysinSystemOfInvertible C) sX
```

**`Stacks.Chow.completedBivariantSubgroupOfInvertible`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean#L472). The attribute's comment: “the almost-vanishing tuples inside the product of the bivariant groups, at the Gysin system of the first Chern class rule, with the Gysin compatibility discharged”.

> **Stacks 0FE0.** The subgroup of `∏_p A^p(X ⟶ Y)` the tag describes — the tuples
> `c = (c_0, c_1, c_2, …)` such that for every connected component `X_i` of `X` the image of `c_p`
> in `A^p(X_i ⟶ Y_{a(i)})` vanishes for almost all `p` — at the Gysin system of the first Chern
> class rule of an invertible module.
>
> This is `Stacks.Chow.completedBivariantSubgroup` with the Gysin compatibility it carries
> discharged, by `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpenImmersion`. Nothing remains
> assumed: the Gysin system itself carries no hypothesis either.

```lean
abbrev completedBivariantSubgroupOfInvertible :
    AddSubgroup (∀ p : ℤ, BivariantClass C (gysinSystemOfInvertible C) sX sY f hf p)
```

**`Stacks.Chow.range_completedBivariantSequenceOfInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean#L499). The attribute's comment: “the image of the completed group is the almost-vanishing tuples, at the Gysin system of the first Chern class rule, with all three Gysin compatibilities discharged”.

> **Stacks 0FE0.** The image of `A^*(X ⟶ Y)^∧` in `∏_p A^p(X ⟶ Y)` is exactly the subgroup of
> tuples that vanish in almost all degrees on each connected component, at the Gysin system of the
> first Chern class rule of an invertible module.
>
> This is `Stacks.Chow.range_completedBivariantSequence` with the three Gysin compatibilities of
> Stacks 0FDZ discharged, by `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpenImmersion`,
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpensRestriction` and
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderPullbackComp`. Nothing remains assumed: the
> Gysin system itself carries no hypothesis either.

```lean
theorem range_completedBivariantSequenceOfInvertible :
    (completedBivariantSequenceOfInvertible C sX sY f hf).range =
      completedBivariantSubgroupOfInvertible C sX sY f hf
```

**`Stacks.Chow.completedBivariantGroupEquivOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean, line 517](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean#L517). The attribute's comment: “the completed group is the group of almost-vanishing tuples, at the Gysin system of the first Chern class rule, with all three Gysin compatibilities discharged”.

> **Stacks 0FE0.** The completed bivariant group is the group of almost-vanishing tuples in
> `∏_p A^p(X ⟶ Y)`, at the Gysin system of the first Chern class rule of an invertible module.
>
> This is `Stacks.Chow.completedBivariantGroupEquiv` with the three Gysin compatibilities of Stacks
> 0FDZ discharged, by `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpenImmersion`,
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderOpensRestriction` and
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderPullbackComp`. Nothing remains assumed: the
> Gysin system itself carries no hypothesis either.

```lean
def completedBivariantGroupEquivOfInvertible :
    completedBivariantGroup C (gysinSystemOfInvertible C) sX sY f hf ≃+
      completedBivariantSubgroup C (gysinSystemOfInvertible C) sX sY f hf
        (gysinSystemOfInvertible_isNaturalUnderOpenImmersion C)
```

**`Stacks.Chow.completedBivariantCompositeOfInvertible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean#L636). The attribute's comment: “the composition extended to the completed bivariant groups, at the Gysin system of the first Chern class rule, with both Gysin compatibilities discharged”.

> **Stacks 0FE0.** The composition
> `A^*(X ⟶ Y)^∧ × A^*(Y ⟶ Z)^∧ ⟶ A^*(X ⟶ Z)^∧` extending the composition of Stacks 0B75 to the
> completions, at the Gysin system of the first Chern class rule of an invertible module.
>
> This is `Stacks.Chow.completedBivariantComposite` with both Gysin compatibilities of Stacks 0B75
> discharged, by `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderBaseChangeIso` and
> `Stacks.Chow.gysinSystemOfInvertible_isNaturalUnderPullbackCompPushforward`. Nothing remains
> assumed: the Gysin system itself carries no hypothesis either.

```lean
def completedBivariantCompositeOfInvertible
    (c : completedBivariantGroup C (gysinSystemOfInvertible C) sX sY f hf)
    (d : completedBivariantGroup C (gysinSystemOfInvertible C) sY sZ g hg) :
    completedBivariantGroup C (gysinSystemOfInvertible C) sX sZ (f ≫ g)
      (comp_comp_structureMorphism_eq hf hg)
```

**`Stacks.Chow.completedBivariantCompositeOfInvertible_of_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean, line 653](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean#L653). The attribute's comment: “the composition on the completions extends the composition of homogeneous classes, at the Gysin system of the first Chern class rule, with both Gysin compatibilities discharged”.

> **Stacks 0FE0.** The composition on the completions extends the composition of Stacks 0B75,
> with nothing assumed: at the Gysin system of the first Chern class rule, if `c` is concentrated in
> degree `p` on the component `X_i` and `d` is concentrated in degree `q` on the component
> `Y_{a(i)}`, then the composite is concentrated in degree `p + q` on `X_i` and is there the
> composite bivariant class `Stacks.Chow.bivariantCompositeOfInvertible` of Stacks 0B75.

```lean
theorem completedBivariantCompositeOfInvertible_of_of
    (c : completedBivariantGroup C (gysinSystemOfInvertible C) sX sY f hf)
    (d : completedBivariantGroup C (gysinSystemOfInvertible C) sY sZ g hg)
    (i : ConnectedComponents X) (p q : ℤ) (hc : c i = DirectSum.of _ p (c i p))
    (hd : d (f.continuous.connectedComponentsMap i) =
      DirectSum.of _ q (d (f.continuous.connectedComponentsMap i) q)) :
    completedBivariantCompositeOfInvertible C sX sY sZ f g hf hg c d i =
      DirectSum.of _ (p + q)
        (completedBivariantCompositeTransport C (gysinSystemOfInvertible C) sX sY sZ f g hf hg
          i (p + q)
          (bivariantCompositeOfInvertible C _ _ _ _ _ _ _ p q (c i p)
            (d (f.continuous.connectedComponentsMap i) q)))
```

**`Stacks.Chow.completedChowCohomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean, line 679](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/BivariantLemmas/Completion.lean#L679). The attribute's comment: “the completed bivariant cohomology ring A^*(X)^∧ of a scheme”.

> **Stacks 0FE0.** The *completed bivariant cohomology ring* `A^*(X)^∧ = A^*(X ⟶ X)^∧` of a
> scheme `X` locally of finite type over the base: the completed bivariant group of the identity
> of `X`. Its multiplication is `Stacks.Chow.completedBivariantComposite` at `f = g = 𝟙 X`, and
> `Stacks.Chow.completedBivariantGroupEquiv` reads it as the group of tuples in `∏_p A^p(X)` that
> vanish in almost all degrees on each connected component of `X`.

```lean
abbrev completedChowCohomology (C : ChowSituation.{u}) (G : GysinSystem C) {X : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] : Type (u + 1)
```

## Tag 0GUC, a lemma

[Tag 0GUC](https://stacks.math.columbia.edu/tag/0GUC) in the Stacks Project.

**`Stacks.Chow.existsUnique_bivariantRestriction_eq_of_isEnvelope`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Bivariant/EnvelopeDescentExistence.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Bivariant/EnvelopeDescentExistence.lean#L168).

> **Stacks 0GUC.** Let `f : X ⟶ Y` be a morphism of schemes locally of finite type over the base
> of chapter 42, let `g : Y' ⟶ Y` be an envelope and write `X' = X ×_Y Y'`. Let
> `c' ∈ A^p(X' ⟶ Y')`. If the two restrictions `res₁(c') = res₂(c')` in
> `A^p(X' ×_X X' ⟶ Y' ×_Y Y')` agree, then there is a unique `c ∈ A^p(X ⟶ Y)` whose restriction
> `res(c)` along `g` is `c'`.
>
> Bivariant classes are taken against the Gysin system of the first Chern class of an invertible
> module.

```lean
theorem existsUnique_bivariantRestriction_eq_of_isEnvelope (C : ChowSituation.{u})
    {X Y Y' : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) [LocallyOfFiniteType f] (comm : f ≫ sY = sX)
    (g : Y' ⟶ Y) (envelope : IsEnvelope g) (p : ℤ) :
    letI : IsProper g := envelope.isProper
    ∀ c' : BivariantClass C (gysinSystemOfInvertible C) (pullback.fst f g ≫ sX) (g ≫ sY)
        (pullback.snd f g) (pullbackSnd_comp_structureMorphism_eq C sX sY f comm g) p,
      envelopeDescentRes₁ C (gysinSystemOfInvertible C) sX sY f comm g p
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c' =
        envelopeDescentRes₂ C (gysinSystemOfInvertible C) sX sY f comm g p
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c' →
      ∃! c : BivariantClass C (gysinSystemOfInvertible C) sX sY f comm p,
        bivariantRestriction C (gysinSystemOfInvertible C) sX sY f comm g p
          (gysinSystemOfInvertible_isNaturalUnderBaseChangeIso C) c = c'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.35, Tag 0FDY](https://stacks.math.columbia.edu/tag/0FDY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_canonicalSection_flatPullbackMap, AlgebraicGeometry.Space.chowClassCanonical_firstChernCapCycleMap_canonicalSection_flatPullbackMap, AlgebraicGeometry.Space.chowClassCanonical_flatPullbackMap_canonicalSection_eq_zero_of_hasRelativeDimension_zero
statement: formalized
proof: formalized
---

# 82.24 Relative effective Cartier divisors

Section 82.24 of the Stacks Project, [Tag 0ERD](https://stacks.math.columbia.edu/tag/0ERD). 1 tag here is carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ERE, a lemma

[Tag 0ERE](https://stacks.math.columbia.edu/tag/0ERE) in the Stacks Project.

**`AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_canonicalSection_flatPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RelativeEffectiveCartierFlatPullback.lean, line 649](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RelativeEffectiveCartierFlatPullback.lean#L649). The attribute's comment: “first identity: i^* p^* α = (p|\_D)^* α in CH\_\{k+r}(D), on cycles: i^* is the refined Gysin map of Stacks 0ER1 for (O\_X(D), 1\_D) (gysinCycleMap at sectionGysinRule), p^* and (p|\_D)^* the flat pullbacks of Stacks 0EP8, the classes taken in the Chow group of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK (chowGroupCanonical); the identity holds already in Z(D)”.

> **Stacks 0ERE, first identity.** In Situation 0EDT let `X, Y/B` be good, let `p : X ⟶ Y` be
> flat of relative dimension `r + 1` and let `i : D → X` be a relative effective Cartier divisor on
> `X/Y` (Stacks 0EPP), with `ℒ = 𝒪_X(D)` and its canonical section `1_D` (Stacks 0841), whose
> vanishing locus `Z(1_D)` is `D` (Stacks 0847). Then for every `(k+1)`-cycle `α` on `Y`
>
> `i^* p^* α = (p|_D)^* α` in `CH_{k+r+1}(D)`,
>
> where `p^*` is the flat pullback of cycles of Stacks 0EP8
> (`AlgebraicGeometry.Space.flatPullbackMap`), `i^*` the refined Gysin map of Stacks 0ER1 for the
> pair `(𝒪_X(D), 1_D)` on cycles (`AlgebraicGeometry.Space.gysinCycleMap` at
> `AlgebraicGeometry.Space.sectionGysinRule`), and `(p|_D)^*` the flat pullback along
> `p|_D : D → Y`, which is flat of relative dimension `r`; the classes are taken in `CH_{k+r+1}(D)`
> of Stacks 0EQ6, `AlgebraicGeometry.Space.chowGroupCanonical`. The identity holds already on
> cycles, `AlgebraicGeometry.Space.gysinCycleMap_sectionGysinRule_flatPullbackMap`.

```lean
theorem chowClassCanonical_gysinCycleMap_canonicalSection_flatPullbackMap (k : ℤ)
    (α : CycleGroup D sY (k + 1)) :
    chowClassCanonical.{v} D (_ ≫ sX) (isGood_vanishingLocus D sX hX _ _) (k + r + 1)
        (gysinCycleMap D sX (vanishingLocus D sX hX
            (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1)
            (canonicalSection D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1))
          (isGood_vanishingLocus D sX hX _ _) (k + r + 1)
          (sectionGysinRule D sX hX _ _ (k + r + 1)
            (associatedInvertibleSheaf_isInvertible D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1))
          (flatPullbackMap D sX hX sY hY p hbase (r + 1) hflat hr (k + 1) (k + r + 1 + 1)
            (by push_cast; ring) α)) =
      chowClassCanonical.{v} D (_ ≫ sX) (isGood_vanishingLocus D sX hX _ _) (k + r + 1)
        (flatPullbackMap D (_ ≫ sX) (isGood_vanishingLocus D sX hX _ _) sY hY (_ ≫ p)
          (comp_structureMorphism_eq D _ sX sY _ p rfl hbase) r
          (isRelativeEffectiveCartierDivisor_vanishingLocus_canonicalSection D sX hX sY hY p Dv
            hDv).2
          (hasRelativeDimension_ι_comp D sX hX sY hY p hbase r hr _
            (isRelativeEffectiveCartierDivisor_vanishingLocus_canonicalSection D sX hX sY hY p Dv
              hDv)) (k + 1) (k + r + 1) (by ring) α)
```

**`AlgebraicGeometry.Space.chowClassCanonical_firstChernCapCycleMap_canonicalSection_flatPullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RelativeEffectiveCartierFlatPullback.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RelativeEffectiveCartierFlatPullback.lean#L688). The attribute's comment: “second identity: c₁(O\_X(D)) ∩ p^* α = i\_*((p|\_D)^* α) in CH\_\{k+r}(X), on cycles: c₁ ∩ - is the cap product of Stacks 0EQJ at the canonical choices, p^* and (p|\_D)^* the flat pullbacks of Stacks 0EP8, i\_* the pushforward along the closed immersion, the classes taken in the Chow group of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK (chowGroupCanonical)”.

> **Stacks 0ERE, second identity.** In the situation of
> `AlgebraicGeometry.Space.chowClassCanonical_gysinCycleMap_canonicalSection_flatPullbackMap`, for
> every `(k+1)`-cycle `α` on `Y`
>
> `c₁(𝒪_X(D)) ∩ p^* α = i_* ((p|_D)^* α)` in `CH_{k+r+1}(X)`,
>
> where `c₁(𝒪_X(D)) ∩ -` is the cycle-level cap product of Stacks 0EQJ at the canonical choices
> (`AlgebraicGeometry.Space.firstChernCapCycleMap` at
> `AlgebraicGeometry.Space.canonicalFirstChernRule`), `i_*` the pushforward of cycles along the
> closed immersion `i : D → X`, and the classes are taken in `CH_{k+r+1}(X)` of Stacks 0EQ6,
> `AlgebraicGeometry.Space.chowGroupCanonical`. It follows from the first identity and Stacks
> 0ER4.

```lean
theorem chowClassCanonical_firstChernCapCycleMap_canonicalSection_flatPullbackMap (k : ℤ)
    (α : CycleGroup D sY (k + 1)) :
    chowClassCanonical.{max (u + 1) v} D sX hX (k + r + 1)
        (firstChernCapCycleMap D sX hX (k + r + 1)
          (canonicalFirstChernRule D sX hX
            (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1)
            (Stacks.SheafOfModules.IsInvertible.ofAlgebraicGeometry _ _ _
              (associatedInvertibleSheaf_isInvertible D.site D.base D.base_mem ⟨X, hX.1⟩ Dv
                hDv.1)) (k + r + 1))
          (flatPullbackMap D sX hX sY hY p hbase (r + 1) hflat hr (k + 1) (k + r + 1 + 1)
            (by push_cast; ring) α)) =
      chowClassCanonical.{max (u + 1) v} D sX hX (k + r + 1)
        (closedSubspaceCyclePushforward D sX hX (vanishingLocus D sX hX
            (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1)
            (canonicalSection D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1)) (k + r + 1)
          (flatPullbackMap D (_ ≫ sX) (isGood_vanishingLocus D sX hX _ _) sY hY (_ ≫ p)
            (comp_structureMorphism_eq D _ sX sY _ p rfl hbase) r
            (isRelativeEffectiveCartierDivisor_vanishingLocus_canonicalSection D sX hX sY hY p Dv
              hDv).2
            (hasRelativeDimension_ι_comp D sX hX sY hY p hbase r hr _
              (isRelativeEffectiveCartierDivisor_vanishingLocus_canonicalSection D sX hX sY hY p
                Dv hDv)) (k + 1) (k + r + 1) (by ring) α))
```

**`AlgebraicGeometry.Space.chowClassCanonical_flatPullbackMap_canonicalSection_eq_zero_of_hasRelativeDimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/RelativeEffectiveCartierFlatPullback.lean, line 805](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/RelativeEffectiveCartierFlatPullback.lean#L805). The attribute's comment: “the case of relative dimension r = 0, where D is empty: every cycle on D is zero, and i^* p^* α = 0 in CH\_k(D) and c₁(O\_X(D)) ∩ p^* α = 0 in CH\_k(X), on cycles, the classes taken in the Chow groups of Stacks 0EQ6 at the canonical embeddings of Stacks 0ENK (chowGroupCanonical)”.

> **Stacks 0ERE in relative dimension zero.** If `p : X ⟶ Y` is flat of relative dimension `0`
> and `i : D → X` is a relative effective Cartier divisor on `X/Y`, then `D` has no points
> (`AlgebraicGeometry.Space.isEmpty_points_of_isRelativeEffectiveCartierDivisor`), so every cycle on
> `D` is zero, and for every `(k+1)`-cycle `α` on `Y` both sides of the two identities of Stacks
> 0ERE vanish: `i^* p^* α = 0` in `CH_k(D)` and `c₁(𝒪_X(D)) ∩ p^* α = i_*(0) = 0` in `CH_k(X)`, the
> operations being those on cycles and the classes taken in the Chow groups of Stacks 0EQ6,
> `AlgebraicGeometry.Space.chowGroupCanonical`.

```lean
theorem chowClassCanonical_flatPullbackMap_canonicalSection_eq_zero_of_hasRelativeDimension_zero
    (Dv : ClosedSubspaces D.site D.base D.base_mem X)
    (hDv : IsRelativeEffectiveCartierDivisor D.site D.base D.base_mem
      (ObjectProperty.homMk p : (⟨X, hX.1⟩ : AlgebraicSpaces D.site D.base D.base_mem) ⟶
        ⟨Y, hY.1⟩) Dv) (k : ℤ) (α : CycleGroup D sY (k + 1)) :
    (∀ (n : ℤ) (β : CycleGroup D ((vanishingLocus D sX hX
        (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1)
        (canonicalSection D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1)).1.ι ≫ sX) n), β = 0) ∧
    chowClassCanonical.{v} D (_ ≫ sX) (isGood_vanishingLocus D sX hX _ _) k
        (gysinCycleMap D sX (vanishingLocus D sX hX
            (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1)
            (canonicalSection D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1))
          (isGood_vanishingLocus D sX hX _ _) k
          (sectionGysinRule D sX hX _ _ k
            (associatedInvertibleSheaf_isInvertible D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1))
          (flatPullbackMap D sX hX sY hY p hbase 0 hflat hr₀ (k + 1) (k + 1) (by simp) α)) = 0 ∧
    chowClassCanonical.{max (u + 1) v} D sX hX k
        (firstChernCapCycleMap D sX hX k
          (canonicalFirstChernRule D sX hX
            (associatedInvertibleSheaf D.site D.base D.base_mem ⟨X, hX.1⟩ Dv hDv.1)
            (Stacks.SheafOfModules.IsInvertible.ofAlgebraicGeometry _ _ _
              (associatedInvertibleSheaf_isInvertible D.site D.base D.base_mem ⟨X, hX.1⟩ Dv
                hDv.1)) k)
          (flatPullbackMap D sX hX sY hY p hbase 0 hflat hr₀ (k + 1) (k + 1) (by simp) α)) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.24, Tag 0ERD](https://stacks.math.columbia.edu/tag/0ERD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

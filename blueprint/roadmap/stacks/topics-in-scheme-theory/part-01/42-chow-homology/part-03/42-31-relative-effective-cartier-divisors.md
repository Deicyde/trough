---
declaration: section
origin: cited
lean: Stacks.Chow.gysinChowOfInvertible_canonicalSection_flatPullbackChow, Stacks.Chow.firstChernClassCapChow_divisorSheaf_flatPullbackChow, Stacks.Chow.gysinChowOfInvertible_canonicalSection_flatPullbackChow_of_relativeDimension_zero, Stacks.Chow.firstChernClassCapChow_divisorSheaf_flatPullbackChow_of_relativeDimension_zero, Stacks.Chow.gysinHomomorphismOfInvertible_flatPullback_primeCycle, Stacks.Chow.effectiveCartierIntersectionOfInvertible_flatPullback_primeCycle, Stacks.Chow.firstChernClassCapOfInvertible_flatPullback_primeCycle, Stacks.Chow.gysinChowOfInvertible_flatPullbackChow
statement: formalized
proof: formalized
---

# 42.31 Relative effective Cartier divisors

Section 42.31 of the Stacks Project, [Tag 02TP](https://stacks.math.columbia.edu/tag/02TP). 1 tag here is carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02TR, a lemma

[Tag 02TR](https://stacks.math.columbia.edu/tag/02TR) in the Stacks Project.

**`Stacks.Chow.gysinChowOfInvertible_canonicalSection_flatPullbackChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierChow.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierChow.lean#L190). The attribute's comment: “first equality i^* p^* α = (p|\_D)^* α, for p of relative dimension r + 1 (relative dimension 0 is `gysinChowOfInvertible_canonicalSection_flatPullbackChow_of_relativeDimension_zero`)”.

> **Stacks 02TR, first equality.** Let `p : X ⟶ Y` be flat of relative dimension `r + 1`
> between schemes locally of finite type over the base, let `i : D ⟶ X` be a relative effective
> Cartier divisor on `X/Y` and let `i^*` be the Gysin map of the canonical section of `𝒪_X(D)`,
> whose zero scheme is `D` (Stacks 01X0). Then `p|_D` is flat of relative dimension `r` and
>
>   `i^* p^* α = (p|_D)^* α`  in  `CH_{k+1+r}(D)`  for every  `α ∈ CH_{k+1}(Y)`.

```lean
theorem gysinChowOfInvertible_canonicalSection_flatPullbackChow (r : ℕ)
    (hp : AlgebraicGeometry.RelativeDimension p (r + 1)) (α : chowGroup C sY (k + 1)) :
    haveI : Stacks.Divisors.IsEffectiveCartierDivisor D := hD.1
    haveI : Flat (D.subschemeι ≫ p) := hD.2
    zeroScheme_divisorSheafGlobalSection D ▸
      gysinChowOfInvertible C sX (k + 1 + (r : ℤ)) (Stacks.Divisors.divisorSheaf D)
        (Stacks.Divisors.divisorSheafGlobalSection D)
        (chowGroupCast C sX (degree_flatPullback_succ k r)
          (flatPullbackChowOfRelativeDimension C sX sY p hbase (r + 1) hp (k + 1) α)) =
      flatPullbackChowOfRelativeDimension C (D.subschemeι ≫ sX) sY (D.subschemeι ≫ p)
        (by rw [Category.assoc, hbase]) r
        (Stacks.Divisors.relativeDimension_subschemeι_comp_of_isRelativeEffectiveCartierDivisor
          p r hp D hD) (k + 1) α
```

**`Stacks.Chow.firstChernClassCapChow_divisorSheaf_flatPullbackChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierChow.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierChow.lean#L238). The attribute's comment: “second equality c\_1(O\_X(D)) ∩ p^* α = i\_*((p|\_D)^* α), for p of relative dimension r + 1 (relative dimension 0 is `firstChernClassCapChow_divisorSheaf_flatPullbackChow_of_relativeDimension_zero`)”.

> **Stacks 02TR, second equality.** In the situation of
> `Stacks.Chow.gysinChowOfInvertible_canonicalSection_flatPullbackChow`, with `ℒ = 𝒪_X(D)`,
>
>   `c₁(ℒ) ∩ p^* α = i_*((p|_D)^* α)`  in  `CH_{k+1+r}(X)`  for every  `α ∈ CH_{k+1}(Y)`.

```lean
theorem firstChernClassCapChow_divisorSheaf_flatPullbackChow (r : ℕ)
    (hp : AlgebraicGeometry.RelativeDimension p (r + 1)) (α : chowGroup C sY (k + 1)) :
    haveI : Stacks.Divisors.IsEffectiveCartierDivisor D := hD.1
    haveI : Flat (D.subschemeι ≫ p) := hD.2
    firstChernClassCapChow C (k + 1 + (r : ℤ)) sX (Stacks.Divisors.divisorSheaf D)
        (chowGroupCast C sX (degree_flatPullback_succ k r)
          (flatPullbackChowOfRelativeDimension C sX sY p hbase (r + 1) hp (k + 1) α)) =
      properChowPushforward C (D.subschemeι ≫ sX) sX D.subschemeι rfl (k + 1 + (r : ℤ))
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper C _ sX _ rfl _)
        (flatPullbackChowOfRelativeDimension C (D.subschemeι ≫ sX) sY (D.subschemeι ≫ p)
          (by rw [Category.assoc, hbase]) r
          (Stacks.Divisors.relativeDimension_subschemeι_comp_of_isRelativeEffectiveCartierDivisor
            p r hp D hD) (k + 1) α)
```

**`Stacks.Chow.gysinChowOfInvertible_canonicalSection_flatPullbackChow_of_relativeDimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierChow.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierChow.lean#L272). The attribute's comment: “first equality, for p of relative dimension 0: D is empty, so CH\_k(D) = 0 and i^* p^* α = 0”.

> **Stacks 02TR in relative dimension zero, first equality.** If `p` has relative dimension `0`
> then a relative effective Cartier divisor `D` on `X/Y` is empty, so `CH_k(D) = 0` and
> `i^* p^* α = 0` for every `α ∈ CH_{k+1}(Y)`.

```lean
theorem gysinChowOfInvertible_canonicalSection_flatPullbackChow_of_relativeDimension_zero
    (hp : AlgebraicGeometry.RelativeDimension p 0) (α : chowGroup C sY (k + 1)) :
    haveI : Stacks.Divisors.IsEffectiveCartierDivisor D := hD.1
    (zeroScheme_divisorSheafGlobalSection D ▸
      gysinChowOfInvertible C sX k (Stacks.Divisors.divisorSheaf D)
        (Stacks.Divisors.divisorSheafGlobalSection D)
        (chowGroupCast C sX (show k + 1 + ((0 : ℕ) : ℤ) = k + 1 by simp)
          (flatPullbackChowOfRelativeDimension C sX sY p hbase 0 hp (k + 1) α)) :
        chowGroup C (D.subschemeι ≫ sX) k) = 0
```

**`Stacks.Chow.firstChernClassCapChow_divisorSheaf_flatPullbackChow_of_relativeDimension_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierChow.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierChow.lean#L289). The attribute's comment: “second equality, for p of relative dimension 0: D is empty, so c\_1(O\_X(D)) ∩ p^* α = i\_*(0) = 0”.

> **Stacks 02TR in relative dimension zero, second equality.** If `p` has relative dimension `0`
> then a relative effective Cartier divisor `D` on `X/Y` is empty, so `i_*((p|_D)^* α) = 0` and
> `c₁(𝒪_X(D)) ∩ p^* α = 0` for every `α ∈ CH_{k+1}(Y)`.

```lean
theorem firstChernClassCapChow_divisorSheaf_flatPullbackChow_of_relativeDimension_zero
    (hp : AlgebraicGeometry.RelativeDimension p 0) (α : chowGroup C sY (k + 1)) :
    haveI : Stacks.Divisors.IsEffectiveCartierDivisor D := hD.1
    firstChernClassCapChow C k sX (Stacks.Divisors.divisorSheaf D)
        (chowGroupCast C sX (show k + 1 + ((0 : ℕ) : ℤ) = k + 1 by simp)
          (flatPullbackChowOfRelativeDimension C sX sY p hbase 0 hp (k + 1) α)) = 0
```

**`Stacks.Chow.gysinHomomorphismOfInvertible_flatPullback_primeCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullback.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullback.lean#L179). The attribute's comment: “first equality, on the fundamental cycle of an integral closed subscheme”.

> **Stacks 02TR, first equality, on an integral component.** Let `p : X ⟶ Y` be flat of
> relative dimension `r + 1` over the base scheme of chapter 42, let `i : D ⟶ X` be a relative
> effective Cartier divisor on `X/Y` presented as the zero scheme of a section `s` of an invertible
> module `L`, and let `W ⊆ Y` be an integral closed subscheme of delta-dimension `k + 1`. Then
>
>   `i^* p^* [W]_{k+1} = (p|_D)^* [W]_{k+1}`  in  `A_{k+1+r}(D)`.
>
> The relative dimension `hq` of `D ⟶ Y` is a parameter; see the implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.RelativeEffectiveCartierFlatPullback`. The flatness of
> `D ⟶ Y` is both the second conjunct of `hD` and an instance binder, because stating
> `(p|_D)^*` needs it before `hD` is available.

```lean
theorem gysinHomomorphismOfInvertible_flatPullback_primeCycle
    (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (p : X ⟶ Y) [LocallyOfFiniteType p] [Flat p] (hbase : p ≫ sY = sX) (r : ℕ)
    (hp : AlgebraicGeometry.RelativeDimension p (r + 1)) (k : ℤ) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : L.sections)
    [Flat ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)]
    (hD : Stacks.Divisors.IsRelativeEffectiveCartierDivisor p
      (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))))
    (hq : AlgebraicGeometry.RelativeDimension
      ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p) r)
    (W : Y.IdealSheafData) (hWint : IsIntegral W.subscheme)
    (hWdim : schemeDeltaDimension C (W.subschemeι ≫ sY) = ((k + 1 : ℤ) : EInt))
    (hcast : k + 1 + ((r + 1 : ℕ) : ℤ) = k + 1 + (r : ℤ) + 1) :
    gysinHomomorphismOfInvertible C sX (k + 1 + (r : ℤ)) L (s.eval (.op ⊤))
        (hcast ▸ flatPullback C sX sY p hbase (r + 1) hp (k + 1)
          (cycleAssociatedToClosedSubscheme C sY W.subschemeι (k + 1))) =
      QuotientAddGroup.mk
        (flatPullback C
          ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sY
          ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)
          (by rw [Category.assoc, hbase]) r hq (k + 1)
          (cycleAssociatedToClosedSubscheme C sY W.subschemeι (k + 1)))
```

**`Stacks.Chow.effectiveCartierIntersectionOfInvertible_flatPullback_primeCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullback.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullback.lean#L242). The attribute's comment: “second equality, as intersection with D, on a fundamental cycle”.

> **Stacks 02TR, second equality, on an integral component, as intersection with `D`.** In the
> situation of `Stacks.Chow.gysinHomomorphismOfInvertible_flatPullback_primeCycle`,
>
>   `D · p^* [W]_{k+1} = i_* ((p|_D)^* [W]_{k+1})`  in  `A_{k+1+r}(X)`,
>
> where `D · −` is intersection with the effective Cartier divisor `D` (Stacks 02T8). The source
> writes the left side as `c₁(ℒ) ∩ p^* α`; that form is
> `Stacks.Chow.firstChernClassCapOfInvertible_flatPullback_primeCycle` below, one rewrite of this
> through Stacks 02T9.

```lean
theorem effectiveCartierIntersectionOfInvertible_flatPullback_primeCycle
    (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (p : X ⟶ Y) [LocallyOfFiniteType p] [Flat p] (hbase : p ≫ sY = sX) (r : ℕ)
    (hp : AlgebraicGeometry.RelativeDimension p (r + 1)) (k : ℤ) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : L.sections)
    [Flat ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)]
    (hD : Stacks.Divisors.IsRelativeEffectiveCartierDivisor p
      (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))))
    (hq : AlgebraicGeometry.RelativeDimension
      ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p) r)
    (W : Y.IdealSheafData) (hWint : IsIntegral W.subscheme)
    (hWdim : schemeDeltaDimension C (W.subschemeι ≫ sY) = ((k + 1 : ℤ) : EInt))
    (hcast : k + 1 + ((r + 1 : ℕ) : ℤ) = k + 1 + (r : ℤ) + 1) :
    effectiveCartierIntersectionOfInvertible C sX (k + 1 + (r : ℤ)) L (s.eval (.op ⊤)) hD.1
        (hcast ▸ flatPullback C sX sY p hbase (r + 1) hp (k + 1)
          (cycleAssociatedToClosedSubscheme C sY W.subschemeι (k + 1))) =
      properChowPushforward C
        ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sX
        (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι rfl (k + 1 + (r : ℤ))
        (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
          (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι C
          ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sX rfl
          (k + 1 + (r : ℤ)))
        (QuotientAddGroup.mk
          (flatPullback C
            ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sY
            ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)
            (by rw [Category.assoc, hbase]) r hq (k + 1)
            (cycleAssociatedToClosedSubscheme C sY W.subschemeι (k + 1))))
```

**`Stacks.Chow.firstChernClassCapOfInvertible_flatPullback_primeCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullback.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullback.lean#L290). The attribute's comment: “second equality, in the c₁(L) ∩ − form, on a fundamental cycle”.

> **Stacks 02TR, second equality, on an integral component.** In the situation of
> `Stacks.Chow.gysinHomomorphismOfInvertible_flatPullback_primeCycle`,
>
>   `c₁(L) ∩ p^* [W]_{k+1} = i_* ((p|_D)^* [W]_{k+1})`  in  `A_{k+1+r}(X)`,
>
> the source's second equality: the left side is the cap product of Stacks 02SO and `L` is
> canonically `𝒪_X(D)`, the divisor being the zero scheme of `s`.
>
> This is `Stacks.Chow.effectiveCartierIntersectionOfInvertible_flatPullback_primeCycle` read
> through Stacks 02T9, in the form
> `Stacks.Chow.effectiveCartierIntersectionOfInvertible_eq_firstChernClassCapOfInvertible`.

```lean
theorem firstChernClassCapOfInvertible_flatPullback_primeCycle
    (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (p : X ⟶ Y) [LocallyOfFiniteType p] [Flat p] (hbase : p ≫ sY = sX) (r : ℕ)
    (hp : AlgebraicGeometry.RelativeDimension p (r + 1)) (k : ℤ) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : L.sections)
    [Flat ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)]
    (hD : Stacks.Divisors.IsRelativeEffectiveCartierDivisor p
      (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))))
    (hq : AlgebraicGeometry.RelativeDimension
      ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p) r)
    (W : Y.IdealSheafData) (hWint : IsIntegral W.subscheme)
    (hWdim : schemeDeltaDimension C (W.subschemeι ≫ sY) = ((k + 1 : ℤ) : EInt))
    (hcast : k + 1 + ((r + 1 : ℕ) : ℤ) = k + 1 + (r : ℤ) + 1) :
    firstChernClassCapOfInvertible C sX (k + 1 + (r : ℤ)) L
        (hcast ▸ flatPullback C sX sY p hbase (r + 1) hp (k + 1)
          (cycleAssociatedToClosedSubscheme C sY W.subschemeι (k + 1))) =
      properChowPushforward C
        ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sX
        (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι rfl (k + 1 + (r : ℤ))
        (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
          (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι C
          ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sX rfl
          (k + 1 + (r : ℤ)))
        (QuotientAddGroup.mk
          (flatPullback C
            ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sY
            ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)
            (by rw [Category.assoc, hbase]) r hq (k + 1)
            (cycleAssociatedToClosedSubscheme C sY W.subschemeι (k + 1))))
```

**`Stacks.Chow.gysinChowOfInvertible_flatPullbackChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullbackChow.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullbackChow.lean#L332). The attribute's comment: “first equality, for an arbitrary class in A\_\{k+1}(Y)”.

> Let `p : X ⟶ Y` be flat of relative dimension `r + 1` over
> the base scheme of chapter 42 and let `i : D ⟶ X` be a relative effective Cartier divisor on
> `X/Y`, presented as the zero scheme of a section `s` of an invertible module `L`. Then for every
> class `α ∈ A_{k+1}(Y)`
>
>   `i^* p^* α = (p|_D)^* α`  in  `A_{k+r}(D)`,
>
> for the Gysin pullback of Stacks 02TO and the flat pullbacks of Stacks 02S1 on Chow groups, `p|_D`
> having relative dimension `r` by
> `AlgebraicGeometry.relativeDimension_of_isRelativeEffectiveCartierDivisor`.

```lean
theorem gysinChowOfInvertible_flatPullbackChow (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (p : X ⟶ Y) [LocallyOfFiniteType p] [Flat p] (hbase : p ≫ sY = sX) (r : ℕ)
    (hp : AlgebraicGeometry.RelativeDimension p (r + 1)) (k : ℤ) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : L.sections)
    [Flat ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)]
    (hD : Stacks.Divisors.IsRelativeEffectiveCartierDivisor p
      (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))))
    (hcast : k + 1 + ((r + 1 : ℕ) : ℤ) = k + 1 + (r : ℤ) + 1)
    (α : chowGroup C sY (k + 1)) :
    gysinChowOfInvertible C sX (k + 1 + (r : ℤ)) L (s.eval (.op ⊤))
        (hcast ▸ flatPullbackChowOfRelativeDimension C sX sY p hbase (r + 1) hp (k + 1) α) =
      flatPullbackChowOfRelativeDimension C
        ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sY
        ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)
        (by rw [Category.assoc, hbase]) r
        (AlgebraicGeometry.relativeDimension_of_isRelativeEffectiveCartierDivisor p r hp
          (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))) hD) (k + 1) α
```

**`Stacks.Chow.firstChernClassCapChow_flatPullbackChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullbackChow.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RelativeEffectiveCartierFlatPullbackChow.lean#L405). The attribute's comment: “second equality, for an arbitrary class in A\_\{k+1}(Y)”.

> In the situation of
> `Stacks.Chow.gysinChowOfInvertible_flatPullbackChow`, for every class `α ∈ A_{k+1}(Y)`
>
>   `c₁(L) ∩ p^* α = i_* ((p|_D)^* α)`  in  `A_{k+r}(X)`,
>
> the cap product being the descended operation of Stacks 02TI, with `D` the zero scheme of `s`, so
> that `L` is `𝒪_X(D)`.

```lean
theorem firstChernClassCapChow_flatPullbackChow (C : ChowSituation.{u}) {X Y : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (p : X ⟶ Y) [LocallyOfFiniteType p] [Flat p] (hbase : p ≫ sY = sX) (r : ℕ)
    (hp : AlgebraicGeometry.RelativeDimension p (r + 1)) (k : ℤ) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : L.sections)
    [Flat ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)]
    (hD : Stacks.Divisors.IsRelativeEffectiveCartierDivisor p
      (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))))
    (hcast : k + 1 + ((r + 1 : ℕ) : ℤ) = k + 1 + (r : ℤ) + 1)
    (α : chowGroup C sY (k + 1)) :
    firstChernClassCapChow C (k + 1 + (r : ℤ)) sX L
        (hcast ▸ flatPullbackChowOfRelativeDimension C sX sY p hbase (r + 1) hp (k + 1) α) =
      properChowPushforward C
        ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sX
        (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι rfl (k + 1 + (r : ℤ))
        (properPushforwardFactorsThroughRationalEquivalence_of_isClosedImmersion
          (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι C
          ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sX rfl
          (k + 1 + (r : ℤ)))
        (flatPullbackChowOfRelativeDimension C
          ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ sX) sY
          ((Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))).subschemeι ≫ p)
          (by rw [Category.assoc, hbase]) r
          (AlgebraicGeometry.relativeDimension_of_isRelativeEffectiveCartierDivisor p r hp
            (Stacks.Divisors.zeroScheme X L (s.eval (.op ⊤))) hD) (k + 1) α)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.31, Tag 02TP](https://stacks.math.columbia.edu/tag/02TP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: Stacks.Chow.firstChernClassCapFundamental, Stacks.Chow.firstChernClassCapFundamental_eq, Stacks.Chow.divisorOfMeromorphicSection, Stacks.ChernCap42.divisorOfMeromorphicSectionCycle_eq_cycleAssociatedToZeroScheme, Stacks.ChernCap42.firstChernClassCapOfInvertible_fundamentalCycle, Stacks.Chow.mk_flatPullback_meromorphicDivisorCycle
statement: formalized
proof: formalized
---

# 42.24 The divisor associated to an invertible sheaf

Section 42.24 of the Stacks Project, [Tag 02SI](https://stacks.math.columbia.edu/tag/02SI). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02SJ, a definition

[Tag 02SJ](https://stacks.math.columbia.edu/tag/02SJ) in the Stacks Project.

**`Stacks.Chow.firstChernClassCapFundamental`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DivisorOfInvertibleSheaf.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DivisorOfInvertibleSheaf.lean#L90). The attribute's comment: “part (2): the Weil divisor class c₁(L) ∩ [X] in CH_{n-1}(X)”. References: SGA 5 VII (3.9), “partial”.

> **The Weil divisor class of an invertible module, Stacks 02SJ (2).** On an integral scheme `X`
> of delta-dimension `n`, locally of finite type over the base of a Chow situation, the class
>
>   `c₁(L) ∩ [X] ∈ CH_{n-1}(X)`
>
> of the divisor of zeros and poles of a nonzero meromorphic section of `L`.
>
> An invertible module on an integral scheme has a regular meromorphic section with nonzero generic
> value (`Stacks.ChernCap42.exists_isRegularMeromorphicSection_of_isIntegral`), and the class of its
> divisor cycle does not depend on which one is taken; the characterizing equality is
> `Stacks.Chow.firstChernClassCapFundamental_eq`, which should be used in place of this
> definition.

```lean
def firstChernClassCapFundamental : chowGroup C p (n - 1)
```

**`Stacks.Chow.firstChernClassCapFundamental_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/DivisorOfInvertibleSheaf.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/DivisorOfInvertibleSheaf.lean#L106). The attribute's comment: “part (2): c₁(L) ∩ [X] is the class of div_L(s) for every nonzero regular meromorphic section s, so the definition does not depend on the chosen section”.

> **The Weil divisor class is the class of `div_L(s)` for every nonzero section,
> Stacks 02SJ (2).** In `CH_{n-1}(X)` the class `c₁(L) ∩ [X]` is represented by the divisor cycle
> of *any* nonzero regular meromorphic section of `L`, not only by the one
> `Stacks.Chow.firstChernClassCapFundamental` chose. This is the well-definedness the source asserts.
>
> The source's nonvanishing of `s` is not assumed: on an integral scheme it follows from
> regularity, by `Stacks.Divisors.genericValue_ne_zero_of_isRegularMeromorphicSection`. See the
> implementation notes of
> `StacksFrontier.AlgebraicGeometry.Chow.DivisorOfInvertibleSheaf`.

```lean
theorem firstChernClassCapFundamental_eq
    (s : AlgebraicGeometry.MeromorphicSection X.sheaf L)
    (hs : AlgebraicGeometry.IsRegularMeromorphicSection X.sheaf L s) :
    firstChernClassCapFundamental C p n hn L =
      QuotientAddGroup.mk (divisorOfMeromorphicSectionCycle C p n hn L s hs)
```

**`Stacks.Chow.divisorOfMeromorphicSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/MeromorphicCascade/DivisorCycle.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/MeromorphicCascade/DivisorCycle.lean#L88). The attribute's comment: “part (1): div_L(s) = ∑_Z ord_{Z, L}(s) [Z] as an element of Z_{n-1}(X), together with its coefficients”.

> **The divisor cycle of a regular meromorphic section, Stacks 02SJ (1).** The Weil divisor
> `div_L(s)` of a regular meromorphic section of an invertible module on an integral scheme of
> delta-dimension `n`, read as a cycle of delta-dimension `n - 1`, together with its coefficient
> specification.
>
> The coefficient at the generic point of a prime divisor `Z` is the order of vanishing
> `ord_{Z, L}(s)` of Stacks 02SF, and the coefficient at a point which is no prime divisor's generic
> point is zero; those are the two components of the subtype obligation, and they are available as
> `Stacks.Chow.divisorOfMeromorphicSectionCycle_genericPoint` and
> `Stacks.Chow.divisorOfMeromorphicSectionCycle_eq_zero`.

```lean
def divisorOfMeromorphicSection (C : ChowSituation.{u}) {X : Scheme.{u}} (p : X ⟶ C.S)
    [LocallyOfFiniteType p] [IsIntegral X] (n : ℤ)
    (hn : schemeDeltaDimension C p = (n : EInt)) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : AlgebraicGeometry.MeromorphicSection X.sheaf L)
    (hs : AlgebraicGeometry.IsRegularMeromorphicSection X.sheaf L s) :
    { c : CycleGroup C p (n - 1) // IsDivisorOfMeromorphicSectionCycle C p n L s hs c }
```

## Tag 02SK, a lemma

[Tag 02SK](https://stacks.math.columbia.edu/tag/02SK) in the Stacks Project.

**`Stacks.ChernCap42.divisorOfMeromorphicSectionCycle_eq_cycleAssociatedToZeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCap42/DivisorOfSectionCycle.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCap42/DivisorOfSectionCycle.lean#L279). The attribute's comment: “divisor cycle”.

> Let `X` be an integral scheme locally of finite type over the base of
> chapter 42, of delta-dimension `n`, let `L` be an invertible `𝒪_X`-module and let `s` be a nonzero
> global section of `L`. Then the divisor of `s` is the cycle of its zero scheme:
> `div_L(s) = [Z(s)]_{n-1}` in `Z_{n-1}(X)`.

```lean
theorem divisorOfMeromorphicSectionCycle_eq_cycleAssociatedToZeroScheme (C : ChowSituation.{u})
    (p : X ⟶ C.S) [LocallyOfFiniteType p] [IsIntegral X] (n : ℤ)
    (hn : schemeDeltaDimension C p = (n : EInt)) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) (hs : s ≠ 0) :
    divisorOfMeromorphicSectionCycle C p n hn L (meromorphicSectionOfSection L s)
        (isRegularMeromorphicSection_of_ne_zero X L s hs) =
      cycleAssociatedToClosedSubscheme C p
        (Stacks.Divisors.zeroScheme X L s).subschemeι (n - 1)
```

**`Stacks.ChernCap42.firstChernClassCapOfInvertible_fundamentalCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/ChernCap42/DivisorOfSectionCycle.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/ChernCap42/DivisorOfSectionCycle.lean#L405). The attribute's comment: “first Chern class”.

> Let `X` be an integral scheme locally of finite type over the base of chapter 42, of
> delta-dimension `n`, let `L` be an invertible `𝒪_X`-module and let `s` be a nonzero global section
> of `L`. Then the first Chern class of `L` capped with the fundamental cycle `[X]` of `X`, in
> degree `n - 1 + 1`, is the class of the cycle of the zero scheme of `s`:
> `c₁(L) ∩ [X] = [Z(s)]_{n-1}` in `CH_{n-1}(X)`.

```lean
theorem firstChernClassCapOfInvertible_fundamentalCycle (C : ChowSituation.{u}) (p : X ⟶ C.S)
    [LocallyOfFiniteType p] [IsIntegral X] (n : ℤ)
    (hn : schemeDeltaDimension C p = (n : EInt)) (L : X.Modules)
    [AlgebraicGeometry.SheafOfModules.IsInvertible X.sheaf.obj X.ringCatSheaf.property L]
    (s : Γ(L, ⊤)) (hs : s ≠ 0) :
    firstChernClassCapOfInvertible C p (n - 1) L
        (cycleAssociatedToClosedSubscheme C p (𝟙 X) (n - 1 + 1)) =
      QuotientAddGroup.mk (cycleAssociatedToClosedSubscheme C p
        (Stacks.Divisors.zeroScheme X L s).subschemeι (n - 1))
```

## Tag 02SM, a lemma

[Tag 02SM](https://stacks.math.columbia.edu/tag/02SM) in the Stacks Project.

**`Stacks.Chow.mk_flatPullback_meromorphicDivisorCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackMeromorphicDivisorIntegral.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/RationalEquivalence/FlatPullbackMeromorphicDivisorIntegral.lean#L143). The attribute's comment: “the flat pullback read on the divisor of a nonzero meromorphic section”.

> **Stacks 02SM.** Let `C = (S, δ)` be the base situation of chapter 42, let `X` and `Y` be
> integral and locally of finite type over `S` with `n = dim_δ(Y)`, and let `f : X ⟶ Y` be flat of
> relative dimension `r`. For an invertible module `L` on `Y`,
>
>   `f^*(c₁(L) ∩ [Y]) = c₁(f^*L) ∩ [X]`
>
> in `A_{n + r - 1}(X)`, where either side is the class of the divisor of a nonzero meromorphic
> section, read on `Y` and pulled back on the left and read on `X` on the right.

```lean
theorem mk_flatPullback_meromorphicDivisorCycle (hs : s ≠ 0) :
    (QuotientAddGroup.mk ((show (n : ℤ) - 1 + (r : ℤ) = n + (r : ℤ) - 1 by ring) ▸
          flatPullback C sX sY f hbase r hf (n - 1)
            (meromorphicDivisorCycleOfInvertible C sY hY L s).val) :
        chowGroup C sX (n + (r : ℤ) - 1)) =
      QuotientAddGroup.mk (meromorphicDivisorCycleOfInvertible C sX
        (schemeDeltaDimension_eq_add_of_flat C sX sY f hbase r hf hY)
        ((Scheme.Modules.pullback f).obj L) (genericStalkPullback f L s)).val
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.24, Tag 02SI](https://stacks.math.columbia.edu/tag/02SI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

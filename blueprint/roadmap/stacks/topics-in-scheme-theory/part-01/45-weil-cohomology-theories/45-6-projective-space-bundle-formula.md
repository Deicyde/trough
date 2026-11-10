---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.isIso_projectiveBundleFormula, Stacks.WeilCohomology.diagonal_projectiveBundle_eq_sum
statement: formalized
proof: formalized
---

# 45.6 Projective space bundle formula

Section 45.6 of the Stacks Project, [Tag 0FGP](https://stacks.math.columbia.edu/tag/0FGP). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FGQ, a lemma

[Tag 0FGQ](https://stacks.math.columbia.edu/tag/0FGQ) in the Stacks Project.

**`Stacks.WeilCohomology.isIso_projectiveBundleFormula`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveBundleMotive.lean, line 731](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveBundleMotive.lean#L731). The attribute's comment: “the projective space bundle formula: the sum of the c_i = c_1(pr_2^*O_P(1))^i ∩ [Gamma_p], from the direct sum of the h(X)(-i), i < r, to h(P), is an isomorphism in M_k”.

> **Stacks Project, Tag 0FGQ (the projective space bundle formula).** Let `k` be a field, `X` a
> smooth projective scheme over `k`, `ℰ` a finite locally free `𝒪_X`-module of rank `r` and
> `p : P = 𝐏(ℰ) ⟶ X` its projective bundle, with `𝒪_P(1)` normalized so that `p_*𝒪_P(1) = ℰ`. For
> `i = 0, …, r - 1` let `c_i = c₁(pr₂^*𝒪_P(1))^i ∩ [Γ_p] ∈ Corr^i(X, P)`, read as a morphism
> `h(X)(-i) ⟶ h(P)`, where `h(Y)(m) = (Y, 1, m)` is `Stacks.WeilCohomology.twistedMotive Y m` and
> `h(P) = (P, 1, 0) = twistedMotive P 0` (`Stacks.WeilCohomology.twistedMotive_zero`). Then
>
>   `∑_{i < r} c_i : ⨁_{i < r} h(X)(-i) ⟶ h(P)`
>
> is an isomorphism in the category `M_k` of Chow motives.

```lean
theorem isIso_projectiveBundleFormula :
    IsIso (biproduct.desc (projectiveBundleOfRankHom X E r) :
      (⨁ fun i : Fin r ↦ twistedMotive X (-((i : ℕ) : ℤ))) ⟶
        twistedMotive (projectiveBundleOfRank X E r) 0)
```

## Tag 0FGR, a lemma

[Tag 0FGR](https://stacks.math.columbia.edu/tag/0FGR) in the Stacks Project.

**`Stacks.WeilCohomology.diagonal_projectiveBundle_eq_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveBundleDiagonal.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveBundleDiagonal.lean#L394).

> **Stacks 0FGR.** Let `X` be smooth and separated over a field `k` (for instance smooth
> projective, as in Lemma 0FGQ), `ℰ` a finite locally free `𝒪_X`-module of rank `r = n + 1`,
> `p : P = 𝐏(ℰ) ⟶ X` its projective bundle with `𝒪_P(1)` normalized so that `p_*𝒪_P(1) = ℰ`
> (`Stacks.Chow.bundle`, `Stacks.Chow.bundleTwist`), and `𝒮` the kernel of the canonical surjection
> `p^*ℰ ⟶ 𝒪_P(1)`. Then the class of the diagonal of `P` in the Chow groups of `P × P` is
>
>   `[Δ_P] = (∑_{i = 0}^{r - 1} c_{r-1-i}(pr₁^*𝒮^∨) ∩ c₁(pr₂^*𝒪_P(1))^i) ∩ (p × p)^*[Δ_X]`,
>
> with integer coefficients. The identity is stated dimension by dimension, which is the whole of
> it since `[Δ_P] = ∑_m [Δ_P]_m`: for every `m`, the part of dimension `m + n` of the cycle of the
> diagonal `Δ_P ⊂ P ×_k P` is the sum over `i ≤ n` of `c_{n-i}(pr₁^*𝒮^∨) ∩ c₁(pr₂^*𝒪_P(1))^i ∩
> (p × p)^*[Δ_X]_m`, where `[Δ_X]_m` is the part of dimension `m` of the cycle of `Δ_X ⊂ X ×_k X`,
> `(p × p)^*` is flat pullback (of relative dimension `2n`), `c₁(-)^i ∩` is the `i`-th power of the
> first Chern class cap (Stacks 02SO) and `c_j(-) ∩` the Chern class cap of Stacks 02U6.
>
> The tag as printed weights the `i`-th summand by a binomial coefficient `C(r - 1, i)`. Read
> literally that is false: for `X = Spec k` and `r = 3` (so `P = 𝐏²`) it gives
> `h₁² + 2h₁h₂ + h₂²` for the diagonal class instead of `h₁² + h₁h₂ + h₂²`. The coefficients are
> dropped here, which is the identity the source's proof establishes: the diagonal is the zero
> scheme of the section of `pr₁^*𝒮^∨ ⊗ pr₂^*𝒪_P(1)`, whose top Chern class expands without them.

```lean
theorem diagonal_projectiveBundle_eq_sum (m : ℤ) :
    letI := flat_bundleProdMap sX E n
    letI := locallyOfFiniteType_bundleProdMap sX E n
    QuotientAddGroup.mk' (rationalEquivalences (fieldChowSituation k)
        (prodBase (bundleProj E ≫ sX) (bundleProj E ≫ sX)) (m + n))
        (cycleAssociatedToClosedSubscheme (fieldChowSituation k)
          (prodBase (bundleProj E ≫ sX) (bundleProj E ≫ sX))
          (pullback.diagonal (bundleProj E ≫ sX)) (m + n)) =
      ∑ i : Fin (n + 1), chowGroupCast (fieldChowSituation k)
        (prodBase (bundleProj E ≫ sX) (bundleProj E ≫ sX)) (by have := i.isLt; omega)
        (GenuineChern.chernFamily (fieldChowSituation k)
          (prodBase (bundleProj E ≫ sX) (bundleProj E ≫ sX))
          ((Scheme.Modules.pullback (pullback.fst (bundleProj E ≫ sX) (bundleProj E ≫ sX))).obj
            (dualSheaf (kernel (bundleTautological E)))) n
          (m + ((n + n : ℕ) : ℤ) - (i : ℕ)) (n - i)
          (capPow (fieldChowSituation k) (prodBase (bundleProj E ≫ sX) (bundleProj E ≫ sX))
            (invCap (fieldChowSituation k) (prodBase (bundleProj E ≫ sX) (bundleProj E ≫ sX))
              ((Scheme.Modules.pullback (pullback.snd (bundleProj E ≫ sX) (bundleProj E ≫ sX))).obj
                (bundleTwist E))) i (m + ((n + n : ℕ) : ℤ)) (m + ((n + n : ℕ) : ℤ) - (i : ℕ))
            (by ring)
            (flatPullbackChowOfRelativeDimension (fieldChowSituation k)
              (prodBase (bundleProj E ≫ sX) (bundleProj E ≫ sX)) (prodBase sX sX)
              (pullback.map (bundleProj E ≫ sX) (bundleProj E ≫ sX) sX sX (bundleProj E)
                (bundleProj E) (𝟙 _) (Category.comp_id _) (Category.comp_id _))
              (bundleProdMap_comp_prodBase sX E) (n + n) (relativeDimension_bundleProdMap sX E n) m
              (QuotientAddGroup.mk' (rationalEquivalences (fieldChowSituation k) (prodBase sX sX) m)
                (cycleAssociatedToClosedSubscheme (fieldChowSituation k) (prodBase sX sX)
                  (pullback.diagonal sX) m)))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.6, Tag 0FGP](https://stacks.math.columbia.edu/tag/0FGP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

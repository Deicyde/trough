---
declaration: section
origin: cited
lean: Stacks.Intersection.ChowRing.chowPullback_eq_flatPullbackChow, Stacks.Intersection.ChowRing.chowMulFun_properChowPushforward_eq, Stacks.Intersection.ChowRing.chowPullback_isRingHom, Stacks.Intersection.ChowRing.chowPullback_comp
statement: formalized
proof: formalized
---

# 43.27 Pullback for a general morphism

Section 43.27 of the Stacks Project, [Tag 0B0H](https://stacks.math.columbia.edu/tag/0B0H). 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B2X, a lemma

[Tag 0B2X](https://stacks.math.columbia.edu/tag/0B2X) in the Stacks Project.

**`Stacks.Intersection.ChowRing.chowPullback_eq_flatPullbackChow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ChowRing/Pullback.lean, line 703](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ChowRing/Pullback.lean#L703). The attribute's comment: “part (4): for flat `f` of relative dimension `e`, the pullback `f^*` of Tag 0B0H is the flat pullback `CH_k(Y) → CH_{k+e}(X)` of Section 43.9”.

> **Stacks 0B2X, part (4): for flat `f` the pullback is flat pullback.** If `f` is flat of
> relative dimension `e`, then `f^* = f^*_{flat} : CH_k(Y) ⟶ CH_{k+e}(X)`.

```lean
theorem chowPullback_eq_flatPullbackChow [Flat f] (e : ℕ)
    (he : topologicalKrullDim X = topologicalKrullDim Y + (e : WithBot ℕ∞)) {k : ℤ}
    (hkm : k + dX = dY + (k + e)) :
    letI : LocallyOfFiniteType f := locallyOfFiniteType_of_isVariety_comp K sX sY f hf
    chowPullback K sX sY hX hY hdX hdY f hf hkm =
      flatPullbackChowOfRelativeDimension (fieldChowSituation K) sX sY f hf e
        (relativeDimension_of_flat_of_isVariety K sX sY f hf e he) k
```

**`Stacks.Intersection.ChowRing.chowMulFun_properChowPushforward_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ChowRing/Pullback.lean, line 850](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ChowRing/Pullback.lean#L850). The attribute's comment: “part (3): the projection formula `f_*(α) · β = f_*(α · f^*β)` on Chow groups, for `α ∈ CH_r(X)` and `β ∈ CH_k(Y)`, `f^*β ∈ CH_m(X)` with `k + dim X = dim Y + m`, and both products in `CH_n` with `r + m = dim X + n`”. References: SGA 7 XVII (5.2), “partial”.

> **Stacks 0B2X, part (3): the projection formula** `f_*(a) · b = f_*(a · f^*b)`. With `s` the
> graph, `s_*(a · f^*b) = s_*(a) · pr_Y^* b` on `X × Y` by the remark on graphs, and
> `f_* = pr_{Y,*} ∘ s_*`, so this is the flat projection formula (Tag 0B10) for `pr_Y`.

```lean
theorem chowMulFun_properChowPushforward_eq {r k m n : ℤ} (hkm : k + dX = dY + m)
    (hn : r + m = dX + n) (a : chowGroup (fieldChowSituation K) sX r)
    (b : chowGroup (fieldChowSituation K) sY k) :
    letI := isProper_of_comp_eq f hf
    chowMulFun K sY hY n
        (properChowPushforward (fieldChowSituation K) sX sY f hf r
          (properPushforwardFactorsThroughRationalEquivalence_of_isProper (fieldChowSituation K)
            sX sY f hf r) a) b =
      properChowPushforward (fieldChowSituation K) sX sY f hf n
        (properPushforwardFactorsThroughRationalEquivalence_of_isProper (fieldChowSituation K)
          sX sY f hf n)
        (chowMulFun K sX hX n a (chowPullback K sX sY hX hY hdX hdY f hf hkm b))
```

**`Stacks.Intersection.ChowRing.chowPullback_isRingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ChowRing/Pullback.lean, line 948](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ChowRing/Pullback.lean#L948). The attribute's comment: “part (1): `f^* : CH^*(Y) → CH^*(X)` is a ring map, stated as the existence of a ring homomorphism between the Chow rings `⨁_c CH^c` which is `f^*` on each graded piece `CH^c(Y) = CH_{dim Y - c}(Y) → CH^c(X) = CH_{dim X - c}(X)`; the content is `chowPullback_chowMulFun` (`f^*(a · b) = f^*a · f^*b`) and `chowPullback_fundamentalClass` (`f^*[Y] = [X]`)”.

> **Stacks Project, Tag 0B2X, part (1).** Let `f : X ⟶ Y` be a morphism of nonsingular
> projective varieties over an algebraically closed field (the chapter's convention, Tag 0AZ8).
> Then the pullback `f^* : CH^*(Y) ⟶ CH^*(X)` of Section 43.23 (Tag 0B0H) is a ring map: there is
> a ring homomorphism between the Chow rings of Section 43.21 (Tag 0B0G) which is `f^*` on every
> graded piece `CH^c(Y) ⟶ CH^c(X)`.

```lean
theorem chowPullback_isRingHom :
    ∃ φ : ChowRing K sY hY dY hdY →+* ChowRing K sX hX dX hdX,
      ∀ (c : ℕ) (a : ChowGrade K sY dY hY hdY c),
        φ (DirectSum.of _ c a) =
          DirectSum.of _ c (chowPullback K sX sY hX hY hdX hdY f hf (k := (dY : ℤ) - c)
            (m := (dX : ℤ) - c) (by ring) a)
```

**`Stacks.Intersection.ChowRing.chowPullback_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Intersection/ChowRing/PullbackComposition.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Intersection/ChowRing/PullbackComposition.lean#L396). The attribute's comment: “part (2): `(g ∘ f)^* = f^* ∘ g^*` for a composable pair of morphisms of nonsingular projective varieties, on Chow groups `CH_k(Z) → CH_l(Y) → CH_m(X)` with `k + dim Y = dim Z + l`, `l + dim X = dim Y + m`”.

> **Stacks Project, Tag 0B2X, part (2).** For morphisms `f : X ⟶ Y` and `g : Y ⟶ Z` of
> nonsingular projective varieties, `(g ∘ f)^* = f^* ∘ g^*` on Chow groups. On
> `W = (X × Y) × Z`, `f^*(g^*c) = pr_{X,*}(q₁₂^*[Γ_f] · q₂₃^*[Γ_g] · q₃^* c)` by base change
> (Tag 02RG), the projection formula for `q₁₂` (Tag 0B10) and Tag 0B0Z; the product
> `q₁₂^*[Γ_f] · q₂₃^*[Γ_g]` is the transversal intersection `{(x, f(x), g(f(x)))}`, which `q₁₃`
> maps isomorphically onto `Γ_{g ∘ f}`, and the projection formula for `q₁₃` gives `(g ∘ f)^* c`.

```lean
theorem chowPullback_comp {k l m : ℤ} (hkl : k + dY = dZ + l) (hlm : l + dX = dY + m)
    (hkm : k + dX = dZ + m) (c : chowGroup (fieldChowSituation K) sZ k) :
    chowPullback K sX sZ hX hZ hdX hdZ (f ≫ g) (by rw [Category.assoc, hg, hf]) hkm c =
      chowPullback K sX sY hX hY hdX hdY f hf hlm
        (chowPullback K sY sZ hY hZ hdY hdZ g hg hkl c)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 43.27, Tag 0B0H](https://stacks.math.columbia.edu/tag/0B0H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

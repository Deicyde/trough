---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.WeilData.pushforward_cupTw_pullTw, Stacks.WeilCohomology.WeilData.pushforward_comp, Stacks.WeilCohomology.poincareDualPushforward_comp, Stacks.WeilCohomology.poincareDualPushforward_cup, Stacks.WeilCohomology.WeilData.pushforward_snd_externalProduct, Stacks.Chow.codimensionIntersectionProduct_eq_codimensionGysin_diag, Stacks.WeilCohomology.WeilData.cycleClassMul_iff_cycleClass_codimensionExteriorProduct, Stacks.WeilCohomology.cycleClass_mul_iff_cycleClass_externalProduct
statement: formalized
proof: formalized
---

# 45.9 Weil cohomology theories, I

Section 45.9 of the Stacks Project, [Tag 0FHA](https://stacks.math.columbia.edu/tag/0FHA). 12 tags here are carried by 43 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FHB, a lemma

[Tag 0FHB](https://stacks.math.columbia.edu/tag/0FHB) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.pushforward_cupTw_pullTw`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectionFormula.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectionFormula.lean#L164). The attribute's comment: “the projection formula f\_*(f^*b ∪ a) = b ∪ f\_*a, over the actual category of smooth projective schemes over k, in every degree and Tate twist”.

> **Stacks 0FHB, the projection formula.** For a morphism `f : X ⟶ Y` of nonempty
> equidimensional smooth projective schemes over `k`, of dimensions `d` and `e`, and classes
> `a ∈ H^j(X)(t)`, `b ∈ H^m(Y)(s)`,
>
> `f_*(f^*b ∪ a) = b ∪ f_*a` in `H^{m+j'}(Y)(s+t')`,
>
> where `f_* : H^j(X)(t) → H^{j'}(Y)(t')` with `j' = j + 2(e - d)`, `t' = t + (e - d)`.
> The proof uses only axiom (A)(b).

```lean
theorem pushforward_cupTw_pullTw (hA : W.PerfectPairing)
    {X Y : (SmoothProjectiveScheme k).FullSubcategory}
    (f : X ⟶ Y) {d e : ℕ} (hX : IsNonemptyEquidimensional X d)
    (hY : IsNonemptyEquidimensional Y e) (m s j t j' t' : ℤ) (hj : j' + 2 * d = j + 2 * e)
    (ht : t' + d = t + e) (b : W.Tw Y m s) (a : W.Tw X j t) :
    W.pushforward hA f hX hY (m + j) (s + t) (m + j') (s + t') (by omega) (by omega)
        (W.cupTw X m j _ rfl s t _ rfl (W.pullTw f m s b) a) =
      W.cupTw Y m j' _ rfl s t' _ rfl b (W.pushforward hA f hX hY j t j' t' hj ht a)
```

**`Stacks.WeilCohomology.WeilData.pushforward_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectionFormula.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectionFormula.lean#L192). The attribute's comment: “functoriality g\_* ∘ f\_* = (g ∘ f)\_* of the pushforward, over the actual category of smooth projective schemes over k, in every degree and Tate twist”.

> **Stacks 0FHB, functoriality of the pushforward.** For morphisms `f : X ⟶ Y` and `g : Y ⟶ Z`
> of nonempty equidimensional smooth projective schemes over `k`, `g_* ∘ f_* = (g ∘ f)_*`.
> The proof uses only axiom (A)(b).

```lean
theorem pushforward_comp (hA : W.PerfectPairing)
    {X Y Z : (SmoothProjectiveScheme k).FullSubcategory} (f : X ⟶ Y)
    (g : Y ⟶ Z) {d e c : ℕ} (hX : IsNonemptyEquidimensional X d)
    (hY : IsNonemptyEquidimensional Y e) (hZ : IsNonemptyEquidimensional Z c)
    (j t j' t' j'' t'' : ℤ) (hj : j' + 2 * d = j + 2 * e) (ht : t' + d = t + e)
    (hj' : j'' + 2 * e = j' + 2 * c) (ht' : t'' + e = t' + c) (a : W.Tw X j t) :
    W.pushforward hA g hY hZ j' t' j'' t'' hj' ht' (W.pushforward hA f hX hY j t j' t' hj ht a) =
      W.pushforward hA (f ≫ g) hX hZ j t j'' t'' (by omega) (by omega) a
```

**`Stacks.WeilCohomology.poincareDualPushforward_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectionFormula/Pushforward.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectionFormula/Pushforward.lean#L57). The attribute's comment: “pushforward\_composition”.

> Poincaré-dual pushforward is covariantly functorial for composable pullbacks.

```lean
theorem poincareDualPushforward_comp
    {R : Type uR} [CommSemiring R]
    {HX : Type uHX} [AddCommMonoid HX] [Module R HX]
    {HY : Type uHY} [AddCommMonoid HY] [Module R HY]
    {HZ : Type uHZ} [AddCommMonoid HZ] [Module R HZ]
    {DX : Type uDX} [AddCommMonoid DX] [Module R DX]
    {DY : Type uDY} [AddCommMonoid DY] [Module R DY]
    {DZ : Type uDZ} [AddCommMonoid DZ] [Module R DZ]
    (pairX : HX →ₗ[R] DX →ₗ[R] R)
    (pairY : HY →ₗ[R] DY →ₗ[R] R)
    (pairZ : HZ →ₗ[R] DZ →ₗ[R] R)
    [pairY.IsPerfPair] [pairZ.IsPerfPair]
    (pullbackF : HY →ₗ[R] HX) (pullbackG : HZ →ₗ[R] HY) :
    (poincareDualPushforward pairY pairZ pullbackG).comp
        (poincareDualPushforward pairX pairY pullbackF) =
      poincareDualPushforward pairX pairZ (pullbackF.comp pullbackG)
```

**`Stacks.WeilCohomology.poincareDualPushforward_cup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectionFormula/Pushforward.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectionFormula/Pushforward.lean#L90). The attribute's comment: “projection\_formula”.

> The projection formula `f₊ (f⁺ b ∪ a) = b ∪ f₊ a` for the pushforward defined by Poincaré
> duality.  The pairing identities are associativity of cup product under integration, and
> `pullback_cup` is its naturality.

```lean
theorem poincareDualPushforward_cup
    {R : Type*} [CommSemiring R]
    {HX DX HX' DX' HY DY HY' DY' BX BY : Type*}
    [AddCommMonoid HX] [Module R HX]
    [AddCommMonoid DX] [Module R DX]
    [AddCommMonoid HX'] [Module R HX']
    [AddCommMonoid DX'] [Module R DX']
    [AddCommMonoid HY] [Module R HY]
    [AddCommMonoid DY] [Module R DY]
    [AddCommMonoid HY'] [Module R HY']
    [AddCommMonoid DY'] [Module R DY']
    [AddCommMonoid BX] [Module R BX]
    [AddCommMonoid BY] [Module R BY]
    (pairX : HX →ₗ[R] DX →ₗ[R] R)
    (pairY : HY →ₗ[R] DY →ₗ[R] R) [pairY.IsPerfPair]
    (pairX' : HX' →ₗ[R] DX' →ₗ[R] R)
    (pairY' : HY' →ₗ[R] DY' →ₗ[R] R) [pairY'.IsPerfPair]
    (pullback : HY →ₗ[R] HX)
    (pullback' : HY' →ₗ[R] HX')
    (pullbackB : BY →ₗ[R] BX)
    (cupX : BX →ₗ[R] DX →ₗ[R] DX')
    (cupY : BY →ₗ[R] DY →ₗ[R] DY')
    (cupLeftX : HX' →ₗ[R] BX →ₗ[R] HX)
    (cupLeftY : HY' →ₗ[R] BY →ₗ[R] HY)
    (pullback_cup : ∀ c b,
      pullback (cupLeftY c b) = cupLeftX (pullback' c) (pullbackB b))
    (trace_assoc_X : ∀ c b a,
      pairX' c (cupX b a) = pairX (cupLeftX c b) a)
    (trace_assoc_Y : ∀ c b a,
      pairY' c (cupY b a) = pairY (cupLeftY c b) a)
    (b : BY) (a : DX) :
    poincareDualPushforward pairX' pairY' pullback'
        (cupX (pullbackB b) a) =
      cupY b (poincareDualPushforward pairX pairY pullback a)
```

## Tag 0FHC, a lemma

[Tag 0FHC](https://stacks.math.columbia.edu/tag/0FHC) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.pushforward_snd_externalProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/SecondProjection.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/SecondProjection.lean#L132). The attribute's comment: “over any field k, for nonempty equidimensional (possibly disconnected) smooth projective X, Y and the actual WeilData of Section 0FHA under (A)(b) and (B)(b): pr\_\{2,*}(pr₁^*a ∪ pr₂^*b) = (∫\_X a) b for a of top degree 2d, and = 0 for a of any other degree, where ∫\_X a is read as zero; b in any degree and Tate twist”.

> **Stacks Project, Tag 0FHC.** Let `H^*` be data (D0), (D1), (D3) over a field `k`
> satisfying axioms (A) and (B), and let `X`, `Y` be nonempty smooth projective schemes over `k`,
> equidimensional of dimensions `d` and `e`. Then `pr_{2, *} : H^*(X × Y)(d + e) ⟶ H^*(Y)(e)`
> sends `a ⊗ b = pr₁^*a ∪ pr₂^*b` to `(∫_X a) b`:
>
> * for `a ∈ H^{2d}(X)(d)` and `b ∈ H^q(Y)(t)`, `pr_{2, *}(a ⊗ b) = (∫_X a) b`;
> * for `a ∈ H^p(X)(s)` with `p ≠ 2d`, where `∫_X a` is read as zero, `pr_{2, *}(a ⊗ b) = 0`.
>
> The source's twists are `t = e`, resp. `s + t = d + e`; any twist is allowed here. Only (A)(b)
> and (B)(b) are used.

```lean
theorem pushforward_snd_externalProduct (hA : W.PerfectPairing) (hK : W.KunnethTrace)
    {X Y : (SmoothProjectiveScheme k).FullSubcategory} {d e : ℕ}
    (hX : IsNonemptyEquidimensional X d) (hY : IsNonemptyEquidimensional Y e) :
    (∀ (q t : ℤ) (a : W.Tw X (2 * d) d) (b : W.Tw Y q t),
      W.pushforward hA (snd X Y) (isNonemptyEquidimensional_prod hX hY) hY (2 * d + q) (d + t)
          q t (by push_cast; ring) (by push_cast; ring)
          (W.cupTw (prod X Y) (2 * d) q _ rfl d t _ rfl (W.pullTw (fst X Y) _ _ a)
            (W.pullTw (snd X Y) _ _ b)) =
        W.trace X d hX a • b) ∧
    ∀ (p q s t : ℤ), p ≠ 2 * d → ∀ (a : W.Tw X p s) (b : W.Tw Y q t),
      W.pushforward hA (snd X Y) (isNonemptyEquidimensional_prod hX hY) hY (p + q) (s + t)
          (p + q - 2 * d) (s + t - d) (by push_cast; ring) (by push_cast; ring)
          (W.cupTw (prod X Y) p q _ rfl s t _ rfl (W.pullTw (fst X Y) _ _ a)
            (W.pullTw (snd X Y) _ _ b)) = 0
```

## Tag 0FHD, a remark

[Tag 0FHD](https://stacks.math.columbia.edu/tag/0FHD) in the Stacks Project.

**`Stacks.Chow.codimensionIntersectionProduct_eq_codimensionGysin_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassExteriorProduct.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassExteriorProduct.lean#L65). The attribute's comment: “the intersection product is α · β = Δ^!(α × β)”.

> **Remark 0FHD: the intersection product is `α · β = Δ^!(α × β)`**, the Gysin map of the
> diagonal `Δ : X ⟶ X ×_k X` (Stacks 0FF3) applied to the exterior product (Stacks 0FBV), for `X`
> smooth and proper over `k` and `α ∈ CH^i(X)`, `β ∈ CH^j(X)`.

```lean
theorem codimensionIntersectionProduct_eq_codimensionGysin_diag (i j : ℤ)
    (α : codimensionChowGroup k sX i) (β : codimensionChowGroup k sX j) :
    codimensionIntersectionProduct k sX i j α β =
      codimensionGysin sX (prodBase sX sX) (f := pullback.diagonal sX)
        (by rw [prodBase, pullback.diagonal_fst_assoc]) (i + j)
        (codimensionExteriorProduct k sX sX i j α β)
```

**`Stacks.WeilCohomology.WeilData.cycleClassMul_iff_cycleClass_codimensionExteriorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassExteriorProduct.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassExteriorProduct.lean#L123). The attribute's comment: “given (C)(a), axiom (C)(c) is equivalent to compatibility of γ with exterior products; (A) and (B), assumed in the source, are not used”.

> **Remark 0FHD.** Given axiom (C)(a), `γ(f^!β) = f^*γ(β)`, axiom (C)(c),
> `γ(α · β) = γ(α) ∪ γ(β)` for every smooth projective `X` over `k`, holds if and only if `γ` is
> compatible with exterior products in the sense that `γ(α × β) = pr₁^*γ(α) ∪ pr₂^*γ(β)` in
> `H^*(X × X)` for every smooth projective `X` over `k` and `α ∈ CH^i(X)`, `β ∈ CH^j(X)`. The source
> assumes (A) and (B) as well; they are not needed.

```lean
theorem cycleClassMul_iff_cycleClass_codimensionExteriorProduct (hCa : W.CycleClassPullback) :
    W.CycleClassMul ↔
      ∀ (X : (SmoothProjectiveScheme k).FullSubcategory) (i j : ℤ)
          (α : codimensionChowGroup k X.obj.hom i)
        (β : codimensionChowGroup k X.obj.hom j),
        W.cycleClass (SmoothProjectiveScheme.prod X X) (i + j)
            (codimensionExteriorProduct k X.obj.hom X.obj.hom i j α β) =
          W.cupTw (SmoothProjectiveScheme.prod X X) (2 * i) (2 * j) _ (by ring) i j _ rfl
            (W.pullTw (SmoothProjectiveScheme.fst X X) _ _ (W.cycleClass X i α))
            (W.pullTw (SmoothProjectiveScheme.snd X X) _ _ (W.cycleClass X j β))
```

**`Stacks.WeilCohomology.cycleClass_mul_iff_cycleClass_externalProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Kunneth.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Kunneth.lean#L95). The attribute's comment: “axiom (C)(c) as compatibility with exterior products”.

> Let the intersection and exterior products of cycles satisfy `α · β = Δ^!(α × β)` and
> `α × β = pr₁^!α · pr₂^!β`, and let the cycle class map satisfy axiom `(C)(a)`,
> `γ(f^!β) = f^*γ(β)`. Then axiom `(C)(c)`, `γ(α · β) = γ(α) ∪ γ(β)`, holds for every smooth
> projective variety if and only if the cycle class map is compatible with exterior products, that
> is `γ(α × β) = pr₁^*γ(α) ∪ pr₂^*γ(β)`.

```lean
theorem cycleClass_mul_iff_cycleClass_externalProduct (k : Type u) [Field k]
    [HasBinaryProducts ((SmoothProjective k).FullSubcategory)]
    (A : (SmoothProjective k).FullSubcategory → ℤ → Type v)
    (cup : ∀ {X : (SmoothProjective k).FullSubcategory} (r s : ℤ), A X r → A X s → A X (r + s))
    (pullback : ∀ {X Y : (SmoothProjective k).FullSubcategory}, (X ⟶ Y) → ∀ r : ℤ, A Y r → A X r)
    (pullback_id : ∀ (X) (r : ℤ) (u : A X r), pullback (𝟙 X) r u = u)
    (pullback_comp : ∀ {X Y Z : (SmoothProjective k).FullSubcategory} (f : X ⟶ Y) (g : Y ⟶ Z)
      (r : ℤ) (u : A Z r), pullback (f ≫ g) r u = pullback f r (pullback g r u))
    (pullback_cup : ∀ {X Y : (SmoothProjective k).FullSubcategory} (f : X ⟶ Y) (r s : ℤ)
      (u : A Y r) (v : A Y s),
      pullback f (r + s) (cup r s u v) = cup r s (pullback f r u) (pullback f s v))
    (CH : (SmoothProjective k).FullSubcategory → ℤ → Type w)
    (chowMul : ∀ {X : (SmoothProjective k).FullSubcategory} (r s : ℤ),
      CH X r → CH X s → CH X (r + s))
    (gysin : ∀ {X Y : (SmoothProjective k).FullSubcategory}, (X ⟶ Y) → ∀ r : ℤ, CH Y r → CH X r)
    (externalProduct : ∀ {X Y : (SmoothProjective k).FullSubcategory} (r s : ℤ),
      CH X r → CH Y s → CH (X ⨯ Y) (r + s))
    (cycleClass : ∀ (X) (r : ℤ), CH X r → A X r)
    -- naturality, `(C)(a)`
    (cycleClass_gysin : ∀ {X Y : (SmoothProjective k).FullSubcategory} (f : X ⟶ Y) (r : ℤ)
      (β : CH Y r), cycleClass X r (gysin f r β) = pullback f r (cycleClass Y r β))
    -- `α × β = pr₁^!α · pr₂^!β`
    (externalProduct_eq : ∀ {X Y : (SmoothProjective k).FullSubcategory} (r s : ℤ)
      (α : CH X r) (β : CH Y s), externalProduct r s α β =
        chowMul r s (gysin (prod.fst : X ⨯ Y ⟶ X) r α) (gysin (prod.snd : X ⨯ Y ⟶ Y) s β))
    -- `α · β = Δ^!(α × β)`, the definition of the intersection product
    (chowMul_eq : ∀ {X : (SmoothProjective k).FullSubcategory} (r s : ℤ)
      (α : CH X r) (β : CH X s), chowMul r s α β =
        gysin (prod.lift (𝟙 X) (𝟙 X) : X ⟶ X ⨯ X) (r + s) (externalProduct r s α β)) :
    (∀ (X) (r s : ℤ) (α : CH X r) (β : CH X s),
        cycleClass X (r + s) (chowMul r s α β) =
          cup r s (cycleClass X r α) (cycleClass X s β)) ↔
      ∀ (X Y) (r s : ℤ) (α : CH X r) (β : CH Y s),
        cycleClass (X ⨯ Y) (r + s) (externalProduct r s α β) =
          cup r s (pullback (prod.fst : X ⨯ Y ⟶ X) r (cycleClass X r α))
            (pullback (prod.snd : X ⨯ Y ⟶ Y) s (cycleClass Y s β))
```

Declarations registered for the tag:

- [`Stacks.WeilCohomology.WeilData.pull_diag_mul`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DiagonalDualBasis.lean#L231), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassExteriorProduct.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassExteriorProduct.lean#L90) (StacksFrontier): “the Künneth map followed by pullback along the diagonal is the cup product”.
- [`Stacks.Chow.codimensionExteriorProduct_eq_codimensionIntersectionProduct`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ExteriorProductGysin.lean#L165), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassExteriorProduct.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassExteriorProduct.lean#L93) (StacksFrontier): “α × β = pr₁^!α · pr₂^!β in CH^*(X × Y), stated without proof in the source”.
- [`Stacks.WeilCohomology.diagonalPullback_kunneth`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Kunneth.lean#L46), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Kunneth.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Kunneth.lean#L65) (StacksFrontier): “the first assertion of the remark, shared verbatim with 0FGU”.

## Tag 0FHE, a lemma

[Tag 0FHE](https://stacks.math.columbia.edu/tag/0FHE) in the Stacks Project.

**`Stacks.Weil.subsingleton_cohomology_of_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/F6Rank201/WeilCohomologyBasePoint.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/F6Rank201/WeilCohomologyBasePoint.lean#L117). The attribute's comment: “vanishing away from degree zero”.

> The cohomology of the base point vanishes outside degree zero.

```lean
theorem subsingleton_cohomology_of_ne_zero (i : ℤ) (hi : i ≠ 0) :
    Subsingleton (H i)
```

**`Stacks.Weil.existsUnique_algebraEquiv_degree_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/F6Rank201/WeilCohomologyBasePoint.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/F6Rank201/WeilCohomologyBasePoint.lean#L132). The attribute's comment: “coefficient-field algebra isomorphism”.

> The coefficient-field algebra map is an isomorphism onto degree-zero
> cohomology of the base point, and it is the unique algebra isomorphism.

```lean
theorem existsUnique_algebraEquiv_degree_zero :
    ∃! e : F ≃ₐ[F] Hpoint,
      ∀ a : F, e a = algebraMap F Hpoint a
```

**`Stacks.Chow.fundamentalChowClass_baseChowMul_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/BasePointChowIdentity.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/BasePointChowIdentity.lean#L153). The attribute's comment: “the Chow identity `[Spec(k)] · [Spec(k)] = [Spec(k)]`, proved from the identification `A_0(Spec(k)) = ℤ` of Stacks 0AZ1 and the normalisation `[Spec(k)] ↦ 1`”.

> **The Chow identity `[S] · [S] = [S]`.** The self-intersection of the fundamental class of
> the base is the fundamental class: it is the unit of the ring `A_0(S) = ℤ` of Stacks 0AZ1. This
> is the step of Stacks 0FHE's proof that the cohomological statements of
> `StacksFrontier.AlgebraicGeometry.F6Rank201.WeilCohomologyBasePoint` carry as a hypothesis.

```lean
theorem fundamentalChowClass_baseChowMul_self (s : C.S) :
    baseChowMul C hδ s (fundamentalChowClass C (𝟙 C.S) 0)
        (fundamentalChowClass C (𝟙 C.S) 0) =
      fundamentalChowClass C (𝟙 C.S) 0
```

**`Stacks.Weil.cycleClass_fundamentalChowClass_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/BasePointChowIdentity.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/BasePointChowIdentity.lean#L227). The attribute's comment: “cycle class of the point”.

> **Stacks Project, Tag 0FHE**, third clause, with the Chow identity proved rather than
> assumed. The cycle class of the fundamental class of the base point is the unit of
> `H⁰(Spec(k))`.
>
> The cycle group is the zeroth Chow group `A_0(Spec(k))` of chapter 42, which is where the cycle
> class map `γ` of `(D2)` is defined, and the only hypothesis on `γ` beyond additivity is axiom
> `(C)(c)`, that it is multiplicative for the intersection product. The idempotency of
> `γ([Spec k])` — the hypothesis `cycleClass_fundamental_mul` of
> `Stacks.Weil.cycleClass_fundamentalClass_eq_one` — is obtained here from
> `Stacks.Chow.fundamentalChowClass_baseChowMul_self`, the Chow identity
> `[Spec(k)] · [Spec(k)] = [Spec(k)]`.

```lean
theorem cycleClass_fundamentalChowClass_eq_one :
    cycleClass (fundamentalChowClass C (𝟙 C.S) 0) = 1
```

**`Stacks.Weil.trace_one_fundamentalChowClass_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/BasePointChowIdentity.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/BasePointChowIdentity.lean#L241). The attribute's comment: “trace of one”.

> **Stacks Project, Tag 0FHE**, fourth clause, with the Chow identity proved rather than
> assumed. Integration of the unit over the base point gives `1`.
>
> Axiom `(C)(d)` normalises the integral at the cycle class of the fundamental class; this is the
> same normalisation read at the unit, which the third clause licenses.

```lean
theorem trace_one_fundamentalChowClass_eq_one : trace 1 = 1
```

**`Stacks.WeilCohomology.WeilData.grade_point_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CohomologyOfPoint.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CohomologyOfPoint.lean#L166). The attribute's comment: “H^i(Spec k) = 0 for i ≠ 0, on the actual category of smooth projective schemes”.

> **Stacks Project, Tag 0FHE**, first clause: `H^i(Spec k) = 0` for `i ≠ 0`.

```lean
theorem grade_point_eq_bot (hBa : W.KunnethIsomorphism) (hCd : W.CycleClassPoint) {i : ℤ}
    (hi : i ≠ 0) : W.grade (point k) i = ⊥
```

**`Stacks.WeilCohomology.WeilData.pointH0AlgEquiv_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CohomologyOfPoint.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CohomologyOfPoint.lean#L192). The attribute's comment: “the unique F-algebra isomorphism F = H^0(Spec k)”.

> **Stacks Project, Tag 0FHE**, second clause: there is a unique `F`-algebra isomorphism
> `F = H^0(Spec k)`. Existence is `Stacks.WeilCohomology.WeilData.pointH0AlgEquiv`; any other
> `F`-algebra isomorphism is equal to it.

```lean
theorem pointH0AlgEquiv_unique (hBa : W.KunnethIsomorphism) (hCd : W.CycleClassPoint)
    (e : F ≃ₐ[F] W.H0 (point k)) : e = pointH0AlgEquiv hBa hCd
```

**`Stacks.WeilCohomology.WeilData.cycleClass_fundamentalClass_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CohomologyOfPoint.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CohomologyOfPoint.lean#L199). The attribute's comment: “γ([Spec k]) = 1, from (B)(a), (C)(c), (C)(d) and the unit law [Spec k]·[Spec k] = [Spec k] in CH^0(Spec k)”.

> **Stacks Project, Tag 0FHE**, third clause: `γ([Spec k]) = 1` in `H^0(Spec k)`.

```lean
theorem cycleClass_fundamentalClass_point (hBa : W.KunnethIsomorphism) (hCc : W.CycleClassMul)
    (hCd : W.CycleClassPoint) :
    W.cycleClass (point k) 0 (fundamentalClass (point k)) =
      W.unitTw (point k) _ _ (by simp)
```

**`Stacks.WeilCohomology.WeilData.trace_unitTw_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CohomologyOfPoint.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CohomologyOfPoint.lean#L232). The attribute's comment: “∫\_\{Spec k} 1 = 1”.

> **Stacks Project, Tag 0FHE**, fourth clause: `∫_{Spec k} 1 = 1`.

```lean
theorem trace_unitTw_point (hBa : W.KunnethIsomorphism) (hCc : W.CycleClassMul)
    (hCd : W.CycleClassPoint) :
    W.trace (point k) 0 isNonemptyEquidimensional_point (W.unitTw (point k) _ _ (by simp)) = 1
```

## Tag 0FHF, a lemma

[Tag 0FHF](https://stacks.math.columbia.edu/tag/0FHF) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.cycleClass_fundamentalClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassFundamental.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassFundamental.lean#L142). The attribute's comment: “the nonempty case, first clause γ([X]) = 1, on the actual category of smooth projective schemes over k with the actual CH^0(X) and Gysin map”.

> For every smooth projective scheme `X` over `k`, the cycle class of the fundamental class is
> the unit: `γ([X]) = 1` in `H^0(X)`.

```lean
theorem cycleClass_fundamentalClass (hBa : W.KunnethIsomorphism) (hCa : W.CycleClassPullback)
    (hCc : W.CycleClassMul) (hCd : W.CycleClassPoint)
    (X : (SmoothProjectiveScheme k).FullSubcategory) :
    W.cycleClass X 0 (fundamentalClass X) = W.unitTw X 0 0 rfl
```

**`Stacks.WeilCohomology.WeilData.nontrivial_of_isNonemptyEquidimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassFundamental.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassFundamental.lean#L155). The attribute's comment: “the nonempty case, second clause 1 ≠ 0 in H^0(X), for X equidimensional”.

> If `X` is nonempty and equidimensional of dimension `d` and `F` has characteristic zero, then
> `H^*(X) ≠ 0`.

```lean
theorem nontrivial_of_isNonemptyEquidimensional [CharZero F] (hA : W.PoincareDuality)
    (hB : W.Kunneth) (hC : W.CycleClassAxiom hA.perfectPairing)
    {X : (SmoothProjectiveScheme k).FullSubcategory}
    {d : ℕ} (hX : IsNonemptyEquidimensional X d) : Nontrivial (W.H X)
```

**`Stacks.WeilCohomology.WeilData.nontrivial_of_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassFundamental.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/CycleClassFundamental.lean#L222). The attribute's comment: “the nonempty case, second clause: 1 ≠ 0 in H^0(X), on the actual category of smooth projective schemes over k”.

> If `X` is a nonempty smooth projective scheme over `k` and `F` has characteristic zero, then
> `1 ≠ 0` in `H^0(X)`, i.e. `H^*(X)` is a nontrivial ring.

```lean
theorem nontrivial_of_nonempty [CharZero F] (hA : W.PoincareDuality) (hB : W.Kunneth)
    (hC : W.CycleClassAxiom hA.perfectPairing) (X : (SmoothProjectiveScheme k).FullSubcategory)
    [Nonempty X.obj.left] : Nontrivial (W.H X)
```

**`Stacks.WeilCohomology.WeilData.subsingleton_of_isEmpty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DisjointUnionIdempotent.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DisjointUnionIdempotent.lean#L287). The attribute's comment: “the empty case: H^*(∅) = 0, on the actual category of smooth projective schemes over k”.

> **Stacks Project, Tag 0FHF**, the empty case: `H^*(∅) = 0`. The proof is the source's idea,
> that `H^*(∅) ⊗ H^*(Q) = H^*(∅ × Q) = H^*(∅)` by (B)(a), made explicit for
> `Q = Spec k ⨿ Spec k`. The idempotent `e = γ([Spec k]) ∈ H^0(Q)` of the first summand restricts
> to `1` and to `0` on the two summands. As `∅ × Q ⟶ ∅` is an isomorphism, `pr₂^*e = pr₁^*a` for
> some `a ∈ H^*(∅)`, so `a ⊗ 1 = 1 ⊗ e` by (B)(a). Restricting the second factor to the two summands
> gives `a ⊗ 1 = 1 ⊗ 1` and `a ⊗ 1 = 0` in `H^*(∅) ⊗ H^*(Spec k)`, hence `1 ⊗ 1 = 0`, and as
> `H^*(Spec k) ≠ 0` (Stacks 0FHE), `1 = 0` in `H^*(∅)`.

```lean
theorem subsingleton_of_isEmpty (hBa : W.KunnethIsomorphism) (hCa : W.CycleClassPullback)
    (hCc : W.CycleClassMul) (hCd : W.CycleClassPoint)
        (E : (SmoothProjectiveScheme k).FullSubcategory)
    [IsEmpty E.obj.left] : Subsingleton (W.H E)
```

**`Stacks.WeilCohomology.subsingleton_cohomology_of_empty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/EmptyScheme.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/EmptyScheme.lean#L200). The attribute's comment: “the empty case: `H^*(∅) = 0`”.

> **Stacks Project, Tag 0FHF**, the empty case: the total cohomology of the empty smooth
> projective scheme over `k` is the zero `F`-vector space.
>
> Axiom `(B)(a)` for the product `E ×_k Y`, with `Y` the projective line, together with the
> isomorphism `E ×_k Y ≅ E` of schemes over `k`, gives `H^*(E) ⊗_F H^*(Y) ≅ H^*(E)`, so
> `dim_F H^*(E) · dim_F H^*(Y) = dim_F H^*(E)`; and `dim_F H^*(Y) ≥ 2` by
> `Stacks.WeilCohomology.one_lt_finrank_cohomology_of_pos_dim`, whose hypotheses are the values at
> the projective line of the quantified axioms. The projective line is nonempty, smooth and proper
> over `k` of relative dimension one, by `AlgebraicGeometry.projectiveLine_smooth`,
> `AlgebraicGeometry.projectiveLine_isProper` and
> `AlgebraicGeometry.projectiveLine_relativeDimension`.

```lean
theorem subsingleton_cohomology_of_empty [CharZero F]
    (H : Scheme.{u} → Type w) [∀ T, AddCommGroup (H T)] [∀ T, Module F (H T)]
    (Hcongr : ∀ {T T' : Scheme.{u}}, (T ≅ T') → (H T' ≃ₗ[F] H T))
    (Hgr : Scheme.{u} → ℤ → Type w)
    [∀ (T : Scheme.{u}) (i : ℤ), AddCommGroup (Hgr T i)]
    [∀ (T : Scheme.{u}) (i : ℤ), Module F (Hgr T i)]
    (grading : ∀ T : Scheme.{u}, DirectSum ℤ (Hgr T) ≃ₗ[F] H T)
    (finiteDimensional : ∀ (T : Scheme.{u}) (pT : T ⟶ (fieldChowSituation k).S),
      Smooth pT → IsProper pT → FiniteDimensional F (H T))
    (kunneth : ∀ (T T' : Scheme.{u}) (pT : T ⟶ (fieldChowSituation k).S)
      (pT' : T' ⟶ (fieldChowSituation k).S), Smooth pT → IsProper pT → Smooth pT' →
      IsProper pT' → (TensorProduct F (H T) (H T') ≃ₗ[F] H (pullback pT pT')))
    (pairing : ∀ (T : Scheme.{u}) (pT : T ⟶ (fieldChowSituation k).S) (_ : Smooth pT)
      (_ : IsProper pT) (d : ℕ), AlgebraicGeometry.RelativeDimension pT d →
      (Hgr T 0 →ₗ[F] Hgr T (2 * (d : ℤ)) →ₗ[F] F))
    (pairing_perfect : ∀ (T : Scheme.{u}) (pT : T ⟶ (fieldChowSituation k).S)
      (hsm : Smooth pT) (hpr : IsProper pT) (d : ℕ)
      (hd : AlgebraicGeometry.RelativeDimension pT d),
      (pairing T pT hsm hpr d hd).IsPerfPair)
    (one : ∀ T : Scheme.{u}, Hgr T 0)
    (cup : ∀ (T : Scheme.{u}) (i : ℤ), Hgr T i →ₗ[F] Hgr T 0 →ₗ[F] Hgr T i)
    (cup_one : ∀ (T : Scheme.{u}) (i : ℤ) (a : Hgr T i), cup T i a (one T) = a)
    (cycleClass : ∀ (T : Scheme.{u}) (pT : T ⟶ (fieldChowSituation k).S) (_ : Smooth pT)
      (_ : IsProper pT) (d : ℕ), AlgebraicGeometry.RelativeDimension pT d →
      (chowGroup (fieldChowSituation k) pT 0 →+ Hgr T (2 * (d : ℤ))))
    (pushforward : ∀ (T : Scheme.{u}) (pT : T ⟶ (fieldChowSituation k).S) (_ : Smooth pT)
      (_ : IsProper pT) (d : ℕ), AlgebraicGeometry.RelativeDimension pT d →
      (Hgr T (2 * (d : ℤ)) →ₗ[F] HptZero))
    (cycleClass_pushforward : ∀ (T : Scheme.{u}) (pT : T ⟶ (fieldChowSituation k).S)
      (hsm : Smooth pT) (hpr : IsProper pT) (d : ℕ)
      (hd : AlgebraicGeometry.RelativeDimension pT d)
      (β : chowGroup (fieldChowSituation k) pT 0),
      letI : Smooth pT := hsm
      letI : IsProper pT := hpr
      pushforward T pT hsm hpr d hd (cycleClass T pT hsm hpr d hd β) =
        cycleClassPoint (properChowPushforward (fieldChowSituation k) pT (𝟙 _) pT
          (Category.comp_id pT) 0
          (properPushforwardFactorsThroughRationalEquivalence_of_isProper (fieldChowSituation k)
            pT (𝟙 _) pT (Category.comp_id pT) 0) β))
    {E : Scheme.{u}} [IsEmpty (E : Type u)] (pE : E ⟶ (fieldChowSituation k).S) :
    Subsingleton (H E)
```

**`Stacks.WeilCohomology.cycleClass_fundamentalChowClass_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/NonemptyScheme.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/NonemptyScheme.lean#L345). The attribute's comment: “the nonempty case, first clause: `γ([X]) = 1`”.

> **Stacks Project, Tag 0FHF**, the first clause of the nonempty case, for an arbitrary smooth
> projective scheme `X` over `k`. The cycle class of the fundamental class `[X] ∈ CH^0(X)` is the
> unit of `H^0(X)`.
>
> No equidimensionality is assumed, and nothing about the cohomology of `X` beyond the cycle class
> map `γ : CH^0(X) → H^0(X)` of `(D2)` enters. The proof is the source's two steps and nothing
> else: `[X] = p^*[Spec(k)]`, which is
> `Stacks.WeilCohomology.structureFlatPullbackDegreeZero_fundamentalChowClass`, and then axiom
> `(C)(a)` for the structure morphism `p`, which is the hypothesis `cycleClass_pullback`, followed
> by Stacks 0FHE, the identity `γ([Spec(k)]) = 1` in `H^0(Spec(k))`, which
> `Stacks.Weil.cycleClass_fundamentalClass_eq_one` supplies from the data and axioms at the base
> point, and the fact `pullbackMap_one` that `p^*` carries the unit of `H^0(Spec(k))`
> to the unit of `H^0(X)`. Nonemptiness of `X` is not needed: for `X` empty both sides vanish.

```lean
theorem cycleClass_fundamentalChowClass_eq_one
    {X : Scheme.{u}} (p : X ⟶ (fieldChowSituation k).S) [Smooth p]
    {HX : Type w} [AddCommGroup HX] [Module F HX] (one : HX)
    (cycleClassX : degreeZeroChow p →+ HX)
    (pullbackMap : HptZero →ₗ[F] HX)
    (cycleClass_pullback : ∀ α,
      cycleClassX (structureFlatPullbackDegreeZero p α) = pullbackMap (cycleClassPoint α))
    (pullbackMap_one : pullbackMap 1 = one) :
    cycleClassX (fundamentalDegreeZeroChow p) = one
```

**`Stacks.WeilCohomology.one_ne_zero_of_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/NonemptyScheme.lean, line 372](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/NonemptyScheme.lean#L372). The attribute's comment: “the nonempty case, second clause: `1 ≠ 0` in `H⁰(X)`”.

> **Stacks Project, Tag 0FHF**, the second clause of the nonempty case. Let `X` be a nonempty
> smooth projective scheme over `k`. Then `1 ≠ 0` in `H^0(X)`.
>
> The coefficient field `F` has characteristic zero, and `H^0(Spec(k))` is a nonzero `F`-algebra,
> so `F` injects into it and `[κ(x) : k] ≠ 0` there. The hypotheses are axiom `(C)(b)` for the
> structure morphism `p`, that the cycle class map commutes with proper pushforward, the data and
> axioms at the base point from which Stacks 0FHE gives `γ([Spec(k)]) = 1`, and the unit law of
> the cup product of `H^*(X)`.

```lean
theorem one_ne_zero_of_nonempty [CharZero F]
    {X : Scheme.{u}} [Nonempty (X : Type u)] (p : X ⟶ (fieldChowSituation k).S)
    [Smooth p] [IsProper p]
    {H0 M : Type w} [AddCommGroup H0] [Module F H0] [AddCommGroup M] [Module F M]
    (one : H0) (cup : M →ₗ[F] H0 →ₗ[F] M) (cup_one : ∀ a : M, cup a one = a)
    (cycleClassX : chowGroup (fieldChowSituation k) p 0 →+ M)
    (pushforward : M →ₗ[F] HptZero)
    (cycleClass_pushforward : ∀ β,
      pushforward (cycleClassX β) =
        cycleClassPoint (properChowPushforward (fieldChowSituation k) p (𝟙 _) p
          (Category.comp_id p) 0
          (properPushforwardFactorsThroughRationalEquivalence_of_isProper (fieldChowSituation k)
            p (𝟙 _) p (Category.comp_id p) 0) β)) :
    one ≠ 0
```

## Tag 0FHG, a lemma

[Tag 0FHG](https://stacks.math.columbia.edu/tag/0FHG) in the Stacks Project.

**`Stacks.WeilCohomology.cycleClass_closedSubscheme_eq_pushforward_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClosedSubschemeClass.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClosedSubschemeClass.lean#L89).

> **Stacks Project, Tag 0FHG.** Let `i : X ⟶ Y` be a closed immersion of nonempty smooth
> projective equidimensional schemes over `k`, and let `c = dim Y - dim X`. Then the cycle class of
> the closed subscheme `X ⊆ Y`, taken in `H^{2c}(Y)(c)`, is `i_* 1`, the pushforward of the unit of
> `H^0(X)`.
>
> The cycle `[X]` here is the cycle of the closed subscheme `X` on the ambient scheme `Y`, of
> dimension `d = dim X`, and not the fundamental cycle of `X` on itself. The hypotheses are the
> data and axioms of a Weil cohomology theory that the source's two-line proof uses: axiom (C)(a)
> for the structure morphism of `X` and the data and axioms at the base point, from which Stacks
> 0FHF (`Stacks.WeilCohomology.cycleClass_fundamentalChowClass_eq_one_of_relativeDimension`) gives
> `γ([X]) = 1` in `H^0(X)`, and axiom (C)(b) for `i`.

```lean
theorem cycleClass_closedSubscheme_eq_pushforward_one
    {k : Type u} [Field k] {F : Type v} [Field F]
    (Hpt : ℤ → Type x) [∀ i : ℤ, AddCommGroup (Hpt i)] [∀ i : ℤ, Module F (Hpt i)]
    [∀ i : ℤ, FiniteDimensional F (Hpt i)]
    (HptZero : Type x) [CommRing HptZero] [Algebra F HptZero]
    (degreeZeroPoint : Hpt 0 ≃ₗ[F] HptZero)
    (kunnethPoint : ∀ n : ℤ,
      DirectSum ℤ (fun j : ℤ ↦ TensorProduct F (Hpt j) (Hpt (n - j))) ≃ₗ[F] Hpt n)
    (cycleClassPoint : chowGroup (fieldChowSituation k) (𝟙 _) 0 →+ HptZero)
    (integrationPoint : HptZero →ₗ[F] F)
    (integration_cycleClassPoint : integrationPoint
      (cycleClassPoint (fundamentalChowClass (fieldChowSituation k) (𝟙 _) 0)) = 1)
    (cycleClassPoint_mul :
      cycleClassPoint (fundamentalChowClass (fieldChowSituation k) (𝟙 _) 0) *
          cycleClassPoint (fundamentalChowClass (fieldChowSituation k) (𝟙 _) 0) =
        cycleClassPoint (fundamentalChowClass (fieldChowSituation k) (𝟙 _) 0))
    {X Y : Scheme.{u}} (sX : X ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType sX] [Flat sX]
    (d : ℕ) (hd : AlgebraicGeometry.RelativeDimension sX d)
    (sY : Y ⟶ (fieldChowSituation k).S) [LocallyOfFiniteType sY]
    (i : X ⟶ Y) [IsClosedImmersion i] (hi : i ≫ sY = sX)
    {HX HY : Type w} [AddCommGroup HX] [Module F HX] [AddCommGroup HY] [Module F HY]
    (one : HX)
    (cycleClassX : chowGroup (fieldChowSituation k) sX (0 + (d : ℤ)) →+ HX)
    (cycleClassY : chowGroup (fieldChowSituation k) sY (0 + (d : ℤ)) →+ HY)
    (pullbackMap : HptZero →ₗ[F] HX) (pullbackMap_one : pullbackMap 1 = one)
    (pushforward : HX →ₗ[F] HY)
    (cycleClass_pullback : ∀ α,
      cycleClassX (flatPullbackChowOfRelativeDimension (fieldChowSituation k) sX (𝟙 _) sX
          (Category.comp_id sX) d hd 0 α) =
        pullbackMap (cycleClassPoint α))
    (cycleClass_pushforward : ∀ α,
      cycleClassY (chowPushforwardOfIsClosedImmersion (fieldChowSituation k) sX sY i hi
          (0 + (d : ℤ)) α) =
        pushforward (cycleClassX α)) :
    cycleClassY (QuotientAddGroup.mk
        (cycleAssociatedToClosedSubscheme (fieldChowSituation k) sY i (0 + (d : ℤ)))) =
      pushforward one
```

**`Stacks.WeilCohomology.WeilData.cycleClass_closedSubschemeClass_eq_pushforward_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ClosedImmersionClass.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ClosedImmersionClass.lean#L146). The attribute's comment: “γ([X]) = i\_*1 for a closed immersion of nonempty equidimensional smooth projective schemes, on the actual category of smooth projective schemes over k with the actual CH^c(Y), the data (D0)-(D3) and axioms (A), (B), (C) as the source states them”.

> **Stacks 0FHG.** Assume given (D0), (D1), (D2), (D3) satisfying (A), (B) and (C). Let
> `i : X ⟶ Y` be a closed immersion of nonempty smooth projective equidimensional schemes over
> `k`, of dimensions `d` and `e`. Then `γ([X]) = i_*1` in `H^{2c}(Y)(c)`, `c = dim(Y) - dim(X)`.
>
> `[X] ∈ CH^c(Y)` is the class of the closed subscheme `X` (`closedSubschemeClass`), `i_*` the
> pushforward of (A) and `1 ∈ H^0(X)` the unit. As in the source: `1 = γ([X])` in `H^0(X)` by
> Stacks 0FHF (`WeilData.cycleClass_fundamentalClass`), and axiom (C)(b) applies to
> `i_*[X]_X = [X]`.

```lean
theorem cycleClass_closedSubschemeClass_eq_pushforward_one (hA : W.PoincareDuality)
    (hB : W.Kunneth) (hC : W.CycleClassAxiom hA.perfectPairing)
        {X Y : (SmoothProjectiveScheme k).FullSubcategory}
    (i : X ⟶ Y) [IsClosedImmersion i.hom.left] {d e : ℕ} (hX : IsNonemptyEquidimensional X d)
    (hY : IsNonemptyEquidimensional Y e) (c : ℤ) (hc : c = e - d) :
    W.cycleClass Y c (closedSubschemeClass Y.obj.hom i.hom.left c) =
      W.pushforward hA.perfectPairing i hX hY 0 0 (2 * c) c (by omega) (by omega)
        (W.unitTw X 0 0 rfl)
```

## Tag 0FHH, a lemma

[Tag 0FHH](https://stacks.math.columbia.edu/tag/0FHH) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.pairing_kunnethComponentTw_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DiagonalDualBasis.lean, line 550](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DiagonalDualBasis.lean#L550). The attribute's comment: “under (D0)–(D3), (A), (B), (C): any family e' with γ([Δ])\_(i,2d-i) = ∑ e ⊗ e', for the actual cycle class γ([Δ]) of the diagonal, is the signed dual basis; the expansion ∫ a ∪ b = ∑ (∫ a ∪ e)(∫ e' ∪ b) is derived, not assumed”.

> **Stacks Project, Tag 0FHH.** Assume given (D0), (D1), (D2), (D3) satisfying (A), (B) and
> (C). Let `X` be a nonempty smooth projective scheme over `k`, equidimensional of dimension `d`,
> and let `e_{i,1}, …, e_{i,β_i}` be a basis of `H^i(X)` over `F`. Write, using the Künneth formula,
> the `(i, 2d - i)` component of the cohomology class of the diagonal as
> `γ([Δ])_{(i, 2d - i)} = ∑_j e_{i,j} ⊗ e'_{2d-i,j}` in `H^i(X) ⊗_F H^{2d-i}(X)(d)`. Then
> `∫_X e_{i,j} ∪ e'_{2d-i,j'} = (-1)^i δ_{jj'}`.
>
> Here `[Δ] ∈ CH^d(X × X)` is the class of the diagonal, a closed subscheme of codimension `d`
> (`Stacks.WeilCohomology.closedSubschemeClass`), `γ([Δ]) ∈ H^{2d}(X × X)(d)` its cohomology class,
> and its components in `⨁_i H^i(X) ⊗_F H^{2d-i}(X)(d)` are those of the Künneth isomorphism
> of axiom (B)(a) (`WeilData.kunnethComponentTw`). The proof is the source's: `γ([Δ]) = Δ_*1`
> (Stacks 0FHG, from 0FHF), so `∫_{X × X} (a ⊗ b) ∪ γ([Δ]) = ∫_X a ∪ b` by the trace equation of
> the pushforward and Remark 0FHD; axiom (B)(b) evaluates the same trace on the Künneth decomposition
> as `∑_j (∫_X a ∪ e_{i,j})(∫_X e'_{2d-i,j} ∪ b)`; and Poincaré duality (A)(b) makes `e'` the dual
> basis.

```lean
theorem pairing_kunnethComponentTw_diagonal (hA : W.PoincareDuality) (hB : W.Kunneth)
    (hC : W.CycleClassAxiom hA.perfectPairing) (i : ℤ) {J : Type*} [Fintype J]
    [DecidableEq J] (e : Module.Basis J F (W.grade X i)) (e' : J → W.Tw X (2 * d - i) d)
    (he : kunnethComponentTw X hB.kunnethIsomorphism (2 * d) d i (2 * d - i)
        (W.cycleClass (SmoothProjectiveScheme.prod X X) d
          (closedSubschemeClass (SmoothProjectiveScheme.prod X X).obj.hom
            (SmoothProjectiveScheme.diag X).hom.left d)) =
      ∑ j, e j ⊗ₜ e' j)
    (j j' : J) :
    W.pairing X d hX i (2 * d - i) (by ring) (e j) (e' j') =
      ((i.negOnePow : ℤ) : F) * if j = j' then 1 else 0
```

**`Stacks.WeilCohomology.WeilData.pairing_diagonalKunnethCoordinates`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DiagonalDualBasis.lean, line 643](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DiagonalDualBasis.lean#L643). The attribute's comment: “the Künneth coordinates of the actual cycle class γ([Δ]) with respect to a basis of H^i(X) are the signed dual basis”.

> **Stacks Project, Tag 0FHH**, for the Künneth coordinates themselves: with
> `e'_{2d-i,j} = WeilData.diagonalKunnethCoordinates`, the coordinates of `γ([Δ])` in bidegree
> `(i, 2d - i)` with respect to the basis `e` of `H^i(X)`,
> `∫_X e_{i,j} ∪ e'_{2d-i,j'} = (-1)^i δ_{jj'}`.

```lean
theorem pairing_diagonalKunnethCoordinates (hA : W.PoincareDuality) (hB : W.Kunneth)
    (hC : W.CycleClassAxiom hA.perfectPairing) (i : ℤ) {J : Type*} [Finite J]
    [DecidableEq J] (e : Module.Basis J F (W.grade X i)) (j j' : J) :
    W.pairing X d hX i (2 * d - i) (by ring) (e j)
        (W.diagonalKunnethCoordinates hB.kunnethIsomorphism X d i e j') =
      ((i.negOnePow : ℤ) : F) * if j = j' then 1 else 0
```

## Tag 0FHI, a lemma

[Tag 0FHI](https://stacks.math.columbia.edu/tag/0FHI) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.finrank_grade_projectiveLineObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCohomology.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCohomology.lean#L431). The attribute's comment: “dim\_F H^i(P¹\_k) = 1 for i = 0, 2 and 0 otherwise, for the actual P¹\_k and the data (D0)–(D3) satisfying (A), (B), (C); the diagonal identity and H^0 ≠ 0 are derived”.

> **Stacks Project, Tag 0FHI**, degree by degree: for a Weil cohomology theory in the sense of
> Section 0FHA, `dim_F H^i(𝐏¹_k)` is `1` for `i = 0, 2` and `0` otherwise.

```lean
theorem finrank_grade_projectiveLineObj [CharZero F] (i : ℤ) :
    Module.finrank F (W.grade (projectiveLineObj k) i) = if i = 0 ∨ i = 2 then 1 else 0
```

**`Stacks.WeilCohomology.WeilData.cohomology_projectiveLineObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCohomology.lean, line 460](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/ProjectiveLineCohomology.lean#L460). The attribute's comment: “H^*(P¹\_k) is 1-dimensional in degrees 0 and 2 and zero in other degrees, for the actual P¹\_k and the data (D0)–(D3) satisfying (A), (B), (C)”.

> **Stacks Project, Tag 0FHI.** For a Weil cohomology theory in the sense of Section 0FHA — data
> (D0)–(D3) satisfying (A), (B) and (C), over a field `k`, with coefficients in a field `F` of
> characteristic zero — `H^*(𝐏¹_k)` is one dimensional in degrees `0` and `2` and zero in every
> other degree.

```lean
theorem cohomology_projectiveLineObj [CharZero F] :
    Module.finrank F (W.grade (projectiveLineObj k) 0) = 1 ∧
      Module.finrank F (W.grade (projectiveLineObj k) 2) = 1 ∧
      ∀ i : ℤ, i ≠ 0 → i ≠ 2 → W.grade (projectiveLineObj k) i = ⊥
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.finrank_piece_zero_eq_one_of_diagonal_two_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectiveLine.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectiveLine.lean#L236). The attribute's comment: “degree zero is one dimensional, for a dimension one `X` whose diagonal class is a sum of two pure tensors; `P¹_k` itself is not constructed in this development”.

> **Stacks Project, Tag 0FHI.** The degree-zero cohomology of a smooth projective scheme of
> dimension one with nonvanishing `H^0` whose diagonal class is a sum of two pure tensors in
> Künneth coordinates — for the source, `P¹_k` — is one dimensional.

```lean
theorem finrank_piece_zero_eq_one_of_diagonal_two_tmul (hd : S.dimension X = 1)
    (hne : Nontrivial ((S.H X).piece 0)) {J : Type t} [Fintype J]
    (e : Module.Basis J F (⨁ n : ℤ, (S.H X).piece n))
    (e' : J → ⨁ n : ℤ, (S.H X).piece n) (hli : LinearIndependent F e')
    (a₁ a₂ b₁ b₂ : ⨁ n : ℤ, (S.H X).piece n)
    (hdiag : ∑ j : J, e j ⊗ₜ[F] e' j = a₁ ⊗ₜ[F] b₁ + a₂ ⊗ₜ[F] b₂) :
    Module.finrank F ((S.H X).piece 0) = 1
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.finrank_piece_two_eq_one_of_diagonal_two_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectiveLine.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectiveLine.lean#L251). The attribute's comment: “degree two is one dimensional, for a dimension one `X` whose diagonal class is a sum of two pure tensors; `P¹_k` itself is not constructed in this development”.

> **Stacks Project, Tag 0FHI.** The degree-two cohomology of a smooth projective scheme of
> dimension one with nonvanishing `H^0` whose diagonal class is a sum of two pure tensors in
> Künneth coordinates — for the source, `P¹_k` — is one dimensional.

```lean
theorem finrank_piece_two_eq_one_of_diagonal_two_tmul (hd : S.dimension X = 1)
    (hne : Nontrivial ((S.H X).piece 0)) {J : Type t} [Fintype J]
    (e : Module.Basis J F (⨁ n : ℤ, (S.H X).piece n))
    (e' : J → ⨁ n : ℤ, (S.H X).piece n) (hli : LinearIndependent F e')
    (a₁ a₂ b₁ b₂ : ⨁ n : ℤ, (S.H X).piece n)
    (hdiag : ∑ j : J, e j ⊗ₜ[F] e' j = a₁ ⊗ₜ[F] b₁ + a₂ ⊗ₜ[F] b₂) :
    Module.finrank F ((S.H X).piece 2) = 1
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.subsingleton_piece_of_diagonal_two_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectiveLine.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectiveLine.lean#L266). The attribute's comment: “vanishing in the other degrees, for a dimension one `X` whose diagonal class is a sum of two pure tensors; `P¹_k` itself is not constructed in this development”.

> **Stacks Project, Tag 0FHI.** Outside degrees `0` and `2` the cohomology of a smooth
> projective scheme of dimension one with nonvanishing `H^0` whose diagonal class is a sum of two
> pure tensors in Künneth coordinates — for the source, `P¹_k` — vanishes.

```lean
theorem subsingleton_piece_of_diagonal_two_tmul (hd : S.dimension X = 1)
    (hne : Nontrivial ((S.H X).piece 0)) {J : Type t} [Fintype J]
    (e : Module.Basis J F (⨁ n : ℤ, (S.H X).piece n))
    (e' : J → ⨁ n : ℤ, (S.H X).piece n) (hli : LinearIndependent F e')
    (a₁ a₂ b₁ b₂ : ⨁ n : ℤ, (S.H X).piece n)
    (hdiag : ∑ j : J, e j ⊗ₜ[F] e' j = a₁ ⊗ₜ[F] b₁ + a₂ ⊗ₜ[F] b₂)
    (i : ℤ) (h0 : i ≠ 0) (h2 : i ≠ 2) :
    Subsingleton ((S.H X).piece i)
```

## Tag 0FHJ, a lemma

[Tag 0FHJ](https://stacks.math.columbia.edu/tag/0FHJ) in the Stacks Project.

**`Stacks.WeilCohomology.WeilData.pullbackPair_bijective_of_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DisjointUnionIso.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DisjointUnionIso.lean#L409). The attribute's comment: “H^*(X ⨿ Y) → H^*(X) × H^*(Y), a ↦ (i^*a, j^*a), is bijective, for any coproduct cofan of X and Y in the actual category of smooth projective schemes over k”.

> Assume given (D0)–(D3) satisfying (A), (B) and (C), with coefficient field `F` of
> characteristic zero. If `X` and `Y` are smooth projective schemes over `k`, then
> `H^*(X ⨿ Y) → H^*(X) × H^*(Y)`, `a ↦ (i^*a, j^*a)` is an isomorphism, where `i`, `j` are the
> coprojections. Here `X ⨿ Y` is any coproduct of `X` and `Y` in the category of smooth projective
> schemes over `k`, given by a colimit cofan `c`.

```lean
theorem pullbackPair_bijective_of_isColimit [CharZero F] (hA : W.PoincareDuality)
    (hB : W.Kunneth) (hC : W.CycleClassAxiom hA.perfectPairing)
        {X Y : (SmoothProjectiveScheme k).FullSubcategory}
    {c : BinaryCofan X Y} (hc : IsColimit c) :
    Function.Bijective fun a : W.H c.pt ↦ (W.pull c.inl a, W.pull c.inr a)
```

**`Stacks.WeilCohomology.WeilData.coprodAlgEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DisjointUnionIso.lean, line 421](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/DisjointUnionIso.lean#L421). The attribute's comment: “the F-algebra isomorphism H^*(X ⨿ Y) ≃ H^*(X) × H^*(Y), a ↦ (i^*a, j^*a), for the coproduct X ⨿ Y in the actual category of smooth projective schemes over k”.

> For smooth projective `X` and `Y` over `k`, restriction to the two coprojections is an
> isomorphism of `F`-algebras `H^*(X ⨿ Y) ≃ H^*(X) × H^*(Y)`, where `X ⨿ Y` is the coproduct in the
> category of smooth projective schemes over `k`.

```lean
def coprodAlgEquiv [CharZero F] (hA : W.PoincareDuality) (hB : W.Kunneth)
    (hC : W.CycleClassAxiom hA.perfectPairing) (X Y : (SmoothProjectiveScheme k).FullSubcategory) :
    W.H (X ⨿ Y) ≃ₐ[F] W.H X × W.H Y
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.pullbackPair_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean#L203). The attribute's comment: “injectivity of restriction to the two components”.

> Restriction to the two components of a disjoint union is injective in every degree: if
> `1 = e + f` in `H^0(Z)` and cup product with `e`, resp. `f`, is `i_* ∘ i^*`, resp. `j_* ∘ j^*`,
> then `a = i_*(i^*a) + j_*(j^*a)`, so a class restricting to zero on both components vanishes.

```lean
theorem pullbackPair_injective (i : X ⟶ Z) (j : Y ⟶ Z) (e f : (S.H Z).piece 0)
    (hone : (S.H Z).one = e + f)
    (pushX : ∀ n : ℤ, (S.H X).piece n →ₗ[F] (S.H Z).piece n)
    (pushY : ∀ n : ℤ, (S.H Y).piece n →ₗ[F] (S.H Z).piece n)
    (hpushX : ∀ (n : ℤ) (a : (S.H Z).piece n),
      ExternallyGraded.degreeCast (R := F) (X := (S.H Z).piece) (add_zero n)
          ((S.H Z).mul n 0 a e) = pushX n (S.pullback i n a))
    (hpushY : ∀ (n : ℤ) (a : (S.H Z).piece n),
      ExternallyGraded.degreeCast (R := F) (X := (S.H Z).piece) (add_zero n)
          ((S.H Z).mul n 0 a f) = pushY n (S.pullback j n a))
    (n : ℤ) :
    Function.Injective ((S.pullback i n).prod (S.pullback j n))
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.pullbackPair_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean#L232). The attribute's comment: “surjectivity of restriction to the two components”.

> Restriction to the two components of a disjoint union is surjective in every degree: if the
> idempotents `e`, `f` of `H^0(Z)` restrict to `1`, `0` on `X` and to `0`, `1` on `Y`, and each of
> `i^*`, `j^*` is surjective, then `a ∪ e + a' ∪ f` restricts to `i^*a` on `X` and to `j^*a'` on
> `Y`.

```lean
theorem pullbackPair_surjective (i : X ⟶ Z) (j : Y ⟶ Z) (e f : (S.H Z).piece 0)
    (hie : S.pullback i 0 e = (S.H X).one) (hif : S.pullback i 0 f = 0)
    (hje : S.pullback j 0 e = 0) (hjf : S.pullback j 0 f = (S.H Y).one)
    (hi : ∀ n : ℤ, Function.Surjective (S.pullback i n))
    (hj : ∀ n : ℤ, Function.Surjective (S.pullback j n))
    (n : ℤ) :
    Function.Surjective ((S.pullback i n).prod (S.pullback j n))
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.pullbackPair_injective_of_pushforward_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean#L278). The attribute's comment: “injectivity of restriction to the two components”.

> Restriction to the two components of a disjoint union is injective in every degree, for
> components of the same dimension as the union, given the decomposition
> `1 = γ([X]) + γ([Y]) = i_*1 + j_*1` of the unit of `H^0(Z)` into orthogonal idempotents.

```lean
theorem pullbackPair_injective_of_pushforward_one (i : X ⟶ Z) (j : Y ⟶ Z)
    (hdX : S.dimension X = S.dimension Z) (hdY : S.dimension Y = S.dimension Z)
    (hone : (S.H Z).one = S.pushforwardOne i hdX + S.pushforwardOne j hdY) (n : ℤ) :
    Function.Injective ((S.pullback i n).prod (S.pullback j n))
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.pullbackPair_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean#L302). The attribute's comment: “restriction to the two components is bijective”.

> For `X` and `Y` smooth projective over `k` of the same dimension as their disjoint union `Z`,
> with coprojections `i`, `j`, the map `H^n(Z) ⟶ H^n(X) × H^n(Y)`, `a ↦ (i^*a, j^*a)`, is bijective
> in every degree, given the decomposition `1 = i_*1 + j_*1` of the unit of `H^0(Z)`, the
> restrictions `i^*(i_*1) = 1`, `i^*(j_*1) = 0`, `j^*(i_*1) = 0`, `j^*(j_*1) = 1`, and surjectivity
> of `i^*` and `j^*`.

```lean
theorem pullbackPair_bijective (i : X ⟶ Z) (j : Y ⟶ Z)
    (hdX : S.dimension X = S.dimension Z) (hdY : S.dimension Y = S.dimension Z)
    (hone : (S.H Z).one = S.pushforwardOne i hdX + S.pushforwardOne j hdY)
    (hie : S.pullback i 0 (S.pushforwardOne i hdX) = (S.H X).one)
    (hif : S.pullback i 0 (S.pushforwardOne j hdY) = 0)
    (hje : S.pullback j 0 (S.pushforwardOne i hdX) = 0)
    (hjf : S.pullback j 0 (S.pushforwardOne j hdY) = (S.H Y).one)
    (hi : ∀ n : ℤ, Function.Surjective (S.pullback i n))
    (hj : ∀ n : ℤ, Function.Surjective (S.pullback j n))
    (n : ℤ) :
    Function.Bijective ((S.pullback i n).prod (S.pullback j n))
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.pullbackPairEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean#L319). The attribute's comment: “the isomorphism onto the product of the cohomologies of the components”.

> The isomorphism `H^n(X ⨿ Y) ≃ H^n(X) × H^n(Y)` given by restriction to the two
> coprojections, in each degree `n`, under the hypotheses of `pullbackPair_bijective`.

```lean
noncomputable def pullbackPairEquiv (i : X ⟶ Z) (j : Y ⟶ Z)
    (hdX : S.dimension X = S.dimension Z) (hdY : S.dimension Y = S.dimension Z)
    (hone : (S.H Z).one = S.pushforwardOne i hdX + S.pushforwardOne j hdY)
    (hie : S.pullback i 0 (S.pushforwardOne i hdX) = (S.H X).one)
    (hif : S.pullback i 0 (S.pushforwardOne j hdY) = 0)
    (hje : S.pullback j 0 (S.pushforwardOne i hdX) = 0)
    (hjf : S.pullback j 0 (S.pushforwardOne j hdY) = (S.H Y).one)
    (hi : ∀ n : ℤ, Function.Surjective (S.pullback i n))
    (hj : ∀ n : ℤ, Function.Surjective (S.pullback j n))
    (n : ℤ) :
    (S.H Z).piece n ≃ₗ[F] (S.H X).piece n × (S.H Y).piece n
```

## Tag 0FHK, a lemma

[Tag 0FHK](https://stacks.math.columbia.edu/tag/0FHK) in the Stacks Project.

**`Stacks.WeilCohomology.WeilRealization.toWeilDataAxioms`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/RealizationWeilData.lean, line 500](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/RealizationWeilData.lean#L500). The attribute's comment: “a Q-linear functor G : M\_k → graded F-vector spaces of symmetric monoidal categories with G(1(1)) nonzero only in degree -2 gives data (D0)-(D3) satisfying (A), (B), (C)”.

> Let `k` be a field and `F` a field of characteristic `0`. A `ℚ`-linear functor
> `G : M_k ⥤ graded F-vector spaces` of symmetric monoidal categories such that `G(𝟏(1))` is nonzero
> only in degree `-2` (a `Stacks.WeilCohomology.WeilRealization`) gives data (D0)–(D3) satisfying
> (A), (B) and (C): `F(1) = G^{-2}(𝟏(1))`, `H^*(X) = G(h(X))` with the cup product from the
> multiplication `[Γ_Δ]` of `h(X)` and the pullbacks `G(h(f))`, the cycle class map
> `γ(α) = G(a_α)(e_{-i})` and the trace map `∫_X x = G([X])(x ⊗ e_d)`
> (`Stacks.WeilCohomology.WeilRealization.toWeilData`).

```lean
def toWeilDataAxioms : WeilDataAxioms k F
```

## Tag 0FHL, a lemma

[Tag 0FHL](https://stacks.math.columbia.edu/tag/0FHL) in the Stacks Project.

**`Stacks.WeilCohomology.WeilDataAxioms.exists_motiveFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/RealizationMotive.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/RealizationMotive.lean#L197). The attribute's comment: “data (D0)-(D3) satisfying (A), (B), (C) give a Q-linear symmetric monoidal functor G : M\_k -> graded F-vector spaces with H^*(X) = G(h(X))”.

> **Stacks Project, Tag 0FHL.** Data (D0), (D1), (D2), (D3) satisfying (A), (B) and (C) give a
> `ℚ`-linear functor `G : M_k ⥤ graded F-vector spaces` of symmetric monoidal categories (for the
> Koszul-signed symmetry of Stacks, Homology, Example 0FFX) with `H^*(X) = G(h(X))`, naturally in `X`
> (pullbacks `f^*` corresponding to `G(h(f))`).

```lean
theorem exists_motiveFunctor (T : WeilDataAxioms k F) :
    ∃ (G : ChowMotiveCat k ⥤ GradedObject ℤ (ModuleCat.{w} F))
      (_ : @Functor.Braided (ChowMotiveCat k) _ _ _ (GradedObject ℤ (ModuleCat.{w} F)) _ _
        GradedObject.koszulBraidedCategory G) (_ : G.Additive) (_ : Functor.Linear ℚ G),
      Nonempty (ChowMotiveCat.h k ⋙ G ≅ T.cohomologyFunctor)
```

## Tag 0FHM, a proposition

[Tag 0FHM](https://stacks.math.columbia.edu/tag/0FHM) in the Stacks Project.

**`Stacks.WeilCohomology.WeilRealization.exists_isoClassEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/WeilRealizationBijection.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/WeilRealizationBijection.lean#L56). The attribute's comment: “for a field k and a field F of characteristic 0, data (D0)-(D3) satisfying (A), (B), (C) correspond 1-to-1 (up to isomorphism) to Q-linear symmetric monoidal functors G : M\_k -> graded F-vector spaces with G(1(1)) nonzero only in degree -2”.

> **Stacks Project, Tag 0FHM.** Let `k` be a field and `F` a field of characteristic `0`.
> Data (D0), (D1), (D2), (D3) satisfying (A), (B), (C) and `ℚ`-linear symmetric monoidal functors
> `G : M_k ⥤ graded F-vector spaces` such that `G(𝟏(1))` is nonzero only in degree `-2` correspond
> `1`-to-`1`, up to isomorphism: the bijection of isomorphism classes sends data `T` to the functor
> of Stacks 0FHL (`Stacks.WeilCohomology.WeilDataAxioms.toWeilRealization`), and its inverse sends
> `G` to the data `H^*(X) = G(h(X))` of Stacks 0FHK
> (`Stacks.WeilCohomology.WeilRealization.toWeilDataAxioms`).

```lean
theorem exists_isoClassEquiv :
    ∃ e : Quotient (WeilDataAxioms.isoSetoid k F) ≃ Quotient (isoSetoid k F),
      (∀ T, e ⟦T⟧ = ⟦T.toWeilRealization⟧) ∧ ∀ G, e.symm ⟦G⟧ = ⟦G.toWeilDataAxioms⟧
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.9, Tag 0FHA](https://stacks.math.columbia.edu/tag/0FHA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

---
declaration: section
origin: cited
lean: Stacks.WeilCohomology.PoincareDualityPushforwardSetup.mul_pushforward_one, Stacks.WeilCohomology.PoincareDualityPushforwardSetup.pushforward_mul_pullback, Stacks.WeilCohomology.PoincareDualityPushforwardSetup.pushforward_comp, Stacks.WeilCohomology.cycleClass_mul_iff_cycleClass_externalProduct', Stacks.WeilCohomology.diagonalPullback_kunneth, Stacks.WeilCohomology.ClassicalWeilCohomologyTheory, Stacks.WeilCohomology.ClassicalWeilCohomology, Stacks.WeilCohomology.integration_cycleClass_codimensionClassOfZeroCycle
statement: formalized
proof: formalized
---

# 45.7 Classical Weil cohomology theories

Section 45.7 of the Stacks Project, [Tag 0FGS](https://stacks.math.columbia.edu/tag/0FGS). 11 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FGT, a lemma

[Tag 0FGT](https://stacks.math.columbia.edu/tag/0FGT) in the Stacks Project.

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.mul_pushforward_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/DisjointUnion.lean#L128). The attribute's comment: “cup product with the pushforward of the unit”.

> Cup product with the pushforward `f_*1` of the unit is `f_* ∘ f^*`, for a morphism
> `f : X ⟶ Z` of smooth projective schemes over `k` of equal dimension:
> `a ∪ f_*1 = f_*(f^*a ∪ 1) = f_*(f^*a)`.

```lean
theorem mul_pushforward_one (f : X ⟶ Z) (hd : S.dimension X = S.dimension Z) (n : ℤ)
    (a : (S.H Z).piece n) :
    ExternallyGraded.degreeCast (R := F) (X := (S.H Z).piece) (add_zero n)
        ((S.H Z).mul n 0 a
          (ExternallyGraded.degreeCast (R := F) (X := (S.H Z).piece)
            (show 2 * (S.dimension Z : ℤ) - 2 * (S.dimension Z : ℤ) = 0 by omega)
            (S.pushforward f (2 * (S.dimension Z : ℤ))
              (ExternallyGraded.degreeCast (R := F) (X := (S.H X).piece)
                (show (0 : ℤ) = 2 * (S.dimension X : ℤ) - 2 * (S.dimension Z : ℤ) by omega)
                (S.H X).one)))) =
      ExternallyGraded.degreeCast (R := F) (X := (S.H Z).piece)
        (show 2 * (S.dimension Z : ℤ) - (2 * (S.dimension Z : ℤ) - n) = n by omega)
        (S.pushforward f (2 * (S.dimension Z : ℤ) - n)
          (ExternallyGraded.degreeCast (R := F) (X := (S.H X).piece)
            (show n = 2 * (S.dimension X : ℤ) - (2 * (S.dimension Z : ℤ) - n) by omega)
            (S.pullback f n a)))
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.pushforward_mul_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectionFormula/Formula.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectionFormula/Formula.lean#L79). The attribute's comment: “projection_formula”.

> The projection formula `f_*(f^*b ∪ a) = b ∪ f_*a` for the pushforward determined by Poincaré
> duality.

```lean
theorem PoincareDualityPushforwardSetup.pushforward_mul_pullback
    {X Y : (SmoothProjective k).FullSubcategory} (f : X ⟶ Y) (i j : ℤ)
    (b : (S.H Y).piece j) (a : (S.H X).piece (2 * (S.dimension X : ℤ) - (i + j))) :
    S.pushforward f i
        (ExternallyGraded.degreeCast (R := F) (by omega)
          ((S.H X).mul j (2 * (S.dimension X : ℤ) - (i + j)) (S.pullback f j b) a)) =
      ExternallyGraded.degreeCast (R := F) (by omega)
        ((S.H Y).mul j (2 * (S.dimension Y : ℤ) - (i + j)) b (S.pushforward f (i + j) a))
```

**`Stacks.WeilCohomology.PoincareDualityPushforwardSetup.pushforward_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectionFormula/Formula.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ProjectionFormula/Formula.lean#L126). The attribute's comment: “pushforward_functoriality”.

> The pushforward determined by Poincaré duality is covariantly functorial:
> `g_* ∘ f_* = (g ∘ f)_*`.

```lean
theorem PoincareDualityPushforwardSetup.pushforward_comp
    {X Y Z : (SmoothProjective k).FullSubcategory} (f : X ⟶ Y) (g : Y ⟶ Z) (i : ℤ) :
    (S.pushforward g i).comp (S.pushforward f i) = S.pushforward (f ≫ g) i
```

## Tag 0FGU, a remark

[Tag 0FGU](https://stacks.math.columbia.edu/tag/0FGU) in the Stacks Project.

**`Stacks.WeilCohomology.cycleClass_mul_iff_cycleClass_externalProduct'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalTheory.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalTheory.lean#L230). The attribute's comment: “axiom (C)(c) as compatibility with exterior products”.

> **Stacks Project, Tag 0FGU.** Granted axiom `(C)(a)`, that `γ(f^!β) = f^*γ(β)`, and the
> diagonal description `α · β = Δ^!(α × β)` of the intersection product, axiom `(C)(c)`, that
> `γ(α · β) = γ(α) ∪ γ(β)`, is equivalent to compatibility of the cycle class map with exterior
> products, that is `γ(α × β) = pr₁^*γ(α) ∪ pr₂^*γ(β)`.
>
> This is the equivalence of the remark in the classical setting: cohomology is the graded algebra
> of a Poincaré duality setup, cycles are a `ChowCycleData`, and the exterior product is the one
> defined by `α × β = pr₁^!α · pr₂^!β`, so that identity of the remark is not a hypothesis here.

```lean
theorem cycleClass_mul_iff_cycleClass_externalProduct'
    [HasBinaryProducts ((SmoothProjective k).FullSubcategory)]
    (S : PoincareDualityPushforwardSetup.{u, v, w} k F) (Ch : ChowCycleData.{u, t} k)
    (cycleClass : ∀ (X : (SmoothProjective k).FullSubcategory) (r : ℤ),
      Ch.group X r →+ (S.H X).piece (2 * r))
    (cycleClass_gysin : ∀ {X Y : (SmoothProjective k).FullSubcategory} (f : X ⟶ Y) (r : ℤ)
      (β : Ch.group Y r),
      cycleClass X r (Ch.gysin f r β) = S.pullback f (2 * r) (cycleClass Y r β))
    (mul_eq : ∀ {Z : (SmoothProjective k).FullSubcategory} (r s : ℤ)
      (α : Ch.group Z r) (β : Ch.group Z s), Ch.mul r s α β =
        Ch.gysin (prod.lift (𝟙 Z) (𝟙 Z) : Z ⟶ Z ⨯ Z) (r + s) (Ch.externalProduct r s α β)) :
    (∀ (Z : (SmoothProjective k).FullSubcategory) (r s : ℤ)
        (α : Ch.group Z r) (β : Ch.group Z s),
        cycleClass Z (r + s) (Ch.mul r s α β) =
          (S.H Z).evenCup r s (cycleClass Z r α) (cycleClass Z s β)) ↔
      ∀ (Z W : (SmoothProjective k).FullSubcategory) (r s : ℤ)
        (α : Ch.group Z r) (β : Ch.group W s),
        cycleClass (Z ⨯ W) (r + s) (Ch.externalProduct r s α β) =
          (S.H (Z ⨯ W)).evenCup r s
            (S.pullback (prod.fst : Z ⨯ W ⟶ Z) (2 * r) (cycleClass Z r α))
            (S.pullback (prod.snd : Z ⨯ W ⟶ W) (2 * s) (cycleClass W s β))
```

**`Stacks.WeilCohomology.diagonalPullback_kunneth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Kunneth.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Kunneth.lean#L46). The attribute's comment: “diagonal_pullback_cup”.

> Pulling the Künneth exterior product `pr₁^*a ∪ pr₂^*b` back along the diagonal
> `Δ : X ⟶ X × X` gives the cup product `a ∪ b`.

```lean
theorem diagonalPullback_kunneth (k : Type u) [Field k] (F : Type v) [Field F]
    (H : (SmoothProjective k).FullSubcategory → ExternallyGradedAlgebra.{v, w} F)
    (pullback : ∀ {X Y : (SmoothProjective k).FullSubcategory},
      (X ⟶ Y) → ∀ i : ℤ, (H Y).piece i →ₗ[F] (H X).piece i)
    (pullback_id : ∀ (X) (i : ℤ), pullback (𝟙 X) i = LinearMap.id)
    (pullback_comp : ∀ {X Y Z} (f : X ⟶ Y) (g : Y ⟶ Z) (i : ℤ),
      pullback (f ≫ g) i = (pullback f i).comp (pullback g i))
    (pullback_mul : ∀ {X Y} (f : X ⟶ Y) (i j : ℤ) (a : (H Y).piece i) (b : (H Y).piece j),
      pullback f (i + j) ((H Y).mul i j a b) =
        (H X).mul i j (pullback f i a) (pullback f j b))
    (X : (SmoothProjective k).FullSubcategory) [HasBinaryProduct X X]
    (i j : ℤ) (a : (H X).piece i) (b : (H X).piece j) :
    pullback (prod.lift (𝟙 X) (𝟙 X) : X ⟶ X ⨯ X) (i + j)
        ((H (X ⨯ X)).mul i j
          (pullback (prod.fst : X ⨯ X ⟶ X) i a) (pullback (prod.snd : X ⨯ X ⟶ X) j b)) =
      (H X).mul i j a b
```

## Tag 0FGV, a definition

[Tag 0FGV](https://stacks.math.columbia.edu/tag/0FGV) in the Stacks Project.

**`Stacks.WeilCohomology.ClassicalWeilCohomologyTheory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalTheory.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalTheory.lean#L158).

> A classical Weil cohomology theory over an algebraically closed field `k` with coefficients
> in a field `F` of characteristic zero, for a given theory of Chow groups: the contravariant
> multiplicative graded-commutative cohomology theory and the trace maps satisfying Poincaré
> duality, together with the cycle class maps, the Künneth formula, and compatibility of the cycle
> class maps with Gysin pullback, proper pushforward, the intersection product and the class of a
> point.

```lean
structure ClassicalWeilCohomologyTheory (k : Type u) [Field k] [IsAlgClosed k]
    (F : Type v) [Field F] [CharZero F] (Ch : ChowCycleData.{u, t} k)
    extends PoincareDualityPushforwardSetup.{u, v, w} k F
```

**`Stacks.WeilCohomology.ClassicalWeilCohomology`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalTheoryChow.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalTheoryChow.lean#L351).

> **Stacks Project, Definition 0FGV.** A *classical Weil cohomology theory* over an
> algebraically closed field `k` with coefficients in a field `F` of characteristic zero: the data
> (D1), (D2), (D3) subject to the axioms (A), (B), (C) of Section 45.7.
>
> * (D1) and (D3), with axiom (A), Poincaré duality, are the parent structure
>   `Stacks.WeilCohomology.PoincareDualityPushforwardSetup`: a contravariant functor `H^*` from
>   smooth projective varieties over `k` to graded commutative `F`-algebras and the trace maps
>   `∫_X : H^{2d}(X) ⟶ F`, with finite dimensionality, perfectness of the trace pairings, vanishing
>   outside `[0, 2d]`, and `∫_X` an isomorphism.
> * (D2) is `cycleClass`: a group homomorphism `γ : CH^i(X) ⟶ H^{2i}(X)`, where
>   `CH^i(X) = CH_{d-i}(X)` is the Chow group of codimension-`i` cycles of the variety `X` of
>   dimension `d` (Stacks 0FE2), `CH_*` being the Chow groups of Stacks 02RW over `Spec k` with the
>   zero dimension function (Stacks 02QM).
> * (B) is `kunneth`.
> * (C)(a)–(d) are `cycleClass_gysinPullback`, `cycleClass_properChowPushforward`,
>   `cycleClass_diagonalIntersectionProduct` and `integration_cycleClass_point`, for the Gysin
>   pullback of Stacks 0FF3, the proper pushforward of Stacks 02R4, the intersection product
>   `α · β = Δ^!(α × β)` of Stacks 0FC0, and the fundamental class `[Spec k]`.
>
> The Gysin pullback `f^!β` and the intersection product `α · β` are classes in `CH_*(X)`, given
> by their parts in each dimension; the identities `γ(f^!β) = f^*γ(β)` and
> `γ(α · β) = γ(α) ∪ γ(β)` of `H^*(X) = ⨁_n H^n(X)` are stated in each degree `2j`, the right-hand
> sides being homogeneous of degrees `2i` and `2(r + s)`. Since every class of
> `CH^*(Y) = ⨁_i CH^i(Y)` is a finite sum of homogeneous classes and all the maps involved are
> additive (the product biadditive), the axioms are stated for homogeneous classes.

```lean
structure ClassicalWeilCohomology (k : Type u) [Field k] [IsAlgClosed k]
    (F : Type v) [Field F] [CharZero F]
    extends PoincareDualityPushforwardSetup.{u, v, w} k F
```

## Tag 0FGW, a lemma

[Tag 0FGW](https://stacks.math.columbia.edu/tag/0FGW) in the Stacks Project.

**`Stacks.WeilCohomology.integration_cycleClass_codimensionClassOfZeroCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalTraceDegree.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalTraceDegree.lean#L217).

> **Stacks Project, Tag 0FGW.** Let `X` be a smooth projective variety of dimension `d`. Then
> `∫_X γ(α) = deg(α)` for every zero cycle class `α ∈ CH_0(X) = CH^d(X)`: the composite
> `CH^d(X) → H^{2d}(X) → F` of the cycle class map and the trace is the degree of zero cycles
> (Chow Homology, Section 0AZ0) followed by `ℤ → F`.
>
> Chow groups graded by codimension are `CH^d(X) = ∏_e CH_{e-d}(X_e)`, the product over the open
> and closed parts `X_e` of `X` of dimension `e`; a variety of dimension `d` is its own part `X_d`,
> so a zero cycle class on `X` is a class `α ∈ CH_0(X_d)`, and its class in `CH^d(X)` is
> `Stacks.WeilCohomology.codimensionClassOfZeroCycle α`. The degree is `Stacks.Chow.chowDegree`
> (Stacks 0AZ1).

```lean
theorem integration_cycleClass_codimensionClassOfZeroCycle
    (X : (SmoothProjective k).FullSubcategory)
    (α : chowGroup (fieldChowSituation k)
      (partBase ((SmoothProjective.toSchemeCat k).obj X).obj.hom (T.dimension X)) 0) :
    haveI := (isClopenDecomposition_dimPart
      ((SmoothProjective.toSchemeCat k).obj X).obj.hom).isProper_ι (T.dimension X)
    T.integration X (T.cycleClass X (T.dimension X)
        (codimensionClassOfZeroCycle (X := (SmoothProjective.toSchemeCat k).obj X) α)) =
      (chowDegree (fieldChowSituation k) (fieldChowSituation_dimensionFunction k)
        (partBase ((SmoothProjective.toSchemeCat k).obj X).obj.hom (T.dimension X)) default α :
        F)
```

## Tag 0FGX, a lemma

[Tag 0FGX](https://stacks.math.columbia.edu/tag/0FGX) in the Stacks Project.

**`Stacks.WeilCohomology.ChowClassicalWeilCohomologyTheory.integration_mul_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalKunnethTrace.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalKunnethTrace.lean#L415).

> **Stacks Project, Tag 0FGX.** Let `H^*` be a classical Weil cohomology theory and let `X` and
> `Y` be smooth projective varieties. Then `∫_{X × Y} = ∫_X ⊗ ∫_Y`: for `P` a fibre product of `X`
> and `Y` over `k`, with projections `p` and `q`, and classes `a ∈ H^{2 dim X}(X)`,
> `b ∈ H^{2 dim Y}(Y)`, `∫_P p^*a ∪ q^*b = ∫_X a · ∫_Y b`.
>
> The source reads `∫_X ⊗ ∫_Y` through the Künneth isomorphism `H^*(X) ⊗ H^*(Y) ≅ H^*(X × Y)`,
> `a ⊗ b ↦ p^*a ∪ q^*b`, on the top piece `H^{2 dim X}(X) ⊗ H^{2 dim Y}(Y)` of
> `H^{2(dim X + dim Y)}(X × Y)`, which is this identity. The extension to the other Künneth
> components, where `∫_X ⊗ ∫_Y` vanishes, is
> `Stacks.WeilCohomology.PoincareDualityPushforwardSetup.traceExtension_mul_pullback`.
>
> As in the source, `H^{2 dim X}(X)` and `H^{2 dim Y}(Y)` are lines, so it suffices to evaluate on
> one pair of classes. The proof takes `γ([x])` for a `k`-point `x` of `X` and any class `v` with
> `∫_Y v = 1`, and computes `∫_P p^*γ([x]) ∪ q^*v = ∫_Y v` through the fibre `x × Y`
> (`integration_mul_pullback_cycleClass_point`); the source instead uses the class
> `γ([(x, y)]) = p^*γ([x]) ∪ q^*γ([y])` of a point of `X × Y`.

```lean
theorem integration_mul_pullback (hP : IsPullback p.hom.left q.hom.left X.obj.hom Y.obj.hom)
    (a : (T.H X).piece (2 * (T.dimension X : ℤ))) (b : (T.H Y).piece (2 * (T.dimension Y : ℤ))) :
    T.integration P (ExternallyGraded.degreeCast (R := F) (X := (T.H P).piece)
        (show 2 * (T.dimension X : ℤ) + 2 * (T.dimension Y : ℤ) = 2 * (T.dimension P : ℤ) by
          rw [T.dimension_eq_add p q hP]; push_cast; ring)
        ((T.H P).mul _ _ (T.pullback p _ a) (T.pullback q _ b))) =
      T.integration X a * T.integration Y b
```

**`Stacks.WeilCohomology.ChowClassicalWeilCohomologyTheory.integration_comp_kunnethMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalKunnethTrace.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalKunnethTrace.lean#L433). The attribute's comment: “as linear maps on H^*(X) ⊗ H^*(Y), through the Künneth map”.

> **Stacks Project, Tag 0FGX**, as an identity of linear maps
> `H^*(X) ⊗_F H^*(Y) → F`. Let `∫_X : H^*(X) → F` be the trace map on the piece of degree
> `2 dim X`, extended by zero to the other pieces. Then `∫_{X × Y}`, composed with the Künneth map
> `H^*(X) ⊗_F H^*(Y) → H^*(X × Y)`, `a ⊗ b ↦ p^*a ∪ q^*b`, is `∫_X ⊗ ∫_Y`.

```lean
theorem integration_comp_kunnethMap
    (hP : IsPullback p.hom.left q.hom.left X.obj.hom Y.obj.hom) :
    ((T.integration P).toLinearMap ∘ₗ
        DirectSum.component F ℤ (T.H P).piece (2 * (T.dimension P : ℤ))) ∘ₗ
      kunnethMap (T.H X) (T.H Y) (T.H P) (fun i ↦ T.pullback p i) (fun j ↦ T.pullback q j) =
    TensorProduct.lift ((LinearMap.mul F F).compl₁₂
      ((T.integration X).toLinearMap ∘ₗ
        DirectSum.component F ℤ (T.H X).piece (2 * (T.dimension X : ℤ)))
      ((T.integration Y).toLinearMap ∘ₗ
        DirectSum.component F ℤ (T.H Y).piece (2 * (T.dimension Y : ℤ))))
```

## Tag 0FGY, a lemma

[Tag 0FGY](https://stacks.math.columbia.edu/tag/0FGY) in the Stacks Project.

**`Stacks.WeilCohomology.ChowClassicalWeilCohomologyTheory.pushforward_mul_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalPushforwardProduct.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalPushforwardProduct.lean#L60).

> **Stacks Project, Tag 0FGY.** Let `H^*` be a classical Weil cohomology theory and let `P`,
> with projections `p : P ⟶ X` and `q : P ⟶ Y`, be the product of smooth projective varieties `X`
> and `Y`. For `a` of degree `i` on `X` and `b` of degree `j` on `Y`, the pushforward along the
> second projection sends `a ⊗ b = p^*a ∪ q^*b` to `(∫_X a) b`: to `∫_X a • b` when `i = 2 dim X`,
> and to zero otherwise, where `∫_X a` is zero.

```lean
theorem pushforward_mul_pullback (p : P ⟶ X) (q : P ⟶ Y)
    (hP : IsPullback p.hom.left q.hom.left X.obj.hom Y.obj.hom)
    (i j : ℤ) (a : (T.H X).piece i) (b : (T.H Y).piece j) :
    T.pushforward q (2 * (T.dimension P : ℤ) - (i + j))
        (ExternallyGraded.degreeCast (R := F) (X := (T.H P).piece)
          (show i + j = 2 * (T.dimension P : ℤ) - (2 * (T.dimension P : ℤ) - (i + j)) by omega)
          ((T.H P).mul i j (T.pullback p i a) (T.pullback q j b))) =
      if h : i = 2 * (T.dimension X : ℤ) then
        T.integration X (ExternallyGraded.degreeCast (R := F) (X := (T.H X).piece) h a) •
          ExternallyGraded.degreeCast (R := F) (X := (T.H Y).piece)
            (show j = 2 * (T.dimension Y : ℤ) - (2 * (T.dimension P : ℤ) - (i + j)) by
              rw [T.dimension_eq_add p q hP]; push_cast; omega) b
      else 0
```

## Tag 0FGZ, a lemma

[Tag 0FGZ](https://stacks.math.columbia.edu/tag/0FGZ) in the Stacks Project.

**`Stacks.WeilCohomology.ChowClassicalWeilCohomologyTheory.integration_mul_diagonalKunnethCoordinate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalDiagonalBasis.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalDiagonalBasis.lean#L436).

> **Stacks Project, Tag 0FGZ.** Let `H^*` be a classical Weil cohomology theory and `X` a smooth
> projective variety of dimension `d`. Choose a basis `e_{i, j}` of `H^i(X)` over `F` and, using
> Künneth, write `γ([Δ]) = ∑_i ∑_j e_{i, j} ⊗ e'_{2d - i, j}` in `⨁_i H^i(X) ⊗_F H^{2d - i}(X)`
> with `e'_{2d - i, j} ∈ H^{2d - i}(X)`. Then `∫_X e_{i, j} ∪ e'_{2d - i, j'} = (-1)^i δ_{jj'}`.
>
> The product `X × X` is a smooth projective variety `P` with projections `p, q : P ⟶ X`
> exhibiting it as the fibre product over `k`, and the diagonal is `δ : X ⟶ P` with
> `δ ≫ p = δ ≫ q = 𝟙`; `[Δ] ∈ CH^d(P)` is the class of the closed subscheme `δ(X)`, and the
> decomposition of `γ([Δ])` is read through the inverse of the Künneth isomorphism of axiom `(B)`.
> The hypothesis `hdecomp` is the `(i, 2d - i)` component of the source's decomposition, for the one
> degree `i` the conclusion concerns; `(-1)^i` is `gradedSign F i`.

```lean
theorem integration_mul_diagonalKunnethCoordinate {X P : (SmoothProjective k).FullSubcategory}
    (p q : P ⟶ X) (hpq : IsPullback p.hom.left q.hom.left X.obj.hom X.obj.hom) (δ : X ⟶ P)
    (hδp : δ ≫ p = 𝟙 X) (hδq : δ ≫ q = 𝟙 X) (i : ℤ) {J : Type t} [Fintype J] [DecidableEq J]
    (e : Module.Basis J F ((T.H X).piece i))
    (e' : J → (T.H X).piece (2 * (T.dimension X : ℤ) - i))
    (hdecomp :
      haveI := SmoothProjective.isClosedImmersion_of_section p δ hδp
      DirectSum.component F (ℤ × ℤ) (fun ij => (T.H X).piece ij.1 ⊗[F] (T.H X).piece ij.2)
          (i, 2 * (T.dimension X : ℤ) - i)
          (TensorProduct.directSum F F (fun n : ℤ => (T.H X).piece n)
            (fun n : ℤ => (T.H X).piece n)
            ((T.kunnethEquiv X X P p q hpq).symm
              (DirectSum.lof F ℤ (fun n => (T.H P).piece n) (2 * (T.dimension X : ℤ))
                (T.cycleClass P (T.dimension X)
                  (closedSubschemeClass ((SmoothProjective.toSchemeCat k).obj P).obj.hom δ.hom.left
          (T.dimension X)))))) =
        ∑ j : J, e j ⊗ₜ[F] e' j)
    (j j' : J) :
    T.integration X (ExternallyGraded.degreeCast (R := F) (X := (T.H X).piece)
        (show i + (2 * (T.dimension X : ℤ) - i) = 2 * (T.dimension X : ℤ) by omega)
        ((T.H X).mul i (2 * (T.dimension X : ℤ) - i) (e j) (e' j'))) =
      gradedSign F i * (if j = j' then 1 else 0)
```

## Tag 0FH0, a lemma

[Tag 0FH0](https://stacks.math.columbia.edu/tag/0FH0) in the Stacks Project.

**`Stacks.WeilCohomology.degree_diagonal_mul_eq_degree_chernCap_tangentSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalDiagonalSelfIntersection.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalDiagonalSelfIntersection.lean#L250). The attribute's comment: “the equality on the right: deg([Δ] · [Δ]) = deg(c_d(T_X) ∩ [X]), for X × X any fibre product P of X with itself over k and Δ the diagonal section”. References: SGA 6 XIII (5.3), “partial”.

> **Stacks Project, Tag 0FH0**, the equality on the right: for a smooth projective variety `X`
> of dimension `d` over `k`, `deg([Δ] · [Δ]) = deg(c_d(𝒯_X) ∩ [X])`.
>
> The product `X × X` is a smooth projective variety `P` with projections `p, q : P ⟶ X`
> exhibiting it as the fibre product over `k`, the diagonal is `δ : X ⟶ P` with
> `δ ≫ p = δ ≫ q = 𝟙`, `[Δ] ∈ CH^d(P)` is the class of the closed subscheme `δ(X)`
> (`Stacks.WeilCohomology.closedSubschemeClass`), `·` is the intersection product of Chapter 42
> (Stacks 0FC0) and `deg` the degree of zero cycles (Stacks 0AZ1) on `CH^{2d}(P) = CH_0(P)` and on
> `CH_0(X)`. `𝒯_X` is the tangent sheaf
> (`Stacks.WeilCohomology.SmoothProjectiveScheme.tangentSheaf`), finite locally free
> of rank `d`, and `c_d(𝒯_X) ∩ -` is the Chern class cap product of Stacks 02U5.
>
> The proof is the source's: `[Δ] · [Δ] = δ_*(δ^![Δ])` (Stacks 0FFE), `δ_*` preserves degrees, and
> `δ^![Δ] = c_d(𝒩) ∩ [X]` for the normal bundle `𝒩` of `δ` (the excess intersection formula,
> Stacks 0FBM), which is `𝒯_X` because the conormal sheaf of the diagonal is `Ω_{X/k}` (Stacks
> 08S2). The theory `H^*` of the source plays no role in this equality, so it is not assumed, and
> neither is `k` algebraically closed.

```lean
theorem degree_diagonal_mul_eq_degree_chernCap_tangentSheaf
    (X P : (SmoothProjective k).FullSubcategory) {d : ℕ}
    (hd : topologicalKrullDim X.obj.left = (d : WithBot ℕ∞)) (p q : P ⟶ X)
    (hpq : IsPullback p.hom.left q.hom.left X.obj.hom X.obj.hom) (δ : X ⟶ P)
    (hδp : δ ≫ p = 𝟙 X) (hδq : δ ≫ q = 𝟙 X) :
    haveI := SmoothProjective.isClosedImmersion_of_section p δ hδp
    haveI := SmoothProjectiveScheme.isFiniteLocallyFreeOfRank_tangentSheaf
      ((SmoothProjective.toSchemeCat k).obj X)
      (SmoothProjective.relativeDimension_hom X hd)
    codimensionDegree ((SmoothProjective.toSchemeCat k).obj P) (d + d)
        (codimensionChowGroupCongr _ (by push_cast; rfl) ((chowCycleData k).mul d d
          (closedSubschemeClass ((SmoothProjective.toSchemeCat k).obj P).obj.hom δ.hom.left d)
          (closedSubschemeClass ((SmoothProjective.toSchemeCat k).obj P).obj.hom δ.hom.left d))) =
      chowDegree (fieldChowSituation k) (fieldChowSituation_dimensionFunction k) X.obj.hom
        default (chowGroupDegreeEquiv _ _ (sub_self (d : ℤ))
          (GenuineChern.chernCap (fieldChowSituation k) d X.obj.hom
            (SmoothProjectiveScheme.tangentSheaf ((SmoothProjective.toSchemeCat k).obj X)) d
            (Fin.last d) (fundamentalChowClass (fieldChowSituation k) X.obj.hom d)))
```

**`Stacks.WeilCohomology.ChowClassicalWeilCohomologyTheory.eulerCharacteristic_eq_degree_diagonal_mul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalEulerCharacteristic.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalEulerCharacteristic.lean#L274). The attribute's comment: “the equality on the left: Σ (-1)^i dim H^i(X) = deg([Δ] · [Δ])”.

> **Stacks Project, Tag 0FH0**, the equality on the left: for a classical Weil cohomology theory
> `H^*` and a smooth projective variety `X` of dimension `d`,
> `∑_{i = 0}^{2d} (-1)^i dim_F H^i(X) = deg([Δ] · [Δ])`.
>
> The product `X × X` is a smooth projective variety `P` with projections `p, q : P ⟶ X`
> exhibiting it as the fibre product over `k`, the diagonal is `δ : X ⟶ P` with
> `δ ≫ p = δ ≫ q = 𝟙`, `[Δ] ∈ CH^d(P)` is the class of the closed subscheme `δ(X)`, `·` is the
> intersection product of Chapter 42 and `deg` the degree of zero cycles on
> `CH^{2d}(P) = CH_0(P)` (`Stacks.WeilCohomology.codimensionDegree`).
>
> The proof is the source's: `deg([Δ] · [Δ]) = ∫_P γ([Δ] · [Δ])` (Stacks 0FGW), which is
> `∫_P γ([Δ]) ∪ δ_*1 = ∫_X δ^*γ([Δ])` by axiom (C)(c) and `γ([Δ]) = δ_*1`; writing
> `γ([Δ]) = ∑ e_{i,j} ⊗ e'_{2d-i,j}` through the Künneth isomorphism, `δ^*` is the cup product, and
> `∑_{i,j} ∫_X e_{i,j} ∪ e'_{2d-i,j} = ∑_i (-1)^i dim H^i(X)` by Stacks 0FGZ.

```lean
theorem eulerCharacteristic_eq_degree_diagonal_mul :
    haveI := SmoothProjective.isClosedImmersion_of_section p δ hδp
    ∑ i ∈ Finset.range (2 * T.dimension X + 1),
        (-1 : ℤ) ^ i * (Module.finrank F ((T.H X).piece (i : ℤ)) : ℤ) =
      codimensionDegree ((SmoothProjective.toSchemeCat k).obj P) (T.dimension X + T.dimension X)
        (codimensionChowGroupCongr _ (by push_cast; rfl)
          ((chowCycleData k).mul (T.dimension X) (T.dimension X)
            (closedSubschemeClass ((SmoothProjective.toSchemeCat k).obj P).obj.hom δ.hom.left
              (T.dimension X))
            (closedSubschemeClass ((SmoothProjective.toSchemeCat k).obj P).obj.hom δ.hom.left
              (T.dimension X))))
```

**`Stacks.WeilCohomology.ChowClassicalWeilCohomologyTheory.eulerCharacteristic_eq_degree_diagonal_mul_eq_degree_chernCap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalEulerCharacteristic.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalEulerCharacteristic.lean#L340).

> **Stacks Project, Tag 0FH0.** Let `H^*` be a classical Weil cohomology theory (Stacks 0FGV)
> and `X` a smooth projective variety of dimension `d`. Then
> `∑_{i = 0}^{2d} (-1)^i dim_F H^i(X) = deg([Δ] · [Δ]) = deg(c_d(𝒯_X) ∩ [X])`.
>
> The product `X × X` is a smooth projective variety `P` with projections `p, q : P ⟶ X`
> exhibiting it as the fibre product over `k`, and the diagonal is `δ : X ⟶ P` with
> `δ ≫ p = δ ≫ q = 𝟙`; `[Δ]`, the intersection product, the degree and `c_d(𝒯_X) ∩ -` are those of
> `ChowClassicalWeilCohomologyTheory.eulerCharacteristic_eq_degree_diagonal_mul`
> (the equality on the left) and
> `Stacks.WeilCohomology.degree_diagonal_mul_eq_degree_chernCap_tangentSheaf`
> (the equality on the right).

```lean
theorem eulerCharacteristic_eq_degree_diagonal_mul_eq_degree_chernCap :
    haveI := SmoothProjective.isClosedImmersion_of_section p δ hδp
    haveI := SmoothProjectiveScheme.isFiniteLocallyFreeOfRank_tangentSheaf
      ((SmoothProjective.toSchemeCat k).obj X)
      (SmoothProjective.relativeDimension_hom X (T.dimension_eq X))
    ∑ i ∈ Finset.range (2 * T.dimension X + 1),
        (-1 : ℤ) ^ i * (Module.finrank F ((T.H X).piece (i : ℤ)) : ℤ) =
      codimensionDegree ((SmoothProjective.toSchemeCat k).obj P) (T.dimension X + T.dimension X)
        (codimensionChowGroupCongr _ (by push_cast; rfl)
          ((chowCycleData k).mul (T.dimension X) (T.dimension X)
            (closedSubschemeClass ((SmoothProjective.toSchemeCat k).obj P).obj.hom δ.hom.left
              (T.dimension X))
            (closedSubschemeClass ((SmoothProjective.toSchemeCat k).obj P).obj.hom δ.hom.left
              (T.dimension X)))) ∧
    codimensionDegree ((SmoothProjective.toSchemeCat k).obj P) (T.dimension X + T.dimension X)
        (codimensionChowGroupCongr _ (by push_cast; rfl)
          ((chowCycleData k).mul (T.dimension X) (T.dimension X)
            (closedSubschemeClass ((SmoothProjective.toSchemeCat k).obj P).obj.hom δ.hom.left
              (T.dimension X))
            (closedSubschemeClass ((SmoothProjective.toSchemeCat k).obj P).obj.hom δ.hom.left
              (T.dimension X)))) =
      chowDegree (fieldChowSituation k) (fieldChowSituation_dimensionFunction k) X.obj.hom
        default (chowGroupDegreeEquiv _ _ (sub_self (T.dimension X : ℤ))
          (GenuineChern.chernCap (fieldChowSituation k) (T.dimension X) X.obj.hom
            (SmoothProjectiveScheme.tangentSheaf ((SmoothProjective.toSchemeCat k).obj X))
            (T.dimension X) (Fin.last (T.dimension X))
            (fundamentalChowClass (fieldChowSituation k) X.obj.hom (T.dimension X))))
```

## Tag 0FH1, a lemma

[Tag 0FH1](https://stacks.math.columbia.edu/tag/0FH1) in the Stacks Project.

**`Stacks.WeilCohomology.WeilRealization.toPreClassical`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/RealizationPreClassical.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/Concrete/RealizationPreClassical.lean#L70). The attribute's comment: “a Q-linear functor G : M_k → graded F-vector spaces of symmetric monoidal categories with G(1(1)) nonzero only in degree -2 gives data (D1), (D2), (D3) satisfying (A), (B), (C) except possibly (A)(c) and (A)(d)”.

> **Stacks Project, Lemma 0FH1.** Let `k` be algebraically closed and `F` of characteristic
> `0`. A `ℚ`-linear functor `G : M_k ⥤ graded F-vector spaces` of symmetric monoidal categories
> with `G(𝟏(1))` nonzero only in degree `-2` gives data (D1), (D2), (D3) satisfying all of (A),
> (B), (C) except possibly (A)(c) and (A)(d): on a smooth projective variety `X`,
> `H^*(X) = G(h(X))`, the cycle class map is `α ↦ G(a_α)(e_{-r})` and the trace is
> `x ↦ G([X])(x ⊗ e_d)`, for generators `e_n` of `G(𝟏(n))` with `e_1` a basis of `G^{-2}(𝟏(1))`.

```lean
def toPreClassical : PreClassicalWeilCohomologyTheory.{u, w, w, u} k F (chowCycleData k)
```

## Tag 0FH2, a lemma

[Tag 0FH2](https://stacks.math.columbia.edu/tag/0FH2) in the Stacks Project.

**`Stacks.WeilCohomology.ClassicalWeilCohomologyTheory.exists_motiveFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalExtension/Realization.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalExtension/Realization.lean#L66). The attribute's comment: “a classical Weil cohomology theory gives a Q-linear symmetric monoidal functor G : M_k -> graded F-vector spaces with H^*(X) = G(h(X))”.

> **Stacks Project, Tag 0FH2.** Let `k` be an algebraically closed field, `F` a field of
> characteristic zero and `H^*` a classical Weil cohomology theory. Then there is a `ℚ`-linear
> functor `G : M_k ⥤ graded F-vector spaces` of symmetric monoidal categories (for the
> Koszul-signed symmetry of Stacks, Homology, Example 0FFX) with `H^*(X) = G(h(X))`, naturally in
> the smooth projective variety `X` (pullbacks `f^*` corresponding to `G(h(f))`).

```lean
theorem exists_motiveFunctor :
    ∃ (G : ChowMotiveCat k ⥤ GradedObject ℤ (ModuleCat.{v} F))
      (_ : @Functor.Braided (ChowMotiveCat k) _ _ _ (GradedObject ℤ (ModuleCat.{v} F)) _ _
        GradedObject.koszulBraidedCategory G) (_ : G.Additive) (_ : Functor.Linear ℚ G),
      Nonempty ((SmoothProjective.toSchemeCat k).op ⋙ ChowMotiveCat.h k ⋙ G ≅
        T.toPre.toPoincarePairingSetup.cohomologyFunctor)
```

## Tag 0FH3, a proposition

[Tag 0FH3](https://stacks.math.columbia.edu/tag/0FH3) in the Stacks Project.

**`Stacks.WeilCohomology.ClassicalWeilCohomologyTheory.exists_classicalMotiveRealization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalWeilRealization.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalWeilRealization.lean#L53). The attribute's comment: “a classical Weil cohomology theory comes from a Q-linear symmetric monoidal G : M_k → graded F-vector spaces with F[2] ≅ G(1(1)), G(h(X)) in nonnegative degrees and dim G⁰(h(X)) = 1, with H^*(X) = G(h(X)) naturally in X”.

> **Stacks Project, Tag 0FH3, from cohomology to a realization.** A classical Weil cohomology
> theory `H^*` (Stacks 0FGV, over the Chow groups of Chapter 42) comes from a realization of Chow
> motives: there is a `ℚ`-linear functor `G : M_k ⥤ graded F-vector spaces` of symmetric monoidal
> categories with an isomorphism `F[2] ≅ G(𝟏(1))`, `G(h(X))` in nonnegative degrees and
> `dim_F G⁰(h(X)) = 1` for every smooth projective variety `X`, and `H^*(X) = G(h(X))` naturally in
> `X`. The functor is that of Stacks 0FH2 (`ClassicalWeilCohomologyTheory.motiveFunctor`);
> `G(𝟏(1))` is a line in degree `-2`, and conditions (1), (2) are axioms (A)(c), (A)(d) and
> Poincaré duality transported along `H^*(X) = G(h(X))`.

```lean
theorem ClassicalWeilCohomologyTheory.exists_classicalMotiveRealization
    (T : ClassicalWeilCohomologyTheory.{u, v, v, u} k F (chowCycleData k)) :
    ∃ R : ClassicalMotiveRealization k F,
      Nonempty (T.toPre.toPoincarePairingSetup.MotiveComparison R.G)
```

**`Stacks.WeilCohomology.ClassicalMotiveRealization.exists_classicalWeilCohomologyTheory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalWeilRealization.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ClassicalWeilRealization.lean#L109). The attribute's comment: “a Q-linear symmetric monoidal G : M_k → graded F-vector spaces with F[2] ≅ G(1(1)), G(h(X)) in nonnegative degrees and dim G⁰(h(X)) = 1 comes from a classical Weil cohomology theory, with H^*(X) = G(h(X)) naturally in X”.

> **Stacks Project, Tag 0FH3, from a realization to cohomology.** Conversely, a `ℚ`-linear
> functor `G : M_k ⥤ graded F-vector spaces` of symmetric monoidal categories with an isomorphism
> `F[2] ≅ G(𝟏(1))` such that `G(h(X))` lives in nonnegative degrees and `dim_F G⁰(h(X)) = 1` for
> every smooth projective variety `X` comes from a classical Weil cohomology theory (Stacks 0FGV,
> over the Chow groups of Chapter 42): there is one with `H^*(X) = G(h(X))` naturally in `X`. By
> Stacks 0FHK, `H^*(X) = G(h(X))` gives data (D0)–(D3) satisfying (A), (B), (C)
> (`WeilRealization.toWeilDataAxioms`); conditions (1) and (2) give axioms (A)(c) and (A)(d) on
> their restriction to varieties.

```lean
theorem ClassicalMotiveRealization.exists_classicalWeilCohomologyTheory
    (R : ClassicalMotiveRealization k F) :
    ∃ T : ClassicalWeilCohomologyTheory.{u, v, v, u} k F (chowCycleData k),
      Nonempty (T.toPre.toPoincarePairingSetup.MotiveComparison R.G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 45.7, Tag 0FGS](https://stacks.math.columbia.edu/tag/0FGS)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

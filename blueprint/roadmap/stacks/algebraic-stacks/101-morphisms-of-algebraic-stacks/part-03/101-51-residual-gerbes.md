---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_of_isGerbeOver, AlgebraicGeometry.Stack.isResidualGerbeAt_inverseImage_of_isGerbeOver, AlgebraicGeometry.Stack.residualGerbe_factorization_of_isReducedStack, AlgebraicGeometry.Stack.factorsThroughSubstack_residualGerbe_of_isClosed_singleton, AlgebraicGeometry.Stack.exists_isResidualGerbeAt_and_isClosed_singleton_iff_isClosedImmersion
statement: formalized
proof: formalized
---

# 101.51 Residual gerbes

Section 101.51 of the Stacks Project, [Tag 0H23](https://stacks.math.columbia.edu/tag/0H23). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H24, a lemma

[Tag 0H24](https://stacks.math.columbia.edu/tag/0H24) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasSingletonPointMonomorphism_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeResidualGerbe.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeResidualGerbe.lean#L122). The attribute's comment: “existence clause: condition (1) of Stacks 06MT transports along a gerbe”.

> **The existence clause of Stacks 0H24.** Let `f : 𝒳 ⟶ 𝒴` make `𝒳` a gerbe over `𝒴` and let
> `x` be a point of `𝒳`. If condition (1) of **Stacks 06MT** holds for `𝒴` at the image of `x`,
> then it holds for `𝒳` at `x`; that is, the residual gerbe of `𝒳` at `x` exists as soon as the
> residual gerbe of `𝒴` at `f(x)` does.
>
> Writing `i : 𝒵 ⟶ 𝒴` for the one-point monomorphism over `f(x)`, the witness is the 2-fibre
> product `𝒳 ×_𝒴 𝒵` with its projection to `𝒳`, which is a monomorphism by
> `AlgebraicGeometry.Stack.AlgebraicStacks.isMonomorphism_fst_twoFibreProductSquareAlgebraicStacks`.
> Its projection to `𝒵` is again a gerbe (**Stacks 06QE**), hence injective on points, and `𝒵` has
> a single point; so the apex has at most one point, and **Stacks 04XH** produces one lying over
> `x`. The identification of the residual gerbe with that 2-fibre product is not proved.

```lean
theorem hasSingletonPointMonomorphism_of_isGerbeOver
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsGerbeOver B S hS f)
    (x : points B S hS 𝒳.val.val (Classical.choose 𝒳.property))
    (hy : HasSingletonPointMonomorphism B S hS 𝒴
      (pointsMap B S hS 𝒳.val.val (Classical.choose 𝒳.property)
        (Classical.choose 𝒴.property) f.hom.hom x)) :
    HasSingletonPointMonomorphism B S hS 𝒳 x
```

**`AlgebraicGeometry.Stack.isResidualGerbeAt_inverseImage_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GerbeResidualGerbeFibreProduct.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GerbeResidualGerbeFibreProduct.lean#L110).

> **Stacks 0H24.** Let `π : 𝒳 ⟶ 𝒴` be a 1-morphism of algebraic stacks over `S` making `𝒳` a
> gerbe over `𝒴`, let `x` be a point of `𝒳` and let `y` be its image in `|𝒴|`. Assume the residual
> gerbe `𝒵_y ⊂ 𝒴` of `𝒴` at `y` exists, cut out by the object property `P` of `𝒴` (the
> specification `AlgebraicGeometry.Stack.IsResidualGerbeAt` of Stacks 06MT). Then
> `𝒵_x = 𝒵_y ×_𝒴 𝒳` is the residual gerbe of `𝒳` at `x`:
>
> * the inverse image `P ∘ π` of `P` meets the residual-gerbe specification of `𝒳` at `x`, so the
>   residual gerbe `𝒵_x` of `𝒳` at `x` exists and is the strictly full subcategory of `𝒳` on the
>   objects sent into `𝒵_y`; and
> * the square formed by the 1-morphism `𝒵_x ⟶ 𝒵_y` induced by `π`, the inclusion `𝒵_x ⟶ 𝒳`, and
>   the inclusion `𝒵_y ⟶ 𝒴`, which commutes on the nose, is a 2-fibre product: `𝒵_x` with its
>   inclusion into `𝒳` is the 2-fibre product `𝒵_y ×_𝒴 𝒳`.
>
> Following the source: the inverse image is algebraic and is the 2-fibre product
> (`AlgebraicGeometry.Stack.isAlgebraicStack_inverseImage`,
> `AlgebraicGeometry.Stack.isTwoFibreProduct_inverseImageSquare`); its projection to `𝒵_y` is a
> base change of `π`, hence smooth (**Stacks 0DN8**, **Stacks 075W**) and a gerbe
> (**Stacks 06QE**), so the apex is reduced and locally Noetherian as `𝒵_y` is (**Stacks 04YF**,
> **Stacks 06R6**) and has exactly one point, which lies over `x` (**Stacks 04XH** and injectivity
> of a gerbe on points).

```lean
theorem isResidualGerbeAt_inverseImage_of_isGerbeOver
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ 𝒴)
    (hf : AlgebraicStacks.IsGerbeOver B S hS f)
    (x : points B S hS 𝒳.val.val (Classical.choose 𝒳.property))
    (P : ObjectProperty 𝒴.val.val.obj)
    (hP : IsResidualGerbeAt B S hS 𝒴
      (pointsMap B S hS 𝒳.val.val (Classical.choose 𝒳.property)
        (Classical.choose 𝒴.property) f.hom.hom x) P) :
    ∃ hQ : IsResidualGerbeAt B S hS 𝒳 x (P.inverseImage f.hom.hom.toFunctor),
      Nonempty (Bicategory.IsTwoFibreProduct
        ({ pt := residualGerbe B S hS 𝒳 x _ hQ
           fst := residualGerbeMap B S hS f hQ.2.choose hP.2.choose (fun _ h => h)
           snd := residualGerbeInclusion B S hS 𝒳 x _ hQ
           iso := Iso.refl _ } :
          Bicategory.TwoCommSq (residualGerbeInclusion B S hS 𝒴 _ P hP) f))
```

## Tag 0H25, a lemma

[Tag 0H25](https://stacks.math.columbia.edu/tag/0H25) in the Stacks Project.

**`AlgebraicGeometry.Stack.residualGerbe_factorization_of_isReducedStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedResidualGerbeFactorization.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ReducedResidualGerbeFactorization.lean#L269).

> **A reduced stack over a point factors through the residual gerbe.** Let `f : 𝒴 ⟶ 𝒳` be a
> 1-morphism of algebraic stacks over `S` and let `x ∈ |𝒳|`. Assume that
> 1. `𝒳` is decent or locally Noetherian (or both),
> 2. the inertia projection `I_𝒳 ⟶ 𝒳` is quasi-compact,
> 3. `|f|(|𝒴|)` is contained in `{x}`, and
> 4. `𝒴` is reduced.
>
> Then the residual gerbe `𝒵_x` of `𝒳` at `x` exists and `f` factors through it. Precisely:
> * the residual gerbe of `𝒳` at `x` exists: some reduced algebraic stack admits a monomorphism to
>   `𝒳` whose space of points is a single point lying over `x`;
> * `f` factors, up to a 2-isomorphism, through every monomorphism `𝒵 ⟶ 𝒳` from an algebraic stack
>   with a single point lying over `x`, in particular through every residual gerbe so presented;
> * `f` factors strictly through the inclusion of every residual gerbe of `𝒳` at `x`, the strictly
>   full subcategory `residualGerbe`.

```lean
theorem residualGerbe_factorization_of_isReducedStack
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒴 ⟶ 𝒳) (x : AlgebraicStacks.points B S hS 𝒳)
    (h1 : IsDecent B S hS 𝒳.val ∨ IsLocallyNoetherianStack B S hS 𝒳)
    (h2 : IsQuasiCompactMorphism.{u, w} B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳))
    (h3 : Set.range (AlgebraicStacks.pointsMap B S hS f) ⊆ {x})
    (h4 : IsReducedStack B S hS 𝒴) :
    HasReducedSingletonPointMonomorphism B S hS 𝒳 x ∧
      (∀ (𝒵 : AlgebraicStacks.{u, w} B S hS) (m : 𝒵 ⟶ 𝒳),
        AlgebraicStacks.IsMonomorphism B S hS m → HasUniquePointOver B S hS m x →
          ∃ g : 𝒴 ⟶ 𝒵, Nonempty (g ≫ m ≅ f)) ∧
      ∀ (P : ObjectProperty 𝒳.val.val.obj) (hP : IsResidualGerbeAt B S hS 𝒳 x P),
        ∃ g : 𝒴 ⟶ residualGerbe B S hS 𝒳 x P hP,
          g ≫ residualGerbeInclusion B S hS 𝒳 x P hP = f
```

## Tag 0H26, a lemma

[Tag 0H26](https://stacks.math.columbia.edu/tag/0H26) in the Stacks Project.

**`AlgebraicGeometry.Stack.factorsThroughSubstack_residualGerbe_of_isClosed_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeClosedPointFactorization.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeClosedPointFactorization.lean#L123). The attribute's comment: “the closed-point case the remark asserts: for X locally Noetherian and x a closed point, f : Y -> X with Y reduced and |f|(|Y|) in \{x} factors through the residual gerbe at x, which exists (via 0H27). The remark's open question, whether Lemma 0H25 holds for every point of a locally Noetherian X without the quasi-compact inertia hypothesis, is NOT asserted”.

> **Stacks 0H26, the closed-point case.** Let `𝒳` be a locally Noetherian algebraic stack over
> `S`, let `x ∈ |𝒳|` be a closed point, and let `f : 𝒴 ⟶ 𝒳` be a 1-morphism of algebraic stacks with
> `𝒴` reduced and `|f|(|𝒴|) ⊆ {x}`. Then the residual gerbe `𝒵_x` of `𝒳` at `x` exists and `f`
> factors through it: every object property of `𝒳` cutting out a residual gerbe at `x` is one `f`
> factors through.
>
> This is the conclusion of **Stacks 0H25** with its quasi-compact-inertia hypothesis dropped, which
> the remark says is true at a closed point because of **Stacks 0H27**. The remark's open question,
> whether the conclusion holds at every point of a locally Noetherian `𝒳`, is not asserted.
>
> The residual gerbe is the reduced closed substack on `{x}` (**Stacks 0509**), which is a residual
> gerbe at `x` as in the proof of Stacks 0H27; every residual gerbe at `x` has closed immersion
> inclusion by Stacks 0H27, so `f` factors through it by **Stacks 050B**.

```lean
theorem factorsThroughSubstack_residualGerbe_of_isClosed_singleton
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (h𝒳 : IsLocallyNoetherianStack B S hS 𝒳)
    (x : AlgebraicStacks.points B S hS 𝒳)
    (hx : @IsClosed _ (pointTopology B S hS 𝒳.val) {x})
    (f : 𝒴 ⟶ 𝒳) (hf : Set.range (AlgebraicStacks.pointsMap B S hS f) ⊆ {x})
    (hred : IsReducedStack B S hS 𝒴) :
    (∃ P : ObjectProperty 𝒳.val.val.obj, IsResidualGerbeAt B S hS 𝒳 x P) ∧
      ∀ P : ObjectProperty 𝒳.val.val.obj, IsResidualGerbeAt B S hS 𝒳 x P →
        FactorsThroughSubstack f P
```

## Tag 0H27, a lemma

[Tag 0H27](https://stacks.math.columbia.edu/tag/0H27) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isResidualGerbeAt_and_isClosed_singleton_iff_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeClosedPoint.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ResidualGerbeClosedPoint.lean#L127).

> **Stacks 0H27.** Let `𝒳` be a locally Noetherian algebraic stack over `S` and `x ∈ |𝒳|`.
> The residual gerbe `𝒵_x ⊂ 𝒳` of `𝒳` at `x` exists (**Stacks 0H22**), and for it, `x` is a closed
> point of `|𝒳|` if and only if the inclusion `𝒵_x ⟶ 𝒳` is a closed immersion.
>
> The residual gerbe is the strictly full subcategory cut out by an object property meeting the
> specification `AlgebraicGeometry.Stack.IsResidualGerbeAt` (**Stacks 06MU**), which is unique by
> `AlgebraicGeometry.Stack.eq_of_isResidualGerbeAt_of_bootstrap`; the equivalence is
> `AlgebraicGeometry.Stack.isClosed_singleton_iff_isClosedImmersion_residualGerbeInclusion`.

```lean
theorem exists_isResidualGerbeAt_and_isClosed_singleton_iff_isClosedImmersion
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (h𝒳 : IsLocallyNoetherianStack B S hS 𝒳)
    (x : AlgebraicStacks.points B S hS 𝒳) :
    ∃ (P : ObjectProperty 𝒳.val.val.obj) (hP : IsResidualGerbeAt B S hS 𝒳 x P),
      (@IsClosed _ (pointTopology B S hS 𝒳.val) {x} ↔
        AlgebraicStacks.IsClosedImmersion B S hS (residualGerbeInclusion B S hS 𝒳 x P hP))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.51, Tag 0H23](https://stacks.math.columbia.edu/tag/0H23)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

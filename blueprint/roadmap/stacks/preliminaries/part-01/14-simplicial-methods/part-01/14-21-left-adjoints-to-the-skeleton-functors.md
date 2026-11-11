---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.Truncated.hasPointwiseLeftKanExtension, CategoryTheory.SimplicialObject.Truncated.underCocone_isColimit, CategoryTheory.SimplicialObject.Truncated.isIso_lanAdjunction_unit_app, SSet.Truncated.mem_degenerate_sk_obj, SSet.exists_iso_skeleton_hom_ι_eq_skAdj_counit, SSet.Subcomplex.isPushout_boundary_ι, SSet.Subcomplex.exists_monotone_sup_ofSimplex_eq_top, AlgebraicTopology.NormalizedMooreComplex.objX_sk_obj_eq_bot
statement: formalized
proof: formalized
---

# 14.21 Left adjoints to the skeleton functors

Section 14.21 of the Stacks Project, [Tag 018K](https://stacks.math.columbia.edu/tag/018K). 10 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 018L, a lemma

[Tag 018L](https://stacks.math.columbia.edu/tag/018L) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.hasPointwiseLeftKanExtension`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L146). References: SGA 4 V (7.1.0), “existence of i\_\{n!}”.

> **Stacks 018L**.
> An `m`-truncated simplicial object `U` of a category `C` with finite colimits has a pointwise
> left Kan extension along `(SimplexCategory.Truncated.inclusion m).op`: for every `⦋n⦌`, the
> colimit of `U` over `(⦋n⦌/Δ)^{opp}_{≤ m}` exists. Hence the left adjoint `i_{m!}` of the
> skeleton functor `sk_m` exists (`CategoryTheory.SimplicialObject.Truncated.sk m`, with
> adjunction `CategoryTheory.SimplicialObject.skAdj m`) and `(i_{m!}U)_n` is that colimit.

```lean
public instance hasPointwiseLeftKanExtension (m : ℕ) (U : SimplicialObject.Truncated C m) :
    (SimplexCategory.Truncated.inclusion m).op.HasPointwiseLeftKanExtension U
```

## Tag 018M, a lemma

[Tag 018M](https://stacks.math.columbia.edu/tag/018M) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.underCocone_isColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 873](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L873).

> **Stacks 018M**.
> Let `C` be a category and let `U` be an `m`-truncated simplicial object of `C`. For an object
> `[n]` of `Δ_{≤ m}` the cocone `underCocone`, with apex `U_n` and leg `U(α) : U_k → U_n` at an
> object `α : [n] → [k]`, exhibits `U_n` as the colimit of the diagram `U(n)`.

```lean
theorem underCocone_isColimit : Nonempty (IsColimit (underCocone U n))
```

## Tag 018N, a lemma

[Tag 018N](https://stacks.math.columbia.edu/tag/018N) in the Stacks Project.

**`CategoryTheory.SimplicialObject.Truncated.isIso_lanAdjunction_unit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/SkeletonTruncationUnit.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/SkeletonTruncationUnit.lean#L40).

> Let `C` be a category with finite colimits and let `U` be an `m`-truncated simplicial object
> of `C`. The unit `U ⟶ sk_m i_{m!} U` of the adjunction `i_{m!} ⊣ sk_m`, where
> `i_{m!} = CategoryTheory.SimplicialObject.Truncated.sk m` is the left Kan extension along the
> inclusion `Δ_{≤ m} ⊆ Δ` and `sk_m = CategoryTheory.SimplicialObject.truncation m` is restriction
> along it, is an isomorphism.

```lean
theorem isIso_lanAdjunction_unit_app (m : ℕ) (U : SimplicialObject.Truncated C m) :
    IsIso (X := U) (Y := (truncation m).obj ((Truncated.sk m).obj U))
      (((SimplexCategory.Truncated.inclusion m).op.lanAdjunction C).unit.app U)
```

## Tag 018O, a lemma

[Tag 018O](https://stacks.math.columbia.edu/tag/018O) in the Stacks Project.

**`SSet.Truncated.mem_degenerate_sk_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 933](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L933).

> **Stacks 018O**.
> For an `m`-truncated simplicial set `U` and `n > m`, every `n`-simplex of
> `i_{m!} U = (SSet.Truncated.sk m).obj U` is degenerate.

```lean
theorem mem_degenerate_sk_obj (m : ℕ) (U : SSet.Truncated m) (n : ℕ) (hn : m < n)
    (x : ((Truncated.sk m).obj U).obj (op (SimplexCategory.mk n))) :
    x ∈ ((Truncated.sk m).obj U).degenerate n
```

## Tag 018P, a lemma

[Tag 018P](https://stacks.math.columbia.edu/tag/018P) in the Stacks Project.

**`SSet.exists_iso_skeleton_hom_ι_eq_skAdj_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L285).

> **Stacks 018P**.
> For a simplicial set `X` and `n : ℕ`, the canonical morphism `i_{n!} sk_n X ⟶ X`, i.e. the counit
> of the adjunction `SSet.skAdj n`, factors as an isomorphism from `(sk n).obj X` onto the
> subcomplex `X.skeleton (n + 1)` generated by the simplices of dimension `≤ n`, followed by the
> inclusion of that subcomplex.

```lean
public theorem exists_iso_skeleton_hom_ι_eq_skAdj_counit (X : SSet.{u}) (n : ℕ) :
    ∃ e : (sk n).obj X ≅ (X.skeleton (n + 1) : SSet),
      e.hom ≫ Subcomplex.ι _ = (skAdj n).counit.app X
```

## Tag 018R, a lemma

[Tag 018R](https://stacks.math.columbia.edu/tag/018R) in the Stacks Project.

**`SSet.Subcomplex.isPushout_boundary_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L416).

> **Stacks 018R**.
> Let `U` be a simplicial subset of a simplicial set
> `V` and let `x` be an `n`-simplex of `V` not in `U` such that `U` contains all simplices of `V`
> of dimension `< n` (`hlt`), `x` is the only `n`-simplex of `V` outside `U` (`hn`), and every
> simplex of `V` outside `U` in a degree `> n` is degenerate (`hgt`). Then the square formed by
> the boundary inclusion `∂Δ[n] ⟶ Δ[n]`, the inclusion `U ⟶ V`, and the morphism
> `Δ[n] ⟶ V` classifying `x` is a pushout square: `V = U ∐_{∂Δ[n]} Δ[n]`.

```lean
public theorem isPushout_boundary_ι {V : SSet.{u}} {U : V.Subcomplex} {n : ℕ} (x : V _⦋n⦌)
    (hx : x ∉ U.obj (op ⦋n⦌)) (hlt : V.skeleton n ≤ U)
    (hn : ∀ y : V _⦋n⦌, y ∈ U.obj (op ⦋n⦌) ∨ y = x)
    (hgt : ∀ j : ℕ, n < j → ∀ z : V _⦋j⦌, z ∉ U.obj (op ⦋j⦌) → z ∈ V.degenerate j)
    (hbd : range (∂Δ[n].ι ≫ yonedaEquiv.symm x) ≤ U) :
    IsPushout (lift (∂Δ[n].ι ≫ yonedaEquiv.symm x) hbd) ∂Δ[n].ι U.ι (yonedaEquiv.symm x)
```

## Tag 018S, a lemma

[Tag 018S](https://stacks.math.columbia.edu/tag/018S) in the Stacks Project.

**`SSet.Subcomplex.exists_monotone_sup_ofSimplex_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 536](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L536).

> **Stacks 018S**.
> Let `U` be a simplicial subset of a simplicial set `V` such that only finitely
> many nondegenerate simplices of `V` lie outside `U`. Then there are `r : ℕ` and an increasing
> sequence `W` of simplicial subsets of `V` with `W 0 = U` and `W r = V` such that, for each
> `i < r`, the subcomplex `W (i + 1)` is obtained from `W i` by adjoining a single simplex `x`
> of `V` which does not lie in `W i` and whose boundary does; equivalently, by
> `SSet.Subcomplex.isPushout_boundary_ι`, each `W i ⊆ W (i + 1)` is the attachment of a cell along
> `∂Δ[n] ⟶ Δ[n]`.

```lean
public theorem exists_monotone_sup_ofSimplex_eq_top {V : SSet.{u}} (U : V.Subcomplex)
    [Finite U.N] :
    ∃ (r : ℕ) (W : ℕ → V.Subcomplex), Monotone W ∧ W 0 = U ∧ W r = ⊤ ∧
      ∀ i < r, ∃ (n : ℕ) (x : V _⦋n⦌), x ∉ (W i).obj (op ⦋n⦌) ∧
        range (∂Δ[n].ι ≫ yonedaEquiv.symm x) ≤ W i ∧
        W (i + 1) = W i ⊔ ofSimplex x
```

## Tag 018T, a lemma

[Tag 018T](https://stacks.math.columbia.edu/tag/018T) in the Stacks Project.

**`AlgebraicTopology.NormalizedMooreComplex.objX_sk_obj_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L585).

> **Stacks 018T**.
> Let `A` be an abelian category and let `U` be an `m`-truncated simplicial object of `A`. For
> `n > m` the degree `n` normalized Moore subobject of the simplicial object `i_{m!}U` obtained
> from `U` by the left adjoint `CategoryTheory.SimplicialObject.Truncated.sk m` of truncation is
> the zero subobject: `N(i_{m!}U)ₙ = 0`.

```lean
public theorem objX_sk_obj_eq_bot {m : ℕ}
    [∀ F : (SimplexCategory.Truncated m)ᵒᵖ ⥤ A,
      (SimplexCategory.Truncated.inclusion m).op.HasPointwiseLeftKanExtension F]
    (U : SimplicialObject.Truncated A m) {n : ℕ} (hmn : m < n) :
    objX ((SimplicialObject.Truncated.sk m).obj U) n = ⊥
```

## Tag 018U, a lemma

[Tag 018U](https://stacks.math.columbia.edu/tag/018U) in the Stacks Project.

**`CategoryTheory.SimplicialObject.isLeast_subobject_mk_skAdj_counit_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 664](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L664).

> **Stacks 018U**.
> Let `U` be a simplicial object of an abelian category `A` and let `n : ℕ`.
> The canonical morphism `i_{n!} sk_n U ⟶ U` — the counit of `i_{n!} ⊣ sk_n` — is in each degree
> `m` a monomorphism, and the subobject of `U_m` it defines is the least subobject through which
> every operator `U(φ) : U_i ⟶ U_m` with `φ : ⦋m⦌ → ⦋i⦌` and `i ≤ n` factors, that is, the sum
> `U'_m = Σ_{φ : ⦋m⦌ → ⦋i⦌, i ≤ n} Im(U(φ))`.

```lean
public theorem isLeast_subobject_mk_skAdj_counit_app (U : SimplicialObject A) (n m : ℕ) :
    ∃ _ : Mono (((skAdj n).counit.app U).app (op ⦋m⦌)),
      IsLeast {P | ∀ i ≤ n, ∀ φ : (⦋m⦌ : SimplexCategory) ⟶ ⦋i⦌, P.Factors (U.map φ.op)}
        (Subobject.mk (((skAdj n).counit.app U).app (op ⦋m⦌)))
```

## Tag 018V, a lemma

[Tag 018V](https://stacks.math.columbia.edu/tag/018V) in the Stacks Project.

**`CategoryTheory.SimplicialObject.nonempty_representableBy_hom_sk_stdSimplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean, line 795](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Skeleton.lean#L795). The attribute's comment: “stated in an arbitrary degree `m`, the source's display being the case `m = n + 1`, and as representability of the presheaf that the source's `Hom(-, V)₀` represents, so that neither finite coproducts nor Tag 017L is needed”.

> **Stacks 018V**.
> Let `V` be a simplicial object of a category `C` and let `n m : ℕ`, and assume the `n`-th
> coskeleton of `C` exists pointwise, as it does when `C` has finite limits. Then the object of
> `m`-simplices of `cosk_n sk_n V` represents the presheaf
> `X ↦ Mor_{Simp(C)}(X × i_{n!} sk_n Δ[m], V)` on `C`, equally
> `X ↦ Mor_{SSet}(i_{n!} sk_n Δ[m], V ⋙ coyoneda.obj (op X))`; that is,
> `(cosk_n sk_n V)_m = Hom(i_{n!} sk_n Δ[m], V)₀`. For `m = n + 1` the simplicial
> set `i_{n!} sk_n Δ[n + 1]` is the boundary `∂Δ[n + 1]`, and a morphism
> `X ⟶ (cosk_n sk_n V)_{n + 1}` is a matching family of `(n + 1)`-simplices of `V` with values in
> `X`.

```lean
public theorem nonempty_representableBy_hom_sk_stdSimplex {C : Type u} [Category.{v} C] (n : ℕ)
    [∀ F : (SimplexCategory.Truncated n)ᵒᵖ ⥤ C,
      (SimplexCategory.Truncated.inclusion n).op.HasPointwiseRightKanExtension F]
    (V : SimplicialObject C) (m : ℕ) :
    Nonempty ((coyoneda ⋙ (Functor.whiskeringLeft SimplexCategoryᵒᵖ C (Type v)).obj V ⋙
      coyoneda.obj (op ((sk n).obj Δ[m]))).RepresentableBy (((cosk n).obj V) _⦋m⦌))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.21, Tag 018K](https://stacks.math.columbia.edu/tag/018K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

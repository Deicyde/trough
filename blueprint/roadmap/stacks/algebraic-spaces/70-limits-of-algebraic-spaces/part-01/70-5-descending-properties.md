---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.existsUnique_point_limit, AlgebraicGeometry.Space.isHomeomorph_pointsLimitComparison, AlgebraicGeometry.Space.pointTopology_limit, AlgebraicGeometry.Space.pointTopology_limit_of_isSiteSmall, AlgebraicGeometry.Space.nonempty_points_limit, AlgebraicGeometry.Space.closure_singleton_limit, AlgebraicGeometry.Space.existsUnique_point_closure_limit, AlgebraicGeometry.Space.exists_iso_limit_reducedClosure
statement: formalized
proof: formalized
---

# 70.5 Descending properties

Section 70.5 of the Stacks Project, [Tag 0826](https://stacks.math.columbia.edu/tag/0826). 17 tags here are carried by 30 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CUJ, a lemma

[Tag 0CUJ](https://stacks.math.columbia.edu/tag/0CUJ) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_point_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/Points.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/Points.lean#L292).

> **Stacks 0CUJ.** Let `D` be a directed inverse system of decent algebraic spaces over `S`
> with affine transition morphisms, indexed by a category whose object type and whose morphism
> types are smaller than the cofinality of the site's size cutoff. Then a family of points of
> the stages which is compatible with the transition morphisms is induced by exactly one point
> of `limit D`; that is, `|lim D| = lim |D|` as sets.

```lean
theorem existsUnique_point_limit (D : I ⥤ (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hSize : #I < B.cutoff.ord.cof)
    (_hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (_hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (hDecent : ∀ i, IsDecentSpace B S hS (D.obj i))
    (x : ∀ i, points B S hS (D.obj i))
    (hx : ∀ {i j : I} (f : i ⟶ j), pointsMap B S hS (D.obj i) (D.map f) (x i) = x j) :
    ∃! y : points B S hS (limit D),
      ∀ i, pointsMap B S hS (limit D) (limit.π D i) y = x i
```

## Tag 086V, a lemma

[Tag 086V](https://stacks.math.columbia.edu/tag/086V) in the Stacks Project.

**`AlgebraicGeometry.Space.isHomeomorph_pointsLimitComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/PointsLimitHomeomorph.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/PointsLimitHomeomorph.lean#L78).

> **Stacks 086V.** Let `D` be a directed inverse system of decent algebraic spaces over `S`
> with affine transition morphisms, indexed by a category small enough for the site, so that
> `limit D` is an algebraic space by Stacks 07SF. Then `|limit D| = lim |D i|` as topological
> spaces: the canonical map `AlgebraicGeometry.Space.pointsLimitComparison` from the points of
> the limit to the inverse limit of the point spaces of the stages is a homeomorphism.
>
> It is bijective by Stacks 0CUJ, `AlgebraicGeometry.Space.existsUnique_point_limit`, which is
> where decency is used, and it is inducing because the point topology of the limit is the
> inverse-limit topology, `AlgebraicGeometry.Space.pointTopology_limit`.

```lean
theorem isHomeomorph_pointsLimitComparison (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (hDecent : ∀ i, IsDecentSpace B S hS (D.obj i)) :
    IsHomeomorph (pointsLimitComparison B S hS D)
```

**`AlgebraicGeometry.Space.pointTopology_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/PointTopology.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/PointTopology.lean#L223).

> The point topology of the limit of a cofiltered inverse system of algebraic spaces over `S`
> with affine transition morphisms, indexed by a small enough category, is the infimum of the
> topologies induced by the limit projections on points.

```lean
theorem pointTopology_limit (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f)) :
    pointTopology B S hS (limit D) =
      ⨅ i : I, TopologicalSpace.induced (pointsMap B S hS (limit D) (limit.π D i))
        (pointTopology B S hS (D.obj i))
```

**`AlgebraicGeometry.Space.pointTopology_limit_of_isSiteSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/PointTopology.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/PointTopology.lean#L375).

> The point topology of the limit of a cofiltered inverse system of algebraic spaces over `S`
> with affine transition morphisms, indexed by a site-small category, is the infimum of the
> topologies induced by the limit projections on points.

```lean
theorem pointTopology_limit_of_isSiteSmall (hb : IsSiteSmall B S hS D)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f)) :
    pointTopology B S hS (limit D) =
      ⨅ i : I, TopologicalSpace.induced (pointsMap B S hS (limit D) (limit.π D i))
        (pointTopology B S hS (D.obj i))
```

## Tag 086W, a lemma

[Tag 086W](https://stacks.math.columbia.edu/tag/086W) in the Stacks Project.

**`AlgebraicGeometry.Space.nonempty_points_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/NonemptyLimit.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/NonemptyLimit.lean#L117).

> **Stacks 086W.** The inverse limit of a cofiltered inverse system of nonempty
> quasi-compact algebraic spaces over `S` with affine transition morphisms has a point, provided
> the index category is small enough for the site: its object type and all of its morphism types
> have cardinality below the cofinality of the site's size cutoff.

```lean
theorem nonempty_points_limit (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (hCompact : ∀ i, IsQuasiCompactSpace B S hS (D.obj i))
    (hNonempty : ∀ i, Nonempty (points B S hS (D.obj i))) :
    Nonempty (points B S hS (limit D))
```

## Tag 0CUK, a lemma

[Tag 0CUK](https://stacks.math.columbia.edu/tag/0CUK) in the Stacks Project.

**`AlgebraicGeometry.Space.closure_singleton_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosureOfPoint.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosureOfPoint.lean#L150). The attribute's comment: “as sets”.

> **Stacks 0CUK, as sets.** Let `x` be a point of the limit `X` of a cofiltered inverse
> system of algebraic spaces over `S` with affine transition morphisms, with images `x i` in the
> stages. The closure of `x` in `|X|` is the intersection of the preimages of the closures of
> the `x i`, that is, the inverse limit of those closures.

```lean
theorem closure_singleton_limit (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (x : points B S hS (limit D)) :
    closure {x} = ⋂ i : I, pointsMap B S hS (limit D) (limit.π D i) ⁻¹'
      closure {pointsMap B S hS (limit D) (limit.π D i) x}
```

**`AlgebraicGeometry.Space.existsUnique_point_closure_limit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosureOfPoint.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosureOfPoint.lean#L215). The attribute's comment: “as sets, for a compatible family of points”.

> **Stacks 0CUK, as sets.** The set-level assertion read through the identification
> `|X| = lim |D i|` of Stacks 0CUJ, for a compatible family of points.

```lean
theorem existsUnique_point_closure_limit (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (hDecent : ∀ i, IsDecentSpace B S hS (D.obj i))
    (x : points B S hS (limit D)) (z : ∀ i, points B S hS (D.obj i))
    (hz : ∀ {i j : I} (f : i ⟶ j), pointsMap B S hS (D.obj i) (D.map f) (z i) = z j)
    (hzmem : ∀ i, z i ∈ closure {pointsMap B S hS (limit D) (limit.π D i) x}) :
    ∃! y : points B S hS (limit D), y ∈ closure {x} ∧
      ∀ i, pointsMap B S hS (limit D) (limit.π D i) y = z i
```

**`AlgebraicGeometry.Space.exists_iso_limit_reducedClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosureOfPoint.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosureOfPoint.lean#L429). The attribute's comment: “as algebraic spaces with the reduced induced structure”.

> **Stacks 0CUK, as algebraic spaces.** Let `x` be a point of the limit `X` of a cofiltered
> inverse system of algebraic spaces over `S` with affine transition morphisms. The closure of
> `x`, with its reduced induced structure, is the limit of the closures of the images `x i` with
> theirs: those closures form an inverse system of algebraic spaces with affine transition
> morphisms, its limit is reduced, and the inclusion of the closure of `x` into `X` factors
> through an isomorphism onto that limit.

```lean
theorem exists_iso_limit_reducedClosure (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (x : points B S hS (limit D)) :
    ∃ (E : I ⥤ (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (η : E ⟶ D)
      (e : (reducedClosedSubspace B S hS (limit D)
          (isAlgebraicSpace_limit B S hS D hSize hHomSize hD hAffine)
          (closure {x}) isClosed_closure).toFunctor ≅ limit E),
      (∀ i : I, ∃ eᵢ : E.obj i ≅ (reducedClosedSubspace B S hS (D.obj i) (hD i)
            (closure {pointsMap B S hS (limit D) (limit.π D i) x}) isClosed_closure).toFunctor,
          eᵢ.hom ≫ (reducedClosedSubspace B S hS (D.obj i) (hD i)
            (closure {pointsMap B S hS (limit D) (limit.π D i) x}) isClosed_closure).ι
            = η.app i) ∧
        (∀ i, IsAlgebraicSpace B S hS (E.obj i)) ∧
        (∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (E.map f)) ∧
        HasEtaleLocalProperty B S hS (limit E) (fun Y : Scheme.{u} ↦ IsReduced Y) ∧
        e.hom ≫ limMap η = (reducedClosedSubspace B S hS (limit D)
          (isAlgebraicSpace_limit B S hS D hSize hHomSize hD hAffine)
          (closure {x}) isClosed_closure).ι
```

## Tag 084R, a situation

[Tag 084R](https://stacks.math.columbia.edu/tag/084R) in the Stacks Project.

**`AlgebraicGeometry.Space.LimitSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LimitSituation.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LimitSituation.lean#L203).

> **Situation 084R.** A *limit situation* for a presheaf `X` on the big fppf site of `S`:
> a directed index set with a chosen element, an inverse system of algebraic spaces over `S`
> indexed by it whose transition morphisms are affine and whose stages are quasi-compact and
> quasi-separated, and an identification of `X` with the limit of that system.
>
> This is the algebraic-space analogue of `AlgebraicGeometry.DescentSituation`, which is
> Situation 086P for schemes, and the two have the same fields. By Stacks 07SF the limit of
> such a system *is* an algebraic space over `S`, so the situation is not vacuous for a
> reason it should not be: `AlgebraicGeometry.Space.LimitSituation.const` builds one for every
> quasi-compact quasi-separated algebraic space.

```lean
structure LimitSituation (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u})) (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.DescentSituation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/Limits.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties.lean#L31) (StacksFrontier).

## Tag 07SI, a lemma

[Tag 07SI](https://stacks.math.columbia.edu/tag/07SI) in the Stacks Project.

**`AlgebraicGeometry.Space.LimitSituation.isSectionsColimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasicoherentSectionsColimit.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasicoherentSectionsColimit.lean#L65).

> Let `ℱ₀` be a quasi-coherent module on `X₀`, and set `ℱᵢ = f_{0i}^*ℱ₀` and `ℱ = f_0^*ℱ₀`.
> Then `Γ(X, ℱ) = colim_{i ≥ 0} Γ(Xᵢ, ℱᵢ)`, in the elementwise form
> `AlgebraicGeometry.Space.LimitSituation.IsSectionsColimit`, for an index set below the
> cofinality of the site's size cutoff.

```lean
theorem isSectionsColimit (hI : #A.I < B.cutoff.ord.cof)
    (F₀ : Modules.{u, u} B S hS (A.stage A.base).obj (A.stage A.base).property)
    (hF₀ : F₀.IsQuasicoherentOnSite) :
    A.IsSectionsColimit F₀ (A.isAlgebraicSpace_of_mk_lt hI)
```

**`AlgebraicGeometry.Space.LimitSituation.isSectionsColimit_of_baseChangeSizeBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasicoherentSectionsColimitSizeBounded.lean, line 350](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/QuasicoherentSectionsColimitSizeBounded.lean#L350). The attribute's comment: “Situation 084R on the bounded site, with the size conventions of Tag 07SD read as an index set below the cutoff with uniformly bounded base changes of the stages; with no size condition the statement is false, Refute07SI.not\_forall\_isSectionsColimit”.

> **Stacks 07SI.**  In Situation 084R, let `ℱ₀` be a quasi-coherent module on `X₀`, and set
> `ℱᵢ = f_{0i}^*ℱ₀` and `ℱ = f_0^*ℱ₀`.  Then `Γ(X, ℱ) = colim_{i ≥ 0} Γ(Xᵢ, ℱᵢ)`, in the
> elementwise form `AlgebraicGeometry.Space.LimitSituation.IsSectionsColimit`.
>
> The size condition, an index set below the cutoff with uniformly bounded base changes, is how the
> bounded site reads the size conventions of the source (Tag 07SD); with no size condition the
> statement is false, by `AlgebraicGeometry.Space.Refute07SI.not_forall_isSectionsColimit`.

```lean
theorem isSectionsColimit_of_baseChangeSizeBounded (hI : #A.I < B.cutoff)
    (hB : BaseChangeSizeBounded B S hS A.system) (hF₀ : F₀.IsQuasicoherentOnSite) :
    A.IsSectionsColimit F₀ (A.isAlgebraicSpace_of_baseChangeSizeBounded hI hB)
```

## Tag 0827, a lemma

[Tag 0827](https://stacks.math.columbia.edu/tag/0827) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isQuasiCompactSpace_preimage_eq_of_isSiteSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendOpens.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendOpens.lean#L327). References: EGA IV (8.2.11).

> **Stacks 0827.** Notation and assumptions as in Situation 084R: let `X = limit D` be the
> limit of a cofiltered inverse system `D` of algebraic spaces over `S` with affine transition
> morphisms, the index category being small enough for the site so that `X` is an algebraic space
> by Stacks 07SF. Then for every quasi-compact open subspace `U ⊆ X` there is a stage `i` and a
> quasi-compact open subspace of `D i` whose inverse image in `X` is `U`.
>
> Neither quasi-separatedness nor quasi-compactness of the stages, which Situation 084R also
> assumes, is needed.

```lean
theorem exists_isOpenSubspace_isQuasiCompactSpace_preimage_eq_of_isSiteSmall (hb : IsSiteSmall B S
    hS D)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (U : Subfunctor (limit D)) (hU : IsOpenSubspace B S hS U)
    (hUqc : IsQuasiCompactSpace B S hS U.toFunctor) :
    ∃ (i : I) (V : Subfunctor (D.obj i)), IsOpenSubspace B S hS V ∧
      IsQuasiCompactSpace B S hS V.toFunctor ∧ V.preimage (limit.π D i) = U
```

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isQuasiCompactSpace_preimage_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendOpens.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/DescendOpens.lean#L348). References: EGA IV (8.2.11).

> **Stacks 0827.** Notation and assumptions as in Situation 084R: let `X = limit D` be the
> limit of a cofiltered inverse system `D` of algebraic spaces over `S` with affine transition
> morphisms, the index category being small enough for the site so that `X` is an algebraic space
> by Stacks 07SF. Then for every quasi-compact open subspace `U ⊆ X` there is a stage `i` and a
> quasi-compact open subspace of `D i` whose inverse image in `X` is `U`.
>
> Neither quasi-separatedness nor quasi-compactness of the stages, which Situation 084R also
> assumes, is needed.

```lean
theorem exists_isOpenSubspace_isQuasiCompactSpace_preimage_eq (hSize : #I < B.cutoff.ord.cof)
    (hHomSize : ∀ i j : I, #(i ⟶ j) < B.cutoff.ord.cof)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj i))
    (hAffine : ∀ {i j : I} (f : i ⟶ j), IsAffineHom B S hS (D.map f))
    (U : Subfunctor (limit D)) (hU : IsOpenSubspace B S hS U)
    (hUqc : IsQuasiCompactSpace B S hS U.toFunctor) :
    ∃ (i : I) (V : Subfunctor (D.obj i)), IsOpenSubspace B S hS V ∧
      IsQuasiCompactSpace B S hS V.toFunctor ∧ V.preimage (limit.π D i) = U
```

## Tag 084S, a lemma

[Tag 084S](https://stacks.math.columbia.edu/tag/084S) in the Stacks Project.

**`AlgebraicGeometry.Space.MorphismDescentSystem.exists_isIso_mapAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/Isomorphism.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/Isomorphism.lean#L363). References: EGA IV (8.8.2.5), “f iso ⇒ f\_i iso”.

> **Stacks 0852**, and **Stacks 084S**. In the situation of Stacks 084W, if the base change
> `f` of `f₀` to the limit `B` is an isomorphism and `f₀` is locally of finite presentation, then
> the base change `f_i` of `f₀` to some stage `B_i` is an isomorphism.
>
> This is Stacks 0852. Stacks 084S draws the same conclusion in the limit situation of Stacks
> 084R, with the source and the target in addition assumed representable over the stage;
> hypothesis (a) of that tag is not needed here, since the three properties into which being an
> isomorphism is decomposed all descend without it.

```lean
theorem exists_isIso_mapAt (hf : IsIso D.mapLimit)
    (hfp : IsLocallyOfFinitePresentation B S hS D.map₀) :
    ∃ (i : I) (hi : D.initial ≤ i), IsIso (D.mapAt i hi)
```

## Tag 084T, a lemma

[Tag 084T](https://stacks.math.columbia.edu/tag/084T) in the Stacks Project.

**`AlgebraicGeometry.Space.DescentSituation.exists_isAbsolutelySeparated_system_obj_of_isSiteSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedDescent.lean, line 818](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedDescent.lean#L818).

> **Stacks 084T.** In the situation of Stacks 084R, over an arbitrary base scheme, if the
> limit `X` of the inverse system is separated then some stage `X_i` is separated.
>
> Separatedness is the absolute notion, taken over the terminal scheme, so the whole descent may
> be read there: the relocalization along `S ⟶ Spec ℤ` carries the descent situation over `S` to
> one over the terminal scheme, which is affine, and the absolute separatedness of a presheaf and
> of its view over the terminal scheme are the same condition.

```lean
theorem exists_isAbsolutelySeparated_system_obj_of_isSiteSmall {I : Type u} [Preorder I]
    [IsDirected I (· ≤ ·)] (D : DescentSituation B S hS hZ I)
    (hb : Space.IsSiteSmall B S hS D.system)
    (hX : IsAbsolutelySeparated B S hS hZ D.limitCone.pt) :
    ∃ i, D.base ≤ i ∧ IsAbsolutelySeparated B S hS hZ (D.system.obj (op i))
```

**`AlgebraicGeometry.Space.DescentSituation.exists_isAbsolutelySeparated_system_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedDescent.lean, line 838](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedDescent.lean#L838).

> **Stacks 084T.** In the situation of Stacks 084R, over an arbitrary base scheme, if the
> limit `X` of the inverse system is separated then some stage `X_i` is separated.
>
> Separatedness is the absolute notion, taken over the terminal scheme, so the whole descent may
> be read there: the relocalization along `S ⟶ Spec ℤ` carries the descent situation over `S` to
> one over the terminal scheme, which is affine, and the absolute separatedness of a presheaf and
> of its view over the terminal scheme are the same condition.

```lean
theorem exists_isAbsolutelySeparated_system_obj {I : Type u} [Preorder I]
    [IsDirected I (· ≤ ·)] (D : DescentSituation B S hS hZ I) (hI : #I < B.cutoff.ord.cof)
    (hX : IsAbsolutelySeparated B S hS hZ D.limitCone.pt) :
    ∃ i, D.base ≤ i ∧ IsAbsolutelySeparated B S hS hZ (D.system.obj (op i))
```

## Tag 07SQ, a lemma

[Tag 07SQ](https://stacks.math.columbia.edu/tag/07SQ) in the Stacks Project.

**`AlgebraicGeometry.Space.DescentSituation.exists_isAffineSpace_system_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineStage/ExistsAffineStage.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineStage/ExistsAffineStage.lean#L174). The attribute's comment: “Correction: the index set is taken smaller than the cofinality of the site's size cutoff, the form the convention of Section 70.2 takes in this size model; without it the statement is false here (a system of projective lines over fields of sizes cofinal in the cutoff has empty, hence affine, limit)”.

> **Stacks 07SQ.** In the situation of Stacks 084R over a scheme `S` — a directed inverse
> system of quasi-compact and quasi-separated algebraic spaces over `S` with affine transition
> morphisms, with a chosen limit `X` and a chosen index `0` — if `X` is affine then so is some stage
> `X_i` with `0 ≤ i`.
>
> The index set may live in any universe; its cardinality is asked to be below the cofinality of
> the size cutoff of the site, which is how the standing convention of Section 70.2 of the source
> (every ring considered has its spectrum in the site) reads in this size model. Without it the
> statement fails here: for fields `F_a` (`a` below the cofinality) of sizes cofinal in the
> cutoff, the system `P¹_{F_a}` has no point over any object of the site, so its limit is the
> empty, affine, scheme while no stage is affine.
>
> The index set is replaced by an order-isomorphic one in the universe of the site,
> `AlgebraicGeometry.Space.DescentSituation.exists_orderIso_of_lift_mk_lt`, along which the
> situation is reindexed, and the case of an index set in that universe is
> `AlgebraicGeometry.Space.DescentSituation.exists_isAffineSpace_system_obj_of_mk_lt`.

```lean
theorem DescentSituation.exists_isAffineSpace_system_obj {B : BigFppfSite.{u}} {S : Scheme.{u}}
    {hS : B.Contains S} {hZ : B.Contains (⊤_ Scheme.{u})} {I : Type v} [Preorder I]
    [IsDirected I (· ≤ ·)] (D : DescentSituation B S hS hZ I)
    (hI : Cardinal.lift.{u} #I < Cardinal.lift.{v} B.cutoff.ord.cof)
    (hX : IsAffineSpace B S hS D.limitCone.pt) :
    ∃ i, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (op i))
```

**`AlgebraicGeometry.Space.hasAffineStageDescent_of_chartsBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineStageDescentChartsBounded.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineStageDescentChartsBounded.lean#L161).

> In the situation of Stacks 084R, if the limit `X` of the inverse system is an affine algebraic
> space then `X_i` is an affine algebraic space for some `i` beyond the distinguished index, the
> charts of the system being bounded in the sense of `AlgebraicGeometry.Space.ChartsBounded`.
>
> The size restriction cannot be dropped: `Stacks.Refute07SQ.not_statement07SQ` exhibits a descent
> situation over an index as large as the cutoff whose limit is the empty algebraic space, which is
> affine, and none of whose stages is affine.

```lean
theorem hasAffineStageDescent_of_chartsBounded : HasAffineStageDescent B S hS hZ
```

**`AlgebraicGeometry.Space.DescentSituation.exists_isAffineSpace_system_obj_of_siteContainsBaseChangeLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineStageSiteSmall.lean, line 716](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineStageSiteSmall.lean#L716).

> **Stacks 07SQ.** In the situation of Stacks 084R, over an arbitrary base scheme, if the limit
> `X` of the inverse system is an affine algebraic space then so is some stage `X_i` with `i` at or
> beyond the distinguished index.
>
> The only hypothesis beyond Situation 084R is the chapter's standing convention of Section 70.2
> (tag 07SD), that every ring considered has its spectrum in the big fppf site; for this system it
> is `AlgebraicGeometry.Space.SiteContainsBaseChangeLimits`: for every stage, every affine
> scheme-valued point of it and the base changes to that point of the later stages, the limit of
> those affine schemes — the spectrum of the colimit of their rings — lies in the site. Nothing is
> asked of the index. The convention is used three times: to make the limit of the affine charts
> of the system an object of the site (Stacks 07SF), to make the ring of global functions of the
> limit the filtered colimit of those of the stages (Stacks 07SI for the structure sheaf), and in
> Stacks 084S.
>
> It cannot be dropped. Index the stages by the finite subsets of a field `F` of cardinality at
> least the cutoff of the site, the stage at a subset being the punctured affine plane over the
> subring of `F` it generates: a directed system of quasi-compact separated schemes with affine
> transition morphisms, none of them affine. A nonempty object of the site has too small a ring of
> functions to receive `F`, so the limit of the system in the site is empty, hence affine. See
> `AlgebraicGeometry.Space.DescentSituation.not_forall_exists_isAffineSpace_system_obj`; that the
> system violates the convention is
> `AlgebraicGeometry.Space.SiteConventionCounterexample.not_siteContainsBaseChangeLimits`.
>
> Affineness of an algebraic space is the absolute notion, taken over the terminal scheme, so the
> whole descent is read there: the relocalization along `S ⟶ Spec ℤ` carries the descent situation
> over `S` to one over the terminal scheme, which is where the identification of an affine
> algebraic space with the spectrum of its global functions is available, and the convention
> survives that passage,
> `AlgebraicGeometry.Space.DescentSituation.siteContainsBaseChangeLimits_viewOverIntegers`.

```lean
theorem exists_isAffineSpace_system_obj_of_siteContainsBaseChangeLimits
    (hconv : SiteContainsBaseChangeLimits B S hS D.system)
    (hX : IsAffineSpace B S hS D.limitCone.pt) :
    ∃ i, D.base ≤ i ∧ IsAffineSpace B S hS (D.system.obj (op i))
```

## Tag 084U, an equation

[Tag 084U](https://stacks.math.columbia.edu/tag/084U) in the Stacks Project.

**`AlgebraicGeometry.Space.commSq_chart_specOfGlobalFunctions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpecGlobalFunctionsChartSquare.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpecGlobalFunctionsChartSquare.lean#L274).

> Let `A` be a `u`-model of the ring of global functions of an algebraic space `X` over `S`,
> let `V` be an étale scheme chart of `X`, let `g₁, …, gₙ` be polynomials in `n` variables over `A`
> and let `h₁, …, hₙ` be global functions on `V` with `g_λ(h) = 0`. Write
> `C = A[x₁, …, xₙ]/(g₁, …, gₙ)`. Then the square whose top is the chart, whose left vertical is a
> canonical morphism `p : X ⟶ Spec A`, whose right vertical is the morphism `V ⟶ Spec C` attached
> to `AlgebraicGeometry.Space.coordinateHom` and whose bottom is the spectrum of `A → C` commutes.
>
> The hypothesis `hp` is the chart formula of `AlgebraicGeometry.Space.exists_specMap_of_globalHom`,
> which determines `p`.

```lean
theorem commSq_chart_specOfGlobalFunctions (X : AlgebraicSpaces B S hS)
    (V : SmallEtale B S hS X.1) (A : Type u) [CommRing A]
    (e : A ≃+* globalFunctions B S hS X.1) {n : ℕ} (g : Fin n → MvPolynomial (Fin n) A)
    (h : Fin n → Γ((BigFppfOver.toScheme B S hS).obj V.1.left, ⊤))
    (hrel : ∀ l, MvPolynomial.eval₂
      ((globalFunctionsChartRestriction B S hS X V).comp e.toRingHom) h (g l) = 0)
    (p : X.1 ⟶ schemePoints B S hS (Spec (CommRingCat.of A)))
    (hp : yonedaEquiv (V.1.hom ≫ p) =
      specMapOfGlobalHom A ((globalFunctionsChartRestriction B S hS X V).comp e.toRingHom)) :
    V.1.hom ≫ p =
      yonedaEquiv.symm (specMapOfGlobalHom (presentationAlgebra g)
          (coordinateHom g ((globalFunctionsChartRestriction B S hS X V).comp e.toRingHom)
            h hrel)) ≫
        schemePointsMap B S hS
          (Spec.map (CommRingCat.ofHom (presentationStructureHom g)))
```

## Tag 07SR, a lemma

[Tag 07SR](https://stacks.math.columbia.edu/tag/07SR) in the Stacks Project.

**`AlgebraicGeometry.Space.DescentSituation.exists_isRepresentable_system_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SchemeStage.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SchemeStage.lean#L207). The attribute's comment: “Correction: the index set is taken smaller than the cofinality of the site's size cutoff, the form the convention of Section 70.2 takes in this size model; without it the statement is false here (base changes of a non locally separated space to fields of sizes cofinal in the cutoff have empty limit, a scheme, and no stage a scheme)”.

> In the situation of Stacks 084R over a scheme `S` — a directed inverse system of quasi-compact
> and quasi-separated algebraic spaces over `S` with affine transition morphisms, together with a
> chosen limit `X` — if `X` is a scheme then some stage `X_i` is a scheme. The index set may live in
> any universe; its cardinality is asked to be below the cofinality of the site's size cutoff.

```lean
theorem exists_isRepresentable_system_obj {I : Type v} [Preorder I] [IsDirected I (· ≤ ·)]
    (D : DescentSituation B S hS hZ I)
    (hI : Cardinal.lift.{u} #I < Cardinal.lift.{v} B.cutoff.ord.cof)
    (hX : D.limitCone.pt.IsRepresentable) :
    ∃ i, (D.system.obj (op i)).IsRepresentable
```

**`AlgebraicGeometry.Space.DescentSituation.exists_isRepresentable_system_obj_of_siteContainsBaseChangeLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SchemeStageSiteSmall.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SchemeStageSiteSmall.lean#L283).

> In the situation of Stacks 084R — a directed inverse system of quasi-compact and
> quasi-separated algebraic spaces over `S` with affine transition morphisms, together with a chosen
> limit `X`, under the convention of Section 70.2 (tag 07SD) that the rings the chapter forms have
> their spectra in the big fppf site — if `X` is a scheme then there is a stage `X_i` which is a
> scheme. Nothing is asked of the index set beyond directedness.

```lean
theorem exists_isRepresentable_system_obj_of_siteContainsBaseChangeLimits {I : Type u}
    [Preorder I] [IsDirected I (· ≤ ·)]
    (D : DescentSituation B S hS hZ I) (hconv : SiteContainsBaseChangeLimits B S hS D.system)
    (hX : D.limitCone.pt.IsRepresentable) :
    ∃ i, (D.system.obj (op i)).IsRepresentable
```

## Tag 0828, a lemma

[Tag 0828](https://stacks.math.columbia.edu/tag/0828) in the Stacks Project.

**`AlgebraicGeometry.Space.eventually_isClosedImmersion_comp_limitπ'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosedImmersionDescent/EventualImmersion.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosedImmersionDescent/EventualImmersion.lean#L502). The attribute's comment: “part (1): closed immersions”.

> **Stacks 0828, part (1).** Let `X = lim Xᵢ` be a directed limit of algebraic spaces over an
> algebraic space `Bspace`, with affine transition morphisms and quasi-compact stages, and let
> `f : Y ⟶ X` be a closed immersion with `Y` locally of finite type over `Bspace`.  Then `Y ⟶ Xᵢ`
> is a closed immersion for all sufficiently large `i`.

```lean
theorem eventually_isClosedImmersion_comp_limitπ'
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (contains : B.Contains S)
    {I : Type u} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (Bspace : (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraicBase : IsAlgebraicSpace B S contains Bspace)
    (D : Iᵒᵖ ⥤ (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraicStage : ∀ i, IsAlgebraicSpace B S contains (D.obj (op i)))
    (t : D ⟶ (Functor.const Iᵒᵖ).obj Bspace)
    (c : Cone D) (isLimit : IsLimit c) (s : c.pt ⟶ Bspace)
    (commutes : c.π ≫ t = (Functor.const Iᵒᵖ).map s)
    (Y : (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraic : IsAlgebraicSpace B S contains Y)
    (f : Y ⟶ c.pt)
    (quasiCompactStage : ∀ i, IsQuasiCompactSpace B S contains (D.obj (op i)))
    (affine : ∀ ⦃i j : I⦄ (h : i ≤ j), Space.IsAffineHom B S contains (D.map (homOfLE h).op))
    (finiteType : Space.IsLocallyOfFiniteType B S contains (f ≫ s))
    (closed : Space.IsClosedImmersion B S contains f) :
    ∀ᶠ i in atTop, Space.IsClosedImmersion B S contains (f ≫ c.π.app (op i))
```

**`AlgebraicGeometry.Space.eventually_isImmersion_comp_limitπ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosedImmersionDescent/EventualImmersion.lean, line 727](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/ClosedImmersionDescent/EventualImmersion.lean#L727). The attribute's comment: “part (2): immersions”.

> **Stacks 0828, part (2).** Let `X = lim Xᵢ` be a directed limit of algebraic spaces over an
> algebraic space `Bspace`, with affine transition morphisms and quasi-separated stages, and let
> `f : Y ⟶ X` be an immersion whose source is quasi-compact and locally of finite type over
> `Bspace`.  Then `Y ⟶ Xᵢ` is an immersion for all sufficiently large `i`.
>
> The image of `Y` in one stage `Xᵢ₀` lies in a quasi-compact open subspace `V`, and the system of
> preimages of `V` in the stages above `i₀` has quasi-compact stages and limit the preimage of `V`
> in `X`, through which `f` factors by an immersion.  An affine étale atlas of `V` reduces the
> statement to schemes, where it is Stacks 081B, part (2)
> (`AlgebraicGeometry.EventualLimit.eventually_isImmersion_comp_π_app`), and the immersion is
> carried back to the stages by effective descent of immersions along surjective étale
> morphisms; quasi-separatedness of `Xᵢ₀` makes the base change of `Y` to the atlas quasi-compact.

```lean
theorem eventually_isImmersion_comp_limitπ
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (contains : B.Contains S)
    {I : Type u} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (Bspace : (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraicBase : IsAlgebraicSpace B S contains Bspace)
    (D : Iᵒᵖ ⥤ (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraicStage : ∀ i, IsAlgebraicSpace B S contains (D.obj (op i)))
    (t : D ⟶ (Functor.const Iᵒᵖ).obj Bspace)
    (c : Cone D) (isLimit : IsLimit c) (s : c.pt ⟶ Bspace)
    (commutes : c.π ≫ t = (Functor.const Iᵒᵖ).map s)
    (Y : (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraic : IsAlgebraicSpace B S contains Y)
    (quasiCompact : IsQuasiCompactSpace B S contains Y)
    (f : Y ⟶ c.pt)
    (affine : ∀ ⦃i j : I⦄ (h : i ≤ j), IsAffineHom B S contains (D.map (homOfLE h).op))
    (quasiSeparated : ∀ i,
      IsAbsolutelyQuasiSeparated B S contains B.contains_terminal (D.obj (op i)))
    (finiteType : IsLocallyOfFiniteType B S contains (f ≫ s))
    (immersion : IsImmersion B S contains f) :
    ∀ᶠ i in atTop, IsImmersion B S contains (f ≫ c.π.app (op i))
```

**`AlgebraicGeometry.Space.eventually_isIso_comp_limitπ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/EventualIsomorphism.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/EventualIsomorphism.lean#L420). The attribute's comment: “part (3): isomorphism”. References: SGA 3 XI (3.11), “more general”.

> **An isomorphism onto a directed limit is eventually an isomorphism onto the stages.**  Let
> `X = lim Xᵢ` be a directed limit of algebraic spaces over an algebraic space `Bspace` and let
> `f : Y ⟶ X` be an isomorphism.  If the stages `Xᵢ` are quasi-compact and locally of finite type
> over `Bspace`, the transition morphisms are closed immersions, and `Y` is locally of finite
> presentation over `Bspace`, then `Y ⟶ Xᵢ` is an isomorphism for all sufficiently large `i`.

```lean
theorem eventually_isIso_comp_limitπ
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (contains : B.Contains S)
    {I : Type v} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (Bspace : (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraicBase : IsAlgebraicSpace B S contains Bspace)
    (D : Iᵒᵖ ⥤ (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraicStage : ∀ i, IsAlgebraicSpace B S contains (D.obj (op i)))
    (t : D ⟶ (Functor.const Iᵒᵖ).obj Bspace)
    (c : Cone D) (isLimit : IsLimit c) (s : c.pt ⟶ Bspace)
    (commutes : c.π ≫ t = (Functor.const Iᵒᵖ).map s)
    (Y : (BigFppfOver B S contains)ᵒᵖ ⥤ Type u) (algebraic : IsAlgebraicSpace B S contains Y)
    (f : Y ⟶ c.pt) (iso : IsIso f)
    (quasiCompactStage : ∀ i, IsQuasiCompactSpace B S contains (D.obj (op i)))
    (finiteType : ∀ i, IsLocallyOfFiniteType B S contains (t.app (op i)))
    (closed : ∀ ⦃i j : I⦄ (h : i ≤ j), IsClosedImmersion B S contains (D.map (homOfLE h).op))
    (finitePresentation : IsLocallyOfFinitePresentation B S contains (f ≫ s)) :
    ∀ᶠ i in atTop, IsIso (f ≫ c.π.app (op i))
```

**`AlgebraicGeometry.Space.eventually_mono_comp_limitπ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/EventualMonomorphism.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/EventualMonomorphism.lean#L162). The attribute's comment: “part (4): monomorphism”.

> **Stacks 0828, part (4).** Let `X = lim Xᵢ` be a directed limit of algebraic spaces over an
> algebraic space `Bspace`, with affine transition morphisms and quasi-separated stages, and let
> `f : Y ⟶ X` be a monomorphism whose source is quasi-compact and locally of finite type over
> `Bspace`.  Then `Y ⟶ Xᵢ` is a monomorphism for all sufficiently large `i`.

```lean
theorem eventually_mono_comp_limitπ
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (contains : B.Contains S)
    {I : Type v} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (Bspace : (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraicBase : IsAlgebraicSpace B S contains Bspace)
    (D : Iᵒᵖ ⥤ (BigFppfOver B S contains)ᵒᵖ ⥤ Type u)
    (algebraicStage : ∀ i, IsAlgebraicSpace B S contains (D.obj (op i)))
    (t : D ⟶ (Functor.const Iᵒᵖ).obj Bspace)
    (c : Cone D) (isLimit : IsLimit c) (s : c.pt ⟶ Bspace)
    (commutes : c.π ≫ t = (Functor.const Iᵒᵖ).map s)
    (Y : (BigFppfOver B S contains)ᵒᵖ ⥤ Type u) (algebraic : IsAlgebraicSpace B S contains Y)
    (quasiCompact : IsQuasiCompactSpace B S contains Y)
    (f : Y ⟶ c.pt) [Mono f]
    (affine : ∀ ⦃i j : I⦄ (h : i ≤ j), IsAffineHom B S contains (D.map (homOfLE h).op))
    (quasiSeparated : ∀ i,
      IsAbsolutelyQuasiSeparated B S contains B.contains_terminal (D.obj (op i)))
    (finiteType : IsLocallyOfFiniteType B S contains (f ≫ s)) :
    ∀ᶠ i in atTop, Mono (f ≫ c.π.app (op i))
```

## Tag 086X, a lemma

[Tag 086X](https://stacks.math.columbia.edu/tag/086X) in the Stacks Project.

**`AlgebraicGeometry.Space.DescentSituation.exists_isSeparated_system_app_of_isSiteSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedDescent.lean, line 1093](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedDescent.lean#L1093).

> **Stacks 086X.** Let `Y` be a quasi-separated algebraic space over `S` and let `X = lim X_i`
> be a directed limit, over `Y` and with affine transition morphisms, of quasi-compact and
> quasi-separated algebraic spaces over `S`, as in the standing situation of Stacks 084R. If
> `X ⟶ Y` is separated then `X_i ⟶ Y` is separated for all `i` large enough.
>
> Fix the distinguished stage `0` of the system and choose an affine étale surjective chart
> `U ⟶ X_0`, which exists because `X_0` is quasi-compact, and let `u : U ⟶ Y` be its composite
> with the structure morphism. Base changing the whole situation along `u` is again a situation of
> Stacks 084R — the stages stay quasi-compact because `U` is quasi-compact and `Y` is
> quasi-separated — whose limit `X ×_Y U` is separated over the affine scheme `U`, hence a
> separated algebraic space. So some stage `X_i ×_Y U` is separated by Stacks 084T, that is,
> `X_i ×_Y U ⟶ U` is separated. Affineness of the transition morphism `X_i ⟶ X_0` turns the chart
> `U ⟶ X_0` into a chart `U_i = U ×_{X_0} X_i ⟶ X_i` of that stage, again surjective and étale and
> with `U_i ⟶ X_i ⟶ Y` factoring through `u`; separatedness of `X_i ⟶ Y` therefore descends from
> that of `X_i ×_Y U ⟶ U`. Finally the transition morphisms are affine, hence separated, so
> `X_k ⟶ Y` is separated for every `k ≥ i`.

```lean
theorem DescentSituation.exists_isSeparated_system_app_of_isSiteSmall [IsDirected I (· ≤ ·)]
    (D : DescentSituation B S hS hZ I) (hb : Space.IsSiteSmall B S hS D.system)
    (hY : IsAlgebraicSpace B S hS Y) (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y)
    (t : D.system ⟶ (Functor.const Iᵒᵖ).obj Y) (f : D.limitCone.pt ⟶ Y)
    (hf : ∀ j, D.limitCone.π.app j ≫ t.app j = f) (hsep : IsSeparated B S hS f) :
    ∃ i, D.base ≤ i ∧ ∀ k, i ≤ k → IsSeparated B S hS (t.app (op k))
```

**`AlgebraicGeometry.Space.DescentSituation.exists_isSeparated_system_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedDescent.lean, line 1160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/SeparatedDescent.lean#L1160).

> **Stacks 086X.** Let `Y` be a quasi-separated algebraic space over `S` and let `X = lim X_i`
> be a directed limit, over `Y` and with affine transition morphisms, of quasi-compact and
> quasi-separated algebraic spaces over `S`, as in the standing situation of Stacks 084R. If
> `X ⟶ Y` is separated then `X_i ⟶ Y` is separated for all `i` large enough.
>
> Fix the distinguished stage `0` of the system and choose an affine étale surjective chart
> `U ⟶ X_0`, which exists because `X_0` is quasi-compact, and let `u : U ⟶ Y` be its composite
> with the structure morphism. Base changing the whole situation along `u` is again a situation of
> Stacks 084R — the stages stay quasi-compact because `U` is quasi-compact and `Y` is
> quasi-separated — whose limit `X ×_Y U` is separated over the affine scheme `U`, hence a
> separated algebraic space. So some stage `X_i ×_Y U` is separated by Stacks 084T, that is,
> `X_i ×_Y U ⟶ U` is separated. Affineness of the transition morphism `X_i ⟶ X_0` turns the chart
> `U ⟶ X_0` into a chart `U_i = U ×_{X_0} X_i ⟶ X_i` of that stage, again surjective and étale and
> with `U_i ⟶ X_i ⟶ Y` factoring through `u`; separatedness of `X_i ⟶ Y` therefore descends from
> that of `X_i ×_Y U ⟶ U`. Finally the transition morphisms are affine, hence separated, so
> `X_k ⟶ Y` is separated for every `k ≥ i`.

```lean
theorem DescentSituation.exists_isSeparated_system_app [IsDirected I (· ≤ ·)]
    (D : DescentSituation B S hS hZ I) (hI : #I < B.cutoff.ord.cof)
    (hY : IsAlgebraicSpace B S hS Y) (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y)
    (t : D.system ⟶ (Functor.const Iᵒᵖ).obj Y) (f : D.limitCone.pt ⟶ Y)
    (hf : ∀ j, D.limitCone.π.app j ≫ t.app j = f) (hsep : IsSeparated B S hS f) :
    ∃ i, D.base ≤ i ∧ ∀ k, i ≤ k → IsSeparated B S hS (t.app (op k))
```

## Tag 0A0R, a lemma

[Tag 0A0R](https://stacks.math.columbia.edu/tag/0A0R) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.DescentSituation.exists_isAffineHom_system_app`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineStage/ExistsAffineStage.lean#L213), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineStageSiteSmall.lean, line 754](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DescendingProperties/AffineStageSiteSmall.lean#L754) (StacksFrontier).

## Tag 0A0S, a lemma

[Tag 0A0S](https://stacks.math.columbia.edu/tag/0A0S) in the Stacks Project.

**`AlgebraicGeometry.Space.eventually_isFinite_of_isLimit_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/EventualFiniteness.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/EventualFiniteness.lean#L193).

> **Stacks 0A0S.** Let `X = lim X_i` be a directed limit of algebraic spaces over an algebraic
> space `Y`, with affine transition morphisms. If `Y` is quasi-compact and quasi-separated, every
> `X_i` is quasi-compact and quasi-separated, the transition morphisms are finite, every
> `X_i → Y` is locally of finite type and `X → Y` is integral, then `X_i → Y` is finite for all
> sufficiently large `i`.
>
> The limit `X` is an algebraic space by Stacks 07SF
> (`AlgebraicGeometry.Space.isAlgebraicSpace_limit_of_isSiteSmall`), so that is not assumed.
> Every input of the source's proof is discharged: the affine étale chart of `Y` by Stacks 03H6,
> the affine stage of the base-changed system by Stacks 07SQ, the finiteness of the base-changed
> stages descending to finiteness over `Y` by Stacks 03ZQ, and the scheme case by Stacks 09ZN. The
> index set is asked to be small compared to the cofinality of the site's size cutoff, the Stacks
> 07SF bound that both Stacks 07SQ and the passage from the site to schemes carry here.

```lean
theorem eventually_isFinite_of_isLimit_of_isIntegral
    {I : Type u} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (hI : #I < B.cutoff.ord.cof)
    (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (D : Iᵒᵖ ⥤ ((BigFppfOver B S hS)ᵒᵖ ⥤ Type u))
    (p : D ⟶ (Functor.const Iᵒᵖ).obj Y)
    (c : Cone D) (hc : IsLimit c) (f : c.pt ⟶ Y)
    (hf : ∀ i : I, f = c.π.app (op i) ≫ p.app (op i))
    (hY : IsAlgebraicSpace B S hS Y)
    (hD : ∀ i : I, IsAlgebraicSpace B S hS (D.obj (op i)))
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y)
    (hDqc : ∀ i : I, IsQuasiCompactSpace B S hS (D.obj (op i)))
    (hDqs : ∀ i : I, IsAbsolutelyQuasiSeparated B S hS hZ (D.obj (op i)))
    (haffine : ∀ {i j : I} (h : i ≤ j), IsAffineHom B S hS (D.map (homOfLE h).op))
    (hfinite : ∀ {i j : I} (h : i ≤ j), IsFinite B S hS (D.map (homOfLE h).op))
    (hfiniteType : ∀ i : I, IsLocallyOfFiniteType B S hS (p.app (op i)))
    (hintegral : IsIntegralHom B S hS f) :
    ∀ᶠ i : I in Filter.atTop, IsFinite B S hS (p.app (op i))
```

## Tag 0A0T, a lemma

[Tag 0A0T](https://stacks.math.columbia.edu/tag/0A0T) in the Stacks Project.

**`AlgebraicGeometry.Space.eventually_isClosedImmersion_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/EventuallyClosedImmersionOverBase.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/EventuallyClosedImmersionOverBase.lean#L619).

> **Stacks 0A0T.** Let `Y` be an algebraic space over `S` and let `X = lim X_i` be a directed
> limit of algebraic spaces over `Y` with affine transition morphisms. Assume `Y` is quasi-compact
> and quasi-separated, the `X_i` are quasi-compact and quasi-separated, the transition morphisms
> `X_{i'} ⟶ X_i` are closed immersions, each `X_i ⟶ Y` is locally of finite type, and `X ⟶ Y` is a
> closed immersion. Then `X_i ⟶ Y` is a closed immersion for `i` large enough.
>
> Closed immersions are affine, so the source's assumption that the transition morphisms are
> affine is implied by the assumption that they are closed immersions and is not stated
> separately.
>
> The proof is `AlgebraicGeometry.Space.eventually_isClosedImmersion_app_of_isRepresentable_stage`,
> which is the source's argument down to its appeal to Stacks 07SR, fed with the stage that Stacks
> 07SR provides: the limit of the system base changed along an affine étale surjective chart of
> `Y` is a closed subspace of an affine scheme, hence a scheme, so
> `AlgebraicGeometry.Space.DescentSituation.exists_isRepresentable_system_obj_of_isSiteSmall` makes
> some stage of that base changed system a scheme.
>
> The index type is `I : Type u` and its cardinality is asked to be small compared to the
> cofinality of the site's size cutoff, as in Situation 084R
> (`AlgebraicGeometry.Space.LimitSituation`) and as in every result of that family which this
> library proves — Stacks 07SF, Stacks 0827, Stacks 084T, Stacks 086X, Stacks 07SQ and
> Stacks 07SR. The bound is used only to invoke Stacks 07SR.

```lean
theorem eventually_isClosedImmersion_app
    {I : Type u} [Preorder I] [IsDirected I (· ≤ ·)] [Nonempty I]
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (D : Iᵒᵖ ⥤ (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (t : D ⟶ (Functor.const Iᵒᵖ).obj Y)
    (c : Cone D) (hc : IsLimit c) (f : c.pt ⟶ Y)
    (hcomm : c.π ≫ t = (Functor.const Iᵒᵖ).map f)
    (hY : IsAlgebraicSpace B S hS Y) (hX : IsAlgebraicSpace B S hS c.pt)
    (hD : ∀ i, IsAlgebraicSpace B S hS (D.obj (op i)))
    (hYqc : IsQuasiCompactSpace B S hS Y)
    (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y)
    (hDqc : ∀ i, IsQuasiCompactSpace B S hS (D.obj (op i)))
    (hDqs : ∀ i, IsAbsolutelyQuasiSeparated B S hS hZ (D.obj (op i)))
    (hClosed : ∀ {a b : Iᵒᵖ} (φ : a ⟶ b), IsClosedImmersion B S hS (D.map φ))
    (hFT : ∀ i, IsLocallyOfFiniteType B S hS (t.app (op i)))
    (hf : IsClosedImmersion B S hS f) (hI : #I < B.cutoff.ord.cof) :
    ∀ᶠ i in atTop, IsClosedImmersion B S hS (t.app (op i))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.5, Tag 0826](https://stacks.math.columbia.edu/tag/0826)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

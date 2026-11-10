---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.chowGroupZeroDegree, AlgebraicGeometry.Space.cycleDegree_eq_finsum, AlgebraicGeometry.Space.cycleDegree_eq_sum, AlgebraicGeometry.Space.cycleDegree_eq_finsum_finrank, AlgebraicGeometry.Space.cycleDegree_eq_sum_finrank, AlgebraicGeometry.Space.intersectionNumber_eq_chowGroupZeroDegree_iteratedFirstChernCapCycle
statement: formalized
proof: formalized
---

# 82.32 Degrees of zero cycles

Section 82.32 of the Stacks Project, [Tag 0ESF](https://stacks.math.columbia.edu/tag/0ESF). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0ESG, a definition

[Tag 0ESG](https://stacks.math.columbia.edu/tag/0ESG) in the Stacks Project.

**`AlgebraicGeometry.Space.chowGroupZeroDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowGroupZeroDegree.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ChowGroupZeroDegree.lean#L102).

> Let `p : X ⟶ Y` be a proper morphism of good algebraic spaces over the base,
> where `Y` plays the role of `Spec(k)`: its space of points is a single point, the dimension
> function vanishes there, and `W` is its integral closed subspace. The *degree of a zero cycle* on
> `X` is the composite
>
>   `deg : CH_0(X) ⟶ CH_0(Y) ⟶ ℤ`
>
> of proper pushforward `p_*`, `AlgebraicGeometry.Space.chowGroupProperPushforward`, with the
> natural isomorphism `CH_0(Y) ≅ ℤ` sending the class of `[W]` to `1`,
> `AlgebraicGeometry.Space.chowGroupZeroEquivInt`.

```lean
def chowGroupZeroDegree (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) {p : X ⟶ Y} (hbase : p ≫ sY = sX)
    (hp : IsProper D.site D.base D.base_mem p)
    (hpt : Subsingleton (points D.site D.base D.base_mem Y))
    (hδ : ∀ y : points D.site D.base D.base_mem Y, D.deltaValue sY y = 0)
    (W : IntegralClosedSubspace D.site D.base D.base_mem Y) :
    chowGroup.{v} D sX hX 0 →+ ℤ
```

## Tag 0ESH, a lemma

[Tag 0ESH](https://stacks.math.columbia.edu/tag/0ESH) in the Stacks Project.

**`AlgebraicGeometry.Space.cycleDegree_eq_finsum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroCycleDegree.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroCycleDegree.lean#L195). The attribute's comment: “deg(Z) read as the degree [R(Z) : k] of the extension of function fields, which is the weight of Stacks 0EP0, rather than as dim_k Γ(Z, 𝒪_Z): the two are identified on a scheme by Stacks.Chow.isIso_Γevaluation_of_isIntegral_of_subsingleton, and for an algebraic space there is no evaluation of a global function in a residue field. Spec(k) is modelled as a good algebraic space over the base with one point and vanishing dimension function. The degree is the cycle-level degree, not the one on CH_0 of Stacks 0ESG, which needs Stacks 0EQC”.

> **Stacks 0ESH, in the shape in which this library presents a cycle.** Let `p : X ⟶ Y` be a
> proper morphism of good algebraic spaces over the base with `|Y|` a single point and with the
> dimension function induced on `Y` vanishing — the situation of `Y = Spec(k)`. A zero cycle `α` on
> `X` is the coefficient family `Z ↦ n_Z` on the integral closed subspaces of `X`, so the formal
> sum `α = ∑ n_Z [Z]` of the source is `α` itself, and the degree of `α` is
>
>     deg(α) = ∑ n_Z deg(Z),
>
> the sum running over every integral closed subspace of `X` and `deg(Z)` being the degree
> `[R(Z) : k]` of `Z → Spec(k)`.
>
> This is the definition of proper pushforward, Stacks 0EP1, after two identifications. The sum
> defining the pushforward coefficient at `W` runs over the integral closed subspaces of `X` whose
> integral closed image is `W`, and that is all of them, by
> `AlgebraicGeometry.Space.cycleImageSubspace_eq_of_subsingleton_points`. And at a subspace `Z`
> with a nonzero coefficient the weight of Stacks 0EP0 is the degree rather than zero: the
> δ-dimension of `Z` is zero because `α` is a zero cycle, and the δ-dimension of its image is zero
> because the dimension function of `Y` vanishes.

```lean
theorem cycleDegree_eq_finsum (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) {p : X ⟶ Y} (hbase : p ≫ sY = sX)
    (hp : IsProper D.site D.base D.base_mem p)
    (hpt : Subsingleton (points D.site D.base D.base_mem Y))
    (hδ : ∀ y : points D.site D.base D.base_mem Y, D.deltaValue sY y = 0)
    (W : IntegralClosedSubspace D.site D.base D.base_mem Y) (α : CycleGroup D sX 0) :
    cycleDegree D sX hX sY hY hbase hp W α =
      ∑ᶠ Z : IntegralClosedSubspace D.site D.base D.base_mem X, α.1 Z *
        (cycleResidueDegree D sX hX sY hY p
          (Z.ambientGenericPoint D.site D.base D.base_mem) : ℤ)
```

**`AlgebraicGeometry.Space.cycleDegree_eq_sum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroCycleDegree.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroCycleDegree.lean#L234). The attribute's comment: “the same restriction on deg(Z_i) as on AlgebraicGeometry.Space.cycleDegree_eq_finsum; this is its restatement for a cycle given as a finite sum over pairwise distinct integral closed subspaces”.

> **Stacks 0ESH, in the source's shape.** In the situation of
> `AlgebraicGeometry.Space.cycleDegree_eq_finsum`, let the zero cycle `α` be presented as a finite
> sum `α = ∑ n_i [Z_i]` over pairwise distinct integral closed subspaces `Z_i ⊆ X` — that is, the
> coefficient of `α` at `Z_i` is `n_i` and its coefficient at a subspace which is no `Z_i`
> vanishes. Then
>
>     deg(α) = ∑ n_i deg(Z_i),
>
> with `deg(Z_i)` the degree `[R(Z_i) : k]` of `Z_i → Spec(k)`.
>
> The sum over all integral closed subspaces of `AlgebraicGeometry.Space.cycleDegree_eq_finsum` is
> supported on the `Z_i`, and the `Z_i` are distinct, so it is the finite sum over the index
> type.

```lean
theorem cycleDegree_eq_sum (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) {p : X ⟶ Y} (hbase : p ≫ sY = sX)
    (hp : IsProper D.site D.base D.base_mem p)
    (hpt : Subsingleton (points D.site D.base D.base_mem Y))
    (hδ : ∀ y : points D.site D.base D.base_mem Y, D.deltaValue sY y = 0)
    (W : IntegralClosedSubspace D.site D.base D.base_mem Y) (α : CycleGroup D sX 0)
    {J : Type v} [Fintype J] (Z : J → IntegralClosedSubspace D.site D.base D.base_mem X)
    (hZ : Function.Injective Z) (n : J → ℤ) (hn : ∀ i, α.1 (Z i) = n i)
    (hsupp : ∀ T : IntegralClosedSubspace D.site D.base D.base_mem X,
      (∀ i, Z i ≠ T) → α.1 T = 0) :
    cycleDegree D sX hX sY hY hbase hp W α =
      ∑ i : J, n i * (cycleResidueDegree D sX hX sY hY p
        ((Z i).ambientGenericPoint D.site D.base D.base_mem) : ℤ)
```

**`AlgebraicGeometry.Space.cycleDegree_eq_finsum_finrank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroCycleDegreeGlobalFunctions.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroCycleDegreeGlobalFunctions.lean#L192). The attribute's comment: “deg(Z) is dim_k Γ(Z, 𝒪_Z), as in the source. Spec(k) is modelled as a reduced good algebraic space over the base with one point and vanishing dimension function (which by Stacks 047Z is the spectrum of the field k = Γ(Y, 𝒪_Y)); the cycle is the coefficient family on the integral closed subspaces, so the sum runs over all of them”.

> **Stacks 0ESH, in the shape in which this library presents a cycle.** Let `p : X ⟶ Y` be a
> proper morphism of good algebraic spaces over the base, with `Y` reduced, with a single point
> and with vanishing induced dimension function — the situation of `Y = Spec(k)`. Writing a zero
> cycle `α` on `X` as the coefficient family `Z ↦ n_Z` on the integral closed subspaces of `X`,
>
>     deg(α) = ∑ n_Z dim_k Γ(Z, 𝒪_Z),
>
> where `k = Γ(Y, 𝒪_Y)`.

```lean
theorem cycleDegree_eq_finsum_finrank (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) {p : X ⟶ Y} (hbase : p ≫ sY = sX)
    (hp : IsProper D.site D.base D.base_mem p)
    (hpt : Subsingleton (points D.site D.base D.base_mem Y))
    (hYred : HasEtaleLocalProperty D.site D.base D.base_mem Y
      (fun T : Scheme.{u} => IsReduced T))
    (hδ : ∀ y : points D.site D.base D.base_mem Y, D.deltaValue sY y = 0)
    (W : IntegralClosedSubspace D.site D.base D.base_mem Y) (α : CycleGroup D sX 0) :
    cycleDegree D sX hX sY hY hbase hp W α =
      ∑ᶠ Z : IntegralClosedSubspace D.site D.base D.base_mem X, α.1 Z *
        (letI : Algebra (globalFunctions' D.site D.base D.base_mem Y)
              (globalFunctions' D.site D.base D.base_mem Z.subspace.toFunctor) :=
            (globalFunctionsMap D.site D.base D.base_mem
              (ObjectProperty.homMk (Z.subspace.ι ≫ p) :
                (⟨Z.subspace.toFunctor, Z.isClosedSubspace.1⟩ :
                    AlgebraicSpaces D.site D.base D.base_mem) ⟶ ⟨Y, hY.1⟩)).toAlgebra
        (Module.finrank (globalFunctions' D.site D.base D.base_mem Y)
          (globalFunctions' D.site D.base D.base_mem Z.subspace.toFunctor) : ℤ))
```

**`AlgebraicGeometry.Space.cycleDegree_eq_sum_finrank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroCycleDegreeGlobalFunctions.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ZeroCycleDegreeGlobalFunctions.lean#L225). The attribute's comment: “the same modelling of Spec(k) as in AlgebraicGeometry.Space.cycleDegree_eq_finsum_finrank; this is its restatement for a cycle given as a finite sum over pairwise distinct integral closed subspaces”.

> **Stacks 0ESH, in the source's shape.** In the situation of
> `AlgebraicGeometry.Space.cycleDegree_eq_finsum_finrank`, let the zero cycle `α` be presented as
> a finite sum `α = ∑ n_i [Z_i]` over pairwise distinct integral closed subspaces `Z_i ⊆ X`. Then
>
>     deg(α) = ∑ n_i dim_k Γ(Z_i, 𝒪_{Z_i}),
>
> where `k = Γ(Y, 𝒪_Y)`.

```lean
theorem cycleDegree_eq_sum_finrank (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) {p : X ⟶ Y} (hbase : p ≫ sY = sX)
    (hp : IsProper D.site D.base D.base_mem p)
    (hpt : Subsingleton (points D.site D.base D.base_mem Y))
    (hYred : HasEtaleLocalProperty D.site D.base D.base_mem Y
      (fun T : Scheme.{u} => IsReduced T))
    (hδ : ∀ y : points D.site D.base D.base_mem Y, D.deltaValue sY y = 0)
    (W : IntegralClosedSubspace D.site D.base D.base_mem Y) (α : CycleGroup D sX 0)
    {J : Type v} [Fintype J] (Z : J → IntegralClosedSubspace D.site D.base D.base_mem X)
    (hZ : Function.Injective Z) (n : J → ℤ) (hn : ∀ i, α.1 (Z i) = n i)
    (hsupp : ∀ T : IntegralClosedSubspace D.site D.base D.base_mem X,
      (∀ i, Z i ≠ T) → α.1 T = 0) :
    cycleDegree D sX hX sY hY hbase hp W α =
      ∑ i : J, n i *
        (letI : Algebra (globalFunctions' D.site D.base D.base_mem Y)
              (globalFunctions' D.site D.base D.base_mem (Z i).subspace.toFunctor) :=
            (globalFunctionsMap D.site D.base D.base_mem
              (ObjectProperty.homMk ((Z i).subspace.ι ≫ p) :
                (⟨(Z i).subspace.toFunctor, (Z i).isClosedSubspace.1⟩ :
                    AlgebraicSpaces D.site D.base D.base_mem) ⟶ ⟨Y, hY.1⟩)).toAlgebra
        (Module.finrank (globalFunctions' D.site D.base D.base_mem Y)
          (globalFunctions' D.site D.base D.base_mem (Z i).subspace.toFunctor) : ℤ))
```

## Tag 0ESI, a lemma

[Tag 0ESI](https://stacks.math.columbia.edu/tag/0ESI) in the Stacks Project.

**`AlgebraicGeometry.Space.intersectionNumber_eq_chowGroupZeroDegree_iteratedFirstChernCapCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/IntersectionNumberChowDegree.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/IntersectionNumberChowDegree.lean#L57).

> **Stacks 0ESI.** Let `k` be a field, `X` a proper algebraic space over `k`, `Z ⊆ X` a closed
> subspace of dimension `d` and `ℒ₁, …, ℒ_d` invertible `𝒪_X`-modules. Then
>
> `(ℒ₁ ⋯ ℒ_d · Z) = deg(c₁(ℒ₁) ∩ ⋯ ∩ c₁(ℒ_d) ∩ [Z]_d)`,
>
> the left hand side the intersection number of Stacks 0EDF, `[Z]_d` the `d`-cycle of `Z`
> (Stacks 0EE9), the cap products those of Stacks 0EQJ and `deg : CH_0(X) → ℤ` the degree of
> Stacks 0ESG, in Situation 0EDT over `Spec k` with the zero dimension function.

```lean
theorem intersectionNumber_eq_chowGroupZeroDegree_iteratedFirstChernCapCycle
    (X : AlgebraicSpaces B (Spec (.of k)) hk) (f : X.1 ⟶ yoneda.obj (baseObject k B hk))
    (hf : IsProper B (Spec (.of k)) hk f) (Z : ClosedSubspaces B (Spec (.of k)) hk X.1) (d : ℕ)
    (hd : dimension B (Spec (.of k)) hk Z.1.toFunctor Z.2.1 = d)
    (L : Fin d → Modules.{u, u} B (Spec (.of k)) hk X.1 X.2)
    [hL : ∀ j, Stacks.SheafOfModules.IsInvertible (structurePresheaf B (Spec (.of k)) hk X.1)
      (Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B (Spec (.of k)) hk X.1 X.2).O).property (L j)] :
    intersectionNumber.{u, w} k B hk X (closedSubspaceToSpace B (Spec (.of k)) hk X Z) d f hf
        (closedSubspaceInclusion B (Spec (.of k)) hk X Z) Z.2.2 hd L =
      chowGroupZeroDegree.{v} (fieldSpaceSituation k B hk) f
        (isGood_fieldSpaceSituation_of_isProper k B hk X hf) (𝟙 _)
        (isGood_fieldSpaceSituation_id k B hk) (Category.comp_id f) hf inferInstance
        (fieldSpaceSituation_deltaValue_id k B hk) (fieldSpacePoint k B hk)
        (chowClass.{v} (fieldSpaceSituation k B hk) f
          (isGood_fieldSpaceSituation_of_isProper k B hk X hf) 0
          (iteratedFirstChernCapCycle (fieldSpaceSituation k B hk) f
            (isGood_fieldSpaceSituation_of_isProper k B hk X hf) d L hL 0
            (cycleGroupCast (fieldSpaceSituation k B hk) f (zero_add _).symm
              (closedSubspaceCycle (fieldSpaceSituation k B hk) f
                (isGood_fieldSpaceSituation_of_isProper k B hk X hf) Z.1 Z.2 d
                (deltaDimensionSubspace_le_of_dimension_eq k B hk X hf Z hd)))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.32, Tag 0ESF](https://stacks.math.columbia.edu/tag/0ESF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

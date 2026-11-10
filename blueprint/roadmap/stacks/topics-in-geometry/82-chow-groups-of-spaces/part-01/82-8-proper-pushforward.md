---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.properCycleDegree, AlgebraicGeometry.Space.properCyclePushforward, AlgebraicGeometry.Space.properPushforwardWeightInDimension, AlgebraicGeometry.Space.properPushforwardInDimension, AlgebraicGeometry.Space.properPushforwardInDimension_cycleOfIntegralClosedSubspace_eq_zero, AlgebraicGeometry.Space.properPushforwardInDimension_cycleOfIntegralClosedSubspace, AlgebraicGeometry.Space.properPushforward_integralCycle_integralClosedSubspaceUniv, AlgebraicGeometry.Space.properPushforwardInDimension_comp
statement: formalized
proof: formalized
---

# 82.8 Proper pushforward

Section 82.8 of the Stacks Project, [Tag 0EP0](https://stacks.math.columbia.edu/tag/0EP0). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EP1, a definition

[Tag 0EP1](https://stacks.math.columbia.edu/tag/0EP1) in the Stacks Project.

**`AlgebraicGeometry.Space.properCycleDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCycles.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCycles.lean#L143). The attribute's comment: “part (1): the coefficient of the image in the pushforward of a prime cycle”.

> The coefficient with which the closure `Z'` of the image of an
> integral closed subspace `Z ⊆ X` occurs in `f_*[Z]`: the degree `[R(Z) : R(Z')]` when the
> δ-dimension is preserved, and `0` when it drops.

```lean
noncomputable def properCycleDegree (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) (f : X ⟶ Y)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) : ℤ
```

**`AlgebraicGeometry.Space.properCyclePushforward`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCycles.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCycles.lean#L380). The attribute's comment: “part (2): the pushforward of a k-cycle, as a homomorphism of abelian groups”.

> The proper pushforward of cycles along a quasi-compact morphism `f : X ⟶ Y` of good
> algebraic spaces over `B`: the additive map `f_* : Z_k(X) → Z_k(Y)` sending a cycle `α` to the
> cycle whose coefficient at `Z'` is `∑ α_Z · [R(Z) : R(Z')]`, the sum being over the integral
> closed subspaces `Z ⊆ X` whose image closure is `Z'` and the degree being taken to be `0` where
> the δ-dimension drops. The morphism `f` is assumed quasi-compact, not proper.

```lean
noncomputable def properCyclePushforward (sX : X ⟶ D.space) (hX : D.IsGood sX) (sY : Y ⟶ D.space)
    (hY : D.IsGood sY) {f : X ⟶ Y} (hfB : f ≫ sY = sX)
    (hf : IsQuasiCompact D.site D.base D.base_mem f) (k : ℤ) :
    CycleGroup D sX k →+ CycleGroup D sY k
```

**`AlgebraicGeometry.Space.properPushforwardWeightInDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean#L194). The attribute's comment: “part (1): the multiplicity of an integral closed subspace in the pushforward”.

> **Stacks 0EP1, part (1).** The multiplicity with which proper pushforward along `f` records
> an integral closed subspace `Z` of `X` in the cycle group of δ-dimension `k`: the degree
> `deg(Z/Z')` of `Z` over its integral closed image `Z'` when `dim_δ(Z') = k`, and `0` when
> `dim_δ(Z') < k`, which for `Z` of δ-dimension `k` is the only other case.

```lean
noncomputable def properPushforwardWeightInDimension (sX : X ⟶ D.space) (sY : Y ⟶ D.space)
    (hX : D.IsGood sX) (hY : D.IsGood sY) (f : X ⟶ Y) (k : ℤ)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) : ℤ
```

**`AlgebraicGeometry.Space.properPushforwardInDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean#L347). The attribute's comment: “part (2): the pushforward of a k-cycle, as a map Z_k(X) → Z_k(Y)”.

> Proper pushforward of cycles of δ-dimension `k` along a proper morphism
> `f : X ⟶ Y` of good algebraic spaces over the base: the cycle whose coefficient at `Z'` is the
> sum of `n_Z deg(Z/Z')` over the integral closed subspaces `Z` of `X` with integral closed image
> `Z'` of δ-dimension `k`.

```lean
noncomputable def properPushforwardInDimension (sX : X ⟶ D.space) (sY : Y ⟶ D.space)
    (hX : D.IsGood sX) (hY : D.IsGood sY) (f : X ⟶ Y) (hfB : f ≫ sY = sX)
    (hf : IsProper D.site D.base D.base_mem f) (k : ℤ) :
    CycleGroup D sX k → CycleGroup D sY k
```

**`AlgebraicGeometry.Space.properPushforwardInDimension_cycleOfIntegralClosedSubspace_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean#L404). The attribute's comment: “part (1): f_*[Z] = 0 when dim_δ(Z') < k”.

> The pushforward of the cycle `[Z]` of
> an integral closed subspace of δ-dimension `k` is zero when its integral closed image has
> smaller δ-dimension.

```lean
theorem properPushforwardInDimension_cycleOfIntegralClosedSubspace_eq_zero (sX : X ⟶ D.space)
    (sY : Y ⟶ D.space) (hX : D.IsGood sX) (hY : D.IsGood sY) (f : X ⟶ Y) (hfB : f ≫ sY = sX)
    (hf : IsProper D.site D.base D.base_mem f) (k : ℤ)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) (hZ : deltaDimension D sX Z = k)
    (hlt : deltaDimension D sY (cycleImageSubspace D sY hY f Z) < k) :
    properPushforwardInDimension D sX sY hX hY f hfB hf k
        (cycleOfIntegralClosedSubspace D sX k Z hZ) = 0
```

**`AlgebraicGeometry.Space.properPushforwardInDimension_cycleOfIntegralClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean#L421). The attribute's comment: “part (1): f_*[Z] = deg(Z/Z')·[Z'] when dim_δ(Z') = k”.

> The pushforward of the cycle `[Z]` of
> an integral closed subspace of δ-dimension `k` whose integral closed image `Z'` again has
> δ-dimension `k` is `deg(Z/Z')·[Z']`.

```lean
theorem properPushforwardInDimension_cycleOfIntegralClosedSubspace (sX : X ⟶ D.space)
    (sY : Y ⟶ D.space) (hX : D.IsGood sX) (hY : D.IsGood sY) (f : X ⟶ Y) (hfB : f ≫ sY = sX)
    (hf : IsProper D.site D.base D.base_mem f) (k : ℤ)
    (Z : IntegralClosedSubspace D.site D.base D.base_mem X) (hZ : deltaDimension D sX Z = k)
    (hdim : deltaDimension D sY (cycleImageSubspace D sY hY f Z) = k) :
    properPushforwardInDimension D sX sY hX hY f hfB hf k
        (cycleOfIntegralClosedSubspace D sX k Z hZ) =
      (IntegralClosedSubspace.degreeOverImage D sX sY hX hY f Z : ℤ) •
        cycleOfIntegralClosedSubspace D sY k
          (cycleImageSubspace D sY hY f Z) hdim
```

**`AlgebraicGeometry.Space.properPushforward_integralCycle_integralClosedSubspaceUniv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisor.lean#L366). The attribute's comment: “f_*[X] = [R(X):R(Y)] [Y]: the pushforward of the fundamental cycle of an integral good X along a dominant quasi-compact morphism to an integral good Y of the same δ-dimension”.

> **Stacks 0EP1 at the fundamental cycle.** For a dominant quasi-compact morphism `f : X ⟶ Y`
> over `B` of integral good algebraic spaces with `dim_δ(X) = dim_δ(Y) = n`,
>
> `f_*[X] = [R(X) : R(Y)] [Y]` in `Z_n(Y)`.
>
> The whole of `X` is the only integral closed subspace carrying a coefficient of `[X]`, its image
> closure is the whole of `Y`, and the degree there is `[R(X) : R(Y)]` because the δ-dimension does
> not drop. This is the identity the source uses to read its second conclusion.

```lean
theorem properPushforward_integralCycle_integralClosedSubspaceUniv
    (hYInt : IsIntegralSpace D.site D.base D.base_mem Y) {f : X ⟶ Y}
    (hfB : f ≫ sY = sX) (hf : IsQuasiCompact D.site D.base D.base_mem f)
    (hdom : IsDominant D.site D.base D.base_mem f) {n : ℤ}
    (hnX : deltaDimensionClosed D sX hX Set.univ isClosed_univ = (n : EInt))
    (hnY : deltaDimensionClosed D sY hY Set.univ isClosed_univ = (n : EInt)) :
    properCyclePushforward D sX hX sY hY hfB hf n (integralCycle D sX n
          (integralClosedSubspaceUniv D sX hX hXInt)
          (deltaDimension_integralClosedSubspaceUniv D sX hX hXInt hnX)) =
      (functionFieldDegreeAtGenericPoint D sX hX sY hY hXInt f : ℤ) •
        integralCycle D sY n (integralClosedSubspaceUniv D sY hY hYInt)
          (deltaDimension_integralClosedSubspaceUniv D sY hY hYInt hnY)
```

## Tag 0EP2, a lemma

[Tag 0EP2](https://stacks.math.columbia.edu/tag/0EP2) in the Stacks Project.

**`AlgebraicGeometry.Space.properPushforwardInDimension_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean, line 564](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardCyclesInDimension.lean#L564).

> Proper pushforward of `k`-cycles is functorial: pushing forward along
> `f : X ⟶ Y` and then along `g : Y ⟶ W` is pushing forward along the composite.

```lean
theorem properPushforwardInDimension_comp (sX : X ⟶ D.space) (sY : Y ⟶ D.space) (sW : W ⟶ D.space)
    (hX : D.IsGood sX) (hY : D.IsGood sY) (hW : D.IsGood sW) (f : X ⟶ Y) (g : Y ⟶ W)
    (hfB : f ≫ sY = sX) (hgB : g ≫ sW = sY) (hf : IsProper D.site D.base D.base_mem f)
    (hg : IsProper D.site D.base D.base_mem g) (k : ℤ) (α : CycleGroup D sX k) :
    properPushforwardInDimension D sY sW hY hW g hgB hg k
        (properPushforwardInDimension D sX sY hX hY f hfB hf k α) =
      properPushforwardInDimension D sX sW hX hW (f ≫ g) (by rw [Category.assoc, hgB, hfB])
        (isProper_comp D.site D.base D.base_mem hX.1 hY.1 hW.1 f g hf hg) k α
```

## Tag 0EP3, a lemma

[Tag 0EP3](https://stacks.math.columbia.edu/tag/0EP3) in the Stacks Project.

**`AlgebraicGeometry.Space.properCyclePushforward_associatedCycle_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardModuleCycle.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardModuleCycle.lean#L147). The attribute's comment: “part (2)”.

> **Stacks 0EP3, part (2).** In Situation 0EDT let `f : X ⟶ Y` be a proper morphism of good
> algebraic spaces over the base and let `F` be a coherent `𝒪_X`-module with
> `dim_δ(Supp(F)) ≤ k`. Then
>
> `f_*[F]_k = [f_*F]_k`
>
> in `Z_k(Y)`: the proper pushforward of the `k`-cycle `[F]_k` of Stacks 0EEB is the `k`-cycle
> whose coefficient at an integral closed subspace `W ⊂ Y` of δ-dimension `k` is the length of
> `f_*F` at the generic point of `W`. The cycles of modules are read at chosen geometric
> representatives `γX`, `γY` of the points (by Stacks 0EE1 the lengths do not depend on them). That
> the coefficient family of `f_*F` is a `k`-cycle is part of the statement
> (`AlgebraicGeometry.Space.cycleCoeffOfModule_directImageModule_mem_cyclesOfDimension`); the
> coherence of `f_*F` (Stacks 08AR) is not needed.

```lean
theorem properCyclePushforward_associatedCycle_eq {f : X ⟶ Y} (hfB : f ≫ sY = sX)
    (hproper : IsProper D.site D.base D.base_mem f)
    (F : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    [IsCoherent D.site D.base D.base_mem X hX.1 F] (k : ℤ)
    (hdimF : deltaDimensionClosed D sX hX (moduleSupport D.site D.base D.base_mem hX.1 F)
      (isClosed_moduleSupport D.site D.base D.base_mem hX.1 F) ≤ (k : EInt))
    (γX : points D.site D.base D.base_mem X → GeometricPoint D.site D.base D.base_mem X)
    (hγX : ∀ x, (γX x).LiesOver x)
    (γY : points D.site D.base D.base_mem Y → GeometricPoint D.site D.base D.base_mem Y)
    (hγY : ∀ y, (γY y).LiesOver y) :
    properCyclePushforward D sX hX sY hY hfB hproper.2.1.2 k
        (associatedCycle D sX hX F k γX hγX hdimF) =
      ⟨cycleCoeffOfModule D sY hY (directImageModule D hX.1 hY.1 f F) k γY,
        cycleCoeffOfModule_directImageModule_mem_cyclesOfDimension D sX hX sY hY hfB hproper F k
          hdimF γX hγX γY hγY⟩
```

**`AlgebraicGeometry.Space.properCyclePushforward_closedSubspaceCycle_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardModuleCycle.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardModuleCycle.lean#L288). The attribute's comment: “part (1)”.

> In Situation 0EDT let `f : X ⟶ Y` be a proper morphism of good algebraic spaces over the base
> and let `Z ⊂ X` be a closed subspace with `dim_δ(Z) ≤ k`. Then
>
> `f_*[Z]_k = [f_*𝒪_Z]_k`
>
> in `Z_k(Y)`, where `[Z]_k` is the `k`-cycle of Stacks 0EE9 and `f_*𝒪_Z` is the direct image of
> the structure sheaf of `Z` along `Z → X → Y`: the proper pushforward of `[Z]_k` is the
> `k`-cycle whose coefficient at an integral closed subspace `W ⊂ Y` of δ-dimension `k` is the
> length of `f_*𝒪_Z` at the generic point of `W` (read at the chosen geometric representative
> `γY`; by Stacks 0EE1 it does not depend on it). That this coefficient family is a `k`-cycle is
> part of the statement
> (`cycleCoeffOfModule_closedSubspaceDirectImageStructureSheaf_mem_cyclesOfDimension`).

```lean
theorem properCyclePushforward_closedSubspaceCycle_eq {f : X ⟶ Y} (hfB : f ≫ sY = sX)
    (hproper : IsProper D.site D.base D.base_mem f) (Z : Subfunctor X)
    (hZ : IsClosedSubspace D.site D.base D.base_mem Z) (k : ℤ)
    (hdim : deltaDimensionSubspace D sX hX Z hZ ≤ (k : EInt))
    (γY : points D.site D.base D.base_mem Y → GeometricPoint D.site D.base D.base_mem Y)
    (hγY : ∀ y, (γY y).LiesOver y) :
    properCyclePushforward D sX hX sY hY hfB hproper.2.1.2 k
        (closedSubspaceCycle D sX hX Z hZ k hdim) =
      ⟨cycleCoeffOfModule D sY hY (closedSubspaceDirectImageStructureSheaf D sX hX sY hY f Z hZ)
          k γY,
        cycleCoeffOfModule_closedSubspaceDirectImageStructureSheaf_mem_cyclesOfDimension D sX hX
          sY hY hfB hproper Z hZ k hdim γY hγY⟩
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.8, Tag 0EP0](https://stacks.math.columbia.edu/tag/0EP0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

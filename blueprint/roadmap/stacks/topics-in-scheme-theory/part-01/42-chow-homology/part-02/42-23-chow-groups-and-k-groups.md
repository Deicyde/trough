---
declaration: section
origin: cited
lean: Stacks.Chow.coherentModulesDimLE_isSerreClass, Stacks.Chow.dimensionLayerCycleHom_integralComponentLayerClass, Stacks.Chow.dimensionLayerCycleHom_finsum_integralComponentLayerClass, Stacks.Chow.mem_range_dimensionLayerCycleHom_of_finite_support, Stacks.Chow.dimensionLayerClassHom, Stacks.Chow.dimensionLayerCycleHom_comp_dimensionLayerClassHom, Stacks.Chow.surjective_dimensionLayerCycleHom, Stacks.Chow.dimensionLayerCycleHom
statement: formalized
proof: formalized
---

# 42.23 Chow groups and K-groups

Section 42.23 of the Stacks Project, [Tag 0FDQ](https://stacks.math.columbia.edu/tag/0FDQ). 6 tags here are carried by 47 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02S8, a lemma

[Tag 02S8](https://stacks.math.columbia.edu/tag/02S8) in the Stacks Project.

**`Stacks.Chow.coherentModulesDimLE_isSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/CoherentSupportDimension.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/CoherentSupportDimension.lean#L166).

> **Stacks 02S8.** Coherent `𝒪_X`-modules whose support has delta-dimension at most `k` form a
> Serre subcategory of the category of coherent `𝒪_X`-modules.

```lean
noncomputable instance coherentModulesDimLE_isSerreClass (C : ChowSituation.{u}) (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (k : ℤ) : (coherentModulesDimLE C f k).IsSerreClass
```

## Tag 02S9, a lemma

[Tag 02S9](https://stacks.math.columbia.edu/tag/02S9) in the Stacks Project.

**`Stacks.Chow.dimensionLayerCycleHom_integralComponentLayerClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean#L126). The attribute's comment: “the map `Z_k(X) → K₀(Coh_{≤k}/Coh_{≤k-1})` on a prime cycle: the class of `𝒪_Z` has cycle `[Z]`”.

> The cycle class homomorphism sends the class of `𝒪_Z` to the cycle `[Z]` of the integral closed
> subscheme `Z` attached to a point of relative dimension `k`.

```lean
theorem dimensionLayerCycleHom_integralComponentLayerClass (x : X)
    (hx : relativeDimension C.dimensionFunction f x = k) :
    dimensionLayerCycleHom C f k (integralComponentLayerClass C f k x) =
      cycleAssociatedToClosedSubscheme C f (integralComponentAt x).subschemeι k
```

**`Stacks.Chow.dimensionLayerCycleHom_finsum_integralComponentLayerClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean#L164). The attribute's comment: “the inverse identity `[∑ n_Z 𝒪_Z]_k = ∑ n_Z[Z]`, for a `k`-cycle of finite support”.

> The cycle of the class `∑ n_Z[𝒪_Z]` attached to a `k`-cycle `∑ n_Z[Z]` of finite support is
> `∑ n_Z[Z]` again.

```lean
theorem dimensionLayerCycleHom_finsum_integralComponentLayerClass (α : CycleGroup C f k)
    (hα : (Function.support (α.1 : X → ℤ)).Finite) :
    dimensionLayerCycleHom C f k
        (∑ᶠ x : X, α.1 x • integralComponentLayerClass C f k x) = α
```

**`Stacks.Chow.mem_range_dimensionLayerCycleHom_of_finite_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean#L196). The attribute's comment: “every `k`-cycle of finite support is in the image of `K₀(Coh_{≤k}/Coh_{≤k-1}) → Z_k(X)`”.

> Every `k`-cycle with finite support is the cycle of a class in the Grothendieck group of the
> dimension layer, namely of the weighted sum of the classes of the structure sheaves of the integral
> closed subschemes it is supported on.

```lean
theorem mem_range_dimensionLayerCycleHom_of_finite_support (α : CycleGroup C f k)
    (hα : (Function.support (α.1 : X → ℤ)).Finite) :
    α ∈ (dimensionLayerCycleHom C f k).range
```

**`Stacks.Chow.dimensionLayerClassHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean#L225). The attribute's comment: “the map `Z_k(X) → K₀(Coh_{≤k}/Coh_{≤k-1})`, `∑ n_Z[Z] ↦ ∑ n_Z[𝒪_Z]`, for `X` quasi-compact”.

> The map `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))` for `X` quasi-compact: a `k`-cycle `∑ n_Z[Z]`
> is sent to `∑ n_Z[𝒪_Z]`, the coefficients weighting the classes of the structure sheaves of the
> integral closed subschemes occurring in the cycle.

```lean
def dimensionLayerClassHom :
    CycleGroup C f k →+ GrothendieckGroup (coherentDimensionQuotient C f (k - 1) k)
```

**`Stacks.Chow.dimensionLayerCycleHom_comp_dimensionLayerClassHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean#L246). The attribute's comment: “the inverse identity `Z_k(X) → K₀(Coh_{≤k}/Coh_{≤k-1}) → Z_k(X) = id`, for `X` quasi-compact”.

> For `X` quasi-compact, the composite
> `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) → Z_k(X)` is the identity.

```lean
theorem dimensionLayerCycleHom_comp_dimensionLayerClassHom :
    (dimensionLayerCycleHom C f k).comp (dimensionLayerClassHom C f k) = AddMonoidHom.id _
```

**`Stacks.Chow.surjective_dimensionLayerCycleHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerClassOfCycle.lean#L255). The attribute's comment: “surjectivity of `K₀(Coh_{≤k}/Coh_{≤k-1}) → Z_k(X)`, for `X` quasi-compact”.

> For `X` quasi-compact, every `k`-cycle is the cycle of a class in the Grothendieck group of the
> dimension layer.

```lean
theorem surjective_dimensionLayerCycleHom :
    Function.Surjective (dimensionLayerCycleHom C f k)
```

**`Stacks.Chow.dimensionLayerCycleHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleClass.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleClass.lean#L219). The attribute's comment: “the map `K₀(Coh_{≤k}/Coh_{≤k-1}) → Z_k(X)`, `F ↦ [F]_k`”.

> **Stacks 02S9**, the map `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) → Z_k(X)`, `F ↦ [F]_k`. The cycle
> class of a coherent `𝒪_X`-module of support dimension at most `k` is additive along short exact
> sequences and vanishes on support dimension at most `k - 1`, so it descends to the Grothendieck
> group of the dimension layer.

```lean
def dimensionLayerCycleHom :
    GrothendieckGroup (coherentDimensionQuotient C f (k - 1) k) →+ CycleGroup C f k
```

**`Stacks.Chow.dimensionLayerCycleHom_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleClass.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleClass.lean#L230). The attribute's comment: “the formula `F ↦ [F]_k` for the map out of `K₀(Coh_{≤k}/Coh_{≤k-1})`”.

> **Stacks 02S9.** The homomorphism `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) → Z_k(X)` sends the class of
> the image of a coherent `𝒪_X`-module `F` of support dimension at most `k` to the cycle
> `[F]_k`.

```lean
theorem dimensionLayerCycleHom_of (F : CoherentModulesDimLE C f k) :
    dimensionLayerCycleHom C f k
        (GrothendieckGroup.of
          ((lowerDimensionClass C f (k - 1) k).isoModSerre.Q.obj F)) =
      dimensionLayerCycle C f k F
```

**`Stacks.Chow.cycleDimensionLayerHom_dimensionLayerCycleHom_mutuallyInverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleEquiv.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleEquiv.lean#L407). The attribute's comment: “the two maps, given by their formulas, are mutually inverse isomorphisms”.

> **Stacks 02S9.** Let `X` be locally of finite type over `(S, δ)`. The maps
> `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))`,
> `∑ n_Z[Z] ↦ [⨁_{n_Z > 0} 𝒪_Z^{⊕n_Z}] - [⨁_{n_Z < 0} 𝒪_Z^{⊕-n_Z}]`, and
> `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) → Z_k(X)`, `F ↦ [F]_k`, are mutually inverse isomorphisms.
>
> The first two conjuncts are the formulas defining the two maps (the direct sums are the locally
> finite direct sums of `Stacks.Chow.cycleStructureSheafDimLE`), the last two the two composites
> being the identity.

```lean
theorem cycleDimensionLayerHom_dimensionLayerCycleHom_mutuallyInverse :
    (∀ c : CycleGroup C f k, cycleDimensionLayerHom C f k c =
      GrothendieckGroup.of ((lowerDimensionClass C f (k - 1) k).isoModSerre.Q.obj
          (cycleStructureSheafDimLE C f k (cyclePositivePart C f k c))) -
        GrothendieckGroup.of ((lowerDimensionClass C f (k - 1) k).isoModSerre.Q.obj
          (cycleStructureSheafDimLE C f k (cycleNegativePart C f k c)))) ∧
    (∀ F : CoherentModulesDimLE C f k, dimensionLayerCycleHom C f k
        (GrothendieckGroup.of ((lowerDimensionClass C f (k - 1) k).isoModSerre.Q.obj F)) =
      dimensionLayerCycle C f k F) ∧
    (dimensionLayerCycleHom C f k).comp (cycleDimensionLayerHom C f k) = AddMonoidHom.id _ ∧
    (cycleDimensionLayerHom C f k).comp (dimensionLayerCycleHom C f k) = AddMonoidHom.id _
```

**`Stacks.Chow.cycleGroupAddEquivDimensionLayer`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleEquiv.lean, line 426](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleEquiv.lean#L426). The attribute's comment: “`Z_k(X) ≃ K₀(Coh_{≤k}/Coh_{≤k-1})` by the two maps of the lemma”.

> **Stacks 02S9**, as an isomorphism: the group of `k`-cycles on `X` and the Grothendieck group
> of the dimension layer `Coh_{≤k}(X)/Coh_{≤k-1}(X)`, identified by the two mutually inverse maps
> `∑ n_Z[Z] ↦ [⨁_{n_Z > 0} 𝒪_Z^{⊕n_Z}] - [⨁_{n_Z < 0} 𝒪_Z^{⊕-n_Z}]` and `F ↦ [F]_k`.

```lean
def cycleGroupAddEquivDimensionLayer :
    CycleGroup C f k ≃+ GrothendieckGroup (coherentDimensionQuotient C f (k - 1) k)
```

**`Stacks.Chow.cycleDimensionLayerHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean#L699). The attribute's comment: “the map `Z_k(X) → K₀(Coh_{≤k}/Coh_{≤k-1})`”.

> **Stacks 02S9**, the map `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))`. A `k`-cycle `∑ n_Z[Z]` is
> sent to `[⨁_{n_Z > 0} 𝒪_Z^{⊕n_Z}] - [⨁_{n_Z < 0} 𝒪_Z^{⊕-n_Z}]`, the two locally finite direct
> sums being coherent `𝒪_X`-modules whose support has delta-dimension at most `k`.

```lean
def cycleDimensionLayerHom (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (k : ℤ) :
    CycleGroup C f k →+ GrothendieckGroup (coherentDimensionQuotient C f (k - 1) k)
```

**`Stacks.Chow.cycleDimensionLayerHom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean, line 708](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean#L708). The attribute's comment: “the formula `∑ n_Z[Z] ↦ [⨁_{n_Z > 0} 𝒪_Z^{⊕n_Z}] - [⨁_{n_Z < 0} 𝒪_Z^{⊕-n_Z}]`”.

> **Stacks 02S9.** The homomorphism `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))` sends a `k`-cycle
> `∑ n_Z[Z]` to the difference of the classes of the direct sums of the structure sheaves of the
> integral closed subschemes occurring with positive, respectively negative, coefficient.

```lean
theorem cycleDimensionLayerHom_apply (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (k : ℤ) (c : CycleGroup C f k) :
    cycleDimensionLayerHom C f k c =
      GrothendieckGroup.of ((lowerDimensionClass C f (k - 1) k).isoModSerre.Q.obj
          (cycleStructureSheafDimLE C f k (cyclePositivePart C f k c))) -
        GrothendieckGroup.of ((lowerDimensionClass C f (k - 1) k).isoModSerre.Q.obj
          (cycleStructureSheafDimLE C f k (cycleNegativePart C f k c)))
```

**`Stacks.Chow.dimensionLayerCycleHom_comp_cycleDimensionLayerHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean, line 992](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean#L992). The attribute's comment: “the composite `Z_k(X) → K₀(Coh_{≤k}/Coh_{≤k-1}) → Z_k(X)` is the identity”.

> **Stacks 02S9**, one of the two inverse identities: the composite
> `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) → Z_k(X)` of the two maps of Tag 02S9 is the identity.
>
> On a cycle `∑ n_Z[Z]` the two locally finite direct sums have cycles `∑_{n_Z > 0} n_Z[Z]` and
> `∑_{n_Z < 0} (-n_Z)[Z]`, whose difference is the cycle one started with.

```lean
theorem dimensionLayerCycleHom_comp_cycleDimensionLayerHom (C : ChowSituation.{u})
    {X : Scheme.{u}} (f : X ⟶ C.S) [LocallyOfFiniteType f] (k : ℤ) :
    (dimensionLayerCycleHom C f k).comp (cycleDimensionLayerHom C f k) = AddMonoidHom.id _
```

**`Stacks.Chow.dimensionLayerCycleHom_cycleDimensionLayerHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean, line 1011](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean#L1011). The attribute's comment: “`[⨁_{n_Z > 0} 𝒪_Z^{⊕n_Z}]_k - [⨁_{n_Z < 0} 𝒪_Z^{⊕-n_Z}]_k = ∑ n_Z[Z]`”.

> **Stacks 02S9.** The cycle class of the element of `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))` attached
> to a `k`-cycle is that cycle.

```lean
theorem dimensionLayerCycleHom_cycleDimensionLayerHom (C : ChowSituation.{u}) {X : Scheme.{u}}
    (f : X ⟶ C.S) [LocallyOfFiniteType f] (k : ℤ) (c : CycleGroup C f k) :
    dimensionLayerCycleHom C f k (cycleDimensionLayerHom C f k c) = c
```

**`Stacks.Chow.injective_cycleDimensionLayerHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean, line 1021](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean#L1021). The attribute's comment: “injectivity of `Z_k(X) → K₀(Coh_{≤k}/Coh_{≤k-1})`”.

> **Stacks 02S9**, half of the bijectivity. The map
> `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))` is injective, the cycle class homomorphism being a left
> inverse of it.

```lean
theorem injective_cycleDimensionLayerHom (C : ChowSituation.{u}) {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (k : ℤ) : Function.Injective (cycleDimensionLayerHom C f k)
```

**`Stacks.Chow.surjective_dimensionLayerCycleHom_of_cycleDimensionLayerHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean, line 1039](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleFromCycles.lean#L1039). The attribute's comment: “surjectivity of `K₀(Coh_{≤k}/Coh_{≤k-1}) → Z_k(X)`, with no quasi-compactness”.

> **Stacks 02S9**, half of the bijectivity. The cycle class homomorphism
> `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) → Z_k(X)` is surjective: every `k`-cycle is the cycle class of the
> element attached to it.
>
> The same conclusion is proved, for a quasi-compact `X`, as
> `Stacks.Chow.surjective_dimensionLayerCycleHom` in
> `StacksFrontier.AlgebraicGeometry.Chow.Degrees.DimensionLayerClassOfCycle`, through the rival
> construction of the map of Tag 02S9 recorded in
> `StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerCycleClass.lean`. The version here
> needs no quasi-compactness, the section it uses being `Stacks.Chow.cycleDimensionLayerHom`,
> which is defined for every `X` locally of finite type over the base; hence the name, and hence
> no quasi-compactness in the attribute below.

```lean
theorem surjective_dimensionLayerCycleHom_of_cycleDimensionLayerHom (C : ChowSituation.{u})
    {X : Scheme.{u}} (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (k : ℤ) : Function.Surjective (dimensionLayerCycleHom C f k)
```

**`Stacks.Chow.cycleDimensionLayerHom_dimensionLayerCycle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean, line 890](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean#L890). The attribute's comment: “`[F] = ∑ m_ξ[Z_ξ]` in `K₀(Coh_{≤k}/Coh_{≤k-1})`, for `X` Noetherian”.

> On a Noetherian scheme, the class of a coherent `𝒪_X`-module `F` of support dimension at most
> `k` in `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))` is the image of its cycle `[F]_k` under the map
> `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))`.

```lean
theorem cycleDimensionLayerHom_dimensionLayerCycle [IsNoetherian X]
    (F : CoherentModulesDimLE C f k) :
    cycleDimensionLayerHom C f k (dimensionLayerCycle C f k F) =
      GrothendieckGroup.of ((lowerDimensionClass C f (k - 1) k).isoModSerre.Q.obj F)
```

**`Stacks.Chow.cycleDimensionLayerHom_comp_dimensionLayerCycleHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean, line 901](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean#L901). The attribute's comment: “`K₀(Coh_{≤k}/Coh_{≤k-1}) → Z_k(X) → K₀` is the identity, for `X` Noetherian”.

> On a Noetherian scheme, the composite
> `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) → Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))` of the cycle map and
> the cycle class map is the identity.

```lean
theorem cycleDimensionLayerHom_comp_dimensionLayerCycleHom [IsNoetherian X] :
    (cycleDimensionLayerHom C f k).comp (dimensionLayerCycleHom C f k) = AddMonoidHom.id _
```

**`Stacks.Chow.surjective_cycleDimensionLayerHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean, line 908](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean#L908). The attribute's comment: “surjectivity of `Z_k(X) → K₀(Coh_{≤k}/Coh_{≤k-1})`, for `X` Noetherian”.

> On a Noetherian scheme, the map `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))` is surjective.

```lean
theorem surjective_cycleDimensionLayerHom [IsNoetherian X] :
    Function.Surjective (cycleDimensionLayerHom C f k)
```

**`Stacks.Chow.bijective_cycleDimensionLayerHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean, line 916](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean#L916). The attribute's comment: “bijectivity of `Z_k(X) → K₀(Coh_{≤k}/Coh_{≤k-1})`, for `X` Noetherian”.

> On a Noetherian scheme, the map `Z_k(X) → K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))` is bijective, the
> cycle class homomorphism being a two-sided inverse.

```lean
theorem bijective_cycleDimensionLayerHom [IsNoetherian X] :
    Function.Bijective (cycleDimensionLayerHom C f k)
```

**`Stacks.Chow.cycleDimensionLayerEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean, line 925](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean#L925). The attribute's comment: “`Z_k(X) ≃ K₀(Coh_{≤k}/Coh_{≤k-1})`, for `X` Noetherian”.

> On a Noetherian scheme `X`, the group of `k`-cycles on `X` is the Grothendieck
> group of the dimension layer `Coh_{≤k}(X)/Coh_{≤k-1}(X)`, by the two mutually inverse
> homomorphisms `∑ n_Z[Z] ↦ [⨁_{n_Z > 0} 𝒪_Z^{⊕n_Z}] - [⨁_{n_Z < 0} 𝒪_Z^{⊕-n_Z}]` and
> `F ↦ [F]_k`.

```lean
def cycleDimensionLayerEquiv [IsNoetherian X] :
    CycleGroup C f k ≃+ GrothendieckGroup (coherentDimensionQuotient C f (k - 1) k)
```

**`Stacks.Chow.cycleDimensionLayerEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean, line 933](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean#L933). The attribute's comment: “the formula for `Z_k(X) ≃ K₀(Coh_{≤k}/Coh_{≤k-1})`, for `X` Noetherian”.

> On a Noetherian scheme, the identification of the group of `k`-cycles with the Grothendieck
> group of the dimension layer sends a cycle `∑ n_Z[Z]` to
> `[⨁_{n_Z > 0} 𝒪_Z^{⊕n_Z}] - [⨁_{n_Z < 0} 𝒪_Z^{⊕-n_Z}]`.

```lean
theorem cycleDimensionLayerEquiv_apply [IsNoetherian X] (c : CycleGroup C f k) :
    cycleDimensionLayerEquiv C f k c = cycleDimensionLayerHom C f k c
```

**`Stacks.Chow.cycleDimensionLayerEquiv_symm_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean, line 941](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerStructureSheafClass.lean#L941). The attribute's comment: “the inverse formula for `Z_k(X) ≃ K₀`, for `X` Noetherian”.

> On a Noetherian scheme, the inverse of the identification of the group of `k`-cycles with the
> Grothendieck group of the dimension layer sends the class of a coherent module `F` to the cycle
> `[F]_k`.

```lean
theorem cycleDimensionLayerEquiv_symm_apply [IsNoetherian X]
    (x : GrothendieckGroup (coherentDimensionQuotient C f (k - 1) k)) :
    (cycleDimensionLayerEquiv C f k).symm x = dimensionLayerCycleHom C f k x
```

## Tag 0FDR, a lemma

[Tag 0FDR](https://stacks.math.columbia.edu/tag/0FDR) in the Stacks Project.

**`Stacks.Chow.finitePushforwardCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L78). The attribute's comment: “the functor `π_* : Coh(X) ⥤ Coh(Y)`”.

> Direct image along a finite morphism to a locally Noetherian scheme, as a functor on coherent
> modules.

```lean
def finitePushforwardCoherent :
    Stacks.SheafOfModules.CoherentModules X.ringCatSheaf ⥤
      Stacks.SheafOfModules.CoherentModules Y.ringCatSheaf
```

**`Stacks.Chow.shortExact_map_finitePushforwardCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L155). The attribute's comment: “`π_*` is an exact functor on coherent sheaves”.

> Direct image along a finite morphism carries a short exact sequence of coherent modules to a
> short exact sequence.

```lean
theorem shortExact_map_finitePushforwardCoherent
    ⦃S : ShortComplex (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)⦄
    (hS : S.ShortExact) : (S.map (finitePushforwardCoherent π)).ShortExact
```

**`Stacks.Chow.finitePushforwardCoherentHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L163). The attribute's comment: “the induced homomorphism `K₀(Coh(X)) → K₀(Coh(Y))`”.

> The homomorphism `K₀(Coh(X)) → K₀(Coh(Y))` induced by direct image along a finite
> morphism.

```lean
def finitePushforwardCoherentHom :
    GrothendieckGroup (Stacks.SheafOfModules.CoherentModules X.ringCatSheaf) →+
      GrothendieckGroup (Stacks.SheafOfModules.CoherentModules Y.ringCatSheaf)
```

**`Stacks.Chow.coherentModulesDimLE_finitePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L184). The attribute's comment: “`π_*` sends `Coh_{≤k}(X)` into `Coh_{≤k}(Y)`”.

> The direct image along a finite morphism of a coherent module whose support has
> delta-dimension at most `k` again has support of delta-dimension at most `k`.

```lean
theorem coherentModulesDimLE_finitePushforward (C : ChowSituation.{u}) (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (π : X ⟶ Y) [IsFinite π]
    (hπ : π ≫ sY = sX) (k : ℤ)
    (F : Stacks.SheafOfModules.CoherentModules X.ringCatSheaf)
    (hF : coherentModulesDimLE C sX k F) :
    have : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian sY
    coherentModulesDimLE C sY k ((finitePushforwardCoherent π).obj F)
```

**`Stacks.Chow.finitePushforwardDimLE`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L201). The attribute's comment: “the functor `π_* : Coh_{≤k}(X) ⥤ Coh_{≤k}(Y)`”.

> The restriction of `π_*` to the coherent modules whose support has delta-dimension at most
> `k`.

```lean
def finitePushforwardDimLE (C : ChowSituation.{u}) (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (π : X ⟶ Y) [IsFinite π] (hπ : π ≫ sY = sX)
    (k : ℤ) : CoherentModulesDimLE C sX k ⥤ CoherentModulesDimLE C sY k
```

**`Stacks.Chow.shortExact_map_finitePushforwardDimLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L250). The attribute's comment: “`π_*` is exact on `Coh_{≤k}`”.

> Direct image along a finite morphism carries a short exact sequence of coherent modules of
> support dimension at most `k` to a short exact sequence.

```lean
theorem shortExact_map_finitePushforwardDimLE (C : ChowSituation.{u}) (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (π : X ⟶ Y) [IsFinite π]
    (hπ : π ≫ sY = sX) (k : ℤ) ⦃S : ShortComplex (CoherentModulesDimLE C sX k)⦄
    (hS : S.ShortExact) : (S.map (finitePushforwardDimLE C sX sY π hπ k)).ShortExact
```

**`Stacks.Chow.finitePushforwardDimLEHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L259). The attribute's comment: “the induced homomorphism `K₀(Coh_{≤k}(X)) → K₀(Coh_{≤k}(Y))`”.

> The homomorphism `K₀(Coh_{≤k}(X)) → K₀(Coh_{≤k}(Y))` induced by direct image along a finite
> morphism.

```lean
def finitePushforwardDimLEHom (C : ChowSituation.{u}) (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (π : X ⟶ Y) [IsFinite π] (hπ : π ≫ sY = sX)
    (k : ℤ) :
    GrothendieckGroup (CoherentModulesDimLE C sX k) →+
      GrothendieckGroup (CoherentModulesDimLE C sY k)
```

**`Stacks.Chow.dimensionLayerFinitePushforwardHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L309). The attribute's comment: “the induced homomorphism `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) → K₀(Coh_{≤k}(Y)/Coh_{≤k-1}(Y))`”.

> The homomorphism `K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X)) → K₀(Coh_{≤k}(Y)/Coh_{≤k-1}(Y))` induced by
> direct image along a finite morphism.

```lean
def dimensionLayerFinitePushforwardHom (C : ChowSituation.{u}) (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (π : X ⟶ Y) [IsFinite π]
    (hπ : π ≫ sY = sX) (k : ℤ) :
    GrothendieckGroup (coherentDimensionQuotient C sX (k - 1) k) →+
      GrothendieckGroup (coherentDimensionQuotient C sY (k - 1) k)
```

**`Stacks.Chow.dimensionLayerFinitePushforwardHom_of`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L322). The attribute's comment: “the induced homomorphism on a layer sends `[F]` to `[π_* F]`”.

> The homomorphism on the Grothendieck groups of the layers sends the class of the image of a
> module `F` of `Coh_{≤k}(X)` to the class of the image of `π_* F`.

```lean
theorem dimensionLayerFinitePushforwardHom_of (C : ChowSituation.{u}) (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (π : X ⟶ Y) [IsFinite π]
    (hπ : π ≫ sY = sX) (k : ℤ) (F : CoherentModulesDimLE C sX k) :
    dimensionLayerFinitePushforwardHom C sX sY π hπ k
        (GrothendieckGroup.of ((lowerDimensionClass C sX (k - 1) k).isoModSerre.Q.obj F)) =
      GrothendieckGroup.of ((lowerDimensionClass C sY (k - 1) k).isoModSerre.Q.obj
        ((finitePushforwardDimLE C sX sY π hπ k).obj F))
```

**`Stacks.Chow.properPushforwardHom_comp_dimensionLayerCycleHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 342](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L342). The attribute's comment: “commutativity of the right-hand square of the diagram”.

> The cycle class homomorphism `K₀(Coh_{≤k}/Coh_{≤k-1}) ⟶ Z_k` commutes with direct image
> along a finite morphism on the source and proper pushforward of `k`-cycles on the target.

```lean
theorem properPushforwardHom_comp_dimensionLayerCycleHom (C : ChowSituation.{u}) (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY] (π : X ⟶ Y) [IsFinite π]
    (hπ : π ≫ sY = sX) (k : ℤ) :
    (properPushforwardHom C sX sY π hπ k).comp (dimensionLayerCycleHom C sX k) =
      (dimensionLayerCycleHom C sY k).comp
        (dimensionLayerFinitePushforwardHom C sX sY π hπ k)
```

**`Stacks.Chow.dimensionLayerFinitePushforwardHom_comp_cycleDimensionLayerHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L367). The attribute's comment: “commutativity of the left-hand square of the diagram, for `Y` Noetherian”.

> For `Y` Noetherian, the homomorphism `Z_k ⟶ K₀(Coh_{≤k}/Coh_{≤k-1})` commutes with proper
> pushforward of `k`-cycles on the source and direct image along the finite morphism `π` on the
> target.

```lean
theorem dimensionLayerFinitePushforwardHom_comp_cycleDimensionLayerHom (C : ChowSituation.{u})
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (π : X ⟶ Y) [IsFinite π] [IsNoetherian Y] (hπ : π ≫ sY = sX) (k : ℤ) :
    (dimensionLayerFinitePushforwardHom C sX sY π hπ k).comp (cycleDimensionLayerHom C sX k) =
      (cycleDimensionLayerHom C sY k).comp (properPushforwardHom C sX sY π hπ k)
```

**`Stacks.Chow.dimensionLayerFinitePushforwardHom_cycleDimensionLayerHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforward.lean#L385). The attribute's comment: “the left-hand square of the diagram on a cycle, for `Y` Noetherian”.

> For `Y` Noetherian, the element of the Grothendieck group of the layer over `Y` attached to
> the proper pushforward of a `k`-cycle `c` on `X` is the direct image along `π` of the element
> attached to `c`.

```lean
theorem dimensionLayerFinitePushforwardHom_cycleDimensionLayerHom (C : ChowSituation.{u})
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (π : X ⟶ Y) [IsFinite π] [IsNoetherian Y] (hπ : π ≫ sY = sX) (k : ℤ)
    (c : CycleGroup C sX k) :
    dimensionLayerFinitePushforwardHom C sX sY π hπ k (cycleDimensionLayerHom C sX k c) =
      cycleDimensionLayerHom C sY k (properPushforwardHom C sX sY π hπ k c)
```

**`Stacks.Chow.cycleDimensionLayerHom_comp_properPushforwardHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforwardSquare.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforwardSquare.lean#L68). The attribute's comment: “commutativity of the left-hand square of the diagram”.

> **Stacks 0FDR**, the left-hand square of the diagram. The homomorphism
> `Z_k ⟶ K₀(Coh_{≤k}/Coh_{≤k-1})` of Stacks 02S9 commutes with proper pushforward of `k`-cycles on
> the source and direct image along the finite morphism `π` on the target.
>
> As in the source, it follows from the right-hand square
> `Stacks.Chow.properPushforwardHom_comp_dimensionLayerCycleHom` because the two maps of Tag 02S9
> are mutually inverse, over `X` and over `Y`, each being merely locally of finite type over the
> base.

```lean
theorem cycleDimensionLayerHom_comp_properPushforwardHom :
    (cycleDimensionLayerHom C sY k).comp (properPushforwardHom C sX sY π hπ k) =
      (dimensionLayerFinitePushforwardHom C sX sY π hπ k).comp
        (cycleDimensionLayerHom C sX k)
```

**`Stacks.Chow.cycleDimensionLayerHom_properPushforwardHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforwardSquare.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforwardSquare.lean#L85). The attribute's comment: “the left-hand square of the diagram on a cycle”.

> **Stacks 0FDR**, the left-hand square read on a cycle. The element of the Grothendieck group
> of the layer over `Y` attached to the proper pushforward of a `k`-cycle `c` on `X` is the direct
> image along `π` of the element attached to `c`.

```lean
theorem cycleDimensionLayerHom_properPushforwardHom (c : CycleGroup C sX k) :
    cycleDimensionLayerHom C sY k (properPushforwardHom C sX sY π hπ k c) =
      dimensionLayerFinitePushforwardHom C sX sY π hπ k (cycleDimensionLayerHom C sX k c)
```

**`Stacks.Chow.finitePushforward_dimensionLayer_diagram_commutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforwardSquare.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/DimensionLayerFinitePushforwardSquare.lean#L95). The attribute's comment: “the maps of Tag 02S9 fit into a commutative diagram with `π_*`”.

> **Stacks 0FDR**, the diagram. The maps of Stacks 02S9,
> `Z_k ⟶ K₀(Coh_{≤k}/Coh_{≤k-1}) ⟶ Z_k`, over `X` and over `Y`, together with proper pushforward
> of `k`-cycles on the two outer columns and direct image along `π` on the middle column, form a
> commutative diagram: both the left-hand and the right-hand square commute.

```lean
theorem finitePushforward_dimensionLayer_diagram_commutes :
    (cycleDimensionLayerHom C sY k).comp (properPushforwardHom C sX sY π hπ k) =
        (dimensionLayerFinitePushforwardHom C sX sY π hπ k).comp
          (cycleDimensionLayerHom C sX k) ∧
      (properPushforwardHom C sX sY π hπ k).comp (dimensionLayerCycleHom C sX k) =
        (dimensionLayerCycleHom C sY k).comp
          (dimensionLayerFinitePushforwardHom C sX sY π hπ k)
```

## Tag 0FDS, a lemma

[Tag 0FDS](https://stacks.math.columbia.edu/tag/0FDS) in the Stacks Project.

**`Stacks.Chow.chowToWideDimensionLayerHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/ChowToWideLayer.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/ChowToWideLayer.lean#L97). The attribute's comment: “for a quasi-compact `X`; the cycle identity is formalized in the orientation `[𝒪_X/fI]_k − [𝒪_X/I]_k = div(f)`, correcting the sign-inverted chain of the source”.

> For a quasi-compact scheme `X` locally of finite type over the base scheme of a Chow situation
> there is a canonical homomorphism
> `CH_k(X) ⟶ K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X))` sending the class of a `k`-cycle `∑ n_Z[Z]` to the
> class of `[⨁_{n_Z > 0} 𝒪_Z^{⊕n_Z}] − [⨁_{n_Z < 0} 𝒪_Z^{⊕-n_Z}]` in the wide dimension layer.

```lean
def chowToWideDimensionLayerHom (C : ChowSituation.{u}) {X : Scheme.{u}} (sX : X ⟶ C.S)
    [LocallyOfFiniteType sX] [CompactSpace X] (k : ℤ) :
    chowGroup C sX k →+ coherentDimensionKZero C sX (k - 1) (k + 1)
```

**`Stacks.Chow.chowToWideLayerHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/ChowToWideLayerGeneral.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/ChowToWideLayerGeneral.lean#L386).

> **Stacks 0FDS.** For a scheme `X` locally of finite type over the base of a Chow situation
> there is a canonical homomorphism `CH_k(X) ⟶ K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X))` induced by the map
> `Z_k(X) ⟶ K₀(Coh_{≤k}(X)/Coh_{≤k-1}(X))` of Tag 02S9: it sends the class of a `k`-cycle `c` to
> the image of the class of `c` under the map widening the layer, see
> `Stacks.Chow.chowToWideLayerHom_mk`.

```lean
def chowToWideLayerHom (C : ChowSituation.{u}) (sX : X ⟶ C.S) [LocallyOfFiniteType sX]
    (k : ℤ) : chowGroup C sX k →+ coherentDimensionKZero C sX (k - 1) (k + 1)
```

## Tag 02SD, a remark

[Tag 02SD](https://stacks.math.columbia.edu/tag/02SD) in the Stacks Project.

**`Stacks.Chow.chowToCoherentQuotientHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/ChowToCoherentQuotient.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/ChowToCoherentQuotient.lean#L71). The attribute's comment: “the canonical map `CH_k(X) → K₀(Coh(X)/Coh_{≤k-1}(X))`, built from Lemma 0FDS”.

> **Stacks 02SD**, the canonical map `CH_k(X) → K₀(Coh(X)/Coh_{≤k-1}(X))` for `X` locally of
> finite type over the base of a Chow situation: the canonical map
> `CH_k(X) → K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X))` of Lemma 0FDS (`Stacks.Chow.chowToWideLayerHom`)
> followed by the canonical map `K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X)) → K₀(Coh(X)/Coh_{≤k-1}(X))`
> (`Stacks.Chow.coherentDimensionToQuotientHom`).

```lean
def chowToCoherentQuotientHom (C : ChowSituation.{u}) (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (k : ℤ) : chowGroup C f k →+ coherentQuotientKZero C f (k - 1)
```

**`Stacks.Chow.coherentDimensionToQuotientHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/CoherentQuotientKGroup.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/CoherentQuotientKGroup.lean#L156). The attribute's comment: “the canonical map `K₀(Coh_{≤b}/Coh_{≤a}) → K₀(Coh/Coh_{≤a})`”.

> The canonical map `K₀(Coh_{≤b}(X)/Coh_{≤a}(X)) → K₀(Coh(X)/Coh_{≤a}(X))`: the homomorphism of
> Grothendieck groups induced by the exact functor that drops the upper dimension bound.

```lean
def coherentDimensionToQuotientHom (C : ChowSituation.{u}) (f : X ⟶ C.S)
    [LocallyOfFiniteType f] (a b : ℤ) :
    coherentDimensionKZero C f a b →+ coherentQuotientKZero C f a
```

**`Stacks.Chow.chowToCoherentQuotientKZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/Degrees/CoherentQuotientKGroup.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/Degrees/CoherentQuotientKGroup.lean#L177). The attribute's comment: “the canonical map `CH_k(X) → K₀(Coh/Coh_{≤k-1})`”.

> The canonical map `CH_k(X) → K₀(Coh(X)/Coh_{≤k-1}(X))`: the composite of a cycle class map
> `φ : CH_k(X) → K₀(Coh_{≤k+1}(X)/Coh_{≤k-1}(X))` with the canonical map that drops the upper
> dimension bound.

```lean
def chowToCoherentQuotientKZero (C : ChowSituation.{u}) (f : X ⟶ C.S) [LocallyOfFiniteType f]
    (k : ℤ) (φ : chowGroup C f k →+ coherentDimensionKZero C f (k - 1) (k + 1)) :
    chowGroup C f k →+ coherentQuotientKZero C f (k - 1)
```

## Tag 0FDT, a lemma

[Tag 0FDT](https://stacks.math.columbia.edu/tag/0FDT) in the Stacks Project.

**`AlgebraicGeometry.coherentToSupportedCoherentKZeroHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentKGroup.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentKGroup.lean#L193). The attribute's comment: “the exact fully faithful inclusion functor Coh(Z) → Coh\_Z(X) and the homomorphism K'\_0(Z) = K\_0(Coh(Z)) → K\_0(Coh\_Z(X)) that it induces. That this homomorphism is an isomorphism is NOT covered: the source inverts it by sending a coherent module F supported on Z to the class of the graded module of its I-adic filtration. The graded pieces of that filtration are available, as the short exact sequence with the coherence and support bound of Stacks.AlgebraicGeometry.IdealAdicFiltration; what is missing is a comparison between the support and coherence predicates used there and those defining SupportedCoherentModules, and the local finiteness of the filtration over a merely locally Noetherian scheme, the available finiteness input being quasi-compact”.

> **[Stacks, Tag 0FDT], the comparison homomorphism of K-groups.** Let `X` be a locally
> Noetherian scheme and `Z ⊂ X` a closed subscheme. The exact inclusion functor
> `Coh(𝒪_Z) ⥤ Coh_Z(X)` induces a homomorphism `K'_0(Z) = K_0(Coh(𝒪_Z)) → K_0(Coh_Z(X))` taking
> the class of a coherent `𝒪_Z`-module to the class of its direct image.

```lean
def coherentToSupportedCoherentKZeroHom :
    KZero (Stacks.SheafOfModules.CoherentModules Z.ringCatSheaf) →+
      KZero (SupportedCoherentModules i)
```

**`AlgebraicGeometry.coherentToSupportedCoherentKZeroHom_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentKGroup.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentKGroup.lean#L202). The attribute's comment: “the defining property of the comparison homomorphism”.

> **[Stacks, Tag 0FDT].** The comparison homomorphism `K_0(Coh(𝒪_Z)) → K_0(Coh_Z(X))` takes
> the class of a coherent `𝒪_Z`-module `ℱ` to the class of its direct image `i_*ℱ`.

```lean
theorem coherentToSupportedCoherentKZeroHom_mk
    (F : Stacks.SheafOfModules.CoherentModules Z.ringCatSheaf) :
    coherentToSupportedCoherentKZeroHom i (KZero.mk _ F) =
      KZero.mk _ ((coherentToSupportedCoherent i).obj F)
```

**`AlgebraicGeometry.coherentToSupportedCoherentKZeroHom_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentKGroupIso/KZeroIso.lean, line 577](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Chow/AdamsOperator/SupportedCoherentKGroupIso/KZeroIso.lean#L577). The attribute's comment: “the homomorphism K'\_0(Z) = K\_0(Coh(Z)) → K\_0(Coh\_Z(X)) induced by the exact inclusion functor is an isomorphism”.

> **[Stacks, Tag 0FDT].** Let `X` be a locally Noetherian scheme and `Z ⊂ X` a closed
> subscheme. The homomorphism `K'_0(Z) = K_0(Coh(𝒪_Z)) → K_0(Coh_Z(X))` induced by the exact
> inclusion functor `Coh(𝒪_Z) ⥤ Coh_Z(X)` is an isomorphism.

```lean
theorem coherentToSupportedCoherentKZeroHom_bijective :
    Function.Bijective (coherentToSupportedCoherentKZeroHom i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.23, Tag 0FDQ](https://stacks.math.columbia.edu/tag/0FDQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.moduleMultiplicity, AlgebraicGeometry.Space.associatedCycle, AlgebraicGeometry.Space.associatedCycle_apply_eq_geometricLength, AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_eq_cycleCoeffOfModule, AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_eq_cycleCoeffOfModule_of_eq_zero, AlgebraicGeometry.Space.associatedCycle_add_of_shortExact
statement: formalized
proof: formalized
---

# 82.6 Cycle associated to a coherent sheaf

Section 82.6 of the Stacks Project, [Tag 0EEA](https://stacks.math.columbia.edu/tag/0EEA). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EEB, a definition

[Tag 0EEB](https://stacks.math.columbia.edu/tag/0EEB) in the Stacks Project.

**`AlgebraicGeometry.Space.moduleMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CoherentSheafCycle.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CoherentSheafCycle.lean#L221). The attribute's comment: “part (1): the multiplicity of an integral closed subspace in a module, at a chosen geometric representative of its generic point and valued in ℕ∞; the reading at a point of |X| additionally needs the equivalence of Lemma 0EE1, and the finiteness asserted by Lemma 0EE4, neither of which is proved in this library”.

> **Stacks 0EEB, part (1).** The *multiplicity of an integral closed subspace `Z ⊆ X` in an
> `𝒪_X`-module `F`*: the length of `F` at the generic point `ξ` of `Z`, in the sense of Stacks 0EE2,
> read at the geometric point that `γ` assigns to `ξ`.
>
> The source defines this when `|Z|` is an irreducible component of `Supp(F)`, where by Stacks 0EE4
> it is a positive integer; the length itself is defined at every integral closed subspace, and the
> positivity on a component is
> `AlgebraicGeometry.Space.moduleMultiplicity_pos_of_isIrreducibleComponent_moduleSupport`.

```lean
def moduleMultiplicity (hX : IsAlgebraicSpace B S hS X) (F : Modules.{u, u} B S hS X hX)
    (γ : points B S hS X → GeometricPoint B S hS X)
    (Z : IntegralClosedSubspace B S hS X) : ℕ∞
```

**`AlgebraicGeometry.Space.associatedCycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CoherentSheafCycle.lean, line 677](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CoherentSheafCycle.lean#L677). The attribute's comment: “part (2): the k-cycle [F]_k of a coherent module, for a chosen geometric representative of each point; the reading at a point of |X| additionally needs the equivalence of Lemma 0EE1, which is not proved in this library”.

> **Stacks 0EEB, part (2).** In Situation 0EDT let `X/B` be good, let `F` be a coherent
> `𝒪_X`-module and assume `dim_δ(Supp(F)) ≤ k`. The *`k`-cycle associated to `F`* is
>
> `[F]_k = ∑ m_{Z, F} [Z]`,
>
> the sum over the integral closed subspaces `Z ⊆ X` whose set of points is an irreducible component
> of `Supp(F)` of δ-dimension `k`, with `m_{Z, F}` the multiplicity of part (1).
>
> As an element of `Z_k(X)` this is the coefficient family
> `AlgebraicGeometry.Space.cycleCoeffOfModule`, which assigns `m_{Z, F}` to each `Z` of δ-dimension
> `k`: off the support the multiplicity already vanishes, and
> `AlgebraicGeometry.Space.exists_irreducibleComponents_of_cycleCoeffOfModule_ne_zero`
> shows that the subspaces left with a nonzero coefficient are exactly the components of `Supp(F)`
> of δ-dimension `k`, so the family is the displayed sum. That it is a `k`-cycle at all is
> Stacks 0EE5, by `AlgebraicGeometry.Space.cycleCoeffOfModule_mem_cyclesOfDimension`.

```lean
def associatedCycle (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (F : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    [IsCoherent D.site D.base D.base_mem X hX.1 F] (k : ℤ)
    (γ : points D.site D.base D.base_mem X → GeometricPoint D.site D.base D.base_mem X)
    (hγ : ∀ x, (γ x).LiesOver x)
    (hdim : deltaDimensionClosed D sX hX (moduleSupport D.site D.base D.base_mem hX.1 F)
      (isClosed_moduleSupport D.site D.base D.base_mem hX.1 F) ≤ (k : EInt)) :
    CycleGroup D sX k
```

## Tag 0EEC, a lemma

[Tag 0EEC](https://stacks.math.columbia.edu/tag/0EEC) in the Stacks Project.

**`AlgebraicGeometry.Space.associatedCycle_apply_eq_geometricLength`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CoherentSheafCycle.lean, line 733](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CoherentSheafCycle.lean#L733). The attribute's comment: “the coefficient at a chosen geometric representative of the generic point, valued in ℤ through ENat.toNat as cycle coefficients are; the reading at a point of |X| additionally needs the equivalence of Lemma 0EE1, which is not proved in this library”.

> **Stacks 0EEC.** In Situation 0EDT let `X/B` be good, let `F` be a coherent `𝒪_X`-module with
> `dim_δ(Supp(F)) ≤ k`, and let `Z` be an integral closed subspace of `X` with `dim_δ(Z) = k` and
> generic point `ξ`. Then the coefficient of `Z` in `[F]_k` is the length of `F` at `ξ`.
>
> The generic point is `AlgebraicGeometry.Space.IntegralClosedSubspace.ambientGenericPoint`, which is
> a generic point of `|Z|` by
> `AlgebraicGeometry.Space.IntegralClosedSubspace.isGenericPoint_ambientGenericPoint`; the length is
> read at the geometric point `γ` assigns to it, and is the multiplicity of part (1) of Stacks 0EEB.
> No hypothesis asks `|Z|` to be an irreducible component of `Supp(F)`: the source reaches that case
> from the dichotomy that `|Z|` is such a component exactly when `ξ` lies in `Supp(F)`, off which the
> length vanishes, and both halves of it are already recorded here, as
> `AlgebraicGeometry.Space.exists_irreducibleComponents_of_cycleCoeffOfModule_ne_zero` and
> `AlgebraicGeometry.Space.moduleMultiplicity_eq_zero_of_notMem_moduleSupport`.

```lean
theorem associatedCycle_apply_eq_geometricLength (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (F : Modules.{u, u} D.site D.base D.base_mem X hX.1)
    [IsCoherent D.site D.base D.base_mem X hX.1 F] (k : ℤ)
    (γ : points D.site D.base D.base_mem X → GeometricPoint D.site D.base D.base_mem X)
    (hγ : ∀ x, (γ x).LiesOver x)
    (hdim : deltaDimensionClosed D sX hX (moduleSupport D.site D.base D.base_mem hX.1 F)
      (isClosed_moduleSupport D.site D.base D.base_mem hX.1 F) ≤ (k : EInt))
    {Z : IntegralClosedSubspace D.site D.base D.base_mem X}
    (hZ : deltaDimension D sX Z = k) :
    (associatedCycle D sX hX F k γ hγ hdim).1 Z =
      ((geometricLength D.site D.base D.base_mem ⟨X, hX.1⟩
        (γ (Z.ambientGenericPoint D.site D.base D.base_mem)) F).toNat : ℤ)
```

## Tag 0EED, a lemma

[Tag 0EED](https://stacks.math.columbia.edu/tag/0EED) in the Stacks Project.

**`AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_eq_cycleCoeffOfModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/StructureSheafCycle.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/StructureSheafCycle.lean#L422). The attribute's comment: “the coefficient at an integral closed subspace contained in Y, for a choice of geometric representatives above the points they are assigned to, using Lemma 0EE1 to compare the two”.

> **Stacks 0EED, at an integral closed subspace contained in `Y`.** In Situation 0EDT let
> `X/B` be good, let `Y ⊂ X` be a closed subspace with inclusion `i : Y → X`, assume
> `dim_δ(Y) ≤ k`, and let `W` be an integral closed subspace of `Y` with image `Z ⊂ X`. Then the
> coefficient of `Z` in `[Y]_k` is the coefficient of `Z` in `[i_*𝒪_Y]_k`.
>
> The chosen geometric representatives `γY` and `γX` are each assumed to lie over the point they
> are assigned to, which `AlgebraicGeometry.Space.exists_compatible_geometricRepresentative` shows
> is possible; the content is then Stacks 0EE3, by way of
> `AlgebraicGeometry.Space.geometricLength_closedSubspacePushforwardStructureSheaf`, together with
> Stacks 0EE1 to move from `γX` at the image of the generic point of `W` to the geometric point
> `i(γY(ξ_W))` that the comparison with `𝒪_Y` is stated at.

```lean
theorem cycleCoeffOfClosedSubspace_eq_cycleCoeffOfModule (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (Y : Subfunctor X) (hY : IsClosedSubspace D.site D.base D.base_mem Y) (k : ℤ)
    (_hdim : deltaDimensionSubspace D sX hX Y hY ≤ (k : EInt))
    (γY : points D.site D.base D.base_mem Y.toFunctor →
      GeometricPoint D.site D.base D.base_mem Y.toFunctor)
    (γX : points D.site D.base D.base_mem X → GeometricPoint D.site D.base D.base_mem X)
    (hγY : ∀ y, (γY y).LiesOver y) (hγX : ∀ x, (γX x).LiesOver x)
    (W : IntegralClosedSubspace D.site D.base D.base_mem Y.toFunctor) :
    cycleCoeffOfClosedSubspace D sX hX Y hY k γY
        (closedSubspaceComponentImage D sX hX Y hY W) =
      cycleCoeffOfModule D sX hX
        (closedSubspacePushforwardStructureSheaf D.site D.base D.base_mem hX.1 Y hY) k γX
        (closedSubspaceComponentImage D sX hX Y hY W)
```

**`AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_eq_cycleCoeffOfModule_of_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/StructureSheafCycle.lean, line 470](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/StructureSheafCycle.lean#L470). The attribute's comment: “the equality of the two k-cycles, for a choice of geometric representatives above the points they are assigned to”.

> **Stacks 0EED.** In Situation 0EDT let `X/B` be good, let `Y ⊂ X` be a closed subspace with
> inclusion `i : Y → X`, and assume `dim_δ(Y) ≤ k`. Then `[Y]_k = [i_*𝒪_Y]_k`, as an equality of
> coefficient families on the integral closed subspaces of `X`.
>
> For an integral closed subspace `Z` with image contained in `|Y|` this is
> `AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_eq_cycleCoeffOfModule`. Otherwise both sides
> vanish: the left by `AlgebraicGeometry.Space.cycleCoeffOfClosedSubspace_eq_zero`, and the right
> because `i_*𝒪_Y` is annihilated by the ideal cutting out `Y`
> (`AlgebraicGeometry.Space.annihilatedByKerIdeal_closedSubspacePushforwardStructureSheaf`), so its
> geometric stalk is trivial at any geometric point over a point of `|X|` outside the image of
> `|Y|`
> (`AlgebraicGeometry.Space.subsingleton_geometricModuleStalk_of_annihilatedByKerIdeal_of_notMem`);
> and the generic point of `Z` is such a point exactly when no integral closed subspace of `Y` has
> image `Z`, since `Y` is a decent space
> (`AlgebraicGeometry.Space.isDecentSpace_of_relativelyRepresentable`) and every integral closed
> subspace of `X` contained in the image of `|Y|` is itself such an image
> (`AlgebraicGeometry.Space.IntegralClosedSubspace.exists_pushforward_eq`). This is the support
> bound of Lemma 07U0, proved rather than taken as a hypothesis.

```lean
theorem cycleCoeffOfClosedSubspace_eq_cycleCoeffOfModule_of_eq_zero (sX : X ⟶ D.space)
    (hX : D.IsGood sX) (Y : Subfunctor X)
    (hY : IsClosedSubspace D.site D.base D.base_mem Y) (k : ℤ)
    (hdim : deltaDimensionSubspace D sX hX Y hY ≤ (k : EInt))
    (γY : points D.site D.base D.base_mem Y.toFunctor →
      GeometricPoint D.site D.base D.base_mem Y.toFunctor)
    (γX : points D.site D.base D.base_mem X → GeometricPoint D.site D.base D.base_mem X)
    (hγY : ∀ y, (γY y).LiesOver y) (hγX : ∀ x, (γX x).LiesOver x) :
    cycleCoeffOfClosedSubspace D sX hX Y hY k γY =
      cycleCoeffOfModule D sX hX
        (closedSubspacePushforwardStructureSheaf D.site D.base D.base_mem hX.1 Y hY) k γX
```

## Tag 0EEE, a lemma

[Tag 0EEE](https://stacks.math.columbia.edu/tag/0EEE) in the Stacks Project.

**`AlgebraicGeometry.Space.associatedCycle_add_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/CoherentSheafCycle.lean, line 807](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/CoherentSheafCycle.lean#L807).

> **Stacks 0EEE.** In Situation 0EDT let `X/B` be good and let `0 → F → G → H → 0` be a short
> exact sequence of coherent `𝒪_X`-modules whose three supports have δ-dimension at most `k`. Then
>
> `[G]_k = [F]_k + [H]_k`.
>
> Coefficientwise this is additivity of the multiplicity,
> `AlgebraicGeometry.Space.moduleMultiplicity_add_of_shortExact`, hence additivity of length in a
> short exact sequence, Stacks 00IV, at the generic point of each integral closed subspace of
> δ-dimension `k`; at the subspaces of other δ-dimension all three coefficients vanish.
>
> Cycle coefficients are integers, reached from the `ℕ∞`-valued multiplicity by `ENat.toNat`, which
> is additive only on finite values, so the proof also needs the multiplicities of the middle term to
> be finite at the subspaces of δ-dimension `k`. Off its support the multiplicity is zero. On its
> support, the generic point of such a subspace attains the δ-dimension bound, so it is a generic
> point of an irreducible component of the support by Stacks 0EE6
> (`AlgebraicGeometry.Space.isGenericPoint_of_deltaDimensionClosed_le`), and the length there is
> finite by Stacks 0EE4
> (`AlgebraicGeometry.Space.geometricLength_ne_top_and_pos_of_isGenericPoint_supportOfSheaf`).
>
> The cycles are read at the geometric points `γ` chooses above the points of `|X|`; by Stacks 0EE1,
> `AlgebraicGeometry.Space.geometricLength_eq_of_image_eq`, the lengths, hence the cycles, do not
> depend on that choice.

```lean
theorem associatedCycle_add_of_shortExact (sX : X ⟶ D.space) (hX : D.IsGood sX)
    (σ : ShortComplex (Modules.{u, u} D.site D.base D.base_mem X hX.1)) (hσ : σ.ShortExact)
    [IsCoherent D.site D.base D.base_mem X hX.1 σ.X₁]
    [IsCoherent D.site D.base D.base_mem X hX.1 σ.X₂]
    [IsCoherent D.site D.base D.base_mem X hX.1 σ.X₃] (k : ℤ)
    (γ : points D.site D.base D.base_mem X → GeometricPoint D.site D.base D.base_mem X)
    (hγ : ∀ x, (γ x).LiesOver x)
    (hdim₁ : deltaDimensionClosed D sX hX
      (moduleSupport D.site D.base D.base_mem hX.1 σ.X₁)
      (isClosed_moduleSupport D.site D.base D.base_mem hX.1 σ.X₁) ≤ (k : EInt))
    (hdim₂ : deltaDimensionClosed D sX hX
      (moduleSupport D.site D.base D.base_mem hX.1 σ.X₂)
      (isClosed_moduleSupport D.site D.base D.base_mem hX.1 σ.X₂) ≤ (k : EInt))
    (hdim₃ : deltaDimensionClosed D sX hX
      (moduleSupport D.site D.base D.base_mem hX.1 σ.X₃)
      (isClosed_moduleSupport D.site D.base D.base_mem hX.1 σ.X₃) ≤ (k : EInt)) :
    associatedCycle D sX hX σ.X₂ k γ hγ hdim₂ =
      associatedCycle D sX hX σ.X₁ k γ hγ hdim₁ +
        associatedCycle D sX hX σ.X₃ k γ hγ hdim₃
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 82.6, Tag 0EEA](https://stacks.math.columbia.edu/tag/0EEA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

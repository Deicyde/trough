---
declaration: section
origin: cited
lean: Stacks.Chow.relativeCycleWeight, Stacks.Chow.isWeighting_relativeCycleWeight, Stacks.Chow.exists_relativeCycle_nsmul_eq_relativeCycleWeight, Stacks.Chow.exists_relativeCycle_primePow_nsmul_eq_relativeCycleWeight
statement: formalized
proof: formalized
---

# 62.8 Weightings and relative zero cycles

Section 62.8 of the Stacks Project. 1 tag here is carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H5P, a lemma

[Tag 0H5P](https://stacks.math.columbia.edu/tag/0H5P) in the Stacks Project.

**`Stacks.Chow.relativeCycleWeight`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Weighting.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/Weighting.lean#L59). The attribute's comment: “the construction of w\_α preceding the lemma; none of the lemma's three claims”.

> The function `w_α : X → ℤ` attached to a family `α` of `0`-cycles on the fibres of
> `f : X ⟶ S`: the coefficient of `α` at a point `x`, taken on the scheme-theoretic fibre through
> `x`, times the inseparable degree `[κ(x) : κ(f x)]_i`.

```lean
def relativeCycleWeight {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (α : FamilyOfCycles f 0) : X → ℤ
```

**`Stacks.Chow.isWeighting_relativeCycleWeight`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/WeightingEquivalence.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/WeightingEquivalence.lean#L58). The attribute's comment: “clause (1): the map attached to a relative zero-cycle is a weighting”.

> **Stacks Project, Tag 0H5P**, clause (1). Let `S` be a locally Noetherian scheme and let
> `f : X ⟶ S` be a locally quasi-finite morphism of schemes. For `α ∈ z(X/S, 0)` the map
> `w_α : X → ℤ` is a weighting of `f`.

```lean
theorem isWeighting_relativeCycleWeight (α : relativeCycles f 0) :
    IsWeighting f (relativeCycleWeight f α.1)
```

**`Stacks.Chow.exists_relativeCycle_nsmul_eq_relativeCycleWeight`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/WeightingEquivalence.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/WeightingEquivalence.lean#L81). The attribute's comment: “clause (2): every weighting is a positive integer multiple of one attached to a relative zero-cycle, for a quasi-compact source”.

> **Stacks Project, Tag 0H5P**, clause (2). Let `S` be a locally Noetherian scheme, let
> `f : X ⟶ S` be a locally quasi-finite morphism of schemes and let `X` be quasi-compact. Given a
> weighting `w : X → ℤ` of `f` there is an integer `n > 0` with `n·w = w_α` for some
> `α ∈ z(X/S, 0)`.

```lean
theorem exists_relativeCycle_nsmul_eq_relativeCycleWeight [CompactSpace X] (w : X → ℤ)
    (hw : IsWeighting f w) :
    ∃ (n : ℕ) (α : relativeCycles f 0), 0 < n ∧
      ∀ x : X, (n : ℤ) * w x = relativeCycleWeight f α.1 x
```

**`Stacks.Chow.exists_relativeCycle_primePow_nsmul_eq_relativeCycleWeight`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/WeightingEquivalence.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/WeightingEquivalence.lean#L94). The attribute's comment: “clause (3): over a scheme of characteristic p the multiple may be taken to be a power of p”.

> **Stacks Project, Tag 0H5P**, clause (3). In the situation of clause (2), if `S` is a scheme
> over `𝔽_p` for a prime `p`, then the integer `n` may be chosen to be a power of `p`.

```lean
theorem exists_relativeCycle_primePow_nsmul_eq_relativeCycleWeight [CompactSpace X] (p : ℕ)
    [Fact p.Prime] (σ : S ⟶ Spec (CommRingCat.of (ULift.{u} (ZMod p)))) (w : X → ℤ)
    (hw : IsWeighting f w) :
    ∃ (e : ℕ) (α : relativeCycles f 0), 0 < p ^ e ∧
      ∀ x : X, ((p ^ e : ℕ) : ℤ) * w x = relativeCycleWeight f α.1 x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Chapter 62, Tag 0H4B](https://stacks.math.columbia.edu/tag/0H4B)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

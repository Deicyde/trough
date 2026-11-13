---
declaration: section
origin: cited
lean: AlgebraicGeometry.unramified_iff_injective_hom_restriction
statement: formalized
proof: formalized
---

# 41.5 The functorial characterization of unramified morphisms

Section 41.5 of the Stacks Project, [Tag 024Q](https://stacks.math.columbia.edu/tag/024Q). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 024R, a theorem

[Tag 024R](https://stacks.math.columbia.edu/tag/024R) in the Stacks Project.

**`AlgebraicGeometry.unramified_iff_injective_hom_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FunctorialUnramified.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/FunctorialUnramified.lean#L73).

> **Stacks 024R.** Let `f : X ⟶ S` be a morphism of schemes with `S` locally Noetherian and `f`
> locally of finite type. Then `f` is unramified if and only if it is formally unramified in the
> functorial sense: for every affine `S`-scheme `T` and every subscheme `T₀` of `T` defined by a
> square-zero ideal, the natural map `Hom_S(T, X) → Hom_S(T₀, X)` is injective.

```lean
public theorem unramified_iff_injective_hom_restriction {X S : Scheme.{u}}
    [IsLocallyNoetherian S] (f : X ⟶ S) [LocallyOfFiniteType f] :
    Unramified f ↔
      ∀ (T T₀ : Over S) (_ : IsAffine T.left) (i : T₀ ⟶ T),
        Stacks.Thickenings.IsFirstOrderThickening i.left →
          Function.Injective fun g : T ⟶ Over.mk f => i ≫ g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.5, Tag 024Q](https://stacks.math.columbia.edu/tag/024Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

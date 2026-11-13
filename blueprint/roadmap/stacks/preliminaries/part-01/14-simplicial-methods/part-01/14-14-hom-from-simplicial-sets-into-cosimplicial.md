---
declaration: section
origin: cited
lean: CategoryTheory.CosimplicialObject.power
statement: formalized
proof: formalized
---

# 14.14 Hom from simplicial sets into cosimplicial objects

Section 14.14 of the Stacks Project, [Tag 07K9](https://stacks.math.columbia.edu/tag/07K9). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 019V, a definition

[Tag 019V](https://stacks.math.columbia.edu/tag/019V) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.power`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Power.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Power.lean#L413). The attribute's comment: “the finiteness and nonemptiness of the `U_n` are replaced by the existence of the products they index, which is all they are used for”.

> **Stacks 019V.** `Hom(U, V)`, the cosimplicial object of maps from a simplicial set `U` into a
> cosimplicial object `V` of `C`. Its degree `n` part is the power `Hom(U, V)_n = ∏_{u ∈ U_n} V_n`,
> the object of `C` whose `X`-valued points are the maps `U_n → Mor_C(X, V_n)`, and for
> `φ : [m] ⟶ [n]` in `Δ` the structure map `Hom(U, V)_m ⟶ Hom(U, V)_n` is the morphism whose `u`-th
> component, for `u ∈ U_n`, is the projection to the `U(φ)(u)`-th factor followed by `V(φ)`; on
> `X`-valued points it is `f ↦ V(φ) ∘ f ∘ U(φ)`.

```lean
noncomputable def power (V : CosimplicialObject C) (U : SSet.{w})
    [∀ n : SimplexCategory, HasProduct fun _ : U.obj (op n) => V.obj n] :
    CosimplicialObject C
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.14, Tag 07K9](https://stacks.math.columbia.edu/tag/07K9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

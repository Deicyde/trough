---
declaration: section
origin: cited
lean: Stacks.NodalEtaleLocalStructure.nonempty_standardNodalDiagram_of_isAtWorstNodal
statement: formalized
proof: formalized
---

# 53.21 Étale local structure of nodal families

Section 53.21 of the Stacks Project, [Tag 0H8M](https://stacks.math.columbia.edu/tag/0H8M). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CBY, a lemma

[Tag 0CBY](https://stacks.math.columbia.edu/tag/0CBY) in the Stacks Project.

**`Stacks.NodalEtaleLocalStructure.nonempty_standardNodalDiagram_of_isAtWorstNodal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Curves/NodalEtaleLocalStructureAssembly.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/NodalEtaleLocalStructureAssembly.lean#L352). The attribute's comment: “the whole statement. The diagram is the structure `Stacks.NodalEtaleLocalStructure.StandardNodalDiagram`, whose fields are the tag's four morphisms with the three etaleness assertions, the commutativity of the left and the middle square, the cartesianness of the right-hand square over the standard nodal family `Spec Z[u,v,a]/(uv-a) -> Spec Z[a]`, and the point of `U` over `x`. The singular point of the fibre is spelled as the failure of smoothness of the fibre `X_s` over `kappa(s)` at `x`; the equivalent spelling as a point of the relative singular subscheme `Sing(f)`, which is the one the source's own first step carries, is `nonempty_standardNodalDiagram_of_mem_relativeSingular`, and the two agree by `mem_relativeSingular_iff_not_smoothAt_fiber` ([Stacks, Tags 0C3I and 0C3K])”.

> **Stacks Project, Tag 0CBY.** Let `f : X ⟶ S` be at-worst-nodal of relative dimension one
> and let `x` be a point of `X` at which the fibre `X_s` through it is *singular*. Then there is a
> commutative diagram
> ```
> X ←—— U ——→ W ——→ Spec ℤ[u, v, a]/(uv - a)
> ↓     ↓     ↓                ↓
> S ←———————— V ——————————→ Spec ℤ[a]
> ```
> in which `U ⟶ X`, `V ⟶ S` and `U ⟶ W` are étale, the right-hand square is cartesian, and some
> point of `U` maps to `x`. The diagram is packaged as
> `Stacks.NodalEtaleLocalStructure.StandardNodalDiagram`; its right-hand vertical arrow is
> `Stacks.NodalEtaleLocalStructure.standardNodalFamily`, the spectrum of the parameter map
> `Stacks.Curves.nodalParam : ℤ[a] ⟶ ℤ[u, v, a]/(uv - a)`, where the ring
> `Stacks.Curves.nodalQuotient` is `ℤ[u, v, a]` modulo the relation `Stacks.Curves.nodalRelation`,
> namely `uv - a`.
>
> The whole content is `nonempty_standardNodalDiagram_of_mem_relativeSingular`, which is the same
> statement with the singular point read on the relative singular subscheme `Sing(f)`; the two
> spellings agree by `mem_relativeSingular_iff_not_smoothAt_fiber`, which is [Stacks, Tag 0C3K]
> on a fibre.

```lean
public theorem nonempty_standardNodalDiagram_of_isAtWorstNodal {X S : Scheme.{u}} (f : X ⟶ S)
    (hf : IsAtWorstNodalOfRelativeDimensionOne f) {x : X}
    (hxsing : ¬ InfinitesimalLifting.SmoothAt (f.fiberToSpecResidueField (f x))
      (f.asFiber x)) :
    Nonempty (StandardNodalDiagram f x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 53.21, Tag 0H8M](https://stacks.math.columbia.edu/tag/0H8M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

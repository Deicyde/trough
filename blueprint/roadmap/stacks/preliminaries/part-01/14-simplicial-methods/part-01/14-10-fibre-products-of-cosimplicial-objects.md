---
declaration: section
origin: cited
lean: CategoryTheory.Limits.pointwisePullback, CategoryTheory.CosimplicialObject.isBijective_canonicalMap_pointwisePullback
statement: formalized
proof: formalized
---

# 14.10 Fibre products of cosimplicial objects

Section 14.10 of the Stacks Project, [Tag 0171](https://stacks.math.columbia.edu/tag/0171). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0172, a definition

[Tag 0172](https://stacks.math.columbia.edu/tag/0172) in the Stacks Project.

**`CategoryTheory.Limits.pointwisePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean#L320). The attribute's comment: “stated for an arbitrary index category `D`: the fibre product of cosimplicial objects is the case `D = SimplexCategory`, and that of simplicial objects, Tag 016T, the case `D = SimplexCategoryᵒᵖ`”.

> **Stacks 0172.** The fibre product of cosimplicial objects, as a pointwise pullback in a
> functor category. Given a cospan `f : F ⟶ H`, `g : G ⟶ H` of morphisms of functors `D ⥤ C` all
> of whose pointwise pullbacks `F d ×_{H d} G d` exist, `pointwisePullback f g` is the functor
> `d ↦ F d ×_{H d} G d`, a morphism `φ : d ⟶ d'` acting by the morphism `F φ ×_{H φ} G φ` that
> `F φ`, `G φ` and `H φ` induce on the pullbacks. For cosimplicial objects `U`, `V`, `W` of `C`
> and `a : V ⟶ U`, `b : W ⟶ U`, so for `D = Δ`, this is the fibre product `V ×_U W`, with
> `(V ×_U W)_n = V_n ×_{U_n} W_n` and `(V ×_U W)(φ) = V(φ) ×_{U(φ)} W(φ)`; for simplicial objects,
> so for `D = Δᵒᵖ`, it is the fibre product of [Stacks, Tag 016T].

```lean
noncomputable def pointwisePullback (f : F ⟶ H) (g : G ⟶ H)
    [∀ d, HasPullback (f.app d) (g.app d)] : D ⥤ C
```

## Tag 0173, a lemma

[Tag 0173](https://stacks.math.columbia.edu/tag/0173) in the Stacks Project.

**`CategoryTheory.CosimplicialObject.isBijective_canonicalMap_pointwisePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/CosimplicialFibreProduct.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/CosimplicialFibreProduct.lean#L52). The attribute's comment: “the fibre product of sets `Mor(T, V) ×_{Mor(T, U)} Mor(T, W)` is `Types.PullbackObj`, the set of pairs `(f, g)` with `f ≫ a = g ≫ b`, and the identification is composition with the degreewise projections of `V ×_U W`”.

> **Stacks 0173**.
> Let `C` be a category, `U V W` cosimplicial objects of `C`, and `a : V ⟶ U`, `b : W ⟶ U`
> morphisms of cosimplicial objects such that every fibre product `V_n ×_{U_n} W_n` exists in `C`,
> and let `V ×_U W = Limits.pointwisePullback a b` be the degreewise fibre product of Tag 0172,
> with its degreewise projections `p`, `q`. Then for every cosimplicial object `T` the map
> `Mor(T, V ×_U W) → Mor(T, V) ×_{Mor(T, U)} Mor(T, W)`, `f ↦ (f ≫ p, f ≫ q)`, is a bijection.

```lean
theorem isBijective_canonicalMap_pointwisePullback
    {C : Type u} [Category.{v} C] {U V W : CosimplicialObject C}
    (a : V ⟶ U) (b : W ⟶ U) [∀ n, HasPullback (a.app n) (b.app n)]
    (T : CosimplicialObject C) :
    Function.Bijective
      (PullbackCone.canonicalMap a b (isPullback_pointwisePullback a b).cone (T := T))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.10, Tag 0171](https://stacks.math.columbia.edu/tag/0171)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

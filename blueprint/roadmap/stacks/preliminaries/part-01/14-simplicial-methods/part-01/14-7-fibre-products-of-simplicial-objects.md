---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialObject.fibreProduct, CategoryTheory.SimplicialObject.fibreProduct.isBijective_canonicalMap
statement: formalized
proof: formalized
---

# 14.7 Fibre products of simplicial objects

Section 14.7 of the Stacks Project, [Tag 016S](https://stacks.math.columbia.edu/tag/016S). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 016T, a definition

[Tag 016T](https://stacks.math.columbia.edu/tag/016T) in the Stacks Project.

**`CategoryTheory.SimplicialObject.fibreProduct`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean#L81). The attribute's comment: “the case `D = SimplexCategoryᵒᵖ` of `CategoryTheory.Limits.pointwisePullback`, Tag 0172, which is stated for an arbitrary index category `D`”.

> **Stacks 016T.** The fibre product `V ×_U W` of two simplicial objects `V`, `W` of a category
> `C` over a third one `U`, along morphisms `a : V ⟶ U` and `b : W ⟶ U`, when the fibre product
> `V_n ×_{U_n} W_n` exists in `C` in every degree: the simplicial object with
> `(V ×_U W)_n = V_n ×_{U_n} W_n` on which a morphism `φ : ⦋m⦌ ⟶ ⦋n⦌` of `Δ` acts by the morphism
> that `V φ`, `W φ` and `U φ` induce on the pullbacks, so that `d^n_i = (d^n_i, d^n_i)` and
> `s^n_i = (s^n_i, s^n_i)`.

```lean
noncomputable abbrev fibreProduct (a : V ⟶ U) (b : W ⟶ U)
    [∀ n, Limits.HasPullback (a.app n) (b.app n)] : SimplicialObject C
```

## Tag 016U, a lemma

[Tag 016U](https://stacks.math.columbia.edu/tag/016U) in the Stacks Project.

**`CategoryTheory.SimplicialObject.fibreProduct.isBijective_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean#L290). The attribute's comment: “the fibre product of sets is `Types.PullbackObj`, and the identification is the map `h ↦ (h ≫ p, h ≫ q)` given by the degreewise projections `fibreProduct.fst`, `fibreProduct.snd`; the limit structure itself is `fibreProduct.isLimit`”.

> **Stacks 016U.** Let `C` be a category, let `U V W` be simplicial objects of `C` and let
> `a : V ⟶ U`, `b : W ⟶ U` be morphisms such that the fibre products `V_n ×_{U_n} W_n` exist in `C`,
> so that the degreewise fibre product `V ×_U W = fibreProduct a b` of Tag 016T exists. For every
> simplicial object `T` of `C`, the map `h ↦ (h ≫ p, h ≫ q)`, with `p`, `q` the degreewise
> projections, is a bijection
> `Mor(T, V ×_U W) → Mor(T, V) ×_{Mor(T, U)} Mor(T, W)`.

```lean
theorem isBijective_canonicalMap (T : SimplicialObject C) :
    Function.Bijective (PullbackCone.canonicalMap a b (cone a b) (T := T))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.7, Tag 016S](https://stacks.math.columbia.edu/tag/016S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

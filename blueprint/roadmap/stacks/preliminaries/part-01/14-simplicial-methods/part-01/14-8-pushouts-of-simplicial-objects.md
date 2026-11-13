---
declaration: section
origin: cited
lean: CategoryTheory.Limits.pointwisePushout, CategoryTheory.IsPushout.existsUnique_desc, CategoryTheory.Square.isPushout_iff_op_map_yoneda_isPullback, CategoryTheory.IsPushout.of_forall_isPushout_app
statement: formalized
proof: formalized
---

# 14.8 Pushouts of simplicial objects

Section 14.8 of the Stacks Project, [Tag 016V](https://stacks.math.columbia.edu/tag/016V). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 016W, a definition

[Tag 016W](https://stacks.math.columbia.edu/tag/016W) in the Stacks Project.

**`CategoryTheory.Limits.pointwisePushout`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/FunctorCategory/Pointwise.lean#L410). The attribute's comment: “stated for an arbitrary index category `D`: the pushout of simplicial objects is the case `D = SimplexCategoryᵒᵖ`, and that of cosimplicial objects the case `D = SimplexCategory`”.

> **Stacks 016W.** The pushout of simplicial objects, as a pointwise pushout in a functor
> category. Given a span `f : F ⟶ G`, `g : F ⟶ H` of morphisms of functors `D ⥤ C` all of whose
> pointwise pushouts `G d ⨿_{F d} H d` exist, `pointwisePushout f g` is the functor
> `d ↦ G d ⨿_{F d} H d`, a morphism `φ : d ⟶ d'` acting by the morphism `G φ ⨿_{F φ} H φ` that
> `G φ`, `H φ` and `F φ` induce on the pushouts. For simplicial objects `U`, `V`, `W` of `C` and
> `a : U ⟶ V`, `b : U ⟶ W`, so for `D = Δᵒᵖ`, this is the pushout `V ⨿_U W`, with
> `(V ⨿_U W)_n = V_n ⨿_{U_n} W_n`, `d^n_i = (d^n_i, d^n_i)` and `s^n_i = (s^n_i, s^n_i)`; for
> cosimplicial objects, so for `D = Δ`, it is their pushout. It is the dual of
> `pointwisePullback`.

```lean
noncomputable def pointwisePushout (f : F ⟶ G) (g : F ⟶ H)
    [∀ d, HasPushout (f.app d) (g.app d)] : D ⥤ C
```

## Tag 016X, a lemma

[Tag 016X](https://stacks.math.columbia.edu/tag/016X) in the Stacks Project.

**`CategoryTheory.IsPushout.existsUnique_desc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean, line 364](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean#L364). The attribute's comment: “for a pushout square in an arbitrary category rather than for the pushout `V ∐_U W` of simplicial objects, and elementwise: an element of the fibre product `Mor(V, T) ×_{Mor(U, T)} Mor(W, T)` is a pair `(p, q)` with `a ≫ p = b ≫ q`, and bijectivity of `φ ↦ (f ≫ φ, g ≫ φ)` is existence and uniqueness of `φ`”.

> **Stacks 016X** (for a pushout square in an arbitrary category, elementwise).
> For a pushout square
>
> ```
> U --a--> V
> |        |
> b        f
> v        v
> W --g--> P
> ```
>
> in a category `C` and an object `T` of `C`, composition with `f` and with `g` identifies
> `Mor(P, T)` with the fibre product `Mor(V, T) ×_{Mor(U, T)} Mor(W, T)`: a pair `p : V ⟶ T`,
> `q : W ⟶ T` with `a ≫ p = b ≫ q` extends to `P` in exactly one way.

```lean
public theorem IsPushout.existsUnique_desc {C : Type u} [Category.{v} C] {U V W P : C}
    {a : U ⟶ V} {b : U ⟶ W} {f : V ⟶ P} {g : W ⟶ P} (h : IsPushout a b f g) {T : C}
    (p : V ⟶ T) (q : W ⟶ T) (w : a ≫ p = b ≫ q) :
    ∃! φ : P ⟶ T, f ≫ φ = p ∧ g ≫ φ = q
```

Declarations registered for the tag:

- [`CategoryTheory.Square.isPushout_iff_op_map_yoneda_isPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Square.isPushout_iff_op_map_yoneda_isPullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean#L373) (StacksFrontier): “the same identification of hom-sets, bundled and in both directions: a square is a pushout square if and only if for every `T` the image of the opposite square under `Mor(-, T)` is a pullback square of types, whose four maps are composition with `f`, `g`, `a`, `b` by `rfl`, so at each `T` it is the source's `Mor(P, T) = Mor(V, T) ×_{Mor(U, T)} Mor(W, T)`”. References: EGA I (3.4.3), “more general”.
- [`CategoryTheory.IsPushout.of_forall_isPushout_app`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsPushout.of_forall_isPushout_app#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean, line 379](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/SimplicialObject/Limits.lean#L379) (StacksFrontier): “with the source's hypothesis that `V ∐_U W` exists: the degreewise pushout of Tag 016W, whose squares `V_n ∐_{U_n} W_n` are pushout squares, is a pushout in the category `Δᵒᵖ ⥤ C` of simplicial objects, to which the statements above then apply”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.8, Tag 016V](https://stacks.math.columbia.edu/tag/016V)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

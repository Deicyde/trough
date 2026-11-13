---
declaration: section
origin: cited
lean: Function.Exact.exists_split_of_field, Function.Exact.split_of_field, Module.projective_lifting_property
statement: formalized
proof: formalized
---

# 9.4 Vector spaces

Section 9.4 of the Stacks Project, [Tag 09FM](https://stacks.math.columbia.edu/tag/09FM). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09FP, a lemma

[Tag 09FP](https://stacks.math.columbia.edu/tag/09FP) in the Stacks Project.

**`Function.Exact.exists_split_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Basis/VectorSpace.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Basis/VectorSpace.lean#L32). The attribute's comment: “Splitting of an exact sequence `M → N → P` at its middle term; the short exact case is `Function.Exact.split_of_field`.”.

> Every exact sequence of modules over a field splits: an exact sequence `M → N → P` of
> `k`-modules splits at `N`, i.e. there are `l : N → M` and `s : P → N` with `f ∘ l ∘ f = f`,
> `g ∘ s ∘ g = g` and `f ∘ l + s ∘ g = id`. Applied at every term, this splits an exact
> sequence of any length; for short exact sequences see `Function.Exact.split_of_field`.

```lean
theorem Function.Exact.exists_split_of_field (h : Function.Exact f g) :
    ∃ (l : N →ₗ[k] M) (s : P →ₗ[k] N),
      f ∘ₗ l ∘ₗ f = f ∧ g ∘ₗ s ∘ₗ g = g ∧ f ∘ₗ l + s ∘ₗ g = LinearMap.id
```

**`Function.Exact.split_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Basis/VectorSpace.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Basis/VectorSpace.lean#L67). The attribute's comment: “Short exact case; the case of an arbitrary exact sequence is `Function.Exact.exists_split_of_field`.”.

> Every short exact sequence `0 → M → N → P → 0` of modules over a field splits: `f` has
> a retraction, `g` has a section, and `N ≅ M × P` compatibly with `f` and `g`.

```lean
theorem Function.Exact.split_of_field (h : Function.Exact f g) (hf : Function.Injective f)
    (hg : Function.Surjective g) :
    (∃ l : N →ₗ[k] M, l ∘ₗ f = LinearMap.id) ∧ (∃ s : P →ₗ[k] N, g ∘ₗ s = LinearMap.id) ∧
      ∃ e : N ≃ₗ[k] M × P, f = e.symm ∘ₗ LinearMap.inl k M P ∧ g = LinearMap.snd k M P ∘ₗ e
```

Declarations registered for the tag:

- [`Module.projective_lifting_property`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.projective_lifting_property#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Module/Projective.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Module/Projective.lean#L10) (StacksCore). References: SGA 5 XV (3.Lemma3), “more general”; SGA 6 I (1.3), “more general”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.4, Tag 09FM](https://stacks.math.columbia.edu/tag/09FM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

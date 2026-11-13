---
declaration: section
origin: cited
lean: AlgebraicTopology.normalizedMooreComplex_faithful, CategoryTheory.Equivalence.exists_of_faithful_of_essSurj, CategoryTheory.Abelian.DoldKan.equivalence, CategoryTheory.Abelian.DoldKan.equivalence_functor
statement: formalized
proof: formalized
---

# 14.24 Dold-Kan

Section 14.24 of the Stacks Project, [Tag 019D](https://stacks.math.columbia.edu/tag/019D). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 019E, a lemma

[Tag 019E](https://stacks.math.columbia.edu/tag/019E) in the Stacks Project.

**`AlgebraicTopology.normalizedMooreComplex_faithful`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/DoldKan/Equivalence.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/DoldKan/Equivalence.lean#L50).

> **Stacks 019E**.
> The normalized complex functor `N : Simp(A) ⥤ Ch_{≥0}(A)` of an abelian category `A`, sending a
> simplicial object `U` to the complex of normalized chains `N(U)_m = ⋂_i Ker(d^m_i)`, is faithful.
> Consequently it reflects monomorphisms, epimorphisms and isomorphisms.

```lean
public instance normalizedMooreComplex_faithful :
    (normalizedMooreComplex A).Faithful
```

## Tag 019F, a lemma

[Tag 019F](https://stacks.math.columbia.edu/tag/019F) in the Stacks Project.

**`CategoryTheory.Equivalence.exists_of_faithful_of_essSurj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicTopology/DoldKan/Equivalence.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicTopology/DoldKan/Equivalence.lean#L134).

> **Stacks 019F**.
> For abelian categories `A` and `B` and exact functors `N : A ⥤ B`, `S : B ⥤ A` with a natural
> isomorphism `g : S ⋙ N ≅ 𝟭 B`, `N` faithful and `S` essentially surjective, `N` and `S` are
> quasi-inverse equivalences of categories: there is an equivalence `A ≌ B` whose functor is `N` and
> whose inverse functor is `S`.

```lean
theorem Equivalence.exists_of_faithful_of_essSurj
    {A B : Type*} [Category A] [Category B] [Abelian A] [Abelian B]
    (N : A ⥤ B) (S : B ⥤ A)
    (g : S ⋙ N ≅ 𝟭 B)
    (hN_faithful : N.Faithful)
    (hS_essSurj : S.EssSurj) :
    ∃ e : A ≌ B, e.functor = N ∧ e.inverse = S
```

## Tag 019G, a theorem

[Tag 019G](https://stacks.math.columbia.edu/tag/019G) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.DoldKan.equivalence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.DoldKan.equivalence#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L81) (StacksFrontier): “the equivalence Simp(A) ≌ Ch\_\{≥0}(A)”.
- [`CategoryTheory.Abelian.DoldKan.equivalence_functor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.DoldKan.equivalence_functor#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch14.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch14.lean#L83) (StacksFrontier): “the functor of the equivalence is N”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 14.24, Tag 019D](https://stacks.math.columbia.edu/tag/019D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

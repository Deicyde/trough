---
declaration: section
origin: cited
lean: CategoryTheory.Projective, projective_tfae, CategoryTheory.Projective.instSigmaObj, CategoryTheory.EnoughProjectives, HasFunctorialProjectiveSurjections
statement: formalized
proof: formalized
---

# 12.28 Projectives

Section 12.28 of the Stacks Project, [Tag 013A](https://stacks.math.columbia.edu/tag/013A). 5 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 013B, a definition

[Tag 013B](https://stacks.math.columbia.edu/tag/013B) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Projective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Projective#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 23](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L23) (StacksFrontier). References: SGA 4 IV (2.6), “partial”; SGA 4 IV (7.6); SGA 6 I (1.2).

## Tag 013C, a lemma

[Tag 013C](https://stacks.math.columbia.edu/tag/013C) in the Stacks Project.

**`projective_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Projective/Characterization.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Projective/Characterization.lean#L56). The attribute's comment: “the four conditions as `List.TFAE`; (4) uses Mathlib's `Abelian.Ext P A 1` for the Yoneda `Ext`, via `CategoryTheory.projective_iff_subsingleton_ext_one`”.

> **Stacks 013C.** Let `𝒜` be an abelian category and `P` an object of `𝒜`. The following
> are equivalent:
> 1. `P` is projective;
> 2. the functor `B ↦ Hom(P, B)` is exact (it sends short exact sequences of `𝒜` to short exact
>    sequences of abelian groups, `HomFunctorExact`);
> 3. every short exact sequence `0 → A → B → P → 0` splits (`EverySESEndingInPSplits`);
> 4. `Ext(P, A) = 0` for every `A`, stated as `Subsingleton (Ext P A 1)` for any choice of
>    `HasExt` universe.
>
> The Stacks `Ext_𝒜(P, A)` is the (Yoneda) group of extension classes `0 → A → E → P → 0`;
> Mathlib's `Abelian.Ext P A 1` (derived category `Ext`) is the standard model of it. The
> equivalence `(1) ↔ (4)` is Mathlib's `CategoryTheory.projective_iff_subsingleton_ext_one`.

```lean
theorem projective_tfae [HasExt.{w} 𝒜] (P : 𝒜) :
    List.TFAE [Projective P, HomFunctorExact P, EverySESEndingInPSplits P,
      ∀ A : 𝒜, Subsingleton (Abelian.Ext.{w} P A 1)]
```

## Tag 013D, a lemma

[Tag 013D](https://stacks.math.columbia.edu/tag/013D) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Projective.instSigmaObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Projective.instSigmaObj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L27) (StacksFrontier).

## Tag 013E, a definition

[Tag 013E](https://stacks.math.columbia.edu/tag/013E) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.EnoughProjectives`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.EnoughProjectives#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L28) (StacksFrontier). References: SGA 4 II (6.9).

## Tag 013F, a definition

[Tag 013F](https://stacks.math.columbia.edu/tag/013F) in the Stacks Project.

**`HasFunctorialProjectiveSurjections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L208).

> An abelian category `𝒜` *has functorial projective surjections* if there
> exists a functor `P : 𝒜 ⥤ Arrow 𝒜` satisfying conditions (1), (2) and (3)
> above.

```lean
def HasFunctorialProjectiveSurjections : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.28, Tag 013A](https://stacks.math.columbia.edu/tag/013A)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

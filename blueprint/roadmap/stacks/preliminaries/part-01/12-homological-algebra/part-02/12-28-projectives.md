---
declaration: section
origin: cited
lean: CategoryTheory.Projective, homFunctor_shortExact_of_projective, projective_iff_every_ses_splits, ext_one_eq_zero_of_projective, CategoryTheory.Projective.instSigmaObj, CategoryTheory.EnoughProjectives, HasFunctorialProjectiveSurjections
statement: formalized
proof: formalized
---

# 12.28 Projectives

Section 12.28 of the Stacks Project, [Tag 013A](https://stacks.math.columbia.edu/tag/013A). 5 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 013B, a definition

[Tag 013B](https://stacks.math.columbia.edu/tag/013B) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Projective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Projective#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L22) (StacksFrontier). References: SGA 4 IV (2.6), “partial”; SGA 4 IV (7.6); SGA 6 I (1.2).

## Tag 013C, a lemma

[Tag 013C](https://stacks.math.columbia.edu/tag/013C) in the Stacks Project.

**`homFunctor_shortExact_of_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L98). The attribute's comment: “(1)⇒(2)”.

> `(1) → (2)`: if `P` is projective then `Hom(P, -)` is exact.

```lean
theorem homFunctor_shortExact_of_projective {P : 𝒜} [hP : Projective P]
    (S : ShortComplex 𝒜) (hS : S.ShortExact) :
    ((homFunctor P).mapShortComplex.obj S).ShortExact
```

**`projective_iff_every_ses_splits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L156). The attribute's comment: “(1)⇔(3)”. References: SGA 3 VIIB (1.4.3), “more general”; SGA 6 I (1.3.1), “(i) ⇔ (ii), special case”; SGA 6 V (2.2.1), “special case”.

> **Stacks 013C** (narrowed). `(1) ↔ (3)`: `P` is projective iff every short exact
> sequence ending in `P` splits.
>
> The Stacks lemma states the equivalence of four conditions; this records the
> equivalence between projectivity and the splitting property. The forward
> implications to the other two conditions are given by
> `homFunctor_shortExact_of_projective` and `ext_one_eq_zero_of_projective`.

```lean
theorem projective_iff_every_ses_splits (P : 𝒜) :
    Projective P ↔ EverySESEndingInPSplits P
```

**`ext_one_eq_zero_of_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L163). The attribute's comment: “(1)⇒(4)”.

> `(1) → (4)`: if `P` is projective then `Ext^1(P, A) = 0` for every `A`.
> We use the standard `HasExt` instance from `HasExt.standard 𝒜`.

```lean
theorem ext_one_eq_zero_of_projective {P : 𝒜} [Projective P] (A : 𝒜) :
    haveI : HasExt.{max u v} 𝒜 := HasExt.standard 𝒜
    ∀ (e : Abelian.Ext.{max u v} P A 1), e = 0
```

## Tag 013D, a lemma

[Tag 013D](https://stacks.math.columbia.edu/tag/013D) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Projective.instSigmaObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Projective.instSigmaObj#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L26) (StacksFrontier).

## Tag 013E, a definition

[Tag 013E](https://stacks.math.columbia.edu/tag/013E) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.EnoughProjectives`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.EnoughProjectives#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L27) (StacksFrontier). References: SGA 4 II (6.9).

## Tag 013F, a definition

[Tag 013F](https://stacks.math.columbia.edu/tag/013F) in the Stacks Project.

**`HasFunctorialProjectiveSurjections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Preadditive/Projective/Basic.lean#L215).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

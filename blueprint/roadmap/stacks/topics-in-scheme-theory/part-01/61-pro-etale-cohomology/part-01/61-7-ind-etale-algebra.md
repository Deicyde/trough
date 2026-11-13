---
declaration: section
origin: cited
lean: StacksDraft.IndEtale, CommAlgCat.ind_etale_of_isPushout, CommAlgCat.ind_etale_comp, CategoryTheory.ObjectProperty.ind_ind, CommRingCat.ind_etale_of_comp, CommAlgCat.ind_etale_of_comp, Algebra.weaklyEtale_of_ind_etale, AlgebraicGeometry.ProEtale.indEtaleQuotientBaseChange
statement: formalized
proof: formalized
---

# 61.7 Ind-étale algebra

Section 61.7 of the Stacks Project, [Tag 097H](https://stacks.math.columbia.edu/tag/097H). 7 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 097I, a definition

[Tag 097I](https://stacks.math.columbia.edu/tag/097I) in the Stacks Project.

**`StacksDraft.IndEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Etale/IndEtaleUniverse.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/IndEtaleUniverse.lean#L249).

> **Ind-étaleness with the base and the algebra in independent universes.** For `A : Type u` and
> `B : Type v`, the `A`-algebra `B` is *ind-étale* if `ULift.{u} B` is a filtered colimit of étale
> `A`-algebras in `CommAlgCat.{max u v} A`. This is the shape of the `ind_etale` field of
> `IsLocalRing.IsHenselization`, and in a common universe it is the usual condition
> (`StacksDraft.indEtale_iff`).

```lean
abbrev IndEtale (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B] : Prop
```

## Tag 097J, a lemma

[Tag 097J](https://stacks.math.columbia.edu/tag/097J) in the Stacks Project.

Declarations registered for the tag:

- [`CommAlgCat.ind_etale_of_isPushout`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L1321), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean#L51) (StacksFrontier).

## Tag 097K, a lemma

[Tag 097K](https://stacks.math.columbia.edu/tag/097K) in the Stacks Project.

Declarations registered for the tag:

- [`CommAlgCat.ind_etale_comp`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L1358), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean#L52) (StacksFrontier).

## Tag 097L, a lemma

[Tag 097L](https://stacks.math.columbia.edu/tag/097L) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.ObjectProperty.ind_ind`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.ind_ind#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean#L53) (StacksFrontier).

## Tag 097M, a lemma

[Tag 097M](https://stacks.math.columbia.edu/tag/097M) in the Stacks Project.

Declarations registered for the tag:

- [`CommRingCat.ind_etale_of_comp`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L752), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean#L54) (StacksFrontier).
- [`CommAlgCat.ind_etale_of_comp`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Etale/FilteredColimit/Basic.lean#L1346), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/Permanence.lean#L55) (StacksFrontier).

## Tag 097N, a lemma

[Tag 097N](https://stacks.math.columbia.edu/tag/097N) in the Stacks Project.

**`Algebra.weaklyEtale_of_ind_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IndEtale.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/IndEtale.lean#L51).

> **Stacks Project, Tag 097N.** A filtered colimit of étale algebras is weakly étale.

```lean
theorem weaklyEtale_of_ind_etale {A B : Type*} [CommRing A] [CommRing B]
    [Algebra A B] (h : StacksDraft.IndEtale A B) :
    Algebra.WeaklyEtale A B
```

## Tag 097P, a lemma

[Tag 097P](https://stacks.math.columbia.edu/tag/097P) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.indEtaleQuotientBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean#L76). The attribute's comment: “the quotient base-change functor”.

> Extension of scalars along `A → A ⧸ I`, restricted to ind-étale algebras.

```lean
public noncomputable def indEtaleQuotientBaseChange (A : Type u) [CommRing A]
    (I : Ideal A) : IndEtaleAlgebra A ⥤ IndEtaleAlgebra (A ⧸ I)
```

**`AlgebraicGeometry.ProEtale.indEtaleQuotientLift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean, line 662](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean#L662). The attribute's comment: “the right-adjoint lift”.

> The canonical lift of an ind-étale algebra over `A ⧸ I` to one over `A`.

```lean
public noncomputable def indEtaleQuotientLift (A : Type u) [CommRing A]
    (I : Ideal A) : IndEtaleAlgebra (A ⧸ I) ⥤ IndEtaleAlgebra A
```

**`AlgebraicGeometry.ProEtale.indEtaleBaseChange_hasFullyFaithfulRightAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean, line 991](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean#L991). The attribute's comment: “the adjunction”.

> Quotient base change is left adjoint to the canonical lift.

```lean
public theorem indEtaleBaseChange_hasFullyFaithfulRightAdjoint
    (A : Type u) [CommRing A] (I : Ideal A) :
    Nonempty (indEtaleQuotientBaseChange A I ⊣ indEtaleQuotientLift A I)
```

**`AlgebraicGeometry.ProEtale.indEtaleQuotientLift_baseChangeIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean, line 1246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean#L1246). The attribute's comment: “the quotient comparison”.

> The quotient of a lifted algebra is naturally the original algebra.

```lean
public theorem indEtaleQuotientLift_baseChangeIso
    (A : Type u) [CommRing A] (I : Ideal A) :
    Nonempty (indEtaleQuotientLift A I ⋙ indEtaleQuotientBaseChange A I ≅
      𝟭 (IndEtaleAlgebra (A ⧸ I)))
```

**`AlgebraicGeometry.ProEtale.indEtaleQuotientLift_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean, line 1267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/IndEtale/QuotientLift.lean#L1267). The attribute's comment: “full faithfulness”.

> The right-adjoint lift is fully faithful.

```lean
public theorem indEtaleQuotientLift_fullyFaithful
    (A : Type u) [CommRing A] (I : Ideal A) :
    Nonempty (indEtaleQuotientLift A I).FullyFaithful
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.7, Tag 097H](https://stacks.math.columbia.edu/tag/097H)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

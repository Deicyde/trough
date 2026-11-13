---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsDecentSpace, AlgebraicGeometry.Space.IsReasonableSpace, AlgebraicGeometry.Space.IsVeryReasonableSpace, AlgebraicGeometry.AffineLineTranslation.not_isDecentSpace_translationQuotient, AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_directedApproximation, AlgebraicGeometry.Space.exists_correctedDirectedApproximation, AlgebraicGeometry.Space.exists_quasiCompact_reasonable_isEmpty_directedApproximation, AlgebraicGeometry.Space.isDecentSpace_relocalizeRestrict
statement: formalized
proof: formalized
---

# 68.6 Reasonable and decent algebraic spaces

Section 68.6 of the Stacks Project, [Tag 03I7](https://stacks.math.columbia.edu/tag/03I7). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03I8, a definition

[Tag 03I8](https://stacks.math.columbia.edu/tag/03I8) in the Stacks Project.

**`AlgebraicGeometry.Space.IsDecentSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent.lean#L111). The attribute's comment: “decent”.

> **Stacks 03I8, decent.** An algebraic space over `S` is *decent* when every one of its
> points satisfies the equivalent conditions of Stacks 03JV, taken here in the form of
> condition (4): a quasi-compact monomorphism from the spectrum of a field.

```lean
abbrev IsDecentSpace : Prop
```

**`AlgebraicGeometry.Space.IsReasonableSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Reasonable.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Reasonable.lean#L119). The attribute's comment: “reasonable”.

> **Stacks 03I8, reasonable.** An algebraic space over `S` is *reasonable* when it
> satisfies the equivalent conditions of Stacks 03JT, taken here in the form of condition (2):
> every étale chart of it by an affine scheme has universally bounded fibres.

```lean
abbrev IsReasonableSpace : Prop
```

**`AlgebraicGeometry.Space.IsVeryReasonableSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Reasonable.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Reasonable.lean#L133). The attribute's comment: “very\_reasonable”.

> **Stacks 03I8, very reasonable.** An algebraic space over `S` is *very reasonable* when
> it satisfies the equivalent conditions of Stacks 03IH, taken here in the form of condition
> (2), which is property `(ε)` of Stacks 03JX: there is a jointly surjective family of étale
> charts by schemes whose two self-intersection projections are quasi-compact.

```lean
abbrev IsVeryReasonableSpace : Prop
```

## Tag 03ID, an example

[Tag 03ID](https://stacks.math.columbia.edu/tag/03ID) in the Stacks Project.

**`AlgebraicGeometry.AffineLineTranslation.not_isDecentSpace_translationQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslationNotDecent.lean, line 759](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AffineLineTranslationNotDecent.lean#L759).

> **Stacks 03ID.** The quotient of the affine line over a field of characteristic zero by
> the integer translations is not a decent algebraic space: the point of the quotient
> represented by the generic point of the line has no monomorphic field-valued
> representative.

```lean
theorem not_isDecentSpace_translationQuotient (k : Type u) [Field k] [CharZero k]
    (B : BigFppfSite.{u}) (hS : B.Contains (Spec (.of k)))
    (hG : B.Contains (Spec (.of (RatFunc k))))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hS) (Type u)] :
    ¬ Space.IsDecentSpace B (Spec (.of k)) hS
      (translationQuotient k B hS (contains_affineLine k B hS))
```

## Tag 03K0, a lemma

[Tag 03K0](https://stacks.math.columbia.edu/tag/03K0) in the Stacks Project.

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_directedApproximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableFilteredApproximation/DirectedApproximation.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableFilteredApproximation/DirectedApproximation.lean#L338). The attribute's comment: “refutation of clause (1) as stated: it forces X quasi-separated, so thecorrect clause (1) restricts to quasi-compact quasi-separated test schemes”.

> **Clause (1) of Stacks 03K0, as stated, forces `X` to be quasi-separated.** Let `X` be a
> quasi-compact algebraic space which is a scheme, and suppose it carries a directed
> approximation by quasi-separated algebraic spaces satisfying clause (1) in the form the
> source states it, over every quasi-compact test scheme. Testing clause (1) on `T = X`
> itself — legitimate, since `X` is a quasi-compact scheme over `S` — produces a section of
> one coprojection `X i ⟶ X`, exhibiting `X` as a retract of the quasi-separated space `X i`;
> so `X` is quasi-separated.
>
> Consequently Stacks 03K0 is **false as stated**: a quasi-compact scheme which is not
> quasi-separated is a quasi-compact reasonable algebraic space carrying no such system. The
> repair supported by the source's own proof is to restrict clause (1) to test schemes that
> are quasi-compact *and quasi-separated*.

```lean
theorem isAbsolutelyQuasiSeparated_of_directedApproximation
    (X : Sheaf (BigFppfOver.topology B S hS) (Type u))
    [hrep : X.obj.IsRepresentable]
    (hqc : IsQuasiCompactSpace B S hS X.obj)
    (A : DirectedApproximation B S hS hZ X) :
    IsAbsolutelyQuasiSeparated B S hS hZ X.obj
```

**`AlgebraicGeometry.Space.exists_correctedDirectedApproximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableFilteredApproximation/Existence.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableFilteredApproximation/Existence.lean#L468). The attribute's comment: “the whole lemma, for every quasi-compact reasonable X: colimit in sheaves of adirected system of qcqs spaces, clauses (2) and (3), and clause (1) with injectivity over allquasi-compact T and surjectivity over quasi-compact quasi-separated T; surjectivity over allquasi-compact T is false (see errata) and is refuted unconditionally”.

> **Stacks 03K0.** A quasi-compact reasonable algebraic space over `S` is the colimit, in
> sheaves, of a directed system of quasi-compact and quasi-separated algebraic spaces, and the
> system can be arranged to satisfy clauses (1), (2) and (3) of the source. No quasi-separatedness
> is assumed of `X`.
>
> The system is the one of the source's proof, and it is not constant: by Stacks 03H6 write
> `X = U/R` with `U` affine, and index the system by the quasi-compact open subschemes `R' ⊆ R`
> which are still equivalence relations on `U`, ordered by inclusion. Reasonableness bounds the
> degrees of the fibres of `U ⟶ X` by some `N` (Stacks 03JL), and that bound is what makes the
> index set *cofinal in the quasi-compact opens of `R`* and hence directed: the chain of
> composites `A ↦ c(A ×_{s, U, t} A)` out of a quasi-compact open `A` containing `e(U)`
> stabilises at step `N`, because a chain of length exceeding `N` repeats a point in a fibre of
> `U(k) ⟶ X(k)` for an algebraically closed `k` and can be shortened. Each stage `U/R'` is an
> algebraic space by Stacks 02WW, and is quasi-separated by Stacks 07S4 because `R'` is
> quasi-compact and `U` affine — whereas `R` itself is quasi-compact only when `X` is
> quasi-separated, which is precisely when the system collapses to a single stage.
>
> Clause (1) is the corrected one: injectivity of `colim X i(T) ⟶ X(T)` over every quasi-compact
> test scheme `T`, surjectivity over the quasi-compact *quasi-separated* ones; see
> `AlgebraicGeometry.Space.CorrectedDirectedApproximation`. Over all quasi-compact `T` the
> surjectivity fails, by
> `AlgebraicGeometry.Space.exists_quasiCompact_reasonable_isEmpty_directedApproximation`.

```lean
theorem exists_correctedDirectedApproximation
    (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (AlgebraicGeometry.BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : AlgebraicGeometry.IsAlgebraicSpace B S hS X)
    (hqc : AlgebraicGeometry.Space.IsQuasiCompactSpace B S hS X)
    (hr : IsReasonableSpace B S hS X) :
    Nonempty (CorrectedDirectedApproximation B S hS hZ ⟨X, hX.isSheaf⟩)
```

**`AlgebraicGeometry.Space.exists_quasiCompact_reasonable_isEmpty_directedApproximation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableFilteredApproximationCounterexample.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonableFilteredApproximationCounterexample.lean#L161). The attribute's comment: “refutation of clause (1) as stated, assuming nothing: the doubled-origin scheme of Example 01KL is a quasi-compact reasonable algebraic space with no such system”.

> **Stacks 03K0 is false as stated.** There are a big fppf site, a scheme over its terminal
> object, and no hypotheses at all, for which the lemma's hypotheses hold and its conclusion
> fails: the represented sheaf is an algebraic space, representable, quasi-compact and
> reasonable, and it carries no directed system of quasi-compact quasi-separated algebraic
> spaces with the three clauses of 03K0, because clause (1) over every quasi-compact test scheme
> forces quasi-separatedness of the space itself — a hypothesis 03K0 does not make.
>
> The witness is the doubled-origin scheme of Example 01KL, and the three facts about it that the
> refutation needs are proved in this library: quasi-compactness
> (`AlgebraicGeometry.compactSpace_scheme`), failure of quasi-separatedness
> (`AlgebraicGeometry.not_quasiSeparatedSpace_scheme`) and reasonableness
> (`AlgebraicGeometry.Space.isReasonableSpace_yoneda`, the composite `(θ) ⇒ (δ)` of Stacks 03JX).
>
> The repair supported by the source's own proof is
> `AlgebraicGeometry.Space.exists_correctedDirectedApproximation`, whose clause (1) quantifies
> over test schemes that are quasi-compact *and quasi-separated*; it holds for every
> quasi-compact reasonable algebraic space, this one included.

```lean
theorem exists_quasiCompact_reasonable_isEmpty_directedApproximation (k : Type u) [Field k] :
    ∃ (B : BigFppfSite.{u}) (hZ : B.Contains (⊤_ Scheme.{u}))
      (X : Sheaf (BigFppfOver.topology B (⊤_ Scheme.{u}) hZ) (Type u))
      (_ : X.obj.IsRepresentable),
      IsAlgebraicSpace B (⊤_ Scheme.{u}) hZ X.obj ∧
      IsQuasiCompactSpace B (⊤_ Scheme.{u}) hZ X.obj ∧
      IsReasonableSpace B (⊤_ Scheme.{u}) hZ X.obj ∧
      IsEmpty (DirectedApproximation B (⊤_ Scheme.{u}) hZ hZ X)
```

## Tag 0ABT, a lemma

[Tag 0ABT](https://stacks.math.columbia.edu/tag/0ABT) in the Stacks Project.

**`AlgebraicGeometry.Space.isDecentSpace_relocalizeRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldBaseChange.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldBaseChange.lean#L218). The attribute's comment: “decency under change of affine base”.

> Decency of an algebraic space over an affine scheme `S` is preserved by restriction along a
> morphism `g : S' ⟶ S` of affine schemes of the site: every point of the restricted space is
> presented by a quasi-compact monomorphism from the spectrum of a field.

```lean
theorem isDecentSpace_relocalizeRestrict (B : BigFppfSite.{u}) (S S' : Scheme.{u})
    (hS : B.Contains S) (hS' : B.Contains S')
    [IsAffine S] [IsAffine S']
    (g : B.obj hS' ⟶ B.obj hS)
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (hdecent : IsDecentSpace B S hS X) :
    IsDecentSpace B S' hS' ((CategoryTheory.OverShriek.relocalizeRestrict g).obj X)
```

**`AlgebraicGeometry.Space.hasMonomorphicFieldRepresentative_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RepresentablePermanence.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RepresentablePermanence.lean#L101). The attribute's comment: “decent, as condition (4) of Stacks 03JU at every point”.

> **Stacks 0ABT, the decent case in the form of condition (4) of Stacks 03JU.** Let
> `f : X ⟶ Y` be a representable morphism of presheaves on the big fppf site over `S`. If every
> point of `Y` is the class of a field-valued point presenting it by a monomorphism, then so is
> every point of `X`.

```lean
theorem hasMonomorphicFieldRepresentative_of_relativelyRepresentable (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f)
    (hY : ∀ y : points B S hS Y, HasMonomorphicFieldRepresentative B S hS Y y)
    (x : points B S hS X) :
    HasMonomorphicFieldRepresentative B S hS X x
```

**`AlgebraicGeometry.Space.hasFiniteRelationFibersAtEveryPoint_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RepresentablePermanence.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RepresentablePermanence.lean#L149). The attribute's comment: “decent, as property (β) of Stacks 03JX”.

> **Stacks 0ABT, the decent case as property `(β)` of Stacks 03JX.** The source of a
> representable morphism into a presheaf all of whose points have a monomorphic field-valued
> representative has property `(β)`: every point of it has a finite relation fibre in some
> étale chart.
>
> This is the reading of
> `AlgebraicGeometry.Space.hasMonomorphicFieldRepresentative_of_relativelyRepresentable`
> through the equivalences of Stacks 03JU, which need the source to be an algebraic space.

```lean
theorem hasFiniteRelationFibersAtEveryPoint_of_relativelyRepresentable
    (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f)
    (hY : ∀ y : points B S hS Y, HasMonomorphicFieldRepresentative B S hS Y y) :
    HasFiniteRelationFibersAtEveryPoint B S hS X
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isDecentSpace_of_relativelyRepresentable`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PropertyGammaPermanence.lean#L76), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PropertyGammaPermanence.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PropertyGammaPermanence.lean#L128) (StacksFrontier): “decent”.
- [`AlgebraicGeometry.Space.isReasonableSpace_of_relativelyRepresentable`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonablePermanence.lean#L72), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonablePermanence.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReasonablePermanence.lean#L90) (StacksFrontier): “reasonable”.

## Tag 0ABU, a lemma

[Tag 0ABU](https://stacks.math.columbia.edu/tag/0ABU) in the Stacks Project.

**`AlgebraicGeometry.Space.isDecentSpace_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleSourceDecency.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleSourceDecency.lean#L62). The attribute's comment: “decent”.

> **Stacks 0ABU, the decent case.** An algebraic space over `S` étale over a decent
> algebraic space over `S` is decent.

```lean
theorem isDecentSpace_of_isEtale (f : X ⟶ Y) (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hf : IsEtale B S hS f)
    (hdec : IsDecentSpace B S hS Y) :
    IsDecentSpace B S hS X
```

**`AlgebraicGeometry.Space.isReasonableSpace_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleSourceReasonableness.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/EtaleSourceReasonableness.lean#L108). The attribute's comment: “reasonable”.

> **Stacks 0ABU, the reasonable case.** An algebraic space over `S` étale over a reasonable
> algebraic space over `S` is reasonable.

```lean
theorem isReasonableSpace_of_isEtale (f : X ⟶ Y) (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hf : IsEtale B S hS f)
    (hreas : IsReasonableSpace B S hS Y) :
    IsReasonableSpace B S hS X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.6, Tag 03I7](https://stacks.math.columbia.edu/tag/03I7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

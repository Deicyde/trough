---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isClosedSubspace_minimal_not_isRepresentable, AlgebraicGeometry.Space.hasEtaleLocalProperty_isReduced_and_irreducibleSpace_of_forall_ne_top_isRepresentable, AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_baseChange_specStalkSiteObject, AlgebraicGeometry.Space.exists_maximal_not_isRepresentable_quotientSpace
statement: formalized
proof: formalized
---

# 70.17 Obtaining schemes

Section 70.17 of the Stacks Project, [Tag 0B7X](https://stacks.math.columbia.edu/tag/0B7X). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0B7Y, a lemma

[Tag 0B7Y](https://stacks.math.columbia.edu/tag/0B7Y) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isClosedSubspace_minimal_not_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MinimalNonSchematicClosedSubspaceExistence.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MinimalNonSchematicClosedSubspaceExistence.lean#L209).

> **Stacks 0B7Y.** Let `X` be a quasi-compact and quasi-separated algebraic space over `S`
> which is not a scheme. Then there is a closed subspace `Z` of `X` which is not a scheme but
> every closed subspace of `Z` other than `Z` itself — every *proper* closed subspace of `Z` — is
> a scheme.
>
> This is the source's proof, by Zorn's lemma applied to the closed subspaces of `X` which are
> not schemes, ordered by inclusion: `⊤` is one of them, and the infimum of a chain of them is
> one of them because it is the inverse limit of the chain, which is
> `AlgebraicGeometry.Space.not_isRepresentable_sInf_of_isChain`. A minimal one is the required
> `Z`, and minimality becomes the inner clause by pushing a proper closed subspace of `Z` forward
> to a closed subspace of `X` contained in `Z`.
>
> Nothing is assumed beyond the tag's own hypotheses. In particular no condition is imposed on
> the size of the chain and none on the site's size cutoff: the chain step is discharged by
> `AlgebraicGeometry.Space.DescentSituation.exists_isRepresentable_system_obj_of_isSiteSmall`,
> the library's Stacks 07SR, whose smallness hypothesis is met through
> `AlgebraicGeometry.Space.IsSiteSmall.of_mono` because the transition morphisms of the chain are
> closed immersions, hence monomorphisms.

```lean
theorem exists_isClosedSubspace_minimal_not_isRepresentable (hT : B.Contains (⊤_ Scheme.{u}))
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hqc : IsQuasiCompactSpace B S hS X)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hT X)
    (hXnotScheme : ¬ X.IsRepresentable) :
    ∃ Z : Subfunctor X, IsClosedSubspace B S hS Z ∧ ¬ Z.toFunctor.IsRepresentable ∧
      ∀ Z' : Subfunctor Z.toFunctor, IsClosedSubspace B S hS Z' → Z' ≠ ⊤ →
        Z'.toFunctor.IsRepresentable
```

## Tag 0B7Z, a lemma

[Tag 0B7Z](https://stacks.math.columbia.edu/tag/0B7Z) in the Stacks Project.

**`AlgebraicGeometry.Space.hasEtaleLocalProperty_isReduced_and_irreducibleSpace_of_forall_ne_top_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MinimalNonSchematicSpaceReducedIrreducible.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MinimalNonSchematicSpaceReducedIrreducible.lean#L233).

> **Stacks 0B7Z.** Let `X` be an algebraic space over `S` which is not a scheme, and assume
> that every closed subspace `Z` of `X` with `Z ≠ ⊤` — that is, every *proper* closed subspace of
> `X` — is a scheme. Then `X` is reduced and `|X|` is irreducible.
>
> A closed subspace with every point of `X` cannot be a scheme, by the closed-immersion form of
> Stacks 07VU. Applied to the reduction of `X` this makes the reduction the whole of `X`, which is
> therefore reduced. Applied to the scheme-theoretic union of the reduced induced subspaces on two
> proper closed subsets covering `|X|`, which is a scheme by Stacks 0CZ1 and Stacks 0EDP, it shows
> that no such cover exists; and `|X|` is nonempty since a space without points is a scheme.
>
> The source also assumes `X` quasi-compact and quasi-separated; the proof does not use either
> assumption, so they are omitted.

```lean
theorem hasEtaleLocalProperty_isReduced_and_irreducibleSpace_of_forall_ne_top_isRepresentable
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hproper : ∀ Z : Subfunctor X, IsClosedSubspace B S hS Z → Z ≠ ⊤ →
      Z.toFunctor.IsRepresentable)
    (hXnotScheme : ¬ X.IsRepresentable) :
    HasEtaleLocalProperty B S hS X (fun Y : Scheme.{u} => IsReduced Y) ∧
      IrreducibleSpace (points B S hS X)
```

## Tag 0B80, a lemma

[Tag 0B80](https://stacks.math.columbia.edu/tag/0B80) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_baseChange_specStalkSiteObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Limits/LocalRingSchemeCriterion.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Limits/LocalRingSchemeCriterion.lean#L510).

> **Stacks 0B80.** Let `X` be an algebraic space over a scheme `S` whose structure morphism
> `f` is quasi-compact and quasi-separated. If for every point of `X`, with image `s` in `S`, the
> base change `X ×_S Spec(𝒪_{S, s})` is a scheme, then `X` is a scheme.
>
> This is the same statement as
> `AlgebraicGeometry.Space.isRepresentable_of_isRepresentable_baseChange_specStalk` with the
> object of the site no longer quantified over: `Spec(𝒪_{S, s})` *is* an object of the big fppf
> site of `S` whenever `S` is, by `AlgebraicGeometry.BigFppfSite.contains_spec_stalk_of_contains`, so
> the
> base change of the tag is formed inside the site with nothing assumed.
>
> Nothing is assumed beyond the tag's own hypotheses: no condition on the size of the system of
> affine open neighbourhoods of `s` and none on the site's size cutoff. See the module
> documentation for how Stacks 07SR is met.

```lean
theorem isRepresentable_of_isRepresentable_baseChange_specStalkSiteObject
    (hX : IsAlgebraicSpace B S hS X) (hqc : IsQuasiCompact B S hS f)
    (hqs : IsQuasiSeparated B S hS f)
    (hloc : ∀ p : FieldValuedPoint B S hS X,
      ((baseChangeSiteFunctor f).obj (specStalkSiteObject B S hS
        (p.toBase (IsLocalRing.closedPoint p.carrier)))).IsRepresentable) :
    X.IsRepresentable
```

## Tag 0B81, a lemma

[Tag 0B81](https://stacks.math.columbia.edu/tag/0B81) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_maximal_not_isRepresentable_quotientSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MaximalNonSchematicQuotient.lean, line 805](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MaximalNonSchematicQuotient.lean#L805).

> **Stacks 0B81.** Let `φ : X ⟶ Spec A` be a quasi-compact and quasi-separated morphism from
> an algebraic space to an affine scheme. If `X` is not a scheme then there is an ideal `I ⊂ A`
> such that the base change `X_{A/I}` is not a scheme while `X_{A/I'}` is a scheme for every
> ideal `I'` with `I ⊊ I'`.
>
> By Zorn's lemma applied to the set of ideals `I` with `X_{A/I}` not a scheme. It contains
> `(0)` because `X_{A/0} ≅ X`, and the supremum of a chain of such ideals is again one of them
> because `X_{A/⨆ K}` is the limit of the `X_{A/K i}`
> (`AlgebraicGeometry.Space.quotientDescentSituation`), so Stacks 07SR makes one member of the
> chain a scheme. A maximal element is the required ideal.
>
> Nothing is assumed beyond the tag's own hypotheses, and in particular no bound on the chain and
> no condition on the site's size cutoff. Stacks 07SR is
> `AlgebraicGeometry.Space.DescentSituation.exists_isRepresentable_system_obj_of_isSiteSmall`, whose
> smallness hypothesis is met by `AlgebraicGeometry.Space.IsSiteSmall.of_mono`: the transition
> morphisms of this system are closed immersions, by
> `AlgebraicGeometry.Space.isClosedImmersion_quotientSpaceDiagram_map`, because `A/K i ↠ A/K j`
> is surjective, hence monomorphisms, and for such a system nothing is asked of the index.

```lean
theorem exists_maximal_not_isRepresentable_quotientSpace
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (hqc : IsQuasiCompact B (Spec (.of A)) hA φ)
    (hqs : IsQuasiSeparated B (Spec (.of A)) hA φ)
    (hnot : ¬ X.IsRepresentable) :
    ∃ I : Ideal A, ¬ (quotientSpace A B hA φ I).IsRepresentable ∧
      ∀ I' : Ideal A, I < I' → (quotientSpace A B hA φ I').IsRepresentable
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.17, Tag 0B7X](https://stacks.math.columbia.edu/tag/0B7X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_colimit, AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_colimit_of_cofinal, AlgebraicGeometry.FormalSpace.not_forall_isAffineFormalAlgebraicSpace_colimit, AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_colimit_closedImmersions_of_admissible, AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_colimit_closedImmersions_of_satisfiesSetTheoreticCondition
statement: formalized
proof: formalized
---

# 87.36 Colimits of formal algebraic spaces

Section 87.36 of the Stacks Project, [Tag 0GVL](https://stacks.math.columbia.edu/tag/0GVL). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GVM, a lemma

[Tag 0GVM](https://stacks.math.columbia.edu/tag/0GVM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DirectedColimit.lean, line 787](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DirectedColimit.lean#L787). The attribute's comment: “granting the set-theoretic condition of Stacks 0AIS for the colimit”.

> The colimit of a directed system of affine formal algebraic spaces over `S` whose transition
> morphisms are representable thickenings -- equivalently, closed immersions inducing isomorphisms
> on reductions -- is an affine formal algebraic space over `S`, provided it satisfies the
> set-theoretic condition of Stacks 0AIS.

```lean
theorem isAffineFormalAlgebraicSpace_colimit (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {I : Type (u + 1)} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (D : I ⥤ Sheaf (BigFppfOver.topology B S hS) (Type (u + 1)))
    (hD : ∀ i, IsAffineFormalAlgebraicSpace B S hS (D.obj i))
    (hthick : ∀ ⦃i j : I⦄ (f : i ⟶ j),
      MorphismProperty.relative (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
        (MorphismProperty.inverseImage
          (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)) (D.map f))
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))) (e : X ≅ colimit D)
    (hset : SatisfiesSetTheoreticCondition B S hS X) :
    IsAffineFormalAlgebraicSpace B S hS X
```

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_colimit_of_cofinal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DirectedColimitSetCondition.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DirectedColimitSetCondition.lean#L114). The attribute's comment: “corrected form: the printed statement is false for an index set as large as the size cutoff of the site, the colimit then failing the set-theoretic condition of Stacks 0AIS (AlgebraicGeometry.FormalSpace.not_forall_isAffineFormalAlgebraicSpace_colimit); stated, under the source's hypotheses, for an index with a cofinal family whose index is admissible for coproducts in the site, the proviso of Stacks 0AIS observation (1) that the coproduct of the stages be representable by an object of the site (always the case for a countable index), and with the set-theoretic condition derived, not assumed”.

> **Stacks 0GVM.** The colimit of a directed system of affine formal algebraic spaces over
> `S` whose transition morphisms are representable thickenings -- equivalently, closed immersions
> inducing isomorphisms on reductions -- is an affine formal algebraic space over `S`, provided
> the index set has a cofinal family `ι : K → I` indexed by a set `K` which is not too large
> (`u`-small, of cardinality below the cofinality of the size cutoff of the site; every countable
> `K` qualifies).
>
> The size bound is the proviso of observation (1) of Remark 0AIS. For a colimit
> `X = colim X_λ` of a system as in Definition 0AI7, the source notes that `U = ∐_λ X_λ ⟶ X` is a
> surjection of fppf sheaves, and that "if `U` is representable by an object of `(Sch/S)_fppf`"
> then the set-theoretic condition is satisfied, which "is always the case if `Λ` is countable"
> (Sets, Lemma 000R). Being `u`-small of cardinality below the cofinality of the size cutoff,
> `AlgebraicGeometry.BigFppfSite.AdmitsCoproductIndex`, is what makes a coproduct of objects of
> the site indexed by `K` an object of the site; every countable `K` qualifies
> (`AlgebraicGeometry.BigFppfSite.admitsCoproductIndex_of_countable`). It is asked only of a
> cofinal family, which has the same colimit. Because the stages here are affine formal algebraic
> spaces rather than affine schemes, each stage `X_{ι k}` is replaced by an object `U_k` of the
> site surjecting onto it, as in observation (3) of Remark 0AIS, and `∐_k U_k` is the object of
> the site that the proviso asks for. The bound cannot be dropped: see
> `AlgebraicGeometry.FormalSpace.not_forall_isAffineFormalAlgebraicSpace_colimit`.

```lean
theorem isAffineFormalAlgebraicSpace_colimit_of_cofinal (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {I : Type (u + 1)} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (D : I ⥤ Sheaf (BigFppfOver.topology B S hS) (Type (u + 1)))
    (hD : ∀ i, IsAffineFormalAlgebraicSpace B S hS (D.obj i))
    (hthick : ∀ ⦃i j : I⦄ (f : i ⟶ j),
      MorphismProperty.relative (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
        (MorphismProperty.inverseImage
          (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)) (D.map f))
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))) (e : X ≅ colimit D)
    {K : Type v} [Small.{u} K] [B.AdmitsCoproductIndex K] (ι : K → I)
    (hι : ∀ i, ∃ k, i ≤ ι k) :
    IsAffineFormalAlgebraicSpace B S hS X
```

**`AlgebraicGeometry.FormalSpace.not_forall_isAffineFormalAlgebraicSpace_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/DirectedColimitSetCondition.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/DirectedColimitSetCondition.lean#L185). The attribute's comment: “the statement as printed is false: over any nonempty S, the directed system Spec(k + k^μ) of affine schemes along thickenings, indexed by the finite subsets μ of a set as large as the size cutoff of the site, has a colimit failing the set-theoretic condition of Stacks 0AIS, the coproduct of its stages not being an object of the site as the proviso of Stacks 0AIS observation (1) requires; the corrected form is AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_colimit_of_cofinal”.

> **Stacks 0GVM needs a size bound on the index set.** Over a nonempty scheme `S` of the site
> it is not the case that the colimit of every directed system of affine formal algebraic spaces
> over `S` along representable thickenings is an affine formal algebraic space: the colimit of
> `AlgebraicGeometry.FormalSpace.sqZeroSheafDiagram`, for a residue field of `S` and an index set
> as large as the size cutoff of the site, does not satisfy the set-theoretic condition of
> Remark 0AIS. This is where the proviso of observation (1) of Remark 0AIS fails: each stage has
> one point, so the coproduct of the stages has as many points as the index, which is as large as
> the size cutoff, while an object of the site has fewer points than the cutoff.

```lean
theorem not_forall_isAffineFormalAlgebraicSpace_colimit (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) [Nonempty S] :
    ¬ ∀ (I : Type (u + 1)) [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
      (D : I ⥤ Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))),
      (∀ i, IsAffineFormalAlgebraicSpace B S hS (D.obj i)) →
      (∀ ⦃i j : I⦄ (f : i ⟶ j),
        MorphismProperty.relative (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS))
          (MorphismProperty.inverseImage
            (@Stacks.Thickenings.IsThickening : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS)) (D.map f)) →
      ∀ (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))), (X ≅ colimit D) →
        IsAffineFormalAlgebraicSpace B S hS X
```

## Tag 0GVN, a lemma

[Tag 0GVN](https://stacks.math.columbia.edu/tag/0GVN) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_colimit_closedImmersions_of_admissible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ColimitOfFormalSpacesAdmissible.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ColimitOfFormalSpacesAdmissible.lean#L374). The attribute's comment: “corrected form: the index is required to admit coproducts in the site (AlgebraicGeometry.BigFppfSite.AdmitsCoproductIndex, e.g. any countable index), the caveat of Remark 0AIS (1) and (3) that the source's proof leaves unchecked; without such a bound the statement is false, by AlgebraicGeometry.FormalSpace.not_forall_isFormalAlgebraicSpace_colimit_closedImmersions”.

> **Stacks 0GVN**, in the form its proof establishes. Let `E` be a directed system of formal
> algebraic spaces over `S` whose transition morphisms are representable thickenings —
> equivalently, by Stacks 0GVL, closed immersions inducing isomorphisms on reductions — indexed by
> a type admitting coproducts in the site (every countable index does). Then a sheaf isomorphic to
> its colimit is a formal algebraic space over `S`.
>
> The bound is forced: the source's proof never checks the set-theoretic condition of
> Definition 0AIM for the colimit, Remark 0AIS (1) and (3) give it only for an index "not too
> large (for example countable)", and without a bound the conclusion is false,
> `AlgebraicGeometry.FormalSpace.not_forall_isFormalAlgebraicSpace_colimit_closedImmersions`.

```lean
theorem isFormalAlgebraicSpace_of_colimit_closedImmersions_of_admissible
    (Λ : Type (u + 1)) [Preorder Λ] [Nonempty Λ] [IsDirected Λ (· ≤ ·)] [Small.{u} Λ]
    [B.AdmitsCoproductIndex Λ] (E : Λ ⥤ FppfSheaf B S hS)
    (hform : ∀ i : Λ, IsFormalAlgebraicSpace B S hS (E.obj i))
    (hthick : ∀ ⦃i j : Λ⦄ (g : i ⟶ j),
      Space.IsRepresentableThickeningULift.{u + 1} B S hS (E.map g).hom)
    (Z : FppfSheaf B S hS) (hZ : Nonempty (Z ≅ colimit E)) :
    IsFormalAlgebraicSpace B S hS Z
```

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_colimit_closedImmersions_of_satisfiesSetTheoreticCondition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ColimitOfFormalSpacesAdmissible.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ColimitOfFormalSpacesAdmissible.lean#L406). The attribute's comment: “corrected form per the recorded erratum: for an arbitrary directed index, the colimit of a system of formal algebraic spaces along closed immersions inducing isomorphisms on reductions (representable thickenings, Stacks 0GVL) is a formal algebraic space provided the colimit satisfies the set-theoretic condition of Remark 0AIS; that condition cannot be dropped, AlgebraicGeometry.FormalSpace.not_forall_isFormalAlgebraicSpace_colimit_closedImmersions”.

> **Stacks 0GVN, corrected per the recorded erratum.** Let `E` be a directed system of formal
> algebraic spaces over `S`, indexed by an arbitrary directed set, whose transition morphisms are
> representable thickenings — equivalently, by Stacks 0GVL, closed immersions inducing
> isomorphisms on reductions. A sheaf `Z` isomorphic to its colimit which satisfies the
> set-theoretic condition of Remark 0AIS is a formal algebraic space over `S`.
>
> The set-theoretic condition is the only hypothesis beyond those of the source, and it cannot be
> dropped
> (`AlgebraicGeometry.FormalSpace.not_forall_isFormalAlgebraicSpace_colimit_closedImmersions`).
> The chart system of the source's proof is constructed from an atlas of one stage by the étale
> lifting of Stacks 0DEG/0DEE and its stages are affine by Stacks 0DE8
> (`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_colimit_of_setTheoretic`, with
> `AlgebraicGeometry.FormalSpace.isAffineOfSurjectiveClosedImmersion`); for an index admitting
> coproducts in the site the condition is itself a theorem,
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_of_colimit_closedImmersions_of_admissible`.

```lean
theorem isFormalAlgebraicSpace_of_colimit_closedImmersions_of_satisfiesSetTheoreticCondition
    (Λ : Type (u + 1)) [Preorder Λ] [Nonempty Λ] [IsDirected Λ (· ≤ ·)]
    (E : Λ ⥤ FppfSheaf B S hS)
    (hform : ∀ i : Λ, IsFormalAlgebraicSpace B S hS (E.obj i))
    (hthick : ∀ ⦃i j : Λ⦄ (g : i ⟶ j),
      Space.IsRepresentableThickeningULift.{u + 1} B S hS (E.map g).hom)
    (Z : FppfSheaf B S hS) (hZset : SatisfiesSetTheoreticCondition B S hS Z)
    (hZ : Nonempty (Z ≅ colimit E)) :
    IsFormalAlgebraicSpace B S hS Z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.36, Tag 0GVL](https://stacks.math.columbia.edu/tag/0GVL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

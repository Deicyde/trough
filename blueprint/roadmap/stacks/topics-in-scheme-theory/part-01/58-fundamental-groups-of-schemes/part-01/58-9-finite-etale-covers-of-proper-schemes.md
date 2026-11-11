---
declaration: section
origin: cited
lean: AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isFinite_of_henselianLocalRing, AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianLocalRing, AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isFinite_of_henselianPair, AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianPair, AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_isAlgClosed, AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian, AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian_of_isAlgClosed
statement: formalized
proof: formalized
---

# 58.9 Finite étale covers of proper schemes

Section 58.9 of the Stacks Project, [Tag 0BQC](https://stacks.math.columbia.edu/tag/0BQC). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A48, a lemma

[Tag 0A48](https://stacks.math.columbia.edu/tag/0A48) in the Stacks Project.

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isFinite_of_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperFiniteCase.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperFiniteCase.lean#L245). The attribute's comment: “for a finite morphism `f : X ⟶ Spec A`, which is the case of a proper `f` in which no algebraization is needed”. References: SGA 3 X (4.0), “more general”; SGA 4 XII (5.9bis), “special case”; SGA 4 XIII (1.1), “partial”; SGA 4½ Arcata (4.2.2), “special case”; SGA 7 IX (2.2.4), “more general”.

> **Tag 0A48 for a finite morphism.** If `A` is a henselian local ring and `f : X ⟶ Spec A` is
> finite, then base change to the closed fibre `X ×_{Spec A} Spec (A ⧸ 𝔪) ⟶ X` is an equivalence on
> finite étale covers.
>
> A henselian local ring forms a henselian pair with its maximal ideal
> (`henselianPair_maximalIdeal`), so this is the case `I = 𝔪` of
> `isEquivalence_finiteEtaleBaseChange_of_isFinite_of_henselianPair`. As there, no algebraization
> is used: the general proper case of Tag 0A48 needs Grothendieck existence together with Artin
> approximation.

```lean
theorem isEquivalence_finiteEtaleBaseChange_of_isFinite_of_henselianLocalRing
    (A : Type u) [CommRing A] [HenselianLocalRing A]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [IsFinite f] :
    (finiteEtaleBaseChange (pullback.fst f
      (Spec.map (CommRingCat.ofHom
        (Ideal.Quotient.mk (IsLocalRing.maximalIdeal A)))))).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperHenselianLimit.lean, line 493](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperHenselianLimit.lean#L493). References: SGA 1 X (2.1), “more general”; SGA 3 X (4.0), “more general”; SGA 3 XXIV (8.1.2), “more general”; SGA 4 XII (5.9); SGA 4½ Arcata (4.2.1), “more general”; SGA 7 IX (2.2.4), “more general”; SGA 7 XIII (1.2.1), “more general”.

> **Stacks Project, Tag 0A48.** Let `A` be a henselian local ring and `X` a proper scheme over
> `A` with closed fibre `X₀ = X ×_{Spec A} Spec (A ⧸ 𝔪)`. Then base change
> `FÉt_X ⥤ FÉt_{X₀}, U ↦ U ×_X X₀` is an equivalence of categories.
>
> The three stages of the source's proof are composed by
> `properHenselianFiniteEtaleEquivalence_of_adicFiniteAlgebraAlgebraization`; its one input,
> Grothendieck existence for finite sheaves of algebras over a proper scheme over a complete local
> Noetherian ring, is `adicFiniteAlgebraAlgebraization_of_isProper` (from Stacks 088C).

```lean
theorem isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianLocalRing
    (A : Type u) [CommRing A] [HenselianLocalRing A] {X : Scheme.{u}} (f : X ⟶ Spec (.of A))
    [IsProper f] :
    (finiteEtaleBaseChange (pullback.fst f
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk (maximalIdeal A)))))).IsEquivalence
```

## Tag 0GS2, a lemma

[Tag 0GS2](https://stacks.math.columbia.edu/tag/0GS2) in the Stacks Project.

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isFinite_of_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperFiniteCase.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperFiniteCase.lean#L177). The attribute's comment: “for a finite morphism `f : X ⟶ Spec A`, which is the case of a proper `f` in which no algebraization is needed”.

> **Tag 0GS2 for a finite morphism.** If `(A, I)` is a henselian pair and `f : X ⟶ Spec A` is
> finite, then base change to the closed fibre `X ×_{Spec A} Spec (A ⧸ I) ⟶ X` is an equivalence on
> finite étale covers.
>
> A finite morphism is affine, so `X.isoSpec` presents `X` as `Spec Γ(X, ⊤)` with `Γ(X, ⊤)` a finite,
> hence integral, `A`-algebra, and the statement becomes the affine core
> `isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_henselianPair`.  The two differences
> between the two base-change morphisms are absorbed by the transport lemmas: the pullback along a
> composite is rebracketed by `pullbackRightPullbackFstIso`, and a pullback projection along the
> isomorphism `X.isoSpec.hom` is itself that isomorphism's inverse precomposed with an isomorphism.
>
> This is the case of Tag 0GS2 in which properness is used only through finiteness: no
> algebraization — neither Grothendieck existence nor Artin approximation — enters.

```lean
theorem isEquivalence_finiteEtaleBaseChange_of_isFinite_of_henselianPair
    (A : Type u) [CommRing A] (I : Ideal A) (hI : HenselianPair A I)
    {X : Scheme.{u}} (f : X ⟶ Spec (.of A)) [IsFinite f] :
    (finiteEtaleBaseChange
      (pullback.fst f (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))))).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperHenselianPair.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperHenselianPair.lean#L465). The attribute's comment: “the full statement: any henselian pair `(A, I)` and any proper `X` over `Spec A`, with nothing granted or assumed”. References: SGA 4 XII (6.13), “more general”.

> **Stacks Project, Tag 0GS2.** Let `(A, I)` be a henselian pair and let `X` be a proper scheme
> over `A`, with closed fibre `X₀ = X ×_{Spec A} Spec (A ⧸ I)`. Then base change
> `FÉt_X ⥤ FÉt_{X₀}, U ↦ U ×_X X₀` is an equivalence of categories.
>
> Essential surjectivity is `essSurj_finiteEtaleBaseChange_of_isProper_of_henselianPair`, applied to
> every scheme finite étale over `X` (each again proper over `A`); full faithfulness follows from it
> by `isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianPair_of_essSurj`, as in the
> source.

```lean
theorem isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianPair (A : Type u)
    [CommRing A] (I : Ideal A) (hI : HenselianPair A I) {X : Scheme.{u}}
    (f : X ⟶ Spec (.of A)) [IsProper f] :
    (finiteEtaleBaseChange (pullback.fst f
      (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))))).IsEquivalence
```

## Tag 0A49, a lemma

[Tag 0A49](https://stacks.math.columbia.edu/tag/0A49) in the Stacks Project.

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleAlgClosedEquivalence.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleAlgClosedEquivalence.lean#L58). The attribute's comment: “As stated in the source: `k ⊆ k'` algebraically closed, `X` proper over `k`.”. References: SGA 1 IX (6.3), “more general”; SGA 1 X (1.8), “more general”.

> **Stacks Project, Tag 0A49.** Let `k ⊆ k'` be an extension of algebraically closed fields and
> let `f : X ⟶ Spec k` be proper. Then base change along the projection `X_{k'} ⟶ X`, that is
> `U ↦ U_{k'}`, is an equivalence between the category of schemes finite étale over `X` and the
> category of schemes finite étale over `X_{k'} = X ×_{Spec k} Spec k'`.
>
> This is `isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian_of_isAlgClosed`
> with Tag 0A48 supplied by `properHenselianFiniteEtaleEquivalence`.

```lean
theorem isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_isAlgClosed
    {k k' : Type u} [Field k] [Field k'] [Algebra k k'] [IsAlgClosed k] [IsAlgClosed k']
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] :
    (finiteEtaleBaseChange (pullback.fst f
      (Spec.map (CommRingCat.ofHom (algebraMap k k'))))).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleAlgClosedExtension.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleAlgClosedExtension.lean#L398). The attribute's comment: “the conclusion, with two inputs of the source proof carried as hypotheses: `ProperHenselianFiniteEtaleEquivalence`, Tag 0A48 for a proper — not merely finite — scheme over a henselian local ring; and `FiniteEtaleDescendsToHenselianPoint`, the source's filtered-colimit spreading out. Proved for an arbitrary field extension. See the module docstring.”.

> **Stacks Project, Tag 0A49, granted the proper case of Tag 0A48 and the spreading-out
> hypothesis.** Let `k'/k` be an extension of fields and let `X` be proper over `k`. Then base change
> `U ↦ U_{k'}` is an equivalence between the category of schemes finite étale over `X` and the
> category of schemes finite étale over `X_{k'}`.
>
> Faithfulness is unconditional
> (`faithful_finiteEtaleBaseChange_specMap_algebraMap`); fullness and essential surjectivity come
> from essential surjectivity over every finite étale cover `P` of `X`, each such `P` being again
> proper over `k`, and that is what the two hypotheses provide. The source states this for `k ⊆ k'`
> algebraically closed, which is the case in which its filtered-colimit argument supplies the
> spreading-out hypothesis; the deduction below does not use algebraic closedness.

```lean
theorem isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) [IsProper f]
    (h0A48 : ProperHenselianFiniteEtaleEquivalence.{u})
    (hdesc : ∀ P : FiniteEtaleOver X, FiniteEtaleDescendsToHenselianPoint k k' (P.hom ≫ f)) :
    (finiteEtaleBaseChange (pullback.fst f
      (Spec.map (CommRingCat.ofHom (algebraMap k k'))))).IsEquivalence
```

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian_of_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleSpreadingOut.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleSpreadingOut.lean#L571). The attribute's comment: “for `k ⊆ k'` algebraically closed, with one input of the source proof carried: `ProperHenselianFiniteEtaleEquivalence`, Tag 0A48 for a proper — not merely finite — scheme over a henselian local ring. The source's filtered-colimit spreading out is proved here.”.

> **Stacks Project, Tag 0A49 for an extension of algebraically closed fields**, granted only
> the proper case of Tag 0A48. Let `k ⊆ k'` be algebraically closed fields and let `X` be proper
> over `k`.  Then base change `U ↦ U_{k'}` is an equivalence between the category of schemes finite
> étale over `X` and the category of schemes finite étale over `X_{k'}`.
>
> This is `isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian` with its
> spreading-out hypothesis discharged by
> `AlgebraicGeometry.finiteEtaleDescendsToHenselianPoint_of_isAlgClosed`, applied to each finite
> étale cover `P` of `X`, which is again proper over `k`.

```lean
theorem isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian_of_isAlgClosed
    [IsProper f] (h0A48 : ProperHenselianFiniteEtaleEquivalence.{u}) :
    (finiteEtaleBaseChange (pullback.fst f
      (Spec.map (CommRingCat.ofHom (algebraMap k k'))))).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.9, Tag 0BQC](https://stacks.math.columbia.edu/tag/0BQC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

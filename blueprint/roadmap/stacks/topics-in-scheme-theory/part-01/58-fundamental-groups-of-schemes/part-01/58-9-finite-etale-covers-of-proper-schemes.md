---
declaration: section
origin: cited
lean: AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isFinite_of_henselianLocalRing, AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianLocalRing, AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianPair, AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_isAlgClosed
statement: formalized
proof: formalized
---

# 58.9 Finite étale covers of proper schemes

Section 58.9 of the Stacks Project, [Tag 0BQC](https://stacks.math.columbia.edu/tag/0BQC). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A48, a lemma

[Tag 0A48](https://stacks.math.columbia.edu/tag/0A48) in the Stacks Project.

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isFinite_of_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperFiniteCase.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperFiniteCase.lean#L244). The attribute's comment: “for a finite morphism `f : X ⟶ Spec A`, which is the case of a proper `f` in which no algebraization is needed”. References: SGA 3 X (4.0), “more general”; SGA 4 XII (5.9bis), “special case”; SGA 4 XIII (1.1), “partial”; SGA 4½ Arcata (4.2.2), “special case”; SGA 7 IX (2.2.4), “more general”.

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

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperHenselianLimit.lean, line 493](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperHenselianLimit.lean#L493). References: SGA 1 X (2.1), “more general”; SGA 3 X (4.0), “more general”; SGA 3 XXIV (8.1.2), “more general”; SGA 4 XII (5.9); SGA 4½ Arcata (4.2.1), “more general”; SGA 7 IX (2.2.4), “more general”; SGA 7 XIII (1.2.1), “more general”.

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

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_of_isProper_of_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperHenselianPair.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleProperHenselianPair.lean#L465). The attribute's comment: “any henselian pair `(A, I)` and any proper `X` over `Spec A`, exactly as in the source; no Noetherian or G-ring hypothesis on `A`”. References: SGA 4 XII (6.13), “more general”.

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

**`AlgebraicGeometry.isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_isAlgClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleAlgClosedEquivalence.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FundamentalGroup/FiniteEtaleAlgClosedEquivalence.lean#L62). The attribute's comment: “Complete, under exactly the source's hypotheses: `k ⊆ k'` algebraically closed, `X` proper over `k`.”. References: SGA 1 IX (6.3), “more general”; SGA 1 X (1.8), “more general”.

> **Stacks Project, Tag 0A49.** Let `k ⊆ k'` be an extension of algebraically closed fields and
> let `f : X ⟶ Spec k` be proper. Then base change along the projection `X_{k'} ⟶ X`, that is
> `U ↦ U_{k'}`, is an equivalence between the category of schemes finite étale over `X` and the
> category of schemes finite étale over `X_{k'} = X ×_{Spec k} Spec k'`.
>
> This is `isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_properHenselian_of_isAlgClosed`
> with Tag 0A48 supplied by `properHenselianFiniteEtaleEquivalence`. The stand-in
> `ProperHenselianFiniteEtaleEquivalence` cannot be discharged inside
> `StacksFrontier.AlgebraicGeometry.FundamentalGroup.FiniteEtaleAlgClosedExtension` itself, since the
> module proving it imports that one; this module is where both inputs are supplied.

```lean
theorem isEquivalence_finiteEtaleBaseChange_specMap_algebraMap_of_isAlgClosed
    {k k' : Type u} [Field k] [Field k'] [Algebra k k'] [IsAlgClosed k] [IsAlgClosed k']
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [IsProper f] :
    (finiteEtaleBaseChange (pullback.fst f
      (Spec.map (CommRingCat.ofHom (algebraMap k k'))))).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 58.9, Tag 0BQC](https://stacks.math.columbia.edu/tag/0BQC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

---
declaration: section
origin: cited
lean: CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_smooth_unconditional, CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmoothUnconditional
statement: formalized
proof: formalized
---

# 92.9 Smooth ring maps

Section 92.9 of the Stacks Project, [Tag 08R4](https://stacks.math.columbia.edu/tag/08R4). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08R4, the section

[Tag 08R4](https://stacks.math.columbia.edu/tag/08R4) in the Stacks Project.

**`CommAlgCat.nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_smooth_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothUnconditional.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SmoothUnconditional.lean#L158). The attribute's comment: “the SECTION tag `\section{Smooth ring maps}`, covered by its lemma 08R5, stated here in full. The remark opening the section introduces `weakly quasi-regular` surjections `C → B` (kernel `I` with `I/I²` flat over `B` and `Tor_*^C(B, B)` the exterior algebra on `I/I²`) to say what a generalization of Lemma 08R2 from étale to smooth maps would look at; the source then says `For the moment we just stick to smooth ring maps`, so that remark states no result and introduces nothing the section uses”.

> **[Stacks, Tag 08R5]**, in existence form: for a smooth ring map `A → B`,
> `L_{B/A} = Ω[B⁄A][0]` in `D(B)`. This is also the covering declaration of the section
> **[Stacks, Tag 08R4]**, whose one result is Lemma 08R5.

```lean
theorem nonempty_cotangentComplexDerived_iso_kaehlerDifferential_of_smooth_unconditional
    (A : Type u) [CommRing A] (B : Type u) [CommRing B] [Algebra A B] [Algebra.Smooth A B] :
    Nonempty (cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
        (ModuleCat.of B (KaehlerDifferential A B)))
```

## Tag 08R5, a lemma

[Tag 08R5](https://stacks.math.columbia.edu/tag/08R5) in the Stacks Project.

**`CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmoothUnconditional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SmoothUnconditional.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SmoothUnconditional.lean#L142). The attribute's comment: “the lemma in full and as data: for a SMOOTH ring map `A → B` (`Algebra.Smooth A B`, formally smooth and of finite presentation, as in Stacks), the isomorphism `L_{B/A} ≅ Ω[B⁄A][0]` in `D(B)`. No hypothesis beyond smoothness: the fundamental triangle used along the proof is Tag 08QX, `CommAlgCat.productFundamentalTriangle_distinguished`, and the reduction to the standard smooth case is Lemma 00TA through `Algebra.Smooth.exists_span_eq_top_isStandardSmooth` with the localization step of Lemma 08R3, as in the source's proof”.

> **[Stacks, Tag 08R5].** For a smooth ring map `A → B`, the identification
> `L_{B/A} ≅ Ω[B⁄A][0]` in `D(B)` of the cotangent complex with the module of Kähler
> differentials placed in cohomological degree `0`. This is
> `CommAlgCat.cotangentComplexDerivedIsoKaehlerDifferentialOfSmooth` with Proposition 08QX
> supplied by `CommAlgCat.hasFundamentalTriangle`.

```lean
noncomputable def cotangentComplexDerivedIsoKaehlerDifferentialOfSmoothUnconditional
    (A : Type u) [CommRing A] (B : Type u) [CommRing B] [Algebra A B] [Algebra.Smooth A B] :
    cotangentComplexDerived.{u, u} A (CommAlgCat.of A B) ≅
      (DerivedCategory.singleFunctor (ModuleCat.{u} B) 0).obj
        (ModuleCat.of B (KaehlerDifferential A B))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.9, Tag 08R4](https://stacks.math.columbia.edu/tag/08R4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

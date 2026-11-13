---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_chowDiagram, AlgebraicGeometry.Space.exists_isProper_isSurjective_isImmersion_projectiveSpace
statement: formalized
proof: formalized
---

# 76.41 Variants of Chow's Lemma

Section 76.41 of the Stacks Project, [Tag 089K](https://stacks.math.columbia.edu/tag/089K). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 089L, a lemma

[Tag 089L](https://stacks.math.columbia.edu/tag/089L) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_chowDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChowLemma/ChowDiagram.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChowLemma/ChowDiagram.lean#L300).

> **Chow's lemma for algebraic spaces, [Stacks, Tag 089L].** Let `Y` be a quasi-compact and
> quasi-separated algebraic space over `S` and let `f : X ⟶ Y` be a separated morphism of finite
> type. Then there are algebraic spaces `X'` and `X̄'` and a commutative diagram
> `X ⟵ X' ⟶ X̄' ⟶ Y` over `Y` in which `X' ⟶ X` is proper and surjective, `X' ⟶ X̄'` is an open
> immersion and `X̄' ⟶ Y` is proper and representable.
>
> Every quasi-compact quasi-separated algebraic space has a finite surjective scheme cover
> (`AlgebraicGeometry.Space.existsFiniteSurjectiveSchemeCover_of_isQuasiCompactSpace`), so
> `AlgebraicGeometry.Space.exists_chowDiagram_of_forall_finiteSchemeCover` applies.

```lean
theorem exists_chowDiagram (hZ : B.Contains (⊤_ Scheme.{u}))
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hYqc : IsQuasiCompactSpace B S hS Y) (hYqs : IsAbsolutelyQuasiSeparated B S hS hZ Y)
    (hfsep : IsSeparated B S hS f) (hfft : IsFiniteType B S hS f) :
    ∃ (X' Xbar : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_hX' : IsAlgebraicSpace B S hS X')
      (_hXbar : IsAlgebraicSpace B S hS Xbar) (q : X' ⟶ X) (j : X' ⟶ Xbar) (g : Xbar ⟶ Y),
      IsProper B S hS q ∧ IsSurjective B S hS q ∧ IsOpenImmersion B S hS j ∧
        IsProper B S hS g ∧ yoneda.relativelyRepresentable g ∧ q ≫ f = j ≫ g
```

## Tag 089M, a lemma

[Tag 089M](https://stacks.math.columbia.edu/tag/089M) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isProper_isSurjective_isImmersion_projectiveSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChowLemma/ProjectiveImmersionCover.lean, line 545](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChowLemma/ProjectiveImmersionCover.lean#L545).

> **Chow's lemma over a quasi-compact separated base, [Stacks, Tag 089M].** Let `S` be a
> scheme and `f : X ⟶ Y` a morphism of algebraic spaces over `S`, separated and of finite type,
> with `Y` separated and quasi-compact. Then there are an algebraic space `X'`, a proper surjective
> morphism `q : X' ⟶ X` and an immersion `i : X' ⟶ ℙⁿ_Y` with `q ≫ f = i ≫ (ℙⁿ_Y ⟶ Y)`.
>
> Relative projective space `ℙⁿ_Y` is the fibre product `Y ×_S ℙⁿ_S` over the presheaf represented
> by `S`, which is terminal, with `ℙⁿ_S` the object `AlgebraicGeometry.Space.projectiveSpaceSiteObj`
> of the site; `ℙⁿ_Y ⟶ Y` is the first projection. "Separated" for `Y` is the absolute notion of
> [Stacks, Tag 03BS].

```lean
theorem exists_isProper_isSurjective_isImmersion_projectiveSpace
    (hZ : B.Contains (⊤_ Scheme.{u})) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hfsep : IsSeparated B S hS f) (hfft : IsFiniteType B S hS f)
    (hYsep : IsAbsolutelySeparated B S hS hZ Y) (hYqc : IsQuasiCompactSpace B S hS Y) :
    ∃ (n : ℕ) (hP : B.Contains (projectiveSpaceOver n S))
      (X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS X') (q : X' ⟶ X)
      (i : X' ⟶ pullback ((isTerminal_yoneda_obj_base B S hS).from Y)
        ((isTerminal_yoneda_obj_base B S hS).from
          (yoneda.obj (projectiveSpaceSiteObj B S hS n hP)))),
      IsProper B S hS q ∧ IsSurjective B S hS q ∧ IsImmersion B S hS i ∧
        q ≫ f = i ≫ pullback.fst _ _
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.41, Tag 089K](https://stacks.math.columbia.edu/tag/089K)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

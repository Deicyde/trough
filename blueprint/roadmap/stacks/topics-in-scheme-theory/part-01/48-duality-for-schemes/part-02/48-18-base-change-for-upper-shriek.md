---
declaration: section
origin: cited
lean: Stacks.Duality.upperShriekFlatBaseChangeIso, Stacks.Duality.upperShriekIsoPullbackOfEtale, Stacks.Duality.nonempty_restrict_derivedPullback_upperShriek_iso, Stacks.Duality.isDualizingComplex_derivedPullback_fibreι_upperShriek_unconditional
statement: formalized
proof: formalized
---

# 48.18 Base change for upper shriek

Section 48.18 of the Stacks Project, [Tag 0BZX](https://stacks.math.columbia.edu/tag/0BZX). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0E9U, a lemma

[Tag 0E9U](https://stacks.math.columbia.edu/tag/0E9U) in the Stacks Project.

**`Stacks.Duality.upperShriekFlatBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFlatBaseChangeIso.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekFlatBaseChangeIso.lean#L91).

> **Flat base change for `f^!`.** Let `S` be Noetherian and let `X' ⟶ X` over `Y' ⟶ Y` be a
> cartesian square of `FTS S` with `g` flat. Then `L(g')^* ∘ f^! ≅ (f')^! ∘ Lg^*` on
> `D^+_QCoh(𝒪_Y)`, with `f^!` computed at any compactification `j` of `f` and `(f')^!` at any
> compactification `c'` of `f'`. It is the base change map `L(g')^* j^* ā ≅ (j')^* L(ḡ')^* ā ⟶
> (j')^* ā' Lg^*` of the base change `j'` of `j`, followed by the comparison
> `(f')^!_{j'} ≅ (f')^!_{c'}` of [Stacks, Tag 0AA0] at `Lg^*K ∈ D^+_QCoh(𝒪_{Y'})`.

```lean
def upperShriekFlatBaseChangeIso (c' : CompactificationOf (Over.mk f'.left)) :
    (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙
        upperShriek f c ⋙ quasiCoherentDerivedPullback' g'.left ≅
      (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙
        quasiCoherentDerivedPullback' g.left ⋙ upperShriek f' c'
```

## Tag 0FWI, a lemma

[Tag 0FWI](https://stacks.math.columbia.edu/tag/0FWI) in the Stacks Project.

**`Stacks.Duality.upperShriekIsoPullbackOfEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/UpperShriekEtale.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/UpperShriekEtale.lean#L99).

> **Stacks Project, Tag 0FWI.** In Situation 48.16.1 let `f : X ⟶ Y` be an
> étale morphism of `FTS S`. Then `f^! ≅ f^*` as functors on `D^+_QCoh(𝒪_Y)`, for `f^!` computed
> at any compactification `j`. The isomorphism at `K` is
> `Lf^*K ≅ Lf^*K ⊗ᴸ 𝒪_X ≅ Lf^*K ⊗ᴸ f^!𝒪_Y ≅ f^!K`, the last map being `μ_{f,K}` of
> [Stacks, Tag 0B6U] (e).

```lean
def upperShriekIsoPullbackOfEtale [Etale f.left] :
    (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙ upperShriek f j ≅
      (ObjectProperty.ι _ : quasiCoherentDerivedCategoryPlusOfModel Y.left ⥤ _) ⋙
        quasiCoherentDerivedPullback' f.left
```

## Tag 0BZY, a lemma

[Tag 0BZY](https://stacks.math.columbia.edu/tag/0BZY) in the Stacks Project.

**`Stacks.Duality.nonempty_restrict_derivedPullback_upperShriek_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingBaseChange/MakeshiftBaseChange.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingBaseChange/MakeshiftBaseChange.lean#L308).

> **[Stacks, Tag 0BZY] (makeshift base change).** In Situation 48.16.1 let `X' = X ×_Y Y'` be a
> cartesian square of `FTS S` with `f` flat, let `E ∈ D⁺_QCoh(𝒪_Y)` with `Lg^*E` bounded below,
> and let `j`, `j'` be compactifications computing `f^!` and `f'^!`. For an affine open `U' ⊆ X'`
> mapping into affine opens `U ⊆ X`, `V' ⊆ Y'`, `V ⊆ Y` of the square (`g'(U') ⊆ U`,
> `f'(U') ⊆ V'`, `f(U) ⊆ V`, `g(V') ⊆ V`), the restrictions to `U'` of `L(g')^*f^!E` and
> `(f')^!Lg^*E` are isomorphic.
>
> *The reading of "mapping into affine opens".* The source asks for `U' ⊂ X'` "affine open mapping
> into affine opens of `Y`, `Y'`, and `X`", and its proof begins "we immediately reduce to the case
> where `X`, `Y`, `Y'`, and `X'` are affine", which needs the four affine opens to form a cartesian
> square of affines; so the opens are a compatible quadruple, `f(U) ⊆ V` and `g(V') ⊆ V`. Three
> independently chosen affine opens containing the images of `U'` need not form such a square:
> `U ∩ f⁻¹(V)` need not be affine (the base `S` is not assumed separated), so no single affine chart
> of `f` need contain `g'(U')`.
>
> The proof is the source's: on the charts both sides are the sheaves
> associated to the algebraic base change
> `Dualizing.nonempty_totalDerivedExtensionScalars_upperShriekFunctor_iso_of_isOpenImmersion`, by
> the chart description `Stacks.Duality.upperShriekCharts` of [Stacks, Tag 0BV2].

```lean
theorem nonempty_restrict_derivedPullback_upperShriek_iso
    {X X' Y Y' : AlgebraicGeometry.FTS S} (f : X ⟶ Y) (f' : X' ⟶ Y') (g : Y' ⟶ Y) (g' : X' ⟶ X)
    (sq : IsPullback g'.left f'.left f.left g.left) [Flat f.left]
    (j : AlgebraicGeometry.CompactificationOf (Over.mk f.left))
    (j' : AlgebraicGeometry.CompactificationOf (Over.mk f'.left))
    (E : quasiCoherentDerivedCategory Y.left) (hE : DerivedCategoryB.IsBoundedBelow E.obj)
    (hE' : DerivedCategoryB.IsBoundedBelow ((quasiCoherentDerivedPullback' g.left).obj E).obj)
    {U' : X'.left.Opens} (hU' : IsAffineOpen U') {U : X.left.Opens} (hU : IsAffineOpen U)
    {V' : Y'.left.Opens} (hV' : IsAffineOpen V') {V : Y.left.Opens} (hV : IsAffineOpen V)
    (hU'U : U' ≤ g'.left ⁻¹ᵁ U) (hU'V' : U' ≤ f'.left ⁻¹ᵁ V') (hUV : U ≤ f.left ⁻¹ᵁ V)
    (hV'V : V' ≤ g.left ⁻¹ᵁ V) :
    Nonempty ((Scheme.Modules.restrictFunctor U'.ι).mapDerivedCategory.obj
        ((quasiCoherentDerivedPullback' g'.left).obj ((upperShriek f j).obj E)).obj ≅
      (Scheme.Modules.restrictFunctor U'.ι).mapDerivedCategory.obj
        ((upperShriek f' j').obj ((quasiCoherentDerivedPullback' g.left).obj E)).obj)
```

## Tag 0BZZ, a lemma

[Tag 0BZZ](https://stacks.math.columbia.edu/tag/0BZZ) in the Stacks Project.

**`Stacks.Duality.isDualizingComplex_derivedPullback_fibreι_upperShriek_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/DualizingBaseChange/FibreDualizingCharts.lean, line 440](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/DualizingBaseChange/FibreDualizingCharts.lean#L440).

> **Stacks Project, Tag 0BZZ (Lemma 48.18.4).** In Situation 48.16.1 let `f : X ⟶ Y` be a flat
> morphism of `FTS S` and set `ω^•_{X/Y} = f^!𝒪_Y`, for any compactification `j` defining `f^!`.
> For `y ∈ Y` let `h : X_y ⟶ X` be the projection from the fibre. Then `Lh^*ω^•_{X/Y}` is a
> dualizing complex on `X_y`.
>
> The fibre charts over the affine charts of `f` cover `X_y`; on each, by
> `Stacks.Duality.upperShriekStructureSheafCharts` and [Stacks, Tag 08DW], `Lh^*ω^•_{X/Y}` is the
> sheaf associated to `ω^•_{A/R} ⊗ᴸ_A (A ⊗_R κ(y))`, which is dualizing by [Stacks, Tag 0BZW];
> [Stacks, Tag 0A86] glues.

```lean
theorem isDualizingComplex_derivedPullback_fibreι_upperShriek_unconditional [Flat f.left]
    (y : Y.left) :
    IsDualizingComplex
      ((derivedPullback (f.left.fiberι y)).obj (relativeDualizingComplexObj f j))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 48.18, Tag 0BZX](https://stacks.math.columbia.edu/tag/0BZX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

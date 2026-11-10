---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_finite_surjective_zariskiLocal_factorization, AlgebraicGeometry.Stack.AlgebraicStacks.hasProperCompactifiableCover_of_isGerbeOver, AlgebraicGeometry.Stack.AlgebraicStacks.hasChowCover
statement: formalized
proof: formalized
---

# 106.10 Chow's lemma for algebraic stacks

Section 106.10 of the Stacks Project, [Tag 0CQ5](https://stacks.math.columbia.edu/tag/0CQ5). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CQ6, a lemma

[Tag 0CQ6](https://stacks.math.columbia.edu/tag/0CQ6) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_finite_surjective_zariskiLocal_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChowFiniteCoverFactorizationUnconditional.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChowFiniteCoverFactorizationUnconditional.lean#L61). The attribute's comment: “Chow's lemma for algebraic stacks: a flat surjection locally of finite presentation onto a quasi-compact open of a qcqs algebraic space splits Zariski locally after a finite surjective base change.”.

> **[Stacks, Tag 0CQ6].** Let `Y` be a quasi-compact and quasi-separated algebraic space over
> `S`, let `V ⊆ Y` be a quasi-compact open subspace and let `f : 𝒳 ⟶ V` be a surjective and flat
> 1-morphism of algebraic stacks which is locally of finite presentation. Then there is a finite
> surjective morphism `g : Y' ⟶ Y` of algebraic spaces such that `V' = g⁻¹(V) ⟶ V` factors Zariski
> locally through `f`: there are open immersions `ι j : W j ⟶ Y'` contained in `g⁻¹(V)` (they
> factor through `V` over `g`, by `q j`) whose images cover `g⁻¹(V)`, and 1-morphisms
> `x j : W j ⟶ 𝒳` with `x j ≫ f` 2-isomorphic to `q j`.
>
> The proof is the source's second paragraph: [Stacks, Proposition 09YC] (in the form
> `AlgebraicGeometry.Space.existsFiniteSurjectiveSchemeCover_of_isQuasiCompactSpace`) gives a finite
> surjective `π : h_{Y₁} ⟶ Y` from a scheme of the site; `Y₁` is quasi-compact and
> quasi-separated, `π⁻¹(V)` is a quasi-compact open of `h_{Y₁}`, and the base change of `f` to it is
> again surjective, flat and locally of finite presentation. The scheme case,
> `AlgebraicGeometry.Stack.exists_finite_surjective_zariskiLocal_factorization_of_yoneda`
> ([Stacks, Tag 0CP0] and [Stacks, Tag 0CNY]), then gives a finite surjective `Y' ⟶ h_{Y₁}`, and
> its composite with `π` is the required `g`.

```lean
theorem exists_finite_surjective_zariskiLocal_factorization
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hY : IsAlgebraicSpace B S hS Y)
    (hYqc : Space.IsQuasiCompactSpace B S hS Y)
    (hYqs : Space.IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    (V : Subfunctor Y) (hV : Space.IsOpenSubspace B S hS V)
    (hVqc : Space.IsQuasiCompactSpace B S hS V.toFunctor)
    {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS V.toFunctor hV.1)
    (hfs : IsSurjective B S hS f) (hff : AlgebraicStacks.IsFlat B S hS f)
    (hfl : AlgebraicStacks.IsLocallyOfFinitePresentation B S hS f) :
    ∃ (Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Y') (g : Y' ⟶ Y),
      Space.IsFinite B S hS g ∧ Space.IsSurjective B S hS g ∧
      ∃ (J : Type u) (W : J → (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
        (hW : ∀ j, IsAlgebraicSpace B S hS (W j)) (ι : ∀ j, W j ⟶ Y')
        (q : ∀ j, W j ⟶ V.toFunctor)
        (x : ∀ j, algebraicSpaceStack.{u, w} B S hS (W j) (hW j) ⟶ 𝒳),
        (∀ j, Space.IsOpenImmersion B S hS (ι j)) ∧ (∀ j, ι j ≫ g = q j ≫ V.ι) ∧
        (∀ y : Space.points B S hS Y',
          Space.pointsMap B S hS Y' g y ∈ Set.range (Space.pointsMap B S hS V.toFunctor V.ι) →
            ∃ j, y ∈ Set.range (Space.pointsMap B S hS (W j) (ι j))) ∧
        ∀ j, Nonempty (x j ≫ f ≅ algebraicSpaceStackMap.{u, w} B S hS (hW j) hV.1 (q j))
```

## Tag 0CQ7, a lemma

[Tag 0CQ7](https://stacks.math.columbia.edu/tag/0CQ7) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.hasProperCompactifiableCover_of_isGerbeOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/C1575Private/ChowGerbeProperCover.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/C1575Private/ChowGerbeProperCover.lean#L202).

> **[Stacks, Tag 0CQ7].** Let `f : 𝒳 ⟶ Y` be a 1-morphism from an algebraic stack to an
> algebraic space and `V ⊆ Y` an open subspace. Assume that `f` is separated and of finite type,
> that `Y` is quasi-compact and quasi-separated, that `V` is quasi-compact, and that `𝒳_V` is a
> gerbe over `V`. Then there are algebraic spaces `Z`, `Z̄`, an open immersion `j : Z ⟶ Z̄`, a proper
> `ḡ : Z̄ ⟶ Y` and a proper `h : Z ⟶ 𝒳` with `h ≫ f` 2-isomorphic to `g = j ≫ ḡ`, such that `|V|`
> is contained in the image of `|g|`.

```lean
theorem hasProperCompactifiableCover_of_isGerbeOver {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hY : IsAlgebraicSpace B S hS Y) {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS Y hY)
    (hfs : IsSeparated B S hS f) (hft : IsFiniteType B S hS f)
    (hYqc : Space.IsQuasiCompactSpace B S hS Y)
    (hYqs : Space.IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    (V : Subfunctor Y) (hV : Space.IsOpenSubspace B S hS V)
    (hVqc : Space.IsQuasiCompactSpace B S hS V.toFunctor)
    (hG : IsGerbeOver B S hS (twoFibreProductSquareAlgebraicStacks B S hS
      (algebraicSpaceStackMap.{u, w} B S hS hV.1 hY V.ι) f).fst) :
    HasProperCompactifiableCover.{u, w} B S hS hY f V
```

## Tag 0CQ8, a theorem

[Tag 0CQ8](https://stacks.math.columbia.edu/tag/0CQ8) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.hasChowCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ChowLemmaAlgebraicStacks.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ChowLemmaAlgebraicStacks.lean#L66). The attribute's comment: “Chow's lemma for algebraic stacks: the commutative diagram is a 2-isomorphism `a ≫ f ≅ i ≫ p` in the 2-category of algebraic stacks over S, with X and X̄ algebraic spaces”.

> **Chow's lemma for algebraic stacks (Stacks 0CQ8).** Let `f : 𝒳 ⟶ Y` be a 1-morphism from an
> algebraic stack to an algebraic space over `S`, with `Y` quasi-compact and quasi-separated and `f`
> separated of finite type. Then there are an algebraic space `X` with a proper surjective
> 1-morphism `a : X ⟶ 𝒳`, an open immersion `i : X ⟶ X̄` and a proper morphism `p : X̄ ⟶ Y` of
> algebraic spaces such that `a ≫ f` is 2-isomorphic to the 1-morphism induced by `i ≫ p`.

```lean
theorem hasChowCover (B : BigFppfSite.{u}) {S : Scheme.{u}} {hS : B.Contains S}
    {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hY : IsAlgebraicSpace B S hS Y)
    (hYqc : Space.IsQuasiCompactSpace B S hS Y)
    (hYqs : Space.IsAbsolutelyQuasiSeparated B S hS B.contains_terminal Y)
    {𝒳 : AlgebraicStacks.{u, w} B S hS} (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS Y hY)
    (hsep : IsSeparated B S hS f) (hft : IsFiniteType B S hS f) :
    HasChowCover.{u, w} B S hS hY f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.10, Tag 0CQ5](https://stacks.math.columbia.edu/tag/0CQ5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

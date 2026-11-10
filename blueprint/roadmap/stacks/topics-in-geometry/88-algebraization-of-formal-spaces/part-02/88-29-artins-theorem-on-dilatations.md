---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.exists_isProper_completion_iso_of_isFormalModification, AlgebraicGeometry.FormalSpace.existsUnique_completionOverFunctor_map_comp_eq_of_isProper, AlgebraicGeometry.FormalSpace.exists_isProper_completionOverFunctor_iso_of_isFormalModification
statement: formalized
proof: formalized
---

# 88.29 Artin's theorem on dilatations

Section 88.29 of the Stacks Project, [Tag 0GDT](https://stacks.math.columbia.edu/tag/0GDT). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GDU, a theorem

[Tag 0GDU](https://stacks.math.columbia.edu/tag/0GDU) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_isProper_completion_iso_of_isFormalModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationEquivalence.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationEquivalence.lean#L105). The attribute's comment: “existence: a proper f : X' ⟶ X, isomorphism over U, with f_{/T} ≅ 𝔣 over X_{/T}”.

> **Stacks 0GDU, existence.** Let `X` be a locally Noetherian algebraic space over `S`, let
> `T ⊆ |X|` be closed, `U ⊂ X` the open subspace with `|U| = |X| ∖ T`, and let
> `𝔣 : 𝔛' ⟶ X_{/T}` be a formal modification (Definition 0GDK). Then there is a proper morphism
> `f : X' ⟶ X` of algebraic spaces which is an isomorphism over `U` and whose completion `f_{/T}`
> is isomorphic to `𝔣` over `X_{/T}`.
>
> By Stacks 0ARB (`isEquivalence_completionModificationFunctor`), `𝔣`, an object of the
> right-hand category of Stacks 0AR5, is the completion of a finite-type modification `f`; by
> Stacks 0ARX (`isProper_iff_isFormalModification_of_iso`) `f` is proper.

```lean
theorem exists_isProper_completion_iso_of_isFormalModification
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hXsp : IsAlgebraicSpace B S hS X)
    (hX : Space.IsLocallyNoetherian B S hS X) (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    {W : FppfSheaf B S hS} {𝔣 : W ⟶ Space.completionSheaf B S hS X T}
    (h𝔣 : IsFormalModification B S hS 𝔣) :
    ∃ (X' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS X') (f : X' ⟶ X),
      Space.IsProper B S hS f ∧ IsIso (pullback.snd f (Space.openSubspaceOfPoints B S hS X Tᶜ).ι) ∧
        Nonempty ((Space.completionOverFunctor B S hS T).obj (Over.mk f) ≅ Over.mk 𝔣)
```

**`AlgebraicGeometry.FormalSpace.existsUnique_completionOverFunctor_map_comp_eq_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationEquivalence.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionModificationEquivalence.lean#L141). The attribute's comment: “uniqueness: any two such proper f₁, f₂ are isomorphic over X by a unique isomorphism compatible with the identifications of f₁_{/T} and f₂_{/T} with 𝔣”.

> **Stacks 0GDU, uniqueness.** In the situation of
> `exists_isProper_completion_iso_of_isFormalModification`, let `f₁ : X₁ ⟶ X` and `f₂ : X₂ ⟶ X`
> be proper morphisms of algebraic spaces which are isomorphisms over `U`, with isomorphisms
> `e₁ : f₁_{/T} ≅ 𝔣` and `e₂ : f₂_{/T} ≅ 𝔣` over `X_{/T}`. Then there is exactly one morphism
> `φ : X₁ ⟶ X₂` over `X` whose completion is compatible with `e₁` and `e₂`, and it is an
> isomorphism. So `f` is unique up to unique isomorphism.
>
> This is Stacks 0GDR (`AlgebraicGeometry.Space.completionOverFunctor_map_bijective`), which holds
> because a proper morphism is locally of finite type.

```lean
theorem existsUnique_completionOverFunctor_map_comp_eq_of_isProper
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hXsp : IsAlgebraicSpace B S hS X)
    (hX : Space.IsLocallyNoetherian B S hS X) (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    {W : FppfSheaf B S hS} (𝔣 : W ⟶ Space.completionSheaf B S hS X T)
    {X₁ X₂ : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX₁ : IsAlgebraicSpace B S hS X₁)
    (hX₂ : IsAlgebraicSpace B S hS X₂) {f₁ : X₁ ⟶ X} {f₂ : X₂ ⟶ X}
    (hf₁ : Space.IsProper B S hS f₁) (hf₂ : Space.IsProper B S hS f₂)
    (hU₁ : IsIso (pullback.snd f₁ (Space.openSubspaceOfPoints B S hS X Tᶜ).ι))
    (hU₂ : IsIso (pullback.snd f₂ (Space.openSubspaceOfPoints B S hS X Tᶜ).ι))
    (e₁ : (Space.completionOverFunctor B S hS T).obj (Over.mk f₁) ≅ Over.mk 𝔣)
    (e₂ : (Space.completionOverFunctor B S hS T).obj (Over.mk f₂) ≅ Over.mk 𝔣) :
    ∃! φ : Over.mk f₁ ⟶ Over.mk f₂,
      (Space.completionOverFunctor B S hS T).map φ ≫ e₂.hom = e₁.hom ∧ IsIso φ
```

## Tag 0GDV, a lemma

[Tag 0GDV](https://stacks.math.columbia.edu/tag/0GDV) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_isProper_completionOverFunctor_iso_of_isFormalModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FormalModificationAlgebraization.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FormalModificationAlgebraization.lean#L273).

> **Stacks 0GDV.** Let `f : 𝔛' ⟶ 𝔛` be a formal modification (Definition 0GDK) of locally
> Noetherian formal algebraic spaces over `S`. Let `A` be an adic Noetherian topological ring and
> let `g : Spf A ⟶ 𝔛` be an adic morphism, `Spf A` being a formal algebraic space over `S` through
> the quotient system `D`. Then there are a proper morphism `p : X ⟶ Spec A` of algebraic spaces
> and an isomorphism `Spf A ×_𝔛 𝔛' ≅ X_{/Z}` over `Spf A` of the base change of `f` with the formal
> completion of `X` along its closed fibre `Z = X ×_{Spec A} Spf(A)_red`.
>
> Algebraic spaces with no base are algebraic spaces over `Spec ℤ`, the terminal scheme, and the
> base change, a formal algebraic space over `S`, is viewed over `Spec ℤ` by the change of base of
> Stacks 04SG (`AlgebraicGeometry.FormalSpace.smallerBaseSheafFunctor`). The closed fibre is the
> inverse image under `p` of the zero locus `V(I)` of an ideal of definition `I`, which is the
> closed subset of `Spec A` underlying `Spf(A)_red`; the completion along it is
> `AlgebraicGeometry.Space.completionOverFunctor`, and the isomorphism is one over the completion of
> `Spec A` along `V(I)`, which is `Spf A`
> (`AlgebraicGeometry.FormalSpace.formalSpectrumCompletionIso`).
> The statement holds for every ideal of definition `I`.
>
> As in the source: the base change `Spf A ×_𝔛 𝔛' ⟶ Spf A` is a formal modification by Stacks
> 0GDN, and Theorem 0GDU applies to it.

```lean
theorem exists_isProper_completionOverFunctor_iso_of_isFormalModification
    {A : Type u} [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : TopologicalRing.IsNoetherianAdic A) (hAB : B.Contains (Spec (.of A)))
    (I : Ideal A) (hI : TopologicalRing.IsIdealOfDefinition I)
    {X' X : FppfSheaf B S hS} (f : X' ⟶ X) (hf : IsFormalModification B S hS f)
    (D : QuotientSystem B S hS A) (g : formalSpectrum D ⟶ X) (hg : IsAdicMorphism B S hS g) :
    ∃ (Y : (BigFppfOver B (⊤_ Scheme.{u}) hZ)ᵒᵖ ⥤ Type u)
      (_ : IsAlgebraicSpace B (⊤_ Scheme.{u}) hZ Y)
      (p : Y ⟶ yoneda.obj (specOverTerminal B hZ hAB)),
      Space.IsProper B (⊤_ Scheme.{u}) hZ p ∧
        Nonempty ((Space.completionOverFunctor B (⊤_ Scheme.{u}) hZ
            (zeroLocusPoints B (⊤_ Scheme.{u}) hZ hAB (terminal.from _) I)).obj (Over.mk p) ≅
          Over.mk ((Ψ).map (pullback.snd f g) ≫
            (formalSpectrumCompletionIso B hZ S hS hAB hA I hI D).hom))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.29, Tag 0GDT](https://stacks.math.columbia.edu/tag/0GDT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

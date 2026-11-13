---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isQuasiCompact_iff_isQuasiCompact_of_overIso, AlgebraicGeometry.FormalSpace.isQuasiSeparated_iff_hasQuasiCompactDiagonal_of_overIso, AlgebraicGeometry.FormalSpace.isSeparated_iff_isSeparatedMorphism_and_isRigSurjective_diagonal_of_iso, AlgebraicGeometry.FormalSpace.isProper_iff_isFormalModification_of_iso, AlgebraicGeometry.FormalSpace.isEtale_iff_isRepresentableEtale_of_overIso
statement: formalized
proof: formalized
---

# 88.28 Completions and morphisms, II

Section 88.28 of the Stacks Project, [Tag 0GDS](https://stacks.math.columbia.edu/tag/0GDS). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ARU, a lemma

[Tag 0ARU](https://stacks.math.columbia.edu/tag/0ARU) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isQuasiCompact_iff_isQuasiCompact_of_overIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasiCompactIff.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasiCompactIff.lean#L462).

> **Stacks 0ARU.** Let `X` be a locally Noetherian algebraic space over `S`, let `T ⊆ |X|` be
> a closed subset and let `U ⊂ X` be the open subspace with `|U| = |X| ∖ T`. Let `f : X' ⟶ X` be
> a morphism of algebraic spaces which is locally of finite type and such that `f⁻¹U ⟶ U` is an
> isomorphism, and let `g : W ⟶ X_{/T}` correspond to `f` under the completion functor of
> Stacks 0AR5, that is, be isomorphic over `X_{/T}` to `f_{/T} : X'_{/T'} ⟶ X_{/T}`. Then `f` is
> quasi-compact if and only if `g` is quasi-compact.

```lean
theorem isQuasiCompact_iff_isQuasiCompact_of_overIso
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hXN : Space.IsLocallyNoetherian B S hS X)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (M : Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ))
    {W : FppfSheaf B S hS} (g : W ⟶ Space.completionSheaf B S hS X T)
    (e : Over.mk g ≅ Over.mk (Space.completionSheafMap B S hS M.obj.hom T)) :
    Space.IsQuasiCompact B S hS M.obj.hom ↔ IsQuasiCompact B S hS g
```

## Tag 0ARV, a lemma

[Tag 0ARV](https://stacks.math.columbia.edu/tag/0ARV) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isQuasiSeparated_iff_hasQuasiCompactDiagonal_of_overIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasiSeparatedIff.lean, line 246](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasiSeparatedIff.lean#L246).

> **Stacks 0ARV.** Let `X` be a locally Noetherian algebraic space over `S`, let `T ⊆ |X|` be
> a closed subset and let `U ⊂ X` be the open subspace with `|U| = |X| ∖ T`. Let `f : X' ⟶ X` be
> a morphism of algebraic spaces which is locally of finite type and such that `f⁻¹U ⟶ U` is an
> isomorphism, and let `g : W ⟶ X_{/T}` correspond to `f` under the equivalence of Stacks 0ARB
> (`isEquivalence_completionModificationFunctor`), that is, be isomorphic over `X_{/T}` to the
> completion `f_{/T} : X'_{/T'} ⟶ X_{/T}`, the value at `f` of the functor
> `completionModificationFunctor` of Stacks 0AR5. Then `f` is quasi-separated (Stacks 03HL,
> part (3)) if and only if `g` is quasi-separated (Stacks 0ARN, part (2)).

```lean
theorem isQuasiSeparated_iff_hasQuasiCompactDiagonal_of_overIso
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hXN : Space.IsLocallyNoetherian B S hS X)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (M : Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ))
    {W : FppfSheaf B S hS} (g : W ⟶ Space.completionSheaf B S hS X T)
    (e : Over.mk g ≅ Over.mk (Space.completionSheafMap B S hS M.obj.hom T)) :
    Space.IsQuasiSeparated B S hS M.obj.hom ↔ HasQuasiCompactDiagonal B S hS g
```

## Tag 0ARW, a lemma

[Tag 0ARW](https://stacks.math.columbia.edu/tag/0ARW) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isSeparated_iff_isSeparatedMorphism_and_isRigSurjective_diagonal_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ModificationOutputSeparated.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ModificationOutputSeparated.lean#L242). The attribute's comment: “the correspondence `f ↔ g` of Theorem 0ARB is rendered as an isomorphism over `X_{/T}` between the image `f_{/T}` of `f` under the completion functor of Stacks 0AR5 and an object `g` of the right-hand category of Stacks 0AR5; the equivalence of Theorem 0ARB itself is not used. Separatedness of `g` is the separatedness axiom of Stacks 0ARN, part (1)”.

> **Stacks 0ARW.** Let `X` be a locally Noetherian algebraic space over `S`, let `T ⊆ |X|` be
> closed with open complement `U`, and let `f : X' ⟶ X` be a finite-type modification of `X`
> outside `U` (Stacks 0AS2), corresponding to an object `g : W ⟶ X_{/T}` of the right-hand
> category of Stacks 0AR5 — a rig-étale morphism with `W` a locally Noetherian formal algebraic
> space — through an isomorphism over `X_{/T}` between `f_{/T}` and `g`. Then `f` is separated if
> and only if `g` is separated (Stacks 0ARN) and its relative diagonal
> `Δ_g : W ⟶ W ×_{X_{/T}} W` is rig-surjective.

```lean
theorem isSeparated_iff_isSeparatedMorphism_and_isRigSurjective_diagonal_of_iso
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hXN : Space.IsLocallyNoetherian B S hS X)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (M : Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ))
    (P : RigEtaleOverCompletion B S hS X T)
    (e : (Space.completionOverFunctor B S hS T).obj M.obj ≅ P.obj) :
    Space.IsSeparated B S hS M.obj.hom ↔
      IsSeparatedMorphism B S hS P.obj.hom ∧
        IsRigSurjective B S hS (pullback.diagonal P.obj.hom)
```

## Tag 0ARX, a lemma

[Tag 0ARX](https://stacks.math.columbia.edu/tag/0ARX) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isProper_iff_isFormalModification_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ModificationOutputProper.lean, line 820](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ModificationOutputProper.lean#L820). The attribute's comment: “the correspondence `f ↔ g` of Theorem 0ARB is rendered as an isomorphism over `X_{/T}` between the image `f_{/T}` of `f` under the completion functor of Stacks 0AR5 and an object `g` of the right-hand category of Stacks 0AR5; the equivalence of Theorem 0ARB itself is not used”.

> Let `X` be a locally Noetherian algebraic space over `S`, let `T ⊆ |X|` be closed with open
> complement `U`, and let `f : X' ⟶ X` be a finite-type modification of `X` outside `U`
> (Stacks 0AS2), corresponding to an object `g : W ⟶ X_{/T}` of the right-hand category of
> Stacks 0AR5 — a rig-étale morphism with `W` a locally Noetherian formal algebraic space — through
> an isomorphism over `X_{/T}` between `f_{/T}` and `g`. Then `f` is proper if and only if `g` is a
> formal modification (Definition 0GDK).

```lean
theorem isProper_iff_isFormalModification_of_iso
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hXN : Space.IsLocallyNoetherian B S hS X)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (M : Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ))
    (P : RigEtaleOverCompletion B S hS X T)
    (e : (Space.completionOverFunctor B S hS T).obj M.obj ≅ P.obj) :
    Space.IsProper B S hS M.obj.hom ↔ IsFormalModification B S hS P.obj.hom
```

## Tag 0GI4, a lemma

[Tag 0GI4](https://stacks.math.columbia.edu/tag/0GI4) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isEtale_iff_isRepresentableEtale_of_overIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionEtaleIff.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionEtaleIff.lean#L75).

> **Stacks 0GI4.** Let `X` be a locally Noetherian algebraic space over `S`, let `T ⊆ |X|` be
> a closed subset and let `U ⊂ X` be the open subspace with `|U| = |X| ∖ T`. Let `f : X' ⟶ X` be
> a morphism of algebraic spaces which is locally of finite type and such that `f⁻¹U ⟶ U` is an
> isomorphism, and let `g : W ⟶ X_{/T}` correspond to `f` under the equivalence of Stacks 0ARB,
> that is, be isomorphic over `X_{/T}` to `f_{/T} : X'_{/T'} ⟶ X_{/T}`. Then `f` is étale if and
> only if `g` is étale.

```lean
theorem isEtale_iff_isRepresentableEtale_of_overIso
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hXN : Space.IsLocallyNoetherian B S hS X)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (M : Space.FiniteTypeModification B S hS (Space.openSubspaceOfPoints B S hS X Tᶜ))
    {W : FppfSheaf B S hS} (g : W ⟶ Space.completionSheaf B S hS X T)
    (e : Over.mk g ≅ Over.mk (Space.completionSheafMap B S hS M.obj.hom T)) :
    Space.IsEtale B S hS M.obj.hom ↔ IsRepresentableEtale B S hS g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.28, Tag 0GDS](https://stacks.math.columbia.edu/tag/0GDS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

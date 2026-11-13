---
declaration: section
origin: cited
lean: AlgebraicGeometry.LocallyNoetherianOver.existsUnique_isAlgebraicSpace_restriction_iso
statement: formalized
proof: formalized
---

# 98.26 Algebraic spaces in the Noetherian setting

Section 98.26 of the Stacks Project, [Tag 0GE6](https://stacks.math.columbia.edu/tag/0GE6). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GE7, a proposition

[Tag 0GE7](https://stacks.math.columbia.edu/tag/0GE7) in the Stacks Project.

**`AlgebraicGeometry.LocallyNoetherianOver.existsUnique_isAlgebraicSpace_restriction_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Artin/LocallyNoetherianAlgebraicSpaceCriterion.lean, line 1039](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Artin/LocallyNoetherianAlgebraicSpaceCriterion.lean#L1039).

> **Stacks 0GE7.** Let `S` be a locally Noetherian scheme and let `F` be a set-valued functor
> on the locally Noetherian étale site `(Noetherian/S)_étale`. If the diagonal
> `Δ : F ⟶ F × F` is representable (Categories 001X), `F` satisfies Artin's axioms `[-1]`,
> `[0]`, `[1]`, `[2]`, `[3]`, `[4]`, `[5]` in the form of Section 0GE6, and the local rings of
> `S` at its finite type points are G-rings, then there is a limit preserving algebraic space `F'`
> on the big fppf site `(Sch/S)_fppf` whose restriction to `(Noetherian/S)_étale` is `F`, and it is
> unique: two such are identified by a unique isomorphism compatible with the identifications of
> their restrictions with `F`.
>
> The extension is the one of Stacks 0GE3, its diagonal is representable by Stacks 0GE5, the
> axioms `[-1]`, `[2]`, `[3]`, `[4]`, `[5]` pass to it because they only involve locally Noetherian
> test objects, and Stacks 07Y1 shows it is an algebraic space.

```lean
theorem existsUnique_isAlgebraicSpace_restriction_iso [IsLocallyNoetherian S]
    (F : (LocallyNoetherianOver B S hS)ᵒᵖ ⥤ Type u)
    (hdiag : (yoneda (C := LocallyNoetherianOver B S hS)).relativelyRepresentable (diag F))
    (hax : SatisfiesArtinAxioms B S hS F)
    (hG : ∀ s : S, IsFiniteTypePoint s → IsGRing (S.presheaf.stalk s)) :
    (∃ F' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u, IsAlgebraicSpace B S hS F' ∧
        LimitPreserving.{u, u, u, u, u + 1, u} (BigFppfOver.toScheme B S hS) F' ∧
        Nonempty ((LocallyNoetherianOver.toBigFppfOver B S hS).op ⋙ F' ≅ F)) ∧
      ∀ (F₁ F₂ : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u),
        IsAlgebraicSpace B S hS F₁ → IsAlgebraicSpace B S hS F₂ →
        LimitPreserving.{u, u, u, u, u + 1, u} (BigFppfOver.toScheme B S hS) F₁ →
        LimitPreserving.{u, u, u, u, u + 1, u} (BigFppfOver.toScheme B S hS) F₂ →
        ∀ (e₁ : (LocallyNoetherianOver.toBigFppfOver B S hS).op ⋙ F₁ ≅ F)
          (e₂ : (LocallyNoetherianOver.toBigFppfOver B S hS).op ⋙ F₂ ≅ F),
        ∃! e : F₁ ≅ F₂,
          Functor.isoWhiskerLeft (LocallyNoetherianOver.toBigFppfOver B S hS).op e ≪≫ e₂ = e₁
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.26, Tag 0GE6](https://stacks.math.columbia.edu/tag/0GE6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

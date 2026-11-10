---
declaration: section
origin: cited
lean: Stacks.Thickenings.FlatDeformation.exists_addTorsor_classes, Stacks.Thickenings.flatThickeningAutEquiv
statement: formalized
proof: formalized
---

# 91.8 Deformations of schemes

Section 91.8 of the Stacks Project, [Tag 0D13](https://stacks.math.columbia.edu/tag/0D13). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D14, a lemma

[Tag 0D14](https://stacks.math.columbia.edu/tag/0D14) in the Stacks Project.

**`Stacks.Thickenings.FlatDeformation.exists_addTorsor_classes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FlatDeformation/Torsor.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FlatDeformation/Torsor.lean#L223). References: SGA 7 VI (4.16), “(b), special case”.

> Let `S ⊂ S'` be a first order thickening of schemes (`t : S ⟶ S'` a closed immersion whose
> ideal sheaf squares to zero) and let `f : X ⟶ S` be flat. Suppose there exist a flat morphism
> `f' : X' ⟶ S'` and an isomorphism `a : X ≅ X' ×_{S'} S` over `S` (a `FlatDeformation t f`,
> recording `a` through `i = pr₁ ∘ a` and the cartesian square `IsPullback i f f' t`;
> `FlatDeformation.ofPair` and `FlatDeformation.a` pass between the two). Then the set of isomorphism
> classes of such pairs (`FlatDeformation.Classes t f`; by `FlatDeformation.nonempty_iso_iff` two
> pairs are isomorphic exactly when there is `e : X'₁ ≅ X'₂` over `S'` with `(e ×_{S'} S) ∘ a₁ = a₂`)
> is principal homogeneous under `Ext¹_{𝒪_X}(NL_{X/S}, f^*𝒞_{S/S'})`
> (`Scheme.naiveCotangentExt f _ 1`, with `pullbackConormalModule f t = f^*𝒞_{S/S'}`).
>
> The action is as follows: a pair is the same thing as a solution of the square-zero extension
> problem
> `0 ⟶ f^*𝒞_{S/S'} ⟶ 𝒪_{X'} ⟶ 𝒪_X ⟶ 0` over `0 ⟶ 𝒞_{S/S'} ⟶ 𝒪_{S'} ⟶ 𝒪_S ⟶ 0`
> (`solutionOf`, with the ideal of `X` in `X'` identified with `f^*𝒞_{S/S'}` by
> [Stacks Project, Tag 063Y]), and `ξ` sends the class of `(f'₁, a₁)` to the class of `(f'₂, a₂)`
> exactly when the obstruction class of [Stacks Project, Tag 08UG] separating the two solutions is
> `ξ`, which is the action of [Stacks Project, Tag 08UK]. The relation is independent of the
> reference pair `D₀` used to write down the extension problem.

```lean
theorem exists_addTorsor_classes [Flat f]
    (hne : Nonempty (FlatDeformation t f)) :
    ∃ T : AddTorsor (Scheme.naiveCotangentExt f (pullbackConormalModule f t) 1)
        (Classes t f),
      ∀ (ξ : Scheme.naiveCotangentExt f (pullbackConormalModule f t) 1)
        (D₀ D₁ D₂ : FlatDeformation t f),
        T.vadd ξ (Quotient.mk (setoid t f) D₁) = Quotient.mk (setoid t f) D₂ ↔
          CompatibleFirstOrderThickening.pairObstruction (solutionOf hst D₀ D₁)
              (solutionOf hst D₀ D₂) =
            extIso f (pullbackConormalModule f t) 1 ξ
```

**`Stacks.Thickenings.flatThickeningAutEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FlatThickeningAutomorphisms.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FlatThickeningAutomorphisms.lean#L488).

> **[Stacks Project, Tag 0D14], part (2).** Let `S ⊂ S'` be a first order thickening of
> schemes, let `f : X ⟶ S` be a morphism, let `f' : X' ⟶ S'` be flat and let `i : X ⟶ X'` make the
> square cartesian, so that `X = X' ×_{S'} S` over `S`.  Then the set of automorphisms
> `φ : X' ⟶ X'` over `S'` which reduce to the identity on `X' ×_{S'} S` is
>
> `Ext⁰_{𝒪_X}(NL_{X/S}, f^*𝒞_{S/S'})`.
>
> The bijection is not merely asserted: its value on a class `ξ` is the morphism
> `Stacks.Thickenings.autOfHom` for the `𝒪_X`-linear map
> `Stacks.Thickenings.flatThickeningActingGroupAddEquiv ... ξ : Ω_{X/S} ⟶ 𝒞_{X/X'}`, whose
> comorphism is `g ↦ g + α(d_{X/S}(i^♯ g))` by
> `Stacks.Thickenings.flatThickeningAutEquiv_apply_appLE`.  In particular the identity
> automorphism corresponds to `0` (`Stacks.Thickenings.autOfHom_zero`) and composition to
> addition (`Stacks.Thickenings.autOfHom_add`), so the bijection is an isomorphism of groups.

```lean
def flatThickeningAutEquiv (i : X ⟶ X') (t : S ⟶ S')
    [AlgebraicGeometry.IsClosedImmersion t] (f : X ⟶ S) (f' : X' ⟶ S') [Flat f']
    (hst : t.ker ^ 2 = ⊥) (sq : IsPullback i f f' t) :
    AlgebraicGeometry.Scheme.naiveCotangentExt f (pullbackConormalModule f t) 0 ≃
      {φ : X' ≅ X' // i ≫ φ.hom = i ∧ φ.hom ≫ f' = f'}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.8, Tag 0D13](https://stacks.math.columbia.edu/tag/0D13)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

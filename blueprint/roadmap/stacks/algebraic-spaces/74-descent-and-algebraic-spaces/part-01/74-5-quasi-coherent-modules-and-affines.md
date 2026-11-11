---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.affineEtaleRestriction_isEquivalence, AlgebraicGeometry.Space.affineEtaleToSmallEtale, AlgebraicGeometry.Space.isIso_restrictionBaseChange_of_isQuasicoherentOnSite, AlgebraicGeometry.Space.affineEtale_quasicoherent_tfae
statement: formalized
proof: formalized
---

# 74.5 Quasi-coherent modules and affines

Section 74.5 of the Stacks Project, [Tag 0H02](https://stacks.math.columbia.edu/tag/0H02). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0H03, an equation

[Tag 0H03](https://stacks.math.columbia.edu/tag/0H03) in the Stacks Project.

**`AlgebraicGeometry.Space.affineEtaleRestriction_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleRingedTopos.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleRingedTopos.lean#L130). The attribute's comment: “equivalence of topoi”.

> Restriction from the small étale site of an algebraic space to its affine étale charts is an
> equivalence on sheaves of sets, at the universe of the objects of the site.

```lean
theorem affineEtaleRestriction_isEquivalence :
    (affineEtaleRestriction B S hS F hF (Type (u + 1))).IsEquivalence
```

**`AlgebraicGeometry.Space.affineEtaleToSmallEtale`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleRingedTopos.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleRingedTopos.lean#L145). The attribute's comment: “canonical morphism of ringed topoi”.

> The canonical morphism from the affine étale ringed topos of an algebraic space to its small
> étale ringed topos.
>
> Its inverse image is restriction to affine charts and is an equivalence, and its structure map
> is an isomorphism which, after forgetting the ring operations, is the identity of the restricted
> structure sheaf.

```lean
noncomputable def affineEtaleToSmallEtale :
    { f : RingedToposHom
        (affineEtaleRingedTopos B S hS F hF)
        (liftedSmallEtaleRingedTopos B S hS F) //
      f.toToposHom.inverseImage =
        affineEtaleRestriction B S hS F hF (Type (u + 1)) ∧
      f.toToposHom.inverseImage.IsEquivalence ∧
      IsIso f.fSharpInverseImage ∧
      HEq ((affineEtaleRingedTopos B S hS F hF).forgetRing.map
        f.fSharpInverseImage)
        (𝟙 ((affineEtaleRingedTopos B S hS F hF).forgetRing.obj
          (affineEtaleRingedTopos B S hS F hF).O)) }
```

## Tag 0H04, a lemma

[Tag 0H04](https://stacks.math.columbia.edu/tag/0H04) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_restrictionBaseChange_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleCartesianModules.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleCartesianModules.lean#L241). The attribute's comment: “quasi-coherent implies cartesian”.

> A quasi-coherent sheaf of modules on the affine étale site of an algebraic space is
> cartesian: each restriction map exhibits its target as a base change of its source.

```lean
theorem isIso_restrictionBaseChange_of_isQuasicoherentOnSite
    (M : SheafOfModules.{max m (u + 1)} (affineEtaleRingSheaf B S hS F hF))
    (hM : M.IsQuasicoherentOnSite)
    {U V : AffineEtale B S hS F} (f : U ⟶ V) :
    IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u + 1, m} M.val f.op)
```

**`AlgebraicGeometry.Space.affineEtale_quasicoherent_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentModules.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/AffineEtaleQuasicoherentModules.lean#L270). The attribute's comment: “the equivalence of (1), (2) and (3)”.

> **Stacks 0H04.**  Let `F` be an algebraic space over a scheme `S` and let `𝓕` be a presheaf
> of `𝒪_F`-modules on the affine étale site of `F`.  The following are equivalent:
>
> 1. for every morphism `U ⟶ U'` of `F_{affine, étale}` the base-change map
>    `𝓕(U') ⊗_{𝒪_F(U')} 𝒪_F(U) ⟶ 𝓕(U)` is an isomorphism;
> 2. `𝓕` is a sheaf and is quasi-coherent on the ringed site `(F_{affine, étale}, 𝒪_F)` in the
>    sense of Modules on Sites, Definition 03DL (6);
> 3. `𝓕` is a sheaf and corresponds, under the equivalence of Stacks 0H03, to a quasi-coherent
>    `𝒪_F`-module on the small étale site of `F`.
>
> Conditions (2) and (3) carry the sheaf condition as a conjunct, because quasi-coherence is a
> condition on a sheaf of modules; the source's proof of (1) ⇒ (2) likewise begins by proving the
> sheaf condition.
>
> (1) ⇒ (2) is `AlgebraicGeometry.Space.isQuasicoherentOnSite_of_isIso_restrictionBaseChange`,
> (2) ⇒ (1) is `AlgebraicGeometry.Space.isIso_restrictionBaseChange_of_isQuasicoherentOnSite`, and
> (2) ⇔ (3) is
> `AlgebraicGeometry.Space.isQuasicoherentOnSite_affineEtaleLiftedModuleRestriction_iff` together
> with the essential surjectivity of restriction to the affine charts.

```lean
theorem affineEtale_quasicoherent_tfae
    (M : PresheafOfModules.{u + 1}
      ((affineEtaleStructureSheaf B S hS F hF).obj ⋙ forget₂ CommRingCat RingCat)) :
    List.TFAE
      [∀ (U V : AffineEtale B S hS F) (f : U ⟶ V),
          IsIso (Stacks.PresheafOfModules.restrictionBaseChange.{u + 1, u, u + 1, u + 1} M f.op),
        ∃ h : Presheaf.IsSheaf (AffineEtale.topology B S hS F) M.presheaf,
          (⟨M, h⟩ : SheafOfModules.{u + 1}
            (affineEtaleRingSheaf B S hS F hF)).IsQuasicoherentOnSite,
        ∃ h : Presheaf.IsSheaf (AffineEtale.topology B S hS F) M.presheaf,
          ∃ G : SheafOfModules.{u + 1} (liftedSmallEtaleRingSheaf B S hS F),
            G.IsQuasicoherentOnSite ∧
              Nonempty ((affineEtaleLiftedModuleRestriction B S hS F hF).obj G ≅ ⟨M, h⟩)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.5, Tag 0H02](https://stacks.math.columbia.edu/tag/0H02)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

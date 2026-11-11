---
declaration: section
origin: cited
lean: CategoryTheory.Functor.whiskeringLeft, CategoryTheory.Functor.sheafPushforwardContinuous, AlgebraicGeometry.smallEtaleUnderlyingSetCommutes, CategoryTheory.Functor.isIso_mateEquiv_sheafAdjunctionContinuous, CategoryTheory.Adjunction.leftExactWhiskerRight, Stacks.Presheaf.AbelianVersusSets.not_universally_agrees
statement: formalized
proof: formalized
---

# 7.44 Sheaves of algebraic structures

Section 7.44 of the Stacks Project, [Tag 00YR](https://stacks.math.columbia.edu/tag/00YR). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00YS, a definition

[Tag 00YS](https://stacks.math.columbia.edu/tag/00YS) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.whiskeringLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.whiskeringLeft#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Pushforward.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Pushforward.lean#L25) (StacksFrontier): “`u^p F (U) = F(u U)` on presheaves, i.e. precomposition with `u.op`”. References: EGA III (7.1.3), “partial”.
- [`CategoryTheory.Functor.sheafPushforwardContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Pushforward.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Pushforward.lean#L27) (StacksFrontier): “`f_* F (U) = F(u U)` on sheaves, by the same rule”. References: SGA 4 IV (4.9.1).

## Tag 00YT, a lemma

[Tag 00YT](https://stacks.math.columbia.edu/tag/00YT) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleUnderlyingSetCommutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean#L95). The attribute's comment: “the forgetful functor from abelian groups to sets, on the small étale sites over X: inverse image along small étale base change commutes with passing to the underlying sheaf of sets”.

> On the small étale sites of the objects of `B` over `X`, inverse image along small étale base
> change to any `T ⟶ X` commutes with passing from an abelian sheaf to its underlying sheaf of
> sets.

```lean
public theorem smallEtaleUnderlyingSetCommutes : SmallEtaleUnderlyingSetCommutes B X
```

**`CategoryTheory.Functor.isIso_mateEquiv_sheafAdjunctionContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Sheaves.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Sheaves.lean#L405). The attribute's comment: “The sheaf level, for an arbitrary `s : A ⥤ B`: for a continuous, representably flat `u : C ⥤ D` and a functor `s` preserving filtered colimits and sheafification, the pullback `f^{-1}` of `A`-valued sheaves commutes with postcomposition by `s`, in that the canonical mate `f^{-1}(s ∘ F) ⟶ s ∘ (f^{-1} F)` of the pushforward square is an isomorphism. The tag is the case `B = Type u`, `s` the underlying-set functor of a type of algebraic structure. The presheaf level, `u_p (F ⋙ s) ≅ (u_p F) ⋙ s`, is `lanCompIsoOfPreserves` at `L = u.op`, which mentions no topology.”. References: SGA 4 III (1.7), “4) diagram commutes”; SGA 4 III (2.4), “underlying sheaf of sets”; SGA 4 IV (3.1.2), “u^* preserves structures”.

> Let `(C, J)` and `(D, K)` be sites, let `u : C ⥤ D` be continuous and representably flat —
> the latter holds under the hypotheses of Stacks 00X6 — and let `s : A ⥤ B` be a functor such that
> `A` and `B` have filtered colimits, `s` preserves them, `A`- and `B`-valued presheaves on `D` can
> be sheafified, sheafification commutes with `s`, and an `A`-valued presheaf is a sheaf as soon as
> its image under `s` is.
>
> Then the pullback functor `f^{-1}` on `A`-valued sheaves commutes with postcomposition by `s`:
> the mate, under the adjunction `f^{-1} ⊣ f_*`, of the identity square expressing that the
> pushforward `f_* = u^s` is restriction along `u.op` on both sides, namely the canonical map
> `f^{-1}(s ∘ F) ⟶ s ∘ (f^{-1} F)`, is an isomorphism.
>
> For `B = Type u` and `s` the underlying-set functor of a type of algebraic structure, this says
> that the pullback of sheaves of algebraic structures commutes with taking the underlying sheaf of
> sets.
>
> At the level of presheaves the corresponding assertion, that `u_p` commutes with postcomposition
> by `s`, is `Functor.lanCompIsoOfPreserves` for `L = u.op`, which needs neither topology.

```lean
public theorem isIso_mateEquiv_sheafAdjunctionContinuous {C : Type u} [SmallCategory C]
    {D : Type u} [SmallCategory D] (u : C ⥤ D) (J : GrothendieckTopology C)
    (K : GrothendieckTopology D) [u.IsContinuous J K] [RepresentablyFlat u] {A : Type w}
    [Category.{v} A] {B : Type w'} [Category.{v'} B] (s : A ⥤ B)
    [HasFilteredColimitsOfSize.{u, u} A] [HasFilteredColimitsOfSize.{u, u} B]
    [PreservesFilteredColimitsOfSize.{u, u} s] [HasWeakSheafify K A] [HasWeakSheafify K B]
    [J.HasSheafCompose s] [K.HasSheafCompose s] [K.PreservesSheafification s] :
    IsIso
      ((mateEquiv (u.sheafAdjunctionContinuous A J K) (u.sheafAdjunctionContinuous B J K)).symm
          (TwoSquare.mk (u.sheafPushforwardContinuous A J K) (sheafCompose K s) (sheafCompose J s)
            (u.sheafPushforwardContinuous B J K) (𝟙 _))).natTrans
```

## Tag 00YV, a proposition

[Tag 00YV](https://stacks.math.columbia.edu/tag/00YV) in the Stacks Project.

**`CategoryTheory.Adjunction.leftExactWhiskerRight`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Sheaves.lean, line 550](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Sheaves.lean#L550). The attribute's comment: “Stated for an arbitrary theory `T` of algebraic structures defined by finite projective limits — structures of type `T` in `E` being the left exact functors `T ⥤ E` — rather than for the seven listed types of algebraic structure separately, and for an arbitrary adjunction between left exact functors rather than for a morphism of topoi: postcomposition with `f⁻¹` and with `f_*` is an adjoint pair on structures, compatible with taking the underlying sheaf of sets by construction.”. References: SGA 4 IV (3.1.2), “finite proj lim structs”; SGA 4 III (1.7), “special case”.

> Let `T` be a theory of algebraic structures defined by finite projective limits, so that a
> structure of that type in a category `E` is a left exact functor `T ⥤ E`, its underlying object
> being its value at the sort. Let `f = (f⁻¹, f_*)` be a morphism of topoi, that is, an adjunction
> `f⁻¹ ⊣ f_*` whose left adjoint `f⁻¹` is left exact (the right adjoint `f_*` then being left exact
> for free).
>
> Then postcomposition with `f⁻¹` and with `f_*` are functors on structures of type `T`, and they
> form an adjoint pair. Since they are postcomposition, they commute with taking the underlying
> object — for `E`, `E'` categories of sheaves of sets, the underlying sheaf of sets — on the nose.

```lean
public noncomputable def leftExactWhiskerRight (T : Type u₁) [Category.{v₁} T] {E : Type u₂}
    [Category.{v₂} E] {E' : Type u₃} [Category.{v₃} E'] {f : E ⥤ₗ E'} {g : E' ⥤ₗ E}
    (adj : f.obj ⊣ g.obj) :
    (LeftExactFunctor.whiskeringRight T E E').obj f ⊣
      (LeftExactFunctor.whiskeringRight T E' E).obj g
```

## Tag 00YU, a remark

[Tag 00YU](https://stacks.math.columbia.edu/tag/00YU) in the Stacks Project.

**`Stacks.Presheaf.AbelianVersusSets.not_universally_agrees`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/AbelianVersusSetsCounterexample.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/AbelianVersusSetsCounterexample.lean#L159).

> **Main Statement (Tag 00YU).** Agreement does not hold in general: there
> exist categories `C`, `D`, a functor `u : C ⥤ D`, a presheaf of abelian groups
> `F` on `C`, and an object `V` of `D` such that the comparison map `θ_{F,V}` is
> *not* a bijection.

```lean
theorem not_universally_agrees :
    ∃ (C D : Type) (_ : SmallCategory C) (_ : SmallCategory D) (u' : C ⥤ D)
      (F : Cᵒᵖ ⥤ AddCommGrpCat.{0}) (V : Dᵒᵖ),
      ¬ Function.Bijective ((theta u' F).app V)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.44, Tag 00YR](https://stacks.math.columbia.edu/tag/00YR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

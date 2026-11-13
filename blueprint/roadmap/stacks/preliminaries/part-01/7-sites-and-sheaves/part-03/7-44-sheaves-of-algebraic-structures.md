---
declaration: section
origin: cited
lean: CategoryTheory.Functor.whiskeringLeft, CategoryTheory.Functor.sheafPushforwardContinuous, AlgebraicGeometry.smallEtaleUnderlyingSetCommutes, CategoryTheory.Functor.isIso_mateEquiv_sheafAdjunctionContinuous, Stacks.Topos.toposAlgebraicStructureAdjunctions, Stacks.Topos.algebraicStructureSheafification, Stacks.Presheaf.AbelianVersusSets.uShriekAb, Stacks.Presheaf.AbelianVersusSets.uShriekAbAdjunction
statement: formalized
proof: formalized
---

# 7.44 Sheaves of algebraic structures

Section 7.44 of the Stacks Project, [Tag 00YR](https://stacks.math.columbia.edu/tag/00YR). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00YS, a definition

[Tag 00YS](https://stacks.math.columbia.edu/tag/00YS) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.whiskeringLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.whiskeringLeft#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Pushforward.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Pushforward.lean#L25) (StacksFrontier): “`u^p F (U) = F(u U)` on presheaves, i.e. precomposition with `u.op`”. References: EGA III (7.1.3), “partial”.
- [`CategoryTheory.Functor.sheafPushforwardContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPushforwardContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Pushforward.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Pushforward.lean#L27) (StacksFrontier): “`f_* F (U) = F(u U)` on sheaves, by the same rule”. References: SGA 4 IV (4.9.1).

## Tag 00YT, a lemma

[Tag 00YT](https://stacks.math.columbia.edu/tag/00YT) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleUnderlyingSetCommutes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StrongSerreAbelian.lean#L95). The attribute's comment: “the forgetful functor from abelian groups to sets, on the small étale sites over X: inverse image along small étale base change commutes with passing to the underlying sheaf of sets”.

> On the small étale sites of the objects of `B` over `X`, inverse image along small étale base
> change to any `T ⟶ X` commutes with passing from an abelian sheaf to its underlying sheaf of
> sets.

```lean
public theorem smallEtaleUnderlyingSetCommutes : SmallEtaleUnderlyingSetCommutes B X
```

**`CategoryTheory.Functor.isIso_mateEquiv_sheafAdjunctionContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Sheaves.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/Sheaves.lean#L405). The attribute's comment: “The sheaf level, for an arbitrary `s : A ⥤ B`: for a continuous, representably flat `u : C ⥤ D` and a functor `s` preserving filtered colimits and sheafification, the pullback `f^{-1}` of `A`-valued sheaves commutes with postcomposition by `s`, in that the canonical mate `f^{-1}(s ∘ F) ⟶ s ∘ (f^{-1} F)` of the pushforward square is an isomorphism. The tag is the case `B = Type u`, `s` the underlying-set functor of a type of algebraic structure. The presheaf level, `u_p (F ⋙ s) ≅ (u_p F) ⋙ s`, is `lanCompIsoOfPreserves` at `L = u.op`, which mentions no topology.”. References: SGA 4 III (1.7), “4) diagram commutes”; SGA 4 III (2.4), “underlying sheaf of sets”; SGA 4 IV (3.1.2), “u^* preserves structures”.

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
            (u.sheafPushforwardContinuous B J K) (𝟙 _)))
```

## Tag 00YV, a proposition

[Tag 00YV](https://stacks.math.columbia.edu/tag/00YV) in the Stacks Project.

**`Stacks.Topos.toposAlgebraicStructureAdjunctions`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/AlgebraicStructureAdjunctions.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/AlgebraicStructureAdjunctions.lean#L96). The attribute's comment: “The adjoint pairs for the seven listed types, each compatible with the underlying sheaves of sets: the underlying sheaf of sets of `f⁻¹ F`, resp. `f_* G`, is `f⁻¹`, resp. `f_*`, of the underlying sheaf of sets, and the unit is the unit of `f⁻¹ ⊣ f_*` on sheaves of sets. Rings are commutative rings; the module case is stated for an arbitrary ring `R`. The final assertion, (α)–(ζ) for each type, is `Stacks.Topos.algebraicStructureSheafification`.”.

> **Stacks 00YV.** Let `C`, `D` be sites and let `f = (f⁻¹, f_*)` be a morphism of topoi
> `Sh(C) → Sh(D)`. Then `f` gives an adjoint pair of functors `(f⁻¹, f_*)` on sheaves of algebraic
> structures compatible with taking the underlying sheaves of sets, for pointed sets, abelian
> groups, groups, monoids, rings, modules over a fixed ring `R` and Lie algebras over a fixed field
> `k`.

```lean
noncomputable def toposAlgebraicStructureAdjunctions
    (f : MorphismOfTopoi (Sheaf J (Type u)) (Sheaf K (Type u))) (R : Type u) [Ring R]
    (k : Type u) [Field k] : AlgebraicStructureAdjunctions f R k
```

**`Stacks.Topos.algebraicStructureSheafification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/AlgebraicStructureAdjunctions.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/AlgebraicStructureAdjunctions.lean#L135). The attribute's comment: “The final assertion: (α)–(ζ) hold for each of the seven listed types, on any site (`Stacks.Sites.SheafificationProperties`). The adjoint pairs themselves are `Stacks.Topos.toposAlgebraicStructureAdjunctions`.”.

> **Stacks 00YV, final assertion.** On any site, for each of the seven types of algebraic
> structures of Stacks 00YV, the properties (α)–(ζ) of sheafification hold: a presheaf is a sheaf
> if and only if its underlying presheaf of sets is; `P# = (P⁺)⁺` is a sheaf; sheafification
> commutes with taking underlying presheaves of sets; `P ⟶ P#` is an isomorphism exactly when `P`
> is a sheaf; sheafification is left adjoint to the inclusion; and sheafification is left exact.

```lean
noncomputable def algebraicStructureSheafification (J : GrothendieckTopology C) (R : Type u)
    [Ring R] (k : Type u) [Field k] : AlgebraicStructureSheafification J R k
```

## Tag 00YU, a remark

[Tag 00YU](https://stacks.math.columbia.edu/tag/00YU) in the Stacks Project.

**`Stacks.Presheaf.AbelianVersusSets.uShriekAb`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/AbelianVersusSetsCounterexample.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/AbelianVersusSetsCounterexample.lean#L135). The attribute's comment: “`u_p^{ab}` is defined on abelian presheaves by the same colimits as `u_p` on presheaves of sets: both are the pointwise left Kan extension along `uᵒᵖ`.”.

> **Definition 4 (the functor `u_p^{ab}` on presheaves of abelian groups).**
> The left adjoint of `u^p` on abelian presheaves, equivalently the left Kan
> extension along `uᵒᵖ`; its pointwise value is the *same* colimit diagram, now
> taken in `Ab`.

```lean
noncomputable def uShriekAb (u' : C ⥤ D) :
    (Cᵒᵖ ⥤ AddCommGrpCat.{u}) ⥤ (Dᵒᵖ ⥤ AddCommGrpCat.{u})
```

**`Stacks.Presheaf.AbelianVersusSets.uShriekAbAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/AbelianVersusSetsCounterexample.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/AbelianVersusSetsCounterexample.lean#L147). The attribute's comment: “`u_p^{ab}` is left adjoint to `u^p` on the categories of abelian presheaves.”.

> Adjointness `u_p^{ab} ⊣ u^p` on presheaves of abelian groups (Stacks
> Remark 00VF, and Stacks 00YU).

```lean
noncomputable def uShriekAbAdjunction (u' : C ⥤ D) :
    uShriekAb u' ⊣ uPullbackAb u'
```

**`Stacks.Presheaf.AbelianVersusSets.exists_isMorphismOfSites_not_bijective_theta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/AbelianVersusSetsMorphismOfSites.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Presheaf/AlgebraicStructure/AbelianVersusSetsMorphismOfSites.lean#L38). The attribute's comment: “Under the remark's hypothesis: a continuous functor defining a morphism of sites for which `u_p^{ab}` does not agree with `u_p` on underlying sets.”.

> **Stacks 00YU (Remark 7.44.4).** Even for a continuous functor defining a morphism of sites,
> `u_p^{ab}` need not agree with `u_p` on underlying presheaves of sets: there exist sites
> `(C, J)` and `(D, K)`, a continuous functor `u : C ⥤ D` which defines a morphism of sites
> (`u_s` exact, Stacks 00X1), a presheaf of abelian groups `F` on `C` and an object `V` of `D`
> such that the comparison map `θ_{F,V} : (u_p F^set)(V) → (u_p^{ab} F)(V)` is not a bijection.
>
> The witness is the empty functor from the empty category to the one-point category `PUnit`,
> which carries the topology `⊤` in which the empty family covers the point.

```lean
theorem exists_isMorphismOfSites_not_bijective_theta :
    ∃ (C D : Type) (_ : SmallCategory C) (_ : SmallCategory D)
      (J : GrothendieckTopology C) (K : GrothendieckTopology D) (u' : C ⥤ D),
      u'.IsMorphismOfSites J K ∧
        ∃ (F : Cᵒᵖ ⥤ AddCommGrpCat.{0}) (V : Dᵒᵖ),
          ¬ Function.Bijective ((theta u' F).app V)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.44, Tag 00YR](https://stacks.math.columbia.edu/tag/00YR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.isIso_tensorDualToEndomorphism_of_localSummand, Stacks.SheafOfModules.exactPairingDualSheafOfLocalSummand, Stacks.SheafOfModules.dualSheaf, Stacks.SheafOfModules.evaluation, Stacks.SheafOfModules.tensorDualToEndomorphism_toTensorSheafSection, Stacks.SheafOfModules.dualSheafIsoOfLeftDual, Stacks.SheafOfModules.dualSheafIsoOfLeftDual_hom_val_app, Stacks.SheafOfModules.evaluation_eq_dualEval_dualSheafIsoOfLeftDual_inv
statement: formalized
proof: formalized
---

# 18.29 Duals

Section 18.29 of the Stacks Project, [Tag 0FNX](https://stacks.math.columbia.edu/tag/0FNX). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FNY, an example

[Tag 0FNY](https://stacks.math.columbia.edu/tag/0FNY) in the Stacks Project.

**`Stacks.SheafOfModules.isIso_tensorDualToEndomorphism_of_localSummand`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualRingedSite.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualRingedSite.lean#L194). The attribute's comment: “the map `ℱ ⊗ 𝓗om(ℱ,𝒪) ⟶ 𝓗om(ℱ,ℱ)` is an ISOMORPHISM, with the local hypothesis in the per-object form the tag states it in”. References: SGA 5 IIIB (5.0), “partial”.

> **Stacks Project, Tag 0FNY, first assertion.** For a sheaf of modules which is locally a
> direct summand of a finite free sheaf of modules, the canonical map
> `F ⊗_𝒪 SheafHom(F, 𝒪) ⟶ SheafHom(F, F)` is an isomorphism.
>
> The map is `Stacks.SheafOfModules.tensorDualToEndomorphism`, pinned down on local sections by
> `Stacks.SheafOfModules.tensorDualToEndomorphism_toTensorSheafSection`.

```lean
theorem isIso_tensorDualToEndomorphism_of_localSummand
    (hF : IsLocallyDirectSummandOfFiniteFree 𝒪 h𝒪 F) :
    IsIso (tensorDualToEndomorphism 𝒪 h𝒪 F)
```

**`Stacks.SheafOfModules.exactPairingDualSheafOfLocalSummand`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualRingedSite.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualRingedSite.lean#L211). The attribute's comment: “the LEFT-DUAL assertion: `𝓗om(ℱ,𝒪)` with the canonical coevaluation and evaluation satisfies the two triangle identities, with the local hypothesis in the per-object form the tag states it in”. References: SGA 5 IIIB (5.0), “5.0.3 iso”.

> **Stacks Project, Tag 0FNY, second assertion.** For a sheaf of modules `F` which is locally a
> direct summand of a finite free sheaf of modules, the dual `F^∨ = SheafHom(F, 𝒪)`, with the
> canonical coevaluation `η : 𝒪 ⟶ F ⊗ F^∨` and the canonical evaluation `ε : F^∨ ⊗ F ⟶ 𝒪`, is a
> **left dual** of `F` in the monoidal category of sheaves of `𝒪`-modules of Tag 01CA. That is, the
> two triangle identities hold.

```lean
noncomputable def exactPairingDualSheafOfLocalSummand
    (hF : IsLocallyDirectSummandOfFiniteFree 𝒪 h𝒪 F) :
    ExactPairing F (dualSheaf 𝒪 h𝒪 F)
```

**`Stacks.SheafOfModules.dualSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHom.lean, line 279](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHom.lean#L279). The attribute's comment: “the dual `SheafHom(ℱ, 𝒪)` whose left-dual property is the content of the tag; the construction is for an arbitrary site, so the ringed-space and the ringed-site tags name the same object”. References: SGA 3 III (0.6).

> **The dual of a sheaf of modules**, `F^∨ = SheafHom(F, 𝒪)`: the sheaf-hom into the
> structure sheaf.

```lean
noncomputable def dualSheaf
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪))
      :
    SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪)
```

**`Stacks.SheafOfModules.evaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHom.lean, line 695](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHom.lean#L695). The attribute's comment: “the evaluation map `ε : ℱ^∨ ⊗ ℱ ⟶ 𝒪`”.

> **The evaluation pairing of sheaves of modules**, `F^∨ ⊗_𝒪 F ⟶ 𝒪`. The tensor product of
> sheaves of modules is the sheafification of the pointwise one (Tag 05NA), so this is the
> morphism which `evaluationPresheaf` induces through the sheafification adjunction.

```lean
noncomputable def evaluation
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪))
      :
    ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, max u v, max u v, max u v}
      ⟨𝒪, Presheaf.isSheaf_of_isSheaf_comp J 𝒪
        (forget₂ CommRingCat RingCat) h𝒪⟩).obj (dualSheaf 𝒪 h𝒪 F)).obj F ⟶
      SheafOfModules.unit (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪)
```

**`Stacks.SheafOfModules.tensorDualToEndomorphism_toTensorSheafSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean, line 646](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean#L646). The attribute's comment: “the map `ℱ ⊗ 𝓗om(ℱ,𝒪) ⟶ 𝓗om(ℱ,ℱ)` read on sections, which pins it down”.

> **The canonical morphism on a local pure tensor is the rank-one operator.** This pins the
> morphism down: its value on the image of `f ⊗ lam` is the endomorphism `g ↦ lam(g) • f`.

```lean
theorem tensorDualToEndomorphism_toTensorSheafSection
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪))
      (U : Cᵒᵖ)
    (f : F.val.obj U) (lam : (dualSheaf 𝒪 h𝒪 F).val.obj U) :
    ((tensorDualToEndomorphism 𝒪 h𝒪 F).val.app U).hom
        (toTensorSheafSection 𝒪 h𝒪 F (dualSheaf 𝒪 h𝒪 F) U
          (f ⊗ₜ[(Stacks.SheafOfModules.TensorSheafification.structureRingPresheaf 𝒪).obj U] lam)) =
      rankOneSection 𝒪 h𝒪 (U := U.unop) f lam
```

## Tag 0FNZ, a lemma

[Tag 0FNZ](https://stacks.math.columbia.edu/tag/0FNZ) in the Stacks Project.

**`Stacks.SheafOfModules.dualSheafIsoOfLeftDual`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualSheafHomIso.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualSheafHomIso.lean#L149). The attribute's comment: “(2), the isomorphism `𝓗om(ℱ,𝒪) ≅ 𝒢`; that it is the map `λ ↦ (λ ⊗ 1)(η)` of the tag is `dualSheafIsoOfLeftDual_hom_val_app`”.

> **Stacks Project, Tag 0FNZ (2).** A left dual `G` of a sheaf of `𝒪`-modules `F` on a ringed
> site is isomorphic to `SheafHom(F, 𝒪)`.
>
> Both `SheafHom(F, 𝒪)` and `G` are left duals of `F` — the first by
> `exactPairingDualSheafOfLeftDual` — and two left duals of one object are isomorphic through the
> adjoint mate of the identity. That this isomorphism is the map Tag 0FNZ (2) names, namely
> `λ ↦ (λ ⊗ 1)(η)`, is `dualSheafIsoOfLeftDual_hom_val_app`.

```lean
noncomputable def dualSheafIsoOfLeftDual : dualSheaf 𝒪 h𝒪 F ≅ G
```

**`Stacks.SheafOfModules.dualSheafIsoOfLeftDual_hom_val_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualSheafHomIso.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualSheafHomIso.lean#L210). The attribute's comment: “(2), that the isomorphism is the map `λ ↦ (λ ⊗ 1)(η)` the tag describes”.

> **Stacks Project, Tag 0FNZ (2), the formula for the isomorphism.** On an object `U` over
> which the coevaluation expands as `η(1) = ∑ fᵢ ⊗ gᵢ`, the isomorphism
> `SheafHom(F, 𝒪) ≅ G` of Tag 0FNZ (2) sends a local section `λ` to `∑ λ(fᵢ) • gᵢ`, which is
> `(λ ⊗ 1)(η)`. In particular that expression does not depend on the chosen expansion.
>
> Such an expansion exists on a covering of every object of the site, by
> `Stacks.SheafOfModules.exists_cover_localDualBasis_tensorSheaf`, so these formulas determine the
> isomorphism.

```lean
theorem dualSheafIsoOfLeftDual_hom_val_app (U : C) {n : ℕ}
    (f : Fin n → F.val.obj (op U)) (g : Fin n → G.val.obj (op U))
    (hη : (η_ F G).val.app (op U)
        (1 : (TensorSheafification.structureSheaf 𝒪 h𝒪).obj.obj (op U)) =
      ∑ i, tensorPt 𝒪 h𝒪 F G (op U) (f i) (g i))
    (lam : (dualSheaf 𝒪 h𝒪 F).val.obj (op U)) :
    (dualSheafIsoOfLeftDual 𝒪 h𝒪 F G).hom.val.app (op U) lam =
      ∑ i, dualEval lam (f i) • g i
```

**`Stacks.SheafOfModules.evaluation_eq_dualEval_dualSheafIsoOfLeftDual_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualSheafHomIso.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualSheafHomIso.lean#L254). The attribute's comment: “(3), the evaluation formula `ε(f, g) = e⁻¹(g)(f)`”.

> **Stacks Project, Tag 0FNZ (3).** Pairing a local section `g` of a left dual `G` of `F`
> against a local section `f` of `F` under the given evaluation `ε` is the value at `f` of the
> local homomorphism `e⁻¹(g) : F ⟶ 𝒪`, where `e` is the isomorphism of Tag 0FNZ (2).

```lean
theorem evaluation_eq_dualEval_dualSheafIsoOfLeftDual_inv (U : C)
    (y : G.val.obj (op U)) (x : F.val.obj (op U)) :
    (ε_ F G).val.app (op U) (tensorPt 𝒪 h𝒪 G F (op U) y x) =
      dualEval ((dualSheafIsoOfLeftDual 𝒪 h𝒪 F G).inv.val.app (op U) y) x
```

**`Stacks.SheafOfModules.exists_cover_retract_finiteFree_of_exactPairing_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorAssociatorSections.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorAssociatorSections.lean#L329). The attribute's comment: “local\_finite\_free\_summand”.

> Let `(C, O)` be a ringed site and let `F` be a sheaf of `O`-modules with a left dual `G` for
> the monoidal structure given by the tensor product sheaf. Then every object `U` of the site has
> a covering on whose members `F` restricts to a direct summand of a finite free module.

```lean
theorem exists_cover_retract_finiteFree_of_exactPairing_tensorSheaf
    [HasSheafify J AddCommGrpCat.{w}]
    [∀ V : C, HasWeakSheafify (J.over V) AddCommGrpCat.{w}]
    [∀ V : C, (J.over V).WEqualsLocallyBijective AddCommGrpCat.{w}]
    (p : ExactPairing F G) (U : C) :
    ∃ S : Sieve U, S ∈ J U ∧
      ∀ (V : C) (i : V ⟶ U), S i →
        ∃ I : Type w, Finite I ∧
          Nonempty (Retract (F.over V)
            (SheafOfModules.free (R := (Stacks.SheafOfModules.TensorSheafification.structureSheaf O
              hO).over V) I))
```

**`AlgebraicGeometry.Space.exists_cover_retract_finiteFree_of_exactPairing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleLeftDualLocalSummand.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleLeftDualLocalSummand.lean#L88). The attribute's comment: “(1), for the modules of an algebraic space”.

> **Stacks 0FNZ (1) for the `𝒪_F`-modules of an algebraic space.**  If an `𝒪_F`-module `M` has
> a left dual `N` in the monoidal category of `𝒪_F`-modules, then every object `U` of the small
> étale site of `F` has a covering on whose members `M` restricts to a direct summand of a free
> module on a finite index type.

```lean
theorem exists_cover_retract_finiteFree_of_exactPairing
    (M N : Modules.{u, u} B S hS F hF) (p : ExactPairing M N)
    (U : (smallEtaleRingedSite B S hS F hF).C) :
    ∃ T : Sieve U, T ∈ (smallEtaleRingedSite B S hS F hF).J U ∧
      ∀ (V : (smallEtaleRingedSite B S hS F hF).C) (i : V ⟶ U), T i →
        ∃ I : Type u, Finite I ∧
          Nonempty (Retract (M.over V)
            (SheafOfModules.free (R := (Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS F hF).O).over V) I))
```

## Tag 08FD, a lemma

[Tag 08FD](https://stacks.math.columbia.edu/tag/08FD) in the Stacks Project.

**`Stacks.SheafOfModules.exists_coveringSieve_retract_free`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatFiniteFreeSummand.lean, line 685](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatFiniteFreeSummand.lean#L685).

> On a ringed site, a sheaf of modules which is flat and locally of finite presentation is,
> locally on the site, a direct summand of a finite free sheaf of modules: every object `U`
> carries a covering sieve on each member `f : V ⟶ U` of which `F|_V` is a retract of
> `O_V^{⊕ I}` for some finite `I`.

```lean
theorem exists_coveringSieve_retract_free
    {C : Type u} [Category.{v} C] {J : GrothendieckTopology C}
    [J.HasSheafCompose (forget₂ CommRingCat.{max v w} RingCat.{max v w})]
    [HasWeakSheafify J AddCommGrpCat.{max v w}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{max v w}]
    [∀ T : C, HasWeakSheafify (J.over T) AddCommGrpCat.{max v w}]
    [∀ T : C, (J.over T).WEqualsLocallyBijective AddCommGrpCat.{max v w}]
    (O : Sheaf J CommRingCat.{max v w})
    (F : _root_.SheafOfModules.{max v w} (commRingSheafToRingSheaf O))
    [F.IsFinitePresentation] (hF : IsFlat F) (U : C) :
    ∃ S : Sieve U, S ∈ J U ∧ ∀ {V : C} (f : V ⟶ U), S f →
      ∃ I : Type (max v w), Finite I ∧
        ∃ (i : F.over V ⟶ _root_.SheafOfModules.free
            (R := (commRingSheafToRingSheaf O).over V) I)
          (r : _root_.SheafOfModules.free (R := (commRingSheafToRingSheaf O).over V) I ⟶
            F.over V), i ≫ r = 𝟙 (F.over V)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.29, Tag 0FNX](https://stacks.math.columbia.edu/tag/0FNX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

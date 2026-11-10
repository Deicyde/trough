---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.exactPairingDualSheafOfRetract, Stacks.SheafOfModules.OnSpace.coevaluation, Stacks.SheafOfModules.OnSpace.coevaluation_comp_tensorDualToEndomorphism, Stacks.SheafOfModules.OnSpace.coevaluation_apply_eq_sum_of_retract, Stacks.SheafOfModules.OnSpace.dualSheaf_isLeftDual, Stacks.SheafOfModules.OnSpace.tensorDualToEndomorphism_tmul_apply, Stacks.SheafOfModules.OnSpace.tensorDualToEndomorphism_isIso, Stacks.SheafOfModules.dualSheaf
statement: formalized
proof: formalized
---

# 17.18 Duals

Section 17.18 of the Stacks Project, [Tag 0FNU](https://stacks.math.columbia.edu/tag/0FNU). 3 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FNV, an example

[Tag 0FNV](https://stacks.math.columbia.edu/tag/0FNV) in the Stacks Project.

**`Stacks.SheafOfModules.exactPairingDualSheafOfRetract`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualLocalDualBasis.lean, line 782](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LeftDualLocalDualBasis.lean#L782). The attribute's comment: “the LEFT-DUAL assertion itself: the canonical coevaluation `𝒪 ⟶ ℱ ⊗ ℱ^∨` and evaluation `ℱ^∨ ⊗ ℱ ⟶ 𝒪` satisfy the two snake identities, so `ℱ^∨` is a left dual of `ℱ` in the monoidal category of Tag 01CA, for `ℱ` locally a retract of a finite free sheaf of modules. This is the clause none of `dual_sheaf`, `evaluation`, `coevaluation` or the rank-one isomorphism `ℱ ⊗ ℱ^∨ ≅ 𝓗om(ℱ,ℱ)` asserts: those construct the four objects and compute them on sections, this one is the duality”.

> **Stacks Project, Tag 0FNV.** Let `𝒪` be a sheaf of commutative rings on a site `(C, J)` and
> let `F` be a sheaf of `𝒪`-modules which is locally a direct summand of a finite free sheaf of
> modules: on the members of a family covering the final object, `F` restricts to a retract of
> `SheafOfModules.free (I k)` with `I k` finite. Then the dual
> `F^∨ = SheafHom(F, 𝒪)`, with the canonical coevaluation `𝒪 ⟶ F ⊗ F^∨` and the canonical
> evaluation `F^∨ ⊗ F ⟶ 𝒪`, is a **left dual** of `F` in the monoidal category of sheaves of
> `𝒪`-modules of Tag 01CA.
>
> The retracts are converted into the dual bases that the canonical coevaluation is built from by
> `Stacks.SheafOfModules.FiniteDualBasis.ofRetract`, and the two snake identities are
> `Stacks.SheafOfModules.coevaluation_evaluation_dualSheaf` and
> `evaluation_coevaluation_dualSheaf`.

```lean
noncomputable def exactPairingDualSheafOfRetract
    (h : ∀ k, Retract (F.over (X k))
      (free (R := (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪).over (X k)) (I
        k))) :
    ExactPairing F (dualSheaf 𝒪 h𝒪 F)
```

**`Stacks.SheafOfModules.OnSpace.coevaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/Coevaluation.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/Coevaluation.lean#L194). The attribute's comment: “coevaluation”.

> **The coevaluation `O_X ⟶ F ⊗ F^∨`** of Stacks 0FNV: the inverse image of the identity
> endomorphism under the rank-one isomorphism `F ⊗ F^∨ ≅ SheafHom(F, F)`.

```lean
noncomputable def coevaluation
    (F : SheafOfModules.{u} (structureSheafRing X))
    (hF : IsLocallyFiniteFreeSummand X F) :
    SheafOfModules.unit (structureSheafRing X) ⟶
      (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj (F)).obj
        ((dualSheaf X F)))
```

**`Stacks.SheafOfModules.OnSpace.coevaluation_comp_tensorDualToEndomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/Coevaluation.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/Coevaluation.lean#L205). The attribute's comment: “coevaluation”.

> Under the rank-one isomorphism, the coevaluation is the identity endomorphism.

```lean
theorem coevaluation_comp_tensorDualToEndomorphism
    (F : SheafOfModules.{u} (structureSheafRing X))
    (hF : IsLocallyFiniteFreeSummand X F) :
    coevaluation X F hF ≫ tensorDualToEndomorphism X F = identityEndomorphism X F
```

**`Stacks.SheafOfModules.OnSpace.coevaluation_apply_eq_sum_of_retract`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/Coevaluation.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/Coevaluation.lean#L219). The attribute's comment: “coevaluation”.

> **Stacks 0FNV.** On an open `U` carrying a splitting `i ≫ p = 𝟙` of `F|_U` through a
> finite free module, the value of the coevaluation at `1` is `∑ j, p(e j) ⊗ (e j)^* ∘ i`. The
> left-hand side does not mention the splitting, so the displayed sum is independent of it.

```lean
theorem coevaluation_apply_eq_sum_of_retract
    (F : SheafOfModules.{u} (structureSheafRing X))
    (hF : IsLocallyFiniteFreeSummand X F) (U : Opens X.carrier) (n : ℕ)
    (i : F.over U ⟶
      SheafOfModules.free (R := (structureSheafRing X).over U) (ULift.{u} (Fin n)))
    (p : SheafOfModules.free (R := (structureSheafRing X).over U)
      (ULift.{u} (Fin n)) ⟶ F.over U) (hip : i ≫ p = 𝟙 _) :
    ((coevaluation X F hF).val.app (op U)).hom (1 : X.presheaf.obj (op U)) =
      ∑ j : Fin n, toTensorSheafSection X F (dualSheaf X F) (op U)
        (splittingBasisSection X F U n p j ⊗ₜ[X.presheaf.obj (op U)]
          splittingDualSection X F U n i j)
```

**`Stacks.SheafOfModules.OnSpace.dualSheaf_isLeftDual`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/LeftDualOnSpace.lean, line 463](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/LeftDualOnSpace.lean#L463). The attribute's comment: “sheaf_module_left_dual”.

> **Stacks Project, Tag 0FNV.** For a sheaf of modules which is locally a direct summand of
> a finite free module, its internal-Hom dual, with the canonical coevaluation and evaluation, is
> a left dual.
>
> The monoidal structure is exhibited together with the equations identifying its unit, its
> tensor product on objects and on morphisms, and its pairing morphisms, with the canonical
> sheaf constructions.

```lean
theorem dualSheaf_isLeftDual
    (F : SheafOfModules.{u} (structureSheafRing X))
    (hF : IsLocallyFiniteFreeSummand X F) :
    ∃ (M : MonoidalCategory (SheafOfModules.{u} (structureSheafRing X))),
      letI := M
      ∃ (hunit : 𝟙_ (SheafOfModules.{u} (structureSheafRing X)) =
          SheafOfModules.unit (structureSheafRing X))
        (htensor : ∀ A B : SheafOfModules.{u} (structureSheafRing X),
          A ⊗ B = (((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj (A)).obj (B)))
        (_htensorMap : ∀ {A A' B B' : SheafOfModules.{u} (structureSheafRing X)}
          (f : A ⟶ A') (g : B ⟶ B'),
          eqToHom (htensor A B).symm ≫ (f ⊗ₘ g) ≫ eqToHom (htensor A' B') =
            ((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩)).map ((f, g) : (_, _) ⟶ (_, _))))
        (p : ExactPairing F (dualSheaf X F)),
        @ExactPairing.coevaluation _ _ _ _ _ p =
          eqToHom hunit ≫ coevaluation X F hF ≫
            eqToHom (htensor F (dualSheaf X F)).symm ∧
        @ExactPairing.evaluation _ _ _ _ _ p =
          eqToHom (htensor (dualSheaf X F) F) ≫ evaluation X F ≫ eqToHom hunit.symm
```

**`Stacks.SheafOfModules.OnSpace.tensorDualToEndomorphism_tmul_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/TensorDualEndomorphism.lean, line 588](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/TensorDualEndomorphism.lean#L588). The attribute's comment: “tensor_dual_endomorphism_iso”.

> On a local pure tensor of a section `f` and a local functional `lam`, the canonical
> morphism is the rank-one endomorphism `g ↦ lam(g) • f`. The formula is recorded on every
> object `V` of the slice site over `U`, so it determines the resulting section of the
> internal hom.

```lean
theorem tensorDualToEndomorphism_tmul_apply
    (F : SheafOfModules.{u} (structureSheafRing X))
    (U : TopologicalSpace.Opens X.carrier)
    (f : F.val.obj (op U)) (lam : (dualSheaf X F).val.obj (op U))
    (V : (Over U)ᵒᵖ) (g : F.val.obj (op V.unop.left)) :
    ((((tensorDualToEndomorphism X F).val.app (op U)).hom
      (toTensorSheafSection X F (dualSheaf X F) (op U)
        (f ⊗ₜ[X.presheaf.obj (op U)] lam))).app V).hom g =
      dualValue X F lam V g • (F.val.map V.unop.hom.op).hom f
```

**`Stacks.SheafOfModules.OnSpace.tensorDualToEndomorphism_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/TensorDualEndomorphism.lean, line 606](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/TensorDualEndomorphism.lean#L606). The attribute's comment: “tensor_dual_endomorphism_iso”.

> **Stacks 0FNV.** If `F` is locally a direct summand of a finite free module, the
> canonical rank-one-operator morphism `F ⊗ F^∨ ⟶ SheafHom(F, F)` is an isomorphism.

```lean
theorem tensorDualToEndomorphism_isIso
    (F : SheafOfModules.{u} (structureSheafRing X))
    (hF : IsLocallyFiniteFreeSummand X F) :
    IsIso (tensorDualToEndomorphism X F)
```

**`Stacks.SheafOfModules.dualSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHom.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHom.lean#L279). The attribute's comment: “dual_sheaf”. References: SGA 3 III (0.6).

> **The dual of a sheaf of modules**, `F^∨ = SheafHom(F, 𝒪)`: the sheaf-hom into the
> structure sheaf.

```lean
noncomputable def dualSheaf
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪))
      :
    SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪)
```

**`Stacks.SheafOfModules.evaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHom.lean, line 696](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafHom.lean#L696). The attribute's comment: “evaluation”.

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

**`Stacks.SheafOfModules.tensorDualToEndomorphism_toTensorSheafSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean, line 655](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean#L655). The attribute's comment: “the rank-one map `ℱ ⊗ ℱ^∨ ⟶ 𝓗om(ℱ,ℱ)` read on sections: a local pure tensor `f ⊗ λ` goes to the endomorphism `g ↦ λ(g) • f`. This pins the morphism down; the companion clause `isIso_tensorDualToEndomorphism` says it is an isomorphism”.

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

**`Stacks.SheafOfModules.isIso_tensorDualToEndomorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean, line 694](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean#L694). The attribute's comment: “the rank-one map `ℱ ⊗ ℱ^∨ ⟶ 𝓗om(ℱ,ℱ)` is an ISOMORPHISM when `ℱ` admits a finite dual basis on a covering family. A different assertion from the section formula that pins the map down, which is carried by `tensorDualToEndomorphism_toTensorSheafSection`”. References: SGA 5 IIIB (5.0), “partial”.

> **`F ⊗ F^∨ ⟶ SheafHom(F, F)` is an isomorphism** when `F` has finite dual bases on a family
> covering the final object — that is, when `F` is locally a direct summand of a finite free sheaf
> of modules.

```lean
theorem isIso_tensorDualToEndomorphism {K : Type*} {X : K → C} (hX : J.CoversTop X)
    {I : K → Type*} [∀ k, Fintype (I k)]
    (b : ∀ k, FiniteDualBasis 𝒪 h𝒪 F (X k) (I k)) :
    IsIso (tensorDualToEndomorphism 𝒪 h𝒪 F)
```

**`Stacks.SheafOfModules.coevaluation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean, line 720](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean#L720). The attribute's comment: “EXISTENCE of the canonical coevaluation `𝒪 ⟶ ℱ ⊗ ℱ^∨`, as a named morphism. Its value on local sections is a separate assertion, carried by `coevaluation_app_one_eq_sum_of_dualBasis`”.

> **The canonical coevaluation `𝒪 ⟶ F ⊗ F^∨`** of a sheaf of modules which is locally a
> direct summand of a finite free sheaf of modules: the inverse image of the identity
> endomorphism under the rank-one isomorphism `F ⊗ F^∨ ≅ SheafHom(F, F)`.

```lean
noncomputable def coevaluation
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪))
    {K : Type*} {X : K → C} (hX : J.CoversTop X) {I : K → Type*} [∀ k, Fintype (I k)]
    (b : ∀ k, FiniteDualBasis 𝒪 h𝒪 F (X k) (I k)) :
    SheafOfModules.unit (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪) ⟶
      ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, max u v, max u v, max u v}
        ⟨𝒪, Presheaf.isSheaf_of_isSheaf_comp _ 𝒪 (forget₂ CommRingCat RingCat) h𝒪⟩).obj F).obj
          (dualSheaf 𝒪 h𝒪 F)
```

**`Stacks.SheafOfModules.coevaluation_app_one_eq_sum_of_dualBasis`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorDualEndomorphism.lean#L757). The attribute's comment: “the canonical coevaluation READ ON SECTIONS: over an object of the covering family it sends `1` to `∑ i, eᵢ ⊗ λᵢ` for a finite dual basis. This is what makes the coevaluation canonical rather than `some morphism exists`”.

> **The local formula for the canonical coevaluation.** On an object `U` over which `F` has a
> finite dual basis `(e i, lam i)`, the value of the coevaluation at the unit section is
> `∑ i, e i ⊗ lam i`.
>
> Because the left-hand side does not mention the dual basis, this also says that the displayed
> sum is **independent of the chosen dual basis** — equivalently, of the chosen finite-free
> retract, since a retract `i ≫ p = 𝟙` of `F|_U` onto a finite free sheaf of modules yields the
> dual basis `e j = p(e_j)`, `lam j = e_j^* ∘ i`.

```lean
theorem coevaluation_app_one_eq_sum_of_dualBasis
    (F : SheafOfModules.{max u v} (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪))
    {K : Type*} {X : K → C} (hX : J.CoversTop X) {I : K → Type*} [∀ k, Fintype (I k)]
    (b : ∀ k, FiniteDualBasis 𝒪 h𝒪 F (X k) (I k))
    (U : C) {I' : Type*} [Fintype I'] (c : FiniteDualBasis 𝒪 h𝒪 F U I') :
    ((coevaluation 𝒪 h𝒪 F hX b).val.app (op U)).hom
        (1 : (Stacks.SheafOfModules.TensorSheafification.structureSheaf 𝒪 h𝒪).obj.obj (op U)) =
      ∑ i : I', toTensorSheafSection 𝒪 h𝒪 F (dualSheaf 𝒪 h𝒪 F) (op U)
        (c.e i ⊗ₜ[(Stacks.SheafOfModules.TensorSheafification.structureRingPresheaf 𝒪).obj (op U)]
          c.lam i)
```

## Tag 0FNW, a lemma

[Tag 0FNW](https://stacks.math.columbia.edu/tag/0FNW) in the Stacks Project.

**`Stacks.SheafOfModules.OnSpace.dualSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/DualSheafIso.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/DualSheafIso.lean#L311). The attribute's comment: “dual_sheaf_isomorphism”.

> **Stacks Project, Tag 0FNW (2).** A left dual `G` of `F` is canonically isomorphic to the
> dual sheaf `F^∨ = SheafHom(F, O_X)`. The isomorphism sends a local functional `lam` over `U` to
> `∑ i, lam (f i) • g i` for any expansion `η(1) = ∑ i, f i ⊗ g i` of the coevaluation over `U`;
> in particular that expression does not depend on the chosen expansion.

```lean
noncomputable def dualSheafIso
    (F G : SheafOfModules.{u} (structureSheafRing X))
    (η : SheafOfModules.unit (structureSheafRing X) ⟶
      ((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj F).obj G)
    (ε : ((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj G).obj F ⟶
      SheafOfModules.unit (structureSheafRing X))
    (h : IsLeftDual X F G η ε) :
    { e : dualSheaf X F ≅ G //
      ∀ (U : Opens X.carrier) (lam : (dualSheaf X F).val.obj (op U))
        (n : ℕ) (f : Fin n → F.val.obj (op U)) (g : Fin n → G.val.obj (op U)),
        (η.val.app (op U)).hom (1 : X.presheaf.obj (op U)) =
          toTensorSheafSection X F G (op U)
            (∑ i, f i ⊗ₜ[X.presheaf.obj (op U)] g i) →
        (e.hom.val.app (op U)).hom lam =
          ∑ i, dualEval X F lam (f i) • g i }
```

**`Stacks.SheafOfModules.OnSpace.evaluation_eq_dualSheafIso_inv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/DualSheafIso.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/DualSheafIso.lean#L332). The attribute's comment: “evaluation_formula”.

> **Stacks Project, Tag 0FNW (3).** Pairing a local section of a left dual `G` with a local
> section of `F` under the evaluation `ε` is ordinary evaluation of the corresponding local
> functional on `F`, the correspondence being the inverse of the isomorphism of Stacks 0FNW (2).

```lean
theorem evaluation_eq_dualSheafIso_inv
    (F G : SheafOfModules.{u} (structureSheafRing X))
    (η : SheafOfModules.unit (structureSheafRing X) ⟶
      ((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj F).obj G)
    (ε : ((Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩).obj G).obj F ⟶
      SheafOfModules.unit (structureSheafRing X))
    (h : IsLeftDual X F G η ε)
    (U : Opens X.carrier)
    (g : G.val.obj (op U)) (f : F.val.obj (op U)) :
    (ε.val.app (op U)).hom
        (toTensorSheafSection X G F (op U) (g ⊗ₜ[X.presheaf.obj (op U)] f)) =
      (((((dualSheafIso X F G η ε h).val.inv.val.app (op U)).hom g).app
        (op (Over.mk (𝟙 U)))).hom f)
```

**`Stacks.SheafOfModules.OnSpace.isLocallyFiniteFreeSummand_of_exactPairing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/LeftDualOnSpace.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/LeftDualOnSpace.lean#L437). The attribute's comment: “local_finite_free_summand”.

> **Stacks Project, Tag 0FNW (1)**, with no coherence hypotheses: a sheaf of modules with a
> left dual in the monoidal category of `O_X`-modules is locally a direct summand of a finite
> free module.
>
> The three coherence hypotheses of
> `Stacks.SheafOfModules.isLocallyFiniteFreeSummand_of_exactPairing` — which constrain the
> supplied monoidal instance on local pure tensors — are discharged here against the constructed
> monoidal structure by `associator_tmul`, `leftUnitor_tmul` and `rightUnitor_tmul`.

```lean
theorem isLocallyFiniteFreeSummand_of_exactPairing
    (F G : SheafOfModules.{u} (structureSheafRing X))
    (p : ExactPairing F G) :
    IsLocallyFiniteFreeSummand X F
```

## Tag 08BL, a lemma

[Tag 08BL](https://stacks.math.columbia.edu/tag/08BL) in the Stacks Project.

**`Stacks.SheafOfModules.isLocallyFiniteFreeSummand_of_isFlat_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/FlatFinitePresentation.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocallyFiniteFreeSummand/FlatFinitePresentation.lean#L113).

> **Stacks 08BL.** A flat sheaf of `O_X`-modules of finite presentation on a ringed space is,
> locally on `X`, a direct summand of a finite free `O_X`-module.
>
> This is Stacks 08FD on the site of opens of `X`: the covering sieve it produces on `⊤` is, by
> `TopologicalSpace.Opens.mem_grothendieckTopology`, a neighbourhood of each point of `X` carrying
> the retraction, and the finite index type of the free module there is reindexed by `Fin n`.

```lean
theorem isLocallyFiniteFreeSummand_of_isFlat_of_isFinitePresentation
    (F : _root_.SheafOfModules.{u} (structureSheafRing X))
    [hfp₀ : F.IsFinitePresentation]
    (hF : AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.sheaf) F) :
    IsLocallyFiniteFreeSummand X F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.18, Tag 0FNU](https://stacks.math.columbia.edu/tag/0FNU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

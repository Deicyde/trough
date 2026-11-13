---
declaration: section
origin: cited
lean: DiffOp.IsGlobalDiffOpOfOrder, DiffOp.isGlobalDiffOpOfOrder_comp, AlgebraicGeometry.SheafOfModules.differentialOperatorsFunctor_isCorepresentable, AlgebraicGeometry.SheafOfModules.moduleOfPrincipalParts, Stacks.Sheaves.PrincipalParts.principalPartsSheafification, AlgebraicGeometry.SheafOfModules.nonempty_principalPartsSequence_opens
statement: formalized
proof: formalized
---

# 17.29 Finite order differential operators

Section 17.29 of the Stacks Project, [Tag 0G3P](https://stacks.math.columbia.edu/tag/0G3P). 7 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G3Q, a definition

[Tag 0G3Q](https://stacks.math.columbia.edu/tag/0G3Q) in the Stacks Project.

Declarations registered for the tag:

- [`DiffOp.IsGlobalDiffOpOfOrder`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperatorsOrder.lean#L185), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperators.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperators.lean#L72) (StacksFrontier).

## Tag 0G3R, a lemma

[Tag 0G3R](https://stacks.math.columbia.edu/tag/0G3R) in the Stacks Project.

Declarations registered for the tag:

- [`DiffOp.isGlobalDiffOpOfOrder_comp`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperatorsOrder.lean#L523), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialOperatorsRingedSpace.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialOperatorsRingedSpace.lean#L40) (StacksFrontier): “the ringed-space case of 09CS”.

## Tag 0G3S, a lemma

[Tag 0G3S](https://stacks.math.columbia.edu/tag/0G3S) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.SheafOfModules.differentialOperatorsFunctor_isCorepresentable`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperators.lean#L571), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialOperatorsRingedSpace.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialOperatorsRingedSpace.lean#L42) (StacksFrontier): “the ringed-space case of 09CT”.

## Tag 0G3T, a definition

[Tag 0G3T](https://stacks.math.columbia.edu/tag/0G3T) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.SheafOfModules.moduleOfPrincipalParts`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean#L164), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsRingedSpace.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsRingedSpace.lean#L33) (StacksFrontier): “the ringed-space case of 09CU”.

## Tag 0G3U, a lemma

[Tag 0G3U](https://stacks.math.columbia.edu/tag/0G3U) in the Stacks Project.

**`Stacks.Sheaves.PrincipalParts.principalPartsSheafification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSheafification.lean, line 697](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSheafification.lean#L697). References: EGA IV (16.4.24), “(ii)”.

> **Stacks Project, Tag 0G3U**, which read as a statement about the sheaf of principal parts
> is **Tag 09CV**. Let `φ : O₁ ⟶ O₂` be a morphism of presheaves of
> commutative rings on a site and let `F` be a presheaf of `O₂`-modules. Then the sheaf of
> principal parts of order `k` of `F^#` relative to `O₂^# / O₁^#` is the sheaf associated to
> the presheaf `X ↦ Pᵏ_{O₂(X)/O₁(X)}(F X)` of sectionwise modules of principal parts, and the
> sectionwise universal operators are compatible with restriction.

```lean
noncomputable def principalPartsSheafification [HasWeakSheafify J CommRingCat.{u}]
    [J.WEqualsLocallyBijective CommRingCat.{u}]
    [J.HasSheafCompose (forget₂ CommRingCat.{u} RingCat.{u})]
    [J.WEqualsLocallyBijective AddCommGrpCat.{max u u₁ v₁ v}]
    [HasWeakSheafify J AddCommGrpCat.{max u u₁ v₁ v}] {O₁ O₂ : Cᵒᵖ ⥤ CommRingCat.{u}}
    (φ : O₁ ⟶ O₂)
    (F : PresheafOfModules.{max u u₁ v₁ v} (O₂ ⋙ forget₂ CommRingCat.{u} RingCat.{u}))
    (k : ℕ) :
    Σ' P : PresheafOfModules.{max u u₁ v₁ v}
        (O₂ ⋙ forget₂ CommRingCat.{u} RingCat.{u}),
      Σ' D : F.presheaf ⟶ P.presheaf,
        Σ' _e : (AlgebraicGeometry.SheafOfModules.differentialOperatorsFunctor.{v₁, u₁, u,
            max u u₁ v₁ v}
            ((sheafCompose J (forget₂ CommRingCat.{u} RingCat.{u})).map
              (associatedCommRingSheafMap J φ))
            ((PresheafOfModules.sheafification (toAssociatedRingSheaf J O₂)).obj F)
            k).coreprX (hF :=
              AlgebraicGeometry.SheafOfModules.differentialOperatorsFunctor_isCorepresentable
                ((sheafCompose J (forget₂ CommRingCat.{u} RingCat.{u})).map
                  (associatedCommRingSheafMap J φ))
                ((PresheafOfModules.sheafification (toAssociatedRingSheaf J O₂)).obj F) k) ≅
          (PresheafOfModules.sheafification (toAssociatedRingSheaf J O₂)).obj P,
        ∀ X : Cᵒᵖ,
          letI : Algebra (O₁.obj X) (O₂.obj X) := (φ.app X).hom.toAlgebra
          letI : Module (O₁.obj X) (F.obj X) :=
            Module.compHom (F.obj X) (φ.app X).hom
          letI : Module (O₁.obj X) (P.obj X) :=
            Module.compHom (P.obj X) (φ.app X).hom
          letI : IsScalarTower (O₁.obj X) (O₂.obj X) (F.obj X) :=
            IsScalarTower.of_algebraMap_smul fun _ _ ↦ rfl
          letI : IsScalarTower (O₁.obj X) (O₂.obj X) (P.obj X) :=
            IsScalarTower.of_algebraMap_smul fun _ _ ↦ rfl
          ∃ d : F.obj X →ₗ[O₁.obj X] P.obj X,
            (∀ x, d x = (D.app X).hom x) ∧
              d.IsUniversalDifferentialOperatorOfOrderLE (O₂.obj X) k
```

## Tag 0G3V, a lemma

[Tag 0G3V](https://stacks.math.columbia.edu/tag/0G3V) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.nonempty_principalPartsSequence_opens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials/PrincipalParts.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/Differentials/PrincipalParts.lean#L77). References: SGA 6 II (AppII.1.2.4), “n = 1, top. space”.

> **Stacks Project, Tag 0G3V.** For a homomorphism `φ : O₁ ⟶ O₂` of sheaves of commutative
> rings on a topological space, the sheaves of first principal parts of the sheaves of
> `O₂`-modules assemble into a functor sitting in a short exact sequence
>
> `0 ⟶ Ω_{O₂/O₁} ⊗_{O₂} F ⟶ P¹_{O₂/O₁}(F) ⟶ F ⟶ 0`
>
> natural in `F`, with its two arrows determined by their values on universal differential
> operators.

```lean
theorem nonempty_principalPartsSequence_opens {X : TopCat.{u}}
    (O₁ O₂ : TopCat.Sheaf CommRingCat.{u} X) (φ : O₁ ⟶ O₂) :
    Nonempty (PrincipalPartsSequence.{u, u, u, m} (J := Opens.grothendieckTopology X) O₁ O₂ φ)
```

## Tag 0G3X, a definition

[Tag 0G3X](https://stacks.math.columbia.edu/tag/0G3X) in the Stacks Project.

Declarations registered for the tag:

- [`DiffOp.IsGlobalDiffOpOfOrder`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperatorsOrder.lean#L185), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperators.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperators.lean#L73) (StacksFrontier): “differential operators on X/S, for the map f♯ : f⁻¹𝒪\_S ⟶ 𝒪\_X”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.29, Tag 0G3P](https://stacks.math.columbia.edu/tag/0G3P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

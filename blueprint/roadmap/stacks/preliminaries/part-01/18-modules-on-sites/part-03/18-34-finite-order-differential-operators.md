---
declaration: section
origin: cited
lean: DiffOp.IsGlobalDiffOpOfOrder, DiffOp.isGlobalDiffOpOfOrder_comp, AlgebraicGeometry.SheafOfModules.existsUnique_descDiffOp, AlgebraicGeometry.SheafOfModules.differentialOperatorsFunctor_isCorepresentable, AlgebraicGeometry.SheafOfModules.moduleOfPrincipalParts, Stacks.Sheaves.PrincipalParts.principalPartsSheafification, AlgebraicGeometry.SheafOfModules.exists_shortExact_principalPartsSequence', AlgebraicGeometry.SheafOfModules.principalPartsSequence_nonempty
statement: formalized
proof: formalized
---

# 18.34 Finite order differential operators

Section 18.34 of the Stacks Project, [Tag 09CQ](https://stacks.math.columbia.edu/tag/09CQ). 7 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09CR, a definition

[Tag 09CR](https://stacks.math.columbia.edu/tag/09CR) in the Stacks Project.

Declarations registered for the tag:

- [`DiffOp.IsGlobalDiffOpOfOrder`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperatorsOrder.lean#L185), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperators.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperators.lean#L71) (StacksFrontier).

## Tag 09CS, a lemma

[Tag 09CS](https://stacks.math.columbia.edu/tag/09CS) in the Stacks Project.

**`DiffOp.isGlobalDiffOpOfOrder_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperatorsOrder.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperatorsOrder.lean#L523). References: EGA IV (16.8.9), “more general”; EGA IV (16.8.10), “more general”; SGA 3 VIIA (1.2), “sheaf, deviations of id”; SGA 3 VIIA (1.4), “partial”; SGA 6 II (AppII.1.2.4), “more general”.

> The composition of a differential operator of order `k` with a differential operator
> of order `k'` is a differential operator of order `k + k'`.
>
> The argument: `IsGlobalDiffOpOfOrder` is `∀ U, IsDiffOpOfOrder` on `restrict`; by
> `GlobalOp.restrict_comp` the restriction of the composite is the raw composite of the
> restrictions; then apply the raw composition lemma `isDiffOpOfOrder_comp_raw`
> (strong induction on `k + k'` via the commutator-of-composition identity).

```lean
theorem isGlobalDiffOpOfOrder_comp (φ : O₁ ⟶ O₂)
    {E F G : SheafOfModules O₂} {k k' : ℕ}
    (D : GlobalOp E F) (D' : GlobalOp F G)
    (hD : IsGlobalDiffOpOfOrder φ k D) (hD' : IsGlobalDiffOpOfOrder φ k' D') :
    IsGlobalDiffOpOfOrder φ (k + k') (D'.comp D)
```

## Tag 09CT, a lemma

[Tag 09CT](https://stacks.math.columbia.edu/tag/09CT) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.existsUnique_descDiffOp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean#L187). The attribute's comment: “unique-factorization form”. References: EGA IV (16.8.3), “(16.8.3.1)”; SGA 6 II (AppII.1.2.3); SGA 6 II (AppII.1.2.2), “(1.2.2.1)”.

> **Stacks 09CT**, in unique-factorization form: every differential operator of order at
> most `k` out of `F` factors through the universal one by a unique morphism of sheaves of
> modules.

```lean
theorem existsUnique_descDiffOp
    (F G : _root_.SheafOfModules.{max u v w m} O₂) (k : ℕ)
    (D : DiffOp.GlobalOp F G) (hD : DiffOp.IsGlobalDiffOpOfOrder phi k D) :
    ∃! f : moduleOfPrincipalParts.{v, u, w, m} phi F k ⟶ G,
      postcomp (universalDiffOp.{v, u, w, m} phi F k) f = D
```

**`AlgebraicGeometry.SheafOfModules.differentialOperatorsFunctor_isCorepresentable`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperators.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/DifferentialOperators.lean#L571). References: EGA IV (16.8.3), “(16.8.3.1)”; SGA 6 II (AppII.1.2.3); SGA 6 II (AppII.1.2.2), “(1.2.2.1)”.

> Differential operators of order at most `k` out of a fixed module sheaf are
> represented by a sheaf of modules (the sheaf of principal parts).

```lean
noncomputable instance differentialOperatorsFunctor_isCorepresentable (phi : O₁ ⟶ O₂)
    (F : _root_.SheafOfModules.{max u v w m} O₂) (k : ℕ) :
    (differentialOperatorsFunctor.{v, u, w, m} phi F k).IsCorepresentable
```

## Tag 09CU, a definition

[Tag 09CU](https://stacks.math.columbia.edu/tag/09CU) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.moduleOfPrincipalParts`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PrincipalPartsUniversal.lean#L164). The attribute's comment: “the module of principal parts of order k”. References: SGA 6 II (AppII.1.2.2), “P^n\_\{X/S}(E)”.

> The sheaf of principal parts `Pᵏ_{O₂/O₁}(F)`: the sheaf of modules corepresenting the
> functor of differential operators of order at most `k` out of `F`.

```lean
noncomputable abbrev moduleOfPrincipalParts
    (F : _root_.SheafOfModules.{max u v w m} O₂) (k : ℕ) :
    _root_.SheafOfModules.{max u v w m} O₂
```

## Tag 09CV, a lemma

[Tag 09CV](https://stacks.math.columbia.edu/tag/09CV) in the Stacks Project.

**`Stacks.Sheaves.PrincipalParts.principalPartsSheafification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSheafification.lean, line 697](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSheafification.lean#L697). References: EGA IV (16.4.24), “(ii)”.

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

## Tag 09CW, a lemma

[Tag 09CW](https://stacks.math.columbia.edu/tag/09CW) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.exists_shortExact_principalPartsSequence'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsJet.lean, line 1178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsJet.lean#L1178). The attribute's comment: “field 8 ALONE: the short exact sequence of the principal-parts sequence, now”. References: SGA 6 II (AppII.1.2.4), “n = 1”.

> **The sequence of principal parts is a short exact sequence.**

```lean
theorem exists_shortExact_principalPartsSequence' :
    ∃ h : (principalPartsInclusion.{v, u, w, m} φ).app F ≫
        (principalPartsProjection.{v, u, w, m}
          (underlyingRingSheafMapOfSite φ) 1).app F = 0,
      (ShortComplex.mk ((principalPartsInclusion.{v, u, w, m} φ).app F)
        ((principalPartsProjection.{v, u, w, m}
          (underlyingRingSheafMapOfSite φ) 1).app F) h).ShortExact
```

**`AlgebraicGeometry.SheafOfModules.principalPartsSequence_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSequenceStructure.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSequenceStructure.lean#L190). The attribute's comment: “the tag's OWN assertion: a functorial first-principal-parts sequence exists, i.e. the eight-field record is inhabited. The individual clauses of field 8 are carried separately in `PrincipalPartsJet.lean` and `PrincipalPartsSequence.lean`.”. References: SGA 6 II (AppII.1.2.4), “n = 1”.

> The functorial short exact sequence of first principal parts exists.

```lean
theorem principalPartsSequence_nonempty (O₁ O₂ : Sheaf J CommRingCat.{w})
    (φ : O₁ ⟶ O₂) : Nonempty (PrincipalPartsSequence.{v, u, w, m} O₁ O₂ φ)
```

## Tag 09CX, a remark

[Tag 09CX](https://stacks.math.columbia.edu/tag/09CX) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.principalPartsMapOfSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsChangeOfRings.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsChangeOfRings.lean#L255). The attribute's comment: “maps”.

> **Stacks 09CX.** The map on order-`k` principal parts induced by a commutative square of
> sheaves of rings together with a compatible linear map of module sheaves.

```lean
noncomputable def principalPartsMapOfSquare
    (φ : A ⟶ B) (φ' : A' ⟶ B') (α : A ⟶ A') (β : B ⟶ B')
    (h : φ ≫ β = α ≫ φ')
    (F : _root_.SheafOfModules.{max u v w m} B)
    (F' : _root_.SheafOfModules.{max u v w m} B')
    (uF : F ⟶ (_root_.SheafOfModules.restrictScalars.{max u v w m} β).obj F')
    (k : ℕ) :
    moduleOfPrincipalParts.{v, u, w, m} φ F k ⟶
      (_root_.SheafOfModules.restrictScalars.{max u v w m} β).obj
        (moduleOfPrincipalParts.{v, u, w, m} φ' F' k)
```

**`AlgebraicGeometry.SheafOfModules.principalPartsMapOfSquare_universalOperator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsChangeOfRings.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsChangeOfRings.lean#L282). The attribute's comment: “maps”.

> The induced map sends each universal local generator to the generator associated to its
> image under the module map.

```lean
theorem principalPartsMapOfSquare_universalOperator (k : ℕ) (X : Cᵒᵖ) (s : F.val.obj X) :
    ((principalPartsMapOfSquare φ φ' α β h F F' uF k).val.app X).hom
      ((differentialOperatorsFunctor.{v, u, w, m} φ F k).coreprx.1 X s) =
      (differentialOperatorsFunctor.{v, u, w, m} φ' F' k).coreprx.1 X
        ((uF.val.app X).hom s)
```

**`AlgebraicGeometry.SheafOfModules.principalPartsMapOfSquare_comp_orderReduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsChangeOfRings.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsChangeOfRings.lean#L323). The attribute's comment: “maps”.

> The induced maps commute with the canonical maps reducing the order from `k + 1` to `k`.

```lean
theorem principalPartsMapOfSquare_comp_orderReduction (k : ℕ) :
    principalPartsOrderReduction.{v, u, w, m} φ F k ≫
        principalPartsMapOfSquare φ φ' α β h F F' uF k =
      principalPartsMapOfSquare φ φ' α β h F F' uF (k + 1) ≫
        (_root_.SheafOfModules.restrictScalars.{max u v w m} β).map
          (principalPartsOrderReduction.{v, u, w, m} φ' F' k)
```

**`AlgebraicGeometry.SheafOfModules.principalPartsMapOfSquare_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsChangeOfRings.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsChangeOfRings.lean#L407). The attribute's comment: “composition of the maps”.

> **Stacks 09CX.** The map on principal parts associated to two successive compatible squares
> is the composite of their maps on principal parts.

```lean
theorem principalPartsMapOfSquare_comp
    (φ : A ⟶ B) (φ' : A' ⟶ B') (φ'' : A'' ⟶ B'')
    (α : A ⟶ A') (β : B ⟶ B')
    (α' : A' ⟶ A'') (β' : B' ⟶ B'')
    (h : φ ≫ β = α ≫ φ') (h' : φ' ≫ β' = α' ≫ φ'')
    (F : _root_.SheafOfModules.{max u v w m} B)
    (F' : _root_.SheafOfModules.{max u v w m} B')
    (F'' : _root_.SheafOfModules.{max u v w m} B'')
    (uF : F ⟶ (_root_.SheafOfModules.restrictScalars.{max u v w m} β).obj F')
    (uF' : F' ⟶ (_root_.SheafOfModules.restrictScalars.{max u v w m} β').obj F'')
    (k : ℕ) :
    principalPartsMapOfSquare.{v, u, w, m} φ φ'' (α ≫ α') (β ≫ β')
        (by rw [← Category.assoc, h, Category.assoc, h', ← Category.assoc])
        F F'' (uF ≫ (_root_.SheafOfModules.restrictScalars.{max u v w m} β).map uF') k =
      principalPartsMapOfSquare.{v, u, w, m} φ φ' α β h F F' uF k ≫
        (_root_.SheafOfModules.restrictScalars.{max u v w m} β).map
          (principalPartsMapOfSquare.{v, u, w, m} φ' φ'' α' β' h' F' F'' uF' k)
```

**`AlgebraicGeometry.SheafOfModules.principalPartsSequence_naturality_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSequenceNaturality.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSequenceNaturality.lean#L280). The attribute's comment: “sequence naturality: the projection square”.

> **Stacks 09CX.** The change-of-rings maps on first principal parts are compatible with the
> projections of the short exact sequences of Tag 09CW: the right-hand square of the naturality
> diagram commutes, the comparison of its two right-hand terms being `uF`.

```lean
theorem principalPartsSequence_naturality_projection
    (φ : O₁ ⟶ O₂) (φ' : O₁' ⟶ O₂') (α : O₁ ⟶ O₁') (β : O₂ ⟶ O₂')
    (hsq : φ ≫ β = α ≫ φ')
    (F : _root_.SheafOfModules.{max u v w m} (Stacks.SheafOfModules.Tensor.ringSheaf O₂))
    (F' : _root_.SheafOfModules.{max u v w m} (Stacks.SheafOfModules.Tensor.ringSheaf O₂'))
    (uF : F ⟶ (_root_.SheafOfModules.restrictScalars.{max u v w m}
      (underlyingRingSheafMapOfSite β)).obj F') :
    principalPartsSquareMap.{v, u, w, m} φ φ' α β hsq F F' uF ≫
        (_root_.SheafOfModules.restrictScalars.{max u v w m}
          (underlyingRingSheafMapOfSite β)).map
          ((principalPartsProjection.{v, u, w, m}
            (underlyingRingSheafMapOfSite φ') 1).app F') =
      (principalPartsProjection.{v, u, w, m}
        (underlyingRingSheafMapOfSite φ) 1).app F ≫ uF
```

**`AlgebraicGeometry.SheafOfModules.principalPartsSequence_naturality_inclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSequenceNaturality.lean, line 658](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsSequenceNaturality.lean#L658). The attribute's comment: “sequence naturality: the inclusion square”.

> **Stacks 09CX.** The change-of-rings maps on first principal parts are compatible with the
> inclusions of the short exact sequences of Tag 09CW: the left-hand square of the naturality
> diagram commutes, with the tensor product of `uF` and the map on differentials on the left.

```lean
theorem principalPartsSequence_naturality_inclusion
    (φ : O₁ ⟶ O₂) (φ' : O₁' ⟶ O₂') (α : O₁ ⟶ O₁') (β : O₂ ⟶ O₂') (hsq : φ ≫ β = α ≫ φ')
    (F : _root_.SheafOfModules.{max u v w m} (Stacks.SheafOfModules.Tensor.ringSheaf O₂))
    (F' : _root_.SheafOfModules.{max u v w m} (Stacks.SheafOfModules.Tensor.ringSheaf O₂'))
    (uF : F ⟶ (_root_.SheafOfModules.restrictScalars.{max u v w m}
      (underlyingRingSheafMapOfSite β)).obj F') :
    (principalPartsInclusion.{v, u, w, m} φ).app F ≫
        principalPartsSquareMap.{v, u, w, m} φ φ' α β hsq F F' uF =
      differentialsTensorMap.{v, u, w, m} φ φ' α β hsq F F' uF ≫
        (_root_.SheafOfModules.restrictScalars.{max u v w m}
          (underlyingRingSheafMapOfSite β)).map
          ((principalPartsInclusion.{v, u, w, m} φ').app F')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.34, Tag 09CQ](https://stacks.math.columbia.edu/tag/09CQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

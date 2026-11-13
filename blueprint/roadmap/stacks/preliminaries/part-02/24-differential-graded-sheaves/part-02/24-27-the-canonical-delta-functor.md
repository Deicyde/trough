---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.coneDescHom, SheafOfModules.DifferentialGradedModule.coneIncl_coneDescHom, SheafOfModules.DifferentialGradedModule.quasiIso_coneDescHom, SheafOfModules.DifferentialGradedModule.moduleToDerivedCategory, SheafOfModules.DifferentialGradedModule.isIso_moduleToDerivedCategory_map_coneDescHom, SheafOfModules.DifferentialGradedModule.shortExactδ, SheafOfModules.DifferentialGradedModule.shortExactδ_eq, SheafOfModules.DifferentialGradedModule.shortExactδ_naturality
statement: formalized
proof: formalized
---

# 24.27 The canonical delta-functor

Section 24.27 of the Stacks Project, [Tag 0FTA](https://stacks.math.columbia.edu/tag/0FTA). 2 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FTB, a lemma

[Tag 0FTB](https://stacks.math.columbia.edu/tag/0FTB) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.coneDescHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean#L253). The attribute's comment: “the comparison q of the cone with the quotient”.

> **The comparison `q : C(a) ⟶ M`.** For a short complex `K --a--> L --b--> M` of right
> differential graded `A`-modules, this is the morphism of differential graded modules out of the
> cone of `a` of tag 0FS5 whose underlying morphism of complexes is Mathlib's comparison of the
> mapping cone with the third term: read through the degreewise splitting of the cone it is the
> second projection followed by `b`. It commutes with the right action because the cone acts in its
> second coordinate as `L` does (`ConePackage.action_second`) and `b` commutes with the action.

```lean
def coneDescHom (S : ShortComplex (DifferentialGradedModule.{t, a, m} A)) :
    (conePackage S.f).cone ⟶ S.X₃
```

**`SheafOfModules.DifferentialGradedModule.coneIncl_coneDescHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean#L269). The attribute's comment: “the comparison q restricts to b along the cone inclusion”.

> The comparison restricts along the cone's inclusion of the middle term to the second map of
> the short complex: this is the equation `i ≫ q = b` that identifies `q` with the map of the
> source.

```lean
theorem coneIncl_coneDescHom (S : ShortComplex (DifferentialGradedModule.{t, a, m} A)) :
    (conePackage S.f).inclusion ≫ coneDescHom S = S.g
```

**`SheafOfModules.DifferentialGradedModule.quasiIso_coneDescHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean, line 278](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean#L278). The attribute's comment: “q is a quasi-isomorphism”.

> **The comparison is a quasi-isomorphism** when the short complex is short exact. The
> underlying complex of the cone is Mathlib's mapping cone, the underlying short complex of
> complexes is short exact by tag 0FRK, and Mathlib's
> `CochainComplex.mappingCone.quasiIso_descShortComplex` applies.

```lean
theorem quasiIso_coneDescHom {S : ShortComplex (DifferentialGradedModule.{t, a, m} A)}
    (hS : S.ShortExact) : QuasiIso (coneDescHom S).toHomologicalComplex
```

**`SheafOfModules.DifferentialGradedModule.moduleToDerivedCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean, line 308](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean#L308). The attribute's comment: “the localization functor Mod(A,d) → D(A,d)”.

> The localization functor `Mod(A, d) ⥤ D(A, d)`: the quotient by homotopy of tag 0FS1 followed
> by the localization at the quasi-isomorphisms of tag 0FT5.

```lean
abbrev moduleToDerivedCategory (A : DifferentialGradedAlgebra.{t, a} R) :
    DifferentialGradedModule.{t, a, m} A ⥤ derivedCategory.{t, a, m} A
```

**`SheafOfModules.DifferentialGradedModule.isIso_moduleToDerivedCategory_map_coneDescHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean#L323). The attribute's comment: “q is invertible in D(A,d)”.

> **The comparison `q` becomes invertible in `D(A, d)`**, so that `q⁻¹` is available there.

```lean
theorem isIso_moduleToDerivedCategory_map_coneDescHom
    {S : ShortComplex (DifferentialGradedModule.{t, a, m} A)} (hS : S.ShortExact) :
    IsIso ((moduleToDerivedCategory A).map (coneDescHom S))
```

**`SheafOfModules.DifferentialGradedModule.shortExactδ`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean#L341). The attribute's comment: “the connecting morphism δ = - p ∘ q⁻¹”.

> **The connecting morphism `δ = - p ∘ q⁻¹` of a short exact sequence of right differential
> graded modules**, as a morphism of `D(A, d)` from the image of the third term to the image of the
> degree-one shift of the first term. Here `q` is the comparison
> `SheafOfModules.DifferentialGradedModule.coneDescHom`, invertible in `D(A, d)`, and `p` is the
> canonical cone projection `ConePackage.projection` of tag 0FS5; **the minus sign is the one the
> source attaches to the cone projection**, and dropping it gives a different connecting morphism.
>
> Because `D(A, d)` carries no translation functor in this development — that is tag 0FT4, see the
> implementation notes — the target is spelled as the image of the differential graded shift
> `SheafOfModules.DifferentialGradedModule.shift` of the first term rather than as a translate of
> the image.

```lean
def shortExactδ {S : ShortComplex (DifferentialGradedModule.{t, a, m} A)} (hS : S.ShortExact) :
    (moduleToDerivedCategory A).obj S.X₃ ⟶
      (moduleToDerivedCategory A).obj (shift S.X₁)
```

**`SheafOfModules.DifferentialGradedModule.shortExactδ_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean#L352). The attribute's comment: “the connecting morphism δ = - p ∘ q⁻¹”.

> **Tag 0FTB, the formula for the connecting morphism**: it is `- p ∘ q⁻¹`, with `q` the
> comparison of the cone with the third term — which restricts to the second map of the sequence
> along the cone's inclusion — and `p` the canonical cone projection.

```lean
theorem shortExactδ_eq {S : ShortComplex (DifferentialGradedModule.{t, a, m} A)}
    (hS : S.ShortExact) :
    (conePackage S.f).inclusion ≫ coneDescHom S = S.g ∧
      ∃ _ : IsIso ((moduleToDerivedCategory A).map (coneDescHom S)),
        shortExactδ hS =
          inv ((moduleToDerivedCategory A).map (coneDescHom S)) ≫
            (moduleToDerivedCategory A).map (-(conePackage S.f).projection)
```

**`SheafOfModules.DifferentialGradedModule.shortExactδ_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeFunctoriality.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeFunctoriality.lean#L415). The attribute's comment: “the naturality of the connecting morphism δ in the short exact sequence”.

> **The naturality of the connecting morphism.** For a morphism `φ` of short exact
> sequences of right differential graded `A`-modules, the square formed by the connecting
> morphisms `δ = - p ∘ q⁻¹` of the two sequences, the image of `φ.τ₃` and the image of the induced
> morphism of the chosen degree-one shifts of the first terms commutes. This is the second of the
> two conditions in the definition of a `δ`-functor, [Stacks, Tag 0150].
>
> Because `D(A, d)` carries no translation functor in this development — see the implementation
> notes of
> `StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedConeComparison.lean` — the
> right-hand vertical arrow is the image of the differential graded shift
> `SheafOfModules.DifferentialGradedModule.coneShiftHom` of `φ.τ₁` rather than a translate of the
> image of `φ.τ₁`.

```lean
theorem shortExactδ_naturality {S₁ S₂ : ShortComplex (DifferentialGradedModule.{t, a, m} A)}
    (h₁ : S₁.ShortExact) (h₂ : S₂.ShortExact) (φ : S₁ ⟶ S₂) :
    shortExactδ h₁ ≫ (moduleToDerivedCategory A).map (coneShiftHom φ.τ₁) =
      (moduleToDerivedCategory A).map φ.τ₃ ≫ shortExactδ h₂
```

**`SheafOfModules.DifferentialGradedModule.shortExactδTranslate_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDeltaFunctorTriangle.lean, line 151](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDeltaFunctorTriangle.lean#L151). The attribute's comment: “the distinguished-triangle axiom of the delta-functor”.

> For a short exact sequence `0 → K --a--> L --b--> M → 0` of right differential graded
> modules, the triangle `(F K, F L, F M, F a, F b, δ)` with `δ = shortExactδTranslate hS` is
> distinguished in `D(A, d)`.

```lean
theorem shortExactδTranslate_distinguished
    {S : ShortComplex (DifferentialGradedModule.{u, v, w} A)} (hS : S.ShortExact) :
    Triangle.mk ((moduleToDerivedCategory.{u, v, w} A).map S.f)
        ((moduleToDerivedCategory.{u, v, w} A).map S.g) (shortExactδTranslate hS) ∈
      distTriang (derivedCategory.{u, v, w} A)
```

**`SheafOfModules.DifferentialGradedModule.shortExactδTranslate_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDeltaFunctorTriangle.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDeltaFunctorTriangle.lean#L207). The attribute's comment: “naturality of the connecting morphism in maps of short exact sequences”.

> The connecting morphism `shortExactδTranslate` is natural in the short exact sequence.

```lean
theorem shortExactδTranslate_naturality
    {S₁ S₂ : ShortComplex (DifferentialGradedModule.{u, v, w} A)}
    (h₁ : S₁.ShortExact) (h₂ : S₂.ShortExact) (φ : S₁ ⟶ S₂) :
    shortExactδTranslate h₁ ≫ ((moduleToDerivedCategory A).map φ.τ₁)⟦(1 : ℤ)⟧' =
      (moduleToDerivedCategory A).map φ.τ₃ ≫ shortExactδTranslate h₂
```

**`SheafOfModules.DifferentialGradedModule.deltaFunctorStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDeltaFunctorTriangle.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDeltaFunctorTriangle.lean#L220). The attribute's comment: “the canonical delta-functor: the localization Mod(A, d) to D(A, d) carries the natural structure of a delta-functor, with delta equal to -p after q inverse, unconditionally”.

> The `δ`-functor structure on the localization functor `Mod(A, d) ⥤ D(A, d)`, with
> `δ = - p ∘ q⁻¹` the connecting morphism `shortExactδTranslate`.

```lean
def deltaFunctorStructure :
    (moduleToDerivedCategory.{u, v, w} A).DeltaFunctorStructure
      (DifferentialGradedModule.{u, v, w} A) (derivedCategory.{u, v, w} A)
```

## Tag 0FTC, a lemma

[Tag 0FTC](https://stacks.math.columbia.edu/tag/0FTC) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.isHomotopyColimit_moduleToDerivedCategory_obj_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedColimits.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedColimits.lean#L221).

> **Stacks 0FTC.** *"Let `(C, O)` be a ringed site. Let `(A, d)` be a sheaf of differential
> graded algebras on `(C, O)`. Let `Mₙ` be a system of differential graded `A`-modules. Then the
> derived colimit `hocolim Mₙ` in `D(A, d)` is represented by the differential graded module
> `colim Mₙ`."*
>
> The conclusion is `CategoryTheory.Pretriangulated.IsHomotopyColimit` of Definition 090Z for the
> image system in `D(A, d)`: the image of `colim Mₙ` sits in a distinguished triangle
> `⊕ₙ Mₙ --(1 - f)--> ⊕ₙ Mₙ ⟶ colim Mₙ ⟶ (⊕ₙ Mₙ)⟦1⟧` of `D(A, d)`.
>
> The three inputs are all proved in this development: the pre-triangulated structure on `D(A, d)`
> in which the statement is read is the one Tag 0FT4 produces, found by instance search from
> `quasiIsomorphisms_hasLeftCalculusOfFractions` and
> `quasiIsomorphisms_isCompatibleWithTriangulation`; the `δ`-functor structure `d` is Tag 0FTB,
> `deltaFunctorStructure`; and the two colimit instances on `D(A, d)` are Tag 0FT9, parts (1) and
> (2), `hasColimitsOfShape_discrete_nat_derivedCategory` and
> `preservesColimitsOfShape_discrete_nat_moduleToDerivedCategory`.

```lean
theorem isHomotopyColimit_moduleToDerivedCategory_obj_colimit
    (F : ℕ ⥤ DifferentialGradedModule.{u, v, max u v w} A) :
    IsHomotopyColimit (F ⋙ moduleToDerivedCategory.{u, v, max u v w} A)
      ((moduleToDerivedCategory.{u, v, max u v w} A).obj (colimit F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.27, Tag 0FTA](https://stacks.math.columbia.edu/tag/0FTA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

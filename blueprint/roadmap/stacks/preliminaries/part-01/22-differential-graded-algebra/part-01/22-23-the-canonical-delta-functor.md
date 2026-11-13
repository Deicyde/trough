---
declaration: section
origin: cited
lean: DifferentialGradedModule.exists_deltaFunctorStructure_δ_eq_neg, DifferentialGradedModule.isHomotopyColimit_toDerivedCategory_obj_colimit
statement: formalized
proof: formalized
---

# 22.23 The canonical delta-functor

Section 22.23 of the Stacks Project, [Tag 09KZ](https://stacks.math.columbia.edu/tag/09KZ). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09L0, a lemma

[Tag 09L0](https://stacks.math.columbia.edu/tag/09L0) in the Stacks Project.

**`DifferentialGradedModule.exists_deltaFunctorStructure_δ_eq_neg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/CanonicalDeltaFunctorStacksSign.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/CanonicalDeltaFunctorStacksSign.lean#L156). The attribute's comment: “delta-functor structure with δ = -p ∘ q⁻¹, Stacks sign convention”.

> **Stacks Project, Tag 09L0**, in the sign convention of the Stacks project. *"Let `(A, d)` be
> a differential graded algebra. The functor `Mod_{(A, d)} → D(A, d)` defined has the natural
> structure of a `δ`-functor, with `δ_{K → L → M} = - p ∘ q⁻¹` with `p` and `q` as explained
> above."*
>
> Here `D(A, d)` is `DifferentialGradedModule.derivedCategory' A`, the localization at the
> quasi-isomorphisms of the homotopy category with the triangulation of Tag 09KH, whose
> distinguished triangles are those isomorphic to the triangle of an admissible short exact
> sequence, so that `(K, L, C(f), f, i, -p)` is distinguished (Tag 09KF,
> `DifferentialGradedModule.mappingConeTriangle_mem_distTriang`). The statement gives a
> `δ`-functor structure on the canonical functor together with, for every short exact sequence
> `0 → K → L → M → 0`, the comparison `q : C(f) ⟶ M`, `(l, k) ↦ g l`, which restricts to `g`
> along the cone inclusion `i` and is a quasi-isomorphism, hence invertible in `D(A, d)`, and the
> identification of the connecting morphism with `- p ∘ q⁻¹`: the inverse of `q` followed by the
> class of the negated cone projection `-p : C(f) ⟶ K[1]` (composed with the commutation of the
> localization with the shift), which is the third arrow of
> `DifferentialGradedModule.mappingConeTriangle` by
> `DifferentialGradedModule.mappingConeTriangle_mor₃_eq_neg`. Since the remaining fields of a
> `δ`-functor structure are `Prop`-valued, this formula determines the structure.
>
> Sign dictionary: the library's default triangulation of the homotopy category,
> `DifferentialGradedModule.instPretriangulatedHomotopyCategory`, declares the unsigned cone
> triangle `(K, L, C(f), f, i, p)` distinguished instead; against it and its localization
> `DifferentialGradedModule.derivedCategory` the same statement holds with `δ = p ∘ q⁻¹`, which is
> `DifferentialGradedModule.canonicalDeltaFunctorStructure_δ_eq`. A triangle is distinguished for
> one structure exactly when negating its third arrow makes it distinguished for the other
> (`DifferentialGradedModule.mem_distinguishedConeTriangles_iff_isDistinguishedTriangle_negMor₃`).

```lean
theorem exists_deltaFunctorStructure_δ_eq_neg :
    ∃ d : (toDerivedCategory' A).DeltaFunctorStructure (DifferentialGradedModule A)
        (derivedCategory' A),
      ∀ {S : ShortComplex (DifferentialGradedModule A)} (hS : S.ShortExact),
        (∀ x : (coneObject S.f).M, (coneDescShortComplex S).toFun x = S.g.toFun x.1) ∧
        coneIncl S.f ≫ coneDescShortComplex S = S.g ∧
        quasiIsomorphisms' A ((toHomotopyCategory A).map (coneDescShortComplex S)) ∧
        ∃ _ : IsIso ((toDerivedCategory' A).map (coneDescShortComplex S)),
          d.δ hS =
            inv ((toDerivedCategory' A).map (coneDescShortComplex S)) ≫
              (quasiIsomorphisms' A).Q.map
                (-((toHomotopyCategory A).map (coneProj S.f) ≫ (quotientShiftIso S.X₁ 1).hom)) ≫
                ((quasiIsomorphisms' A).Q.commShiftIso (1 : ℤ)).hom.app
                  ((toHomotopyCategory A).obj S.X₁)
```

## Tag 0CRL, a lemma

[Tag 0CRL](https://stacks.math.columbia.edu/tag/0CRL) in the Stacks Project.

**`DifferentialGradedModule.isHomotopyColimit_toDerivedCategory_obj_colimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedColimits.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedColimits.lean#L298).

> Let `(A, d)` be a differential graded algebra and `Mₙ` a system of differential graded
> modules. Then the derived colimit `hocolim Mₙ` in `D(A, d)` is represented by the differential
> graded module `colim Mₙ`.

```lean
theorem isHomotopyColimit_toDerivedCategory_obj_colimit
    (A : DifferentialGradedAlgebra.{u, u} R) (F : ℕ ⥤ DifferentialGradedModule.{u, u, u} A) :
    IsHomotopyColimit (F ⋙ toDerivedCategory A) ((toDerivedCategory A).obj (colimit F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.23, Tag 09KZ](https://stacks.math.columbia.edu/tag/09KZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_square_presentation_hasJacobianDelta, Algebra.Presentation.toMatrix_cotangentComplex_eq_relationJacobiMatrix, Algebra.Presentation.isRankZero_cotangentComplex, Algebra.Presentation.cotangentDeterminantBasis, Algebra.Presentation.coe_cotangentDeterminantBasis_apply, Algebra.Presentation.delta_cotangentComplex_eq, Algebra.Presentation.hasJacobianDelta, Algebra.Presentation.exists_basis_cotangent_relation
statement: formalized
proof: formalized
---

# 49.13 The Tate map

Section 49.13 of the Stacks Project, [Tag 0FKB](https://stacks.math.columbia.edu/tag/0FKB). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FKC, a remark

[Tag 0FKC](https://stacks.math.columbia.edu/tag/0FKC) in the Stacks Project.

**`AlgebraicGeometry.exists_square_presentation_hasJacobianDelta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/CotangentDeterminant.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/CotangentDeterminant.lean#L42). The attribute's comment: “the local picture around a point of the source of a locally quasi-finite syntomic morphism; the presentation is chosen by Tag 0BWE part (5)”.

> Around every point of the source of a locally quasi-finite syntomic morphism of schemes there
> is a square relative global complete intersection presentation `B = A[x_1, …, x_n]/(f_1, …, f_n)`
> with the local Jacobian picture of the determinant of its naive cotangent complex: the conormal
> module is free on the classes of the relations, the differential is the Jacobian matrix in that
> basis and the basis `dxᵢ`, the determinant line is free of rank one on the generator matching
> those two bases, and the canonical section is the Jacobian determinant times that generator.

```lean
theorem exists_square_presentation_hasJacobianDelta {Y X : Scheme.{u}} {f : Y ⟶ X}
    (hqf : LocallyQuasiFinite f) (hf : Syntomic f) (y : Y) :
    ∃ (V : Y.affineOpens) (U : X.affineOpens) (_ : y ∈ V.1) (hVU : V.1 ≤ f ⁻¹ᵁ U.1),
      letI : Algebra Γ(X, U.1) Γ(Y, V.1) := (f.appLE U.1 V.1 hVU).hom.toAlgebra
      ∃ (n : ℕ) (P : Algebra.Presentation Γ(X, U.1) Γ(Y, V.1) (Fin n) (Fin n))
          (hP : P.IsRelativeGlobalCompleteIntersection),
        letI := hP
        P.HasJacobianDelta
```

**`Algebra.Presentation.toMatrix_cotangentComplex_eq_relationJacobiMatrix`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean#L107). The attribute's comment: “NL\_\{B/A} is the two-term complex (f)/(f)^2 -> sum\_i B dx\_i: its differential, in the basis of the relation classes and the basis dx\_i, is the matrix df\_j/dx\_i”.

> In a basis of the conormal module given by the classes of the relations and the basis `dxᵢ`
> of the cotangent space, the differential of the naive cotangent complex is the Jacobian matrix.

```lean
theorem Presentation.toMatrix_cotangentComplex_eq_relationJacobiMatrix
    (b : Module.Basis (Fin n) B P.toExtension.Cotangent)
    (hb : ∀ i, b i = Extension.Cotangent.mk ⟨P.relation i, P.relation_mem_ker i⟩) :
    LinearMap.toMatrix b P.cotangentSpaceBasis P.toExtension.cotangentComplex =
      P.relationJacobiMatrix
```

**`Algebra.Presentation.isRankZero_cotangentComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean#L122). The attribute's comment: “the two terms of NL\_\{B/A} have equal rank, so delta(NL\_\{B/A}) is defined”.

> The naive cotangent complex of a relative global complete intersection with as many relations
> as variables has rank zero: both of its terms are free of rank the number of variables.

```lean
theorem Presentation.isRankZero_cotangentComplex :
    TwoTermComplex.IsRankZero P.toExtension.cotangentComplex
```

**`Algebra.Presentation.cotangentDeterminantBasis`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean#L131). The attribute's comment: “det(L\_\{B/A}) is free of rank one”.

> The determinant line of the naive cotangent complex of a relative global complete
> intersection with as many relations as variables, as a free module of rank one on the
> isomorphism matching a basis of the conormal module with the basis `dxᵢ`.

```lean
noncomputable def Presentation.cotangentDeterminantBasis
    (b : Module.Basis (Fin n) B P.toExtension.Cotangent) :
    Module.Basis (Fin 1) B (TwoTermComplex.determinantLine P.toExtension.cotangentComplex)
```

**`Algebra.Presentation.coe_cotangentDeterminantBasis_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean#L141). The attribute's comment: “the generator of det(L\_\{B/A}) is dx\_1 ^ ... ^ dx\_n tensor (f-bar\_1 ^ ... ^ f-bar\_n)^\{tensor -1}: it carries the wedge of the relation classes to the wedge of the dx\_i”.

> The generator of the determinant line of the naive cotangent complex carries the wedge of the
> classes of the relations to the wedge of the `dxᵢ`.

```lean
theorem Presentation.coe_cotangentDeterminantBasis_apply
    (b : Module.Basis (Fin n) B P.toExtension.Cotangent)
    (hb : ∀ i, b i = Extension.Cotangent.mk ⟨P.relation i, P.relation_mem_ker i⟩) (k : Fin 1)
    (x : ProjectiveDeterminant.module (R := B) (M := P.toExtension.Cotangent))
    (hx : (x : ExteriorAlgebra B P.toExtension.Cotangent) =
      ExteriorAlgebra.ιMulti B n
        fun j ↦ Extension.Cotangent.mk ⟨P.relation j, P.relation_mem_ker j⟩) :
    ((P.cotangentDeterminantBasis b k x :
        ProjectiveDeterminant.module (R := B) (M := P.toExtension.CotangentSpace)) :
          ExteriorAlgebra B P.toExtension.CotangentSpace) =
      ExteriorAlgebra.ιMulti B n P.cotangentSpaceBasis
```

**`Algebra.Presentation.delta_cotangentComplex_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean#L166). The attribute's comment: “delta(NL\_\{B/A}) = det(df\_j/dx\_i) . dx\_1 ^ ... ^ dx\_n tensor (f-bar\_1 ^ ... ^ f-bar\_n)^\{tensor -1}. Not a tautology: `TwoTermComplex.delta` is the pre-existing general construction `ProjectiveDeterminant.map`, defined with no reference to any Jacobian or basis, and this computes it in the two ordered bases”.

> The canonical section of the determinant line of the naive cotangent complex is the Jacobian
> determinant times the generator given by the classes of the relations and the `dxᵢ`.

```lean
theorem Presentation.delta_cotangentComplex_eq
    (b : Module.Basis (Fin n) B P.toExtension.Cotangent)
    (hb : ∀ i, b i = Extension.Cotangent.mk ⟨P.relation i, P.relation_mem_ker i⟩) (k : Fin 1) :
    TwoTermComplex.delta P.toExtension.cotangentComplex P.isRankZero_cotangentComplex =
      P.relationJacobiMatrix.det • P.cotangentDeterminantBasis b k
```

**`Algebra.Presentation.hasJacobianDelta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean#L192). The attribute's comment: “the four assertions bundled for one square relative global complete intersection presentation”.

> A relative global complete intersection presentation with as many relations as variables has
> the local Jacobian picture of the determinant of its naive cotangent complex.

```lean
theorem Presentation.hasJacobianDelta : P.HasJacobianDelta
```

Declarations registered for the tag:

- [`Algebra.Presentation.exists_basis_cotangent_relation`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/RelativeConormal.lean#L981), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CompleteIntersection/CotangentDeterminant.lean#L200) (StacksFrontier): “the conormal module (f\_1, ..., f\_n)/(f\_1, ..., f\_n)^2 is free on the classes f-bar\_i”.

## Tag 0FKD, a proposition

[Tag 0FKD](https://stacks.math.columbia.edu/tag/0FKD) in the Stacks Project.

**`AlgebraicGeometry.TateMap.existsUnique_tateRule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TateMap/TateMap.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/TateMap/TateMap.lean#L108). The attribute's comment: “the unique rule c\_\{Y/X} : det(NL\_\{Y/X}) ≅ ω\_\{Y/X} carrying δ(NL\_\{Y/X}) to τ\_\{Y/X} and compatible with restriction to opens and with base change”.

> **Stacks Project, Tag 0FKD.** There exists a unique rule that to every locally quasi-finite
> syntomic morphism of locally Noetherian schemes `Y → X` assigns an isomorphism
> `c_{Y/X} : det(NL_{Y/X}) ≅ ω_{Y/X}` such that
>
> 1. the section `δ(NL_{Y/X})` is mapped to `τ_{Y/X}`, and
> 2. the rule is compatible with restriction to opens and with base change.
>
> The source of a locally quasi-finite morphism to a locally Noetherian scheme is locally
> Noetherian, so the hypothesis is placed on the target only.

```lean
theorem existsUnique_tateRule : ∃! c : TateRule.{u}, IsTateRule c
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 49.13, Tag 0FKB](https://stacks.math.columbia.edu/tag/0FKB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

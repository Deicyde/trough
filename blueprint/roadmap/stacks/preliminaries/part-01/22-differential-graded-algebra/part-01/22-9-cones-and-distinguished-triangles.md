---
declaration: section
origin: cited
lean: DifferentialGradedModule.mappingCone_isAdmissibleShortExact, DifferentialGradedModule.associatedTriangle_mappingCone_eq, DifferentialGradedModule.rotatedAssociatedTriangle_iso_connectingConeTriangle, DifferentialGradedModule.inverseRotatedAssociatedTriangle_iso_mappingConeTriangle, DifferentialGradedModule.isIso_mappingConeMap_of_isIso, DifferentialGradedModule.mem_distinguishedConeTriangles_iff_isDistinguishedTriangle_negMor₃, DifferentialGradedModule.mem_distinguishedTriangles_admissible_iff, DifferentialGradedModule.mem_distinguishedTriangles_cone_iff
statement: formalized
proof: formalized
---

# 22.9 Cones and distinguished triangles

Section 22.9 of the Stacks Project, [Tag 09P1](https://stacks.math.columbia.edu/tag/09P1). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09KB, a lemma

[Tag 09KB](https://stacks.math.columbia.edu/tag/09KB) in the Stacks Project.

**`DifferentialGradedModule.mappingCone_isAdmissibleShortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeAdmissible.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeAdmissible.lean#L107). The attribute's comment: “the admissible short exact sequence”.

> The cone sequence `L ⟶ C(f) ⟶ K[1]` of a homomorphism of differential graded modules is an
> admissible short exact sequence.

```lean
theorem mappingCone_isAdmissibleShortExact (f : K ⟶ L) :
    IsAdmissibleShortExact (coneInclusion f) (coneProjection f)
```

**`DifferentialGradedModule.associatedTriangle_mappingCone_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeAdmissible.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeAdmissible.lean#L148). The attribute's comment: “the associated triangle”.

> The triangle of the cone sequence of `f` is the displayed triangle `L → C(f) → K[1]` whose
> connecting arrow is the shift `f[1]` of `f`.

```lean
theorem associatedTriangle_mappingCone_eq (f : K ⟶ L)
    (h : IsAdmissibleShortExact (coneInclusion f) (coneProjection f)) :
    Pretriangulated.Triangle.mk
      ((toHomotopyCategory A).map (coneInclusion f))
      ((toHomotopyCategory A).map (coneProjection f))
      ((toHomotopyCategory A).map (shiftMap f 1) ≫
        eqToHom (CategoryTheory.Quotient.functor_obj_shift (homotopyRel A) ℤ L 1).symm) =
      associatedTriangle A (coneInclusion f) (coneProjection f) h
```

## Tag 09KC, a lemma

[Tag 09KC](https://stacks.math.columbia.edu/tag/09KC) in the Stacks Project.

**`DifferentialGradedModule.rotatedAssociatedTriangle_iso_connectingConeTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeRotation.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeRotation.lean#L351). The attribute's comment: “source sign convention”.

> The rotated admissible-sequence triangle is isomorphic to the cone triangle of its
> desuspended connecting homomorphism.

```lean
theorem rotatedAssociatedTriangle_iso_connectingConeTriangle (f : K ⟶ L) (g : L ⟶ M)
    (hfg : IsAdmissibleShortExact f g) :
    Nonempty (rotatedAssociatedTriangle f g hfg ≅ connectingConeTriangle f g hfg)
```

**`DifferentialGradedModule.inverseRotatedAssociatedTriangle_iso_mappingConeTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeRotation.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeRotation.lean#L427). The attribute's comment: “standard cone sign convention”.

> The standard inverse rotation of an admissible-sequence triangle is the standard cone
> triangle of the negative desuspended connecting map.

```lean
theorem inverseRotatedAssociatedTriangle_iso_mappingConeTriangle (f : K ⟶ L) (g : L ⟶ M)
    (hfg : IsAdmissibleShortExact f g) :
    Nonempty (inverseRotatedAssociatedTriangle f g hfg ≅
      mappingConeTriangle (-desuspendedConnectingHom f g hfg))
```

## Tag 09KE, a lemma

[Tag 09KE](https://stacks.math.columbia.edu/tag/09KE) in the Stacks Project.

**`DifferentialGradedModule.isIso_mappingConeMap_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeHomotopyEquivalence.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeHomotopyEquivalence.lean#L128).

> In a morphism of cone triangles, if the maps on the source and the target of the two
> original arrows are homotopy equivalences, then so is the induced map on the cones.

```lean
theorem isIso_mappingConeMap_of_isIso
    (f₁ : K₁ ⟶ L₁) (f₂ : K₂ ⟶ L₂)
    (a : K₁ ⟶ K₂) (b : L₁ ⟶ L₂)
    (c : coneModule f₁ ⟶ coneModule f₂)
    (h₁ : Homotopic (a ≫ f₂) (f₁ ≫ b))
    (h₂ : Homotopic (b ≫ coneInclusion f₂) (coneInclusion f₁ ≫ c))
    (h₃ : Homotopic (c ≫ coneProjection f₂)
      (coneProjection f₁ ≫ shiftMap a 1))
    [IsIso ((toHomotopyCategory A).map a)]
    [IsIso ((toHomotopyCategory A).map b)] :
    IsIso ((toHomotopyCategory A).map c)
```

## Tag 09KF, a lemma

[Tag 09KF](https://stacks.math.columbia.edu/tag/09KF) in the Stacks Project.

**`DifferentialGradedModule.mem_distinguishedConeTriangles_iff_isDistinguishedTriangle_negMor₃`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/ConeSignClasses.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DGA/ConeSignClasses.lean#L138). The attribute's comment: “the two cone sign conventions against the admissible-sequence class”.

> A triangle of the homotopy category is isomorphic to a cone triangle exactly when negating
> its third arrow gives the triangle of an admissible short exact sequence: the two classes are the
> two sign conventions for the third arrow of the triangle of a homomorphism.

```lean
theorem mem_distinguishedConeTriangles_iff_isDistinguishedTriangle_negMor₃
    (T : Triangle (HomotopyCategory.{u, v, w} A)) :
    T ∈ distinguishedConeTriangles.{u, v, w} (A := A) ↔
      IsDistinguishedTriangle A (Triangle.mk T.mor₁ T.mor₂ (-T.mor₃))
```

**`DifferentialGradedModule.mem_distinguishedTriangles_admissible_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/ConeSignTransfer.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/ConeSignTransfer.lean#L162). The attribute's comment: “the admissible-sequence pretriangulated structure against the cone-triangle one”.

> **The sign comparison of the two pretriangulated structures on `K(Mod_(A, d))`.** A triangle
> is distinguished for the admissible-sequence structure
> `DifferentialGradedModule.instPretriangulatedHomotopyCategory'` exactly when negating its third
> arrow gives a triangle distinguished for the default cone-triangle structure
> `DifferentialGradedModule.instPretriangulatedHomotopyCategory`.

```lean
theorem mem_distinguishedTriangles_admissible_iff
    (T : Triangle (HomotopyCategory.{u, v, w} A)) :
    T ∈ (instPretriangulatedHomotopyCategory' A).distinguishedTriangles ↔
      Triangle.mk T.mor₁ T.mor₂ (-T.mor₃) ∈
        (instPretriangulatedHomotopyCategory (A := A)).distinguishedTriangles
```

**`DifferentialGradedModule.mem_distinguishedTriangles_cone_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/ConeSignTransfer.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/ConeSignTransfer.lean#L179). The attribute's comment: “the cone-triangle pretriangulated structure against the admissible-sequence one”.

> **The sign comparison, from the side of the default structure.** A triangle is distinguished
> for the cone-triangle structure `DifferentialGradedModule.instPretriangulatedHomotopyCategory`
> exactly when negating its third arrow gives a triangle distinguished for the admissible-sequence
> structure `DifferentialGradedModule.instPretriangulatedHomotopyCategory'`.

```lean
theorem mem_distinguishedTriangles_cone_iff
    (T : Triangle (HomotopyCategory.{u, v, w} A)) :
    T ∈ (instPretriangulatedHomotopyCategory (A := A)).distinguishedTriangles ↔
      Triangle.mk T.mor₁ T.mor₂ (-T.mor₃) ∈
        (instPretriangulatedHomotopyCategory' A).distinguishedTriangles
```

**`DifferentialGradedModule.exists_mappingConeTriangle_iso_associatedTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeTriangle.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeTriangle.lean#L376). The attribute's comment: “part (1)”. References: SGA 4 XVII (1.1.1), “DG modules over a DGA”.

> For an admissible short exact sequence, the projection of the cone onto the third term is a
> homotopy equivalence and completes the identity maps on `K` and `L` to an isomorphism from the
> cone triangle to the triangle of the sequence.

```lean
theorem exists_mappingConeTriangle_iso_associatedTriangle (f : K ⟶ L) (g : L ⟶ M)
    (hfg : IsAdmissibleShortExact f g) :
    ∃ (q : coneModule f ⟶ M),
      (∀ x : (coneModule f).M,
        q.toFun x = g.toFun ((cone f).coordinates x).1) ∧
      ∃ e : mappingConeTriangle f ≅ associatedTriangle A f g hfg,
        e.hom.hom₁ = 𝟙 _ ∧ e.hom.hom₂ = 𝟙 _ ∧
          e.hom.hom₃ = (toHomotopyCategory A).map q
```

**`DifferentialGradedModule.exists_associatedTriangle_iso_mappingConeTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeTriangle.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/MappingConeTriangle.lean#L431). The attribute's comment: “part (2)”. References: SGA 4 XVII (1.1.1), “DG modules over a DGA”.

> Every cone triangle is isomorphic to the triangle of an admissible short exact sequence, by
> the identity on the first vertex and a comparison to the original second vertex compatible with
> the given homomorphism.

```lean
theorem exists_associatedTriangle_iso_mappingConeTriangle (f : K ⟶ L) :
    ∃ (L' M' : DifferentialGradedModule A) (f' : K ⟶ L') (g' : L' ⟶ M')
      (hfg : IsAdmissibleShortExact f' g') (b : L' ⟶ L),
      f' ≫ b = f ∧
        ∃ e : associatedTriangle A f' g' hfg ≅ mappingConeTriangle f,
          e.hom.hom₁ = 𝟙 _ ∧ e.hom.hom₂ = (toHomotopyCategory A).map b
```

**`AlgebraicGeometry.RingedSite.tensorWithComplexToDerivedCategory_negMor₃_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexConeExactness.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorWithComplexConeExactness.lean#L50). The attribute's comment: “the sign that relates the two classes of triangles”.

> The image in `D(O)` of a triangle isomorphic to a cone triangle of `K(Mod_(E, d))` is
> distinguished once its third arrow is negated: that negation turns a cone triangle into the
> triangle of an admissible short exact sequence, which tensoring with `K` keeps distinguished.

```lean
theorem tensorWithComplexToDerivedCategory_negMor₃_distinguished
    (T : Triangle (DifferentialGradedModule.HomotopyCategory.{0, max u v w t s, max u v w t s}
      (Rep.{u, v, w, t, s, 0} X ℤ K).algebra))
    (hT : T ∈ distinguishedConeTriangles.{0, max u v w t s, max u v w t s}
      (A := (Rep.{u, v, w, t, s, 0} X ℤ K).algebra)) :
    (tensorWithComplexToDerivedCategory.{u, v, w, t, s, 0} X ℤ K).mapTriangle.obj
        (Triangle.mk T.mor₁ T.mor₂ (-T.mor₃)) ∈
      distTriang (DerivedCategory (TensorModO.{u, v, w, t, s} X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.9, Tag 09P1](https://stacks.math.columbia.edu/tag/09P1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

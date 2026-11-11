---
declaration: section
origin: cited
lean: CategoryTheory.nonempty_serreEquivalence_iff, CategoryTheory.SerreEquivalence, AlgebraicGeometry.diagonalPeriodicityEquiv, AlgebraicGeometry.diagonalPeriodicityEquiv_d₁, AlgebraicGeometry.diagonalPeriodicityEquiv_d₂, AlgebraicGeometry.HomDoubleComplexSetup.d₁_exact, AlgebraicGeometry.HomDoubleComplexSetup.d₂_exact, AlgebraicGeometry.HomDoubleComplexSetup.d₁_comp_d₁
statement: formalized
proof: formalized
---

# 57.3 Serre functors

Section 57.3 of the Stacks Project, [Tag 0FY3](https://stacks.math.columbia.edu/tag/0FY3). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FY4, a lemma

[Tag 0FY4](https://stacks.math.columbia.edu/tag/0FY4) in the Stacks Project.

**`CategoryTheory.nonempty_serreEquivalence_iff`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Basic.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Basic.lean#L533).

> **Stacks Project, Tag 0FY4.** A Hom-finite linear category admits a Serre equivalence
> exactly when both dual Hom functors are representable in the appropriate variance.

```lean
lemma nonempty_serreEquivalence_iff
    [∀ X Y : C, FiniteDimensional k (X ⟶ Y)] :
    Nonempty (SerreEquivalence k (C := C)) ↔
      (∀ X : C,
        (homDualPresheaf k X ⋙ forget (ModuleCat.{max u w} k)).IsRepresentable) ∧
        (∀ X : C,
          (homDualCopresheaf k X ⋙ forget (ModuleCat.{max u w} k)).IsCorepresentable)
```

## Tag 0FY5, a definition

[Tag 0FY5](https://stacks.math.columbia.edu/tag/0FY5) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.SerreEquivalence`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Basic.lean#L100), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Basic.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Basic.lean#L117) (StacksFrontier).

## Tag 0H8B, a remark

[Tag 0H8B](https://stacks.math.columbia.edu/tag/0H8B) in the Stacks Project.

**`AlgebraicGeometry.diagonalPeriodicityEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/DiagonalPeriodicity.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/DiagonalPeriodicity.lean#L85). The attribute's comment: “diagonal\_periodicity”.

> The diagonal three-periodicity identification in the Hom double-complex of two
> distinguished triangles.

```lean
noncomputable def diagonalPeriodicityEquiv
    (K : HomDoubleComplexSetup (C := C)) (p q : ℤ) :
    K.term p q ≃+ K.term (p + 3) (q - 3)
```

**`AlgebraicGeometry.diagonalPeriodicityEquiv_d₁`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/DiagonalPeriodicity.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/DiagonalPeriodicity.lean#L385). The attribute's comment: “diagonal\_periodicity”.

> The diagonal periodicity identification commutes with the first differential.

```lean
lemma diagonalPeriodicityEquiv_d₁
    (K : HomDoubleComplexSetup (C := C)) (p q : ℤ) (f : K.term p q) :
    cast (congrArg (fun i => K.term i (q - 3)) (by omega))
        (diagonalPeriodicityEquiv K (p + 1) q (K.d₁ p q f)) =
      K.d₁ (p + 3) (q - 3) (diagonalPeriodicityEquiv K p q f)
```

**`AlgebraicGeometry.diagonalPeriodicityEquiv_d₂`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/DiagonalPeriodicity.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/DiagonalPeriodicity.lean#L417). The attribute's comment: “diagonal\_periodicity”.

> The diagonal periodicity identification commutes with the second differential.

```lean
lemma diagonalPeriodicityEquiv_d₂
    (K : HomDoubleComplexSetup (C := C)) (p q : ℤ) (f : K.term p q) :
    cast (congrArg (K.term (p + 3)) (by omega))
        (diagonalPeriodicityEquiv K p (q + 1) (K.d₂ p q f)) =
      K.d₂ (p + 3) (q - 3) (diagonalPeriodicityEquiv K p q f)
```

**`AlgebraicGeometry.HomDoubleComplexSetup.d₁_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/ExactRowsColumns.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/ExactRowsColumns.lean#L228). The attribute's comment: “exact\_rows\_columns”.

> Consecutive horizontal differentials in the Hom double complex are exact.

```lean
theorem d₁_exact (K : HomDoubleComplexSetup (C := C)) (p q : ℤ) :
    Function.Exact (K.d₁ p q) (K.d₁ (p + 1) q)
```

**`AlgebraicGeometry.HomDoubleComplexSetup.d₂_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/ExactRowsColumns.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/ExactRowsColumns.lean#L243). The attribute's comment: “exact\_rows\_columns”.

> Consecutive vertical differentials in the Hom double complex are exact.

```lean
theorem d₂_exact (K : HomDoubleComplexSetup (C := C)) (p q : ℤ) :
    Function.Exact (K.d₂ p q) (K.d₂ p (q + 1))
```

**`AlgebraicGeometry.HomDoubleComplexSetup.d₁_comp_d₁`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplex.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplex.lean#L245). The attribute's comment: “hom\_double\_complex: the horizontal differential squares to zero”.

> Consecutive horizontal differentials in the Hom double complex compose to zero.

```lean
lemma d₁_comp_d₁ (K : HomDoubleComplexSetup (C := C)) (p q : ℤ) :
    AddCommGrpCat.ofHom (K.d₁ p q) ≫ AddCommGrpCat.ofHom (K.d₁ (p + 1) q) = 0
```

**`AlgebraicGeometry.HomDoubleComplexSetup.d₂_comp_d₂`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplex.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplex.lean#L262). The attribute's comment: “hom\_double\_complex: the vertical differential squares to zero”.

> Consecutive vertical differentials in the Hom double complex compose to zero.

```lean
lemma d₂_comp_d₂ (K : HomDoubleComplexSetup (C := C)) (p q : ℤ) :
    AddCommGrpCat.ofHom (K.d₂ p q) ≫ AddCommGrpCat.ofHom (K.d₂ p (q + 1)) = 0
```

**`AlgebraicGeometry.HomDoubleComplexSetup.d₂_comp_d₁`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplex.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplex.lean#L272). The attribute's comment: “hom\_double\_complex: the two differentials commute”.

> The horizontal and vertical differentials in the Hom double complex commute.

```lean
lemma d₂_comp_d₁ (K : HomDoubleComplexSetup (C := C)) (p q : ℤ) :
    AddCommGrpCat.ofHom (K.d₂ p q) ≫ AddCommGrpCat.ofHom (K.d₁ p (q + 1)) =
      AddCommGrpCat.ofHom (K.d₁ p q) ≫ AddCommGrpCat.ofHom (K.d₂ (p + 1) q)
```

**`AlgebraicGeometry.HomDoubleComplexSetup.homDoubleComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplex.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplex.lean#L283). The attribute's comment: “hom\_double\_complex”.

> The double complex of abelian groups obtained from a pair of distinguished triangles.

```lean
noncomputable def homDoubleComplex (K : HomDoubleComplexSetup (C := C)) :
    HomologicalComplex₂.DoubleComplex AddCommGrpCat
```

**`AlgebraicGeometry.HomDoubleComplexSetup.exists_fill`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplexMatress.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplexMatress.lean#L59). The attribute's comment: “the filling property of the Hom double complex, i.e. axiom TR3 in the form the remark states it”.

> **Stacks 0H8B.** The filling property of the Hom double complex: a commuting square between
> two three-periodic sequences of distinguished triangles extends one step further along the
> diagonal, where it closes up with the periodicity identification. This is axiom TR3.

```lean
theorem exists_fill (K : HomDoubleComplexSetup (C := C)) (a q : ℤ)
    (α : triangleObject K.X a ⟶ triangleObject K.Y q)
    (β : triangleObject K.X (a + 1) ⟶ triangleObject K.Y (q + 1))
    (hαβ : triangleMap K.X a ≫ β = α ≫ triangleMap K.Y q) :
    ∃ γ : triangleObject K.X (a + 2) ⟶ triangleObject K.Y (q + 2),
      (triangleMap K.X (a + 1) ≫
          eqToHom (congrArg (triangleObject K.X) (show a + 1 + 1 = a + 2 by omega))) ≫ γ =
        β ≫ triangleMap K.Y (q + 1) ≫
          eqToHom (congrArg (triangleObject K.Y) (show q + 1 + 1 = q + 2 by omega)) ∧
      (triangleObjectPeriodicityIso K.X (a + 2)).hom ≫
          (γ ≫ triangleMap K.Y (q + 2) ≫
            eqToHom (congrArg (triangleObject K.Y)
              (show q + 2 + 1 = q + 3 by omega)))⟦(-1 : ℤ)⟧' ≫
          (triangleObjectPeriodicityIso K.Y (q + 3)).inv =
        -(triangleMap K.X (a + 2 - 3) ≫
          eqToHom (congrArg (triangleObject K.X) (show a + 2 - 3 + 1 = a by omega)) ≫ α ≫
          eqToHom (congrArg (triangleObject K.Y) (show q = q + 3 - 3 by omega)))
```

**`AlgebraicGeometry.HomDoubleComplexSetup.homDoubleComplexMatress`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplexMatress.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/HomDoubleComplexMatress.lean#L196). The attribute's comment: “the whole remark for the Hom double complex of two distinguished triangles: the matress structure, so exact rows and columns, three-periodicity compatible with both differentials, and the TR3 filling condition”.

> **Stacks 0H8B.** The double complex of morphism groups between the three-periodic sequences
> of two distinguished triangles is a matress: its rows and columns are exact, it is three-periodic
> compatibly with both differentials, and it satisfies the filling condition.

```lean
noncomputable def homDoubleComplexMatress (K : HomDoubleComplexSetup (C := C)) :
    HomologicalComplex₂.Matress (homDoubleComplex K)
```

**`HomologicalComplex₂.Matress`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Matress.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Matress.lean#L64). The attribute's comment: “matress”.

> **Stacks Project, Tag 0H8B.** A matress structure on a concrete double complex of abelian
> groups: its rows and columns are exact, it is compatibly three-periodic, and every compatible
> pair on a diagonal admits the prescribed filling.

```lean
structure Matress (K : HomologicalComplex₂.DoubleComplex C)
```

**`AlgebraicGeometry.segmentTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/SegmentTriangle.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/SegmentTriangle.lean#L327). The attribute's comment: “the shifting the remark appeals to: three consecutive steps of a three-periodic sequence form a distinguished triangle, so TR3 applies in every degree”.

> **Stacks 0H8B.** Three consecutive steps of the three-periodic sequence of a distinguished
> triangle form a distinguished triangle.

```lean
theorem segmentTriangle_distinguished (T : Triangle C) (hT : T ∈ distTriang C) (p : ℤ) :
    segmentTriangle T p ∈ distTriang C
```

## Tag 0H8C, a remark

[Tag 0H8C](https://stacks.math.columbia.edu/tag/0H8C) in the Stacks Project.

**`Stacks.DerivedEquivalence.exists_dual_matress`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/MatressDual.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/MatressDual.lean#L444).

> **Stacks 0H8C.** The dual of a finite-dimensional matress is a matress.

```lean
public theorem exists_dual_matress (k : Type u) [Field k]
    (K : HomologicalComplex₂.DoubleComplex (ModuleCat.{max u v} k))
    [∀ p q : ℤ, FiniteDimensional k (K.X p q)]
    (hK : HomologicalComplex₂.Matress K) :
    ∃ L : HomologicalComplex₂.DoubleComplex (ModuleCat.{max u v} k),
      (∀ p q : ℤ, L.X p q = ModuleCat.of k (Module.Dual k (K.X (-q) (-p)))) ∧
      (∀ p q : ℤ,
        HEq (L.d₁ p q)
          (ModuleCat.ofHom (K.d₂ (-q) (-p - 1)).hom.dualMap)) ∧
      (∀ p q : ℤ,
        HEq (L.d₂ p q)
          (ModuleCat.ofHom (K.d₁ (-q - 1) (-p)).hom.dualMap)) ∧
      Nonempty (HomologicalComplex₂.Matress L)
```

## Tag 0FY6, a lemma

[Tag 0FY6](https://stacks.math.columbia.edu/tag/0FY6) in the Stacks Project.

**`CategoryTheory.serreEquivalence_exists_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Exactness.lean, line 620](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Exactness.lean#L620). The attribute's comment: “serre\_functor\_exact”.

> **Stacks Project, Tag 0FY6.** A Serre equivalence has a coherent translation isomorphism
> under which it is an exact functor of triangulated categories.

```lean
theorem serreEquivalence_exists_isTriangulated
    (S : SerreEquivalence k (C := C)) :
    ∃ commShift : S.equivalence.functor.CommShift ℤ,
      letI := commShift
      S.equivalence.functor.IsTriangulated
```

**`CategoryTheory.serreEquivalence_uniqueUpToUniqueIso`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Uniqueness.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/SerreFunctors/Uniqueness.lean#L167). The attribute's comment: “serre\_functor\_unique”.

> **Stacks Project, Tag 0FY6.** Two Serre functors have a unique natural isomorphism
> preserving their Serre pairings.

```lean
lemma serreEquivalence_uniqueUpToUniqueIso
    (S T : SerreEquivalence k (C := C)) :
    ∃! α : S.equivalence.functor ≅ T.equivalence.functor,
      ∀ (X Y : C) (f : X ⟶ Y) (g : Y ⟶ S.equivalence.functor.obj X),
        S.pairing X Y f g = T.pairing X Y f (g ≫ α.hom.app X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.3, Tag 0FY3](https://stacks.math.columbia.edu/tag/0FY3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

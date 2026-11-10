---
declaration: section
origin: cited
lean: DifferentialGradedModule.connectingHom_gradedSplit, CochainComplex.gradedSplitOfDegreewiseSplit, CochainComplex.connectingHom_gradedSplitOfDegreewiseSplit, CochainComplex.dgShiftComparisonData, DGCategory.GradedSplitShortExact.connectingHom, DGCategory.GradedSplitShortExact.connectingHom_eq_neg_d_comp, DGCategory.GradedSplitShortExact.connectingHom_closed, DGCategory.GradedSplitShortExact.comp_zero
statement: formalized
proof: formalized
---

# 22.27 Obtaining triangulated categories

Section 22.27 of the Stacks Project, [Tag 09P5](https://stacks.math.columbia.edu/tag/09P5). 17 tags here are carried by 43 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09P6, a lemma

[Tag 09P6](https://stacks.math.columbia.edu/tag/09P6) in the Stacks Project.

**`DifferentialGradedModule.connectingHom_gradedSplit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/GradedSplitAdmissible.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/GradedSplitAdmissible.lean#L143). The attribute's comment: “the connecting morphism of a graded splitting is the connecting homomorphism”.

> **The connecting homomorphism of the admissible sequence is the connecting morphism of the
> graded splitting.** Both are `π d(s)`: the Hom differential of the differential graded category
> is the graded commutator `d ∘ s - s ∘ d`, and its second term is killed by `π ∘ s = 0`.

```lean
theorem connectingHom_gradedSplit (z : Z.M) :
    (connectingHom (homOfCocycle A E.a) (homOfCocycle A E.b)
        (isAdmissibleShortExact_gradedSplit A E)
        (gradedSplitS A E) (gradedSplitPi A E)
        (gradedSplit_b_s A E) (gradedSplit_pi_a A E)
        (compatibleSplittings_gradedSplit A E).hker).val.toFun z =
      (DGCategory.GradedSplitShortExact.connectingHom E).1 z
```

**`CochainComplex.gradedSplitOfDegreewiseSplit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexGradedSplit.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexGradedSplit.lean#L102). The attribute's comment: “a degreewise split short exact sequence of complexes”.

> **A degreewise split short complex of cochain complexes is a graded-split short exact
> sequence of the differential graded category of complexes.**

```lean
def gradedSplitOfDegreewiseSplit :
    DGCategory.GradedSplitShortExact (A := dgCategory B) S.X₁ S.X₂ S.X₃
```

**`CochainComplex.connectingHom_gradedSplitOfDegreewiseSplit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexGradedSplit.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexGradedSplit.lean#L163). The attribute's comment: “the connecting morphism of a degreewise split sequence of complexes”.

> **The connecting morphism of a degreewise split sequence of complexes is Mathlib's
> `CochainComplex.cocycleOfDegreewiseSplit`.** The Hom differential of `s` is the graded
> commutator `s ≫ d - d ≫ s`, and its second term dies against `π` because `π ∘ s = 0`, leaving
> `(σ p).s ≫ d ≫ (σ q).r`.

```lean
theorem connectingHom_gradedSplitOfDegreewiseSplit :
    DGCategory.GradedSplitShortExact.connectingHom (gradedSplitOfDegreewiseSplit S σ) =
      (cocycleOfDegreewiseSplit S σ).1
```

**`CochainComplex.dgShiftComparisonData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexShiftComparison.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/CochainComplexShiftComparison.lean#L111). The attribute's comment: “axiom (B)'s identification of Hom complexes, for complexes”.

> **Mathlib's shift supplies axiom (B)'s identification of Hom modules for the differential
> graded category of complexes.** A degree `k + n` cochain `X ⟶ Y` is a degree `k` cochain
> `X ⟶ Y[n]`; the identification multiplies the Hom differential by `(-1)^n` and leaves
> composition on the right alone.

```lean
noncomputable def dgShiftComparisonData :
    DGCategory.ShiftComparisonData (dgCategory B)
```

**`DGCategory.GradedSplitShortExact.connectingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L165). The attribute's comment: “the connecting morphism”.

> The connecting morphism `π d(s)`, as a homogeneous morphism of degree one.

```lean
public def connectingHom {x y z : A.Obj} (E : GradedSplitShortExact (A := A) x y z) :
    A.Hom z x 1
```

**`DGCategory.GradedSplitShortExact.connectingHom_eq_neg_d_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L282). The attribute's comment: “alternative formula for the connecting morphism”.

> The alternative formula `δ = -d(π)s` for the connecting morphism.

```lean
public theorem connectingHom_eq_neg_d_comp {x y z : A.Obj}
    (E : GradedSplitShortExact (A := A) x y z) :
    connectingHom E =
      -A.comp (by omega : (0 + 1 : ℤ) + 0 = 1) (A.d E.π) E.s
```

**`DGCategory.GradedSplitShortExact.connectingHom_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L290). The attribute's comment: “the connecting morphism is closed”.

> The connecting morphism is a cocycle.

```lean
public theorem connectingHom_closed {x y z : A.Obj}
    (E : GradedSplitShortExact (A := A) x y z) : A.d (connectingHom E) = 0
```

**`DGCategory.GradedSplitShortExact.comp_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L300). The attribute's comment: “the first consecutive composite”.

> The composite `x ⟶ y ⟶ z` is zero.

```lean
public theorem comp_zero {x y z : A.Obj}
    (E : GradedSplitShortExact (A := A) x y z) :
    A.comp (by omega : (0 : ℤ) + 0 = 0) E.b.1 E.a.1 = 0
```

**`DGCategory.GradedSplitShortExact.comp_connectingHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L338). The attribute's comment: “the third consecutive composite”.

> The composite `z ⟶ x[1] ⟶ y[1]` is the boundary `d(s)` before shifting.

```lean
public theorem comp_connectingHom {x y z : A.Obj}
    (E : GradedSplitShortExact (A := A) x y z) :
    A.comp (by omega : (0 : ℤ) + 1 = 1) E.a.1 (connectingHom E) = A.d E.s
```

**`DGCategory.GradedSplitShortExact.connectingHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L345). The attribute's comment: “the second consecutive composite”.

> The composite `y ⟶ z ⟶ x[1]` is the boundary `d(-π)` before shifting.

```lean
public theorem connectingHom_comp {x y z : A.Obj}
    (E : GradedSplitShortExact (A := A) x y z) :
    A.comp (by omega : (1 : ℤ) + 0 = 1) (connectingHom E) E.b.1 = A.d (-E.π)
```

**`DGCategory.GradedSplitShortExact.connecting_shift_closed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L353). The attribute's comment: “closed connecting map into the shift”.

> The degree-one connecting cocycle remains closed after conversion to a map into
> the shifted object.

```lean
public theorem connecting_shift_closed {x y z : A.Obj}
    (S : ShiftAxiomB A) (E : GradedSplitShortExact (A := A) x y z) :
    A.d ((S.toShift 1 z x 0) (connectingHom E)) = 0
```

**`DGCategory.GradedSplitShortExact.connectingCocycle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L366). The attribute's comment: “the triangle's connecting arrow”.

> The actual connecting arrow `z ⟶ x[1]` in `Comp(A)`.

```lean
public def connectingCocycle {x y z : A.Obj}
    (S : ShiftAxiomB A) (E : GradedSplitShortExact (A := A) x y z) :
    A.Cocycle z ((S.shiftFunctor 1).obj x)
```

**`DGCategory.GradedSplitShortExact.associatedCompTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L384). The attribute's comment: “the associated triangle in the category of complexes”.

> The associated triangle in the category of complexes, with the arrow
> `z ⟶ x[1]` given by `π d(s)`.

```lean
public def associatedCompTriangle {x y z : A.Obj}
    (S : ShiftAxiomB A) (E : GradedSplitShortExact (A := A) x y z) :
    letI : HasShift A.Comp ℤ := S.compShift
    Pretriangulated.Triangle A.Comp
```

**`DGCategory.GradedSplitShortExact.associatedKTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L397). The attribute's comment: “the associated triangle in the homotopy category”.

> The same triangle, regarded in the homotopy category.

```lean
public def associatedKTriangle {x y z : A.Obj}
    (S : ShiftAxiomB A) (E : GradedSplitShortExact (A := A) x y z) :
    letI : HasShift A.K ℤ := S.kShift
    Pretriangulated.Triangle A.K
```

**`DGCategory.GradedSplitShortExact.first_comp_zero_in_K`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L413). The attribute's comment: “first composite vanishes in the homotopy category”.

> The first two arrows compose to zero in the homotopy category.

```lean
public theorem first_comp_zero_in_K {x y z : A.Obj}
    (E : GradedSplitShortExact (A := A) x y z) :
    A.compK (Quotient.mk (A.homotopySetoid y z) E.b)
      (Quotient.mk (A.homotopySetoid x y) E.a) =
    Quotient.mk (A.homotopySetoid x z)
      (⟨0, A.d_zero⟩ : A.Cocycle x z)
```

**`DGCategory.GradedSplitShortExact.connecting_comp_zero_in_K`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L436). The attribute's comment: “second composite vanishes in the homotopy category”.

> The composite `y ⟶ z ⟶ x[1]` is zero in `K(A)`.

```lean
public theorem connecting_comp_zero_in_K {x y z : A.Obj}
    (S : ShiftAxiomB A)
    (E : GradedSplitShortExact (A := A) x y z) :
    A.compK (Quotient.mk (A.homotopySetoid z ((S.shiftFunctor 1).obj x))
        (connectingCocycle S E))
      (Quotient.mk (A.homotopySetoid y z) E.b) =
    Quotient.mk (A.homotopySetoid y ((S.shiftFunctor 1).obj x))
      (⟨0, A.d_zero⟩ : A.Cocycle y ((S.shiftFunctor 1).obj x))
```

**`DGCategory.GradedSplitShortExact.comp_connecting_zero_in_K`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L465). The attribute's comment: “third composite vanishes in the homotopy category”.

> The composite `z ⟶ x[1] ⟶ y[1]` is zero in `K(A)`.

```lean
public theorem comp_connecting_zero_in_K {x y z : A.Obj}
    (S : ShiftAxiomB A)
    (E : GradedSplitShortExact (A := A) x y z) :
    A.compK (Quotient.mk (A.homotopySetoid ((S.shiftFunctor 1).obj x)
        ((S.shiftFunctor 1).obj y)) ((S.shiftFunctor 1).mapCocycle E.a))
      (Quotient.mk (A.homotopySetoid z ((S.shiftFunctor 1).obj x))
        (connectingCocycle S E)) =
    Quotient.mk (A.homotopySetoid z ((S.shiftFunctor 1).obj y))
      (⟨0, A.d_zero⟩ : A.Cocycle z ((S.shiftFunctor 1).obj y))
```

**`DGCategory.GradedSplitShortExact.shifted_connecting_comp_zero_in_K`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Triangulated.lean#L527). The attribute's comment: “rotated composite vanishes in the homotopy category”.

> The rotated composite `z[-1] ⟶ x ⟶ y` is zero in `K(A)`.

```lean
public theorem shifted_connecting_comp_zero_in_K {x y z : A.Obj}
    (S : ShiftAxiomB A)
    (E : GradedSplitShortExact (A := A) x y z) :
    A.compK (Quotient.mk (A.homotopySetoid x y) E.a)
      (Quotient.mk (A.homotopySetoid ((S.shiftFunctor (-1)).obj z) x)
        (shiftedConnecting S E)) =
    Quotient.mk (A.homotopySetoid ((S.shiftFunctor (-1)).obj z) y)
      (⟨0, A.d_zero⟩ : A.Cocycle ((S.shiftFunctor (-1)).obj z) y)
```

## Tag 09QJ, a situation

[Tag 09QJ](https://stacks.math.columbia.edu/tag/09QJ) in the Stacks Project.

**`DGCategory.ConeSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ConeSituation.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ConeSituation.lean#L37).

> Axioms (A), (B), and (C) for a differential graded category. For every closed degree-zero
> arrow `f : x ⟶ y`, the sequence `y ⟶ c(f) ⟶ x[1]` is admissible and its connecting arrow
> `x[1] ⟶ y[1]` is `f[1]`.

```lean
structure ConeSituation {R : Type w} [CommRing R] (A : DGCategory.{v, u} R)
```

## Tag 09P7, a lemma

[Tag 09P7](https://stacks.math.columbia.edu/tag/09P7) in the Stacks Project.

**`DGCategory.exists_coneTriangleMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ConeMorphism.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ConeMorphism.lean#L254).

> A homotopy-commutative square of complexes induces a morphism of their cone triangles, whose
> cone component has a representative in the category of complexes.

```lean
theorem exists_coneTriangleMorphism (S : ConeSituation A)
    {x₁ y₁ x₂ y₂ : A.Obj}
    (f₁ : A.Cocycle x₁ y₁) (f₂ : A.Cocycle x₂ y₂)
    (a : A.Cocycle x₁ x₂) (b : A.Cocycle y₁ y₂)
    (hcomm : A.compK (Quotient.mk (A.homotopySetoid y₁ y₂) b)
        (Quotient.mk (A.homotopySetoid x₁ y₁) f₁) =
      A.compK (Quotient.mk (A.homotopySetoid x₂ y₂) f₂)
        (Quotient.mk (A.homotopySetoid x₁ x₂) a)) :
    ∃ c : A.Cocycle (S.cone f₁) (S.cone f₂),
      (A.compK
          (Quotient.mk (A.homotopySetoid (S.cone f₁) (S.cone f₂)) c)
          (Quotient.mk (A.homotopySetoid y₁ (S.cone f₁)) (S.coneSequence f₁).a) =
        A.compK
          (Quotient.mk (A.homotopySetoid y₂ (S.cone f₂)) (S.coneSequence f₂).a)
          (Quotient.mk (A.homotopySetoid y₁ y₂) b)) ∧
      (A.compK
          (Quotient.mk (A.homotopySetoid (S.cone f₂)
            ((S.shift.shiftFunctor 1).obj x₂)) (S.coneSequence f₂).b)
          (Quotient.mk (A.homotopySetoid (S.cone f₁) (S.cone f₂)) c) =
        A.compK
          (Quotient.mk (A.homotopySetoid ((S.shift.shiftFunctor 1).obj x₁)
            ((S.shift.shiftFunctor 1).obj x₂))
            ((S.shift.shiftFunctor 1).mapCocycle a))
          (Quotient.mk (A.homotopySetoid (S.cone f₁)
            ((S.shift.shiftFunctor 1).obj x₁)) (S.coneSequence f₁).b))
```

## Tag 09QK, a lemma

[Tag 09QK](https://stacks.math.columbia.edu/tag/09QK) in the Stacks Project.

**`DGCategory.id_cone_homotopic_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ConeMorphism.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ConeMorphism.lean#L404).

> The identity of the cone of an identity morphism is homotopic to zero.

```lean
theorem id_cone_homotopic_zero (S : ConeSituation A) (x : A.Obj) :
    let c := S.cone (⟨A.id x, A.d_id x⟩ : A.Cocycle x x)
    A.Homotopic (⟨A.id c, A.d_id c⟩ : A.Cocycle c c) (⟨0, A.d_zero⟩ : A.Cocycle c c)
```

## Tag 09QL, a lemma

[Tag 09QL](https://stacks.math.columbia.edu/tag/09QL) in the Stacks Project.

**`DGCategory.exists_rectification_of_isAdmissibleMono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Rectification.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Rectification.lean#L66). The attribute's comment: “adjust\_right”.

> Rectify the right arrow of a homotopy-commutative square along an admissible
> monomorphism.

```lean
theorem exists_rectification_of_isAdmissibleMono {x y z w : A.Obj}
    (f : A.Cocycle x y) (a : A.Cocycle x z) (b : A.Cocycle y w) (g : A.Cocycle z w)
    (hcomm : A.Homotopic (A.compCocycle b f) (A.compCocycle g a))
    (hf : IsAdmissibleMono f) :
    ∃ b' : A.Cocycle y w,
      A.Homotopic b b' ∧ A.compCocycle b' f = A.compCocycle g a
```

**`DGCategory.exists_rectification_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Rectification.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Rectification.lean#L87). The attribute's comment: “adjust\_left”.

> Rectify the left arrow of a homotopy-commutative square along an admissible epimorphism,
> presented by a degree-zero section of its lower horizontal arrow.

```lean
theorem exists_rectification_left (C : ConeSituation A) (S : HomotopyCommutativeSquare C)
    (hg : ∃ s : A.Hom S.w S.z 0,
      A.comp (show (0 : ℤ) + 0 = 0 by omega) S.g.1 s = A.id S.w) :
    ∃ a' : A.Cocycle S.x S.z,
      A.Homotopic S.a a' ∧ A.compCocycle S.g a' = A.compCocycle S.b S.f
```

## Tag 09QM, a lemma

[Tag 09QM](https://stacks.math.columbia.edu/tag/09QM) in the Stacks Project.

**`DGCategory.exists_admissibleMono_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/AdmissibleMonoFactorization.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/AdmissibleMonoFactorization.lean#L351).

> Every morphism in the category of complexes factors through an admissible monomorphism
> followed by a retraction admitting a strict section and a homotopy inverse.

```lean
public theorem exists_admissibleMono_factorization
    {R : Type w} [CommRing R] {A : DGCategory.{v, u} R}
    (S : ConeSituation A) {x y : A.Obj} (α : A.Cocycle x y) :
    ∃ (y' z : A.Obj) (E : GradedSplitShortExact (A := A) x y' z)
      (π : A.Cocycle y' y) (s : A.Cocycle y y'),
      (A.compCocycle π E.a = α) ∧
      (A.compCocycle π s = (⟨A.id y, A.d_id y⟩ : A.Cocycle y y)) ∧
      A.Homotopic (A.compCocycle s π)
        (⟨A.id y', A.d_id y'⟩ : A.Cocycle y' y')
```

## Tag 09QN, a lemma

[Tag 09QN](https://stacks.math.columbia.edu/tag/09QN) in the Stacks Project.

**`DGCategory.exists_admissibleMono_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/AdmissibleMonoFactorization.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/AdmissibleMonoFactorization.lean#L515).

> A finite chain of maps in the category of complexes has a commuting replacement by
> admissible monomorphisms, with a homotopy equivalence at every vertex.

```lean
public theorem exists_admissibleMono_sequence {R : Type w} [CommRing R]
    (A : DGCategory.{v, u} R) (S : ConeSituation A) (n : ℕ)
    (x : Fin (n + 1) → A.Comp)
    (f : ∀ i : Fin n, x i.castSucc ⟶ x i.succ) :
    ∃ (y : Fin (n + 1) → A.Comp)
      (g : ∀ i : Fin n, y i.castSucc ⟶ y i.succ)
      (p : ∀ i : Fin (n + 1), y i ⟶ x i),
      (∀ i : Fin n,
        ∃ z : A.Obj, ∃ E : GradedSplitShortExact (A := A)
          (y i.castSucc) (y i.succ) z, E.a = g i) ∧
      (∀ i : Fin (n + 1), IsIso ((A.compToK).map (p i))) ∧
      (∀ i : Fin n, g i ≫ p i.succ = p i.castSucc ≫ f i)
```

## Tag 09QP, a lemma

[Tag 09QP](https://stacks.math.columbia.edu/tag/09QP) in the Stacks Project.

**`DGCategory.comp_homotopic_zero_of_gradedSplitShortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/AdmissibleNullHomotopy.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/AdmissibleNullHomotopy.lean#L109).

> Two morphisms whose composites with opposite sides of an admissible short exact sequence
> vanish up to homotopy have null-homotopic composite.

```lean
theorem comp_homotopic_zero_of_gradedSplitShortExact {x y z y₁ y₃ : A.Obj}
    (E : GradedSplitShortExact (A := A) x y z)
    (b : A.Cocycle y₁ y) (b' : A.Cocycle y y₃)
    (hb : A.Homotopic (A.compCocycle E.b b) ⟨0, A.d_zero⟩)
    (hb' : A.Homotopic (A.compCocycle b' E.a) ⟨0, A.d_zero⟩) :
    A.Homotopic (A.compCocycle b' b) ⟨0, A.d_zero⟩
```

## Tag 09QQ, a lemma

[Tag 09QQ](https://stacks.math.columbia.edu/tag/09QQ) in the Stacks Project.

**`DGCategory.associatedKTriangle_eq_of_same_sequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/TriangleIndependence.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/TriangleIndependence.lean#L139).

> Changing the graded splitting of an admissible short exact sequence does not change its
> associated triangle in the homotopy category.

```lean
theorem associatedKTriangle_eq_of_same_sequence {x y z : A.Obj} (S : ShiftAxiomB A)
    (E E' : GradedSplitShortExact (A := A) x y z) (ha : E.a = E'.a) (hb : E.b = E'.b) :
    GradedSplitShortExact.associatedKTriangle S E =
      GradedSplitShortExact.associatedKTriangle S E'
```

## Tag 09QR, a lemma

[Tag 09QR](https://stacks.math.columbia.edu/tag/09QR) in the Stacks Project.

**`DGCategory.associatedCompTriangle_coneSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/RotatedConeTriangle.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/RotatedConeTriangle.lean#L60). The attribute's comment: “the statement in `Comp(A)`: the triangle associated to the cone sequence of `f` is the triangle on `y`, `c(f)`, `x[1]` whose first two arrows are that sequence's inclusion and projection and whose connecting arrow is `f[1]`. The homotopy-category form is `associatedKTriangle_coneSequence`; neither covers the comparison with the cone triangle of `f` (Tag 09QU) nor the rotation of this triangle (Tag 09QS)”.

> Let `f : x ⟶ y` be a morphism in `Comp(𝒜)`. The triangle `(y, c(f), x[1], i, p, f[1])` is
> the triangle associated to the admissible short exact sequence `y ⟶ c(f) ⟶ x[1]`.

```lean
theorem associatedCompTriangle_coneSequence (C : ConeSituation A) {x y : A.Obj}
    (f : A.Cocycle x y) :
    letI : HasShift A.Comp ℤ := C.shift.compShift
    GradedSplitShortExact.associatedCompTriangle C.shift (C.coneSequence f) =
      Pretriangulated.Triangle.mk
        ((C.coneSequence f).a : (show A.Comp from y) ⟶ (show A.Comp from C.cone f))
        ((C.coneSequence f).b :
          (show A.Comp from C.cone f) ⟶
            (show A.Comp from (C.shift.shiftFunctor 1).obj x))
        (((C.shift.shiftFunctor 1).mapCocycle f :
            (show A.Comp from (C.shift.shiftFunctor 1).obj x) ⟶
              (show A.Comp from (C.shift.shiftFunctor 1).obj y)) ≫
          eqToHom (congrArg (fun F : A.Comp ⥤ A.Comp => F.obj y)
            (C.shift.compShift_functor 1)).symm)
```

**`DGCategory.associatedKTriangle_coneSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/RotatedConeTriangle.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/RotatedConeTriangle.lean#L86). The attribute's comment: “the statement in `K(A)`: the triangle associated to the cone sequence of `f` is the triangle on `y`, `c(f)`, `x[1]` whose first two arrows are the homotopy classes of that sequence's inclusion and projection and whose connecting arrow is the class of `f[1]`. The form in `Comp(A)` is `associatedCompTriangle_coneSequence`; neither covers the comparison with the cone triangle of `f` (Tag 09QU) nor the rotation of this triangle (Tag 09QS)”.

> The same identification in the homotopy category: the triangle
> `(y, c(f), x[1], i, p, f[1])` is the triangle associated to the admissible short exact sequence
> `y ⟶ c(f) ⟶ x[1]`.

```lean
theorem associatedKTriangle_coneSequence (C : ConeSituation A) {x y : A.Obj}
    (f : A.Cocycle x y) :
    letI : HasShift A.K ℤ := C.shift.kShift
    GradedSplitShortExact.associatedKTriangle C.shift (C.coneSequence f) =
      Pretriangulated.Triangle.mk
        (Quotient.mk (A.homotopySetoid y (C.cone f)) (C.coneSequence f).a)
        (Quotient.mk (A.homotopySetoid (C.cone f) ((C.shift.shiftFunctor 1).obj x))
          (C.coneSequence f).b)
        ((Quotient.mk (A.homotopySetoid ((C.shift.shiftFunctor 1).obj x)
              ((C.shift.shiftFunctor 1).obj y))
            ((C.shift.shiftFunctor 1).mapCocycle f)) ≫
          eqToHom (congrArg (fun F : A.K ⥤ A.K => F.obj y)
            (C.shift.kShift_functor 1)).symm)
```

## Tag 09QS, a lemma

[Tag 09QS](https://stacks.math.columbia.edu/tag/09QS) in the Stacks Project.

**`DGCategory.rotatedAssociatedTriangle_iso_connectingConeTriangle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/RotatedConeTriangle.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/RotatedConeTriangle.lean#L308).

> The rotated triangle of an admissible sequence is isomorphic to the cone
> triangle of its desuspended connecting map.

```lean
theorem rotatedAssociatedTriangle_iso_connectingConeTriangle
    (C : ConeSituation A) {x y z : A.Obj}
    (E : GradedSplitShortExact (A := A) x y z) :
    letI : HasShift A.K ℤ := C.shift.kShift
    Nonempty (rotatedAssociatedTriangle C E ≅ connectingConeTriangle C E)
```

## Tag 09QT, a lemma

[Tag 09QT](https://stacks.math.columbia.edu/tag/09QT) in the Stacks Project.

**`DGCategory.isIso_cone_of_isIso_source_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ConeHomotopyEquivalence.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ConeHomotopyEquivalence.lean#L293).

> In a morphism of cone triangles, homotopy equivalences on the source and target
> induce a homotopy equivalence on the cones.

```lean
public theorem isIso_cone_of_isIso_source_target
    (S : ConeSituation A)
    {x₁ y₁ x₂ y₂ : A.Obj} (f₁ : A.Cocycle x₁ y₁) (f₂ : A.Cocycle x₂ y₂)
    (φ :
      letI : HasShift A.K ℤ := S.shift.kShift
      coneTriangle S f₁ ⟶ coneTriangle S f₂) :
    letI : HasShift A.K ℤ := S.shift.kShift
    IsIso φ.hom₁ → IsIso φ.hom₂ → IsIso φ.hom₃
```

## Tag 09QU, a lemma

[Tag 09QU](https://stacks.math.columbia.edu/tag/09QU) in the Stacks Project.

**`DGCategory.coneTriangleIsoOfShortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ConeTriangleComparison.lean, line 713](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ConeTriangleComparison.lean#L713). The attribute's comment: “part (1)”. References: SGA 4 XVII (1.1.1), “DG category setting”.

> An admissible short exact sequence identifies its quotient with the cone of its
> first arrow, compatibly with the two triangles and the identity on their first two terms.

```lean
public theorem coneTriangleIsoOfShortExact (S : ConeSituation A)
    {x y z : A.Obj} (E : GradedSplitShortExact (A := A) x y z) :
    letI : HasShift A.K ℤ := S.shift.kShift
    ∃ φ : negativeConeTriangle S E.a ⟶ GradedSplitShortExact.associatedKTriangle S.shift E,
      φ.hom₁ = 𝟙 _ ∧ φ.hom₂ = 𝟙 _ ∧ IsIso φ.hom₃
```

**`DGCategory.shortExactTriangleIsoOfFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ConeTriangleComparison.lean, line 864](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ConeTriangleComparison.lean#L864). The attribute's comment: “part (2)”. References: SGA 4 XVII (1.1.1), “DG cat. with cone situat”.

> The admissible sequence in a factorization of a closed arrow gives a triangle
> isomorphic to the cone triangle of that arrow, by the identity on the source and the
> factorization's homotopy equivalence on the target.

```lean
public theorem shortExactTriangleIsoOfFactorization (S : ConeSituation A)
    {x y y' z : A.Obj} (α : A.Cocycle x y)
    (E : GradedSplitShortExact (A := A) x y' z)
    (π : A.Cocycle y' y) (hπα : A.compCocycle π E.a = α)
    (s : A.Cocycle y y')
    (hπs : A.compCocycle π s = (⟨A.id y, A.d_id y⟩ : A.Cocycle y y))
    (hsπ : A.Homotopic (A.compCocycle s π)
      (⟨A.id y', A.d_id y'⟩ : A.Cocycle y' y')) :
    letI : HasShift A.K ℤ := S.shift.kShift
    ∃ φ : GradedSplitShortExact.associatedKTriangle S.shift E ⟶ negativeConeTriangle S α,
      φ.hom₁ = 𝟙 _ ∧
      φ.hom₂ = Quotient.mk (A.homotopySetoid y' y) π ∧
      IsIso φ.hom₃
```

## Tag 09QW, a lemma

[Tag 09QW](https://stacks.math.columbia.edu/tag/09QW) in the Stacks Project.

**`DGCategory.homotopyPretriangulated`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/HomotopyCategoryTriangulated.lean, line 1406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/HomotopyCategoryTriangulated.lean#L1406). The attribute's comment: “the pre-triangulated structure”. References: SGA 4½ Etat 0 (1.2.2), “TR1, TR2, TR3”.

> The homotopy category with the triangles of admissible short exact sequences as its
> distinguished triangles is pretriangulated.

```lean
public noncomputable def homotopyPretriangulated :
    letI : Preadditive A.K := homotopyPreadditive A
    letI : HasZeroObject A.K := homotopyHasZeroObject A T
    letI : HasShift A.K ℤ := T.shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor A.K n).Additive := fun n => homotopyShiftAdditive A T n
    Pretriangulated A.K
```

**`DGCategory.distinguishedTriangles_homotopyPretriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/HomotopyCategoryTriangulated.lean, line 1417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/HomotopyCategoryTriangulated.lean#L1417). The attribute's comment: “its distinguished triangles”. References: SGA 4½ Etat 0 (1.2.2), “more general”.

> The distinguished triangles of the pretriangulated structure on `K(A)` are exactly the
> triangles isomorphic to that of an admissible short exact sequence.

```lean
public theorem distinguishedTriangles_homotopyPretriangulated :
    letI : Preadditive A.K := homotopyPreadditive A
    letI : HasZeroObject A.K := homotopyHasZeroObject A T
    letI : HasShift A.K ℤ := T.shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor A.K n).Additive := fun n => homotopyShiftAdditive A T n
    (homotopyPretriangulated A T).distinguishedTriangles =
      {U | IsDistinguishedTriangle A T U}
```

## Tag 09QX, a lemma

[Tag 09QX](https://stacks.math.columbia.edu/tag/09QX) in the Stacks Project.

**`DGCategory.admissibleMonomorphisms_octahedron`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/Octahedron.lean, line 761](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/Octahedron.lean#L761).

> The octahedral diagram associated to two composable admissible monomorphisms.
> The input exact sequences witness admissibility and fix the two quotient objects.

```lean
theorem admissibleMonomorphisms_octahedron
    (S : ConeSituation A)
    {x y z q₁ q₃ : A.Obj}
    (E₁ : GradedSplitShortExact (A := A) x y q₁)
    (E₃ : GradedSplitShortExact (A := A) y z q₃) :
    letI : HasShift A.K ℤ := S.shift.kShift
    let T₁ := GradedSplitShortExact.associatedKTriangle S.shift E₁
    let T₃ := GradedSplitShortExact.associatedKTriangle S.shift E₃
    ∃ (q₂ : A.Obj)
      (E₂ : GradedSplitShortExact (A := A) x z q₂)
      (E₄ : GradedSplitShortExact (A := A) q₁ q₂ q₃),
      let T₂ := GradedSplitShortExact.associatedKTriangle S.shift E₂
      let T₄ := GradedSplitShortExact.associatedKTriangle S.shift E₄
      (E₂.a.1 = A.comp (by rfl : (0 : ℤ) + 0 = 0) E₃.a.1 E₁.a.1) ∧
      (T₁.mor₁ ≫ T₃.mor₁ = T₂.mor₁) ∧
      (T₁.mor₂ ≫ T₄.mor₁ = T₃.mor₁ ≫ T₂.mor₂) ∧
      (T₄.mor₁ ≫ T₂.mor₃ = T₁.mor₃) ∧
      (T₂.mor₂ ≫ T₄.mor₂ = T₃.mor₂) ∧
      (T₂.mor₃ ≫ T₁.mor₁⟦1⟧' = T₄.mor₂ ≫ T₃.mor₃) ∧
      (T₄.mor₃ = T₃.mor₃ ≫ T₁.mor₂⟦1⟧')
```

## Tag 09QY, a proposition

[Tag 09QY](https://stacks.math.columbia.edu/tag/09QY) in the Stacks Project.

**`DGCategory.homotopyCategory_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/HomotopyCategoryTriangulated.lean, line 1431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/HomotopyCategoryTriangulated.lean#L1431). References: SGA 4½ Etat 0 (1.2.2); SGA 4 Vbis (2.5.1), “more general”.

> The homotopy category of a differential graded category satisfying axioms (A), (B) and (C),
> with the translation functors of axiom (B) and the triangles of admissible short exact sequences
> as distinguished triangles, is a triangulated category.

```lean
public theorem homotopyCategory_isTriangulated :
    letI : Preadditive A.K := homotopyPreadditive A
    letI : HasZeroObject A.K := homotopyHasZeroObject A T
    letI : HasShift A.K ℤ := T.shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor A.K n).Additive := fun n => homotopyShiftAdditive A T n
    letI : Pretriangulated A.K := homotopyPretriangulated A T
    IsTriangulated A.K
```

## Tag 0FQF, a lemma

[Tag 0FQF](https://stacks.math.columbia.edu/tag/0FQF) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.isTriangulated_onK`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCrossSiteExact.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedCrossSiteExact.lean#L149). The attribute's comment: “the induced functor on homotopy categories is exact, across two ringed sites”.

> **A differential graded functor across two ringed sites commuting with the shift is exact on
> the homotopy categories**, which is [Stacks, Tag 0FQF] in the generality the derived pullback
> and the derived pushforward of a sheaf of differential graded modules need. The triangulated
> structures are the ones of [Stacks, Tag 0FS7]: restriction of scalars to `ℤ` changes neither the
> homotopy categories, nor their cones, nor their admissible short exact sequences, so the cone
> situation here is the one that puts the triangulated structure on `K(Mod(A, d))`.

```lean
theorem isTriangulated_onK
    {F : DGCategory.DGFunctor (dgCategoryOverInt.{u, v, w} A) (dgCategoryOverInt.{u, v, w} B)}
    (hF : F.CommShiftB (coneSituationOverInt.{u, v, w} A).shift
      (coneSituationOverInt.{u, v, w} B).shift) :
    letI : Preadditive (dgCategoryOverInt.{u, v, w} A).K :=
      DGCategory.homotopyPreadditive _
    letI : HasZeroObject (dgCategoryOverInt.{u, v, w} A).K :=
      DGCategory.homotopyHasZeroObject _ (coneSituationOverInt.{u, v, w} A)
    letI : HasShift (dgCategoryOverInt.{u, v, w} A).K ℤ :=
      (coneSituationOverInt.{u, v, w} A).shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor (dgCategoryOverInt.{u, v, w} A).K n).Additive := fun n =>
      DGCategory.homotopyShiftAdditive _ (coneSituationOverInt.{u, v, w} A) n
    letI : Pretriangulated (dgCategoryOverInt.{u, v, w} A).K :=
      DGCategory.homotopyPretriangulated _ (coneSituationOverInt.{u, v, w} A)
    letI : Preadditive (dgCategoryOverInt.{u, v, w} B).K :=
      DGCategory.homotopyPreadditive _
    letI : HasZeroObject (dgCategoryOverInt.{u, v, w} B).K :=
      DGCategory.homotopyHasZeroObject _ (coneSituationOverInt.{u, v, w} B)
    letI : HasShift (dgCategoryOverInt.{u, v, w} B).K ℤ :=
      (coneSituationOverInt.{u, v, w} B).shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor (dgCategoryOverInt.{u, v, w} B).K n).Additive := fun n =>
      DGCategory.homotopyShiftAdditive _ (coneSituationOverInt.{u, v, w} B) n
    letI : Pretriangulated (dgCategoryOverInt.{u, v, w} B).K :=
      DGCategory.homotopyPretriangulated _ (coneSituationOverInt.{u, v, w} B)
    letI : F.onK.CommShift ℤ := commShift_onK A B hF
    F.onK.IsTriangulated
```

**`DGCategory.DGFunctor.CommShiftB.isDistinguishedTriangle_mapTriangleK`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean, line 427](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean#L427). The attribute's comment: “distinguished triangles are carried to distinguished triangles”.

> **Tag 0FQF.** The functor induced by `F` on homotopy categories carries the distinguished
> triangles of `K(A)` to the distinguished triangles of `K(B)`, the third arrow of the image
> triangle being formed with the comparison isomorphism `F(x[1]) = F(x)[1]`.

```lean
theorem isDistinguishedTriangle_mapTriangleK (CA : ConeSituation A) (CB : ConeSituation B)
    (hF : F.CommShiftB CA.shift CB.shift) :
    letI : HasShift A.K ℤ := CA.shift.kShift
    letI : HasShift B.K ℤ := CB.shift.kShift
    ∀ T : Pretriangulated.Triangle A.K, IsDistinguishedTriangle A CA T →
      IsDistinguishedTriangle B CB (hF.mapTriangleK.obj T)
```

**`DGCategory.DGFunctor.CommShiftK.commShift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean, line 523](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean#L523). The attribute's comment: “the induced functor commutes with the translations”.

> **Tag 0FQF.** The induced functor `K(A) ⥤ K(B)` commutes with the translation functors.

```lean
def commShift (hF : F.CommShiftK SA SB) :
    letI : HasShift A.K ℤ := SA.kShift
    letI : HasShift B.K ℤ := SB.kShift
    F.onK.CommShift ℤ
```

**`DGCategory.DGFunctor.CommShiftK.isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean#L544). The attribute's comment: “the induced functor on homotopy categories is exact, from the translation coherences as data”. References: SGA 4 Vbis (2.5.1), “more general”.

> **Tag 0FQF.** A functor `F : A ⥤ B` of differential graded categories over `R` between
> categories satisfying axioms (A), (B) and (C), which commutes with the shift, induces an exact
> functor `K(A) ⥤ K(B)` of triangulated categories.
>
> The commutation is asked for here as a `CommShiftK`, that is, together with the two coherences of
> the comparison isomorphisms with the `ℤ`-action data of the translations. Under the source's
> hypothesis `F(x[1]) = F(x)[1]` alone those two are
> `DGCategory.DGFunctor.CommShiftK.ofCommShiftB` away, as soon as the translations of the homotopy
> categories are strict; `DGCategory.DGFunctor.CommShiftB.isTriangulated` is that form.

```lean
theorem isTriangulated (CA : ConeSituation A) (CB : ConeSituation B)
    (hF : F.CommShiftK CA.shift CB.shift) :
    letI : Preadditive A.K := homotopyPreadditive A
    letI : HasZeroObject A.K := homotopyHasZeroObject A CA
    letI : HasShift A.K ℤ := CA.shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor A.K n).Additive := fun n => homotopyShiftAdditive A CA n
    letI : Pretriangulated A.K := homotopyPretriangulated A CA
    letI : Preadditive B.K := homotopyPreadditive B
    letI : HasZeroObject B.K := homotopyHasZeroObject B CB
    letI : HasShift B.K ℤ := CB.shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor B.K n).Additive := fun n => homotopyShiftAdditive B CB n
    letI : Pretriangulated B.K := homotopyPretriangulated B CB
    letI : F.onK.CommShift ℤ := hF.commShift
    F.onK.IsTriangulated
```

**`DGCategory.DGFunctor.CommShiftB.isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean, line 580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean#L580). The attribute's comment: “the induced functor on homotopy categories is exact, from F(x[1]) = F(x)[1]”. References: SGA 4 Vbis (2.5.1), “more general”.

> **Tag 0FQF.** A functor `F : A ⥤ B` of differential graded categories over `R` between
> categories satisfying axioms (A), (B) and (C) and such that `F(x[1]) = F(x)[1]` induces an exact
> functor `K(A) ⥤ K(B)` of triangulated categories.
>
> The hypothesis on `F` is exactly the source's, namely `CommShiftB`; what is assumed besides is
> not about `F` but about the two axiom (B) data, namely that the translations they put on the
> homotopy categories are the strict ones of the source
> (`DGCategory.ShiftAxiomB.IsStrictKShift`). That is what makes the two coherences of
> `DGCategory.DGFunctor.CommShiftK` — the agreement of the comparison isomorphisms with
> `shiftFunctorZero` and `shiftFunctorAdd`, which Mathlib's `Functor.CommShift` demands and which
> `F(x[1]) = F(x)[1]` does not imply for an arbitrary translation — available, by
> `DGCategory.DGFunctor.CommShiftK.ofCommShiftB`.

```lean
theorem isTriangulated (CA : ConeSituation A) (CB : ConeSituation B)
    (hA : CA.shift.IsStrictKShift) (hB : CB.shift.IsStrictKShift)
    (hF : F.CommShiftB CA.shift CB.shift) :
    letI : Preadditive A.K := homotopyPreadditive A
    letI : HasZeroObject A.K := homotopyHasZeroObject A CA
    letI : HasShift A.K ℤ := CA.shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor A.K n).Additive := fun n => homotopyShiftAdditive A CA n
    letI : Pretriangulated A.K := homotopyPretriangulated A CA
    letI : Preadditive B.K := homotopyPreadditive B
    letI : HasZeroObject B.K := homotopyHasZeroObject B CB
    letI : HasShift B.K ℤ := CB.shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor B.K n).Additive := fun n => homotopyShiftAdditive B CB n
    letI : Pretriangulated B.K := homotopyPretriangulated B CB
    letI : F.onK.CommShift ℤ := (CommShiftK.ofCommShiftB hF hA hB).commShift
    F.onK.IsTriangulated
```

**`DGCategory.DGFunctor.CommShiftB.isTriangulated_strictify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean, line 637](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/DifferentialGraded/ExactFunctor.lean#L637). The attribute's comment: “the induced functor on homotopy categories is exact, from F(x[1]) = F(x)[1] alone”. References: SGA 4 Vbis (2.5.1), “more general”.

> **Tag 0FQF, with nothing assumed but the source's hypothesis.** A functor `F : A ⥤ B` of
> differential graded categories over `R` between categories satisfying axioms (A), (B) and (C) and
> such that `F(x[1]) = F(x)[1]` induces an exact functor `K(A) ⥤ K(B)` of triangulated categories,
> for the triangulated structures attached to the strictifications of the two axiom bundles.
>
> Passing to the strictifications changes nothing about the differential graded categories, their
> shifts, their cones or the distinguished triangles of Tag 09QW: it only replaces the `HasShift`
> field of axiom (B), whose functors `kShift_functor` already pins down, by the one whose coherence
> isomorphisms are the canonical ones. So this is Tag 0FQF with no hypothesis beyond the source's
> `F(x[1]) = F(x)[1]`, and `DGCategory.DGFunctor.CommShiftB.isTriangulated` is the form in which
> the strictness is left as a hypothesis, for a caller who already knows it of the translations
> in hand.

```lean
theorem isTriangulated_strictify (CA : ConeSituation A) (CB : ConeSituation B)
    (hF : F.CommShiftB CA.shift CB.shift) :
    letI : Preadditive A.K := homotopyPreadditive A
    letI : HasZeroObject A.K := homotopyHasZeroObject A CA.strictify
    letI : HasShift A.K ℤ := CA.strictify.shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor A.K n).Additive := fun n =>
      homotopyShiftAdditive A CA.strictify n
    letI : Pretriangulated A.K := homotopyPretriangulated A CA.strictify
    letI : Preadditive B.K := homotopyPreadditive B
    letI : HasZeroObject B.K := homotopyHasZeroObject B CB.strictify
    letI : HasShift B.K ℤ := CB.strictify.shift.kShift
    letI : ∀ n : ℤ, (shiftFunctor B.K n).Additive := fun n =>
      homotopyShiftAdditive B CB.strictify n
    letI : Pretriangulated B.K := homotopyPretriangulated B CB.strictify
    letI : F.onK.CommShift ℤ := (CommShiftK.ofCommShiftB hF.strictify
      CA.isStrictKShift_strictify CB.isStrictKShift_strictify).commShift
    F.onK.IsTriangulated
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.27, Tag 09P5](https://stacks.math.columbia.edu/tag/09P5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: DifferentialGradedModule, DifferentialGradedModule.Hom, DifferentialGradedModule.instCategory, differentialGradedModule_abelian, differentialGradedModule_hasLimits, differentialGradedModule_hasColimits, DifferentialGradedModule.shortExact_forgetToCochainComplex, DifferentialGradedModule.longExactCohomology
statement: formalized
proof: formalized
---

# 22.4 Differential graded modules

Section 22.4 of the Stacks Project, [Tag 09JH](https://stacks.math.columbia.edu/tag/09JH). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09JI, a definition

[Tag 09JI](https://stacks.math.columbia.edu/tag/09JI) in the Stacks Project.

Declarations registered for the tag:

- [`DifferentialGradedModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/Abelian/Basic.lean#L85), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/CochainComplex.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/CochainComplex.lean#L134) (StacksFrontier): “differential graded modules”.
- [`DifferentialGradedModule.Hom`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/Abelian/Basic.lean#L124), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/CochainComplex.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/CochainComplex.lean#L135) (StacksFrontier): “homomorphisms”.
- [`DifferentialGradedModule.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DifferentialGradedModule.instCategory#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/DifferentialGraded/Module/CochainComplex.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/CochainComplex.lean#L136) (StacksFrontier): “the category”.

## Tag 09JJ, a lemma

[Tag 09JJ](https://stacks.math.columbia.edu/tag/09JJ) in the Stacks Project.

**`differentialGradedModule_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/Abelian/AbelianComplete.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/Abelian/AbelianComplete.lean#L92). The attribute's comment: “abelian”.

> The category `Mod_(A, d)` of right differential graded `A`-modules is abelian.

```lean
theorem differentialGradedModule_abelian (A : DifferentialGradedAlgebra.{u, v} R) :
    Nonempty (Abelian (DifferentialGradedModule.{u, v, w} A))
```

**`differentialGradedModule_hasLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/Abelian/AbelianComplete.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/Abelian/AbelianComplete.lean#L103). The attribute's comment: “limits”.

> The category `Mod_(A, d)` of right differential graded `A`-modules has all limits indexed by
> categories in the universe `w` of the carriers.

```lean
theorem differentialGradedModule_hasLimits (A : DifferentialGradedAlgebra.{u, v} R) :
    HasLimitsOfSize.{w, w} (DifferentialGradedModule.{u, v, w} A)
```

**`differentialGradedModule_hasColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DGA/Abelian/AbelianComplete.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DGA/Abelian/AbelianComplete.lean#L112). The attribute's comment: “colimits”.

> The category `Mod_(A, d)` of right differential graded `A`-modules has all colimits indexed by
> categories in the universe `w` of the carriers.

```lean
theorem differentialGradedModule_hasColimits (A : DifferentialGradedAlgebra.{u, v} R) :
    HasColimitsOfSize.{w, w} (DifferentialGradedModule.{u, v, w} A)
```

## Tag 09JK, an equation

[Tag 09JK](https://stacks.math.columbia.edu/tag/09JK) in the Stacks Project.

**`DifferentialGradedModule.shortExact_forgetToCochainComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/LongExactSequence.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/LongExactSequence.lean#L89). The attribute's comment: “the underlying exact sequence of cochain complexes”.

> A short exact sequence of differential graded modules remains short exact after forgetting
> to cochain complexes of modules over the base ring.

```lean
theorem shortExact_forgetToCochainComplex (S : ShortComplex (DifferentialGradedModule A))
    (hS : S.ShortExact) :
    (S.map (forgetToCochainComplex A)).ShortExact
```

**`DifferentialGradedModule.longExactCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/LongExactSequence.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/LongExactSequence.lean#L115). The attribute's comment: “the long exact cohomology sequence”.

> The cohomology of a short exact sequence of differential graded modules forms a long exact
> sequence, including its canonical connecting maps.

```lean
theorem longExactCohomology (S : ShortComplex (DifferentialGradedModule A))
    (hS : S.ShortExact) (n m : ℤ) (hnm : (ComplexShape.up ℤ).Rel n m) :
    (HomologicalComplex.HomologySequence.composableArrows₅
      (C := ModuleCat.{u} R) (c := ComplexShape.up ℤ)
      (S₁ := S.map (forgetToCochainComplex A))
      (shortExact_forgetToCochainComplex A S hS) n m hnm).Exact
```

## Tag 09JL, a definition

[Tag 09JL](https://stacks.math.columbia.edu/tag/09JL) in the Stacks Project.

**`DifferentialGradedModule.shift`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Shift.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Shift.lean#L54). The attribute's comment: “the shifted module”.

> The `k`-shifted differential graded module `M[k]`: degree `n` is the old degree `n + k`,
> the differential is multiplied by `(-1)^k`, and the right algebra action is unchanged.

```lean
noncomputable def shift (M : DifferentialGradedModule A) (k : ℤ) :
    DifferentialGradedModule A
```

**`DifferentialGradedModule.shiftMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Shift.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Shift.lean#L109). The attribute's comment: “the shifted homomorphism”.

> A homomorphism of differential graded modules, viewed as a homomorphism of their `k`-shifts
> by the same underlying linear map.

```lean
def shiftMap {M N : DifferentialGradedModule A} (f : Hom M N) (k : ℤ) :
    Hom (shift M k) (shift N k)
```

**`DifferentialGradedModule.shiftFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/Shift.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/Shift.lean#L127). The attribute's comment: “the shift functor”.

> Shifting by `k`, as a functor on the category of differential graded modules.

```lean
noncomputable def shiftFunctor (A : DifferentialGradedAlgebra R) (k : ℤ) :
    DifferentialGradedModule A ⥤ DifferentialGradedModule A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.4, Tag 09JH](https://stacks.math.columbia.edu/tag/09JH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

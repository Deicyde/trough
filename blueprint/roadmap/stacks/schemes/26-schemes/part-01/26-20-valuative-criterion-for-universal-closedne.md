---
declaration: section
origin: cited
lean: AlgebraicGeometry.UniversallyClosed, AlgebraicGeometry.universallyClosed_eq_universallySpecializing, AlgebraicGeometry.ValuativeCriterion.Existence, AlgebraicGeometry.ValuativeCriterion.Uniqueness, AlgebraicGeometry.exists_valuation_ring_of_specializes, AlgebraicGeometry.projectiveLine_valuativeCriterion_existence, AlgebraicGeometry.projectiveLine_quasiCompact, AlgebraicGeometry.projectiveLine_universallyClosed
statement: formalized
proof: formalized
---

# 26.20 Valuative criterion for universal closedness

Section 26.20 of the Stacks Project, [Tag 01KA](https://stacks.math.columbia.edu/tag/01KA). 5 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01KB, a definition

[Tag 01KB](https://stacks.math.columbia.edu/tag/01KB) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.UniversallyClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyClosed#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L222) (StacksFrontier). References: EGA II (5.4.1); EGA II (5.4.9).

## Tag 01KC, a lemma

[Tag 01KC](https://stacks.math.columbia.edu/tag/01KC) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.universallyClosed_eq_universallySpecializing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.universallyClosed_eq_universallySpecializing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L223) (StacksFrontier): “(1) and (2)”.

## Tag 01KD, a definition

[Tag 01KD](https://stacks.math.columbia.edu/tag/01KD) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.ValuativeCriterion.Existence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.ValuativeCriterion.Existence#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 248](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L248) (StacksFrontier): “existence part of the valuative criterion”.
- [`AlgebraicGeometry.ValuativeCriterion.Uniqueness`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.ValuativeCriterion.Uniqueness#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L250) (StacksFrontier): “uniqueness part of the valuative criterion”.

## Tag 01J8, a lemma

[Tag 01J8](https://stacks.math.columbia.edu/tag/01J8) in the Stacks Project.

**`AlgebraicGeometry.exists_valuation_ring_of_specializes`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Valuative/Specialization.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Valuative/Specialization.lean#L49).

> A specialization of points of a scheme is witnessed by a valuation ring.  The valuation
> ring may be chosen so that the residue-field extension at its generic point is any prescribed
> extension.

```lean
public lemma exists_valuation_ring_of_specializes (S : AlgebraicGeometry.Scheme.{u})
    {s' s : S} (h : s' ⤳ s) (K : Type u) [Field K]
    (i : S.residueField s' ⟶ CommRingCat.of K) :
    ∃ (A : Type u) (_ : CommRing A) (_ : IsDomain A) (_ : ValuationRing A)
      (f : AlgebraicGeometry.Spec (.of A) ⟶ S)
      (e : (AlgebraicGeometry.Spec (.of A)).residueField
        (genericPoint (AlgebraicGeometry.Spec (.of A))) ≅ CommRingCat.of K)
      (hη : f (genericPoint (AlgebraicGeometry.Spec (.of A))) = s'),
      f (closedPoint A) = s ∧
        (S.residueFieldCongr hη).inv ≫
          f.residueFieldMap (genericPoint (AlgebraicGeometry.Spec (.of A))) ≫ e.hom = i
```

## Tag 01KG, an example

[Tag 01KG](https://stacks.math.columbia.edu/tag/01KG) in the Stacks Project.

**`AlgebraicGeometry.projectiveLine_valuativeCriterion_existence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineUniversallyClosed.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineUniversallyClosed.lean#L127). The attribute's comment: “valuative extension”.

> Every valuative square for the structure morphism of the projective line
> has a diagonal lift.

```lean
theorem projectiveLine_valuativeCriterion_existence (k : Type u) [CommRing k] :
    ValuativeCriterion.Existence
      (projectiveLine k ↘ Spec (.of k))
```

**`AlgebraicGeometry.projectiveLine_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineUniversallyClosed.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineUniversallyClosed.lean#L346). The attribute's comment: “quasi-compactness”.

> The structure morphism of the projective line is quasi-compact.

```lean
theorem projectiveLine_quasiCompact (k : Type u) [CommRing k] :
    QuasiCompact (projectiveLine k ↘ Spec (.of k))
```

**`AlgebraicGeometry.projectiveLine_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineUniversallyClosed.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineUniversallyClosed.lean#L353). The attribute's comment: “universal closedness”.

> The structure morphism of the projective line is universally closed.

```lean
theorem projectiveLine_universallyClosed (k : Type u) [CommRing k] :
    UniversallyClosed (projectiveLine k ↘ Spec (.of k))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.20, Tag 01KA](https://stacks.math.columbia.edu/tag/01KA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

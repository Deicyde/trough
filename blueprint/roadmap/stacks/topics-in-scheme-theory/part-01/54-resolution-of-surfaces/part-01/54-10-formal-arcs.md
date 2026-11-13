---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_nonsingularFormalArc_of_pointBlowupSequence, AlgebraicGeometry.exists_regular_center
statement: formalized
proof: formalized
---

# 54.10 Formal arcs

Section 54.10 of the Stacks Project, [Tag 0BG1](https://stacks.math.columbia.edu/tag/0BG1). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BG2, a lemma

[Tag 0BG2](https://stacks.math.columbia.edu/tag/0BG2) in the Stacks Project.

**`AlgebraicGeometry.exists_nonsingularFormalArc_of_pointBlowupSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/FormalArcs/PointBlowups.lean, line 1103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/FormalArcs/PointBlowups.lean#L1103).

> **Stacks Project, Tag 0BG2.** An infinite point-blowup sequence whose
> exceptional divisors are locally defined by the transforms of one initial
> function is induced by a nonsingular formal arc.

```lean
theorem exists_nonsingularFormalArc_of_pointBlowupSequence
    (s : PointBlowupSequence.{u}) [IsLocallyNoetherian (s.scheme 0)]
    (x : (s.scheme 0).presheaf.stalk (s.point 0))
    (hx : x ∈ IsLocalRing.maximalIdeal ((s.scheme 0).presheaf.stalk (s.point 0)))
    (hExceptional : ∀ n, s.exceptionalIdealAt n =
      Ideal.span {s.stalkImage (n + 1) x}) :
    ∃ (R : CommRingCat.{u}) (hDomain : IsDomain R),
      letI : IsDomain R := hDomain
      ∃ (hDVR : IsDiscreteValuationRing R),
        letI : IsDiscreteValuationRing R := hDVR
        ∃ (_hComplete : IsAdicComplete (IsLocalRing.maximalIdeal R) R)
          (a : Spec R ⟶ s.scheme 0)
          (hCenter : a (IsLocalRing.closedPoint R) = s.point 0),
          IsIso (a.residueFieldMap (IsLocalRing.closedPoint R)) ∧
          IsLocalRing.maximalIdeal R =
            Ideal.span {(Scheme.stalkClosedPointTo a).hom (hCenter.symm ▸ x)} ∧
          ∃ lifts : (n : ℕ) → Spec R ⟶ s.scheme n,
            lifts 0 = a ∧
            (∀ n, lifts (n + 1) ≫ s.stepMap n = lifts n) ∧
            (∀ n, lifts n (IsLocalRing.closedPoint R) = s.point n)
```

## Tag 0BG3, a lemma

[Tag 0BG3](https://stacks.math.columbia.edu/tag/0BG3) in the Stacks Project.

**`AlgebraicGeometry.exists_regular_center`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/FormalArcs/Basic/RegularCenter.lean, line 721](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ResolutionOfSurfaces/FormalArcs/Basic/RegularCenter.lean#L721).

> A sequence of blowups along a formal arc whose generic image is regular eventually
> reaches a regular center.

```lean
theorem exists_regular_center
    {A R : Type u} [CommRing A] [IsDomain A] [IsLocalRing A]
    [IsNoetherianRing A] [CommRing R] [IsDomain R]
    [IsDiscreteValuationRing R] [IsAdicComplete (maximalIdeal R) R]
    (hA : ringKrullDim A = 2) (f : A →+* R) (hf : Function.Surjective f)
    (hgeneric : IsRegularLocalRing ((Spec (.of A)).presheaf.stalk
      (Spec.map (CommRingCat.ofHom f) (genericPoint (Spec (.of R))))))
    (s : ArcBlowupSequence A R f) :
    ∃ i : ℕ, IsRegularLocalRing ((s.scheme i).presheaf.stalk
      (s.arc i (closedPoint R)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 54.10, Tag 0BG1](https://stacks.math.columbia.edu/tag/0BG1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

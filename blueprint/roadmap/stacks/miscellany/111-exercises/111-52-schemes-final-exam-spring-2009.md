---
declaration: section
origin: cited
lean: Stacks.ProjectiveSpace.Cohomology.projectivePlane_exists_iso_twistingSheaf_and_sections, AlgebraicGeometry.ProjectiveSpectrum.Proj.twistSheafOfModules
statement: formalized
proof: formalized
---

# 111.52 Schemes, Final Exam, Spring 2009

Section 111.52 of the Stacks Project, [Tag 02AV](https://stacks.math.columbia.edu/tag/02AV). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02AX, a remark

[Tag 02AX](https://stacks.math.columbia.edu/tag/02AX) in the Stacks Project.

**`Stacks.ProjectiveSpace.Cohomology.projectivePlane_exists_iso_twistingSheaf_and_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/ProjectivePlaneInvertibleSheaves.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/ProjectivePlaneInvertibleSheaves.lean#L145). The attribute's comment: “invertible sheaves on ℙ²\_k are the twists 𝒪(n), and Γ(ℙ²\_k, 𝒪(n)) is the degree-n part of k[X₀, X₁, X₂] for every n ∈ ℤ (through the canonical map for n ≥ 0)”.

> **Stacks Project, Tag 02AX.** Let `k` be a field and `ℙ²_k = Proj k[X₀, X₁, X₂]`.
>
> 1. Every invertible sheaf on `ℙ²_k` is isomorphic to `𝒪(n)` for some `n ∈ ℤ`.
> 2. For `n ≥ 0` the canonical map `k[X₀, X₁, X₂]_n ⟶ Γ(ℙ²_k, 𝒪(n))` is bijective.
> 3. For every `n ∈ ℤ`, `Γ(ℙ²_k, 𝒪(n))` is the degree-`n` part of `k[X₀, X₁, X₂]` (the grading
>    extended by zero, so both sides vanish for `n < 0`).
>
> The twist `ℱ(n) = ℱ ⊗ 𝒪(n)` of the last sentence of the source is the definition
> `AlgebraicGeometry.ProjectiveSpectrum.Proj.twistSheafOfModules`.

```lean
theorem projectivePlane_exists_iso_twistingSheaf_and_sections (k : Type u) [Field k] :
    (∀ L : (AlgebraicGeometry.Proj
        (MvPolynomial.homogeneousSubmodule (Fin (2 + 1)) k)).Modules,
      Stacks.SheafOfModules.IsInvertible (AlgebraicGeometry.Proj
          (MvPolynomial.homogeneousSubmodule (Fin (2 + 1)) k)).presheaf
        (AlgebraicGeometry.Proj
          (MvPolynomial.homogeneousSubmodule (Fin (2 + 1)) k)).ringCatIsSheaf L →
      ∃ m : ℤ, Nonempty
        (L ≅ twistingSheaf (MvPolynomial.homogeneousSubmodule (Fin (2 + 1)) k) m)) ∧
    (∀ n : ℕ, Function.Bijective
      (degreeSection (MvPolynomial.homogeneousSubmodule (Fin (2 + 1)) k) n)) ∧
    (∀ n : ℤ, Nonempty (twistTopSections k 2 n ≃+
      integerGrading (S := MvPolynomial (Fin (2 + 1)) k)
        (MvPolynomial.homogeneousSubmodule (Fin (2 + 1)) k) n))
```

Declarations registered for the tag:

- [`AlgebraicGeometry.ProjectiveSpectrum.Proj.twistSheafOfModules`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Constructions/ProjTwist.lean#L178), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/ProjectiveSpaceTwist.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/ProjectiveSpaceTwist.lean#L22) (StacksFrontier): “sheaf\_twist”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.52, Tag 02AV](https://stacks.math.columbia.edu/tag/02AV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProjectiveGenerator.twistSum, Stacks.AlgebraicGeometry.ProjectiveGenerator.matrixRingEquivEnd, Stacks.AlgebraicGeometry.Beilinson.beilinson_equivalence_matrixAlgebra
statement: formalized
proof: formalized
---

# 36.20 An example equivalence

Section 36.20 of the Stacks Project, [Tag 0CS7](https://stacks.math.columbia.edu/tag/0CS7). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0CS8, an equation

[Tag 0CS8](https://stacks.math.columbia.edu/tag/0CS8) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveGenerator.twistSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveGeneratorAlgebra.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveGeneratorAlgebra.lean#L136).

> The direct sum `𝒪_X ⊕ 𝒪_X(-1) ⊕ ⋯ ⊕ 𝒪_X(-n)` of the `n + 1` nonpositive twists of the
> structure sheaf of `X = ℙⁿ_A`.

```lean
public def twistSum : (projectiveSpaceOverRing n (.of A)).Modules
```

## Tag 0CS9, an equation

[Tag 0CS9](https://stacks.math.columbia.edu/tag/0CS9) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveGenerator.matrixRingEquivEnd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveGeneratorHomGroups.lean, line 683](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveGeneratorHomGroups.lean#L683).

> **[Stacks, Tag 0CS9]: `R = Hom_{𝒪_X}(P, P)`.** On `X = ℙⁿ_A = Proj A[X₀, …, Xₙ]`, the ring
> of upper triangular `(n + 1) × (n + 1)` matrices whose `(i, j)` entry is homogeneous of degree
> `j - i` — `S₀` on the diagonal, `S₁` above it, and so on — is the endomorphism ring of
> `P = 𝒪_X ⊕ 𝒪_X(-1) ⊕ ⋯ ⊕ 𝒪_X(-n)`, the `(i, j)` entry acting as the component
> `𝒪_X(-j) ⟶ 𝒪_X(-i)` by multiplication.

```lean
public def matrixRingEquivEnd : endomorphismMatrices A n ≃+* End (projTwistSum A n)
```

## Tag 0BQU, a lemma

[Tag 0BQU](https://stacks.math.columbia.edu/tag/0BQU) in the Stacks Project.

**`Stacks.AlgebraicGeometry.Beilinson.beilinson_equivalence_matrixAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/BeilinsonMatrixAlgebra.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/BeilinsonMatrixAlgebra.lean#L67). The attribute's comment: “Beilinson's equivalence - ⊗\_R^L P : D(R) → D\_QCoh(O\_X) on X = P^n\_A, with P = O\_X ⊕ O\_X(-1) ⊕ ... ⊕ O\_X(-n) of Tag 0CS8 and R = Hom\_\{O\_X}(P, P) of Tag 0CS9 read as the differential graded algebra Hom^dg(P, P) with zero differential: an equivalence, exact, A-linear, sending R to P, with the ring of R identified with the upper triangular matrix algebra of Tag 0CS9 by endAlgebraRingEquivMatrices”.

> **[Stacks, Tag 0BQU] (Beilinson).** Let `A` be a ring, `X = P^n_A = Proj A[X₀, …, Xₙ]`,
> `P = 𝒪_X ⊕ 𝒪_X(-1) ⊕ ⋯ ⊕ 𝒪_X(-n)` as in Tag 0CS8, and `R = Hom_{𝒪_X}(P, P)` as in Tag 0CS9,
> viewed as the differential graded algebra `Hom_{Comp^dg(𝒪_X)}(P, P)` with zero differential.
> Then `- ⊗_R^𝐋 P : D(R) ⥤ D_QCoh(𝒪_X)` is an equivalence of categories, is exact, sends `R` to
> `P`, and is `A`-linear (for `A ⊂ center(R)` acting on `D(R)` and `A → Γ(X, 𝒪_X)` acting on
> `D_QCoh(𝒪_X)`); and the ring of `R` is the upper triangular algebra of matrices over
> `A[X₀, …, Xₙ]` with `(i, j)` entry homogeneous of degree `j - i`.

```lean
theorem beilinson_equivalence_matrixAlgebra :
    ((tensorWithGenerator A n).IsEquivalence ∧ (tensorWithGenerator A n).IsTriangulated ∧
      Nonempty ((tensorWithGenerator A n).obj (regular A n) ≅ twistSumQCoh A n) ∧
      letI := derivedCategoryRLinear A n
      letI := quasiCoherentDerivedCategoryLinear A n
      (tensorWithGenerator A n).Linear A) ∧
      Nonempty ((endAlgebra A n).A ≃+* endomorphismMatrices A n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.20, Tag 0CS7](https://stacks.math.columbia.edu/tag/0CS7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

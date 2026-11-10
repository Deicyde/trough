---
declaration: section
origin: cited
lean: Stacks.AlgebraicGeometry.ProjectiveGenerator.twistSum, Stacks.AlgebraicGeometry.ProjectiveGenerator.matrixRingEquivEnd, Stacks.AlgebraicGeometry.ProjectiveGenerator.twistSum_tensorDerived_isEquivalence, Stacks.AlgebraicGeometry.ProjectiveGenerator.twistSumTensorDerivedObjRegularIso, Stacks.AlgebraicGeometry.Beilinson.beilinson_equivalence
statement: formalized
proof: formalized
---

# 36.20 An example equivalence

Section 36.20 of the Stacks Project, [Tag 0CS7](https://stacks.math.columbia.edu/tag/0CS7). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CS8, an equation

[Tag 0CS8](https://stacks.math.columbia.edu/tag/0CS8) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveGenerator.twistSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveGeneratorAlgebra.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveGeneratorAlgebra.lean#L136).

> The direct sum `𝒪_X ⊕ 𝒪_X(-1) ⊕ ⋯ ⊕ 𝒪_X(-n)` of the `n + 1` nonpositive twists of the
> structure sheaf of `X = ℙⁿ_A`.

```lean
public def twistSum : (projectiveSpaceOverRing n (.of A)).Modules
```

## Tag 0CS9, an equation

[Tag 0CS9](https://stacks.math.columbia.edu/tag/0CS9) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ProjectiveGenerator.matrixRingEquivEnd`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveGeneratorHomGroups.lean, line 683](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveGeneratorHomGroups.lean#L683).

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

**`Stacks.AlgebraicGeometry.ProjectiveGenerator.twistSum_tensorDerived_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveSpaceExampleEquivalence.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveSpaceExampleEquivalence.lean#L399). The attribute's comment: “RESTRICTED. UNCONDITIONAL HERE is the assembly of Beilinson's argument at X = ℙⁿ\_A with P the twist sum of Tag 0CS8 placed in degree zero: the adjunction - ⊗\_E^𝐋 P ⊣ RHom(P, -) of Tag 09LY, supplied by its carrier AlgebraicGeometry.RingedSite.tensorWithComplexDerived\_adj\_derivedHomWithComplex, together with the commutation of RHom(P, -) with the translation that the adjunction induces (derivedHomWithComplexCommShift); the dévissage of Tag 0FQE, supplied by its carrier DifferentialGradedModule.General.property\_of\_coproducts\_of\_two\_out\_of\_three\_of\_shifts; the direct sums of D(E), supplied by DifferentialGradedModule.General.hasCoproducts\_derivedCategory; the weak generation of D(E) by the regular module, proved here as isWeakTriangulatedGenerator\_q\_regularModule, the independent-universe cone-triangle form of DifferentialGradedModule.isWeakTriangulatedGenerator\_q\_regularModule; full faithfulness by Tag 09LZ; the conversion of the weak-generator property of P into the kernel condition hker of Tag 09J1 (isZero\_of\_isZero\_derivedHom); and the conclusion by Tag 09J1 that the functor - ⊗\_E^𝐋 P of Tag 09LX is an equivalence of categories and is exact. The clause 'sending R to P' is twistSumTensorDerivedObjRegularIso. NOT PROVED: the identification of E = Hom^dg(P, P) with the upper triangular matrix algebra R of Tag 0CS9, so the source category is D(E) and not D(R); and A-linearity, the library supplying no A-linear structure on D(E), the ground ring of the differential graded category of complexes on a ringed site being ℤ by Tag 09L9. CARRIED HYPOTHESES. (i) hKgen, that P weakly generates D(O\_X). This is exactly the conclusion of Tag 0A9V, which this library has as Stacks.AlgebraicGeometry.ExampleGenerator.isWeakTriangulatedGenerator\_twistSum\_of\_twists and which is itself conditional: it carries hvanish, the vanishing criterion the source obtains from Tag 0BQR applied to the ample invertible sheaf O\_X(1) of Tag 01Q2. Tag 0BQR has no carrier in this library, so it is carried as a declared hypothesis here and is neither proved nor duplicated. Tag 0A9V is moreover stated for the locally small model of the derived category of SheafOfModules (projRingSheaf (polyGrading A n)) and for the whole of D(O\_X), whereas the functor of Tag 09LX is formed in the standard derived category of the ambient module category of the ringed site and the source's statement is about D\_QCoh(O\_X), which is also the scope on which hvanish is available from Tag 0BQR; neither identification is made here, so no transport of Tag 0A9V is claimed and hKgen is taken in the model in which the functor lives. (ii) The three inputs of Tag 09LZ this library does not discharge. The exactness of RHom(P, -): Mathlib's CategoryTheory.Adjunction.isTriangulated\_rightAdjoint would give it from the exactness of - ⊗\_E^𝐋 P, but that is the second conjunct of the conclusion here, and the independent route AlgebraicGeometry.RingedSite.tensorWithComplexDerived\_isTriangulated needs the exactness of - ⊗\_E P on K(Mod\_E), which Tag 09LW supplies only against the pretriangulated structure whose distinguished triangles come from admissible short exact sequences, whereas D(E) and the dévissage of Tag 0FQE are read in the structure whose distinguished triangles are the cone triangles, the two classes agreeing by Tag 09KH, which this library does not formalize. The commutation of RHom(P, -) with direct sums, which is the only use the source's proof makes of its hypothesis (1) that P represents a compact object of D(O\_X). And hExt, hypothesis (2) of Tag 09LZ that E computes the ext groups of P”.

> **Stacks 0BQU**, with the matrix description of the endomorphism algebra and `A`-linearity
> omitted and the inputs of Tag 09LZ and Tag 0A9V carried. *"Let `A` be a ring. Let
> `X = ℙⁿ_A = Proj(S)` where `S = A[X₀, …, Xₙ]`. With `P` as in Tag 0CS8 and `R` as in Tag 0CS9
> the functor `- ⊗_R^𝐋 P : D(R) ⟶ D_QCoh(𝒪_X)` is an `A`-linear equivalence of triangulated
> categories sending `R` to `P`."*
>
> What is proved: for `P` the twist sum of Tag 0CS8 on `ℙⁿ_A`, placed in degree zero, and
> `E = Hom^{dg}(P, P)` its endomorphism differential graded algebra, the functor `- ⊗_E^𝐋 P` of
> Tag 09LX is an equivalence of categories and is exact. The image of the regular module is `P`,
> which is
> `Stacks.AlgebraicGeometry.ProjectiveGenerator.twistSumTensorDerivedObjRegularIso`.
>
> What is not: the identification `E = R` with the upper triangular matrix algebra of Tag 0CS9,
> which this library does not have, so the source category is `D(E)` rather than `D(R)`; and
> `A`-linearity, for which the library supplies no `A`-linear structure on `D(E)`. The carried
> hypotheses are the three inputs of Tag 09LZ this library does not discharge — the exactness of
> `RHom(P, -)`, its commutation with direct sums and `hExt` — together with `hKgen`, the weak
> generation of `D(𝒪_X)` by `P`, which is the conclusion of Tag 0A9V; see the module's
> implementation notes for why Tag 0A9V is carried rather than applied. The adjunction of
> Tag 09LY, the dévissage of Tag 0FQE, the direct sums of `D(E)` and the weak generation of `D(E)`
> by the regular module are *not* carried: each is supplied by a carrier of this library.

```lean
theorem twistSum_tensorDerived_isEquivalence
    [(derivedHomWithComplex.{u, u, u, u, u} (projectiveSpaceSite A n)
      (twistSumComplex A n)).IsTriangulated]
    [∀ ι : Type u, PreservesColimitsOfShape (Discrete ι)
      (derivedHomWithComplex.{u, u, u, u, u} (projectiveSpaceSite A n)
        (twistSumComplex A n))]
    (hExt : ∀ m : ℤ, Function.Bijective
      (fun f : repRegularDerived.{u, u, u, u, u} (projectiveSpaceSite A n)
            (twistSumComplex A n) ⟶
          (repRegularDerived.{u, u, u, u, u} (projectiveSpaceSite A n)
            (twistSumComplex A n))⟦m⟧ =>
        (tensorWithComplexDerived.{u, u, u, u, u, 0} (projectiveSpaceSite A n) ℤ
          (twistSumComplex A n)).map f))
    (hKgen : (ObjectProperty.singleton (DerivedCategory.Q.obj
      (liftComplex.{u, u, u, u, u} (projectiveSpaceSite A n)
        (twistSumComplex A n)))).IsWeakTriangulatedGenerator) :
    (tensorWithComplexDerived.{u, u, u, u, u, 0} (projectiveSpaceSite A n) ℤ
        (twistSumComplex A n)).IsEquivalence ∧
      (tensorWithComplexDerived.{u, u, u, u, u, 0} (projectiveSpaceSite A n) ℤ
        (twistSumComplex A n)).IsTriangulated
```

**`Stacks.AlgebraicGeometry.ProjectiveGenerator.twistSumTensorDerivedObjRegularIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveSpaceExampleEquivalence.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ProjectiveSpaceExampleEquivalence.lean#L432). The attribute's comment: “the clause 'sending R to P', with the regular module read over E = Hom^dg(P, P) rather than over the upper triangular matrix algebra R of Tag 0CS9, the identification E = R not being available in this library”.

> **Stacks 0BQU**, the clause *"sending `R` to `P`"*: the derived tensor product with the twist
> sum sends the regular module of its endomorphism differential graded algebra to the twist sum
> itself.
>
> This is `AlgebraicGeometry.RingedSite.tensorWithComplexDerivedObjRegularIso` at `X = ℙⁿ_A` and
> `K = P`. The source writes the regular module as `R`, which this library does not identify with
> the matrix algebra of Tag 0CS9; it is here the regular module over `E = Hom^{dg}(P, P)`.

```lean
def twistSumTensorDerivedObjRegularIso :
    (tensorWithComplexDerived.{u, u, u, u, u, 0} (projectiveSpaceSite A n) ℤ
        (twistSumComplex A n)).obj
        ((quasiIsomorphisms (RingedSite.Rep.{u, u, u, u, u, 0} (projectiveSpaceSite A n) ℤ
            (twistSumComplex A n)).algebra).Q.obj
          ((toHomotopyCategory (RingedSite.Rep.{u, u, u, u, u, 0} (projectiveSpaceSite A n) ℤ
              (twistSumComplex A n)).algebra).obj
            ((RingedSite.Rep.{u, u, u, u, u, 0} (projectiveSpaceSite A n) ℤ
                (twistSumComplex A n)).functor.obj
              (liftComplex.{u, u, u, u, u} (projectiveSpaceSite A n)
                (twistSumComplex A n))))) ≅
      DerivedCategory.Q.obj (liftComplex.{u, u, u, u, u} (projectiveSpaceSite A n)
        (twistSumComplex A n))
```

**`Stacks.AlgebraicGeometry.Beilinson.beilinson_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/BeilinsonEquivalenceLinear.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProjectiveSpace/ExampleGenerator/BeilinsonEquivalenceLinear.lean#L320).

> **[Stacks, Tag 0BQU] (Beilinson).** Let `A` be a ring, `X = P^n_A = Proj A[T₀, …, Tₙ]`,
> `P = 𝒪_X ⊕ 𝒪_X(-1) ⊕ ⋯ ⊕ 𝒪_X(-n)` and `R = Hom_{𝒪_X}(P, P)`, read as in the source as the
> differential graded algebra `Hom_{Comp^dg(𝒪_X)}(P, P)` with zero differential. Then
> `- ⊗_R^𝐋 P : D(R) ⥤ D_QCoh(𝒪_X)` is an `A`-linear equivalence of triangulated categories sending
> `R` to `P`.

```lean
theorem beilinson_equivalence :
    (tensorWithGenerator A n).IsEquivalence ∧ (tensorWithGenerator A n).IsTriangulated ∧
      Nonempty ((tensorWithGenerator A n).obj (regular A n) ≅ twistSumQCoh A n) ∧
      letI := derivedCategoryRLinear A n
      letI := quasiCoherentDerivedCategoryLinear A n
      (tensorWithGenerator A n).Linear A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.20, Tag 0CS7](https://stacks.math.columbia.edu/tag/0CS7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

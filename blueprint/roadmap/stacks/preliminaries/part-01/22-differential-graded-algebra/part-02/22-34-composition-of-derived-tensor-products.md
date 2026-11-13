---
declaration: section
origin: cited
lean: DifferentialGraded.Bimodule.derivedTensorFunctorCounit, DifferentialGraded.Bimodule.compTensor, DifferentialGraded.Bimodule.derivedTensorFunctorCompTensorIso, DifferentialGraded.isIso_derivedTensorBaseChangeComparison_degreeZeroBase, DifferentialGraded.tripleTensorIso, DifferentialGraded.derivedTensorBaseChangeComparison, DifferentialGraded.Bimodule.derivedTensorFunctorCompIsoDegreeZeroBase, DifferentialGraded.Bimodule.compTensorResolution
statement: formalized
proof: formalized
---

# 22.34 Composition of derived tensor products

Section 22.34 of the Stacks Project, [Tag 0BZ1](https://stacks.math.columbia.edu/tag/0BZ1). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BZ2, an equation

[Tag 0BZ2](https://stacks.math.columbia.edu/tag/0BZ2) in the Stacks Project.

**`DifferentialGraded.Bimodule.derivedTensorFunctorCounit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorFunctor.lean#L138). The attribute's comment: “the canonical map from the derived to the plain tensor product”.

> The canonical comparison from the derived tensor product to ordinary tensoring: the counit of
> the Kan extension defining `- ⊗_A^𝐋 N`. Its components are the maps
> `P ⊗_A^𝐋 N → P ⊗_A N` in `D(B, d)`, which are isomorphisms exactly on the objects at which
> ordinary tensoring already computes the derived functor.

```lean
def derivedTensorFunctorCounit (N : Bimodule A B) :
    (quasiIsomorphisms' A).Q ⋙ derivedTensorFunctor N ⟶ tensorFunctorToDerivedCategory N
```

## Tag 0BZ3, a lemma

[Tag 0BZ3](https://stacks.math.columbia.edu/tag/0BZ3) in the Stacks Project.

**`DifferentialGraded.Bimodule.compTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleComposition.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleComposition.lean#L362). The attribute's comment: “the composite bimodule N'' = N (x)\_B N' as an (A, C)-bimodule”.

> **Stacks Tag 0BZ3.** The composite of a differential graded `(A, B)`-bimodule `N` with a
> differential graded `(B, C)`-bimodule `N'`: the relative tensor product `N ⊗_B N'` of the right
> `B`-module underlying `N` with `N'`, carrying the left `A`-action inherited from `N`. This is the
> bimodule `N''` of Tag 0BZ3.

```lean
def compTensor (N : Bimodule A B) (N' : Bimodule B C) : Bimodule A C
```

**`DifferentialGraded.Bimodule.derivedTensorFunctorCompTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorComposition.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorComposition.lean#L291). The attribute's comment: “composition of the derived tensor functors”.

> **Stacks Tag 0BZ3.** *"Let `R` be a ring. Let `(A, d)`, `(B, d)`, and `(C, d)` be differential
> graded `R`-algebras. Let `N` be a differential graded `(A, B)`-bimodule. Let `N'` be a differential
> graded `(B, C)`-bimodule. Assume that (0BZ2) `N_B ⊗_B^𝐋 N' ⟶ (N ⊗_B N')_C` is an isomorphism.
> Then the composition `D(A, d) → D(B, d) → D(C, d)` of `- ⊗_A^𝐋 N` and `- ⊗_B^𝐋 N'` is isomorphic
> to `- ⊗_A^𝐋 N''` where `N'' = N ⊗_B N'`."*
>
> The bimodule `N''` is `DifferentialGraded.Bimodule.compTensor N N'`, the relative tensor product
> with the left `A`-action inherited from `N`, exactly as in the source; the isomorphism is
> `DifferentialGraded.Bimodule.derivedTensorCompNatTrans`, the transformation attached to the
> associativity isomorphism of the plain tensor functors by the universal property of Tag 09LS.

```lean
def derivedTensorFunctorCompTensorIso (N : Bimodule A B) (N' : Bimodule B C)
    (hiso : IsIso ((derivedTensorFunctorCounit N').app
      ((toHomotopyCategory B).obj N.rightModule))) :
    derivedTensorFunctor N ⋙ derivedTensorFunctor N' ≅
      derivedTensorFunctor (compTensor N N')
```

## Tag 0BZ4, an equation

[Tag 0BZ4](https://stacks.math.columbia.edu/tag/0BZ4) in the Stacks Project.

**`DifferentialGraded.isIso_derivedTensorBaseChangeComparison_degreeZeroBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeUnitBaseAlgebra.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeUnitBaseAlgebra.lean#L240). The attribute's comment: “the canonical map is an isomorphism when the first algebra is the base ring in degree zero”.

> **The canonical map of Stacks 0BZ4 is an isomorphism when the first algebra is the base ring
> in degree zero.** For differential graded `R`-algebras `(B, d)` and `(C, d)`, the map
> `(R ⊗_R B)_B ⊗_B^𝐋 {}_B(B ⊗_R C)_C ⟶ (R ⊗_R B ⊗_R C)_C` of `D(C, d)` is invertible, with nothing
> assumed about `B` or `C`.
>
> By `DifferentialGraded.Bimodule.isIso_derivedTensorBaseChangeComparison_iff` the assertion is
> that the comparison of Tag 09LS from the derived to the plain tensor product with
> `{}_B(B ⊗_R C)_C` is invertible at the right differential graded `B`-module `(R ⊗_R B)_B`. That
> module is the regular module, by `DifferentialGraded.unitBaseChangeIso`, and the regular module
> is orthogonal on the left to the acyclic modules by Tag 09K1, where the plain tensor product
> already computes the derived one.
>
> This is the hypothesis that Stacks 0BZ5 assumes and that Stacks 09S4 discharges from K-flatness
> of `C`; over the base ring no K-flatness is needed.

```lean
theorem isIso_derivedTensorBaseChangeComparison_degreeZeroBase
    (C : DifferentialGradedAlgebra.{u, u} R) :
    IsIso (derivedTensorBaseChangeComparison (degreeZero R R) B C)
```

**`DifferentialGraded.tripleTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorAlgebraComparison.lean, line 566](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorAlgebraComparison.lean#L566). The attribute's comment: “the identification of the plain tensor products”.

> The identification
> `(A ⊗_R B)_B ⊗_B {}_B(B ⊗_R C)_C = (A ⊗_R B ⊗_R C)_C`: the plain relative tensor product of the
> two base-change bimodules is the triple tensor product, as right differential graded
> `C`-modules.

```lean
def tripleTensorIso : plainTensorObj A B C ≅ baseChangeModule (tensorProduct A B) C
```

**`DifferentialGraded.derivedTensorBaseChangeComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorAlgebraComparison.lean, line 592](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorAlgebraComparison.lean#L592). The attribute's comment: “the canonical map in D(C, d)”.

> The canonical map
> `(A ⊗_R B)_B ⊗_B^𝐋 {}_B(B ⊗_R C)_C ⟶ (A ⊗_R B ⊗_R C)_C` in `D(C, d)`. It is the comparison of
> the derived with the plain tensor product at the right differential graded `B`-module
> `A ⊗_R B`, followed by the identification of the plain tensor product
> `(A ⊗_R B)_B ⊗_B {}_B(B ⊗_R C)_C` with `A ⊗_R B ⊗_R C`.

```lean
def derivedTensorBaseChangeComparison :
    (Bimodule.derivedTensorFunctor (baseChangeBimodule B C)).obj
        ((quasiIsomorphisms' B).Q.obj ((toHomotopyCategory B).obj (baseChangeModule A B))) ⟶
      (quasiIsomorphisms' C).Q.obj
        ((toHomotopyCategory C).obj (baseChangeModule (tensorProduct A B) C))
```

## Tag 0BZ5, a lemma

[Tag 0BZ5](https://stacks.math.columbia.edu/tag/0BZ5) in the Stacks Project.

**`DifferentialGraded.Bimodule.derivedTensorFunctorCompIsoDegreeZeroBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeUnitBaseAlgebra.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeUnitBaseAlgebra.lean#L265). The attribute's comment: “unconditionally when the first algebra is the base ring in degree zero”.

> **Stacks 0BZ5 when the first algebra is the base ring in degree zero**, with nothing assumed.
> For a differential graded `R`-algebra `(C, d)`, a differential graded `(R, B)`-bimodule `N` and a
> differential graded `(B, C)`-bimodule `N'`, the composite of `- ⊗_R^𝐋 N : D(R) ⥤ D(B, d)` and
> `- ⊗_B^𝐋 N' : D(B, d) ⥤ D(C, d)` is the derived tensor functor of the differential graded
> `(R, C)`-bimodule `N'' = Ñ ⊗_B Ñ'` of Stacks 0BZ3.
>
> This is `DifferentialGraded.Bimodule.derivedTensorFunctorCompIsoOfBaseChange` with its only
> hypothesis — the map of Tag 0BZ4, which Stacks 0BZ5 assumes to be an isomorphism — supplied by
> `DifferentialGraded.isIso_derivedTensorBaseChangeComparison_degreeZeroBase`. Here `D(R)` is the
> derived category of the base ring viewed as a differential graded algebra concentrated in degree
> zero, which is the derived category of `R`-modules by
> `DifferentialGradedModule.degreeZeroDerivedEquivalence`.

```lean
def derivedTensorFunctorCompIsoDegreeZeroBase
    (C : DifferentialGradedAlgebra.{u, u} R)
    (N : Bimodule (degreeZero R R) B) (N' : Bimodule B C) :
    derivedTensorFunctor N ⋙ derivedTensorFunctor N' ≅
      derivedTensorFunctor (compTensorResolution N N')
```

**`DifferentialGraded.Bimodule.compTensorResolution`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleComposition.lean, line 415](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleComposition.lean#L415). The attribute's comment: “the bimodule N'' described in the proof”.

> **The bimodule `N''` of Stacks Tag 0BZ5.** Given a differential graded `(A, B)`-bimodule `N`
> and a differential graded `(B, C)`-bimodule `N'`, it is the composite `Ñ ⊗_B Ñ'` of their
> property-(P) replacements, viewed as a differential graded `(A, C)`-bimodule.

```lean
def compTensorResolution (N : Bimodule A B) (N' : Bimodule B C) : Bimodule A C
```

**`DifferentialGraded.Bimodule.derivedTensorFunctorCompIsoOfBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorBaseChangeSecondVariable.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorBaseChangeSecondVariable.lean#L318). The attribute's comment: “the composite of the two derived tensor functors is the derived tensor functor of the composite bimodule, under the Tag 0BZ4 isomorphism that the source itself assumes”.

> **Stacks 0BZ5 with Tag 0BZ4 as its only hypothesis.** For differential graded algebras
> `(A, d)`, `(B, d)` and `(C, d)` over `R` such that the canonical map
> `(A ⊗_R B)_B ⊗_B^𝐋 {}_B(B ⊗_R C)_C ⟶ (A ⊗_R B ⊗_R C)_C` of Tag 0BZ4 is an isomorphism, the
> composite of `- ⊗_A^𝐋 N` and `- ⊗_B^𝐋 N'` is isomorphic to `- ⊗_A^𝐋 N''` for the differential
> graded `(A, C)`-bimodule `N'' = Ñ ⊗_B Ñ'` of the source.
>
> This is `DifferentialGraded.Bimodule.derivedTensorFunctorCompIso` with all four of its remaining
> inputs supplied: the second assertion of Tag 09S3 twice, Tag 0BZ3, and the dévissage of the
> present proof.

```lean
def derivedTensorFunctorCompIsoOfBaseChange
    (hiso : IsIso (derivedTensorBaseChangeComparison A B C))
    (N : Bimodule A B) (N' : Bimodule B C) :
    derivedTensorFunctor N ⋙ derivedTensorFunctor N' ≅
      derivedTensorFunctor (compTensorResolution N N')
```

## Tag 09S4, a lemma

[Tag 09S4](https://stacks.math.columbia.edu/tag/09S4) in the Stacks Project.

**`DifferentialGraded.Bimodule.isIso_derivedTensorBaseChangeComparison_of_kFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeTensorKFlat.lean, line 1023](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/BaseChangeTensorKFlat.lean#L1023). The attribute's comment: “the canonical map (0BZ4) is an isomorphism”.

> **Stacks Tag 09S4, first conclusion.** *"Let `R` be a ring. Let `(A, d)`, `(B, d)`, and
> `(C, d)` be differential graded `R`-algebras. If `C` is K-flat as a complex of `R`-modules, then
> (0BZ4) is an isomorphism."*
>
> The map of Tag 0BZ4 is
> `DifferentialGraded.derivedTensorBaseChangeComparison`, the canonical map
> `(A ⊗_R B)_B ⊗_B^𝐋 {}_B(B ⊗_R C)_C ⟶ (A ⊗_R B ⊗_R C)_C` in `D(C, d)`, and K-flatness is
> `CochainComplex.KFlat` (Tag 06XZ) of the complex of `R`-modules underlying `C`.
>
> The source's argument is followed: on underlying complexes, tensoring over `B` with
> `{}_B(B ⊗_R C)_C` is tensoring over `R` with `C`, so by Tag 06Y0 it carries quasi-isomorphisms to
> quasi-isomorphisms; hence the plain tensor functor already computes the derived one and the
> comparison of Tag 09LS is invertible everywhere, in particular at `(A ⊗_R B)_B`, which by
> `DifferentialGraded.Bimodule.isIso_derivedTensorBaseChangeComparison_iff` is the assertion.

```lean
theorem isIso_derivedTensorBaseChangeComparison_of_kFlat
    (A B C : DifferentialGradedAlgebra.{u, u} R)
    (hC : CochainComplex.KFlat.{u, u} (regularModule C).toCochainComplex) :
    IsIso (derivedTensorBaseChangeComparison A B C)
```

**`DifferentialGraded.Bimodule.derivedTensorFunctorCompIsoOfKFlatAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorBaseChangeSecondVariable.lean, line 344](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/DifferentialGraded/Module/DerivedTensorBaseChangeSecondVariable.lean#L344). The attribute's comment: “the conclusion of Stacks 0BZ5 is valid when C is K-flat as a complex of R-modules”.

> **Stacks Tag 09S4, second conclusion.** *"Let `R` be a ring. Let `(A, d)`, `(B, d)`, `(C, d)`
> be differential graded `R`-algebras. If `C` is K-flat as a complex of `R`-modules, then (0BZ4) is
> an isomorphism and the conclusion of Lemma 0BZ5 is valid."* This is the second half: if `C` is
> K-flat as a complex of `R`-modules, then for every differential graded `(A, B)`-bimodule `N` and
> every differential graded `(B, C)`-bimodule `N'` the composite of `- ⊗_A^𝐋 N` and `- ⊗_B^𝐋 N'`
> is isomorphic to `- ⊗_A^𝐋 N''` for the differential graded `(A, C)`-bimodule
> `N'' = Ñ ⊗_B Ñ'` of `DifferentialGraded.Bimodule.compTensorResolution`, which is the conclusion
> of Tag 0BZ5.
>
> K-flatness of `C` is the only hypothesis, exactly as in the source. The first half of the tag,
> `DifferentialGraded.Bimodule.isIso_derivedTensorBaseChangeComparison_of_kFlat`, supplies the sole
> hypothesis of Tag 0BZ5 in the form
> `DifferentialGraded.Bimodule.derivedTensorFunctorCompIsoOfBaseChange`, whose own four inputs are
> discharged there by the second assertion of Tag 09S3 twice, Tag 0BZ3 and the dévissage above.

```lean
def derivedTensorFunctorCompIsoOfKFlatAlgebra
    (hC : CochainComplex.KFlat.{u, u} (regularModule C).toCochainComplex)
    (N : Bimodule A B) (N' : Bimodule B C) :
    derivedTensorFunctor N ⋙ derivedTensorFunctor N' ≅
      derivedTensorFunctor (compTensorResolution N N')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.34, Tag 0BZ1](https://stacks.math.columbia.edu/tag/0BZ1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

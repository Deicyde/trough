---
declaration: section
origin: cited
lean: SheafOfModules.koszulDifferentialGradedAlgebra, Stacks.AlgebraicGeometry.SeqKoszul.koszulDifferentialGradedAlgebra
statement: formalized
proof: formalized
---

# 17.24 Koszul complexes

Section 17.24 of the Stacks Project, [Tag 062J](https://stacks.math.columbia.edu/tag/062J). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 062K, a definition

[Tag 062K](https://stacks.math.columbia.edu/tag/062K) in the Stacks Project.

**`SheafOfModules.koszulDifferentialGradedAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/DifferentialGradedAlgebra.lean, line 193](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/DifferentialGradedAlgebra.lean#L193). References: SGA 3 III (4.6.1), “Koszul complex”.

> **The Koszul complex `K_•(φ)` of an `O`-module map `φ : F → O`, as a sheaf of differential
> graded algebras.** This is Stacks tag 062K. Its underlying graded algebra is the exterior algebra
> `⋀(F)` of Section 17.21, read with the grading negated because the complex of a sheaf of
> differential graded algebras is a cochain complex while the Koszul differential lowers the
> exterior degree; that is
> `SheafOfModules.koszulDifferentialGradedAlgebra_toGradedAlgebra`, and `⋀(F)` has the universal
> property of the exterior algebra on `F` by
> `SheafOfModules.isExteriorAlgebra_sheafifiedExteriorAlgebra`, which is item (1) of the tag. Its
> differential is the Koszul differential of `φ`, which is the unique graded derivation of `⋀(F)`
> taking a degree-one local section `e` to `φ(e)`
> (`SheafOfModules.existsUnique_koszulDerivation`), which is item (2). The tag calls the result a
> *commutative* differential graded algebra; `SheafOfModules.DifferentialGradedAlgebra` is Stacks
> tag 0FRF's notion and carries no commutativity axiom, and graded commutativity of `⋀(F)` is
> `SheafOfModules.sheafifiedExteriorMul_comm`.
>
> `SheafOfModules.ringedSpaceKoszulDifferentialGradedAlgebra` is the specialization to a ringed
> space, which is the generality the tag is stated in.

```lean
noncomputable def koszulDifferentialGradedAlgebra :
    DifferentialGradedAlgebra.{w, w} (toRingCat J Osharp)
```

## Tag 062L, a definition

[Tag 062L](https://stacks.math.columbia.edu/tag/062L) in the Stacks Project.

**`Stacks.AlgebraicGeometry.SeqKoszul.koszulDifferentialGradedAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/SequenceDifferentialGradedAlgebra.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/SequenceDifferentialGradedAlgebra.lean#L99). The attribute's comment: “the Koszul complex of 062K at `(f₁, …, f_r) : O_X^{⊕ r} → O_X`, as a sheaf of differential graded algebras; `sheafComplex` is its chain complex of sectionwise exterior powers”.

> **The Koszul complex `K_•(O_X, f₁, …, f_r)` on a family of global sections of a ringed
> space**: the Koszul complex of Stacks tag 062K associated to the map
> `(f₁, …, f_r) : O_X^{⊕ r} → O_X`, as a sheaf of differential graded algebras. Its underlying
> graded algebra is the exterior algebra `⋀(O_X^{⊕ r})`, and its differential is the unique
> derivation taking a local section `v` of `O_X^{⊕ r}` to `∑ i, vᵢ fᵢ`
> (`koszulDifferentialGradedAlgebra_d_exteriorGenerator`,
> `SheafOfModules.existsUnique_koszulDerivation`).

```lean
noncomputable def koszulDifferentialGradedAlgebra :
    SheafOfModules.DifferentialGradedAlgebra.{u, u} (structureSheafRing X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.24, Tag 062J](https://stacks.math.columbia.edu/tag/062J)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

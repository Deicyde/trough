---
declaration: section
origin: cited
lean: SheafOfModules.koszulDifferentialGradedAlgebra, PresheafOfModules.seqExteriorFunctional, Stacks.AlgebraicGeometry.SeqKoszul.sheafComplex
statement: formalized
proof: formalized
---

# 17.24 Koszul complexes

Section 17.24 of the Stacks Project, [Tag 062J](https://stacks.math.columbia.edu/tag/062J). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 062K, a definition

[Tag 062K](https://stacks.math.columbia.edu/tag/062K) in the Stacks Project.

**`SheafOfModules.koszulDifferentialGradedAlgebra`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/DifferentialGradedAlgebra.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/DifferentialGradedAlgebra.lean#L193). References: SGA 3 III (4.6.1), “Koszul complex”.

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

**`PresheafOfModules.seqExteriorFunctional`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/Sequence.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/Sequence.lean#L167). The attribute's comment: “the morphism `(f₁, …, f_r) : O^{⊕ r} → O` the Koszul complex is attached to, not the complex itself”.

> **The functional `(f₁, …, f_r) : O^{⊕ r} → O`.** Over each object it is the ring-level
> `Koszul.seqDual` of the family of sections restricted there.

```lean
noncomputable def seqExteriorFunctional {r : ℕ} (f : Sequence O r) :
    ExteriorFunctional.{v, u, w, w} (finFree O r)
```

**`Stacks.AlgebraicGeometry.SeqKoszul.sheafComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/SheafCondition.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Koszul/Sheaf/SheafCondition.lean#L192). The attribute's comment: “the complex `K_•(O_X, f₁, …, f_r)` itself, on a ringed space and as a chain complex of sheaves of modules”. References: EGA III (1.1.1), “more general”; SGA 3 III (4.6.1), “more general”; SGA 6 VII (1.1), “special case”.

> **`K_•(O_X, f₁, …, f_r)` as a chain complex of sheaves of modules.** In degree `n` it is the
> sheaf of exterior powers `U ↦ ⋀^n_{O_X(U)}(O_X(U)^r)` and the differential is contraction by
> `(f₁, …, f_r)`. This is the complex whose acyclicity in positive degrees is Koszul-regularity of
> the family, in the sense of Stacks tag 063D.

```lean
noncomputable def sheafComplex : ChainComplex (SheafOfModules.{u} (ringSheaf X)) ℕ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.24, Tag 062J](https://stacks.math.columbia.edu/tag/062J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

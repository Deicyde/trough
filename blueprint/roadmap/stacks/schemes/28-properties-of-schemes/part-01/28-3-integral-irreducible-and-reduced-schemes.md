---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsIntegral, AlgebraicGeometry.IsReduced.component_reduced, AlgebraicGeometry.isReduced_of_isReduced_stalk, AlgebraicGeometry.isReduced_stalk_of_isReduced, AlgebraicGeometry.IsReduced.of_openCover, AlgebraicGeometry.isReduced_of_isAffine_isReduced, AlgebraicGeometry.Scheme.irreducibleSpace_tfae, AlgebraicGeometry.isIntegral_iff_irreducibleSpace_and_isReduced
statement: formalized
proof: formalized
---

# 28.3 Integral, irreducible, and reduced schemes

Section 28.3 of the Stacks Project, [Tag 01OJ](https://stacks.math.columbia.edu/tag/01OJ). 4 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01OK, a definition

[Tag 01OK](https://stacks.math.columbia.edu/tag/01OK) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsIntegral`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsIntegral#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L32) (StacksFrontier): “Mathlib asks Γ(X, U) to be a domain for every nonempty open U; this is equivalent to the affine-open condition”. References: EGA I (2.1.8); SGA 6 XIII (2.2).

## Tag 01OL, a lemma

[Tag 01OL](https://stacks.math.columbia.edu/tag/01OL) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsReduced.component_reduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsReduced.component_reduced#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L34) (StacksFrontier): “(4): the definition of `IsReduced`, every Γ(X, U) is reduced”.
- [`AlgebraicGeometry.isReduced_of_isReduced_stalk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isReduced_of_isReduced_stalk#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L36) (StacksFrontier): “(1) ⇒ (4): reduced local rings give reduced rings of sections”.
- [`AlgebraicGeometry.isReduced_stalk_of_isReduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isReduced_stalk_of_isReduced#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L38) (StacksFrontier): “(4) ⇒ (1): the local rings of a reduced scheme are reduced”. References: EGA IV (10.10.4), “forward direction”.
- [`AlgebraicGeometry.IsReduced.of_openCover`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsReduced.of_openCover#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L40) (StacksFrontier): “(2) ⇒ (4): reducedness can be checked on an open cover”.
- [`AlgebraicGeometry.isReduced_of_isAffine_isReduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isReduced_of_isAffine_isReduced#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L42) (StacksFrontier): “(2) ⇒ (4): an affine piece with reduced global sections is reduced”. References: EGA I (5.1.4), “partial”; EGA II (1.3.8), “special case”.

## Tag 01OM, a lemma

[Tag 01OM](https://stacks.math.columbia.edu/tag/01OM) in the Stacks Project.

**`AlgebraicGeometry.Scheme.irreducibleSpace_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/Irreducible.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/Irreducible.lean#L115).

> **Stacks Project, Tag 01OM.** A scheme is irreducible if and only if it
> has a nonempty affine open cover by irreducible opens whose members meet
> pairwise, if and only if it is nonempty and every nonempty affine open is
> irreducible.

```lean
theorem irreducibleSpace_tfae (X : Scheme.{u}) :
    List.TFAE [
      IrreducibleSpace X,
      ∃ (ι : Type u) (U : ι → X.Opens),
        Nonempty ι ∧
          IsOpenCover U ∧
          (∀ i, IsAffineOpen (U i)) ∧
          (∀ i, IrreducibleSpace (U i)) ∧
          ∀ i j, Set.Nonempty ((U i : Set X) ∩ (U j : Set X)),
      Nonempty X ∧
        ∀ U : X.Opens, IsAffineOpen U → Nonempty U → IrreducibleSpace U]
```

## Tag 01ON, a lemma

[Tag 01ON](https://stacks.math.columbia.edu/tag/01ON) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.isIntegral_iff_irreducibleSpace_and_isReduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isIntegral_iff_irreducibleSpace_and_isReduced#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch28.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch28.lean#L45) (StacksFrontier): “the equivalence”. References: EGA I (6.1.12), “necessity”; EGA I (2.1.8); EGA I (7.2.8), “partial”; EGA I (7.3.6), “partial”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.3, Tag 01OJ](https://stacks.math.columbia.edu/tag/01OJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

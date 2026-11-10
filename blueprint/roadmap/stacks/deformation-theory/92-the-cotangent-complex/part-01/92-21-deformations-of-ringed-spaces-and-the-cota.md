---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpaceThickening.DeformationSolution, AlgebraicGeometry.RingedSpaceThickening.solutionClassesCotangentAddTorsor, AlgebraicGeometry.RingedSpaceThickening.cotangentObstruction_eq_zero_iff, AlgebraicGeometry.RingedSpaceThickening.DeformationSolution.solutionAutMulEquivCotangentExt
statement: formalized
proof: formalized
---

# 92.21 Deformations of ringed spaces and the cotangent complex

Section 92.21 of the Stacks Project, [Tag 08UX](https://stacks.math.columbia.edu/tag/08UX). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08UY, an equation

[Tag 08UY](https://stacks.math.columbia.edu/tag/08UY) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.DeformationSolution`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/DeformationDiagram.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/DeformationDiagram.lean#L60). The attribute's comment: “the same displayed deformation problem for ringed spaces”.

> A solution of the first order deformation problem for a fixed
> first order thickening `t : S ⟶ S'`, morphism `f : X ⟶ S`, `𝒪_X`-module `𝒢` and prescribed map
> `c : f^* t^* 𝒥 ⟶ 𝒢`: a first order thickening `i : X ⟶ X'` and a morphism `f' : X' ⟶ S'` over
> `t`, together with an identification of the ideal of `i` with `𝒢` under which the vertical map
> on ideals induced by `f'` is exactly `c`.

```lean
structure DeformationSolution {X S S' : RingedSpace.{u, u}} (t : S ⟶ S')
    (ht : IsFirstOrderThickening t) (f : X ⟶ S)
    (G : SheafOfModules.{u} (structureSheafRing X))
    (c : (modulePullback f).obj
      ((modulePullback t).obj (AlgebraicGeometry.SheafOfModules.idealSheaf t)) ⟶ G)
```

## Tag 08UZ, a lemma

[Tag 08UZ](https://stacks.math.columbia.edu/tag/08UZ) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.solutionClassesCotangentAddTorsor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/CotangentDeformationClassesTorsor.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/CotangentDeformationClassesTorsor.lean#L75). The attribute's comment: “clause (2): if a solution of 08UY exists, the set of isomorphism classes of solutions is principal homogeneous under Ext¹(L_{X/S}, 𝒢)”. References: SGA 7 VI (4.16), “more general”.

> **Stacks Project, Tag 08UZ, clause (2).** If there exists a solution of the deformation
> problem of **Stacks 08UY**, then the set of isomorphism classes of solutions is principal
> homogeneous under `Ext¹_{𝒪_X}(L_{X/S}, 𝒢)`, as Mathlib's `AddTorsor`.
>
> The set of isomorphism classes is `SolutionClasses t ht f G c`, the `Quotient` of the solutions
> by `Isomorphic`. The structure is the one of **Stacks 08UC** (`solutionClassesAddTorsor`) under
> `Ext¹_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢)`, read through the identification
> `Ext¹_{𝒪_X}(𝖭𝖫_{X/S}, 𝒢) = Ext¹_{𝒪_X}(L_{X/S}, 𝒢)` of **Stacks 08UW**
> (`naiveExtCotangentAddEquiv`). `hne` is the source's "if there exists a solution".

```lean
noncomputable def solutionClassesCotangentAddTorsor
    (hne : Nonempty (DeformationSolution t ht f G c)) :
    AddTorsor (cotangentExt f G 1) (SolutionClasses t ht f G c)
```

**`AlgebraicGeometry.RingedSpaceThickening.cotangentObstruction_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/CotangentObstruction.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/CotangentObstruction.lean#L339). The attribute's comment: “clause (1): there is a canonical element ξ ∈ Ext²(L_{X/S}, 𝒢) whose vanishing is a sufficient and necessary condition for the existence of a solution to (08UY)”.

> **Stacks Project, Tag 08UZ, clause (1).** Let `t : S ⟶ S'` be a first order thickening of
> ringed spaces with ideal `𝒥`, `f : X ⟶ S` a morphism of ringed spaces, `𝒢` an `𝒪_X`-module and
> `c : f^* t^* 𝒥 ⟶ 𝒢` the prescribed map on ideals (the setup of **Stacks 08UY**). The canonical
> class `ξ = cotangentObstruction f G ht c ∈ Ext²_{𝒪_X}(L_{X/S}, 𝒢)` vanishes if and only if the
> deformation problem (08UY) has a solution.
>
> The proof is the source's: by **Stacks 0GQ3** (realized here through square-zero extensions of
> `(f ∘ t)⁻¹𝒪_{S'}`-algebras with bijective ideal, `exists_ideal_bijective_extClass_eq`, and the
> correspondence `DeformationSolution.toAlgebraExtension` / `toDeformationSolution` with solutions)
> a solution exists exactly when `ξ' = c ∘ κ ∈ Ext¹(L_{A/A'} ⊗_A 𝒪_X, 𝒢)` comes from
> `Ext¹(L_{X/S'}, 𝒢) = Ext¹(𝖭𝖫_{X/S'}, 𝒢)` (**Stacks 08UW**), and the long exact sequence of the
> distinguished triangle of **Stacks 08T4** identifies those classes with the ones whose image
> in `Ext²(L_{X/S}, 𝒢)` vanishes.

```lean
theorem cotangentObstruction_eq_zero_iff :
    cotangentObstruction f G ht c = 0 ↔ Nonempty (DeformationSolution t ht f G c)
```

**`AlgebraicGeometry.RingedSpaceThickening.DeformationSolution.solutionAutMulEquivCotangentExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/SolutionAutomorphismGroup.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/RingedSpaceThickening/SolutionAutomorphismGroup.lean#L233). The attribute's comment: “clause (3): the group of automorphisms of a solution X' fitting into (08UY), under composition, is isomorphic to the additive group Ext^0(L_{X/S}, G)”.

> **Stacks Project, Tag 08UZ, clause (3).** Given a solution `X'` of the deformation problem
> of (08UY), the group of automorphisms of `X'` fitting into that diagram is canonically
> isomorphic to `Ext⁰_{𝒪_X}(L_{X/S}, 𝒢)`.
>
> The automorphisms in question are the `SolutionHom Q Q`: morphisms of the deformed space under
> `X`, over `S'`, and the identity on the prescribed ideal `𝒢`. Every one is invertible by
> `SolutionHom.isIso_hom`, so these are the automorphisms of `X'` in the diagram; they form a
> group under composition (`SolutionHom.instGroup`, with `SolutionHom.mul_hom`,
> `SolutionHom.one_hom`, `SolutionHom.inv_hom`). The isomorphism is a group isomorphism onto the
> additive group `Ext⁰_{𝒪_X}(L_{X/S}, 𝒢)`, written multiplicatively. Its underlying bijection is
> `solutionHomEquivCotangentExt`: an automorphism is `x ↦ x + δ(x)` for a unique relative
> derivation `δ` of `𝒪_X` over `f⁻¹𝒪_S` with values in `𝒢`, and these derivations are
> `Hom_{𝒪_X}(Ω_{X/S}, 𝒢) = Ext⁰_{𝒪_X}(L_{X/S}, 𝒢)`. Composition goes to addition because
> `(id + δ₁) ∘ (id + δ₂) = id + δ₁ + δ₂`, the ideal having square zero (`toDerivation_mul`).

```lean
noncomputable def solutionAutMulEquivCotangentExt :
    SolutionHom Q Q ≃* Multiplicative (cotangentExt f G 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.21, Tag 08UX](https://stacks.math.columbia.edu/tag/08UX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: TensorProduct, LinearMap.baseChange, Algebra.TensorProduct.includeRight, literalModule, Module.Finite.tensorBaseChange, Module.FinitePresentation.tensorBaseChange, Algebra.FiniteType.baseChange, Algebra.FinitePresentation.baseChange
statement: formalized
proof: formalized
---

# 10.14 Base change

Section 10.14 of the Stacks Project, [Tag 05G3](https://stacks.math.columbia.edu/tag/05G3). 5 tags here are carried by 3 declarations of the repository (all in StacksCore) and 15 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05G4, a definition

[Tag 05G4](https://stacks.math.columbia.edu/tag/05G4) in the Stacks Project.

Declarations registered for the tag:

- [`TensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/Basic.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Basic.lean#L11) (StacksCore). References: EGA 0 (21.1.4), “partial”; EGA III (7.2.6); EGA IV (2.5.8), “partial”; EGA IV (18.3.2.1); SGA 2 III (2.11); SGA 2 IV (4.6); SGA 3 VIIB (2.3.2), “partial”; SGA 4 IV (12.7), “special case”; SGA 4 XVII (4.1.6), “special case”; SGA 4½ Cycle (1.3), “Clause a)”; SGA 4½ Fonctions L (3.8); SGA 5 V (1.2), “special case”; SGA 6 IV (2.6), “special case”; SGA 6 VII (4.6), “more general”; SGA 7 IX (4.7.3).
- [`LinearMap.baseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LinearMap.baseChange#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/Tower.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Tower.lean#L12) (StacksCore). References: EGA II (6.4.1); EGA II (6.4.2); EGA II (6.4.7); SGA 1 IV (2.6); SGA 4½ Fonctions L (3.8).
- [`Algebra.TensorProduct.includeRight`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.TensorProduct.includeRight#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/BaseChangeDefinition.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BaseChangeDefinition.lean#L22) (StacksFrontier): “The base change of the ring map `R → S` by `R → R'` is the ring map `R' → S' = S ⊗[R] R'`, `r' ↦ 1 ⊗ r'`.”. References: EGA 0 (7.7.6); EGA 0 (20.4.1), “partial”; EGA I (3.2.2); EGA IV (16.3.7).
- [`literalModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FiniteStability.lean#L124), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/BaseChangeDefinition.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/BaseChangeDefinition.lean#L25) (StacksFrontier): “The base change of the `S`-module `M` is the `S' = S ⊗[R] R'`-module `M ⊗[R] R'`.”.

## Tag 05G5, a lemma

[Tag 05G5](https://stacks.math.columbia.edu/tag/05G5) in the Stacks Project.

**`Module.Finite.tensorBaseChange`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/FiniteStability.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FiniteStability.lean#L156). The attribute's comment: “(1)”.

> **Stacks 05G5 (1)**: if `M` is a finite `S`-module then `M' = M ⊗[R] R'` is a finite
> `S' = S ⊗[R] R'`-module.

```lean
theorem Module.Finite.tensorBaseChange [Module.Finite S M] :
    Module.Finite (S ⊗[R] R') (M ⊗[R] R')
```

**`Module.FinitePresentation.tensorBaseChange`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/FiniteStability.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FiniteStability.lean#L165). The attribute's comment: “(2)”.

> **Stacks 05G5 (2)**: if `M` is a finitely presented `S`-module then `M' = M ⊗[R] R'` is a
> finitely presented `S' = S ⊗[R] R'`-module.

```lean
theorem Module.FinitePresentation.tensorBaseChange [Module.FinitePresentation S M] :
    Module.FinitePresentation (S ⊗[R] R') (M ⊗[R] R')
```

Declarations registered for the tag:

- [`Algebra.FiniteType.baseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FiniteType.baseChange#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FiniteStability.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FiniteStability.lean#L171) (StacksCore): “(3): if `R → S` is of finite type then so is the base change `R' → S'`.”. References: EGA I (6.3.4), “(iv), affine case”; EGA II (3.5.5), “special case”; EGA IV (1.3.1); EGA IV (1.5.4), “(iii), special case”; EGA IV (2.7.1.1), “partial”; SGA 1 VIII (3.4), “forward implication”.
- [`Algebra.FinitePresentation.baseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FinitePresentation.baseChange#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/FiniteStability.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/FiniteStability.lean#L173) (StacksCore): “(4): if `R → S` is of finite presentation then so is the base change `R' → S'`.”. References: EGA IV (8.6.2), “special case”; EGA IV (1.4.1); EGA IV (1.4.3), “(iii), special case”; EGA IV (1.6.2), “(iii), special case”; SGA 1 VIII (3.6), “partial”; SGA 3 XIX (2.1), “special case”.
- [`Module.Finite.base_change`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Finite.base_change#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks05G5.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks05G5.lean#L14) (StacksFrontier): “part 1, base-change form: applied with base ring `S` and `A = S' = S ⊗[R] R'`, a finite `S`-module `M` gives a finite `S'`-module `S' ⊗[S] M`, which is `S'`-isomorphic to `M ⊗[R] R'`”. References: EGA III (2.6.2.1), “special case”; EGA II (6.1.5), “(iii), finite, affine”; SGA 1 III (1.4), “partial”.
- [`FinitePresentation.of_isBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=FinitePresentation.of_isBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks05G5.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks05G5.lean#L17) (StacksFrontier): “part 2, `IsBaseChange` form: applied with base ring `S` and `A = S'`”.
- [`Algebra.FiniteType.baseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FiniteType.baseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks05G5.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks05G5.lean#L19) (StacksFrontier): “part 3”. References: EGA I (6.3.4), “(iv), affine case”; EGA II (3.5.5), “special case”; EGA IV (1.3.1); EGA IV (1.5.4), “(iii), special case”; EGA IV (2.7.1.1), “partial”; SGA 1 VIII (3.4), “forward implication”.
- [`Algebra.FinitePresentation.baseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.FinitePresentation.baseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks05G5.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks05G5.lean#L20) (StacksFrontier): “part 4”. References: EGA IV (8.6.2), “special case”; EGA IV (1.4.1); EGA IV (1.4.3), “(iii), special case”; EGA IV (1.6.2), “(iii), special case”; SGA 1 VIII (3.6), “partial”; SGA 3 XIX (2.1), “special case”.

## Tag 05DQ, a lemma

[Tag 05DQ](https://stacks.math.columbia.edu/tag/05DQ) in the Stacks Project.

Declarations registered for the tag:

- [`ModuleCat.extendRestrictScalarsAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ModuleCat.extendRestrictScalarsAdj#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Category/ModuleCat/ChangeOfRings.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Category/ModuleCat/ChangeOfRings.lean#L29) (StacksCore): “Base change `M ↦ S ⊗_R M` is left adjoint to restriction of scalars `N ↦ N_R`. The tag writes the tensor product in the other order.”.
- [`LinearMap.liftBaseChangeEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LinearMap.liftBaseChangeEquiv#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/TensorProduct/Basic.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/TensorProduct/Basic.lean#L22) (StacksCore): “`Hom_R(M, N_R) = Hom_S(S ⊗_R M, N)`, as an `S`-linear equivalence. The tag writes the tensor product in the other order.”.

## Tag 08YP, a lemma

[Tag 08YP](https://stacks.math.columbia.edu/tag/08YP) in the Stacks Project.

Declarations registered for the tag:

- [`ModuleCat.restrictCoextendScalarsAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ModuleCat.restrictCoextendScalarsAdj#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Category/ModuleCat/ChangeOfRings.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Category/ModuleCat/ChangeOfRings.lean#L33) (StacksCore): “Restriction of scalars `N ↦ N_R` is left adjoint to coextension of scalars `M ↦ Hom_R(S, M)`.”.
- [`ModuleCat.RestrictionCoextensionAdj.HomEquiv.fromRestriction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ModuleCat.RestrictionCoextensionAdj.HomEquiv.fromRestriction#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Category/ModuleCat/ChangeOfRings.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Category/ModuleCat/ChangeOfRings.lean#L35) (StacksCore): “`Hom_R(N_R, M) → Hom_S(N, Hom_R(S, M))`, one direction of the tag's Hom-set formula.”.
- [`ModuleCat.RestrictionCoextensionAdj.HomEquiv.toRestriction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ModuleCat.RestrictionCoextensionAdj.HomEquiv.toRestriction#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Category/ModuleCat/ChangeOfRings.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Algebra/Category/ModuleCat/ChangeOfRings.lean#L37) (StacksCore): “`Hom_S(N, Hom_R(S, M)) → Hom_R(N_R, M)`, the other direction of the tag's Hom-set formula.”.

## Tag 08YQ, a lemma

[Tag 08YQ](https://stacks.math.columbia.edu/tag/08YQ) in the Stacks Project.

**`tensorHomAdjEquiv`**, a def in StacksCore (human-reviewed), declared in [StacksCore/LinearAlgebra/TensorProduct/Tower.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Tower.lean#L116).

> **Stacks 08YQ**: `Hom_R(M ⊗_S N, P) = Hom_S(M, Hom_R(N, P))` for `S`-modules `M`, `N` and an
> `R`-module `P`.
>
> Stated `S`-linearly rather than as a bare bijection: both sides carry the source `S`-action —
> the left through `M ⊗_S N`, the right through `Hom_R(N, P)` — so `S` is the finer structure and
> `R`-linearity is its restriction. This matches how Mathlib states the sibling tag 05DQ, where
> `LinearMap.liftBaseChangeEquiv` is linear over the *bigger* ring.

```lean
noncomputable def tensorHomAdjEquiv : (M ⊗[S] N →ₗ[R] P) ≃ₗ[S] (M →ₗ[S] (N →ₗ[R] P))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.14, Tag 05G3](https://stacks.math.columbia.edu/tag/05G3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

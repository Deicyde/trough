---
declaration: section
origin: cited
lean: LinearMap.mk₂, TensorProduct.existsUnique_linearEquiv_compr₂_eq_of_universal, IsTensorProduct.existsUnique_linearEquiv_compr₂_eq, TensorProduct.lift, TensorProduct.lift.unique, TensorProduct.lift.tmul, TensorProduct.directSumLeft, TensorProduct.lid
statement: formalized
proof: formalized
---

# 10.12 Tensor products

Section 10.12 of the Stacks Project, [Tag 00CV](https://stacks.math.columbia.edu/tag/00CV). 16 tags here are carried by 15 declarations of the repository (3 in StacksCore and 12 in StacksFrontier) and 27 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00CW, a definition

[Tag 00CW](https://stacks.math.columbia.edu/tag/00CW) in the Stacks Project.

Declarations registered for the tag:

- [`LinearMap.mk₂`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LinearMap.mk₂#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/BilinearMap.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/BilinearMap.lean#L8) (StacksCore).

## Tag 00CX, a lemma

[Tag 00CX](https://stacks.math.columbia.edu/tag/00CX) in the Stacks Project.

**`TensorProduct.existsUnique_linearEquiv_compr₂_eq_of_universal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/UniversalPair.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/UniversalPair.lean#L48). The attribute's comment: “Uniqueness: two universal pairs `(T, g)`, `(T', g')` admit a unique isomorphism `j : T ≃ T'` with `j ∘ g = g'`; the universal property quantifies over modules in the universe of `T` and `T'`.”.

> **Stacks 00CX** (uniqueness). If `(T, g)` and `(T', g')` are two pairs of an `R`-module and an
> `R`-bilinear map `M × N → _` which both have the universal property (every bilinear map `f` to an
> `R`-module `P` is `f̃ ∘ g` for a unique linear `f̃`), then there is a unique `R`-linear isomorphism
> `j : T ≃ T'` with `j ∘ g = g'`. The universal property is quantified over modules `P` in the
> universe of `T` and `T'`.

```lean
theorem existsUnique_linearEquiv_compr₂_eq_of_universal {T T' : Type w} [AddCommGroup T]
    [Module R T] [AddCommGroup T'] [Module R T'] (g : M →ₗ[R] N →ₗ[R] T)
    (g' : M →ₗ[R] N →ₗ[R] T')
    (hg : ∀ (P : Type w) [AddCommGroup P] [Module R P] (f : M →ₗ[R] N →ₗ[R] P),
      ∃! f' : T →ₗ[R] P, g.compr₂ f' = f)
    (hg' : ∀ (P : Type w) [AddCommGroup P] [Module R P] (f : M →ₗ[R] N →ₗ[R] P),
      ∃! f' : T' →ₗ[R] P, g'.compr₂ f' = f) :
    ∃! j : T ≃ₗ[R] T', g.compr₂ j.toLinearMap = g'
```

**`IsTensorProduct.existsUnique_linearEquiv_compr₂_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/UniversalPair.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/UniversalPair.lean#L83). The attribute's comment: “Uniqueness, for pairs exhibited as tensor products by `IsTensorProduct`: there is a unique isomorphism `j : T ≃ T'` with `j ∘ g = g'`.”.

> **Stacks 00CX** (uniqueness, for `IsTensorProduct`). If `g : M × N → T` and `g' : M × N → T'`
> are bilinear maps exhibiting `T` and `T'` as tensor products of `M` and `N` (Mathlib's
> `IsTensorProduct`), then there is a unique `R`-linear isomorphism `j : T ≃ T'` with
> `j ∘ g = g'`.

```lean
theorem existsUnique_linearEquiv_compr₂_eq {g : M →ₗ[R] N →ₗ[R] T} {g' : M →ₗ[R] N →ₗ[R] T'}
    (hg : IsTensorProduct g) (hg' : IsTensorProduct g') :
    ∃! j : T ≃ₗ[R] T', g.compr₂ j.toLinearMap = g'
```

Declarations registered for the tag:

- [`TensorProduct.lift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.lift#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/Basic.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Basic.lean#L8) (StacksCore). References: EGA III (7.2.1), “special case”; SGA 3 VIIB (0.3.5).
- [`TensorProduct.lift.unique`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.lift.unique#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/Basic.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Basic.lean#L9) (StacksCore).
- [`TensorProduct.lift.tmul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.lift.tmul#doc) registered with `add_to_stacks` in [StacksFrontier/LinearAlgebra/TensorProduct/UniversalPair.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/UniversalPair.lean#L30) (StacksFrontier): “The factorization identity `f = f̃ ∘ g`: `TensorProduct.lift f` composed with `m ⊗ₜ n` is `f m n`.”.

## Tag 00CY, a lemma

[Tag 00CY](https://stacks.math.columbia.edu/tag/00CY) in the Stacks Project.

Declarations registered for the tag:

- [`TensorProduct.directSumLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.directSumLeft#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/DirectSum/TensorProduct.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/DirectSum/TensorProduct.lean#L8) (StacksCore). References: EGA III (7.2.6), “special case”; SGA 3 I (4.7.3), “special case”.
- [`TensorProduct.lid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.lid#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/Associator.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Associator.lean#L8) (StacksCore). References: SGA 3 VIIB (0.3.2), “special case”.
- [`TensorProduct.comm`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.comm#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/Basic.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Basic.lean#L10) (StacksCore).
- [`TensorProduct.comm`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.comm#doc) registered with `add_to_stacks` in [StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean#L25) (StacksFrontier): “the first isomorphism”.
- [`TensorProduct.comm_tmul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.comm_tmul#doc) registered with `add_to_stacks` in [StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean#L26) (StacksFrontier): “the first isomorphism, on pure tensors”.
- [`TensorProduct.prodLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.prodLeft#doc) registered with `add_to_stacks` in [StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean#L27) (StacksFrontier): “the second isomorphism”. References: EGA III (7.2.6), “special case”.
- [`TensorProduct.prodLeft_tmul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.prodLeft_tmul#doc) registered with `add_to_stacks` in [StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean#L29) (StacksFrontier): “the second isomorphism, on pure tensors”.
- [`TensorProduct.lid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.lid#doc) registered with `add_to_stacks` in [StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean#L30) (StacksFrontier): “the third isomorphism”. References: SGA 3 VIIB (0.3.2), “special case”.
- [`TensorProduct.lid_tmul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.lid_tmul#doc) registered with `add_to_stacks` in [StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean#L31) (StacksFrontier): “the third isomorphism, on pure tensors”.
- [`TensorProduct.ext'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.ext'#doc) registered with `add_to_stacks` in [StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/CanonicalIsos.lean#L32) (StacksFrontier): “uniqueness of each of the three”.

## Tag 00CZ, a lemma

[Tag 00CZ](https://stacks.math.columbia.edu/tag/00CZ) in the Stacks Project.

**`PiTensorProduct.existsUnique_linearEquiv_of_universal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/PiTensorProduct/Universal.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/PiTensorProduct/Universal.lean#L33). The attribute's comment: “Uniqueness clause: such a `T` is unique up to unique isomorphism; the existence of `(T, g)` with the universal property is `PiTensorProduct.lift` with `PiTensorProduct.lift.unique`.”.

> **Stacks 00CZ.** The tensor product is unique up to unique isomorphism: if a module `T`
> and a multilinear map `g : Π i, s i → T` have the universal property (every multilinear map
> `f` to a module `P` factors as `f' ∘ g` for a unique linear `f'`), then there is a unique
> linear isomorphism `e : (⨂[R] i, s i) ≃ₗ[R] T` with `e ∘ tprod R = g`.

```lean
theorem existsUnique_linearEquiv_of_universal (T : Type t) [AddCommMonoid T] [Module R T]
    (g : MultilinearMap R s T)
    (hg : ∀ (P : Type (max u v w t)) [AddCommMonoid P] [Module R P] (f : MultilinearMap R s P),
      ∃! f' : T →ₗ[R] P, f'.compMultilinearMap g = f) :
    ∃! e : (⨂[R] i, s i) ≃ₗ[R] T, e.toLinearMap.compMultilinearMap (tprod R) = g
```

Declarations registered for the tag:

- [`PiTensorProduct.lift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PiTensorProduct.lift#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/PiTensorProduct/Basic.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/PiTensorProduct/Basic.lean#L8) (StacksCore).
- [`PiTensorProduct.lift.unique`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PiTensorProduct.lift.unique#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/PiTensorProduct/Basic.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/PiTensorProduct/Basic.lean#L9) (StacksCore).

## Tag 00D0, a lemma

[Tag 00D0](https://stacks.math.columbia.edu/tag/00D0) in the Stacks Project.

**`PiTensorProduct.tmulTmulLeftEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/PiTensorProduct/FinThree.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/PiTensorProduct/FinThree.lean#L102). The attribute's comment: “the map `f`; the three modules are the family `M 0`, `M 1`, `M 2` and the threefold tensor product is `PiTensorProduct` over `Fin 3`”.

> **Stacks 00D0**, the map `f`: the isomorphism `(M ⊗_R N) ⊗_R P ≅ M ⊗_R N ⊗_R P` from the
> iterated tensor product to the threefold tensor product of Stacks 00CZ, with
> `f ((x ⊗ y) ⊗ z) = x ⊗ y ⊗ z` (`tmulTmulLeftEquiv_tmul`).

```lean
noncomputable def tmulTmulLeftEquiv : ((M 0 ⊗[R] M 1) ⊗[R] M 2) ≃ₗ[R] ⨂[R] i, M i
```

**`PiTensorProduct.tmulTmulRightEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/PiTensorProduct/FinThree.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/PiTensorProduct/FinThree.lean#L135). The attribute's comment: “the map `g`; the three modules are the family `M 0`, `M 1`, `M 2` and the threefold tensor product is `PiTensorProduct` over `Fin 3`”.

> **Stacks 00D0**, the map `g`: the isomorphism `M ⊗_R N ⊗_R P ≅ M ⊗_R (N ⊗_R P)` from the
> threefold tensor product of Stacks 00CZ to the iterated tensor product, with
> `g (x ⊗ y ⊗ z) = x ⊗ (y ⊗ z)` (`tmulTmulRightEquiv_tprod`).

```lean
noncomputable def tmulTmulRightEquiv : (⨂[R] i, M i) ≃ₗ[R] M 0 ⊗[R] (M 1 ⊗[R] M 2)
```

**`PiTensorProduct.tmulTmulLeftEquiv_trans_tmulTmulRightEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/PiTensorProduct/FinThree.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/PiTensorProduct/FinThree.lean#L158). The attribute's comment: “the composite `g ∘ f` is `TensorProduct.assoc`”.

> **Stacks 00D0**, the composite: `g ∘ f` is the associator
> `TensorProduct.assoc : (M ⊗_R N) ⊗_R P ≅ M ⊗_R (N ⊗_R P)`.

```lean
theorem tmulTmulLeftEquiv_trans_tmulTmulRightEquiv :
    tmulTmulLeftEquiv R M ≪≫ₗ tmulTmulRightEquiv R M = TensorProduct.assoc R (M 0) (M 1) (M 2)
```

Declarations registered for the tag:

- [`TensorProduct.assoc`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.assoc#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/Associator.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Associator.lean#L9) (StacksCore).
- [`TensorProduct.assoc_tmul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.assoc_tmul#doc) registered with `add_to_stacks` in [StacksFrontier/LinearAlgebra/PiTensorProduct/FinThree.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/PiTensorProduct/FinThree.lean#L29) (StacksFrontier): “the composite g ∘ f, on pure tensors”.

## Tag 00D1, a definition

[Tag 00D1](https://stacks.math.columbia.edu/tag/00D1) in the Stacks Project.

**`DistribMulAction.commute_toAddMonoidEnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Bimodule.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Bimodule.lean#L95). The attribute's comment: “The source's condition, that multiplication by `a` and multiplication by `b` commute, at the level of the multiplication operators: an equation in `AddMonoid.End N`. The condition as a class on the two actions is `SMulCommClass`, tagged below.”.

> **Stacks 00D1.** In an `(A, B)`-bimodule multiplication by `a : A` and multiplication by
> `b : B` commute, as additive endomorphisms of `N`: this is the source's own phrasing of the
> bimodule condition, an equation in `AddMonoid.End N`.
>
> The condition itself is `SMulCommClass A B N`, whose field `smul_comm` is the pointwise identity
> `a • b • n = b • a • n`; commuting of the operators is the form consumed by
> `Algebra.TensorProduct.liftEquiv`, hence by `TensorProduct.Algebra.module`.

```lean
public theorem DistribMulAction.commute_toAddMonoidEnd {A B N : Type*} [Monoid A] [Monoid B]
    [AddMonoid N] [DistribMulAction A N] [DistribMulAction B N] [SMulCommClass A B N] (a : A)
    (b : B) :
    Commute (DistribMulAction.toAddMonoidEnd A N a) (DistribMulAction.toAddMonoidEnd B N b)
```

Declarations registered for the tag:

- [`SMulCommClass`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SMulCommClass#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/Bimodule.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Bimodule.lean#L104) (StacksFrontier): “An `(A, B)`-bimodule is a type with `[Module A N] [Module B N] [SMulCommClass A B N]`: the source's data is the two module structures, and its one condition, that the actions commute, is this class, `smul_comm` being `a • b • n = b • a • n`, the source's `b (a n) = a (b n)` read from the other side. The class asks only for two `SMul`s, so this covers semirings acting on an additive commutative monoid as well as the source's rings acting on an abelian group. Writing the `B`-action on the right is the source's notation, not a further condition; the genuine right-action form is this class at `Bᵐᵒᵖ`, the bimodule set-up of `Mathlib/Algebra/Module/Bimodule.lean`.”.

## Tag 00D2, a lemma

[Tag 00D2](https://stacks.math.columbia.edu/tag/00D2) in the Stacks Project.

**`TensorProduct.smulCommClass_bimoduleAssoc_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/BimoduleAssoc.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/BimoduleAssoc.lean#L103). The attribute's comment: “The `(A, B)`-bimodule structure on `(M ⊗_A N) ⊗_B P`: `A` acts through `M`, `B` through `N` (`TensorProduct.rightModule`), and the two actions commute.”.

> **Stacks 00D2**, the bimodule structure on `(M ⊗_A N) ⊗_B P`: here `B` acts on `M ⊗_A N`
> through `N`, and `A` and `B` act on the outer tensor product through its left factor.

```lean
theorem smulCommClass_bimoduleAssoc_left : SMulCommClass A B ((M ⊗[A] N) ⊗[B] P)
```

**`TensorProduct.smulCommClass_bimoduleAssoc_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/BimoduleAssoc.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/BimoduleAssoc.lean#L111). The attribute's comment: “The `(A, B)`-bimodule structure on `M ⊗_A (N ⊗_B P)`: `A` acts through `M`, `B` through `N` (`TensorProduct.rightModule`), and the two actions commute.”.

> **Stacks 00D2**, the bimodule structure on `M ⊗_A (N ⊗_B P)`: here `A` and `B` act on
> `N ⊗_B P` through `N`, `A` acts on the outer tensor product through `M` and `B` through
> `N ⊗_B P`.

```lean
theorem smulCommClass_bimoduleAssoc_right : SMulCommClass A B (M ⊗[A] (N ⊗[B] P))
```

**`TensorProduct.bimoduleAssoc`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/BimoduleAssoc.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/BimoduleAssoc.lean#L181). The attribute's comment: “The isomorphism `(M ⊗_A N) ⊗_B P ≅ M ⊗_A (N ⊗_B P)` for an `(A, B)`-bimodule `N`, with no ring map between `A` and `B`, as an `A`-linear isomorphism; the same map as a `B`-linear isomorphism is `TensorProduct.bimoduleAssocRight`.”.

> **Stacks 00D2**: for an `A`-module `M`, a `B`-module `P` and an `(A, B)`-bimodule `N`,
> `(M ⊗_A N) ⊗_B P ≅ M ⊗_A (N ⊗_B P)` via `(m ⊗ n) ⊗ p ↦ m ⊗ (n ⊗ p)`, an `A`-linear isomorphism.
> The same map is `B`-linear: `TensorProduct.bimoduleAssocRight`.

```lean
noncomputable def bimoduleAssoc : ((M ⊗[A] N) ⊗[B] P) ≃ₗ[A] M ⊗[A] (N ⊗[B] P)
```

**`TensorProduct.bimoduleAssocRight`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/BimoduleAssoc.lean, line 232](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/BimoduleAssoc.lean#L232). The attribute's comment: “The isomorphism `(M ⊗_A N) ⊗_B P ≅ M ⊗_A (N ⊗_B P)` as a `B`-linear isomorphism; its underlying additive equivalence is that of the `A`-linear `TensorProduct.bimoduleAssoc`.”.

> **Stacks 00D2**: `bimoduleAssoc` as a `B`-linear isomorphism; its underlying map is that of
> the `A`-linear `bimoduleAssoc` (`bimoduleAssocRight_toAddEquiv`), so the two triple tensor
> products are isomorphic as `A`-modules and as `B`-modules via the same mapping.

```lean
noncomputable def bimoduleAssocRight : ((M ⊗[A] N) ⊗[B] P) ≃ₗ[B] M ⊗[A] (N ⊗[B] P)
```

Declarations registered for the tag:

- [`TensorProduct.AlgebraTensorModule.assoc`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.AlgebraTensorModule.assoc#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/Tower.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Tower.lean#L11) (StacksCore).

## Tag 00DE, a lemma

[Tag 00DE](https://stacks.math.columbia.edu/tag/00DE) in the Stacks Project.

Declarations registered for the tag:

- [`TensorProduct.lift.equiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.lift.equiv#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/Associator.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/Associator.lean#L10) (StacksCore).

## Tag 00DD, a lemma

[Tag 00DD](https://stacks.math.columbia.edu/tag/00DD) in the Stacks Project.

Declarations registered for the tag:

- [`TensorProduct.directLimitLeft`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TensorProduct.directLimitLeft#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/DirectLimit.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/DirectLimit.lean#L8) (StacksCore). References: EGA 0 (4.3.2), “special case”; EGA III (6.5.6), “special case”; SGA 4 V (8.2.4), “special case”; SGA 5 V (1.2.1), “special case”.

## Tag 00DF, a lemma

[Tag 00DF](https://stacks.math.columbia.edu/tag/00DF) in the Stacks Project.

Declarations registered for the tag:

- [`rTensor_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=rTensor_exact#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/RightExactness.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/RightExactness.lean#L8) (StacksCore). References: EGA 0 (4.1.5), “special case”; EGA III (7.2.6), “partial”; SGA 3 VIIB (0.3.2), “Corollary, special case”.
- [`LinearMap.rTensor_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LinearMap.rTensor_surjective#doc) registered with `add_to_stacks` in [StacksCore/LinearAlgebra/TensorProduct/RightExactness.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/LinearAlgebra/TensorProduct/RightExactness.lean#L9) (StacksCore).

## Tag 00DH, a remark

[Tag 00DH](https://stacks.math.columbia.edu/tag/00DH) in the Stacks Project.

**`tensorRight_not_preserve_exactness`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Counterexamples/TensorProduct.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/Counterexamples/TensorProduct.lean#L25).

```lean
theorem tensorRight_not_preserve_exactness :
    ¬ ∀ (R : Type u) (_ : CommRing R) (M₁ : Type v)
      (M₂ M₃ : Type v') (N : Type w)
      (_ : AddCommGroup M₁) (_ : Module R M₁)
      (_ : AddCommGroup M₂) (_ : Module R M₂)
      (_ : AddCommGroup M₃) (_ : Module R M₃)
      (_ : AddCommGroup N) (_ : Module R N)
      (f : M₁ →ₗ[R] M₂) (g : M₂ →ₗ[R] M₃),
      Function.Exact f g →
      Function.Exact (f.rTensor N) (g.rTensor N)
```

## Tag 00DI, an example

[Tag 00DI](https://stacks.math.columbia.edu/tag/00DI) in the Stacks Project.

**`TensorProduct.not_injective_rTensor_zmod_two_lsmul_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/TensorProduct/NotLeftExact.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/TensorProduct/NotLeftExact.lean#L84).

> **Stacks 00DI**.
> Multiplication by `2` is an injective map of `ℤ`-modules `ℤ → ℤ`, but the induced map
> `ℤ ⊗[ℤ] ℤ/2 → ℤ ⊗[ℤ] ℤ/2` is the zero map and hence not injective, `ℤ ⊗[ℤ] ℤ/2` being nonzero.
> So tensoring does not preserve injectivity.

```lean
public theorem TensorProduct.not_injective_rTensor_zmod_two_lsmul_two :
    Function.Injective (LinearMap.lsmul ℤ ℤ (2 : ℤ)) ∧
      (LinearMap.lsmul ℤ ℤ (2 : ℤ)).rTensor (ZMod 2) = 0 ∧
      ¬ Function.Injective ((LinearMap.lsmul ℤ ℤ (2 : ℤ)).rTensor (ZMod 2))
```

## Tag 00DJ, a remark

[Tag 00DJ](https://stacks.math.columbia.edu/tag/00DJ) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Flat/Basic.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Flat/Basic.lean#L8) (StacksCore). References: EGA 0 (10.3.1.2); EGA 0 (10.3.1.3); EGA 0 (6.1.1); EGA IV (6.1.3); EGA IV (2.1.12); SGA 1 IV (4.3); SGA 3 VIIB (2.2.1), “special case”; SGA 4 V (1.1), “special case”; SGA 4 XVII (5.5.6.3); SGA 4½ Etat 0 (6.2), “special case”; SGA 5 IIIB (5.10); SGA 5 IIIB (6.1), “partial”; SGA 6 X (7.18.1).

## Tag 05BS, a lemma

[Tag 05BS](https://stacks.math.columbia.edu/tag/05BS) in the Stacks Project.

**`Module.FinitePresentation.tensorProduct`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/TensorProduct/Finite.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/TensorProduct/Finite.lean#L38). The attribute's comment: “part 2”.

> **Stacks 05BS (2).** The tensor product of two finitely presented modules is finitely
> presented.

```lean
instance Module.FinitePresentation.tensorProduct
    [Module.FinitePresentation R M] [Module.FinitePresentation R N] :
    Module.FinitePresentation R (M ⊗[R] N)
```

Declarations registered for the tag:

- [`Module.Finite.tensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Finite.tensorProduct#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/TensorProduct/Finite.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/TensorProduct/Finite.lean#L31) (StacksCore): “part 1”. References: EGA 0 (5.2.1), “special case”.

## Tag 00DK, a lemma

[Tag 00DK](https://stacks.math.columbia.edu/tag/00DK) in the Stacks Project.

Declarations registered for the tag:

- [`LocalizedModule.equivTensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocalizedModule.equivTensorProduct#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Localization/BaseChange.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/BaseChange.lean#L24) (StacksCore). References: EGA 0 (1.2.5); EGA 0 (1.5.4), “partial”; EGA 0 (6.3.1); EGA 0 (6.3.3), “partial”.

## Tag 00DL, a lemma

[Tag 00DL](https://stacks.math.columbia.edu/tag/00DL) in the Stacks Project.

**`IsLocalization.tensorLocalizeEquivTensor`**, a def in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Localization/BaseChange.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/RingTheory/Localization/BaseChange.lean#L62). References: EGA 0 (1.3.4), “more general”.

> **Stacks 00DL.** Localization commutes with tensor product: for any localization `P` of
> `M ⊗[R] N` at `S`, there is a canonical `Rₛ`-linear isomorphism `M' ⊗[Rₛ] N' ≃ P`. Taking
> `Rₛ = S⁻¹R`, `M' = S⁻¹M`, `N' = S⁻¹N` and `P = S⁻¹(M ⊗_R N)` gives the isomorphism
> `S⁻¹M ⊗_{S⁻¹R} S⁻¹N ≅ S⁻¹(M ⊗_R N)` of the Stacks project.

```lean
noncomputable def IsLocalization.tensorLocalizeEquivTensor
    [IsLocalizedModule S f] [IsLocalizedModule S g] [IsLocalizedModule S h] :
    M' ⊗[Rₛ] N' ≃ₗ[Rₛ] P
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.12, Tag 00CV](https://stacks.math.columbia.edu/tag/00CV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

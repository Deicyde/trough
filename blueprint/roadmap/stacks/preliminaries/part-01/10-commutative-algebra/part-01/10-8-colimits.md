---
declaration: section
origin: cited
lean: DirectedSystem, Module.DirectLimit, DirectLimit.Module.of, DirectLimit.Module.lift, ModuleCat.directLimitIsColimit, DirectLimit.exists_eq_zero, ModuleCat.ker_hom_comp_inl_and_ker_hom_inl_of_isPushout, Module.IsSystemHom
statement: formalized
proof: formalized
---

# 10.8 Colimits

Section 10.8 of the Stacks Project, [Tag 07N7](https://stacks.math.columbia.edu/tag/07N7). 10 tags here are carried by 6 declarations of the repository (2 in StacksCore and 4 in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00D4, a definition

[Tag 00D4](https://stacks.math.columbia.edu/tag/00D4) in the Stacks Project.

Declarations registered for the tag:

- [`DirectedSystem`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DirectedSystem#doc) registered with `add_to_stacks` in [StacksCore/Order/DirectedInverseSystem.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Order/DirectedInverseSystem.lean#L10) (StacksCore).

## Tag 00D5, a lemma

[Tag 00D5](https://stacks.math.columbia.edu/tag/00D5) in the Stacks Project.

Declarations registered for the tag:

- [`Module.DirectLimit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.DirectLimit#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Colimit/Module.lean, line 9](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Colimit/Module.lean#L9) (StacksCore). References: EGA 0 (6.2.3), “special case”.
- [`DirectLimit.Module.of`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DirectLimit.Module.of#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Colimit/Module.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Colimit/Module.lean#L10) (StacksCore).
- [`DirectLimit.Module.lift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DirectLimit.Module.lift#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Colimit/Module.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Colimit/Module.lean#L11) (StacksCore).

## Tag 00D6, a lemma

[Tag 00D6](https://stacks.math.columbia.edu/tag/00D6) in the Stacks Project.

Declarations registered for the tag:

- [`ModuleCat.directLimitIsColimit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ModuleCat.directLimitIsColimit#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Category/ModuleCat/Limits.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Category/ModuleCat/Limits.lean#L8) (StacksCore).

## Tag 00D7, a lemma

[Tag 00D7](https://stacks.math.columbia.edu/tag/00D7) in the Stacks Project.

Declarations registered for the tag:

- [`DirectLimit.exists_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=DirectLimit.exists_eq_zero#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Colimit/Module.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Colimit/Module.lean#L12) (StacksCore).

## Tag 00D8, an example

[Tag 00D8](https://stacks.math.columbia.edu/tag/00D8) in the Stacks Project.

**`ModuleCat.ker_hom_comp_inl_and_ker_hom_inl_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Colimits.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Colimits.lean#L112). The attribute's comment: “The poset `{a < b, a < c}` is the span shape, so the colimit of a system over it is a pushout in `ModuleCat R`, taken here abstractly rather than through the model `Coker(μ_ab ⊕ -μ_ac)`; that the pushout is that cokernel is Mathlib's `CategoryTheory.IsPushout.isColimitCokernelCofork`. The mirror `Ker(inr) = μ_ac(Ker(μ_ab))` is this statement applied to `h.flip`.”.

> Let `R` be a ring and let `M = colim M_i` be the colimit of a system of
> `R`-modules over the poset `{a < b, a < c}`, that is, the pushout of a span
> `M_b ← M_a → M_c` of `R`-modules, with canonical maps `inl : M_b → M` and `inr : M_c → M`. Then the
> kernel of the canonical map `M_a → M` is `Ker(μ_ab) + Ker(μ_ac)`, and the kernel of `inl` is the
> image of `Ker(μ_ac)` under `μ_ab`.

```lean
theorem ModuleCat.ker_hom_comp_inl_and_ker_hom_inl_of_isPushout {R : Type u} [Ring R]
    {Ma Mb Mc M : ModuleCat.{v} R} {μab : Ma ⟶ Mb} {μac : Ma ⟶ Mc} {inl : Mb ⟶ M} {inr : Mc ⟶ M}
    (h : IsPushout μab μac inl inr) :
    LinearMap.ker (μab ≫ inl).hom = LinearMap.ker μab.hom ⊔ LinearMap.ker μac.hom ∧
      LinearMap.ker inl.hom = Submodule.map μab.hom (LinearMap.ker μac.hom)
```

## Tag 00D9, a definition

[Tag 00D9](https://stacks.math.columbia.edu/tag/00D9) in the Stacks Project.

**`Module.IsSystemHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs/Colimits.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs/Colimits.lean#L75). The attribute's comment: “Stated as a `Prop`-valued predicate on the family `φ`, in the unbundled language of `Module.DirectLimit`, so that `Module.DirectLimit.map φ h` is the induced map on colimits of Lemma 00DA. The axioms of a system (`DirectedSystem`) are not assumed, the commuting squares not referring to them, and `R` is only a semiring acting on additive commutative monoids.”.

> **Stacks 00D9.** Let `(M i, μ i j)` and `(N i, ν i j)` be systems of `R`-modules over the same
> preordered set `ι`. A family of `R`-linear maps `φ i : M i →ₗ[R] N i` is a *homomorphism of
> systems* from `(M, μ)` to `(N, ν)` when every transition square commutes, that is, when
> `φ j ∘ₗ μ i j = ν i j ∘ₗ φ i` for all `i ≤ j`; equivalently, when `φ` is a natural transformation
> between the associated diagrams `ι ⥤ ModuleCat R`. The axioms making `μ` and `ν` systems are not
> needed to state the condition and are not assumed.

```lean
def IsSystemHom {R : Type*} [Semiring R] {ι : Type*} [Preorder ι]
    {M : ι → Type*} [∀ i, AddCommMonoid (M i)] [∀ i, Module R (M i)]
    (μ : (i j : ι) → i ≤ j → M i →ₗ[R] M j)
    {N : ι → Type*} [∀ i, AddCommMonoid (N i)] [∀ i, Module R (N i)]
    (ν : (i j : ι) → i ≤ j → N i →ₗ[R] N j)
    (φ : (i : ι) → M i →ₗ[R] N i) : Prop
```

Declarations registered for the tag:

- [`Module.DirectLimit.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.DirectLimit.map#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Colimit/Module.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Colimit/Module.lean#L13) (StacksCore).

## Tag 00DA, a lemma

[Tag 00DA](https://stacks.math.columbia.edu/tag/00DA) in the Stacks Project.

Declarations registered for the tag:

- [`Module.DirectLimit.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.DirectLimit.map#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Colimit/Module.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Colimit/Module.lean#L14) (StacksCore).

## Tag 00DB, a lemma

[Tag 00DB](https://stacks.math.columbia.edu/tag/00DB) in the Stacks Project.

**`Module.DirectLimit.comp_eq_zero`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Colimit/Module.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Colimit/Module.lean#L28). The attribute's comment: “part 1”.

```lean
public lemma Module.DirectLimit.comp_eq_zero :
    Module.DirectLimit.map g' hg' ∘ₗ Module.DirectLimit.map g hg = 0
```

**`Module.DirectLimit.homologyColimitEquiv`**, a def in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Colimit/Module.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Colimit/Module.lean#L127). The attribute's comment: “part 2”.

> Homology intertwines with direct limits.

```lean
public def Module.DirectLimit.homologyColimitEquiv
    [Nonempty ι] [IsDirectedOrder ι]
    [DirectedSystem M fun i j h ↦ ⇑(f' i j h)]
    [DirectedSystem N fun x1 x2 x3 ↦ ⇑(l x1 x2 x3)] :
    Module.DirectLimit (hObj g g') (hMap g hg g' hg') ≃ₗ[R] homologyLimit g hg g' hg'
```

## Tag 00DC, an example

[Tag 00DC](https://stacks.math.columbia.edu/tag/00DC) in the Stacks Project.

**`ModuleCat.not_injective_hom_of_isColimit_binaryCofan_of_isPushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Colimits.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Colimits.lean#L149). The attribute's comment: “The poset `{a < b, a < c}` is the span shape, so the colimit of a system over it is a pushout in `ModuleCat R` and the colimit of the sub-system with apex the zero module is the coproduct `B ⊔ C`; the morphism of systems `(0 → A, 𝟙 B, 𝟙 C)` is injective on each object, and `ψ` is pinned by the two commuting squares of `Stacks 00DA`. Stated for an arbitrary nonzero span over an arbitrary ring instead of the source's `(0, ℤ, ℤ, 0, 0) → (ℤ, ℤ, ℤ, 1, 1)`.”.

> Taking colimits is not exact in general: let `R` be a ring, let `M` be the
> colimit of a system `(A, B, C, μ_ab, μ_ac)` of `R`-modules over the poset `{a < b, a < c}`, that
> is, the pushout of the span `B ← A → C`, and let `L` be the colimit `B ⊔ C` of the sub-system
> `(0, B, C, 0, 0)`. If one of `μ_ab`, `μ_ac` is nonzero, then the induced map of colimits
> `ψ : L → M` is not injective, even though the morphism of systems `(0 → A, 𝟙 B, 𝟙 C)` is
> injective on each object.

```lean
theorem ModuleCat.not_injective_hom_of_isColimit_binaryCofan_of_isPushout {R : Type u}
    [Ring R] {A B C L M : ModuleCat.{v} R} {μab : A ⟶ B} {μac : A ⟶ C} {l : B ⟶ L} {r : C ⟶ L}
    {inl : B ⟶ M} {inr : C ⟶ M} {ψ : L ⟶ M} (hL : IsColimit (BinaryCofan.mk l r))
    (hM : IsPushout μab μac inl inr) (hl : l ≫ ψ = inl) (hr : r ≫ ψ = inr)
    (hμ : μab ≠ 0 ∨ μac ≠ 0) :
    ¬ Function.Injective ψ.hom
```

## Tag 04B0, a lemma

[Tag 04B0](https://stacks.math.columbia.edu/tag/04B0) in the Stacks Project.

**`CategoryTheory.hasExactColimitsOfShape_of_isPseudofiltered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Colimits.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Colimits.lean#L290). The attribute's comment: “Stated as `HasExactColimitsOfShape J C`, i.e. `colim : (J ⥤ C) ⥤ C` preserves finite limits, which for a left adjoint is exactness and is the form of `Stacks 00DB` the source asks for. The assumptions of `Stacks 002X` are spelled out because Mathlib has no predicate for a pseudofiltered category. Stated for an arbitrary abelian category with colimits of size `w` whose filtered colimits are exact, instead of the source's abelian groups, since the source's proof uses only that; AB4 is derived from AB5 rather than assumed.”.

> Let `J` be an index category satisfying the assumptions of Stacks 002X: every span
> `y ← x → z` is completed by some commutative square, and every pair of parallel morphisms
> `a b : x ⟶ y` is coequalized by some `c : y ⟶ z`. Then taking colimits of diagrams over `J` in an
> abelian category with exact filtered colimits is exact.

```lean
theorem CategoryTheory.hasExactColimitsOfShape_of_isPseudofiltered {C : Type u}
    [Category.{v} C] [Abelian C] [Limits.HasColimitsOfSize.{w, w} C] [AB5OfSize.{w, w} C]
    {J : Type w} [Category.{w} J]
    (hspan : ∀ ⦃x y z : J⦄ (a : x ⟶ y) (b : x ⟶ z), ∃ (t : J) (c : y ⟶ t) (d : z ⟶ t),
      a ≫ c = b ≫ d)
    (hpar : ∀ ⦃x y : J⦄ (a b : x ⟶ y), ∃ (z : J) (c : y ⟶ z), a ≫ c = b ≫ c) :
    HasExactColimitsOfShape J C
```

Declarations registered for the tag:

- [`instPreservesHomologyFunctorAddCommGrpCatColim`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instPreservesHomologyFunctorAddCommGrpCatColim#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Category/Grp/AB.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Category/Grp/AB.lean#L8) (StacksCore). References: EGA 0 (11.2.4), “special case”; SGA 4 XVII (5.5.6.3), “A = ℤ”.
- [`instAB5AddCommGrpCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instAB5AddCommGrpCat#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Category/Grp/AB.lean, line 9](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Category/Grp/AB.lean#L9) (StacksCore). References: SGA 4 I (2.10), “special case”; SGA 6 II (3.1), “special case”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.8, Tag 07N7](https://stacks.math.columbia.edu/tag/07N7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

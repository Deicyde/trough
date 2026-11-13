---
declaration: section
origin: cited
lean: Module.support_eq_empty_iff, Ideal.torsionOf, Module.annihilator, ann_extension_eq_ann_baseChange_elem, ann_extension_eq_ann_baseChange_module, Module.isClosed_support, IsBaseChange.support_eq_preimage_comap, isClosed_support_and_isCompact_compl_support
statement: formalized
proof: formalized
---

# 10.40 Supports and annihilators

Section 10.40 of the Stacks Project, [Tag 080S](https://stacks.math.columbia.edu/tag/080S). 7 tags here are carried by 5 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0585, a lemma

[Tag 0585](https://stacks.math.columbia.edu/tag/0585) in the Stacks Project.

Declarations registered for the tag:

- [`Module.support_eq_empty_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.support_eq_empty_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Support/Basic.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Support/Basic.lean#L182) (StacksFrontier). References: EGA 0 (1.7.1), “M = 0 ⇔ Supp M = ∅”.

## Tag 07T7, a definition

[Tag 07T7](https://stacks.math.columbia.edu/tag/07T7) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.torsionOf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.torsionOf#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L161) (StacksFrontier): “(1) Ann(m) = \{f | fm = 0}”.
- [`Module.annihilator`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.annihilator#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L162) (StacksFrontier): “(2) Ann(M) = \{f | fm = 0 for all m}”. References: EGA 0 (5.3.7), “special case”; EGA IV (5.6.11); EGA IV (5.6.11.1); SGA 2 III (1.1).

## Tag 07T8, a lemma

[Tag 07T8](https://stacks.math.columbia.edu/tag/07T8) in the Stacks Project.

**`ann_extension_eq_ann_baseChange_elem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/Annihilator/FlatBaseChange.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/Annihilator/FlatBaseChange.lean#L78).

> For a flat ring map `φ : R → S` and any `m` in an `R`-module `M`, the extension of the
> annihilator `Ann_R(m)` to `S` equals the `S`-annihilator of the base-changed element
> `1 ⊗ m ∈ S ⊗_R M`: `Ann_R(m) S = Ann_S(1 ⊗ m)`.

```lean
theorem ann_extension_eq_ann_baseChange_elem [Module.Flat R S] (m : M) :
    Ideal.map (algebraMap R S) (Ideal.torsionOf R M m)
      = Ideal.torsionOf S (S ⊗[R] M) ((1 : S) ⊗ₜ[R] m)
```

**`ann_extension_eq_ann_baseChange_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/Annihilator/FlatBaseChange.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/Annihilator/FlatBaseChange.lean#L301). References: EGA IV (2.1.11), “affine case”.

> For a flat ring map `φ : R → S` and a finite `R`-module `M`, the extension of the
> annihilator `Ann_R(M)` to `S` equals the `S`-annihilator of the base change `S ⊗_R M`:
> `Ann_R(M) S = Ann_S(S ⊗_R M)`.

```lean
theorem ann_extension_eq_ann_baseChange_module [Module.Flat R S] [Module.Finite R M] :
    Ideal.map (algebraMap R S) (Module.annihilator R M)
      = Module.annihilator S (S ⊗[R] M)
```

## Tag 00L2, a lemma

[Tag 00L2](https://stacks.math.columbia.edu/tag/00L2) in the Stacks Project.

Declarations registered for the tag:

- [`Module.isClosed_support`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.isClosed_support#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Support/Basic.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Support/Basic.lean#L168) (StacksFrontier): “the support of a finite module is closed”. References: EGA 0 (16.1.7), “partial”; EGA 0 (5.2.2), “special case”; EGA I (4.1.2), “affine case”; EGA IV (5.1.12), “special case”; EGA IV (8.9.1), “closedness of Supp(F)”; SGA 3 VIA (2.1.3), “special case”.

## Tag 0BUR, a lemma

[Tag 0BUR](https://stacks.math.columbia.edu/tag/0BUR) in the Stacks Project.

**`IsBaseChange.support_eq_preimage_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Support/Basic.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Support/Basic.lean#L137).

> **Stacks 0BUR**. Let `R → S` be a ring map, let `M` be a finite `R`-module and let
> `f : M →ₗ[R] N` exhibit the `S`-module `N` as the base change `S ⊗_R M`. Then `Supp_S(N)` is the
> inverse image of `Supp_R(M)` under the map `Spec(S) → Spec(R)` induced by `R → S`.

```lean
theorem support_eq_preimage_comap {R S M N : Type*} [CommRing R] [CommRing S]
    [Algebra R S] [AddCommGroup M] [Module R M] [Module.Finite R M] [AddCommGroup N]
    [Module R N] [Module S N] [IsScalarTower R S N] {f : M →ₗ[R] N} (h : IsBaseChange S f) :
    Module.support S N = PrimeSpectrum.comap (algebraMap R S) ⁻¹' Module.support R M
```

## Tag 051B, a lemma

[Tag 051B](https://stacks.math.columbia.edu/tag/051B) in the Stacks Project.

**`isClosed_support_and_isCompact_compl_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Fitting/Basic.lean, line 715](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Fitting/Basic.lean#L715). The attribute's comment: “Supp(M) = V(Fit\_0(M)) with Fit\_0(M) finitely generated, as in the source proof”.

> **Stacks 051B.** The support of a finitely presented module is a closed subset of `Spec R`
> whose complement is quasi-compact. The support is the zero locus of the zeroth Fitting ideal,
> the ideal of maximal minors of a presentation matrix, and that ideal is finitely generated for
> a finitely presented module.

```lean
theorem isClosed_support_and_isCompact_compl_support {R : Type*} [CommRing R]
    (M : Type*) [AddCommGroup M] [Module R M] [Module.FinitePresentation R M] :
    IsClosed (Module.support R M) ∧ IsCompact (Module.support R M)ᶜ
```

## Tag 00L3, a lemma

[Tag 00L3](https://stacks.math.columbia.edu/tag/00L3) in the Stacks Project.

**`support_submodule_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Support/Basic.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Support/Basic.lean#L192). The attribute's comment: “(2)”. References: EGA 0 (1.7.2), “partial”.

> The support of a submodule is contained in the support of the ambient module.

```lean
theorem support_submodule_subset
    {R : Type*} {M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (N : Submodule R M) :
    Module.support R N ⊆ Module.support R M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.40, Tag 080S](https://stacks.math.columbia.edu/tag/080S)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

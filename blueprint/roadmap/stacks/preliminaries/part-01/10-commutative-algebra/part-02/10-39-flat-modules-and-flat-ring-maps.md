---
declaration: section
origin: cited
lean: Module.Flat, Module.Flat.iff_lTensor_exact, Module.FaithfullyFlat, Module.FaithfullyFlat.iff_exact_iff_lTensor_exact, RingHom.Flat, ideal_smul_top_inf, colimit_flat_of_flat, RingHom.Flat.comp
statement: formalized
proof: formalized
---

# 10.39 Flat modules and flat ring maps

Section 10.39 of the Stacks Project, [Tag 00H9](https://stacks.math.columbia.edu/tag/00H9). 18 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 19 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00HB, a definition

[Tag 00HB](https://stacks.math.columbia.edu/tag/00HB) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Defs.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Defs.lean#L22) (StacksFrontier): “(1)”. References: EGA 0 (10.3.1.2); EGA 0 (10.3.1.3); EGA 0 (6.1.1); EGA IV (6.1.3); EGA IV (2.1.12); SGA 1 IV (4.3); SGA 3 VIIB (2.2.1), “special case”; SGA 4 V (1.1), “special case”; SGA 4 XVII (5.5.6.3); SGA 4½ Etat 0 (6.2), “special case”; SGA 5 IIIB (5.10); SGA 5 IIIB (6.1), “partial”; SGA 6 X (7.18.1).
- [`Module.Flat.iff_lTensor_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.iff_lTensor_exact#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Defs.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Defs.lean#L23) (StacksFrontier): “(1), as the exactness condition the tag states”. References: EGA 0 (6.1.1); EGA 0 (6.4.1), “a)”; EGA III (6.1.1), “special case”; EGA IV (2.2.7), “partial”; SGA 4 V (1.1), “special case”; SGA 4 V (1.7.2), “(i) ⇔ (ii), special case”; SGA 4½ Etat 0 (6.2), “special case”; SGA 6 0 (2.9), “affine case”; SGA 7 VII (3.7.6), “partial”.
- [`Module.FaithfullyFlat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FaithfullyFlat#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Defs.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Defs.lean#L34) (StacksFrontier): “(2)”. References: EGA 0 (22.4.8); EGA 0 (6.4.1); EGA 0 (6.6.1); EGA IV (2.2.4), “special case”; SGA 1 IV (2.1).
- [`Module.FaithfullyFlat.iff_exact_iff_lTensor_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FaithfullyFlat.iff_exact_iff_lTensor_exact#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Defs.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Defs.lean#L40) (StacksFrontier): “(2), as the exactness condition the tag states”. References: EGA 0 (6.6.1), “more general”; EGA IV (2.2.7), “special case”; EGA 0 (6.4.1), “(a) <=> (d)”; SGA 1 IV (2.1); SGA 1 IV (2.6), “(i)⇒(iv)”; SGA 4½ Arcata (1.4.2), “Clause (i), special case”.
- [`RingHom.Flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.Flat#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Defs.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Defs.lean#L49) (StacksFrontier): “(3)”. References: SGA 6 I (3.7), “special case”.

## Tag 0BBY, a lemma

[Tag 0BBY](https://stacks.math.columbia.edu/tag/0BBY) in the Stacks Project.

**`ideal_smul_top_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ShortExact.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ShortExact.lean#L208). References: EGA 0 (6.1.3), “second formula”.

> Stacks Tag 0BBY: for a flat module `M`, `IM ∩ JM = (I ∩ J) M`.

```lean
theorem ideal_smul_top_inf (R : Type*) [CommRing R] (I J : Ideal R)
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Flat R M] :
    (I • (⊤ : Submodule R M)) ⊓ (J • (⊤ : Submodule R M))
      = (I ⊓ J) • (⊤ : Submodule R M)
```

## Tag 05UT, a lemma

[Tag 05UT](https://stacks.math.columbia.edu/tag/05UT) in the Stacks Project.

**`colimit_flat_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/DirectLimit.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/DirectLimit.lean#L757). References: EGA 0 (6.1.2); EGA 0 (6.2.3), “constant ring system”; EGA 0 (6.3.4), “partial”; SGA 3 V (4.1.2), “partial”; SGA 4 V (1.2), “special case”; SGA 4 VI (8.6.4), “special case”; SGA 4 XVII (5.5.1.2), “partial”; SGA 4 XVII (5.5.6.3), “partial”.

> Stacks 05UT: the direct limit (colimit) of a directed system of flat
> $R$-modules is flat.

```lean
theorem colimit_flat_of_flat
    {R : Type*} [CommRing R]
    {ι : Type*} [Preorder ι] [IsDirected ι (· ≤ ·)] [Nonempty ι] [DecidableEq ι]
    (G : ι → Type*) [(i : ι) → AddCommGroup (G i)] [(i : ι) → Module R (G i)]
    (f : (i j : ι) → i ≤ j → G i →ₗ[R] G j) [DirectedSystem G (fun i j h => f i j h)]
    [∀ i, Module.Flat R (G i)] :
    Module.Flat R (Module.DirectLimit G f)
```

## Tag 00HC, a lemma

[Tag 00HC](https://stacks.math.columbia.edu/tag/00HC) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.Flat.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.Flat.comp#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Basic.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Basic.lean#L54) (StacksFrontier): “a composition of flat ring maps is flat”. References: EGA 0 (6.7.5), “Affine schemes”; EGA IV (11.3.10.2), “1°, special case”; EGA IV (2.1.6), “special case”; EGA IV (7.3.5), “special case”; EGA 0 (6.6.4), “flat maps compose”; SGA 3 VIIB (1.3.3), “(i), special case”; SGA 6 III (3.4), “special case”.
- [`RingHom.FaithfullyFlat.stableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.FaithfullyFlat.stableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Basic.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Basic.lean#L62) (StacksFrontier): “a composition of faithfully flat ring maps is faithfully flat”. References: EGA IV (2.2.13), “(iii)”; EGA 0 (6.6.4), “ff maps compose”.
- [`Module.Flat.trans`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.trans#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Basic.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Basic.lean#L66) (StacksFrontier): “a flat module over a flat algebra is flat over the base”. References: EGA 0 (10.2.5), “(a)”; EGA 0 (6.2.1), “more general”; EGA 0 (6.7.5), “special case”; EGA IV (11.3.10.2), “1°”; EGA IV (2.1.5), “special case”; EGA IV (2.1.6), “special case”; EGA IV (2.2.11), “(iii), special case”; EGA IV (7.3.5), “special case”; EGA 0 (6.6.4), “necessity, flat case”; SGA 1 IV (5.9), “(i)”; SGA 3 VIIB (1.3.3), “(i), special case”.
- [`Module.FaithfullyFlat.trans`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FaithfullyFlat.trans#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Basic.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Basic.lean#L78) (StacksFrontier): “a faithfully flat module over a faithfully flat algebra is faithfully flat”. References: EGA IV (11.3.10.2), “1°, special case”; EGA IV (2.2.10), “special case”; EGA IV (2.2.11), “special case”; EGA IV (2.2.13), “(iii)”; EGA 0 (6.6.4), “necessity, ff case”.

## Tag 00HD, a lemma

[Tag 00HD](https://stacks.math.columbia.edu/tag/00HD) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Flat.iff_rTensor_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.iff_rTensor_exact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L165) (StacksFrontier): “(1) flat iff - ⊗ M exact (links Mathlib's Flat to the Stacks definition)”. References: EGA 0 (6.1.1); EGA III (6.1.1), “special case”; EGA IV (2.2.7), “partial”; SGA 4 V (1.1), “special case”; SGA 4 V (1.7.2), “(i) ⇔ (ii), special case”; SGA 4½ Etat 0 (6.2), “special case”; SGA 6 0 (2.9), “affine case”; SGA 7 VII (3.7.6), “partial”.
- [`Module.Flat.iff_rTensor_preserves_injective_linearMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.iff_rTensor_preserves_injective_linearMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L167) (StacksFrontier): “(1) <=> (2)”. References: EGA 0 (6.1.1); EGA IV (2.2.7), “partial”; EGA IV (21.5.3), “partial”; SGA 3 I (5.3.1.1), “partial”.
- [`Module.Flat.iff_rTensor_injective'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.iff_rTensor_injective'#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L168) (StacksFrontier): “(1) <=> (3)”. References: EGA 0 (6.1.1), “special case”.
- [`Module.Flat.iff_rTensor_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.iff_rTensor_injective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L169) (StacksFrontier): “(1) <=> (4)”. References: EGA 0 (6.1.1), “more general”; EGA 0 (6.7.3), “Algebraic reduction”.

## Tag 05UU, a lemma

[Tag 05UU](https://stacks.math.columbia.edu/tag/05UU) in the Stacks Project.

**`StacksColimitRingsFlat.flat_of_forall_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/DirectLimit.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/DirectLimit.lean#L195). The attribute's comment: “(1)”. References: EGA 0 (6.2.3), “special case”.

> If `M` is an `R`-module that is flat as an `R_i`-module for every
> `i` (via the structure map `R_i → R`), then `M` is flat as an `R`-module.

```lean
theorem flat_of_forall_flat
    [Nonempty ι] [IsDirected ι (· ≤ ·)] [DirectedSystem G (fun i j h => (φ i j h : G i → G j))]
    (M : Type*) [AddCommGroup M] [Module (ColimitRing G φ) M]
    (hflat : ∀ i : ι, @Module.Flat (G i) M _ _ (Module.compHom M (structHom G φ i))) :
    Module.Flat (ColimitRing G φ) M
```

**`StacksColimitRingsFlat.colimitModule_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/DirectLimit.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/DirectLimit.lean#L469). The attribute's comment: “(2)”. References: EGA 0 (6.1.2), “more general”; EGA 0 (6.2.3); SGA 4 VI (8.6.4), “special case”.

> If each `M_i` is a flat `R_i`-module and the `f_{ii'}` are a
> compatible system of `φ_{ii'}`-semilinear maps, then the colimit
> `M = colim_i M_i` is a flat `R`-module.

```lean
theorem colimitModule_flat
    [Nonempty ι] [IsDirected ι (· ≤ ·)] [DecidableEq ι]
    [DirectedSystem G (fun i j h => (φ i j h : G i → G j))]
    (M : ι → Type*) [(i : ι) → AddCommGroup (M i)] [(i : ι) → Module (G i) (M i)]
    (hflat : ∀ i : ι, Module.Flat (G i) (M i))
    (f : (i j : ι) → (h : i ≤ j) → M i →ₛₗ[φ i j h] M j)
    (hf_id : ∀ (i : ι) (x : M i), f i i le_rfl x = x)
    (hf_comp : ∀ (i j k : ι) (hij : i ≤ j) (hjk : j ≤ k) (x : M i),
      f j k hjk (f i j hij x) = f i k (hij.trans hjk) x) :
    Module.Flat (ColimitRing G φ) (ColimitModule M f)
```

## Tag 00HI, a lemma

[Tag 00HI](https://stacks.math.columbia.edu/tag/00HI) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Flat.baseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.baseChange#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Basic.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Basic.lean#L88) (StacksFrontier): “flat base change”. References: EGA 0 (6.2.1), “more general”; EGA 0 (6.6.3), “necessity”; EGA III (7.4.1), “partial”; EGA III (7.7.2), “special case”; EGA III (7.9.7), “special case”; EGA IV (11.2.6.1), “(ii), sufficiency”; EGA IV (11.3.10.2), “1°”; EGA IV (2.1.4), “special case”; EGA IV (2.1.5), “special case”; EGA IV (2.2.10), “special case”; EGA IV (20.6.9), “partial”; EGA IV (21.15.9), “partial”; SGA 3 III (0.13), “special case”; SGA 3 V (7.4), “(i), special case”; SGA 3 VIB (10.1), “special case”; SGA 3 VIB (11.1), “special case”; SGA 3 VIB (2.1.2), “special case”; SGA 3 VIIB (1.2.1), “partial”; SGA 3 VIIB (1.3.3), “(iii), special case”; SGA 3 XIX (2.1), “special case”; SGA 3 XV (3.8), “partial”; SGA 4 V (1.7.1), “special case”; SGA 4 V (8.2.9), “special case”; SGA 6 III (3.5.2), “Affine case”; SGA 6 IV (3.1.1), “special case”; SGA 6 XII (2.3), “(a)”; SGA 7 VII (1.3.8), “flatness clause”.
- [`Module.FaithfullyFlat.instTensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FaithfullyFlat.instTensorProduct#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Basic.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Basic.lean#L116) (StacksFrontier): “faithfully flat base change”. References: EGA 0 (6.6.3), “necessity”; EGA IV (11.9.14), “affine case”; EGA IV (2.2.10), “special case”; EGA IV (2.2.11), “(i), affine case”; EGA IV (2.2.13), “(i) for affine schemes”; EGA IV (2.2.2), “partial”; EGA IV (2.5.1), “special case”; EGA IV (2.5.8.8), “partial”; EGA 0 (6.4.5), “first assertion”; EGA 0 (6.4.4), “last assertion”.

## Tag 00HJ, a lemma

[Tag 00HJ](https://stacks.math.columbia.edu/tag/00HJ) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Flat.iff_flat_tensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.iff_flat_tensorProduct#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/Basic.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Basic.lean#L131) (StacksFrontier): “flatness descends along a faithfully flat base change”. References: EGA 0 (6.6.3); EGA IV (2.2.11), “(iii), special case”; EGA IV (2.5.1), “flat part, affine”; SGA 3 XIX (2.1), “special case”; SGA 4½ Arcata (1.4.2), “more general”; SGA 6 I (5.7), “a), special case”.

## Tag 0584, a lemma

[Tag 0584](https://stacks.math.columbia.edu/tag/0584) in the Stacks Project.

**`Module.Flat.tensorProduct_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/BaseChangeAlongFlatAlgebra.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/BaseChangeAlongFlatAlgebra.lean#L74). The attribute's comment: “(1)”. References: EGA 0 (6.2.1), “M⊗_A N is B-flat”.

> **Stacks 0584 (1)**: if `S → S'` is a flat map of `R`-algebras and `M` is an `S`-module that
> is flat over `R`, then `S' ⊗_S M` is flat over `R`.

```lean
theorem tensorProduct_of_flat [Module.Flat S S'] [Module.Flat R M] :
    Module.Flat R (S' ⊗[S] M)
```

**`Module.Flat.tensorProduct_iff_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/BaseChangeAlongFlatAlgebra.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/BaseChangeAlongFlatAlgebra.lean#L84). The attribute's comment: “(2)”.

> **Stacks 0584 (2)**: if `S → S'` is a faithfully flat map of `R`-algebras, then an `S`-module
> `M` is flat over `R` if and only if `S' ⊗_S M` is flat over `R`.

```lean
theorem tensorProduct_iff_of_faithfullyFlat {R S S' M : Type*} [CommRing R] [CommRing S]
    [CommRing S'] [Algebra R S] [Algebra R S'] [Algebra S S'] [IsScalarTower R S S']
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.FaithfullyFlat S S'] :
    Module.Flat R (S' ⊗[S] M) ↔ Module.Flat R M
```

## Tag 039V, a lemma

[Tag 039V](https://stacks.math.columbia.edu/tag/039V) in the Stacks Project.

**`Stacks.Flatness.NilpotentFibreCriterion.flat_of_flat_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FibrewiseCriterion.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FibrewiseCriterion.lean#L412). References: EGA 0 (6.6.4), “sufficiency, flat case”.

> **Flat permanence**. If an `S`-module `M` is flat over `R` and faithfully flat over `S`,
> then `S` is flat over `R`.

```lean
theorem flat_of_flat_of_faithfullyFlat
    (M : Type*) [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.Flat R M] [Module.FaithfullyFlat S M] : Module.Flat R S
```

## Tag 00HL, a lemma

[Tag 00HL](https://stacks.math.columbia.edu/tag/00HL) in the Stacks Project.

**`tensor_flat_quotient_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTensorShortExact.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatTensorShortExact.lean#L121). References: EGA 0 (6.1.2), “exactness”; EGA IV (2.1.8), “(i), affine case”; EGA 0 (15.1.17), “more general”; EGA IV (2.1.10), “special case”; SGA 1 IV (1.1), “(i)”; SGA 3 III (4.6.4), “more general”; SGA 4 XVII (4.1.1), “(ii), special case”.

> Let `0 → F'' → F' → F → 0` be a short exact sequence of modules over a commutative ring `R`:
> `a : F'' → F'` is injective, the sequence is exact at `F'` and `b : F' → F` is surjective. If `F`
> is flat, then for every `R`-module `G` the tensored sequence `0 → F'' ⊗ G → F' ⊗ G → F ⊗ G → 0`
> is short exact: `a ⊗ 1` is injective, the sequence is exact at `F' ⊗ G`, and `b ⊗ 1` is
> surjective.

```lean
theorem tensor_flat_quotient_shortExact
    {R : Type*} [CommRing R]
    {F'' F' F : Type*} [AddCommGroup F''] [AddCommGroup F'] [AddCommGroup F]
    [Module R F''] [Module R F'] [Module R F]
    (a : F'' →ₗ[R] F') (b : F' →ₗ[R] F)
    (ha : Function.Injective a) (hexact : Function.Exact a b)
    (hb : Function.Surjective b)
    (hFflat : Module.Flat R F)
    (G : Type*) [AddCommGroup G] [Module R G] :
    Function.Injective (LinearMap.rTensor G a) ∧
      Function.Exact (LinearMap.rTensor G a) (LinearMap.rTensor G b) ∧
      Function.Surjective (LinearMap.rTensor G b)
```

**`flat_tor_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ShortExact.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ShortExact.lean#L310). References: EGA IV (2.1.8), “(i), affine case”; EGA 0 (15.1.17), “more general”; EGA 0 (6.1.2); SGA 1 IV (1.1); SGA 3 XV (2.10), “partial”; SGA 4 XVII (4.1.1), “(ii), special case”.

> If `0 → M'' → M' → M → 0` is a short exact sequence of `R`-modules whose quotient
> term `M` is flat, then tensoring with an arbitrary `R`-module `N` leaves the sequence
> short exact.

```lean
theorem flat_tor_zero
    {R : Type*} [CommRing R]
    {M'' M' M N : Type*}
    [AddCommGroup M''] [AddCommGroup M'] [AddCommGroup M] [AddCommGroup N]
    [Module R M''] [Module R M'] [Module R M] [Module R N]
    [Module.Flat R M]
    (f : M'' →ₗ[R] M') (g : M' →ₗ[R] M)
    (hf : Function.Injective f)
    (hfg : Function.Exact f g)
    (hg : Function.Surjective g) :
    Function.Injective (LinearMap.lTensor N f) ∧
    Function.Exact (LinearMap.lTensor N f) (LinearMap.lTensor N g) ∧
    Function.Surjective (LinearMap.lTensor N g)
```

## Tag 00HM, a lemma

[Tag 00HM](https://stacks.math.columbia.edu/tag/00HM) in the Stacks Project.

**`flat_of_flat_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ShortExact.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ShortExact.lean#L236). References: EGA 0 (6.4.3), “M is flat”; EGA 0 (6.1.2), “M' flat implies M flat”; EGA III (6.5.10), “special case”; EGA IV (2.1.8), “(ii)”; SGA 1 IV (1.1), “(ii)”.

> Part 1: In a short exact sequence `0 → M' → M → M'' → 0` of `R`-modules,
> if `M'` and `M''` are flat, then `M` is flat.

```lean
theorem flat_of_flat_of_flat
    {R : Type*} [CommRing R]
    {M' M M'' : Type*}
    [AddCommGroup M'] [AddCommGroup M] [AddCommGroup M'']
    [Module R M'] [Module R M] [Module R M'']
    (f : M' →ₗ[R] M) (g : M →ₗ[R] M'')
    (hf : Function.Injective f)
    (hfg : Function.Exact f g)
    (hg : Function.Surjective g)
    [Module.Flat R M'] [Module.Flat R M''] :
    Module.Flat R M
```

**`flat_of_flat_of_flat_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/ShortExact.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/ShortExact.lean#L277). References: EGA 0 (20.6.21), “more general”; EGA 0 (6.1.2), “M flat implies M' flat”; EGA IV (2.1.10), “Affine case”; EGA IV (2.1.8), “(ii)”; SGA 1 IV (1.1), “(ii)”; SGA 4 XVII (4.1.1), “(i), special case”; SGA 6 I (5.1.1), “special case”.

> Part 2: In a short exact sequence `0 → M' → M → M'' → 0` of `R`-modules,
> if `M` and `M''` are flat, then `M'` is flat.

```lean
theorem flat_of_flat_of_flat_quotient
    {R : Type*} [CommRing R]
    {M' M M'' : Type*}
    [AddCommGroup M'] [AddCommGroup M] [AddCommGroup M'']
    [Module R M'] [Module R M] [Module R M'']
    (f : M' →ₗ[R] M) (g : M →ₗ[R] M'')
    (hf : Function.Injective f)
    (hfg : Function.Exact f g)
    (hg : Function.Surjective g)
    [Module.Flat R M] [Module.Flat R M''] :
    Module.Flat R M'
```

## Tag 00HO, a lemma

[Tag 00HO](https://stacks.math.columbia.edu/tag/00HO) in the Stacks Project.

Declarations registered for the tag:

- [`Module.FaithfullyFlat.iff_zero_iff_rTensor_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FaithfullyFlat.iff_zero_iff_rTensor_zero#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean#L203) (StacksFrontier): “with the two modules implicit and the inner biconditional the other way round”. References: EGA 0 (6.6.1), “more general”; EGA IV (2.2.7), “special case”; EGA 0 (6.4.1), “(a) ⇔ (c)”; EGA 0 (6.4.1), “(a) <=> (c)”; SGA 1 IV (2.1).
- [`Module.FaithfullyFlat.iff_zero_iff_lTensor_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FaithfullyFlat.iff_zero_iff_lTensor_zero#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean#L209) (StacksFrontier): “the `lTensor` variant”. References: EGA 0 (6.4.1); EGA 0 (6.6.1), “more general”; EGA IV (2.2.7), “special case”; SGA 1 IV (2.1).

## Tag 00HP, a lemma

[Tag 00HP](https://stacks.math.columbia.edu/tag/00HP) in the Stacks Project.

**`faithfullyFlat_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean#L90). References: EGA 0 (6.4.1), “(a) ⇔ (b), (a) ⇔ (d)”; EGA IV (2.2.1), “affine case, a)<=>b)”; EGA IV (2.2.7), “special case”; EGA IV (2.5.8.8), “partial”; SGA 1 IV (2.1), “(i bis) <=> (i ter)”.

> For a flat `R`-module `M`, faithful flatness is equivalent to each of: `M ⊗[R] N` is
> nonzero for every nonzero `R`-module `N`; `M ⊗[R] κ(𝔭)` is nonzero for every prime `𝔭`;
> `M ⊗[R] κ(𝔪)` is nonzero for every maximal ideal `𝔪`.

```lean
theorem faithfullyFlat_tfae [Module.Flat R M] :
    [ FaithfullyFlat R M,
      ∀ (N : Type (max u v)) [AddCommGroup N] [Module R N],
        Nontrivial N → Nontrivial (M ⊗[R] N),
      ∀ (p : Ideal R) [p.IsPrime], Nontrivial (M ⊗[R] p.ResidueField),
      ∀ (m : Ideal R) [m.IsMaximal], Nontrivial (M ⊗[R] m.ResidueField) ].TFAE
```

## Tag 00HQ, a lemma

[Tag 00HQ](https://stacks.math.columbia.edu/tag/00HQ) in the Stacks Project.

**`faithfullyFlat_tfae00HQ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean#L168). References: EGA IV (2.2.2), “a)<=>b'), affine F=O_X”; EGA IV (2.2.3), “M = B with A → B flat”; EGA IV (2.2.5), “special case”; EGA IV (2.2.6), “special case”; SGA 1 IV (2.6), “(i) ⇔ (ii) ⇔ (ii bis)”; SGA 1 IV (2.3), “M = B”; SGA 3 V (4.1.1), “Faithful flatness clause”; SGA 4½ Arcata (1.4.1), “special case”.

> For a flat ring map `f : R →+* S`, faithful flatness is equivalent to surjectivity of
> `Spec(S) → Spec(R)`, and to every closed point of `Spec(R)` lying in the image of that
> map.

```lean
theorem faithfullyFlat_tfae00HQ
    {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S) (hf : RingHom.Flat f) :
    List.TFAE
      [ RingHom.FaithfullyFlat f,
        Function.Surjective (PrimeSpectrum.comap f),
        ∀ x : PrimeSpectrum R, IsClosed ({x} : Set (PrimeSpectrum R)) →
          x ∈ Set.range (PrimeSpectrum.comap f) ]
```

## Tag 00HR, a lemma

[Tag 00HR](https://stacks.math.columbia.edu/tag/00HR) in the Stacks Project.

Declarations registered for the tag:

- [`Module.FaithfullyFlat.of_flat_of_isLocalHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FaithfullyFlat.of_flat_of_isLocalHom#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Basic.lean#L215) (StacksFrontier). References: EGA 0 (6.6.1), “(e) ⇒ (a), special case”; EGA 0 (6.6.2), “partial, special case”; EGA IV (2.5.5.4), “special case”; SGA 1 IV (2.6), “(i), special case”; SGA 1 IV (2.2), “case M = B”.

## Tag 00HT, a lemma

[Tag 00HT](https://stacks.math.columbia.edu/tag/00HT) in the Stacks Project.

**`flat_of_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Localization.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Localization.lean#L65). The attribute's comment: “part1”. References: SGA 1 IV (1.2), “M = B = A”.

> The localisation `S⁻¹R` is a flat `R`-algebra.

```lean
theorem flat_of_isLocalization
    {R : Type*} [CommRing R] (S : Submonoid R)
    (Rs : Type*) [CommRing Rs] [Algebra R Rs] [IsLocalization S Rs] :
    Module.Flat R Rs
```

**`flat_iff_flat_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Localization.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Localization.lean#L73). The attribute's comment: “part2”. References: SGA 1 IV (1.2), “(i) 2nd assertion”.

> For an `S⁻¹R`-module `M`, flatness over `R` is equivalent to flatness over `S⁻¹R`.

```lean
theorem flat_iff_flat_localization
    {R : Type*} [CommRing R] (S : Submonoid R)
    (Rs : Type*) [CommRing Rs] [Algebra R Rs] [IsLocalization S Rs]
    (M : Type*) [AddCommGroup M] [Module R M] [Module Rs M] [IsScalarTower R Rs M] :
    Module.Flat R M ↔ Module.Flat Rs M
```

**`flat_iff_forall_flat_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Localization.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Localization.lean#L91). The attribute's comment: “part3”. References: SGA 1 IV (1.2), “B = A, primes”.

> `M` is flat over `R` iff `M_𝔭` is flat over `R_𝔭` for every prime `𝔭` of `R`.

```lean
theorem flat_iff_forall_flat_atPrime
    {R : Type*} [CommRing R] (M : Type*) [AddCommGroup M] [Module R M] :
    Module.Flat R M ↔
      ∀ (P : Ideal R) (_ : P.IsPrime),
        Module.Flat (Localization.AtPrime P) (LocalizedModule.AtPrime P M)
```

**`flat_iff_flat_localizedModule_atMaximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Localization.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Localization.lean#L103). The attribute's comment: “part4”. References: SGA 1 IV (1.2), “B = A”.

> `M` is flat over `R` iff `M_𝔪` is flat over `R_𝔪` for every maximal ideal `𝔪` of `R`.

```lean
theorem flat_iff_flat_localizedModule_atMaximal
    {R : Type*} [CommRing R] (M : Type*) [AddCommGroup M] [Module R M] :
    Module.Flat R M ↔
      ∀ (m : Ideal R) (_ : m.IsMaximal),
        haveI : m.IsPrime := Ideal.IsMaximal.isPrime ‹_›
        Module.Flat (Localization.AtPrime m) (LocalizedModule.AtPrime m M)
```

**`flat_of_flat_localizedModule_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Localization.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Localization.lean#L190). The attribute's comment: “part7_backward”. References: SGA 1 IV (1.2), “(ii)”.

> If every `M_𝔪` (for `𝔪 ⊆ A` maximal) is flat over `R_𝔭` (with `𝔭 = R ∩ 𝔪`), then `M` is flat
> over `R`.

```lean
theorem flat_of_flat_localizedModule_maximal
    {R : Type*} [CommRing R]
    {A : Type*} [CommRing A] [Algebra R A]
    (M : Type*) [AddCommGroup M] [Module R M] [Module A M] [IsScalarTower R A M]
    (h : ∀ (m : Ideal A) (_ : m.IsMaximal),
        letI : m.IsPrime := Ideal.IsMaximal.isPrime ‹_›
        letI : (m.comap (algebraMap R A)).IsPrime := Ideal.comap_isPrime _ _
        letI : m.LiesOver (m.comap (algebraMap R A)) := ⟨rfl⟩
        letI : Algebra (Localization.AtPrime (m.comap (algebraMap R A)))
                       (Localization.AtPrime m) :=
          Localization.AtPrime.algebraOfLiesOver _ _
        letI : Module (Localization.AtPrime (m.comap (algebraMap R A)))
                      (LocalizedModule.AtPrime m M) :=
          Module.compHom _ (algebraMap _ (Localization.AtPrime m))
        Module.Flat
          (Localization.AtPrime (m.comap (algebraMap R A)))
          (LocalizedModule.AtPrime m M)) :
    Module.Flat R M
```

**`flat_of_flat_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/Localization.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/Localization.lean#L217). The attribute's comment: “part6_backward”. References: SGA 1 IV (1.2), “(ii) with all primes”.

> If every `M_𝔮` (for `𝔮 ⊆ A` prime) is flat over `R_𝔭` (with `𝔭 = 𝔮 ∩ R`), then `M` is flat
> over `R`.

```lean
theorem flat_of_flat_atPrime
    {R : Type*} [CommRing R]
    {A : Type*} [CommRing A] [Algebra R A]
    (M : Type*) [AddCommGroup M] [Module R M] [Module A M] [IsScalarTower R A M]
    (h : ∀ (Q : Ideal A) (_ : Q.IsPrime),
        letI : (Q.comap (algebraMap R A)).IsPrime := Ideal.comap_isPrime _ _
        letI : Q.LiesOver (Q.comap (algebraMap R A)) := ⟨rfl⟩
        letI : Algebra (Localization.AtPrime (Q.comap (algebraMap R A)))
                       (Localization.AtPrime Q) :=
          Localization.AtPrime.algebraOfLiesOver _ _
        letI : Module (Localization.AtPrime (Q.comap (algebraMap R A)))
                      (LocalizedModule.AtPrime Q M) :=
          Module.compHom _ (algebraMap _ (Localization.AtPrime Q))
        Module.Flat
          (Localization.AtPrime (Q.comap (algebraMap R A)))
          (LocalizedModule.AtPrime Q M)) :
    Module.Flat R M
```

## Tag 090N, a lemma

[Tag 090N](https://stacks.math.columbia.edu/tag/090N) in the Stacks Project.

**`faithfullyFlat_directLimit_of_faithfullyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/DirectLimit.lean, line 582](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/DirectLimit.lean#L582). References: SGA 3 VIB (11.17.1), “constant base”.

> A directed colimit of faithfully flat `R`-algebras is faithfully flat over `R`: if each
> `R → Sᵢ` is faithfully flat and the transition maps are `R`-algebra maps, then the induced
> map from `R` to `colim Sᵢ` is faithfully flat.

```lean
theorem faithfullyFlat_directLimit_of_faithfullyFlat
    {ι : Type*} [Preorder ι] [IsDirectedOrder ι] [Nonempty ι]
    (R : Type*) [CommRing R]
    (S : ι → Type*) [(i : ι) → CommRing (S i)] [(i : ι) → Algebra R (S i)]
    (φ : (i j : ι) → i ≤ j → S i →+* S j)
    [DirectedSystem S (fun i j h => φ i j h)]
    -- transition maps are R-algebra maps:
    (hφ : ∀ i j (h : i ≤ j), (φ i j h).comp (algebraMap R (S i)) = algebraMap R (S j))
    -- each Sᵢ is faithfully flat over R:
    (hff : ∀ i, (algebraMap R (S i)).FaithfullyFlat) :
    ((Ring.DirectLimit.of S (fun i j h => φ i j h) (Classical.arbitrary ι)).comp
      (algebraMap R (S (Classical.arbitrary ι)))).FaithfullyFlat
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.39, Tag 00H9](https://stacks.math.columbia.edu/tag/00H9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

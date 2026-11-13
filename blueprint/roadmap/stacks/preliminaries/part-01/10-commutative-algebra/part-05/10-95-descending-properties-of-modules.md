---
declaration: section
origin: cited
lean: Module.mittagLeffler_of_mittagLeffler_tensorProduct, countablyGenerated_of_faithfullyFlat_baseChange, Module.countablyGenerated_and_projective_of_faithfullyFlat_baseChange, exists_countablyGenerated_submodule_le_baseChange_range, exists_countablyGenerated_baseChange_eq_iSup_of_internal_directSum, Module.Projective.of_projective_tensorProduct
statement: formalized
proof: formalized
---

# 10.95 Descending properties of modules

Section 10.95 of the Stacks Project, [Tag 05A4](https://stacks.math.columbia.edu/tag/05A4). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05A5, a lemma

[Tag 05A5](https://stacks.math.columbia.edu/tag/05A5) in the Stacks Project.

**`Module.mittagLeffler_of_mittagLeffler_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/MittagLeffler/Descent.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/MittagLeffler/Descent.lean#L497). The attribute's comment: “Mittag-Leffler is spelled out inline as condition (1) of 059E, as in 05A3, 05CN and 05CQ. The base change is written `S ⊗[R] M`, Mathlib's order, the source writing `M ⊗_R S`.”. References: SGA 3 VIB (11.8.2).

> **Stacks 05A5.** Let `R → S` be a faithfully flat ring map and let `M` be an `R`-module. If the
> `S`-module `S ⊗_R M` is Mittag-Leffler, then `M` is Mittag-Leffler. The Mittag-Leffler condition is
> spelled out in the intrinsic form 059E (1): every map `f` from a finitely presented module into the
> module in question dominates and is dominated by a map `g` into a finitely presented module,
> domination meaning equality of the kernels of the maps `· ⊗ id_T`.

```lean
public theorem Module.mittagLeffler_of_mittagLeffler_tensorProduct {R : Type u} [CommRing R]
    [Small.{v} R] {S : Type v} [CommRing S] [Algebra R S] [Module.FaithfullyFlat R S]
    {M : Type v} [AddCommGroup M] [Module R M]
    (hM : ∀ (P : Type v) [AddCommGroup P] [Module S P] [Module.FinitePresentation S P]
      (f : P →ₗ[S] S ⊗[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module S Q)
        (_ : Module.FinitePresentation S Q) (g : P →ₗ[S] Q), ∀ (T : Type v) [AddCommGroup T]
          [Module S T], LinearMap.ker (f.rTensor T) = LinearMap.ker (g.rTensor T)) :
    ∀ (P : Type v) [AddCommGroup P] [Module R P] [Module.FinitePresentation R P]
      (f : P →ₗ[R] M), ∃ (Q : Type v) (_ : AddCommGroup Q) (_ : Module R Q)
        (_ : Module.FinitePresentation R Q) (g : P →ₗ[R] Q), ∀ (T : Type v) [AddCommGroup T]
          [Module R T], LinearMap.ker (f.rTensor T) = LinearMap.ker (g.rTensor T)
```

## Tag 0GVD, a lemma

[Tag 0GVD](https://stacks.math.columbia.edu/tag/0GVD) in the Stacks Project.

**`countablyGenerated_of_faithfullyFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Descent.lean#L273).

> **Stacks 0GVD**. Let `R → S` be a faithfully flat ring map and let `M` be an `R`-module.
> If the base change `S ⊗[R] M` is countably generated as an `S`-module, then `M` is countably
> generated as an `R`-module.

```lean
theorem countablyGenerated_of_faithfullyFlat_baseChange
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Module.FaithfullyFlat R S]
    (M : Type*) [AddCommGroup M] [Module R M]
    (h : Module.CountablyGenerated S (S ⊗[R] M)) :
    Module.CountablyGenerated R M
```

## Tag 05A6, a lemma

[Tag 05A6](https://stacks.math.columbia.edu/tag/05A6) in the Stacks Project.

**`Module.countablyGenerated_and_projective_of_faithfullyFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/CountablyGeneratedProjective.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/FaithfullyFlat/CountablyGeneratedProjective.lean#L273). The attribute's comment: “Countable generation is `Module.CountablyGenerated`, the predicate introduced with 0GVD. The base change is written `S ⊗[R] M`, Mathlib's order, the source writing `M ⊗_R S`.”. References: SGA 3 VIB (11.8.2), “countably generated case”; SGA 3 VIB (11.8.1), “(ii), special case”.

> **Stacks 05A6.** Let `R → S` be a faithfully flat ring map and let `M` be an `R`-module. If the
> `S`-module `S ⊗_R M` is countably generated and projective, then `M` is countably generated and
> projective.

```lean
public theorem countablyGenerated_and_projective_of_faithfullyFlat_baseChange {R : Type*}
    [CommRing R] {S : Type*} [CommRing S] [Algebra R S] [Module.FaithfullyFlat R S] {M : Type*}
    [AddCommGroup M] [Module R M] [Module.Projective S (S ⊗[R] M)]
    (hM : Module.CountablyGenerated S (S ⊗[R] M)) :
    Module.CountablyGenerated R M ∧ Module.Projective R M
```

## Tag 05A7, a lemma

[Tag 05A7](https://stacks.math.columbia.edu/tag/05A7) in the Stacks Project.

**`exists_countablyGenerated_submodule_le_baseChange_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/CountablyGenerated.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/CountablyGenerated.lean#L77).

> **Stacks Tag 05A7, Lemma 10.95.4.**
> Let `R → S` be a ring map, `M` an `R`-module, and `Q` a countably generated
> `S`-submodule of `S ⊗[R] M`. Then there exists a countably generated
> `R`-submodule `P` of `M` such that `Q ⊆ Im(S ⊗[R] P → S ⊗[R] M)`, where the map
> is induced by the inclusion `P ↪ M`.

```lean
theorem exists_countablyGenerated_submodule_le_baseChange_range
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    {M : Type*} [AddCommGroup M] [Module R M]
    (Q : Submodule S (S ⊗[R] M)) (hQ : Q.IsCountablyGenerated) :
    ∃ P : Submodule R M, P.IsCountablyGenerated ∧
      Q ≤ LinearMap.range (LinearMap.baseChange S P.subtype)
```

## Tag 05A8, a lemma

[Tag 05A8](https://stacks.math.columbia.edu/tag/05A8) in the Stacks Project.

**`exists_countablyGenerated_baseChange_eq_iSup_of_internal_directSum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/CountablyGenerated.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/CountablyGenerated.lean#L167).

> **Stacks Tag 05A8 / Lemma 10.95.5.**  If `M ⊗_R S` decomposes as an internal
> direct sum of countably generated `S`-submodules `Q_i`, then any countably
> generated `R`-submodule `N` of `M` is contained in a countably generated
> `R`-submodule `N'` whose image `Im(N' ⊗_R S → M ⊗_R S) = N'.baseChange S` equals
> the partial direct sum `⨁_{i ∈ I'} Q_i` over some subset `I' ⊆ I`.

```lean
theorem exists_countablyGenerated_baseChange_eq_iSup_of_internal_directSum
    (Q : I → Submodule S (TensorProduct R S M))
    (hQ : DirectSum.IsInternal Q)
    (hQcg : ∀ i, (Q i).IsCountablyGenerated)
    (N : Submodule R M) (hN : N.IsCountablyGenerated) :
    ∃ (N' : Submodule R M) (I' : Set I),
      N'.IsCountablyGenerated ∧ N ≤ N' ∧
      N'.baseChange S = ⨆ i : I', Q i
```

## Tag 05A9, a theorem

[Tag 05A9](https://stacks.math.columbia.edu/tag/05A9) in the Stacks Project.

**`Module.Projective.of_projective_tensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FaithfullyFlat/Projective.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/FaithfullyFlat/Projective.lean#L580). The attribute's comment: “The source's `M ⊗_R S` is written `S ⊗[R] M`, Mathlib's order for a base change and the one used by `Module.Flat.of_flat_tensorProduct`. The finite case is 058S and the countably generated case is 05A6; neither hypothesis appears here.”. References: SGA 3 VIB (11.8.2); SGA 3 VIB (11.8.1), “(ii)”.

> **Stacks 05A9.** Let `R → S` be a faithfully flat ring map and let `M` be an `R`-module. If
> the `S`-module `S ⊗_R M` is projective, then `M` is projective. This is the projective analogue of
> `Module.Flat.of_flat_tensorProduct`, and it assumes no finiteness of `M`.

```lean
public theorem Projective.of_projective_tensorProduct {R : Type*} [CommRing R] {M : Type*}
    [AddCommGroup M] [Module R M] (S : Type*) [CommRing S] [Algebra R S]
    [Module.FaithfullyFlat R S] [Module.Projective S (S ⊗[R] M)] :
    Module.Projective R M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.95, Tag 05A4](https://stacks.math.columbia.edu/tag/05A4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

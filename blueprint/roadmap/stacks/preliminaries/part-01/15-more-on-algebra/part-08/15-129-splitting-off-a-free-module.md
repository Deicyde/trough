---
declaration: section
origin: cited
lean: ClosedPointSpace, ClosedPointResidueField, ClosedPointFiber, sectionAt, finiteDimensional_fiber, canonicalKernel, CanonicalQuotient, canonical_exact_and_splits_iff_linearIndependent
statement: formalized
proof: formalized
---

# 15.129 Splitting off a free module

Section 15.129 of the Stacks Project, [Tag 0GV7](https://stacks.math.columbia.edu/tag/0GV7). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GV8, a situation

[Tag 0GV8](https://stacks.math.columbia.edu/tag/0GV8) in the Stacks Project.

**`ClosedPointSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean#L83).

> The space of closed points of the prime spectrum of `R`, with its induced topology.

```lean
abbrev ClosedPointSpace (R : Type u) [CommRing R]
```

**`ClosedPointResidueField`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean#L88).

> The residue field at a closed point `x` of `Spec(R)`.

```lean
abbrev ClosedPointResidueField {R : Type u} [CommRing R] (x : ClosedPointSpace R)
```

**`ClosedPointFiber`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean#L105).

> The fibre `M(x) = M / xM` of an `R`-module at a closed point `x`.

```lean
abbrev ClosedPointFiber {R : Type u} [CommRing R] (M : Type v) [AddCommGroup M] [Module R M]
    (x : ClosedPointSpace R)
```

**`sectionAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean#L111).

> The canonical image `s(x)` of a module element `s` in the fibre at `x`.

```lean
abbrev sectionAt {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    (x : ClosedPointSpace R) (s : M) : ClosedPointFiber M x
```

**`finiteDimensional_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean#L118).

> The fibre of a finite module at a closed point is finite-dimensional over the
> residue field at that point.

```lean
theorem finiteDimensional_fiber
    {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    [Module.Finite R M] (x : ClosedPointSpace R) :
    FiniteDimensional (ClosedPointResidueField x) (ClosedPointFiber M x)
```

## Tag 0GV9, a lemma

[Tag 0GV9](https://stacks.math.columbia.edu/tag/0GV9) in the Stacks Project.

**`canonicalKernel`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean#L154).

> The canonical subspace `B(x)` of the fibre: the common kernel of all fibre
> functionals induced by `R`-linear maps `M → R`.

```lean
noncomputable def canonicalKernel {R : Type u} [CommRing R]
    (M : Type v) [AddCommGroup M] [Module R M] (x : ClosedPointSpace R) :
    Submodule (ClosedPointResidueField x) (ClosedPointFiber M x)
```

**`CanonicalQuotient`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean#L169).

> The canonical quotient `V(x) = M(x) / B(x)`.

```lean
abbrev CanonicalQuotient {R : Type u} [CommRing R]
    (M : Type v) [AddCommGroup M] [Module R M] (x : ClosedPointSpace R)
```

**`canonical_exact_and_splits_iff_linearIndependent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean#L368). References: EGA 0 (5.5.5), “affine case, closed pt”.

> The canonical sequence `0 → B(x) → M(x) → V(x) → 0` is short exact.
> Moreover, a finite family of elements of `M` splits off a free direct summand after
> inverting an element outside `x` if and only if its images in `V(x)` are linearly
> independent.

```lean
theorem canonical_exact_and_splits_iff_linearIndependent
    {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    [Module.FinitePresentation R M] (x : ClosedPointSpace R) :
    Function.Injective (canonicalKernel M x).subtype ∧
      Function.Exact (canonicalKernel M x).subtype (canonicalKernel M x).mkQ ∧
      Function.Surjective (canonicalKernel M x).mkQ ∧
      ∀ (r : ℕ) (s : Fin r → M),
        (∃ f : R, f ∉ x.1.asIdeal ∧ SplitsAfterInverting f s) ↔
          LinearIndependent (ClosedPointResidueField x)
            (fun i ↦ (canonicalKernel M x).mkQ (sectionAt x (s i)))
```

## Tag 0GVA, a lemma

[Tag 0GVA](https://stacks.math.columbia.edu/tag/0GVA) in the Stacks Project.

**`pi_canonicalQuotient_mkQ_sectionAt_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Fibres.lean#L390).

> At finitely many distinct closed points, every family of values in the canonical quotients
> `V(x)` is induced by a single element of the module.

```lean
theorem pi_canonicalQuotient_mkQ_sectionAt_surjective
    {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    {ι : Type w} [Finite ι] (x : ι → ClosedPointSpace R) (hx : Function.Injective x) :
    Function.Surjective fun s : M ↦
      fun i ↦ (canonicalKernel M (x i)).mkQ (sectionAt (x i) s)
```

## Tag 0GVB, a proposition

[Tag 0GVB](https://stacks.math.columbia.edu/tag/0GVB) in the Stacks Project.

**`exists_section_dependentLocus_subset_union_of_card_add_le_finrank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Basic.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Basic.lean#L348).

> Suppose that the dependent locus of `h` sections of a finitely presented module is contained
> in a closed set `F` of the Noetherian space of closed points. If every canonical quotient `V(y)`
> has dimension at least `h + k`, then one can choose a further section with arbitrary prescribed
> values at finitely many distinct points of `F`. The new dependent locus is contained in `F`
> together with a closed set all of whose irreducible components have codimension at least `k`.

```lean
theorem exists_section_dependentLocus_subset_union_of_card_add_le_finrank
    {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    [Module.FinitePresentation R M] [NoetherianSpace (ClosedPointSpace R)]
    {h k : ℕ} (sections : Fin h → M) (F : Set (ClosedPointSpace R)) (hF : IsClosed F)
    (hsections :
      {y | ¬LinearIndependent (ClosedPointResidueField y)
        (fun i ↦ (canonicalKernel M y).mkQ (sectionAt y (sections i)))} ⊆ F)
    {ι : Type w} [Finite ι] (x : ι → ClosedPointSpace R) (hx : Function.Injective x)
    (hxF : ∀ i, x i ∈ F) (v : ∀ i, CanonicalQuotient M (x i))
    (hdim : ∀ y : ClosedPointSpace R,
      h + k ≤ Module.finrank (ClosedPointResidueField y) (CanonicalQuotient M y)) :
    ∃ (s : M) (F' : Set (ClosedPointSpace R)),
      (∀ i, (canonicalKernel M (x i)).mkQ (sectionAt (x i) s) = v i) ∧
        IsClosed F' ∧
        {y | ¬LinearIndependent (ClosedPointResidueField y)
          (fun i ↦ (canonicalKernel M y).mkQ
            (sectionAt y ((Fin.snoc sections s : Fin (h + 1) → M) i)))} ⊆ F ∪ F' ∧
        ∀ Z : IrreducibleCloseds (ClosedPointSpace R),
          Maximal (fun W : IrreducibleCloseds (ClosedPointSpace R) ↦
            (W : Set (ClosedPointSpace R)) ⊆ F') Z →
            (k : ℕ∞) ≤ codimension Z
```

## Tag 0GVC, a theorem

[Tag 0GVC](https://stacks.math.columbia.edu/tag/0GVC) in the Stacks Project.

**`exists_linearEquiv_prod_of_local_free_summand_rank_gt_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Projective/SplitFree/Basic.lean, line 716](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Module/Projective/SplitFree/Basic.lean#L716).

> Let `M` be a finitely presented module over a commutative ring whose Noetherian space of
> closed points has dimension at most `d`. If at every closed point the localization of `M` has
> a free direct summand of some rank strictly greater than `d`, then a rank-one free summand
> splits from `M`.

```lean
theorem exists_linearEquiv_prod_of_local_free_summand_rank_gt_dimension
    {R : Type u} [CommRing R] {M : Type v} [AddCommGroup M] [Module R M]
    [Module.FinitePresentation R M] [NoetherianSpace (ClosedPointSpace R)]
    (d : ℕ) (hdim : topologicalKrullDim (ClosedPointSpace R) ≤ (d : WithBot ℕ∞))
    (hlocal : ∀ x : ClosedPointSpace R,
      ∃ r : ℕ, d < r ∧
        ∃ s : Fin r → LocalizedModule x.1.asIdeal.primeCompl M,
          ∃ p : LocalizedModule x.1.asIdeal.primeCompl M →ₗ[Localization x.1.asIdeal.primeCompl]
              (Fin r → Localization x.1.asIdeal.primeCompl),
            p.comp (Fintype.linearCombination (Localization x.1.asIdeal.primeCompl) s) =
              LinearMap.id) :
    ∃ N : Submodule R M, Nonempty (M ≃ₗ[R] R × N)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.129, Tag 0GV7](https://stacks.math.columbia.edu/tag/0GV7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)

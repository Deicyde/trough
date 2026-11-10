---
declaration: section
origin: cited
lean: RingTheory.Sequence.IsRegular, RingTheory.Sequence.isRegular_iff, RingTheory.Sequence.IsWeaklyRegular, RingTheory.Sequence.isWeaklyRegular_iff, regularSequence_xyz_one_sub_x, not_regularSequence_permuted_xyz_one_sub_x, IsLocalRing.isRegular_of_perm, RingTheory.Sequence.isRegular_map_algebraMap_iff_of_faithfullyFlat_of_isBaseChange
statement: formalized
proof: formalized
---

# 10.68 Regular sequences

Section 10.68 of the Stacks Project, [Tag 0AUH](https://stacks.math.columbia.edu/tag/0AUH). 9 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00LF, a definition

[Tag 00LF](https://stacks.math.columbia.edu/tag/00LF) in the Stacks Project.

Declarations registered for the tag:

- [`RingTheory.Sequence.IsRegular`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingTheory.Sequence.IsRegular#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Sequence/Regular/Basic.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Basic.lean#L93) (StacksFrontier): “an `M`-regular sequence”. References: EGA 0 (15.1.7), “nonzero quotient added”; SGA 1 II (4.14).
- [`RingTheory.Sequence.isRegular_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingTheory.Sequence.isRegular_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Sequence/Regular/Basic.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Basic.lean#L96) (StacksFrontier): “its two conditions”.
- [`RingTheory.Sequence.IsWeaklyRegular`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingTheory.Sequence.IsWeaklyRegular#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Sequence/Regular/Basic.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Basic.lean#L97) (StacksFrontier): “condition (1): each `fᵢ` is a nonzerodivisor on the previous quotient”. References: EGA 0 (15.2.2), “special case”; EGA IV (19.5.1); EGA 0 (15.1.7), “M-regular sequence”.
- [`RingTheory.Sequence.isWeaklyRegular_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingTheory.Sequence.isWeaklyRegular_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Sequence/Regular/Basic.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Basic.lean#L102) (StacksFrontier): “condition (1), unfolded”. References: EGA 0 (15.1.7), “M-regular sequence”.

## Tag 00LG, an example

[Tag 00LG](https://stacks.math.columbia.edu/tag/00LG) in the Stacks Project.

**`regularSequence_xyz_one_sub_x`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/Regular/Basic.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Basic.lean#L281). The attribute's comment: “(1)”.

> The sequence `x, y(1-x), z(1-x)` is a regular sequence on `k[x, y, z]`.

```lean
theorem regularSequence_xyz_one_sub_x (k : Type) [Field k] :
    RingTheory.Sequence.IsRegular (mvPolyRingFin3 k)
      ([X 0, X 1 * (1 - X 0), X 2 * (1 - X 0)] : List (mvPolyRingFin3 k))
```

**`not_regularSequence_permuted_xyz_one_sub_x`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/Regular/Basic.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Basic.lean#L295). The attribute's comment: “(2)”.

> The sequence `y(1-x), z(1-x), x` is not a regular sequence on `k[x, y, z]`.

```lean
theorem not_regularSequence_permuted_xyz_one_sub_x (k : Type) [Field k] :
    ¬ RingTheory.Sequence.IsRegular (mvPolyRingFin3 k)
      ([X 1 * (1 - X 0), X 2 * (1 - X 0), X 0] : List (mvPolyRingFin3 k))
```

## Tag 00LJ, a lemma

[Tag 00LJ](https://stacks.math.columbia.edu/tag/00LJ) in the Stacks Project.

Declarations registered for the tag:

- [`IsLocalRing.isRegular_of_perm`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalRing.isRegular_of_perm#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Sequence/Regular/Permutation.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Permutation.lean#L18) (StacksFrontier): “for a Noetherian module over a local ring”.

## Tag 00LM, a lemma

[Tag 00LM](https://stacks.math.columbia.edu/tag/00LM) in the Stacks Project.

**`RingTheory.Sequence.isRegular_map_algebraMap_iff_of_faithfullyFlat_of_isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/BaseChange.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/BaseChange.lean#L155). References: EGA 0 (15.1.14), “converse (ff case)”; EGA 0 (15.2.5), “affine, faithfully flat”; EGA 0 (15.1.13), “special case”; SGA 3 VIIB (5.5.2), “special case”.

> Let `R` be a commutative ring, `M` an `R`-module, `S` a faithfully flat `R`-algebra and
> `f : M →ₗ[R] N` a base change of `M` to `S`. Then a sequence `rs` in `R` is `M`-regular if and
> only if its image in `S` is `N`-regular.

```lean
public theorem isRegular_map_algebraMap_iff_of_faithfullyFlat_of_isBaseChange
    {f : M →ₗ[R] N} (hf : IsBaseChange S f) (rs : List R) :
    IsRegular N (rs.map (algebraMap R S)) ↔ IsRegular M rs
```

## Tag 061L, a lemma

[Tag 061L](https://stacks.math.columbia.edu/tag/061L) in the Stacks Project.

**`regular_sequence_localize_away_of_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/Regular/Basic.lean, line 580](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Basic.lean#L580). References: EGA 0 (15.2.4), “special case”.

> Regularity of a sequence over the localization at a prime spreads out to a localization away
> from some element not in the prime.

```lean
theorem regular_sequence_localize_away_of_atPrime
    {R : Type*} [CommRing R] [IsNoetherianRing R]
    {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (p : Ideal R) [p.IsPrime] (xs : List R)
    (hp : IsRegular (LocalizedModule p.primeCompl M)
      (xs.map (algebraMap R (Localization.AtPrime p)))) :
    ∃ g ∈ p.primeCompl,
      IsRegular (LocalizedModule (Submonoid.powers g) M)
        (xs.map (algebraMap R (Localization.Away g)))
```

## Tag 065K, a lemma

[Tag 065K](https://stacks.math.columbia.edu/tag/065K) in the Stacks Project.

**`Stacks.RingTheory.Sequence.isRegular_append_of_isRegular_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/Regular/Append.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Append.lean#L50).

> Let `f` be a regular sequence in `A` generating the ideal `I`, and let `g` be a list of
> elements of `A` whose images in `A ⧸ I` form a regular sequence. Then `f ++ g` is a regular
> sequence in `A`.

```lean
theorem isRegular_append_of_isRegular_quotient {A : Type*} [CommRing A] {I : Ideal A}
    {f g : List A} (hf : IsRegular A f) (hI : Ideal.ofList f = I)
    (hg : IsRegular (A ⧸ I) (g.map (Ideal.Quotient.mk I))) : IsRegular A (f ++ g)
```

## Tag 0F1T, a lemma

[Tag 0F1T](https://stacks.math.columbia.edu/tag/0F1T) in the Stacks Project.

**`isRegular_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/Regular/Basic.lean, line 670](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Basic.lean#L670).

> Given a short exact sequence `0 → M₁ →[α] M₂ →[β] M₃ → 0` of `R`-modules, if a sequence `rs` of
> elements of `R` is both `M₁`-regular and `M₃`-regular, then it is `M₂`-regular.

```lean
theorem isRegular_of_shortExact {R : Type*} [CommRing R]
    {M₁ M₂ M₃ : Type*} [AddCommGroup M₁] [Module R M₁]
    [AddCommGroup M₂] [Module R M₂] [AddCommGroup M₃] [Module R M₃]
    (α : M₁ →ₗ[R] M₂) (β : M₂ →ₗ[R] M₃)
    (hα : Function.Injective α) (hβ : Function.Surjective β)
    (hexact : LinearMap.range α = LinearMap.ker β)
    (rs : List R)
    (h1 : IsRegular M₁ rs) (h3 : IsRegular M₃ rs) :
    IsRegular M₂ rs
```

## Tag 07DV, a lemma

[Tag 07DV](https://stacks.math.columbia.edu/tag/07DV) in the Stacks Project.

**`RingTheory.Sequence.isRegular_zipWith_pow_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/Powers.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Powers.lean#L302). References: EGA 0 (15.1.20), “first assertion”.

> **Stacks 07DV.** Let `R` be a commutative ring, let `M` be an `R`-module, let
> `rs = [f₁, …, f_r]` be a list of elements of `R` and let `es = [e₁, …, e_r]` be a list of
> positive integers of the same length. Then `f₁ ^ e₁, …, f_r ^ e_r` is an `M`-regular sequence
> if and only if `f₁, …, f_r` is an `M`-regular sequence.

```lean
public theorem RingTheory.Sequence.isRegular_zipWith_pow_iff {R : Type*} [CommRing R]
    (M : Type*) [AddCommGroup M] [Module R M] {rs : List R} {es : List ℕ}
    (hlen : rs.length = es.length) (hes : ∀ e ∈ es, 0 < e) :
    IsRegular M (rs.zipWith (· ^ ·) es) ↔ IsRegular M rs
```

## Tag 07DW, a lemma

[Tag 07DW](https://stacks.math.columbia.edu/tag/07DW) in the Stacks Project.

**`tfae_isRegular_perm_sublist_polySeq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/Regular/Permutation.lean, line 721](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/Regular/Permutation.lean#L721).

> **Stacks Tag 07DW (Lemma 10.68.10).** For `fs = [f_1, …, f_r] : List R` whose entries
> do not generate the unit ideal (`Ideal.span {x | x ∈ fs} ≠ ⊤`, i.e. `(f_1, …, f_r) ≠ R`),
> the three conditions are equivalent. The proof is the 3-cycle `1 → 2 → 3 → 1`:
> `1 → 2` extends a sublist to a permutation; `2 → 3` is `sg_two_to_three` (Stacks 07DV);
> `3 → 1` is `sg_three_to_one` (variable-permutation automorphism + descent).

```lean
theorem tfae_isRegular_perm_sublist_polySeq (fs : List R) (hfs : Ideal.span {x | x ∈ fs} ≠ ⊤) :
    List.TFAE
      [ ∀ l' : List R, l'.Perm fs → IsRegular R l',
        ∀ l' : List R, l' <+ fs → IsRegular R l',
        IsRegular (MvPolynomial (Fin fs.length) R) (polySeq fs) ]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.68, Tag 0AUH](https://stacks.math.columbia.edu/tag/0AUH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

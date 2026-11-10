---
declaration: section
origin: cited
lean: quasiRegularCanonicalMap, RingTheory.Sequence.IsQuasiRegular, Stacks.QuasiregularSequence.isRegular_isQuasiregularSeq, Stacks.QuasiregularSequence.isRegular_isQuasiregularSeq_self, RingTheory.Sequence.IsQuasiRegular.of_flat_of_isBaseChange, RingTheory.Sequence.exists_notMem_isQuasiRegular_away_of_isQuasiRegular_atPrime, RingTheory.Sequence.IsQuasiRegular.quasiRegular_drop_mod_prev, RingTheory.Sequence.IsRegular.of_isQuasiRegular_of_mem_maximalIdeal
statement: formalized
proof: formalized
---

# 10.69 Quasi-regular sequences

Section 10.69 of the Stacks Project, [Tag 061M](https://stacks.math.columbia.edu/tag/061M). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 061N, an equation

[Tag 061N](https://stacks.math.columbia.edu/tag/061N) in the Stacks Project.

**`quasiRegularCanonicalMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/QuasiRegular/Defs.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/QuasiRegular/Defs.lean#L220). References: EGA 0 (15.1.1); EGA 0 (15.1.4); EGA 0 (15.1.5), “special case”; EGA 0 (15.2.1), “special case”; EGA 0 (17.1.1), “more general”; EGA IV (19.5.1); EGA IV (19.5.4), “more general”; EGA IV (19.6.2), “special case”; EGA IV (19.7.1), “special case”.

> **The canonical map** `φ : S → T`, the `(R/J)`-linear map induced by `canonicalBilin`. On a
> monomial generator it sends `X^e ⊗ m̄ ↦ (f^e · m mod J^{|e|+1}M)`.

```lean
noncomputable def quasiRegularCanonicalMap {c : ℕ} (f : Fin c → R) :
    Source M f →ₗ[qrRbar f] Target M f
```

## Tag 061P, a definition

[Tag 061P](https://stacks.math.columbia.edu/tag/061P) in the Stacks Project.

**`RingTheory.Sequence.IsQuasiRegular`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/QuasiRegular/Defs/Defs.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/QuasiRegular/Defs/Defs.lean#L50). References: EGA 0 (15.1.7), “quasi-regular half”; EGA 0 (15.1.4), “M-quasi-regular”; EGA 0 (15.2.2), “special case”; EGA IV (19.5.1); EGA IV (19.5.5.2), “more general”.

> A sequence `rs = f_1, …, f_c` of elements of a commutative ring `R` is **`M`-quasi-regular**,
> for an `R`-module `M`, if the canonical map of graded `(R/J)[X_1, …, X_c]`-modules
> `Φ_M : (R/J)[X_1, …, X_c] ⊗_{R/J} (M/JM) → ⨁_{n ≥ 0} J^n M / J^{n+1} M`,
> `X_1^{e_1} ⋯ X_c^{e_c} ⊗ m̄ ↦ f_1^{e_1} ⋯ f_c^{e_c} m mod J^{e_1 + … + e_c + 1} M`, is an
> isomorphism, where `J = (f_1, …, f_c)`. An `R`-quasi-regular sequence is called simply a
> *quasi-regular sequence*.

```lean
def IsQuasiRegular {R : Type*} [CommRing R] (M : Type*) [AddCommGroup M] [Module R M]
    (rs : List R) : Prop
```

## Tag 00LN, a lemma

[Tag 00LN](https://stacks.math.columbia.edu/tag/00LN) in the Stacks Project.

**`Stacks.QuasiregularSequence.isRegular_isQuasiregularSeq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/RegularIsQuasiRegular.lean, line 900](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/RegularIsQuasiRegular.lean#L900). The attribute's comment: “(2)”. References: EGA 0 (15.1.10), “necessity”; EGA 0 (15.1.9), “first assertion”; EGA IV (19.5.1), “a) ⇒ c)”.

> **Statement 2.** An `M`-regular sequence (Mathlib's `IsRegular`, i.e. the
> full Definition 1 including `M/JM ≠ 0`) is `M`-quasi-regular.
>
> Proved by REVERSE induction (last-element peel) on `rs` via `List.reverseRecOn`,
> using `isQuasiregularSeq_snoc` for the step.

```lean
theorem isRegular_isQuasiregularSeq (M : Type*) [AddCommGroup M] [Module R M] (rs : List R)
    (h : RingTheory.Sequence.IsRegular M rs) : IsQuasiregularSeq rs M
```

**`Stacks.QuasiregularSequence.isRegular_isQuasiregularSeq_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/RegularIsQuasiRegular.lean, line 921](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/RegularIsQuasiRegular.lean#L921). The attribute's comment: “(1)”. References: EGA 0 (15.1.9), “first part, M = R”; EGA IV (19.5.1), “a) ⇒ c) for M = A”.

> **Statement 1.** A regular sequence of `R` (the case `M = R`) is a
> quasi-regular sequence. This is the special case `M = R` of Statement 2.

```lean
theorem isRegular_isQuasiregularSeq_self (rs : List R) (h : RingTheory.Sequence.IsRegular R rs) :
    IsQuasiregularSeq rs R
```

## Tag 065L, a lemma

[Tag 065L](https://stacks.math.columbia.edu/tag/065L) in the Stacks Project.

**`RingTheory.Sequence.IsQuasiRegular.of_flat_of_isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/FlatBaseChangeAndLocalConverse.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/FlatBaseChangeAndLocalConverse.lean#L357).

> **Stacks 065L.** Let `R → S` be a flat ring map, `M` an `R`-module and `rs = f_1, …, f_r` an
> `M`-quasi-regular sequence in `R`. Then the images of `f_1, …, f_r` in `S` form a
> `M ⊗_R S`-quasi-regular sequence, where the base change is taken abstractly: `N` is any
> `S`-module receiving an `R`-linear `f : M →ₗ[R] N` that exhibits it as the base change of `M`.

```lean
public theorem IsQuasiRegular.of_flat_of_isBaseChange {R S M N : Type*} [CommRing R] [CommRing S]
    [Algebra R S] [AddCommGroup M] [Module R M] [AddCommGroup N] [Module R N] [Module S N]
    [IsScalarTower R S N] [Module.Flat R S] {f : M →ₗ[R] N} (hf : IsBaseChange S f) {rs : List R}
    (reg : IsQuasiRegular M rs) : IsQuasiRegular N (rs.map (algebraMap R S))
```

## Tag 061Q, a lemma

[Tag 061Q](https://stacks.math.columbia.edu/tag/061Q) in the Stacks Project.

**`RingTheory.Sequence.exists_notMem_isQuasiRegular_away_of_isQuasiRegular_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/SpreadToStandardOpen.lean, line 502](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/SpreadToStandardOpen.lean#L502).

> **Stacks 061Q.** Let `R` be a Noetherian ring, `M` a finite `R`-module, `𝔭 ⊂ R` a prime and
> `rs = x₁, …, x_c` a sequence of elements of `R` whose image in `R_𝔭` is `M_𝔭`-quasi-regular. Then
> there is a `g ∈ R`, `g ∉ 𝔭`, such that the image of `rs` in `R_g` is `M_g`-quasi-regular.

```lean
public theorem exists_notMem_isQuasiRegular_away_of_isQuasiRegular_atPrime {R : Type*} [CommRing R]
    [IsNoetherianRing R] {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (p : Ideal R) [p.IsPrime] (rs : List R) (Rₚ : Type*) [CommRing Rₚ] [Algebra R Rₚ]
    [IsLocalization.AtPrime Rₚ p] (Mₚ : Type*) [AddCommGroup Mₚ] [Module R Mₚ] [Module Rₚ Mₚ]
    [IsScalarTower R Rₚ Mₚ] (fₚ : M →ₗ[R] Mₚ) [IsLocalizedModule p.primeCompl fₚ]
    (hp : IsQuasiRegular Mₚ (rs.map (algebraMap R Rₚ))) :
    ∃ g ∉ p,
      ∀ (Rg : Type*) [CommRing Rg] [Algebra R Rg] [IsLocalization.Away g Rg] (Mg : Type*)
        [AddCommGroup Mg] [Module R Mg] [Module Rg Mg] [IsScalarTower R Rg Mg] (fg : M →ₗ[R] Mg)
        [IsLocalizedModule (Submonoid.powers g) fg],
        IsQuasiRegular Mg (rs.map (algebraMap R Rg))
```

## Tag 061R, a lemma

[Tag 061R](https://stacks.math.columbia.edu/tag/061R) in the Stacks Project.

**`RingTheory.Sequence.IsQuasiRegular.quasiRegular_drop_mod_prev`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/QuotientByPrefix.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/QuotientByPrefix.lean#L554).

> **Stacks 061R.** Let `M` be a module over a commutative ring `R` and let `rs = f_1, …, f_c` be
> an `M`-quasi-regular sequence in `R`. For any `i`, the images `f̄_{i+1}, …, f̄_c` of the remaining
> elements in `R̄ = R/(f_1, …, f_i)` form an `M̄`-quasi-regular sequence, where
> `M̄ = M/(f_1, …, f_i)M`.

```lean
public theorem IsQuasiRegular.quasiRegular_drop_mod_prev {R M : Type*} [CommRing R]
    [AddCommGroup M] [Module R M] {rs : List R} (reg : IsQuasiRegular M rs) (i : ℕ) :
    IsQuasiRegular (M ⧸ (Ideal.ofList (rs.take i) • ⊤ : Submodule R M))
      ((rs.drop i).map (Ideal.Quotient.mk (Ideal.ofList (rs.take i))))
```

## Tag 061S, a lemma

[Tag 061S](https://stacks.math.columbia.edu/tag/061S) in the Stacks Project.

**`RingTheory.Sequence.IsRegular.of_isQuasiRegular_of_mem_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/FlatBaseChangeAndLocalConverse.lean, line 708](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/QuasiRegular/Basic/FlatBaseChangeAndLocalConverse.lean#L708). References: EGA 0 (15.1.9), “converse, local”; EGA 0 (15.1.11), “converse, local case”; EGA 0 (15.2.2), “converse: q-reg ⇒ reg”; EGA IV (16.9.11), “local Noetherian ring”; EGA 0 (15.1.10), “sufficiency”; EGA 0 (15.1.3), “partial”; EGA IV (16.9.12), “parenthetical”; EGA IV (19.5.1), “special case”.

> **Stacks 061S.** Let `(R, 𝔪)` be a local Noetherian ring and let `M` be a nonzero finite
> `R`-module. An `M`-quasi-regular sequence `f_1, …, f_c` of elements of `𝔪` is an `M`-regular
> sequence.

```lean
public theorem IsRegular.of_isQuasiRegular_of_mem_maximalIdeal {R M : Type*} [CommRing R]
    [IsLocalRing R] [IsNoetherianRing R] [AddCommGroup M] [Module R M] [Nontrivial M]
    [Module.Finite R M] {rs : List R} (mem : ∀ r ∈ rs, r ∈ IsLocalRing.maximalIdeal R)
    (reg : IsQuasiRegular M rs) : IsRegular M rs
```

## Tag 065N, a lemma

[Tag 065N](https://stacks.math.columbia.edu/tag/065N) in the Stacks Project.

**`isMQuasiregular_iff_isMQuasiregular_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Sequence/QuasiRegular/Graded.lean, line 704](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Sequence/QuasiRegular/Graded.lean#L704).

> **Theorem (Stacks Tag 065N, Lemma 10.69.9).**
> The sequence `f_1, ..., f_r` is `M`-quasi-regular (over `R`, with respect to `M`)
> if and only if the image sequence `f̄_1, ..., f̄_r` is `M̄`-quasi-regular (over
> `R̄ = R / I_R`, with respect to `M̄ = M / I_M`).

```lean
theorem isMQuasiregular_iff_isMQuasiregular_quotient {c : ℕ} (f : Fin c → R) :
    letI := mbarModule (M := M) f
    IsMQuasiregular (M := M) f ↔
      IsMQuasiregular (R := Rbar f) (M := Mbar (M := M) f) (fbar f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.69, Tag 061M](https://stacks.math.columbia.edu/tag/061M)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: support_eq_iUnion_zeroLocus, mem_support_of_isQuotientEquivQuotientPrime_series, support_point, main_theorem_00l6, Module.setOf_minimal_range_eq_setOf_minimal_support_and_ncard_eq_length, Module.hilbertSamuelDegree_eq_supportDim, Module.supportDim_of_exact
statement: formalized
proof: formalized
---

# 10.62 Support and dimension of modules

Section 10.62 of the Stacks Project, [Tag 00KY](https://stacks.math.columbia.edu/tag/00KY). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00L4, a lemma

[Tag 00L4](https://stacks.math.columbia.edu/tag/00L4) in the Stacks Project.

**`support_eq_iUnion_zeroLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Support/Finite.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Support/Finite.lean#L140).

> **Stacks 00L4, main statement.** With the filtration data of Stacks 00L0,
> the support of `M` is the union of the closed sets `V(𝔭ᵢ)`.

```lean
theorem support_eq_iUnion_zeroLocus
    (A : Type*) [CommRing A] (M : Type*) [AddCommGroup M] [Module A M]
    [IsNoetherianRing A] [Module.Finite A M]
    (s : RelSeries {(N₁, N₂) : Submodule A M × Submodule A M |
          N₁.IsQuotientEquivQuotientPrime N₂})
    (hhead : s.head = ⊥) (hlast : s.last = ⊤)
    (p : Fin s.length → PrimeSpectrum A)
    (hp : ∀ i : Fin s.length,
      Nonempty (((s.toFun i.succ) ⧸ (s.toFun i.castSucc).submoduleOf (s.toFun i.succ))
        ≃ₗ[A] A ⧸ (p i).asIdeal)) :
    Module.support A M
      = ⋃ i : Fin s.length, PrimeSpectrum.zeroLocus ((p i).asIdeal : Set A)
```

**`mem_support_of_isQuotientEquivQuotientPrime_series`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Support/Finite.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Support/Finite.lean#L161).

> **Stacks 00L4, "in particular".** Each prime `𝔭ᵢ` lies in the support of
> `M`.

```lean
theorem mem_support_of_isQuotientEquivQuotientPrime_series
    (A : Type*) [CommRing A] (M : Type*) [AddCommGroup M] [Module A M]
    [IsNoetherianRing A] [Module.Finite A M]
    (s : RelSeries {(N₁, N₂) : Submodule A M × Submodule A M |
          N₁.IsQuotientEquivQuotientPrime N₂})
    (hhead : s.head = ⊥) (hlast : s.last = ⊤)
    (p : Fin s.length → PrimeSpectrum A)
    (hp : ∀ i : Fin s.length,
      Nonempty (((s.toFun i.succ) ⧸ (s.toFun i.castSucc).submoduleOf (s.toFun i.succ))
        ≃ₗ[A] A ⧸ (p i).asIdeal)) :
    ∀ i : Fin s.length, p i ∈ Module.support A M
```

## Tag 00L5, a lemma

[Tag 00L5](https://stacks.math.columbia.edu/tag/00L5) in the Stacks Project.

**`support_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Support/Finite.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Support/Finite.lean#L328). References: EGA 0 (16.1.10), “local ring case”; EGA IV (4.7.7), “special case”; SGA 6 X (1.1.2), “special case”.

> Stacks 00L5. Over a Noetherian local ring `R` with maximal ideal `m`, a nonzero
> finite `R`-module `M` has support equal to the singleton `{m}` if and only if `M`
> has finite length over `R`.

```lean
theorem support_point {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M] [Nontrivial M] :
    Module.support R M = {IsLocalRing.closedPoint R} ↔ IsFiniteLength R M
```

## Tag 00L6, a lemma

[Tag 00L6](https://stacks.math.columbia.edu/tag/00L6) in the Stacks Project.

**`main_theorem_00l6`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Support/Finite.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Support/Finite.lean#L354). References: EGA I (9.3.4), “affine case”.

> For a finite module `M` over a Noetherian ring `R` and an ideal `I ⊆ R`,
> some power of `I` annihilates `M` if and only if the support of `M` is contained
> in the zero locus of `I`.

```lean
theorem main_theorem_00l6 {R : Type*} {M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    [IsNoetherianRing R] [Module.Finite R M] (I : Ideal R) :
    (∃ n : ℕ, (I ^ n) • (⊤ : Submodule R M) = ⊥) ↔
      Module.support R M ⊆ PrimeSpectrum.zeroLocus (I : Set R)
```

## Tag 00L7, a lemma

[Tag 00L7](https://stacks.math.columbia.edu/tag/00L7) in the Stacks Project.

**`Module.setOf_minimal_range_eq_setOf_minimal_support_and_ncard_eq_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/Additivity.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Additivity.lean#L417).

> **Stacks 00L7**.
> Let `R` be a ring, `M` an `R`-module, and let `0 = N₀ ⊆ N₁ ⊆ ⋯ ⊆ Nₙ = M` be a filtration whose
> successive quotients are `Nᵢ₊₁ ⧸ Nᵢ ≅ R ⧸ 𝔭ᵢ` for primes `𝔭ᵢ = p i` of `R`, as produced by
> Stacks 00L0. Then the minimal elements of the set `{𝔭ᵢ}` are exactly the minimal elements of
> `Supp(M)`, and each minimal `𝔭 ∈ Supp(M)` occurs among the `𝔭ᵢ` exactly
> `length_{R_𝔭} M_𝔭` times.

```lean
public theorem setOf_minimal_range_eq_setOf_minimal_support_and_ncard_eq_length {R M : Type*}
    [CommRing R] [AddCommGroup M] [Module R M] {n : ℕ} (N : Fin (n + 1) → Submodule R M)
    (p : Fin n → PrimeSpectrum R) (hle : ∀ i : Fin n, N i.castSucc ≤ N i.succ)
    (hquot : ∀ i : Fin n,
      Nonempty ((↥(N i.succ) ⧸ (N i.castSucc).submoduleOf (N i.succ)) ≃ₗ[R] R ⧸ (p i).asIdeal))
    (hbot : N 0 = ⊥) (htop : N (Fin.last n) = ⊤) :
    {q | Minimal (· ∈ Set.range p) q} = {q | Minimal (· ∈ Module.support R M) q} ∧
      ∀ q : PrimeSpectrum R, Minimal (· ∈ Module.support R M) q →
        ({i | p i = q}.ncard : ℕ∞) =
          Module.length (Localization.AtPrime q.asIdeal)
            (LocalizedModule q.asIdeal.primeCompl M)
```

## Tag 00L8, a lemma

[Tag 00L8](https://stacks.math.columbia.edu/tag/00L8) in the Stacks Project.

**`Module.hilbertSamuelDegree_eq_supportDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/HilbertSamuel/Dimension.lean, line 310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/HilbertSamuel/Dimension.lean#L310). References: EGA 0 (16.2.3), “special case”.

> **Stacks 00L8**.
> Let `R` be a Noetherian local ring and let `M` be a finite `R`-module. Then the Hilbert–Samuel
> degree `d(M)` of Definition 00KA equals the dimension of the support of `M`, that is, the Krull
> dimension of `Supp(M) ⊆ Spec(R)`.
>
> The equation is stated in `WithBot ℕ∞`, where `dim Supp(M)` lives, with `d(M) : WithBot ℕ`
> transported along the order embedding `WithBot.map (Nat.cast : ℕ → ℕ∞)`; it therefore also
> asserts that `dim Supp(M)` is finite. Both sides are `⊥ = -∞` exactly when `M = 0`.

```lean
public theorem hilbertSamuelDegree_eq_supportDim (R : Type*) [CommRing R] [IsNoetherianRing R]
    [IsLocalRing R] (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    (hilbertSamuelDegree R M).map (Nat.cast : ℕ → ℕ∞) = supportDim R M
```

## Tag 0B51, a lemma

[Tag 0B51](https://stacks.math.columbia.edu/tag/0B51) in the Stacks Project.

**`Module.supportDim_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/Module.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/KrullDimension/Module.lean#L222).

> **Stacks 0B51**.
> Let `R` be a commutative ring and let `0 → M → N → P → 0` be a short exact sequence of
> `R`-modules, given by `f : M →ₗ[R] N` injective, `g : N →ₗ[R] P` surjective and
> `Function.Exact f g`. Then `dim Supp(N) = max (dim Supp(M)) (dim Supp(P))`.
>
> The source assumes `R` Noetherian and the three modules finite; neither hypothesis is needed
> for this formulation of the dimension of the support.

```lean
public theorem supportDim_of_exact {R M N P : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    [AddCommGroup N] [Module R N] [AddCommGroup P] [Module R P] {f : M →ₗ[R] N} {g : N →ₗ[R] P}
    (h : Function.Exact f g) (hf : Function.Injective f) (hg : Function.Surjective g) :
    supportDim R N = max (supportDim R M) (supportDim R P)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.62, Tag 00KY](https://stacks.math.columbia.edu/tag/00KY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

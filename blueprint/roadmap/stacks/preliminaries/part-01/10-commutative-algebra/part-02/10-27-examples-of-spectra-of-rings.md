---
declaration: section
origin: cited
lean: IntXSqSubFour.isPrime_iff, Polynomial.isPrime_int_trichotomy, Polynomial.isPrime_iff_eq_bot_or_eq_span_or_eq_span_pair, NodalCubicAffineOpen.quotientSpanAlgEquiv, NodalCubicAffineOpen.isOpenEmbedding_comap_inclRToRa, NodalCubicAffineOpen.range_comap_inclRToRa, NodalCubicAffineOpen.range_comap_inclRToRa_ne_basicOpen, NodalCubicAffineOpen.not_exists_isLocalization
statement: formalized
proof: formalized
---

# 10.27 Examples of spectra of rings

Section 10.27 of the Stacks Project, [Tag 00EX](https://stacks.math.columbia.edu/tag/00EX). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00EY, an example

[Tag 00EY](https://stacks.math.columbia.edu/tag/00EY) in the Stacks Project.

**`IntXSqSubFour.isPrime_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean#L178).

> **Classification of `Spec(R)` (Stacks Tag 00EY).**
> An ideal `p` of `R = ℤ[x]/(x² - 4)` is prime if and only if it is one of the
> listed ideals: `(2, x̄)`, or `(q, x̄ - 2)`/`(q, x̄ + 2)` for some odd prime `q`,
> or one of the two generic primes `(x̄ - 2)`, `(x̄ + 2)`.
>
> A prime contains `x̄ - 2` or `x̄ + 2`, since their product is `0`. The evaluations
> `R → ℤ`, `x̄ ↦ ±2`, are surjective with kernels `(x̄ ∓ 2)`, so the primes containing
> `x̄ ∓ 2` are the preimages of the primes `(0)` and `(q)` of `ℤ`; for `q = 2` both
> preimages are `(2, x̄)`.

```lean
theorem isPrime_iff (p : Ideal IntXSqSubFour) :
    p.IsPrime ↔
      (p = p2 ∨
       (∃ q : ℕ, q.Prime ∧ Odd q ∧ (p = pMinus q ∨ p = pPlus q)) ∨
       p = gMinus ∨ p = gPlus)
```

## Tag 00EZ, an example

[Tag 00EZ](https://stacks.math.columbia.edu/tag/00EZ) in the Stacks Project.

**`Polynomial.isPrime_int_trichotomy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean#L303).

> **Stacks Tag 00EZ** (Description of `Spec(ℤ[x])`).
>
> Every prime ideal `𝔭` of `ℤ[x]` has one of the following forms:
> * `𝔭 = (0)`;
> * `𝔭 = (f)` with `f` irreducible in `ℤ[x]`; this covers the nonzero primes with
>   `𝔭 ∩ ℤ = (0)` and the primes `(q)` (take `f = q`) for a prime number `q`;
> * `𝔭 = (q, f)` for a prime number `q` and `f` irreducible in `ℤ[x]` whose reduction modulo `q`
>   is irreducible in `(ℤ/qℤ)[x]`.
>
> The Stacks text omits the primes `(q)`, which lie over `(q)` without being of the third form.

```lean
theorem Polynomial.isPrime_int_trichotomy
    (𝔭 : Ideal ℤ[X]) (h𝔭 : 𝔭.IsPrime) :
    𝔭 = ⊥ ∨
    (∃ f : ℤ[X], Irreducible f ∧ 𝔭 = Ideal.span {f}) ∨
    (∃ (q : ℕ) (f : ℤ[X]), q.Prime ∧
        Irreducible f ∧
        Irreducible (f.map (Int.castRingHom (ZMod q))) ∧
        𝔭 = Ideal.span {(C (q : ℤ)), f})
```

## Tag 00F0, an example

[Tag 00F0](https://stacks.math.columbia.edu/tag/00F0) in the Stacks Project.

**`Polynomial.isPrime_iff_eq_bot_or_eq_span_or_eq_span_pair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Polynomial.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Polynomial.lean#L312). The attribute's comment: “for `R[X]` over any principal ideal domain `R`; the tag is the case `R = k[x]`”.

> **Stacks 00F0**, both directions: the prime ideals of `R[X]`, for `R` a principal ideal
> domain. The tag is the case `R = k[x]` for a field `k`.

```lean
theorem isPrime_iff_eq_bot_or_eq_span_or_eq_span_pair [IsDomain R] [IsPrincipalIdealRing R]
    (P : Ideal R[X]) :
    P.IsPrime ↔ P = ⊥ ∨ (∃ f : R[X], Irreducible f ∧ P = span {f}) ∨
      (∃ (p : R) (f : R[X]), Irreducible p ∧
        Irreducible (Ideal.Quotient.mk (span {C p}) f) ∧ P = span {C p, f})
```

## Tag 00F1, an example

[Tag 00F1](https://stacks.math.columbia.edu/tag/00F1) in the Stacks Project.

**`NodalCubicAffineOpen.quotientSpanAlgEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean, line 615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean#L615). The attribute's comment: “`R ≅ ℚ[A, B]/(A³ - B² + AB)`”.

> The isomorphism `ℚ[A, B] / (A³ - B² + A·B) ≃ₐ[ℚ] R` induced by `φ`.

```lean
def quotientSpanAlgEquiv :
    (MvPolynomial (Fin 2) ℚ ⧸ Ideal.span {((MvPolynomial.X 0 : MvPolynomial (Fin 2) ℚ) ^ 3 -
      MvPolynomial.X 1 ^ 2 + MvPolynomial.X 0 * MvPolynomial.X 1)}) ≃ₐ[ℚ] R
```

**`NodalCubicAffineOpen.isOpenEmbedding_comap_inclRToRa`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean, line 792](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean#L792). The attribute's comment: “`θ : Spec R_a → Spec R` is an open embedding”.

> The inclusion `R ↪ R_a` induces an open embedding
> `θ : Spec R_a → Spec R`.

```lean
theorem isOpenEmbedding_comap_inclRToRa (a : ℚ)
    (ha0 : a ≠ 0) (ha1 : a ≠ 1) :
    Topology.IsOpenEmbedding
      (PrimeSpectrum.comap (inclRToRa a ha0 ha1).toRingHom)
```

**`NodalCubicAffineOpen.range_comap_inclRToRa`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean, line 806](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean#L806). The attribute's comment: “the image of `θ` is `Spec R ∖ {𝔪_a}`”.

> The image of `θ : Spec R_a → Spec R` is exactly the complement of the
> closed point `𝔪_a` in `Spec R`.

```lean
theorem range_comap_inclRToRa (a : ℚ)
    (ha0 : a ≠ 0) (ha1 : a ≠ 1) :
    Set.range (PrimeSpectrum.comap (inclRToRa a ha0 ha1).toRingHom) =
      {p : PrimeSpectrum R | p ≠ mRPoint a}
```

**`NodalCubicAffineOpen.range_comap_inclRToRa_ne_basicOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean, line 847](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean#L847).

> **Headline.** The image of `θ : Spec R_a → Spec R` is **not** the basic
> open `D(f)` of any element `f ∈ R`. Hence `Spec R_a ⊂ Spec R` is an affine
> open which is not standard / principal.

```lean
theorem range_comap_inclRToRa_ne_basicOpen (a : ℚ)
    (ha0 : a ≠ 0) (ha1 : a ≠ 1) (ha12 : a ≠ 1 / 2) (f : R) :
    Set.range (PrimeSpectrum.comap (inclRToRa a ha0 ha1).toRingHom) ≠
      (PrimeSpectrum.basicOpen f : Set (PrimeSpectrum R))
```

**`NodalCubicAffineOpen.not_exists_isLocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean, line 892](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Examples.lean#L892). The attribute's comment: “`R_a` is not a localization of `R`”.

> `R_a` is **not** a localization of `R`: there is no submonoid `S ⊆ R`
> for which `R_a` becomes the localization `S⁻¹ R` via `inclRToRa`.

```lean
theorem not_exists_isLocalization (a : ℚ)
    (ha0 : a ≠ 0) (ha1 : a ≠ 1) (ha12 : a ≠ 1 / 2) :
    let _ : Algebra R (Ra a ha0 ha1) := (inclRToRa a ha0 ha1).toAlgebra
    ¬ ∃ (S : Submonoid R), IsLocalization S (Ra a ha0 ha1)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.27, Tag 00EX](https://stacks.math.columbia.edu/tag/00EX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: section
origin: cited
lean: IsLocalizedModule.Away.injective_pi_and_exact_of_span_range_eq_top, alphaLin_injective, ker_betaLin_eq_range_alphaLin, PrimeSpectrum.exists_ringEquiv_prod_of_isOpen_of_isCompl, bigLambda_injective_iff_bigPhi_injective, ModuleGluingData.psi_apply_of_mem_gluedModule, ModuleGluingData.proj_isLocalizedModule
statement: formalized
proof: formalized
---

# 10.24 Glueing functions

Section 10.24 of the Stacks Project, [Tag 00EI](https://stacks.math.columbia.edu/tag/00EI). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00EK, a lemma

[Tag 00EK](https://stacks.math.columbia.edu/tag/00EK) in the Stacks Project.

**`IsLocalizedModule.Away.injective_pi_and_exact_of_span_range_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Module/Localization/Exactness.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/Localization/Exactness.lean#L294).

> Let `R` be a commutative semiring, let `f : ι → R` be a family of elements generating the unit
> ideal and let `M` be an `R`-module. Let `Mf i` be the localization of `M` away from `f i`, with
> localization map `g i`, and let `Mff i j` be the localization of `M` away from `f i * f j`,
> reached from `Mf i` by `l i j` and from `Mf j` by `r i j`. Then the sequence
> `0 → M → ∏ i, Mf i → ∏ (i, j), Mff i j`
> is exact, the first map being `m ↦ (g i m)` and the second
> `(m i) ↦ (l i j (m i) - r i j (m j))`.

```lean
public theorem injective_pi_and_exact_of_span_range_eq_top
    (hf : Ideal.span (Set.range f) = ⊤)
    (hlr : ∀ i j, (l i j).comp (g i) = (r i j).comp (g j)) :
    Function.Injective (LinearMap.pi g) ∧
      Function.Exact (LinearMap.pi g) (LinearMap.pi fun p : ι × ι ↦
        (l p.1 p.2).comp (LinearMap.proj p.1) - (r p.1 p.2).comp (LinearMap.proj p.2))
```

## Tag 00EJ, a lemma

[Tag 00EJ](https://stacks.math.columbia.edu/tag/00EJ) in the Stacks Project.

**`alphaLin_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/Functions.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/Functions.lean#L125). The attribute's comment: “exactness at `R`, i.e. injectivity of `α`”.

> If `f` generates the unit ideal, then `α` is injective.

```lean
theorem alphaLin_injective (hf : Ideal.span (Set.range f) = ⊤) :
    Function.Injective (alphaLin R n f)
```

**`ker_betaLin_eq_range_alphaLin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/Functions.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/Functions.lean#L234). The attribute's comment: “exactness at the middle term, i.e. `ker β = im α`”.

> If `f` generates the unit ideal, then the kernel of `β` equals the range of `α`.

```lean
theorem ker_betaLin_eq_range_alphaLin (hf : Ideal.span (Set.range f) = ⊤) :
    LinearMap.ker (betaLin R n f) = LinearMap.range (alphaLin R n f)
```

## Tag 00EM, a lemma

[Tag 00EM](https://stacks.math.columbia.edu/tag/00EM) in the Stacks Project.

**`PrimeSpectrum.exists_ringEquiv_prod_of_isOpen_of_isCompl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/ConnectedComponents.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/ConnectedComponents.lean#L538).

> A disjoint open cover of `Spec R` yields a product decomposition of `R`.
>
> Let `R` be a commutative ring with `Spec(R) = U ⊔ V` for two open subsets `U, V`.
> Then there is an idempotent `e ∈ R` such that, setting `R₁ := R⧸(1-e)` and
> `R₂ := R⧸e`:
>
> * the canonical ring map `φ := RingHom.quotientProdOneSub e : R →+* R₁ × R₂` lifts to a
>   ring isomorphism `R ≃+* R₁ × R₂`;
> * `Spec(R₁)` is homeomorphic to `U` (as a subspace of `Spec R`) and `Spec(R₂)`
>   is homeomorphic to `V`, with both homeomorphisms realised by the canonical maps
>   of the product decomposition, i.e. via `PrimeSpectrum.primeSpectrumProdHomeo`;
> * each factor is simultaneously a quotient and a localization of `R`:
>   the quotient maps make `R₁` a localization at `e` and `R₂` a localization at `1 - e`.

```lean
theorem PrimeSpectrum.exists_ringEquiv_prod_of_isOpen_of_isCompl
    {R : Type*} [CommRing R]
    {U V : Set (PrimeSpectrum R)}
    (hU : IsOpen U) (hV : IsOpen V)
    (h : IsCompl U V) :
    ∃ e : R, IsIdempotentElem e ∧
      ∃ φ : R ≃+* (R ⧸ Ideal.span ({1 - e} : Set R)) ×
                  (R ⧸ Ideal.span ({e} : Set R)),
        (φ : R →+* (R ⧸ Ideal.span ({1 - e} : Set R)) ×
                   (R ⧸ Ideal.span ({e} : Set R))) = RingHom.quotientProdOneSub e ∧
        (∃ eU : PrimeSpectrum (R ⧸ Ideal.span ({1 - e} : Set R)) ≃ₜ U,
          ∀ p, (eU p).1 =
            PrimeSpectrum.comap
              (φ : R →+* (R ⧸ Ideal.span ({1 - e} : Set R)) ×
                         (R ⧸ Ideal.span ({e} : Set R)))
              (PrimeSpectrum.primeSpectrumProdHomeo.symm (Sum.inl p))) ∧
        (∃ eV : PrimeSpectrum (R ⧸ Ideal.span ({e} : Set R)) ≃ₜ V,
          ∀ p, (eV p).1 =
            PrimeSpectrum.comap
              (φ : R →+* (R ⧸ Ideal.span ({1 - e} : Set R)) ×
                         (R ⧸ Ideal.span ({e} : Set R)))
              (PrimeSpectrum.primeSpectrumProdHomeo.symm (Sum.inr p))) ∧
        IsLocalization.Away e (R ⧸ Ideal.span ({1 - e} : Set R)) ∧
        IsLocalization.Away (1 - e) (R ⧸ Ideal.span ({e} : Set R))
```

## Tag 0565, a lemma

[Tag 0565](https://stacks.math.columbia.edu/tag/0565) in the Stacks Project.

**`bigLambda_injective_iff_bigPhi_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/Functions.lean, line 429](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/Functions.lean#L429).

> The map `Λ : M → ⨁_i M_{f_i}`, `m ↦ (m/1, ..., m/1)`,
> is injective if and only if the map `Φ : M → ⨁_i M`, `m ↦ (f_1 m, ..., f_n m)`, is
> injective.

```lean
theorem bigLambda_injective_iff_bigPhi_injective
    (n : ℕ) (f : Fin n → R) :
    Function.Injective (bigLambda (M := M) n f) ↔ Function.Injective (bigPhi (M := M) n f)
```

## Tag 00EQ, a lemma

[Tag 00EQ](https://stacks.math.columbia.edu/tag/00EQ) in the Stacks Project.

**`ModuleGluingData.psi_apply_of_mem_gluedModule`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/Modules.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/Modules.lean#L272). The attribute's comment: “moreover clause: `ψ i j (m/1) = m/1` for `m` in the glued module”.

> For `m ∈ gluedModule`, the gluing relation holds: `ψ i j (m_i/1) = m_j/1`.

```lean
lemma psi_apply_of_mem_gluedModule
    (D : ModuleGluingData ι f) (m : D.gluedModule) (i j : ι) :
    D.ψ i j (LocalizedModule.mkLinearMap (Submonoid.powers (f j))
              (D.M i) ((m : D.DirectSumM) i)) =
      LocalizedModule.mkLinearMap (Submonoid.powers (f i)) (D.M j) ((m : D.DirectSumM) j)
```

**`ModuleGluingData.proj_isLocalizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/Glueing/Modules.lean, line 452](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/Glueing/Modules.lean#L452). The attribute's comment: “localization comparison”.

> **Stacks 00EQ (localization comparison).** For finite module gluing data, projection to the
> `i`-th component is the localization map at the powers of `f i`. Thus the induced canonical map
> from the localization of the glued module to `D.M i` is an isomorphism.

```lean
theorem proj_isLocalizedModule (D : ModuleGluingData ι f) (i : ι) :
    IsLocalizedModule (Submonoid.powers (f i)) (D.proj i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.24, Tag 00EI](https://stacks.math.columbia.edu/tag/00EI)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)

---
declaration: module
origin: cited
lean: CondensedMatter.FiniteBloch.hopping, CondensedMatter.FiniteBloch.hopping_apply, CondensedMatter.FiniteBloch.bloch, CondensedMatter.FiniteBloch.fourier, CondensedMatter.FiniteBloch.fourier_hopping, CondensedMatter.FiniteBloch.mem_spectrum_iff_exists, CondensedMatter.FiniteBloch.mem_spectrum_matrix_iff, CondensedMatter.FiniteBloch.fourier_smul
statement: formalized
proof: formalized
---

# The spectrum of a finite periodic crystal

The module `PhyslibAlpha.CondensedMatter.Bloch.FiniteBloch`, [PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean): 12 declarations, 10 with a docstring.

> The spectrum of a translation-invariant operator on a finite periodic crystal is the union of the
> spectra of its Bloch matrices.

## i. Overview

> A finite periodic crystal has a finite abelian translation group `G`, for instance `(ℤ / mℤ) ^ d`,
> and `N` orbitals in each cell. A configuration is a function `ψ : G → ℂ ^ N`, and a hopping
> operator `(B ψ) x = ∑_r A_r ψ (x - r)` moves amplitude by the lattice vector `r` through the
> matrix `A_r`. A plane wave `x ↦ χ(x) v` of crystal momentum `χ`, a character of `G`, is mapped to
> `χ(x) b(χ) v`, where `b(χ) = ∑_r χ(-r) A_r` is the Bloch matrix. So an eigenvector of `b(χ)`
> gives an eigenvector of `B` with the same eigenvalue. Conversely, the Fourier transform
> `ψ̂(χ) = ∑_x χ(-x) ψ(x)` of an eigenvector of `B` satisfies `b(χ) ψ̂(χ) = λ ψ̂(χ)`, and a
> nonzero function has a nonzero Fourier transform at some momentum, by orthogonality of the
> characters. Hence `spec B = ⋃_χ spec b(χ)`, with no analysis: the space is finite dimensional.
>
> For the infinite lattice `ℤ ^ d` the same statement holds on `ℓ²`, where the Fourier transform is
> a unitary map onto `L²` of the Brillouin zone, and is proved in `RegularRep.spectrum_blochOperator`.

## ii. Key results

> - `FiniteBloch.hopping` : the hopping operator with matrices `A_r`.
> - `FiniteBloch.bloch` : its Bloch matrix at a crystal momentum.
> - `FiniteBloch.fourier_hopping` : the Fourier transform intertwines the operator with its Bloch
>   matrix.
> - `FiniteBloch.spectrum_hopping` : the spectrum is the union of the spectra of the Bloch matrices.

## iv. References

> * F. Bloch, Über die Quantenmechanik der Elektronen in Kristallgittern, Z. Phys. 52 (1929). [ref:
>   bloch\_1929]
> * N. Ashcroft & N. D. Mermin, Solid State Physics, Chapters 4 and 8.

## A. The hopping operator and its Bloch matrix

**`CondensedMatter.FiniteBloch.hopping`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L68).

> The hopping operator `(B ψ) x = ∑_r A_r ψ (x - r)` on configurations of a finite periodic
> crystal.

```lean
def hopping (A : G → Matrix (Fin N) (Fin N) ℂ) :
    (G → Fin N → ℂ) →ₗ[ℂ] (G → Fin N → ℂ)
```

**`CondensedMatter.FiniteBloch.hopping_apply`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L79).

```lean
lemma hopping_apply (A : G → Matrix (Fin N) (Fin N) ℂ) (ψ : G → Fin N → ℂ) (x : G) :
    hopping A ψ x = ∑ r, (A r).mulVec (ψ (x - r))
```

**`CondensedMatter.FiniteBloch.bloch`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L83).

> The Bloch matrix `b(χ) = ∑_r χ(-r) A_r` of a hopping operator.

```lean
def bloch (A : G → Matrix (Fin N) (Fin N) ℂ) (χ : AddChar G ℂ) : Matrix (Fin N) (Fin N) ℂ
```

**`CondensedMatter.FiniteBloch.fourier`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L87).

> The Fourier transform `ψ̂(χ) = ∑_x χ(-x) ψ(x)` of a configuration.

```lean
def fourier (χ : AddChar G ℂ) (ψ : G → Fin N → ℂ) : Fin N → ℂ
```

**`CondensedMatter.FiniteBloch.fourier_hopping`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L92).

> **Bloch's theorem on a finite crystal.** The Fourier transform of `B ψ` at momentum `χ` is
> the Bloch matrix applied to the Fourier transform of `ψ`.

```lean
lemma fourier_hopping (A : G → Matrix (Fin N) (Fin N) ℂ) (χ : AddChar G ℂ)
    (ψ : G → Fin N → ℂ) : fourier χ (hopping A ψ) = (bloch A χ).mulVec (fourier χ ψ)
```

## B. The spectrum

**`CondensedMatter.FiniteBloch.mem_spectrum_iff_exists`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L107).

> An eigenvalue of an operator on a finite-dimensional space is a point of its spectrum.

```lean
lemma mem_spectrum_iff_exists {V : Type*} [AddCommGroup V] [Module ℂ V] [FiniteDimensional ℂ V]
    (f : Module.End ℂ V) (μ : ℂ) : μ ∈ spectrum ℂ f ↔ ∃ v, v ≠ 0 ∧ f v = μ • v
```

**`CondensedMatter.FiniteBloch.mem_spectrum_matrix_iff`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L118).

> A complex number is in the spectrum of a matrix exactly when it has an eigenvector.

```lean
lemma mem_spectrum_matrix_iff (M : Matrix (Fin N) (Fin N) ℂ) (μ : ℂ) :
    μ ∈ spectrum ℂ M ↔ ∃ v : Fin N → ℂ, v ≠ 0 ∧ M.mulVec v = μ • v
```

**`CondensedMatter.FiniteBloch.fourier_smul`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L125).

```lean
lemma fourier_smul (χ : AddChar G ℂ) (c : ℂ) (ψ : G → Fin N → ℂ) :
    fourier χ (c • ψ) = c • fourier χ ψ
```

**`CondensedMatter.FiniteBloch.sum_character_smul_fourier`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L130).

> **Fourier inversion** on a finite abelian group.

```lean
lemma sum_character_smul_fourier (ψ : G → Fin N → ℂ) (x : G) :
    ∑ χ : AddChar G ℂ, χ x • fourier χ ψ = (Fintype.card G : ℂ) • ψ x
```

**`CondensedMatter.FiniteBloch.eq_zero_of_fourier_eq_zero`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L145).

> A configuration with vanishing Fourier transform vanishes.

```lean
lemma eq_zero_of_fourier_eq_zero {ψ : G → Fin N → ℂ} (h : ∀ χ, fourier χ ψ = 0) : ψ = 0
```

**`CondensedMatter.FiniteBloch.hopping_planeWave`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L154).

> A plane wave of crystal momentum `χ` is mapped to a plane wave with the same momentum.

```lean
lemma hopping_planeWave (A : G → Matrix (Fin N) (Fin N) ℂ) (χ : AddChar G ℂ)
    (v : Fin N → ℂ) :
    hopping A (fun x => χ x • v) = fun x => χ x • (bloch A χ).mulVec v
```

**`CondensedMatter.FiniteBloch.spectrum_hopping`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean#L165).

> **The spectrum of a translation-invariant operator on a finite periodic crystal is the union
> of the spectra of its Bloch matrices.**

```lean
lemma spectrum_hopping (A : G → Matrix (Fin N) (Fin N) ℂ) :
    spectrum ℂ (hopping A) = ⋃ χ : AddChar G ℂ, spectrum ℂ (bloch A χ)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/FiniteBloch.lean)

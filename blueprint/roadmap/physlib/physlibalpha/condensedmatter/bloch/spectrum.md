---
declaration: module
origin: cited
lean: CondensedMatter.Bloch.RegularRep.norm_sq_calculus_projection_localized, CondensedMatter.Bloch.RegularRep.toEuclideanCLM_single_apply, CondensedMatter.Bloch.RegularRep.internal_single_localized, CondensedMatter.Bloch.RegularRep.blochOperator, CondensedMatter.Bloch.RegularRep.commute_projection_internal, CondensedMatter.Bloch.RegularRep.blochOperator_projection_localized, CondensedMatter.Bloch.RegularRep.entry_combination_apply, CondensedMatter.Bloch.RegularRep.sum_norm_entry_combination
statement: formalized
proof: formalized
---

# The spectrum of a translation-invariant operator is the union of the Bloch bands

The module `PhyslibAlpha.CondensedMatter.Bloch.Spectrum`, [PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean): 12 declarations, 11 with a docstring.

> For the space `ℓ²(G, ℂ^N)`, the spectrum of the operator of a continuous symbol is exactly the union
> of the spectra of its values.

## i. Overview

> Let `b` be a continuous function from the Brillouin zone `Ĝ` to the `N × N` matrices, and let
> `B = ∫ b dP` be the corresponding translation-invariant operator on `ℓ²(G, ℂ^N)`. We showed that
> `spec B ⊆ ⋃_χ spec b(χ)`. The converse holds on `ℓ²(G, ℂ^N)`. If `λ` is an eigenvalue of `b(χ₀)`
> with eigenvector `e₀`, the state localized at the origin with internal state `e₀` has the uniform
> momentum distribution given by Haar measure, so its component in a small neighbourhood `W` of `χ₀`
> is nonzero, and on `W` the symbol maps `e₀` to within `δ` of `λ e₀`. These components are
> approximate eigenvectors of `B` with eigenvalue `λ`, so `λ` is in the spectrum. Hence
> `spec B = ⋃_χ spec b(χ)`: the spectrum of a translation-invariant operator is the union of the
> bands.

## ii. Key results

> - `RegularRep.norm_sq_calculus_projection_localized` : the norm of a symbol applied to the
>   momentum-`W` component of a localized state.
> - `RegularRep.spectrum_blochHom` : `spec ∫ b dP = ⋃_χ spec b(χ)`.

## iv. References

> * None.

## A. Norms of spectral components of localized states

**`CondensedMatter.Bloch.RegularRep.norm_sq_calculus_projection_localized`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L72).

> The norm of a continuous function of the translations applied to the momentum-`W` component of
> a localized state: the `L²` norm of the function over `W`, for the Haar measure.

```lean
lemma norm_sq_calculus_projection_localized (g : C(PontryaginDual (Multiplicative G), ℂ))
    {W : Set (PontryaginDual (Multiplicative G))} (hW : MeasurableSet W)
    (e : EuclideanSpace ℂ (Fin N)) :
    ‖UnitaryRep.calculus (translation G N) g
        (UnitaryRep.projection (translation G N) W (localized e))‖ ^ 2 =
      ‖e‖ ^ 2 * ∫ χ in W, ‖g χ‖ ^ 2 ∂(dualHaar (G := G))
```

**`CondensedMatter.Bloch.RegularRep.toEuclideanCLM_single_apply`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L119).

> The matrix unit `E_{ij}` acts on a vector as the `j`-th coordinate carried to the `i`-th.

```lean
lemma toEuclideanCLM_single_apply (i j : Fin N) (e : EuclideanSpace ℂ (Fin N)) :
    Matrix.toEuclideanCLM (n := Fin N) (𝕜 := ℂ) (Matrix.single i j (1 : ℂ)) e =
      e j • EuclideanSpace.single i (1 : ℂ)
```

**`CondensedMatter.Bloch.RegularRep.internal_single_localized`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L137).

> The internal matrix unit `E_{ij}` acts on a localized state by moving the `j`-th component
> to the `i`-th.

```lean
lemma internal_single_localized (i j : Fin N) (e : EuclideanSpace ℂ (Fin N)) :
    internal (G := G) (Matrix.single i j (1 : ℂ)) (localized e) =
      e j • localized (EuclideanSpace.single i (1 : ℂ))
```

**`CondensedMatter.Bloch.RegularRep.blochOperator`**, an abbrev, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L144).

> The translation-invariant operator `∫ f dP` of a symbol `f` on `ℓ²(G, ℂ^N)`.

```lean
abbrev blochOperator (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) :
    Space G N →L[ℂ] Space G N
```

**`CondensedMatter.Bloch.RegularRep.commute_projection_internal`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L149).

> The internal matrix units commute with the spectral projections.

```lean
lemma commute_projection_internal (W : Set (PontryaginDual (Multiplicative G)))
    (M : Matrix (Fin N) (Fin N) ℂ) :
    Commute (UnitaryRep.projection (translation G N) W) (internal (G := G) M)
```

**`CondensedMatter.Bloch.RegularRep.blochOperator_projection_localized`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L159).

> **Action of a symbol on a spectral component of a localized state**: the operator of a symbol
> `f` applied to the momentum-`W` component of the state localized at the origin with internal state
> `e` is the sum over the internal indices `i` of functions of the translations applied to the
> momentum-`W` component of the state localized in the `i`-th internal state.

```lean
lemma blochOperator_projection_localized
    (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (W : Set (PontryaginDual (Multiplicative G))) (e : EuclideanSpace ℂ (Fin N)) :
    blochOperator f (UnitaryRep.projection (translation G N) W (localized e)) =
      ∑ i, UnitaryRep.calculus (translation G N) (∑ j, e j • UnitaryRep.entry f i j)
        (UnitaryRep.projection (translation G N) W
          (localized (EuclideanSpace.single i (1 : ℂ))))
```

**`CondensedMatter.Bloch.RegularRep.entry_combination_apply`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L193).

> The `i`-th component of a symbol applied to a vector is the combination of its entries.

```lean
lemma entry_combination_apply
    (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (e : EuclideanSpace ℂ (Fin N)) (i : Fin N) (χ : PontryaginDual (Multiplicative G)) :
    (∑ j, e j • UnitaryRep.entry f i j) χ =
      (Matrix.toEuclideanCLM (n := Fin N) (𝕜 := ℂ) (f χ) e) i
```

**`CondensedMatter.Bloch.RegularRep.sum_norm_entry_combination`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L208).

```lean
lemma sum_norm_entry_combination
    (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (e : EuclideanSpace ℂ (Fin N)) (χ : PontryaginDual (Multiplicative G)) :
    ∑ i, ‖(∑ j, e j • UnitaryRep.entry f i j) χ‖ ^ 2 =
      ‖Matrix.toEuclideanCLM (n := Fin N) (𝕜 := ℂ) (f χ) e‖ ^ 2
```

**`CondensedMatter.Bloch.RegularRep.norm_blochOperator_projection_localized_le`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L220).

> **The symbol acts on spectral components of a localized state with the size of the symbol on
> those momenta**: if the symbol moves the internal state `e` by at most `δ` at all crystal momenta
> in `W`, then the operator of the symbol moves the momentum-`W` component of the localized state by
> at most `√N δ` times its norm, up to the norm of `e`.

```lean
lemma norm_blochOperator_projection_localized_le
    (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    {W : Set (PontryaginDual (Multiplicative G))} (hW : MeasurableSet W)
    (e : EuclideanSpace ℂ (Fin N)) {δ : ℝ}
    (hδ : ∀ χ ∈ W, ‖Matrix.toEuclideanCLM (n := Fin N) (𝕜 := ℂ) (f χ) e‖ ≤ δ) :
    ‖blochOperator f (UnitaryRep.projection (translation G N) W (localized e))‖ ^ 2 ≤
      N * δ ^ 2 * (dualHaar (G := G)).real W
```

**`CondensedMatter.Bloch.RegularRep.norm_sq_projection_localized`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L269).

> The squared norm of the momentum-`W` component of a localized state.

```lean
lemma norm_sq_projection_localized {W : Set (PontryaginDual (Multiplicative G))}
    (hW : MeasurableSet W) (e : EuclideanSpace ℂ (Fin N)) :
    ‖UnitaryRep.projection (translation G N) W (localized e)‖ ^ 2 =
      ‖e‖ ^ 2 * (dualHaar (G := G)).real W
```

## B. The spectrum

**`CondensedMatter.Bloch.RegularRep.spectrum_blochOperator`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L290).

> **The spectrum of a translation-invariant operator is the union of its Bloch bands.** For
> every continuous symbol `b` on the Brillouin zone, the spectrum of the operator `∫ b dP` on
> `ℓ²(G, ℂ^N)` is the union over crystal momenta `χ` of the spectra of the matrices `b(χ)`.

```lean
lemma spectrum_blochOperator
    (b : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) :
    spectrum ℂ (blochOperator b) =
      ⋃ χ : PontryaginDual (Multiplicative G), spectrum ℂ (b χ)
```

**`CondensedMatter.Bloch.RegularRep.spectrum_blochOperator_eq_bands`**, a lemma, [line 384](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean#L384).

> **The band structure**: for a Hermitian symbol, the spectrum of the translation-invariant
> operator on `ℓ²(G, ℂ^N)` is exactly the set of band values `ε_k(χ)`, the ordered eigenvalues of the
> Bloch matrices.

```lean
lemma spectrum_blochOperator_eq_bands
    (b : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (hb : ∀ χ, (b χ).IsHermitian) :
    spectrum ℂ (blochOperator b) =
      {z | ∃ (χ : PontryaginDual (Multiplicative G)) (k : Fin (Fintype.card (Fin N))),
        z = ((bandOf (hb χ) k : ℝ) : ℂ)}
```

## Depends on

- [The space of wavefunctions on a lattice with internal states](regularrep.md)
- [Bloch bands](../../probabilistictheory/representation/bands.md)

## Sources

- [PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/CondensedMatter/Bloch/Spectrum.lean)

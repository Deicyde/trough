---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.UnitaryRep.calculus, ProbabilisticTheory.QuantumMechanics.UnitaryRep.calculus_character, ProbabilisticTheory.QuantumMechanics.UnitaryRep.calculus_commute, ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry, ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_apply, ProbabilisticTheory.QuantumMechanics.UnitaryRep.calculus_commute_ι, ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochOp, ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_add
statement: formalized
proof: formalized
---

# Bloch–Floquet theory for representations with a finite-dimensional internal space

The module `PhyslibAlpha.ProbabilisticTheory.Representation.Floquet`, [PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean): 25 declarations (1 instance with no name), 11 with a docstring.

> Operators built from a unitary representation of an abelian group and an internal matrix algebra
> are integrals of a matrix-valued symbol over the dual group.

## i. Overview

> Let `π` be a unitary representation of a discrete abelian group `G` on a Hilbert space `H`, and let
> `ι : M_N(ℂ) → B(H)` be a ⋆-homomorphism commuting with `π`: an `N`-dimensional internal space
> attached to every point. Nothing is assumed about what `H` describes. It may carry the
> wavefunctions of a quantum particle, the displacement fields of a classical lattice, or an
> `L²` space of a classical statistical ensemble. The spectral measure `P` of `π` turns every
> continuous matrix-valued function `f` on the dual group `Ĝ` into the operator
> `∫ f dP = ∑_{ij} (∫ f_{ij} dP) ι(E_{ij})`, and this is a unital ⋆-homomorphism from `C(Ĝ, M_N)`
> to `B(H)`. Operators commuting with `π` and `ι` that arise this way are the translation-invariant
> operators with symbol `f`. Consequently the spectrum of the operator of a symbol is contained in the
> union of the spectra of the matrices `f(χ)`: the spectrum is the union of the bands. Under full
> support of the representation the map is injective.

## ii. Key results

> - `UnitaryRep.calculus` : the functional calculus `f ↦ ∫ f dP` of a representation.
> - `UnitaryRep.blochHom` : the ⋆-homomorphism `f ↦ ∫ f dP` on matrix-valued continuous functions.
> - `UnitaryRep.spectrum_blochHom_subset` : the spectrum of the operator of a symbol is contained in
>   the union of the spectra of the values of the symbol.
> - `UnitaryRep.blochHom_injective` : the map is injective for a representation of full support.

## iv. References

> * None.

**An instance with no name**, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L73).

```lean
instance : Nonempty (PontryaginDual (Multiplicative G))
```

## A. The functional calculus of the representation

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.calculus`**, a def, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L79).

> **The functional calculus of a unitary representation**: `f ↦ ∫ f dP` is a unital
> ⋆-homomorphism from the continuous functions on the Pontryagin dual to the bounded operators.

```lean
def calculus : C(PontryaginDual (Multiplicative G), ℂ) →⋆ₐ[ℂ] (H →L[ℂ] H)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.calculus_character`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L83).

> The functional calculus sends the character `χ ↦ χ(g)` to the operator `π(g)`.

```lean
lemma calculus_character (g : Multiplicative G) :
    calculus π ⟨fun χ => ((χ g : Circle) : ℂ),
      (TauCeti.PontryaginDual.continuous_coe_eval_const (G := Multiplicative G) g)⟩ =
      ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.calculus_commute`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L90).

> An operator commuting with the representation commutes with its functional calculus.

```lean
lemma calculus_commute {T : H →L[ℂ] H}
    (hT : ∀ g, Commute ((π g : unitary (H →L[ℂ] H)) : H →L[ℂ] H) T)
    (f : C(PontryaginDual (Multiplicative G), ℂ)) : Commute (calculus π f) T
```

## B. Matrix-valued functions

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L109).

> The `(i, j)` entry of a continuous matrix-valued function.

```lean
def entry (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) (i j : Fin N) :
    C(PontryaginDual (Multiplicative G), ℂ)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_apply`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L116).

```lean
lemma entry_apply (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (i j : Fin N) (χ : PontryaginDual (Multiplicative G)) : entry f i j χ = f χ i j
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.calculus_commute_ι`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L124).

```lean
lemma calculus_commute_ι (f : C(PontryaginDual (Multiplicative G), ℂ))
    (M : Matrix (Fin N) (Fin N) ℂ) : calculus π f * ι M = ι M * calculus π f
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochOp`**, a def, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L131).

> The operator `∑_{ij} (∫ f_{ij} dP) ι(E_{ij})` of a continuous matrix-valued function.

```lean
def blochOp (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) : H →L[ℂ] H
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_add`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L137).

```lean
lemma entry_add (f g : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (i j : Fin N) : entry (f + g) i j = entry f i j + entry g i j
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_smul`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L143).

```lean
lemma entry_smul (c : ℂ) (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (i j : Fin N) : entry (c • f) i j = c • entry f i j
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_zero`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L149).

```lean
lemma entry_zero (i j : Fin N) :
    entry (0 : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) i j = 0
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_mul`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L155).

```lean
lemma entry_mul (f g : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (i j : Fin N) : entry (f * g) i j = ∑ k, entry f i k * entry g k j
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_star`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L163).

```lean
lemma entry_star (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (i j : Fin N) : entry (star f) i j = star (entry f j i)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_one`**, a lemma, [line 171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L171).

```lean
lemma entry_one (i j : Fin N) :
    entry (1 : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) i j =
      if i = j then 1 else 0
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochOp_add`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L180).

```lean
lemma blochOp_add (f g : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) :
    blochOp π ι (f + g) = blochOp π ι f + blochOp π ι g
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochOp_smul`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L185).

```lean
lemma blochOp_smul (c : ℂ)
    (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) :
    blochOp π ι (c • f) = c • blochOp π ι f
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochOp_one`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L191).

```lean
lemma blochOp_one : blochOp π ι (1 : C(PontryaginDual (Multiplicative G),
    Matrix (Fin N) (Fin N) ℂ)) = 1
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochOp_mul`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L203).

```lean
lemma blochOp_mul (f g : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) :
    blochOp π ι (f * g) = blochOp π ι f * blochOp π ι g
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochOp_star`**, a lemma, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L250).

```lean
lemma blochOp_star (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) :
    blochOp π ι (star f) = star (blochOp π ι f)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochHom`**, a def, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L270).

> **Bloch–Floquet**: the map `f ↦ ∑_{ij} (∫ f_{ij} dP) ι(E_{ij})` is a unital ⋆-homomorphism from
> the continuous matrix-valued functions on the Brillouin zone to the bounded operators.

```lean
def blochHom : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ) →⋆ₐ[ℂ]
    (H →L[ℂ] H)
```

## C. The spectrum

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.spectrum_blochHom_subset`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L293).

> **The spectrum of the operator of a symbol is contained in the union of the spectra of the
> symbol's values**: a translation-invariant operator has no spectrum outside its Bloch bands.

```lean
lemma spectrum_blochHom_subset
    (b : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ)) :
    spectrum ℂ (blochHom π ι hι b) ⊆
      ⋃ χ : PontryaginDual (Multiplicative G), spectrum ℂ (b χ)
```

## D. Faithful representations

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.HasFullSupport`**, a def, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L315).

> A representation has **full support** relative to the internal space when the spectral
> projection of every nonempty open set of crystal momenta is nonzero on every internal state:
> every crystal momentum is present in every orbital.

```lean
def HasFullSupport : Prop
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.compress_blochOp`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L323).

> Compressing the image of a matrix-valued function to the `(i, j)` orbitals isolates the
> `(i, j)` entry.

```lean
lemma compress_blochOp (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (i j : Fin N) :
    ι (Matrix.single i i 1) * blochOp π ι f * ι (Matrix.single j i 1) =
      calculus π (entry f i j) * ι (Matrix.single i i 1)
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.entry_eq_zero_of_blochOp_eq_zero`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L360).

> An entry of the image vanishes only if the entry function vanishes: this is the content of
> full support.

```lean
lemma entry_eq_zero_of_blochOp_eq_zero (hfull : HasFullSupport π ι)
    (f : C(PontryaginDual (Multiplicative G), Matrix (Fin N) (Fin N) ℂ))
    (hf : blochOp π ι f = 0) : f = 0
```

**`ProbabilisticTheory.QuantumMechanics.UnitaryRep.blochHom_injective`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean#L429).

> Under full support the map `f ↦ ∫ f dP` is injective.

```lean
lemma blochHom_injective (hfull : HasFullSupport π ι) :
    Function.Injective (blochHom π ι hι)
```

## Depends on

- [The continuous functional calculus of a spectral measure](../hilbertspace/part-02/unbounded-continuouscalculus.md)
- [The commutant of a unitary representation of an abelian group](commutant.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Representation/Floquet.lean)

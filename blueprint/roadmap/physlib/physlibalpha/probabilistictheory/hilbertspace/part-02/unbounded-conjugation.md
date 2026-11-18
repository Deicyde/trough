---
declaration: module
origin: cited
lean: ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConj, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjAddHom, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.continuous_unitaryConjAddHom, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConj_mul, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConj_star, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConj_one, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjSpectralMeasure, ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjSpectralMeasure_apply
statement: formalized
proof: formalized
---

# Transporting spectral measures along unitaries

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.Conjugation`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean): 11 declarations, 3 with a docstring.

> Conjugating operators and spectral measures by a unitary.

## i. Overview

> A unitary `u : H ≃ₗᵢ[ℂ] H'` conjugates operators on `H` to operators on `H'`, and conjugation is a
> `⋆`-isomorphism in the weak operator topology. Conjugating a spectral measure on `H` gives a
> spectral measure on `H'` whose scalar and diagonal measures are those of the original, transported
> along `u`.

## ii. Key results

> - `unitaryConj` : conjugation of an operator by `u`.
> - `unitaryConjSpectralMeasure` : conjugation of a spectral measure by `u`.
> - `unitaryConjSpectralMeasure_scalarMeasure`, `unitaryConjSpectralMeasure_diagonalMeasure` : the
>   transported scalar and diagonal measures.

## iv. References

> * None.

## A. Conjugation of a single operator

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConj`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L62).

> Conjugation of a bounded operator by a Hilbert-space unitary, viewed in the WOT type.

```lean
def unitaryConj {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H']
    [CompleteSpace H'] (u : H ≃ₗᵢ[ℂ] H') (A : H →WOT[ℂ] H) : H' →WOT[ℂ] H'
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjAddHom`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L69).

> Unitary conjugation is additive on WOT operators.

```lean
def unitaryConjAddHom {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H']
    [CompleteSpace H'] (u : H ≃ₗᵢ[ℂ] H') :
    (H →WOT[ℂ] H) →+ (H' →WOT[ℂ] H')
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.continuous_unitaryConjAddHom`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L80).

```lean
lemma continuous_unitaryConjAddHom {H' : Type*} [NormedAddCommGroup H']
    [InnerProductSpace ℂ H'] [CompleteSpace H'] (u : H ≃ₗᵢ[ℂ] H') :
    Continuous (unitaryConjAddHom u)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConj_mul`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L99).

```lean
lemma unitaryConj_mul {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H']
    [CompleteSpace H'] (u : H ≃ₗᵢ[ℂ] H') (A B : H →WOT[ℂ] H) :
    unitaryConj u (A * B) = unitaryConj u A * unitaryConj u B
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConj_star`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L106).

```lean
lemma unitaryConj_star {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H']
    [CompleteSpace H'] (u : H ≃ₗᵢ[ℂ] H') (A : H →WOT[ℂ] H) :
    unitaryConj u (star A) = star (unitaryConj u A)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConj_one`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L128).

```lean
lemma unitaryConj_one {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H']
    [CompleteSpace H'] (u : H ≃ₗᵢ[ℂ] H') :
    unitaryConj u (1 : H →WOT[ℂ] H) = 1
```

## B. Conjugation of a spectral measure

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjSpectralMeasure`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L138).

> Transport a WOT spectral measure through a Hilbert-space unitary.

```lean
def unitaryConjSpectralMeasure {H' : Type*} [NormedAddCommGroup H']
    [InnerProductSpace ℂ H'] [CompleteSpace H'] (u : H ≃ₗᵢ[ℂ] H') :
    WOTSpectralMeasure α H → WOTSpectralMeasure α H'
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjSpectralMeasure_apply`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L157).

```lean
lemma unitaryConjSpectralMeasure_apply {H' : Type*} [NormedAddCommGroup H']
    [InnerProductSpace ℂ H'] [CompleteSpace H'] (u : H ≃ₗᵢ[ℂ] H')
    (μS : WOTSpectralMeasure α H) (S : Set α) :
    unitaryConjSpectralMeasure u μS S = unitaryConj u (μS S)
```

## C. Interaction with the scalar and diagonal measures

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjSpectralMeasure_scalarMeasure_apply`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L165).

```lean
lemma unitaryConjSpectralMeasure_scalarMeasure_apply
    {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H'] [CompleteSpace H']
    (u : H ≃ₗᵢ[ℂ] H') (μS : WOTSpectralMeasure α H) (x y : H') (S : Set α) :
    (unitaryConjSpectralMeasure u μS).scalarMeasure x y S =
      μS.scalarMeasure (u.symm x) (u.symm y) S
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjSpectralMeasure_scalarMeasure`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L174).

```lean
lemma unitaryConjSpectralMeasure_scalarMeasure
    {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H'] [CompleteSpace H']
    (u : H ≃ₗᵢ[ℂ] H') (μS : WOTSpectralMeasure α H) (x y : H') :
    (unitaryConjSpectralMeasure u μS).scalarMeasure x y =
      μS.scalarMeasure (u.symm x) (u.symm y)
```

**`ProbabilisticTheory.QuantumMechanics.WOTSpectralMeasure.unitaryConjSpectralMeasure_diagonalMeasure`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean#L183).

```lean
lemma unitaryConjSpectralMeasure_diagonalMeasure
    {H' : Type*} [NormedAddCommGroup H'] [InnerProductSpace ℂ H'] [CompleteSpace H']
    (u : H ≃ₗᵢ[ℂ] H') (μS : WOTSpectralMeasure α H) (x : H') :
    (unitaryConjSpectralMeasure u μS).diagonalMeasure x =
      μS.diagonalMeasure (u.symm x)
```

## Depends on

- [Scalar and diagonal measures of a spectral measure](unbounded-scalarmeasure.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/Conjugation.lean)

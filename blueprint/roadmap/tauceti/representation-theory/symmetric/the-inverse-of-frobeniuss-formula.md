---
declaration: theorem
origin: cited
lean: TauCeti.sum_spechtChar_smul_psumPart
statement: formalized
proof: formalized
---

# The inverse of Frobenius's formula

weighting the power-sum products over the cycle types by
a Specht character recovers the Schur polynomial, `∑_{π ∈ Sₙ} χ^μ(π) p_{ρ(π)} = n! s_μ`. Over a
`ℚ`-algebra this says that `(1 / n!) ∑_π χ^μ(π) p_{ρ(π)}` is `s_μ`.

```lean
TauCeti.sum_spechtChar_smul_psumPart.{u_1, u_2} {n : ℕ} {σ : Type u_1} [Fintype σ] (R : Type u_2)
  [CommRing R] (μ : n.Partition) :
  ∑ π, TauCeti.spechtChar μ π • MvPolynomial.psumPart σ R π.partition =
    n.factorial • TauCeti.schurPoly σ R μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's bialternant formula](../../ring-theory/mv-polynomial/jacobis-bialternant-formula.md)
- [James's dominance lemma](jamess-dominance-lemma.md)
- [James's submodule theorem](jamess-submodule-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_spechtChar_smul_psumPart`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.html#TauCeti.sum_spechtChar_smul_psumPart).

## Sources

- [Tau Ceti documentation: `TauCeti.sum_spechtChar_smul_psumPart`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.html#TauCeti.sum_spechtChar_smul_psumPart)
- [Source of `TauCeti.sum_spechtChar_smul_psumPart` in TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.lean#L193)

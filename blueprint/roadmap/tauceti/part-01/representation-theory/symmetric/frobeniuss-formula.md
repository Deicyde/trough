---
declaration: theorem
origin: cited
lean: TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly
statement: formalized
proof: formalized
---

# Frobenius's formula

the power-sum product of a partition `ρ` of `n` expands in the Schur
polynomials as `p_ρ = ∑_{λ ⊢ n} χ^λ(ρ) s_λ`, the coefficients being the column of `ρ` in the
character table of `Sₙ`. This holds in every finite alphabet and over every commutative ring; the
Schur polynomials of the partitions with more parts than the alphabet has letters vanish.

```lean
TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly.{u_1, u_2} {n : ℕ} {σ : Type u_1} [Fintype σ]
  (R : Type u_2) [CommRing R] (ρ : n.Partition) :
  MvPolynomial.psumPart σ R ρ = ∑ l, TauCeti.spechtCharValue l ρ • TauCeti.schurPoly σ R l
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jacobi's bialternant formula](../../ring-theory/part-01/multivariate-polynomials/jacobis-bialternant-formula.md)
- [James's dominance lemma](jamess-dominance-lemma.md)
- [James's submodule theorem](jamess-submodule-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.html#TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly).

## Sources

- [Tau Ceti documentation: `TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.html#TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly)
- [Source of `TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly` in TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.lean#L173)

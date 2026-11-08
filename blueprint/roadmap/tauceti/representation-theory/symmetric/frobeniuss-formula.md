---
declaration: theorem
origin: cited
lean: TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly, TauCeti.card_productOneTriples_eq_sum_characterTable
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

- [Jacobi's bialternant formula](../../ring-theory/mv-polynomial/jacobis-bialternant-formula.md)
- [James's dominance lemma](jamess-dominance-lemma.md)
- [James's submodule theorem](jamess-submodule-theorem.md)
- [Schur's lemma, vanishing form](../../quantum-groups/quantum-groups-compact-reconstruction-and-generi/schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.html#TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly).

## Other forms

**The Frobenius formula.** Formalized in Tau Ceti as [`TauCeti.card_productOneTriples_eq_sum_characterTable`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/CharacterTable/ProductOne.html#TauCeti.card_productOneTriples_eq_sum_characterTable).

```lean
TauCeti.card_productOneTriples_eq_sum_characterTable.{u, v} {k : Type u} {G : Type v} [Field k]
  [IsAlgClosed k] [CharZero k] [Group G] [Fintype G] [DecidableEq G] [Invertible ↑(Nat.card G)]
  (C0 C1 Cinf : ConjClasses G) :
  ↑(TauCeti.productOneTriples C0 C1 Cinf).card =
    ↑(Nat.card ↑C0.carrier) * ↑(Nat.card ↑C1.carrier) * ↑(Nat.card ↑Cinf.carrier) / ↑(Nat.card G) *
      ∑ l,
        TauCeti.characterTable k G l C0 * TauCeti.characterTable k G l C1 *
            TauCeti.characterTable k G l Cinf /
          ↑(TauCeti.characterDegree k l)
```

## Sources

- [Tau Ceti documentation: `TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.html#TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly)
- [Source of `TauCeti.psumPart_eq_sum_spechtCharValue_smul_schurPoly` in TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Symmetric/FrobeniusCharacteristic.lean#L173)

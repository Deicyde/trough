---
declaration: theorem
origin: cited
lean: Finset.IsSquarefreeBasis.exists_rootMultiplicity_lazardEval_eq_sum
statement: formalized
proof: formalized
---

# Finset.IsSquarefreeBasis.exists_rootMultiplicity_lazardEval_eq_sum

The multiplicities in an input's Lazard evaluation are fixed weighted sums
of the multiplicities in the basis evaluations, even on nullified ordinary fibers.

```lean
Finset.IsSquarefreeBasis.exists_rootMultiplicity_lazardEval_eq_sum.{u_1} {R : Type u_1} [CommRing R]
  {n : ℕ} {F B : Finset (Polynomial (MvPolynomial (Fin n) R))} [IsDomain R]
  (hB : F.IsSquarefreeBasis B) {f : Polynomial (MvPolynomial (Fin n) R)} (hf : f ∈ F) :
  ∃ e,
    ∀ (a : Fin n → R) (t : R),
      Polynomial.rootMultiplicity t
          ((((MvPolynomial.optionEquivLeft R (Fin n)).symm.trans
                  (MvPolynomial.optionEquivRight R (Fin n)))
                f).lazardEval
            (⇑Polynomial.C ∘ a)) =
        ∑ b ∈ B,
          e b *
            Polynomial.rootMultiplicity t
              ((((MvPolynomial.optionEquivLeft R (Fin n)).symm.trans
                      (MvPolynomial.optionEquivRight R (Fin n)))
                    b).lazardEval
                (⇑Polynomial.C ∘ a))
```

## Depends on

- [Finset.IsSquarefreeBasis](finset-issquarefreebasis.md)

## Lean

Formalized in Tau Ceti as [`Finset.IsSquarefreeBasis.exists_rootMultiplicity_lazardEval_eq_sum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/SquarefreeBasis/Lazard.html#Finset.IsSquarefreeBasis.exists_rootMultiplicity_lazardEval_eq_sum).

## Sources

- [Tau Ceti documentation: `Finset.IsSquarefreeBasis.exists_rootMultiplicity_lazardEval_eq_sum`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/SquarefreeBasis/Lazard.html#Finset.IsSquarefreeBasis.exists_rootMultiplicity_lazardEval_eq_sum)
- [Source of `Finset.IsSquarefreeBasis.exists_rootMultiplicity_lazardEval_eq_sum` in TauCeti/RingTheory/MvPolynomial/SquarefreeBasis/Lazard.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/MvPolynomial/SquarefreeBasis/Lazard.lean#L127)
- [Tau Ceti roadmap status: Real algebraic geometry: sign determination and cylindrical decomposition](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/RealAlgebraicGeometry/STATUS.md)

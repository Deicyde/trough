---
declaration: theorem
origin: cited
lean: AddMonoidAlgebra.exists_ringEquiv_pi_field_of_isFractionRing
statement: formalized
proof: formalized
---

# AddMonoidAlgebra.exists_ringEquiv_pi_field_of_isFractionRing

The total quotient ring of the group ring of a finitely generated commutative additive group
over a formally real Noetherian ring, such as `ℤ[H]` for a finitely generated abelian group `H`,
is a finite product of fields of characteristic zero.

```lean
AddMonoidAlgebra.exists_ringEquiv_pi_field_of_isFractionRing.{u, v, w} (R : Type u) (H : Type v)
  (K : Type w) [CommRing R] [IsFormallyReal R] [AddCommGroup H] [CommRing K]
  [Algebra (AddMonoidAlgebra R H) K] [IsFractionRing (AddMonoidAlgebra R H) K] [IsNoetherianRing R]
  [AddGroup.FG H] :
  ∃ ι, ∃ (_ : Finite ι), ∃ F x, (∀ (i : ι), CharZero (F i)) ∧ Nonempty (K ≃+* ((i : ι) → F i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddMonoidAlgebra.exists_ringEquiv_pi_field_of_isFractionRing`](https://taucetiproject.org/docs/TauCeti/Algebra/MonoidAlgebra/TotalQuotient.html#AddMonoidAlgebra.exists_ringEquiv_pi_field_of_isFractionRing).

## Sources

- [Tau Ceti documentation: `AddMonoidAlgebra.exists_ringEquiv_pi_field_of_isFractionRing`](https://taucetiproject.org/docs/TauCeti/Algebra/MonoidAlgebra/TotalQuotient.html#AddMonoidAlgebra.exists_ringEquiv_pi_field_of_isFractionRing)
- [Source of `AddMonoidAlgebra.exists_ringEquiv_pi_field_of_isFractionRing` in TauCeti/Algebra/MonoidAlgebra/TotalQuotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/MonoidAlgebra/TotalQuotient.lean#L195)
- [Tau Ceti roadmap status: Morse–Novikov homology and dynamical Reidemeister torsion](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseNovikov/STATUS.md)

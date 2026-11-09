---
declaration: theorem
origin: cited
lean: TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_congr
statement: formalized
proof: formalized
---

# Functoriality of the marked presentation in even degree

The two even dyadic marked
theorems `TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_plusMinus` and
`TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_principal` present `G_K(2)` by the same
word `demushkinWordTwoEven a f (N + 2)` on `N + 2` generators and record the same values on the
second and fourth marked generators, the value `-(1 + a)⁻¹` and the value `(1 - 2^f)⁻¹`; they differ
only in the hypotheses that select the parameters `a` and `f`. Hence the transport of their marking
is a single statement. For `e : K ≃+* K'` an isomorphism of fields, the transported isomorphism
`(absoluteGaloisGroupProPCongr e).trans m` of a marked presentation of `G_K(2)` of the even form
presents `G_{K'}(2)` by the same relator word and takes the same values.

Only the transport of the recorded values is claimed, and it uses no property of `e` beyond being an
isomorphism of fields; the transport is the naturality of the cyclotomic orientation along the
induced isomorphism of the absolute Galois groups
(`TauCeti.cyclotomicOrientation_trans_absoluteGaloisGroupProPCongr`). For the transported
presentation to be *the* marked presentation of `G_{K'}(2)` in the sense of
`TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_plusMinus` or
`TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_principal`, the target must have the
same even degree over `ℚ₂` and the same cyclotomic image as the source; an isomorphism of local
fields over `ℚ₂` provides that (`TauCeti.isDyadicEvenPlusMinusCase_iff_of_algEquiv` and
`TauCeti.isDyadicEvenPrincipalCase_iff_of_algEquiv`).

```lean
TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_congr.{u_1, u_2} {K : Type u_1}
  {K' : Type u_2} [Field K] [Algebra ℚ_[2] K] [Field K'] (e : K ≃+* K')
  (hmu : ∃ ζ, IsPrimitiveRoot ζ 2) (hmu' : ∃ ζ, IsPrimitiveRoot ζ 2) {a f : ℕ}
  (m :
    TauCeti.absoluteGaloisGroupProP 2 K ≃ₜ*
      TauCeti.presentedProP 2 (Fin (Module.finrank ℚ_[2] K + 2))
        {TauCeti.demushkinWordTwoEven a f (Module.finrank ℚ_[2] K + 2)
            (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))})
  (hm₁ :
    ↑((TauCeti.cyclotomicOrientation 2 K hmu)
            (m.symm
              (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                {TauCeti.demushkinWordTwoEven a f (Module.finrank ℚ_[2] K + 2)
                    (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                1))) *
        (1 + ↑a) =
      -1)
  (hm₃ :
    ↑((TauCeti.cyclotomicOrientation 2 K hmu)
            (m.symm
              (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                {TauCeti.demushkinWordTwoEven a f (Module.finrank ℚ_[2] K + 2)
                    (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                3))) *
        (1 - 2 ^ f) =
      1)
  (hm :
    ∀ (i : ℕ),
      i ≠ 1 →
        i ≠ 3 →
          i < Module.finrank ℚ_[2] K + 2 →
            (TauCeti.cyclotomicOrientation 2 K hmu)
                (m.symm
                  (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                    {TauCeti.demushkinWordTwoEven a f (Module.finrank ℚ_[2] K + 2)
                        (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                    i)) =
              1) :
  ↑((TauCeti.cyclotomicOrientation 2 K' hmu')
            (((TauCeti.absoluteGaloisGroupProPCongr 2 K K' e).trans m).symm
              (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                {TauCeti.demushkinWordTwoEven a f (Module.finrank ℚ_[2] K + 2)
                    (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                1))) *
        (1 + ↑a) =
      -1 ∧
    ↑((TauCeti.cyclotomicOrientation 2 K' hmu')
              (((TauCeti.absoluteGaloisGroupProPCongr 2 K K' e).trans m).symm
                (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                  {TauCeti.demushkinWordTwoEven a f (Module.finrank ℚ_[2] K + 2)
                      (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                  3))) *
          (1 - 2 ^ f) =
        1 ∧
      ∀ (i : ℕ),
        i ≠ 1 →
          i ≠ 3 →
            i < Module.finrank ℚ_[2] K + 2 →
              (TauCeti.cyclotomicOrientation 2 K' hmu')
                  (((TauCeti.absoluteGaloisGroupProPCongr 2 K K' e).trans m).symm
                    (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                      {TauCeti.demushkinWordTwoEven a f (Module.finrank ℚ_[2] K + 2)
                          (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                      i)) =
                1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_congr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.html#TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_congr).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_congr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.html#TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_congr)
- [Source of `TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_even_congr` in TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.lean#L400)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)

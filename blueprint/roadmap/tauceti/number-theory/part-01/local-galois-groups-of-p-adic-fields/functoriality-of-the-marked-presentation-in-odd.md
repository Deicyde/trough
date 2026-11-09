---
declaration: theorem
origin: cited
lean: TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_congr
statement: formalized
proof: formalized
---

# Functoriality of the marked presentation in odd degree

Let `e : K ≃+* K'` be an isomorphism
of fields, and let `m` be a marked presentation of `G_K(2)` with the relator word and the values
that `TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd` records for `K`. Then
`(absoluteGaloisGroupProPCongr e).trans m` presents `G_{K'}(2)` by the same relator word
`demushkinWordTwoOdd` and takes the same values on the generators `0`, `2` and the remaining ones.

Only the transport of the recorded values is claimed, and it uses no property of `e` beyond being an
isomorphism of fields; the transport is the naturality of the cyclotomic orientation along the
induced isomorphism of the absolute Galois groups
(`TauCeti.cyclotomicOrientation_trans_absoluteGaloisGroupProPCongr`). For the transported
presentation to be *the* marked presentation of `G_{K'}(2)` in the sense of
`TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd`, the target must have the same odd degree
over `ℚ₂` as the source; an isomorphism of local fields over `ℚ₂` provides that
(`TauCeti.isDyadicOddCase_iff_of_algEquiv`).

```lean
TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_congr.{u_1, u_2} {K : Type u_1}
  {K' : Type u_2} [Field K] [Algebra ℚ_[2] K] [Field K'] (e : K ≃+* K')
  (hmu : ∃ ζ, IsPrimitiveRoot ζ 2) (hmu' : ∃ ζ, IsPrimitiveRoot ζ 2)
  (m :
    TauCeti.absoluteGaloisGroupProP 2 K ≃ₜ*
      TauCeti.presentedProP 2 (Fin (Module.finrank ℚ_[2] K + 2))
        {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] K + 2)
            (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))})
  (hm₀ :
    (TauCeti.cyclotomicOrientation 2 K hmu)
        (m.symm
          (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
            {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] K + 2)
                (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
            0)) =
      -1)
  (hm₂ :
    ↑((TauCeti.cyclotomicOrientation 2 K hmu)
            (m.symm
              (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] K + 2)
                    (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                2))) *
        (1 - 2 ^ 2) =
      1)
  (hm :
    ∀ (i : ℕ),
      i ≠ 0 →
        i ≠ 2 →
          i < Module.finrank ℚ_[2] K + 2 →
            (TauCeti.cyclotomicOrientation 2 K hmu)
                (m.symm
                  (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                    {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] K + 2)
                        (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                    i)) =
              1) :
  (TauCeti.cyclotomicOrientation 2 K' hmu')
        (((TauCeti.absoluteGaloisGroupProPCongr 2 K K' e).trans m).symm
          (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
            {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] K + 2)
                (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
            0)) =
      -1 ∧
    ↑((TauCeti.cyclotomicOrientation 2 K' hmu')
              (((TauCeti.absoluteGaloisGroupProPCongr 2 K K' e).trans m).symm
                (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                  {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] K + 2)
                      (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                  2))) *
          (1 - 2 ^ 2) =
        1 ∧
      ∀ (i : ℕ),
        i ≠ 0 →
          i ≠ 2 →
            i < Module.finrank ℚ_[2] K + 2 →
              (TauCeti.cyclotomicOrientation 2 K' hmu')
                  (((TauCeti.absoluteGaloisGroupProPCongr 2 K K' e).trans m).symm
                    (TauCeti.presentedProPGen 2 (Module.finrank ℚ_[2] K + 2)
                      {TauCeti.demushkinWordTwoOdd 2 (Module.finrank ℚ_[2] K + 2)
                          (TauCeti.freeProPGen 2 (Module.finrank ℚ_[2] K + 2))}
                      i)) =
                1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_congr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.html#TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_congr).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_congr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.html#TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_congr)
- [Source of `TauCeti.absoluteGaloisGroupProP_two_marked_of_degree_odd_congr` in TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.lean#L344)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)

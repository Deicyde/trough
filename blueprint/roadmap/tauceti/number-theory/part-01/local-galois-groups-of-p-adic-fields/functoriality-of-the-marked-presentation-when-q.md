---
declaration: theorem
origin: cited
lean: TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_congr
statement: formalized
proof: formalized
---

# Functoriality of the marked presentation when `q(K) ≠ 2`

Let `e : K ≃+* K'` be an
isomorphism of fields, and let `m` be a marked presentation of `G_K(p)` with the relator word and
the values that `TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two` records for `K`. Then
`(absoluteGaloisGroupProPCongr e).trans m` presents `G_{K'}(p)` by the same relator word and takes
the same values of the cyclotomic orientation on the generators.

Only the transport of the recorded values is claimed, and it uses no property of `e` beyond being an
isomorphism of fields: it is the naturality of the cyclotomic orientation along the induced
isomorphism of the absolute Galois groups
(`TauCeti.cyclotomicOrientation_trans_absoluteGaloisGroupProPCongr`). For the transported
presentation to be *the* marked presentation of `G_{K'}(p)` in the sense of
`TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two`, the target must have the same degree over
`ℚ_p` and the same number of `p`-power roots of unity as the source; an isomorphism of local fields
over `ℚ_p` provides that (`TauCeti.isQNeTwoCase_iff_of_algEquiv`).

```lean
TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_congr.{u_1, u_2} (p : ℕ) [Fact (Nat.Prime p)]
  {K : Type u_1} {K' : Type u_2} [Field K] [Algebra ℚ_[p] K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field K'] (e : K ≃+* K') (hmu : ∃ ζ, IsPrimitiveRoot ζ p)
  (hmu' : ∃ ζ, IsPrimitiveRoot ζ p)
  (m :
    TauCeti.absoluteGaloisGroupProP p K ≃ₜ*
      TauCeti.presentedProP p (Fin (Module.finrank ℚ_[p] K + 2))
        {TauCeti.demushkinWordNeTwo (TauCeti.localRootOfUnityOrder p K ⋯)
            (Module.finrank ℚ_[p] K + 2) (TauCeti.freeProPGen p (Module.finrank ℚ_[p] K + 2))})
  (hm₁ :
    ↑((TauCeti.cyclotomicOrientation p K hmu)
            (m.symm
              (TauCeti.presentedProPGen p (Module.finrank ℚ_[p] K + 2)
                {TauCeti.demushkinWordNeTwo (TauCeti.localRootOfUnityOrder p K ⋯)
                    (Module.finrank ℚ_[p] K + 2)
                    (TauCeti.freeProPGen p (Module.finrank ℚ_[p] K + 2))}
                1))) *
        (1 - ↑(TauCeti.localRootOfUnityOrder p K ⋯)) =
      1)
  (hm₂ :
    ∀ (i : ℕ),
      i ≠ 1 →
        i < Module.finrank ℚ_[p] K + 2 →
          (TauCeti.cyclotomicOrientation p K hmu)
              (m.symm
                (TauCeti.presentedProPGen p (Module.finrank ℚ_[p] K + 2)
                  {TauCeti.demushkinWordNeTwo (TauCeti.localRootOfUnityOrder p K ⋯)
                      (Module.finrank ℚ_[p] K + 2)
                      (TauCeti.freeProPGen p (Module.finrank ℚ_[p] K + 2))}
                  i)) =
            1) :
  ↑((TauCeti.cyclotomicOrientation p K' hmu')
            (((TauCeti.absoluteGaloisGroupProPCongr p K K' e).trans m).symm
              (TauCeti.presentedProPGen p (Module.finrank ℚ_[p] K + 2)
                {TauCeti.demushkinWordNeTwo (TauCeti.localRootOfUnityOrder p K ⋯)
                    (Module.finrank ℚ_[p] K + 2)
                    (TauCeti.freeProPGen p (Module.finrank ℚ_[p] K + 2))}
                1))) *
        (1 - ↑(TauCeti.localRootOfUnityOrder p K ⋯)) =
      1 ∧
    ∀ (i : ℕ),
      i ≠ 1 →
        i < Module.finrank ℚ_[p] K + 2 →
          (TauCeti.cyclotomicOrientation p K' hmu')
              (((TauCeti.absoluteGaloisGroupProPCongr p K K' e).trans m).symm
                (TauCeti.presentedProPGen p (Module.finrank ℚ_[p] K + 2)
                  {TauCeti.demushkinWordNeTwo (TauCeti.localRootOfUnityOrder p K ⋯)
                      (Module.finrank ℚ_[p] K + 2)
                      (TauCeti.freeProPGen p (Module.finrank ℚ_[p] K + 2))}
                  i)) =
            1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_congr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.html#TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_congr).

## Sources

- [Tau Ceti documentation: `TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_congr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.html#TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_congr)
- [Source of `TauCeti.absoluteGaloisGroupProP_marked_of_q_ne_two_congr` in TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/ProP/Marked/Functoriality.lean#L284)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)

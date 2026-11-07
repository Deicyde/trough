---
declaration: theorem
origin: cited
lean: TauCeti.LazardRing.coproduct_coassoc
statement: formalized
proof: formalized
---

# Coassociativity

`(Δ ⊗ id) Δ = (id ⊗ Δ) Δ` of the coproduct: composition of strict
isomorphisms is associative. Both sides take values in the triple tensor product
`Γ ⊗_L Γ ⊗_L Γ = MvPolynomial ℕ+ (Γ ⊗_L Γ)`, the pushout of `Γ ⊗_L Γ` along the target of its right
factor and of `Γ` along `η_L`, whose three factors are `C ∘ C`, `C ∘ MvPolynomial.map η_R` and
`MvPolynomial.map (MvPolynomial.map η_R ∘ η_R)`. In it, `Δ ⊗ id` is `tensorLift (C ∘ Δ, ι₃)` with
`ι₃` the third factor, and `id ⊗ Δ` is `tensorLift (C ∘ C, ι₂₃ ∘ Δ)` with
`ι₂₃ = MvPolynomial.map (MvPolynomial.map η_R)` the inclusion of the last two factors.

```lean
TauCeti.LazardRing.coproduct_coassoc :
  (TauCeti.LazardRing.tensorLift
          ⟨(MvPolynomial.C.comp TauCeti.LazardRing.coproduct,
              MvPolynomial.map
                ((MvPolynomial.map TauCeti.LazardRing.rightUnit).comp
                  TauCeti.LazardRing.rightUnit)),
            ⋯⟩).comp
      TauCeti.LazardRing.coproduct =
    (TauCeti.LazardRing.tensorLift
          ⟨(MvPolynomial.C.comp MvPolynomial.C,
              (MvPolynomial.map (MvPolynomial.map TauCeti.LazardRing.rightUnit)).comp
                TauCeti.LazardRing.coproduct),
            ⋯⟩).comp
      TauCeti.LazardRing.coproduct
```

## Depends on

- [Strict coordinate changes of commutative formal group laws are representable](strict-coordinate-changes-of-commutative-formal.md)
- [TauCeti.FormalCoordinate](../../part-03/formal-laurent-fields-puiseux-expansions-and-con/tauceti-formalcoordinate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.coproduct_coassoc`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/HopfAlgebroid.html#TauCeti.LazardRing.coproduct_coassoc).

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.coproduct_coassoc`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/HopfAlgebroid.html#TauCeti.LazardRing.coproduct_coassoc)
- [Source of `TauCeti.LazardRing.coproduct_coassoc` in TauCeti/RingTheory/FormalGroup/CoordinateChange/HopfAlgebroid.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/CoordinateChange/HopfAlgebroid.lean#L253)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BordismFormalGroups/STATUS.md)

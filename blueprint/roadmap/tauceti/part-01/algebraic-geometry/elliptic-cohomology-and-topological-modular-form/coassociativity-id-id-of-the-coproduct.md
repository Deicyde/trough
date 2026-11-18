---
declaration: theorem
origin: cited
lean: TauCeti.WeierstrassHopfAlgebroid.coproduct_coassoc
statement: formalized
proof: formalized
---

# Coassociativity `(Δ ⊗ id) Δ = (id ⊗ Δ) Δ` of the coproduct

composition of changes of
variables is associative. Both sides take values in the triple tensor product
`Γ ⊗_A Γ ⊗_A Γ = (Γ ⊗_A Γ)[u, u⁻¹, r, s, t]`, the pushout of `Γ ⊗_A Γ` along the target
`ρ = map η_R ∘ η_R` of its universal composable pair and of `Γ` along `η_L`. In it, `Δ ⊗ id` is
`pushoutLift (algebraMap ∘ Δ, map ρ)`, and `id ⊗ Δ` is `pushoutLift (algebraMap ∘ algebraMap,
map (map η_R) ∘ Δ)`, where `map (map η_R)` is the inclusion of the last two factors.

```lean
TauCeti.WeierstrassHopfAlgebroid.coproduct_coassoc :
  TauCeti.WeierstrassHopfAlgebroid.coproductLeft.comp TauCeti.WeierstrassHopfAlgebroid.coproduct =
    ((TauCeti.WeierstrassChange.ChangeRing.pushoutLift TauCeti.WeierstrassHopfAlgebroid.rightUnit)
          ⟨((algebraMap
                    (TauCeti.WeierstrassChange.ChangeRing
                      TauCeti.WeierstrassHopfAlgebroid.ArrowRing)
                    (TauCeti.WeierstrassChange.ChangeRing
                      (TauCeti.WeierstrassChange.ChangeRing
                        TauCeti.WeierstrassHopfAlgebroid.ArrowRing))).comp
                (algebraMap TauCeti.WeierstrassHopfAlgebroid.ArrowRing
                  (TauCeti.WeierstrassChange.ChangeRing
                    TauCeti.WeierstrassHopfAlgebroid.ArrowRing)),
              (TauCeti.WeierstrassChange.ChangeRing.map
                    (TauCeti.WeierstrassChange.ChangeRing.map
                      TauCeti.WeierstrassHopfAlgebroid.rightUnit)).comp
                TauCeti.WeierstrassHopfAlgebroid.coproduct),
            ⋯⟩).comp
      TauCeti.WeierstrassHopfAlgebroid.coproduct
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.WeierstrassHopfAlgebroid.coproduct_coassoc`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.html#TauCeti.WeierstrassHopfAlgebroid.coproduct_coassoc).

## Sources

- [Tau Ceti documentation: `TauCeti.WeierstrassHopfAlgebroid.coproduct_coassoc`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.html#TauCeti.WeierstrassHopfAlgebroid.coproduct_coassoc)
- [Source of `TauCeti.WeierstrassHopfAlgebroid.coproduct_coassoc` in TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/VariableChange/HopfAlgebroid.lean#L343)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCohomology/STATUS.md)

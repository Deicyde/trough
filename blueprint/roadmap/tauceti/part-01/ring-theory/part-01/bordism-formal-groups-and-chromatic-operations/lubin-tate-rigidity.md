---
declaration: theorem
origin: cited
lean: TauCeti.FormalGroupHom.eq_of_map_residue_eq
statement: formalized
proof: formalized
---

# Lubin–Tate rigidity

Let `A` be an `𝔪`-adically Hausdorff local ring whose residue field
has characteristic `p`, and let `F` and `G` be commutative formal group laws over `A` such that
the reduction of `F` has finite height. Then a homomorphism from `F` to `G` is determined by its
reduction to the residue field.

```lean
TauCeti.FormalGroupHom.eq_of_map_residue_eq.{u_1} {A : Type u_1} [CommRing A] {F G : FormalGroup A}
  [IsLocalRing A] [IsHausdorff (IsLocalRing.maximalIdeal A) A] [G.IsComm] {p : ℕ}
  [hp : Fact (Nat.Prime p)] [CharP (IsLocalRing.ResidueField A) p] [F.IsComm]
  (f g : TauCeti.FormalGroupHom F G) {h : ℕ} (hF : (F.map (IsLocalRing.residue A)).height p = ↑h)
  (hfg :
    (PowerSeries.map (IsLocalRing.residue A)) f.toPowerSeries =
      (PowerSeries.map (IsLocalRing.residue A)) g.toPowerSeries) :
  f = g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FormalGroupHom.eq_of_map_residue_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Rigidity.html#TauCeti.FormalGroupHom.eq_of_map_residue_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.FormalGroupHom.eq_of_map_residue_eq`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Rigidity.html#TauCeti.FormalGroupHom.eq_of_map_residue_eq)
- [Source of `TauCeti.FormalGroupHom.eq_of_map_residue_eq` in TauCeti/RingTheory/FormalGroup/Rigidity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/Rigidity.lean#L182)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)

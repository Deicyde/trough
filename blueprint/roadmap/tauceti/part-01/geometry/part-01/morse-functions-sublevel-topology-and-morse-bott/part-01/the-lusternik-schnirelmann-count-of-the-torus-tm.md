---
declaration: theorem
origin: cited
lean: TauCeti.lsCategoryCount_univ_pi_addCircle
statement: formalized
proof: formalized
---

# The Lusternik–Schnirelmann count of the torus `Tᵐ` is `m + 1`

```lean
TauCeti.lsCategoryCount_univ_pi_addCircle.{u} {ι : Type u} {p : ι → ℝ} [Fintype ι]
  [∀ (i : ι), Fact (0 < p i)] :
  TauCeti.lsCategoryCount ((i : ι) → AddCircle (p i)) Set.univ = ↑(Fintype.card ι) + 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Eilenberg–Zilber theorem for singular chains](../../../../algebraic-topology/singular/the-eilenberg-zilber-theorem-for-singular-chains.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The universal coefficient theorem over a field](../../../../algebraic-topology/cohomology/the-universal-coefficient-theorem-over-a-field.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.lsCategoryCount_univ_pi_addCircle`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/LusternikSchnirelmann/Torus.html#TauCeti.lsCategoryCount_univ_pi_addCircle).

## Sources

- [Tau Ceti documentation: `TauCeti.lsCategoryCount_univ_pi_addCircle`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/LusternikSchnirelmann/Torus.html#TauCeti.lsCategoryCount_univ_pi_addCircle)
- [Source of `TauCeti.lsCategoryCount_univ_pi_addCircle` in TauCeti/Topology/Homotopy/LusternikSchnirelmann/Torus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Homotopy/LusternikSchnirelmann/Torus.lean#L175)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseTheory/STATUS.md)

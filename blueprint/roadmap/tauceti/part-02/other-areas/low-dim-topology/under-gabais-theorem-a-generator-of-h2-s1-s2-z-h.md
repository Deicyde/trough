---
declaration: theorem
origin: cited
lean: TauCeti.GabaiZeroSurgeryGenusTheorem.minimalGenus_circle_prod_sphere
statement: formalized
proof: formalized
---

# Under Gabai's theorem, a generator of `H₂(S¹ × S²; ℤ)` has minimal genus `0`

`S¹ × S²` is
the `0`-surgery on the unknot, which has Seifert genus `0`.

```lean
TauCeti.GabaiZeroSurgeryGenusTheorem.minimalGenus_circle_prod_sphere
  (hG : TauCeti.GabaiZeroSurgeryGenusTheorem)
  {c : ↑(TauCeti.secondHomology (Circle × ↑(Metric.sphere 0 1)))} (hc : ℤ ∙ c = ⊤) :
  TauCeti.minimalGenus c = 0
```

## Depends on

- [The Hurewicz theorem](../../../part-01/algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../../../part-01/algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../../../part-01/algebraic-topology/singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GabaiZeroSurgeryGenusTheorem.minimalGenus_circle_prod_sphere`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/DehnSurgery/ZeroSurgeryGenus.html#TauCeti.GabaiZeroSurgeryGenusTheorem.minimalGenus_circle_prod_sphere), assuming [`TauCeti.GabaiZeroSurgeryGenusTheorem`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/DehnSurgery/ZeroSurgeryGenus.html#TauCeti.GabaiZeroSurgeryGenusTheorem), a proposition Tau Ceti defines.

## Sources

- [Tau Ceti documentation: `TauCeti.GabaiZeroSurgeryGenusTheorem.minimalGenus_circle_prod_sphere`](https://taucetiproject.org/docs/TauCeti/LowDimTopology/DehnSurgery/ZeroSurgeryGenus.html#TauCeti.GabaiZeroSurgeryGenusTheorem.minimalGenus_circle_prod_sphere)
- [Source of `TauCeti.GabaiZeroSurgeryGenusTheorem.minimalGenus_circle_prod_sphere` in TauCeti/LowDimTopology/DehnSurgery/ZeroSurgeryGenus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LowDimTopology/DehnSurgery/ZeroSurgeryGenus.lean#L90)

---
declaration: theorem
origin: cited
lean: TauCeti.GridLink.unknottingNumber_toGridLink_torusLink_le
statement: formalized
proof: formalized
---

# The upper bound of the Milnor conjecture

If `P = p + 1` and `Q = q + 1` are coprime, the
`(P, Q)` torus knot, presented by its standard grid, has unknotting number at most
`(P - 1) (Q - 1) / 2 = p q / 2`.

Following Euclid's algorithm, removing a full twist reduces the `(P, Q + P)` torus knot to the
`(P, Q)` torus knot at the cost of `P choose 2` crossing changes, and transposition exchanges the
roles of `P` and `Q`, until the `(1, 1)` torus knot, the unknot, is reached.

```lean
TauCeti.GridLink.unknottingNumber_toGridLink_torusLink_le (p q : ℕ) (h : (p + 1).Coprime (q + 1)) :
  (TauCeti.GridDiagram.torusLink p q).toGridLink.unknottingNumber ≤ ↑(p * q / 2)
```

## Depends on

- [TauCeti.GridLink.unknottingNumber](tauceti-gridlink-unknottingnumber.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GridLink.unknottingNumber_toGridLink_torusLink_le`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/TorusLink/UnknottingNumber.html#TauCeti.GridLink.unknottingNumber_toGridLink_torusLink_le).

## Sources

- [Tau Ceti documentation: `TauCeti.GridLink.unknottingNumber_toGridLink_torusLink_le`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/TorusLink/UnknottingNumber.html#TauCeti.GridLink.unknottingNumber_toGridLink_torusLink_le)
- [Source of `TauCeti.GridLink.unknottingNumber_toGridLink_torusLink_le` in TauCeti/KnotTheory/Grid/TorusLink/UnknottingNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Grid/TorusLink/UnknottingNumber.lean#L299)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)

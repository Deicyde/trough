---
declaration: def
origin: cited
lean: WeierstrassCurve.bsdQuotient
statement: formalized
---

# The Birch–Swinnerton-Dyer quotient

**The Birch–Swinnerton-Dyer quotient** of an elliptic curve `E` over `ℚ` whose
Shafarevich–Tate group is finite:

  `Ω(E) · Reg(E/ℚ) · #Sha(E/ℚ) · ∏_p c_p / #E(ℚ)_tors²`,

with `Ω(E)` the real period of a global minimal equation, `Reg(E/ℚ)` the regulator of the
Néron–Tate pairing, `c_p` the local Tamagawa number at the prime `p` and `E(ℚ)_tors` the torsion
subgroup of the Mordell–Weil group. The order of `Sha(E/ℚ)` is counted with the finiteness
hypothesis, so the quotient has no value on a curve with infinite `Sha(E/ℚ)`
(`WeierstrassCurve.bsdQuotient_def` restates it with `Nat.card`).

```lean
WeierstrassCurve.bsdQuotient (E : WeierstrassCurve ℚ) [E.IsElliptic] [Finite ↥E.sha] : ℝ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mordell–Weil theorem](the-mordell-weil-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.bsdQuotient`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/BirchSwinnertonDyer/Quotient.html#WeierstrassCurve.bsdQuotient).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.bsdQuotient`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/BirchSwinnertonDyer/Quotient.html#WeierstrassCurve.bsdQuotient)
- [Source of `WeierstrassCurve.bsdQuotient` in TauCeti/AlgebraicGeometry/EllipticCurve/BirchSwinnertonDyer/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/BirchSwinnertonDyer/Quotient.lean#L73)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCurves/STATUS.md)

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

- [The real period of an elliptic curve over `ℚ`](the-real-period-of-an-elliptic-curve-over-q.md)

## Proof depends on

- [The Mordell–Weil theorem](the-mordell-weil-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.bsdQuotient`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/BirchSwinnertonDyer/Quotient.html#WeierstrassCurve.bsdQuotient).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.bsdQuotient`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/BirchSwinnertonDyer/Quotient.html#WeierstrassCurve.bsdQuotient)
- [Source of `WeierstrassCurve.bsdQuotient` in TauCeti/AlgebraicGeometry/EllipticCurve/BirchSwinnertonDyer/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/BirchSwinnertonDyer/Quotient.lean#L73)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)

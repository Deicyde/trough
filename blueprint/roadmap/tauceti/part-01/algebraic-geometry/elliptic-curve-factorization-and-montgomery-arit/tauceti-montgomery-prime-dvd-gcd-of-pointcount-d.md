---
declaration: theorem
origin: cited
lean: TauCeti.Montgomery.prime_dvd_gcd_of_pointCount_dvd
statement: formalized
proof: formalized
---

# TauCeti.Montgomery.prime_dvd_gcd_of_pointCount_dvd

On an elliptic monic model the projective point count can replace the cardinality
of the native group in stage-1 detection.

```lean
TauCeti.Montgomery.prime_dvd_gcd_of_pointCount_dvd {n p m : ℕ} [Fact (Nat.Prime p)] {A B : ZMod p}
  [(TauCeti.Montgomery.model A B).IsElliptic] (hpn : p ∣ n)
  (P : (TauCeti.Montgomery.model A B).toAffine.Point) (R : TauCeti.Montgomery.Pair (ZMod n))
  (hm : (TauCeti.Montgomery.model A B).pointCount ∣ m)
  (hR :
    (TauCeti.Montgomery.Pair.map (ZMod.castHom hpn (ZMod p)) R).cross
        (TauCeti.Montgomery.coordinates A B (m • P)) =
      0) :
  p ∣ R.z.val.gcd n
```

## Depends on

- [TauCeti.Montgomery.coordinates](tauceti-montgomery-coordinates.md)
- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)

## Proof depends on

- [Stage-1 detection by the native group cardinality](stage-1-detection-by-the-native-group-cardinalit.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.prime_dvd_gcd_of_pointCount_dvd`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Detection.html#TauCeti.Montgomery.prime_dvd_gcd_of_pointCount_dvd).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.prime_dvd_gcd_of_pointCount_dvd`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Detection.html#TauCeti.Montgomery.prime_dvd_gcd_of_pointCount_dvd)
- [Source of `TauCeti.Montgomery.prime_dvd_gcd_of_pointCount_dvd` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Detection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Detection.lean#L68)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ECM/STATUS.md)

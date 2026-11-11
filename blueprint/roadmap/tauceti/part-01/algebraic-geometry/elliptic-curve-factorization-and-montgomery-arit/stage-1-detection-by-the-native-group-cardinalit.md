---
declaration: theorem
origin: cited
lean: TauCeti.Montgomery.prime_dvd_gcd_of_card_dvd
statement: formalized
proof: formalized
---

# Stage-1 detection by the native group cardinality

A multiple of the group order
annihilates every point, so a raw pair representing that multiple modulo `p` has denominator
gcd divisible by `p`. No ellipticity assumption is needed on the monic model.

```lean
TauCeti.Montgomery.prime_dvd_gcd_of_card_dvd {n p m : ℕ} [Fact (Nat.Prime p)] {A B : ZMod p}
  (hpn : p ∣ n) (P : (TauCeti.Montgomery.model A B).toAffine.Point)
  (R : TauCeti.Montgomery.Pair (ZMod n))
  (hm : Nat.card (TauCeti.Montgomery.model A B).toAffine.Point ∣ m)
  (hR :
    (TauCeti.Montgomery.Pair.map (ZMod.castHom hpn (ZMod p)) R).cross
        (TauCeti.Montgomery.coordinates A B (m • P)) =
      0) :
  p ∣ R.z.val.gcd n
```

## Depends on

- [TauCeti.Montgomery.coordinates](tauceti-montgomery-coordinates.md)
- [TauCeti.Montgomery.model](tauceti-montgomery-model.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.prime_dvd_gcd_of_card_dvd`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Detection.html#TauCeti.Montgomery.prime_dvd_gcd_of_card_dvd).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.prime_dvd_gcd_of_card_dvd`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Detection.html#TauCeti.Montgomery.prime_dvd_gcd_of_card_dvd)
- [Source of `TauCeti.Montgomery.prime_dvd_gcd_of_card_dvd` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Detection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Detection.lean#L58)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ECM/STATUS.md)

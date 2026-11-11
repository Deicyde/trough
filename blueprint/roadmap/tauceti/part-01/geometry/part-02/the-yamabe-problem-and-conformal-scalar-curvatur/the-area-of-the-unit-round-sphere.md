---
declaration: theorem
origin: cited
lean: TauCeti.roundSphereVolume_eq_two_mul_pi_rpow_div_Gamma
statement: formalized
proof: formalized
---

# The area of the unit round sphere

`|Sⁿ| = 2 π ^ ((n + 1) / 2) / Γ((n + 1) / 2)`.

```lean
TauCeti.roundSphereVolume_eq_two_mul_pi_rpow_div_Gamma (n : ℕ) :
  TauCeti.roundSphereVolume n = 2 * Real.pi ^ ((↑n + 1) / 2) / Real.Gamma ((↑n + 1) / 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.roundSphereVolume_eq_two_mul_pi_rpow_div_Gamma`](https://taucetiproject.org/docs/TauCeti/Geometry/Euclidean/Volume/Sphere.html#TauCeti.roundSphereVolume_eq_two_mul_pi_rpow_div_Gamma).

## Sources

- [Tau Ceti documentation: `TauCeti.roundSphereVolume_eq_two_mul_pi_rpow_div_Gamma`](https://taucetiproject.org/docs/TauCeti/Geometry/Euclidean/Volume/Sphere.html#TauCeti.roundSphereVolume_eq_two_mul_pi_rpow_div_Gamma)
- [Source of `TauCeti.roundSphereVolume_eq_two_mul_pi_rpow_div_Gamma` in TauCeti/Geometry/Euclidean/Volume/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Euclidean/Volume/Sphere.lean#L426)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Yamabe/STATUS.md)

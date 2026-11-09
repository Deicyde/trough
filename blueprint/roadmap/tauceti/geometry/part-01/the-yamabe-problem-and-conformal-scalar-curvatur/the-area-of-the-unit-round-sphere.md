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
- [Source of `TauCeti.roundSphereVolume_eq_two_mul_pi_rpow_div_Gamma` in TauCeti/Geometry/Euclidean/Volume/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Euclidean/Volume/Sphere.lean#L396)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Yamabe/STATUS.md)

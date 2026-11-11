---
declaration: def
origin: cited
lean: WeierstrassCurve.toAbelianVariety
statement: formalized
---

# An elliptic curve is an abelian variety

The projective model `projModel W ⟶ Spec K` of an
elliptic Weierstrass curve over a field, with the group law `grpObjProjModel`, is a proper
geometrically integral group scheme over `Spec K`.

```lean
WeierstrassCurve.toAbelianVariety.{u} {K : Type u} [Field K] (W : WeierstrassCurve K)
  [W.IsElliptic] : TauCeti.AlgebraicGeometry.AbelianVariety K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.toAbelianVariety`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/AbelianVariety.html#WeierstrassCurve.toAbelianVariety).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.toAbelianVariety`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/AbelianVariety.html#WeierstrassCurve.toAbelianVariety)
- [Source of `WeierstrassCurve.toAbelianVariety` in TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/AbelianVariety.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/AbelianVariety.lean#L62)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/JacobianChallenge/STATUS.md)

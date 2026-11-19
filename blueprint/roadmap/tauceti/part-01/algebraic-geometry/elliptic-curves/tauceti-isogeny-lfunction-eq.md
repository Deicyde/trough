---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.LFunction_eq
statement: formalized
proof: formalized
---

# TauCeti.Isogeny.LFunction_eq

Isogenous elliptic curves over a number field have the same L-function as a formal Dirichlet
series, including the Euler factors at all bad places.

```lean
TauCeti.Isogeny.LFunction_eq.{u_1} {K : Type u_1} [Field K] [NumberField K]
  {W₁ W₂ : WeierstrassCurve K} [W₁.IsElliptic] [W₂.IsElliptic]
  (φ : TauCeti.Isogeny W₁.toAffine W₂.toAffine) : W₁.LFunction = W₂.LFunction
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [Dedekind's different theorem, the tame case](../../number-theory/part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The factorisation theorem](../elliptic-curve/the-factorisation-theorem.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The first half of Dedekind's different theorem](../../number-theory/part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Hensel's lemma without monicity](../../ring-theory/part-02/other-results/part-01/hensels-lemma-without-monicity.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The kernel form of the factorisation theorem (Silverman III.4.11)](../elliptic-curve/the-kernel-form-of-the-factorisation-theorem-sil.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../../number-theory/part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.LFunction_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/LFunction/Isogeny.html#TauCeti.Isogeny.LFunction_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.LFunction_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/LFunction/Isogeny.html#TauCeti.Isogeny.LFunction_eq)
- [Source of `TauCeti.Isogeny.LFunction_eq` in TauCeti/AlgebraicGeometry/EllipticCurve/LFunction/Isogeny.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/LFunction/Isogeny.lean#L76)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCurves/STATUS.md)

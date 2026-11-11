---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.existsUnique_comp_iterateRelativeFrobeniusIsogeny_eq
statement: formalized
proof: formalized
---

# The factorisation theorem for isogenies (Silverman II.2.12)

when `p ^ r` is the
inseparable degree of `φ : W₁ → W₂`, it factors through the `r`-fold relative Frobenius
`F^r : W₁ → W₁⁽ᵖʳ⁾` as `φ = χ ∘ F^r` for a unique isogeny `χ : W₁⁽ᵖʳ⁾ → W₂`. The factor is
separable (`isSeparable_of_comp_iterateRelativeFrobeniusIsogeny_eq`), of degree the separable
degree of `φ` (`degree_eq_separableDegree_of_comp_iterateRelativeFrobeniusIsogeny_eq`).

```lean
TauCeti.Isogeny.existsUnique_comp_iterateRelativeFrobeniusIsogeny_eq.{u_1} {F : Type u_1} [Field F]
  (p : ℕ) [ExpChar F p] {W₁ W₂ : WeierstrassCurve.Affine F} (φ : TauCeti.Isogeny W₁ W₂) {r : ℕ}
  (hr : φ.inseparableDegree = p ^ r) :
  ∃! χ, χ.comp (TauCeti.Isogeny.iterateRelativeFrobeniusIsogeny p W₁ r) = φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The factorisation theorem](the-factorisation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.existsUnique_comp_iterateRelativeFrobeniusIsogeny_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/RelativeFrobenius/Factorisation.html#TauCeti.Isogeny.existsUnique_comp_iterateRelativeFrobeniusIsogeny_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.existsUnique_comp_iterateRelativeFrobeniusIsogeny_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/RelativeFrobenius/Factorisation.html#TauCeti.Isogeny.existsUnique_comp_iterateRelativeFrobeniusIsogeny_eq)
- [Source of `TauCeti.Isogeny.existsUnique_comp_iterateRelativeFrobeniusIsogeny_eq` in TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/RelativeFrobenius/Factorisation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Isogeny/RelativeFrobenius/Factorisation.lean#L125)

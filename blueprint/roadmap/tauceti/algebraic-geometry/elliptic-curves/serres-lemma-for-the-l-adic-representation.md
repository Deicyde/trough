---
declaration: theorem
origin: cited
lean: WeierstrassCurve.tateModuleGaloisRepresentation_eq_one_of_isOfFinOrder
statement: formalized
proof: formalized
---

# Serre's lemma for the `ℓ`-adic representation

An automorphism `σ` fixing every point of
`E[ℓ ^ k]`, with `ℓ ^ k ≥ 3`, and acting on `T_ℓ E` with finite order, acts trivially on `T_ℓ E`.

```lean
WeierstrassCurve.tateModuleGaloisRepresentation_eq_one_of_isOfFinOrder.{u_1, u_2} {F : Type u_1}
  {K : Type u_2} [Field F] [Field K] [DecidableEq K] [Algebra F K] {W : WeierstrassCurve F} {ℓ : ℕ}
  [Fact (Nat.Prime ℓ)] {σ : Gal(K/F)} (hσ : IsOfFinOrder ((W.tateModuleGaloisRepresentation ℓ) σ))
  {k : ℕ} (hk : 3 ≤ ℓ ^ k)
  (hfix :
    ∀ (P : (W.baseChange K).toAffine.Point),
      ℓ ^ k • P = 0 → (WeierstrassCurve.Affine.Point.map ↑σ) P = P) :
  (W.tateModuleGaloisRepresentation ℓ) σ = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's lemma on the Tate module](../../algebra/module/serres-lemma-on-the-tate-module.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.tateModuleGaloisRepresentation_eq_one_of_isOfFinOrder`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/Galois.html#WeierstrassCurve.tateModuleGaloisRepresentation_eq_one_of_isOfFinOrder).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.tateModuleGaloisRepresentation_eq_one_of_isOfFinOrder`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/Galois.html#WeierstrassCurve.tateModuleGaloisRepresentation_eq_one_of_isOfFinOrder)
- [Source of `WeierstrassCurve.tateModuleGaloisRepresentation_eq_one_of_isOfFinOrder` in TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/Galois.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/TateModule/Galois.lean#L110)

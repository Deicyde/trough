---
declaration: theorem
origin: cited
lean: RootPairing.Base.neg_inv_two_smul_killingForm_eq_neg_smul
statement: formalized
proof: formalized
---

# The critical level

if the invariant form `Φ` is normalised by `Φ(θ^∨, θ^∨) = 2`, then
`κ_c = -½ κ` is `-h^∨ Φ`.

```lean
RootPairing.Base.neg_inv_two_smul_killingForm_eq_neg_smul.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsSimple K L] {H : LieSubalgebra K L} [H.IsCartanSubalgebra]
  [LieModule.IsTriangularizable K (↥H) L] (b : (LieAlgebra.IsKilling.rootSystem H).Base)
  [IsAlgClosed K] {Φ : LinearMap.BilinForm K L} (hΦ : LinearMap.BilinForm.lieInvariant L Φ)
  (h :
    (Φ ↑((LieAlgebra.IsKilling.rootSystem H).coroot b.highestRoot))
        ↑((LieAlgebra.IsKilling.rootSystem H).coroot b.highestRoot) =
      2) :
  -2⁻¹ • killingForm K L = -↑b.dualCoxeterNumber • Φ
```

## Depends on

- [RootPairing.Base.dualCoxeterNumber](rootpairing-base-dualcoxeternumber.md)

## Proof depends on

- [The Killing form is `2 h^∨` times the invariant form normalised at the highest coroot](the-killing-form-is-2-h-times-the-invariant-form.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.Base.neg_inv_two_smul_killingForm_eq_neg_smul`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/DualCoxeterNumber.html#RootPairing.Base.neg_inv_two_smul_killingForm_eq_neg_smul).

## Sources

- [Tau Ceti documentation: `RootPairing.Base.neg_inv_two_smul_killingForm_eq_neg_smul`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/DualCoxeterNumber.html#RootPairing.Base.neg_inv_two_smul_killingForm_eq_neg_smul)
- [Source of `RootPairing.Base.neg_inv_two_smul_killingForm_eq_neg_smul` in TauCeti/Algebra/Lie/Killing/DualCoxeterNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Killing/DualCoxeterNumber.lean#L209)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)

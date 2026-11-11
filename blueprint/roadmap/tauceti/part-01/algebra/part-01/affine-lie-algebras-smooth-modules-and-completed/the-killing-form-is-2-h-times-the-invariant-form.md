---
declaration: theorem
origin: cited
lean: RootPairing.Base.killingForm_eq_smul_iff_apply_coroot_highestRoot_eq_two
statement: formalized
proof: formalized
---

# The Killing form is `2 h^∨` times the invariant form normalised at the highest coroot

an
invariant form `Φ` on a simple Lie algebra over an algebraically closed field of characteristic
zero satisfies `κ = 2 h^∨ Φ` if and only if `Φ(θ^∨, θ^∨) = 2`.

```lean
RootPairing.Base.killingForm_eq_smul_iff_apply_coroot_highestRoot_eq_two.{u_1, u_2} {K : Type u_1}
  {L : Type u_2} [Field K] [CharZero K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsSimple K L] {H : LieSubalgebra K L} [H.IsCartanSubalgebra]
  [LieModule.IsTriangularizable K (↥H) L] (b : (LieAlgebra.IsKilling.rootSystem H).Base)
  [IsAlgClosed K] {Φ : LinearMap.BilinForm K L} (hΦ : LinearMap.BilinForm.lieInvariant L Φ) :
  killingForm K L = (2 * ↑b.dualCoxeterNumber) • Φ ↔
    (Φ ↑((LieAlgebra.IsKilling.rootSystem H).coroot b.highestRoot))
        ↑((LieAlgebra.IsKilling.rootSystem H).coroot b.highestRoot) =
      2
```

## Depends on

- [RootPairing.Base.dualCoxeterNumber](rootpairing-base-dualcoxeternumber.md)

## Proof depends on

- [Schur's lemma for Lie modules](../../part-02/lie/part-02/schurs-lemma-for-lie-modules.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.Base.killingForm_eq_smul_iff_apply_coroot_highestRoot_eq_two`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/DualCoxeterNumber.html#RootPairing.Base.killingForm_eq_smul_iff_apply_coroot_highestRoot_eq_two).

## Sources

- [Tau Ceti documentation: `RootPairing.Base.killingForm_eq_smul_iff_apply_coroot_highestRoot_eq_two`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/DualCoxeterNumber.html#RootPairing.Base.killingForm_eq_smul_iff_apply_coroot_highestRoot_eq_two)
- [Source of `RootPairing.Base.killingForm_eq_smul_iff_apply_coroot_highestRoot_eq_two` in TauCeti/Algebra/Lie/Killing/DualCoxeterNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Killing/DualCoxeterNumber.lean#L167)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)

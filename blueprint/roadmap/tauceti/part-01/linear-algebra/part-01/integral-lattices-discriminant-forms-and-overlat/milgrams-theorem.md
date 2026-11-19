---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_eq_sigPos_sub_sigNeg, TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_rankOne
statement: formalized
proof: formalized
---

# Milgram's theorem

The Gauss-sum invariant of the discriminant form of an even
nondegenerate lattice is its signature `t₊ - t₋` modulo `8`.

```lean
TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_eq_sigPos_sub_sigNeg.{u} {V : Type u}
  [AddCommGroup V] [_root_.Module ℚ V] (L : TauCeti.IntegralLattice V) [L.IsNondegenerate]
  (hL : L.IsEven) : (L.discriminantQuadraticModule hL).gaussSign = ↑L.sigPos - ↑L.sigNeg
```

## Depends on

- [TauCeti.FiniteQuadraticModule](../../../number-theory/part-01/integral-quadratic-forms-and-lattices/tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice](tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](tauceti-integrallattice-discriminantquadraticmod.md)

## Proof depends on

- [Euler's four-square identity for a quadratic map](../quadratic-form/eulers-four-square-identity-for-a-quadratic-map.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_eq_sigPos_sub_sigNeg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Milgram.html#TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_eq_sigPos_sub_sigNeg).

## Other forms

**Milgram's theorem for `⟨2m⟩`.** Formalized in Tau Ceti as [`TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_rankOne`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Milgram.html#TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_rankOne).

```lean
TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_rankOne (m : ℤ) [NeZero m] :
  ((TauCeti.IntegralLattice.rankOne (2 * m)).discriminantQuadraticModule ⋯).gaussSign = ↑m.sign
```

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_eq_sigPos_sub_sigNeg`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/Milgram.html#TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_eq_sigPos_sub_sigNeg)
- [Source of `TauCeti.IntegralLattice.gaussSign_discriminantQuadraticModule_eq_sigPos_sub_sigNeg` in TauCeti/LinearAlgebra/IntegralLattice/Milgram.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/IntegralLattice/Milgram.lean#L311)
- [Tau Ceti roadmap status: Integral lattices, discriminant forms, and overlattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/IntegralLattices/STATUS.md)

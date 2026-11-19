---
declaration: theorem
origin: cited
lean: RootPairing.orbitSum_ne_zero
statement: formalized
proof: formalized
---

# RootPairing.orbitSum_ne_zero

For an automorphism permuting the simple roots of a base, no orbit sum vanishes: the roots
of an orbit are all positive or all negative, so they cannot cancel.

```lean
RootPairing.orbitSum_ne_zero.{u_1, u_2, u_3, u_4} {ι : Type u_1} {R : Type u_2} {M : Type u_3}
  {N : Type u_4} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] {P : RootPairing ι R M N} [Finite ι] {σ : P.Aut} [CharZero R] {b : P.Base}
  (hσ : ∀ j ∈ b.support, (↑σ).indexEquiv j ∈ b.support) (i : ι) : P.orbitSum σ i ≠ 0
```

## Depends on

- [RootPairing.orbitSum](rootpairing-orbitsum.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.orbitSum_ne_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/OrbitSum.html#RootPairing.orbitSum_ne_zero).

## Sources

- [Tau Ceti documentation: `RootPairing.orbitSum_ne_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/OrbitSum.html#RootPairing.orbitSum_ne_zero)
- [Source of `RootPairing.orbitSum_ne_zero` in TauCeti/LinearAlgebra/RootSystem/OrbitSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/RootSystem/OrbitSum.lean#L299)
- [Tau Ceti roadmap status: Root systems, integral dominance and finite diagram folding, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RootSystemsPartII/STATUS.md)

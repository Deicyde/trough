---
declaration: theorem
origin: cited
lean: TauCeti.Perfectoid.uniformTilt.theta_eq_fontaineTheta
statement: formalized
proof: formalized
---

# TauCeti.Perfectoid.uniformTilt.theta_eq_fontaineTheta

`θ_B` is Mathlib's `fontaineTheta` under the identification `B♭⁺ ≃+* PreTilt B⁺ p`.

```lean
TauCeti.Perfectoid.uniformTilt.theta_eq_fontaineTheta.{u_1} {p : ℕ} {B : Type u_1} [CommRing B]
  [Fact (Nat.Prime p)] [UniformSpace B] [IsUniformAddGroup B] [IsTopologicalRing B]
  [TauCeti.Huber.IsTateRing B] [CompleteSpace B] [T2Space B] [TauCeti.Huber.IsUniform B]
  [hpn : Fact (IsTopologicallyNilpotent ↑p)] {Bplus : Subring B}
  (h : TauCeti.Huber.IsRingOfIntegralElements Bplus) [Nontrivial B] [Fact ¬IsUnit ↑p]
  [IsAdicComplete (Ideal.span {↑p}) ↥Bplus] :
  TauCeti.Perfectoid.uniformTilt.theta p h =
    (WittVector.fontaineTheta (↥Bplus) p).comp
      (WittVector.map (TauCeti.Perfectoid.uniformTilt.plusEquivPreTilt p h).toRingHom)
```

## Depends on

- [TauCeti.Perfectoid.uniformTilt](tauceti-perfectoid-uniformtilt.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Perfectoid.uniformTilt.theta_eq_fontaineTheta`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/UniformTilt/Theta.html#TauCeti.Perfectoid.uniformTilt.theta_eq_fontaineTheta).

## Sources

- [Tau Ceti documentation: `TauCeti.Perfectoid.uniformTilt.theta_eq_fontaineTheta`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfectoid/UniformTilt/Theta.html#TauCeti.Perfectoid.uniformTilt.theta_eq_fontaineTheta)
- [Source of `TauCeti.Perfectoid.uniformTilt.theta_eq_fontaineTheta` in TauCeti/RingTheory/Perfectoid/UniformTilt/Theta.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Perfectoid/UniformTilt/Theta.lean#L159)
- [Tau Ceti roadmap status: Perfectoid rings and spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PerfectoidSpaces/STATUS.md)

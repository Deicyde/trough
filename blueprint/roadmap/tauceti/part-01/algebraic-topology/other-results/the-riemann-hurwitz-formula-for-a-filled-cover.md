---
declaration: theorem
origin: cited
lean: TauCeti.FilledCover.two_mul_genus_sub_two
statement: formalized
proof: formalized
---

# The Riemann–Hurwitz formula for a filled cover

For a connected cover of degree `n`, whose
monodromy triple has genus `g`, the total ramification `∑ (e - 1)` over the added points satisfies
`2 g - 2 = -2 n + ∑ (e - 1)`. This is the shape of the Riemann–Hurwitz formula for a degree-`n`
branched cover of the Riemann sphere, which has genus `0`.

```lean
TauCeti.FilledCover.two_mul_genus_sub_two.{u_1} {E : Type u_1} [TopologicalSpace E]
  {p : E → TauCeti.ThricePuncturedSphere} (hp : IsCoveringMap p) {n : ℕ}
  (ν : ↑(p ⁻¹' {TauCeti.ThricePuncturedSphere.basePt}) ≃ Fin n) [PathConnectedSpace E]
  [Fintype (TauCeti.FilledPoint p)] :
  2 * ↑(hp.monodromyTriple ν).genus - 2 = -2 * ↑n + ∑ i, (↑(TauCeti.FilledCover.degree p i) - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Euler bound for a pair of permutations](../../group-theory/permutations/the-euler-bound-for-a-pair-of-permutations.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FilledCover.two_mul_genus_sub_two`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Ramification.html#TauCeti.FilledCover.two_mul_genus_sub_two).

## Sources

- [Tau Ceti documentation: `TauCeti.FilledCover.two_mul_genus_sub_two`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Ramification.html#TauCeti.FilledCover.two_mul_genus_sub_two)
- [Source of `TauCeti.FilledCover.two_mul_genus_sub_two` in TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Ramification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Ramification.lean#L119)

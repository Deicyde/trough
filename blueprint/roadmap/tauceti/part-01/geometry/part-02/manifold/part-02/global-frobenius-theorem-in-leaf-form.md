---
declaration: theorem
origin: cited
lean: TauCeti.IsContMDiffDistribution.isInvolutiveDistribution_iff_forall_exists_leaf
statement: formalized
proof: formalized
---

# Global Frobenius theorem in leaf form

For `2 ≤ m` and `m + 1 ≤ r`, a `C^m` distribution of
constant rank `k` on a finite-dimensional real `C^r` manifold with boundaryless model is involutive
if and only if every point lies on a connected, injectively parametrized, maximal `C^m` integral
manifold inheriting second countability from `M`.

```lean
TauCeti.IsContMDiffDistribution.isInvolutiveDistribution_iff_forall_exists_leaf.{u, u_1, u_2}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] {M : Type u}
  [tM : TopologicalSpace M] [ChartedSpace H M] {m : ℕ∞} {r : WithTop ℕ∞} [IsManifold I 1 M]
  [IsManifold I r M] {k : ℕ} {D : (x : M) → Submodule ℝ (TangentSpace I x)} (hm : 2 ≤ m)
  (hmr : ↑m + 1 ≤ r) (hD : TauCeti.IsContMDiffDistribution I (↑m) k D) :
  TauCeti.IsInvolutiveDistribution I D ↔
    ∀ (x : M),
      ∃ N,
        x ∈ Set.range N.map ∧
          ConnectedSpace N.carrier ∧
            Function.Injective N.map ∧
              (∀ (N' : TauCeti.IntegralManifold (↑m) D k),
                  ConnectedSpace N'.carrier →
                    (Set.range N'.map ∩ Set.range N.map).Nonempty →
                      Set.range N'.map ⊆ Set.range N.map) ∧
                (SecondCountableTopology M → SecondCountableTopology N.carrier)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Global Frobenius integrability theorem](global-frobenius-integrability-theorem.md)
- [The inverse function theorem for a converging family](../../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)
- [The inverse function theorem for manifolds](the-inverse-function-theorem-for-manifolds.md)
- [The local Frobenius theorem (`TauCeti.IsInvolutiveDistribution.exists_flatChart`)](../part-03/the-local-frobenius-theorem-tauceti-isinvolutive.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsContMDiffDistribution.isInvolutiveDistribution_iff_forall_exists_leaf`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/IntegralManifold/Leaf.html#TauCeti.IsContMDiffDistribution.isInvolutiveDistribution_iff_forall_exists_leaf).

## Sources

- [Tau Ceti documentation: `TauCeti.IsContMDiffDistribution.isInvolutiveDistribution_iff_forall_exists_leaf`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/IntegralManifold/Leaf.html#TauCeti.IsContMDiffDistribution.isInvolutiveDistribution_iff_forall_exists_leaf)
- [Source of `TauCeti.IsContMDiffDistribution.isInvolutiveDistribution_iff_forall_exists_leaf` in TauCeti/Geometry/Manifold/Distribution/IntegralManifold/Leaf.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Distribution/IntegralManifold/Leaf.lean#L517)

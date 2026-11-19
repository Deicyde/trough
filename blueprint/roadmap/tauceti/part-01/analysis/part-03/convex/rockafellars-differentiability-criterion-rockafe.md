---
declaration: theorem
origin: cited
lean: TauCeti.differentiableAt_toReal_iff_subsingleton_subdifferential
statement: formalized
proof: formalized
---

# Rockafellar's differentiability criterion (Rockafellar, *Convex Analysis*, Theorem 25.1)

Let `f : E → EReal` have convex real epigraph and never take the value `⊥` on a finite-dimensional
real inner product space `E`. At an interior point `x` of `{x | f x ≠ ⊤}`, the real representative
`x' ↦ (f x').toReal` is differentiable at `x` if and only if the subdifferential
`subdifferential (innerₗ E) f x` contains at most one element.

```lean
TauCeti.differentiableAt_toReal_iff_subsingleton_subdifferential.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {f : E → EReal}
  (hf : Convex ℝ {p | f p.1 ≤ ↑p.2}) (hbot : ∀ (x : E), f x ≠ ⊥) {x : E}
  (hx : x ∈ interior {x | f x ≠ ⊤}) :
  DifferentiableAt ℝ (fun x' => (f x').toReal) x ↔
    (TauCeti.subdifferential (innerₗ E) f x).Subsingleton
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.differentiableAt_toReal_iff_subsingleton_subdifferential`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SubgradientImage.html#TauCeti.differentiableAt_toReal_iff_subsingleton_subdifferential).

## Sources

- [Tau Ceti documentation: `TauCeti.differentiableAt_toReal_iff_subsingleton_subdifferential`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/SubgradientImage.html#TauCeti.differentiableAt_toReal_iff_subsingleton_subdifferential)
- [Source of `TauCeti.differentiableAt_toReal_iff_subsingleton_subdifferential` in TauCeti/Analysis/Convex/SubgradientImage.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Convex/SubgradientImage.lean#L265)

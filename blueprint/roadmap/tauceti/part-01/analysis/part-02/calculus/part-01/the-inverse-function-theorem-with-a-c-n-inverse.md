---
declaration: theorem
origin: cited
lean: TauCeti.ContDiffOn.exists_openPartialHomeomorph
statement: formalized
proof: formalized
---

# The inverse function theorem, with a `C^n` inverse on the whole target

A map which is
`C^n` on an open set `s`, with `1 ≤ n`, and whose derivative at `a ∈ s` is a continuous linear
equivalence, coincides on a neighbourhood of `a` with an `OpenPartialHomeomorph` whose source is
contained in `s` and whose inverse is `C^n` on its target.

```lean
TauCeti.ContDiffOn.exists_openPartialHomeomorph.{u_1, u_2, u_3} {𝕂 : Type u_1} [RCLike 𝕂]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕂 E] [CompleteSpace E] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace 𝕂 F] {n : WithTop ℕ∞} {g : E → F} {s : Set E} {a : E}
  (hg : ContDiffOn 𝕂 n g s) (hs : IsOpen s) (ha : a ∈ s) (hn : 1 ≤ n) {e : E ≃L[𝕂] F}
  (he : ↑e = fderiv 𝕂 g a) :
  ∃ Θ, ↑Θ = g ∧ a ∈ Θ.source ∧ Θ.source ⊆ s ∧ ContDiffOn 𝕂 n (↑Θ.symm) Θ.target
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContDiffOn.exists_openPartialHomeomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/InverseFunctionTheorem.html#TauCeti.ContDiffOn.exists_openPartialHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.ContDiffOn.exists_openPartialHomeomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/InverseFunctionTheorem.html#TauCeti.ContDiffOn.exists_openPartialHomeomorph)
- [Source of `TauCeti.ContDiffOn.exists_openPartialHomeomorph` in TauCeti/Analysis/Calculus/InverseFunctionTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/InverseFunctionTheorem.lean#L189)

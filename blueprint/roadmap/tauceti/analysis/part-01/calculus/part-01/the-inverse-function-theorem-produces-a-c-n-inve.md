---
declaration: theorem
origin: cited
lean: HasStrictFDerivAt.contDiffOn_toOpenPartialHomeomorph_symm, TauCeti.ContDiffOn.exists_openPartialHomeomorph
statement: formalized
proof: formalized
---

# The inverse function theorem produces a `C^n` inverse

If `f` is `C^n` on the source of the
homeomorphism built by the inverse function theorem, then the inverse is `C^n` on the target.

```lean
HasStrictFDerivAt.contDiffOn_toOpenPartialHomeomorph_symm.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] [CompleteSpace E] {f : E → F} {L : E ≃L[𝕜] F} {a : E}
  {n : WithTop ℕ∞} (hf : HasStrictFDerivAt f (↑L) a)
  (hcont : ContDiffOn 𝕜 n f (HasStrictFDerivAt.toOpenPartialHomeomorph f hf).source) :
  ContDiffOn 𝕜 n (↑(HasStrictFDerivAt.toOpenPartialHomeomorph f hf).symm)
    (HasStrictFDerivAt.toOpenPartialHomeomorph f hf).target
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HasStrictFDerivAt.contDiffOn_toOpenPartialHomeomorph_symm`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/InverseFunctionTheorem.html#HasStrictFDerivAt.contDiffOn_toOpenPartialHomeomorph_symm).

## Other forms

**The inverse function theorem, with a `C^n` inverse on the whole target.** Formalized in Tau Ceti as [`TauCeti.ContDiffOn.exists_openPartialHomeomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/InverseFunctionTheorem.html#TauCeti.ContDiffOn.exists_openPartialHomeomorph).

```lean
TauCeti.ContDiffOn.exists_openPartialHomeomorph.{u_1, u_2, u_3} {𝕂 : Type u_1} [RCLike 𝕂]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕂 E] [CompleteSpace E] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace 𝕂 F] {n : WithTop ℕ∞} {g : E → F} {s : Set E} {a : E}
  (hg : ContDiffOn 𝕂 n g s) (hs : IsOpen s) (ha : a ∈ s) (hn : 1 ≤ n) {e : E ≃L[𝕂] F}
  (he : ↑e = fderiv 𝕂 g a) :
  ∃ Θ, ↑Θ = g ∧ a ∈ Θ.source ∧ Θ.source ⊆ s ∧ ContDiffOn 𝕂 n (↑Θ.symm) Θ.target
```

## Sources

- [Tau Ceti documentation: `HasStrictFDerivAt.contDiffOn_toOpenPartialHomeomorph_symm`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/InverseFunctionTheorem.html#HasStrictFDerivAt.contDiffOn_toOpenPartialHomeomorph_symm)
- [Source of `HasStrictFDerivAt.contDiffOn_toOpenPartialHomeomorph_symm` in TauCeti/Analysis/Calculus/InverseFunctionTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/InverseFunctionTheorem.lean#L129)

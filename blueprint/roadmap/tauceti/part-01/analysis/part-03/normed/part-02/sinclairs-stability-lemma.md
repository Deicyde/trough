---
declaration: theorem
origin: cited
lean: TauCeti.eventuallyConst_separatingSpace
statement: formalized
proof: formalized
---

# Sinclair's stability lemma

Let `E n` and `F` be Banach spaces, let
`R n : E (n + 1) → E n` be continuous linear maps, and let `T n : E n →ₗ F` be linear maps, not
assumed continuous, with `T (n + 1) = T n ∘ R n`, so that `T n = T 0 ∘ R 0 ∘ ⋯ ∘ R (n - 1)`.
Then the decreasing sequence of separating spaces of the `T n` is eventually constant.

```lean
TauCeti.eventuallyConst_separatingSpace.{u_1, u_2, u_3} {𝕜 : Type u_1} {F : Type u_2}
  [NontriviallyNormedField 𝕜] [NormedAddCommGroup F] [NormedSpace 𝕜 F] {E : ℕ → Type u_3}
  [(n : ℕ) → NormedAddCommGroup (E n)] [(n : ℕ) → NormedSpace 𝕜 (E n)]
  {R : (n : ℕ) → E (n + 1) →L[𝕜] E n} [CompleteSpace F] [∀ (n : ℕ), CompleteSpace (E n)]
  {T : (n : ℕ) → E n →ₗ[𝕜] F} (hT : ∀ (n : ℕ), T (n + 1) = T n ∘ₗ ↑(R n)) :
  Filter.EventuallyConst (fun n => (T n).separatingSpace) Filter.atTop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.eventuallyConst_separatingSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SeparatingSpace.html#TauCeti.eventuallyConst_separatingSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.eventuallyConst_separatingSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/SeparatingSpace.html#TauCeti.eventuallyConst_separatingSpace)
- [Source of `TauCeti.eventuallyConst_separatingSpace` in TauCeti/Analysis/Normed/Operator/SeparatingSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/SeparatingSpace.lean#L459)

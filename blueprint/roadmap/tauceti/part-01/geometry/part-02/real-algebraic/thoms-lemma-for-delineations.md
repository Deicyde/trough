---
declaration: theorem
origin: cited
lean: TauCeti.Delineation.root_notMem_uIcc_of_sign_eval_eq
statement: formalized
proof: formalized
---

# Thom's lemma for delineations

Suppose that at a point `x` of the base the derivative of
every member of the family is zero or a member. If every member has the same sign at two distinct
points `t ≠ t'` of the fiber over `x`, then no root function takes a value in `[t, t']` at `x`.

```lean
TauCeti.Delineation.root_notMem_uIcc_of_sign_eval_eq.{u_1, u_3} {X : Type u_1} {ι : Type u_3}
  [TopologicalSpace X] {P : ι → X → Polynomial ℝ} (D : TauCeti.Delineation P) {x : X}
  (hder : ∀ (k : ι), Polynomial.derivative (P k x) = 0 ∨ ∃ l, P l x = Polynomial.derivative (P k x))
  {t t' : ℝ} (htt' : t ≠ t')
  (h :
    ∀ (k : ι),
      SignType.sign (Polynomial.eval t (P k x)) = SignType.sign (Polynomial.eval t' (P k x)))
  (i : Fin D.count) : D.root i x ∉ Set.uIcc t t'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Delineation.root_notMem_uIcc_of_sign_eval_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Stack/Delineation.html#TauCeti.Delineation.root_notMem_uIcc_of_sign_eval_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Delineation.root_notMem_uIcc_of_sign_eval_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Stack/Delineation.html#TauCeti.Delineation.root_notMem_uIcc_of_sign_eval_eq)
- [Source of `TauCeti.Delineation.root_notMem_uIcc_of_sign_eval_eq` in TauCeti/Geometry/RealAlgebraic/Stack/Delineation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/Stack/Delineation.lean#L434)

---
declaration: theorem
origin: cited
lean: ContinuousAlternatingMap.wedgePow_two_apply
statement: formalized
proof: formalized
---

# The Pfaffian formula

the square of a two-form `ω` takes on `(a, b, c, d)` twice the
value `ω(a, b) ω(c, d) - ω(a, c) ω(b, d) + ω(a, d) ω(b, c)`.

```lean
ContinuousAlternatingMap.wedgePow_two_apply.{u_1} {E : Type u_1} [AddCommGroup E]
  [_root_.Module ℝ E] [TopologicalSpace E] (ω : E [⋀^Fin 2]→L[ℝ] ℝ) (a b c d : E) :
  (ω.wedgePow 2) ![a, b, c, d] =
    2 * (ω ![a, b] * ω ![c, d] - ω ![a, c] * ω ![b, d] + ω ![a, d] * ω ![b, c])
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousAlternatingMap.wedgePow_two_apply`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Module/Alternating/Wedge/TwoForm.html#ContinuousAlternatingMap.wedgePow_two_apply).

## Sources

- [Tau Ceti documentation: `ContinuousAlternatingMap.wedgePow_two_apply`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Module/Alternating/Wedge/TwoForm.html#ContinuousAlternatingMap.wedgePow_two_apply)
- [Source of `ContinuousAlternatingMap.wedgePow_two_apply` in TauCeti/Topology/Algebra/Module/Alternating/Wedge/TwoForm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Module/Alternating/Wedge/TwoForm.lean#L113)

---
declaration: theorem
origin: cited
lean: TauCeti.NormedRing.IsTate.banach_steinhaus
statement: formalized
proof: formalized
---

# Banach–Steinhaus theorem (Uniform Boundedness Principle) over a Tate ring

If a family `g : ι → E →L[R] F` of continuous linear maps from a complete seminormed module `E`
over a Tate ring `R` is pointwise bounded, then the operator norms `‖g i‖` are uniformly
bounded.

```lean
TauCeti.NormedRing.IsTate.banach_steinhaus.{u_1, u_2, u_3, u_4} {R : Type u_1} {E : Type u_2}
  {F : Type u_3} [SeminormedRing R] [TauCeti.NormedRing.IsTate R] [SeminormedAddCommGroup E]
  [_root_.Module R E] [IsBoundedSMul R E] [SeminormedAddCommGroup F] [_root_.Module R F]
  [IsBoundedSMul R F] [CompleteSpace E] {ι : Type u_4} (g : ι → E →L[R] F)
  (h : ∀ (x : E), ∃ C, ∀ (i : ι), ‖(g i) x‖ ≤ C) : ∃ C, ∀ (i : ι), ‖g i‖ ≤ C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NormedRing.IsTate.banach_steinhaus`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/UniformBoundedness.html#TauCeti.NormedRing.IsTate.banach_steinhaus).

## Sources

- [Tau Ceti documentation: `TauCeti.NormedRing.IsTate.banach_steinhaus`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/RingOpNorm/UniformBoundedness.html#TauCeti.NormedRing.IsTate.banach_steinhaus)
- [Source of `TauCeti.NormedRing.IsTate.banach_steinhaus` in TauCeti/Analysis/Normed/Operator/RingOpNorm/UniformBoundedness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/RingOpNorm/UniformBoundedness.lean#L71)

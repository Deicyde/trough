---
declaration: theorem
origin: cited
lean: NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall, NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall_zero_one
statement: formalized
proof: formalized
---

# Goldstine's theorem

The weak-star closure of the image of the closed ball `closedBall x r`
under the canonical embedding into the bidual is the closed ball of radius `r` about the image
of `x`.

```lean
NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall.{u_1, u_2} (𝕜 : Type u_1)
  (E : Type u_2) [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] (x : E) (r : ℝ) :
  closure
      (⇑(NormedSpace.inclusionInDoubleDualWeak 𝕜 E) ''
        ⇑(toWeakSpace 𝕜 E) '' Metric.closedBall x r) =
    ⇑WeakDual.toStrongDual ⁻¹' Metric.closedBall ((NormedSpace.inclusionInDoubleDual 𝕜 E) x) r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Goldstine.html#NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall).

## Other forms

**Goldstine's theorem, unit-ball form.** Formalized in Tau Ceti as [`NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall_zero_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Goldstine.html#NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall_zero_one).

```lean
NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall_zero_one.{u_1, u_2} (𝕜 : Type u_1)
  (E : Type u_2) [RCLike 𝕜] [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] :
  closure
      (⇑(NormedSpace.inclusionInDoubleDualWeak 𝕜 E) ''
        ⇑(toWeakSpace 𝕜 E) '' Metric.closedBall 0 1) =
    ⇑WeakDual.toStrongDual ⁻¹' Metric.closedBall 0 1
```

## Sources

- [Tau Ceti documentation: `NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/Goldstine.html#NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall)
- [Source of `NormedSpace.closure_image_inclusionInDoubleDualWeak_closedBall` in TauCeti/Analysis/Normed/Module/Dual/Goldstine.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Dual/Goldstine.lean#L47)

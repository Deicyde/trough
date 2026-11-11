---
declaration: def
origin: cited
lean: TauCeti.ParabolicC2HolderSpace
statement: formalized
---

# TauCeti.ParabolicC2HolderSpace

Bounded order-two parabolic Hölder maps on a nondegenerate closed time slab.
The norm is the sum of the value and gradient supremum norms and the two top-order
supremum-plus-Hölder norms.

```lean
TauCeti.ParabolicC2HolderSpace.{u_1, u_2} (α : NNReal) (E : Type u_1) (F : Type u_2)
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {a b : ℝ}
  (hab : a < b) : Type (max u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Two.html#TauCeti.ParabolicC2HolderSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.ParabolicC2HolderSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Two.html#TauCeti.ParabolicC2HolderSpace)
- [Source of `TauCeti.ParabolicC2HolderSpace` in TauCeti/Analysis/PDE/Parabolic/Holder/Two.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Parabolic/Holder/Two.lean#L174)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PDE/STATUS.md)

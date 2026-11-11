---
declaration: theorem
origin: cited
lean: TauCeti.zigzagGradedCartanMatrix_apply
statement: formalized
proof: formalized
---

# The entrywise graded Cartan formula

The diagonal entries are `1 + q²`, the entries over an
edge are `q`, and all the others vanish.

```lean
TauCeti.zigzagGradedCartanMatrix_apply.{u, w} (k : Type w) [Field k] {V : Type u}
  (G : SimpleGraph V) (hns : ∀ (i : V), ∃ j, G.Adj i j) [Finite V] [DecidableEq V]
  [DecidableRel G.Adj] (i j : V) :
  TauCeti.zigzagGradedCartanMatrix k G i j =
    (if i = j then 1 + Polynomial.X ^ 2 else 0) + if G.Adj i j then Polynomial.X else 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.zigzagGradedCartanMatrix_apply`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/CartanMatrix.html#TauCeti.zigzagGradedCartanMatrix_apply).

## Sources

- [Tau Ceti documentation: `TauCeti.zigzagGradedCartanMatrix_apply`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/CartanMatrix.html#TauCeti.zigzagGradedCartanMatrix_apply)
- [Source of `TauCeti.zigzagGradedCartanMatrix_apply` in TauCeti/RepresentationTheory/Quiver/Zigzag/CartanMatrix.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Zigzag/CartanMatrix.lean#L509)

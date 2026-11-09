---
declaration: theorem
origin: cited
lean: TauCeti.BoundedHolomorphicFunctions.restrict_injective
statement: formalized
proof: formalized
---

# Identity theorem

If `V` is finite-dimensional, `E` is complete, and every connected
component of `U` meets `U'`, then restriction `H^∞(U, E) → H^∞(U', E)` is injective.

```lean
TauCeti.BoundedHolomorphicFunctions.restrict_injective.{u_1, u_2} {V : Type u_1} {E : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup E] [NormedSpace ℂ E]
  {U U' : TopologicalSpace.Opens V} [FiniteDimensional ℂ V] [CompleteSpace E] (h : U' ≤ U)
  (hU' : ∀ x ∈ U, (connectedComponentIn (↑U) x ∩ ↑U').Nonempty) :
  Function.Injective ⇑(TauCeti.BoundedHolomorphicFunctions.restrict h)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Osgood's lemma](../../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BoundedHolomorphicFunctions.restrict_injective`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/HolomorphicFunctions/Bounded.html#TauCeti.BoundedHolomorphicFunctions.restrict_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.BoundedHolomorphicFunctions.restrict_injective`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/HolomorphicFunctions/Bounded.html#TauCeti.BoundedHolomorphicFunctions.restrict_injective)
- [Source of `TauCeti.BoundedHolomorphicFunctions.restrict_injective` in TauCeti/Analysis/Complex/HolomorphicFunctions/Bounded.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/HolomorphicFunctions/Bounded.lean#L290)

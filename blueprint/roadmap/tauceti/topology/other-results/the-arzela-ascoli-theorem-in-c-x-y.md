---
declaration: theorem
origin: cited
lean: ArzelaAscoli.isCompact_closure_of_equicontinuous, ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded
statement: formalized
proof: formalized
---

# The Arzelà–Ascoli theorem in `C(X, Y)`

On a space `X` whose topology is coherent with its
compact sets (for instance a locally compact space), an equicontinuous set of continuous maps
whose values at each point lie in a common compact set has compact closure in the compact-open
topology.

```lean
ArzelaAscoli.isCompact_closure_of_equicontinuous.{u_1, u_2} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [CompactlyCoherentSpace X] [UniformSpace Y] {A : Set C(X, Y)}
  (hA : Equicontinuous fun f => ⇑↑f) (hApt : ∀ (x : X), ∃ Q, IsCompact Q ∧ ∀ f ∈ A, f x ∈ Q) :
  IsCompact (closure A)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ArzelaAscoli.isCompact_closure_of_equicontinuous`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#ArzelaAscoli.isCompact_closure_of_equicontinuous).

## Other forms

**The Arzelà–Ascoli theorem in `C(X, Y)`, with a dense set of points.** Formalized in Tau Ceti as [`ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded).

```lean
ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [CompactlyCoherentSpace X] [UniformSpace Y] [CompleteSpace Y]
  {A : Set C(X, Y)} {D : Set X} (hD : Dense D) (hA : Equicontinuous fun f => ⇑↑f)
  (hAD : ∀ x ∈ D, TotallyBounded ((fun f => f x) '' A)) : IsCompact (closure A)
```

## Sources

- [Tau Ceti documentation: `ArzelaAscoli.isCompact_closure_of_equicontinuous`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#ArzelaAscoli.isCompact_closure_of_equicontinuous)
- [Source of `ArzelaAscoli.isCompact_closure_of_equicontinuous` in TauCeti/Topology/ContinuousMap/Ascoli.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/ContinuousMap/Ascoli.lean#L80)

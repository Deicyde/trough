---
declaration: theorem
origin: cited
lean: TauCeti.leftQuotient_rigidity
statement: formalized
proof: formalized
---

# Left quotient rigidity

On a connected open set (including the empty set),
pointwise existence of a left quotient slope is equivalent to a single left-affine formula.
Only the function's values on the set are constrained.

```lean
TauCeti.leftQuotient_rigidity {f : Quaternion ℝ → Quaternion ℝ} {s : Set (Quaternion ℝ)}
  (hs : IsOpen s) (hc : IsPreconnected s) :
  TauCeti.LeftQuotientDifferentiableOn f s ↔ ∃ a b, ∀ q ∈ s, f q = a + q * b
```

## Depends on

- [TauCeti.HasLeftQuotientFDerivAt](tauceti-hasleftquotientfderivat.md)

## Proof depends on

- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.leftQuotient_rigidity`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Rigidity.html#TauCeti.leftQuotient_rigidity).

## Sources

- [Tau Ceti documentation: `TauCeti.leftQuotient_rigidity`](https://taucetiproject.org/docs/TauCeti/Analysis/Quaternion/Rigidity.html#TauCeti.leftQuotient_rigidity)
- [Source of `TauCeti.leftQuotient_rigidity` in TauCeti/Analysis/Quaternion/Rigidity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Quaternion/Rigidity.lean#L97)
- [Tau Ceti roadmap status: Quaternionic analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuaternionicAnalysis/STATUS.md)

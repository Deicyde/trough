---
declaration: theorem
origin: cited
lean: TauCeti.hasBoundedSublevelsOn_iff_seq
statement: formalized
proof: formalized
---

# TauCeti.hasBoundedSublevelsOn_iff_seq

Bounded sublevels are equivalent to boundedness of every admissible sequence with
bounded-above energies.

```lean
TauCeti.hasBoundedSublevelsOn_iff_seq.{u_1, u_2} {V : Type u_1} {β : Type u_2} [PseudoMetricSpace V]
  [Preorder β] {E : V → β} {S : Set V} :
  TauCeti.HasBoundedSublevelsOn E S ↔
    ∀ (u : ℕ → V),
      (∀ (n : ℕ), u n ∈ S) → BddAbove (Set.range (E ∘ u)) → Bornology.IsBounded (Set.range u)
```

## Depends on

- [TauCeti.HasBoundedSublevelsOn](tauceti-hasboundedsublevelson.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hasBoundedSublevelsOn_iff_seq`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/BoundedSublevels.html#TauCeti.hasBoundedSublevelsOn_iff_seq).

## Sources

- [Tau Ceti documentation: `TauCeti.hasBoundedSublevelsOn_iff_seq`](https://taucetiproject.org/docs/TauCeti/Analysis/Variational/BoundedSublevels.html#TauCeti.hasBoundedSublevelsOn_iff_seq)
- [Source of `TauCeti.hasBoundedSublevelsOn_iff_seq` in TauCeti/Analysis/Variational/BoundedSublevels.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Variational/BoundedSublevels.lean#L223)
- [Tau Ceti roadmap status: Variational methods and constrained spectral theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VariationalMethods/STATUS.md)

---
declaration: theorem
origin: cited
lean: TauCeti.exists_isCirculation_iff
statement: formalized
proof: formalized
---

# Hoffman's circulation theorem

A bounded circulation exists exactly when every vertex
set has total lower bound entering it at most the total upper bound leaving it.

```lean
TauCeti.exists_isCirculation_iff.{u, v, w} {V : Type u} {Q : V → V → Type v} {K : Type w}
  [Fintype V] [(x y : V) → Fintype (Q x y)] [AddCommGroup K] [LinearOrder K] [IsOrderedAddMonoid K]
  [DecidableEq V] {lo hi : TauCeti.Assignment Q K} (hlo : lo ≤ hi) :
  (∃ f ∈ Set.Icc lo hi, TauCeti.IsCirculation f) ↔
    ∀ (S : Finset V), TauCeti.arrowSum lo Sᶜ S ≤ TauCeti.arrowSum hi S Sᶜ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Generalized Hoffman's theorem](generalized-hoffmans-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isCirculation_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Hoffman.html#TauCeti.exists_isCirculation_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isCirculation_iff`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/Hoffman.html#TauCeti.exists_isCirculation_iff)
- [Source of `TauCeti.exists_isCirculation_iff` in TauCeti/Combinatorics/Network/Hoffman.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/Hoffman.lean#L422)

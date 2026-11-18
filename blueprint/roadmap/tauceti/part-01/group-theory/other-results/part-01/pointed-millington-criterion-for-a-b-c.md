---
declaration: theorem
origin: cited
lean: TauCeti.TriangleGroup.markedIsoClass_cosetTriple_eq_iff
statement: formalized
proof: formalized
---

# Pointed Millington criterion for `Δ(a, b, c)`

Two coset triples marked at their base
cosets `e₁ 1` and `e₂ 1` define the same marked isomorphism class if and only if their subgroups
are equal.

```lean
TauCeti.TriangleGroup.markedIsoClass_cosetTriple_eq_iff {a b c n : ℕ}
  {H₁ H₂ : Subgroup (TauCeti.TriangleGroup a b c)} (e₁ : TauCeti.TriangleGroup a b c ⧸ H₁ ≃ Fin n)
  (e₂ : TauCeti.TriangleGroup a b c ⧸ H₂ ≃ Fin n) :
  TauCeti.MarkedIsoClass.mk ⟨TauCeti.TriangleGroup.cosetTriple H₁ e₁, ⋯⟩ (e₁ ↑1) =
      TauCeti.MarkedIsoClass.mk ⟨TauCeti.TriangleGroup.cosetTriple H₂ e₂, ⋯⟩ (e₂ ↑1) ↔
    H₁ = H₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Pointed Millington criterion](../../../algebra/part-02/other-results/pointed-millington-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TriangleGroup.markedIsoClass_cosetTriple_eq_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TriangleGroup/CosetTriple.html#TauCeti.TriangleGroup.markedIsoClass_cosetTriple_eq_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.TriangleGroup.markedIsoClass_cosetTriple_eq_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TriangleGroup/CosetTriple.html#TauCeti.TriangleGroup.markedIsoClass_cosetTriple_eq_iff)
- [Source of `TauCeti.TriangleGroup.markedIsoClass_cosetTriple_eq_iff` in TauCeti/GroupTheory/TriangleGroup/CosetTriple.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/TriangleGroup/CosetTriple.lean#L174)

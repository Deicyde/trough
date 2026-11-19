---
declaration: theorem
origin: cited
lean: TauCeti.TriangleGroup.cosetTriple_equivalent_cosetTriple_iff, TauCeti.TriangleGroup.cosetIsoClassEquiv
statement: formalized
proof: formalized
---

# Millington's theorem for `Δ(a, b, c)` (relational form)

Two coset triples of degree `n`
are isomorphic if and only if the subgroups are conjugate in `Δ(a, b, c)`.

```lean
TauCeti.TriangleGroup.cosetTriple_equivalent_cosetTriple_iff {a b c n : ℕ}
  {H₁ H₂ : Subgroup (TauCeti.TriangleGroup a b c)} (e₁ : TauCeti.TriangleGroup a b c ⧸ H₁ ≃ Fin n)
  (e₂ : TauCeti.TriangleGroup a b c ⧸ H₂ ≃ Fin n) :
  (TauCeti.TriangleGroup.cosetTriple H₁ e₁).Equivalent (TauCeti.TriangleGroup.cosetTriple H₂ e₂) ↔
    ∃ g, g • H₁ = H₂
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Abstract Millington criterion](../../../algebra/part-02/other-results/abstract-millington-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TriangleGroup.cosetTriple_equivalent_cosetTriple_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TriangleGroup/CosetTriple.html#TauCeti.TriangleGroup.cosetTriple_equivalent_cosetTriple_iff).

## Other forms

**Millington's theorem for `Δ(a, b, c)` (bundled bijection).** Formalized in Tau Ceti as [`TauCeti.TriangleGroup.cosetIsoClassEquiv`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TriangleGroup/CosetTriple.html#TauCeti.TriangleGroup.cosetIsoClassEquiv).

```lean
TauCeti.TriangleGroup.cosetIsoClassEquiv {a b c n : ℕ} [NeZero n] :
  MulAction.orbitRel.Quotient (ConjAct (TauCeti.TriangleGroup a b c))
      ↥(Subgroup.ofIndex (TauCeti.TriangleGroup a b c) n) ≃
    ↑(TauCeti.TriangleGroup.connectedIsoClasses a b c n)
```

## Sources

- [Tau Ceti documentation: `TauCeti.TriangleGroup.cosetTriple_equivalent_cosetTriple_iff`](https://taucetiproject.org/docs/TauCeti/GroupTheory/TriangleGroup/CosetTriple.html#TauCeti.TriangleGroup.cosetTriple_equivalent_cosetTriple_iff)
- [Source of `TauCeti.TriangleGroup.cosetTriple_equivalent_cosetTriple_iff` in TauCeti/GroupTheory/TriangleGroup/CosetTriple.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/TriangleGroup/CosetTriple.lean#L164)

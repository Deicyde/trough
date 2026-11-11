---
declaration: theorem
origin: cited
lean: TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq
statement: formalized
proof: formalized
---

# Labute's Theorem 2 for `q ≠ 2`

Let `r, r' ∈ Φ(F)` be relators of the free pro-`p` group
on `n` generators whose presented groups are Demushkin groups with the same `q`-invariant `q ≠ 2`.
Then a continuous automorphism of `F` carries `r` to `r'`; in particular the closed normal
closures of `r` and `r'` are carried to each other.

```lean
TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq {p : ℕ} [Fact (Nat.Prime p)]
  {n : ℕ} {r r' : TauCeti.freeProP p (Fin n)}
  (hr : r ∈ TauCeti.proPFrattini p (TauCeti.freeProP p (Fin n)))
  (hr' : r' ∈ TauCeti.proPFrattini p (TauCeti.freeProP p (Fin n)))
  (hG : TauCeti.IsDemushkin p (TauCeti.presentedProP p (Fin n) {r}))
  (hG' : TauCeti.IsDemushkin p (TauCeti.presentedProP p (Fin n) {r'}))
  (hq : TauCeti.demushkinQ hG = TauCeti.demushkinQ hG') (hq2 : TauCeti.demushkinQ hG ≠ 2) :
  ∃ e, e r = r'
```

## Depends on

- [The Demushkin predicate](the-demushkin-predicate.md)

## Proof depends on

- [The abelianization structure theorem for one-relator pro-`p` groups](../../algebra/part-01/the-abelianization-structure-theorem-for-one-rel.md)
- [Burnside's basis theorem, cardinal form](../../algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The first isomorphism theorem for a surjective strict homomorphism of topological groups](../../algebra/part-01/the-first-isomorphism-theorem-for-a-surjective-s.md)
- [The relative successive-approximation theorem](../part-02/the-relative-successive-approximation-theorem.md)
- [The unconstrained successive-approximation theorem](the-unconstrained-successive-approximation-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.html#TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq)
- [Source of `TauCeti.freeProP.exists_continuousMulEquiv_apply_eq_of_demushkinQ_eq` in TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/Demushkin/NormalForm/Uniqueness.lean#L88)

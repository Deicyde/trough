---
declaration: theorem
origin: cited
lean: TauCeti.TateModule.eq_one_of_isOfFinOrder_of_forall_proj_eq
statement: formalized
proof: formalized
---

# Serre's lemma on the Tate module

An endomorphism of finite order of `T_p A` that induces
the identity on `A[p ^ k]`, with `p ^ k ≥ 3`, is the identity.

```lean
TauCeti.TateModule.eq_one_of_isOfFinOrder_of_forall_proj_eq.{u_1} {p : ℕ} {A : Type u_1}
  [AddCommGroup A] [hp : Fact (Nat.Prime p)] {φ : Module.End ℤ_[p] (TauCeti.TateModule p A)}
  (hφ : IsOfFinOrder φ) {k : ℕ} (hk : 3 ≤ p ^ k)
  (hfix :
    ∀ (t : TauCeti.TateModule p A),
      (TauCeti.TateModule.proj k) (φ t) = (TauCeti.TateModule.proj k) t) :
  φ = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Serre's lemma (`TauCeti.eq_one_of_isOfFinOrder_of_pow_dvd_sub_one`)](../../../ring-theory/part-02/other-results/part-02/serres-lemma-tauceti-eq-one-of-isoffinorder-of-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TateModule.eq_one_of_isOfFinOrder_of_forall_proj_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Torsion/TateModule.html#TauCeti.TateModule.eq_one_of_isOfFinOrder_of_forall_proj_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.TateModule.eq_one_of_isOfFinOrder_of_forall_proj_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/Torsion/TateModule.html#TauCeti.TateModule.eq_one_of_isOfFinOrder_of_forall_proj_eq)
- [Source of `TauCeti.TateModule.eq_one_of_isOfFinOrder_of_forall_proj_eq` in TauCeti/Algebra/Module/Torsion/TateModule.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Module/Torsion/TateModule.lean#L687)

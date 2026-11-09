---
declaration: theorem
origin: cited
lean: TauCeti.Floer.CapClass.mk_eq_mk_iff_action_eq_and_index_eq
statement: formalized
proof: formalized
---

# TauCeti.Floer.CapClass.mk_eq_mk_iff_action_eq_and_index_eq

Two raw caps have the same class exactly when they have the same action and the same grading,
for functions `a` and `m` on raw caps obeying the recapping laws for area and twice the first
Chern number.

```lean
TauCeti.Floer.CapClass.mk_eq_mk_iff_action_eq_and_index_eq.{u_1, u_2} {S : Type u_1} [AddGroup S]
  {ω : S →+ ℝ} {c : S →+ ℤ} {P : Type u_2} [AddTorsor S P] {a : P → ℝ} {m : P → ℤ}
  (ha : ∀ (g : S) (p : P), a (g +ᵥ p) = ω g + a p)
  (hm : ∀ (g : S) (p : P), m (g +ᵥ p) = 2 * c g + m p) {p q : P} :
  Quotient.mk'' p = Quotient.mk'' q ↔ a p = a q ∧ m p = m q
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.Floer.PeriodGroup](tauceti-floer-periodgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.CapClass.mk_eq_mk_iff_action_eq_and_index_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Basic.html#TauCeti.Floer.CapClass.mk_eq_mk_iff_action_eq_and_index_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.CapClass.mk_eq_mk_iff_action_eq_and_index_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/Cap/Basic.html#TauCeti.Floer.CapClass.mk_eq_mk_iff_action_eq_and_index_eq)
- [Source of `TauCeti.Floer.CapClass.mk_eq_mk_iff_action_eq_and_index_eq` in TauCeti/Geometry/Symplectic/Floer/Cap/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Floer/Cap/Basic.lean#L160)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)

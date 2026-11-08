---
declaration: theorem
origin: cited
lean: TauCeti.Floer.NovikovRing.forall_finite_lt_iff_bddAbove_degree
statement: formalized
proof: formalized
---

# TauCeti.Floer.NovikovRing.forall_finite_lt_iff_bddAbove_degree

For a positively monotone pair, a coefficient function on the period group satisfies the
Novikov condition of the Floer Novikov ring exactly when the degrees of its support are bounded
above.

```lean
TauCeti.Floer.NovikovRing.forall_finite_lt_iff_bddAbove_degree.{u_1, u_2} {S : Type u_1}
  [AddGroup S] {R : Type u_2} {ω : S →+ ℝ} {c : S →+ ℤ} [Zero R] {τ : ℝ}
  (h : ∀ (s : S), ω s = τ * ↑(c s)) (hτ : 0 < τ) (g : TauCeti.Floer.PeriodGroup ω c → R) :
  (∀ (C : ℝ), {γ | g γ ≠ 0 ∧ (-TauCeti.Floer.PeriodGroup.area ω c) γ < C}.Finite) ↔
    BddAbove (⇑(TauCeti.Floer.PeriodGroup.degree ω c) '' Function.support g)
```

## Depends on

- [TauCeti.Floer.PeriodGroup](tauceti-floer-periodgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Floer.NovikovRing.forall_finite_lt_iff_bddAbove_degree`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/NovikovRing.html#TauCeti.Floer.NovikovRing.forall_finite_lt_iff_bddAbove_degree).

## Sources

- [Tau Ceti documentation: `TauCeti.Floer.NovikovRing.forall_finite_lt_iff_bddAbove_degree`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/NovikovRing.html#TauCeti.Floer.NovikovRing.forall_finite_lt_iff_bddAbove_degree)
- [Source of `TauCeti.Floer.NovikovRing.forall_finite_lt_iff_bddAbove_degree` in TauCeti/Geometry/Symplectic/Floer/NovikovRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Floer/NovikovRing.lean#L160)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)

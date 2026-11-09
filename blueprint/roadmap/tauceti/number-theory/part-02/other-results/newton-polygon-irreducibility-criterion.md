---
declaration: theorem
origin: cited
lean: Polynomial.irreducible_of_forall_mem_newtonSlopes_eq, Polynomial.irreducible_of_forall_mem_newtonSlopes_eq_div
statement: formalized
proof: formalized
---

# Newton polygon irreducibility criterion

If the valuation takes integer values on
nonzero elements, a polynomial `f` with nonzero constant coefficient whose finite slopes all
equal a rational number `q`, and whose degree is the denominator of `q`, is irreducible.

```lean
Polynomial.irreducible_of_forall_mem_newtonSlopes_eq.{u_1} {K : Type u_1} [Field K]
  {v : AddValuation K (WithTop ℝ)} (hint : ∀ (x : K), x ≠ 0 → ∃ n, v x = ↑↑n) {f : Polynomial K}
  (hf : f.coeff 0 ≠ 0) {q : ℚ} (hq : ∀ m ∈ f.newtonSlopes v, m = ↑q) (hden : q.den = f.natDegree) :
  Irreducible f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.irreducible_of_forall_mem_newtonSlopes_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Irreducible.html#Polynomial.irreducible_of_forall_mem_newtonSlopes_eq).

## Other forms

**Newton polygon irreducibility criterion, coprime form.** Formalized in Tau Ceti as [`Polynomial.irreducible_of_forall_mem_newtonSlopes_eq_div`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Irreducible.html#Polynomial.irreducible_of_forall_mem_newtonSlopes_eq_div).

```lean
Polynomial.irreducible_of_forall_mem_newtonSlopes_eq_div.{u_1} {K : Type u_1} [Field K]
  {v : AddValuation K (WithTop ℝ)} (hint : ∀ (x : K), x ≠ 0 → ∃ n, v x = ↑↑n) {f : Polynomial K}
  (hf : f.coeff 0 ≠ 0) (hdeg : 0 < f.natDegree) {a : ℤ} (hcop : a.natAbs.Coprime f.natDegree)
  (ha : ∀ m ∈ f.newtonSlopes v, m = ↑a / ↑f.natDegree) : Irreducible f
```

## Sources

- [Tau Ceti documentation: `Polynomial.irreducible_of_forall_mem_newtonSlopes_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Irreducible.html#Polynomial.irreducible_of_forall_mem_newtonSlopes_eq)
- [Source of `Polynomial.irreducible_of_forall_mem_newtonSlopes_eq` in TauCeti/NumberTheory/NewtonPolygon/Irreducible.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NewtonPolygon/Irreducible.lean#L92)

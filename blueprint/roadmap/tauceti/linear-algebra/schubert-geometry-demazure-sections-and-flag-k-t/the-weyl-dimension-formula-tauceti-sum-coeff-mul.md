---
declaration: theorem
origin: cited
lean: TauCeti.sum_coeff_mul_prod_coroot'_weylVector_eq, TauCeti.sum_coeff_mul_prod_form_weylVector_root_eq
statement: formalized
proof: formalized
---

# The Weyl dimension formula (`TauCeti.sum_coeff_mul_prod_coroot'_weylVector_eq`)

If `f · Δ = N(λ)` and `g · Δ = N(0)` in `ℤ[M]`, then the
sums of the coefficients of `f` and `g` satisfy

`(∑ f) ∏_{α>0} ⟨ρ, α^∨⟩ = (∑ g) ∏_{α>0} ⟨λ+ρ, α^∨⟩`.

For the formal character `f = ch L(λ)` of an irreducible module and `g = ch L(0) = 1` this is
`dim L(λ) ∏_{α>0} ⟨ρ, α^∨⟩ = ∏_{α>0} ⟨λ+ρ, α^∨⟩`, the division-free form of
`dim L(λ) = ∏_{α>0} ⟨λ+ρ, α^∨⟩ / ⟨ρ, α^∨⟩`. An invariant form on the root pairing is needed for
the proof, though it does not appear in the statement.

```lean
TauCeti.sum_coeff_mul_prod_coroot'_weylVector_eq.{u, v, w, x} {ι : Type u} {R : Type v} {M : Type w}
  {N : Type x} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] (P : RootPairing ι R M N) [Finite ι] [CharZero R] (b : P.Base) [Algebra ℚ R]
  [IsDomain R] [Invertible 2] [P.IsCrystallographic] [P.IsReduced] [Fintype ↥P.weylGroup]
  (B : P.InvariantForm) {f g : AddMonoidAlgebra ℤ M} {lam : M}
  (hf : f * TauCeti.weylDenominator P b = TauCeti.weylNumerator P b lam)
  (hg : g * TauCeti.weylDenominator P b = TauCeti.weylNumerator P b 0) :
  ↑(f.coeff.sum fun x n => n) *
      ∏ i ∈ TauCeti.posRootsFinset P b, (P.coroot' i) (TauCeti.weylVector P b) =
    ↑(g.coeff.sum fun x n => n) *
      ∏ i ∈ TauCeti.posRootsFinset P b, (P.coroot' i) (lam + TauCeti.weylVector P b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_coeff_mul_prod_coroot'_weylVector_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Dimension.html#TauCeti.sum_coeff_mul_prod_coroot'_weylVector_eq).

## Other forms

**The Weyl dimension formula, in terms of an invariant form.** Formalized in Tau Ceti as [`TauCeti.sum_coeff_mul_prod_form_weylVector_root_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Dimension.html#TauCeti.sum_coeff_mul_prod_form_weylVector_root_eq).

```lean
TauCeti.sum_coeff_mul_prod_form_weylVector_root_eq.{u, v, w, x} {ι : Type u} {R : Type v}
  {M : Type w} {N : Type x} [CommRing R] [AddCommGroup M] [_root_.Module R M] [AddCommGroup N]
  [_root_.Module R N] (P : RootPairing ι R M N) [Finite ι] [CharZero R] (b : P.Base) [Algebra ℚ R]
  [IsDomain R] [Invertible 2] [P.IsCrystallographic] [P.IsReduced] [Fintype ↥P.weylGroup]
  (B : P.InvariantForm) {f g : AddMonoidAlgebra ℤ M} {lam : M}
  (hf : f * TauCeti.weylDenominator P b = TauCeti.weylNumerator P b lam)
  (hg : g * TauCeti.weylDenominator P b = TauCeti.weylNumerator P b 0) :
  ↑(f.coeff.sum fun x n => n) *
      ∏ i ∈ TauCeti.posRootsFinset P b, (B.form (TauCeti.weylVector P b)) (P.root i) =
    ↑(g.coeff.sum fun x n => n) *
      ∏ i ∈ TauCeti.posRootsFinset P b, (B.form (lam + TauCeti.weylVector P b)) (P.root i)
```

## Sources

- [Tau Ceti documentation: `TauCeti.sum_coeff_mul_prod_coroot'_weylVector_eq`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Dimension.html#TauCeti.sum_coeff_mul_prod_coroot'_weylVector_eq)
- [Source of `TauCeti.sum_coeff_mul_prod_coroot'_weylVector_eq` in TauCeti/LinearAlgebra/RootSystem/Weyl/Dimension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/Weyl/Dimension.lean#L186)

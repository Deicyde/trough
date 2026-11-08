---
declaration: theorem
origin: cited
lean: RootPairing.weylDenominator_mul_prod_map_demazureOperator_single, RootPairing.weylDenominator_mul_prod_map_demazureOperator
statement: formalized
proof: formalized
---

# Demazure's formula on a basis element

`D_{w₀}(e^λ)` is Weyl's quotient. For a reduced word
`ω` of the longest element `w₀` and a weight `λ`,

`Δ · D_{w₀}(e^λ) = ∑_{w ∈ W} sgn(w) e^{w λ - (ρ - w ρ)}`,

the alternating sum over the dot orbit `w ⬝ λ = w(λ + ρ) - ρ`.

```lean
RootPairing.weylDenominator_mul_prod_map_demazureOperator_single.{u_1, u_2, u_3} {ι : Type u_1}
  {M : Type u_2} {N : Type u_3} [AddCommGroup M] [AddCommGroup N] (P : RootPairing ι ℤ M N)
  [Finite ι] (b : P.Base) [P.IsReduced] [Fintype ↥P.weylGroup] {ω : List ↥b.support}
  (hω : (TauCeti.weylCoxeterSystem P b).IsReduced ω)
  (hdesc :
    ∀ (i : ↥b.support),
      (TauCeti.weylCoxeterSystem P b).IsLeftDescent ((TauCeti.weylCoxeterSystem P b).wordProd ω) i)
  (lam : M) :
  TauCeti.weylDenominator P b *
      (List.map (fun m => P.demazureOperator ↑m) ω).prod (AddMonoidAlgebra.single lam 1) =
    ∑ w,
      ↑((TauCeti.weylSign P b) w) •
        AddMonoidAlgebra.single (w • lam - ∑ i ∈ TauCeti.inversionsFinset P b w⁻¹, P.root i) 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The localization identity of the Demazure operator](the-localization-identity-of-the-demazure-operat.md)
- [Matsumoto's theorem, relational form](matsumotos-theorem-relational-form.md)
- [The Weyl denominator identity](../root-system/the-weyl-denominator-identity.md)

## Lean

Formalized in Tau Ceti as [`RootPairing.weylDenominator_mul_prod_map_demazureOperator_single`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/LongestElement.html#RootPairing.weylDenominator_mul_prod_map_demazureOperator_single).

## Other forms

**Demazure's formula for the longest element.** Formalized in Tau Ceti as [`RootPairing.weylDenominator_mul_prod_map_demazureOperator`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/LongestElement.html#RootPairing.weylDenominator_mul_prod_map_demazureOperator).

```lean
RootPairing.weylDenominator_mul_prod_map_demazureOperator.{u_1, u_2, u_3} {ι : Type u_1}
  {M : Type u_2} {N : Type u_3} [AddCommGroup M] [AddCommGroup N] (P : RootPairing ι ℤ M N)
  [Finite ι] (b : P.Base) [P.IsReduced] [Fintype ↥P.weylGroup] {ω : List ↥b.support}
  (hω : (TauCeti.weylCoxeterSystem P b).IsReduced ω)
  (hdesc :
    ∀ (i : ↥b.support),
      (TauCeti.weylCoxeterSystem P b).IsLeftDescent ((TauCeti.weylCoxeterSystem P b).wordProd ω) i)
  (f : AddMonoidAlgebra ℤ M) :
  TauCeti.weylDenominator P b * (List.map (fun m => P.demazureOperator ↑m) ω).prod f =
    (P.dotAlternatization b) f
```

## Sources

- [Tau Ceti documentation: `RootPairing.weylDenominator_mul_prod_map_demazureOperator_single`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/LongestElement.html#RootPairing.weylDenominator_mul_prod_map_demazureOperator_single)
- [Source of `RootPairing.weylDenominator_mul_prod_map_demazureOperator_single` in TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/LongestElement.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/RootSystem/Weyl/Demazure/LongestElement.lean#L145)

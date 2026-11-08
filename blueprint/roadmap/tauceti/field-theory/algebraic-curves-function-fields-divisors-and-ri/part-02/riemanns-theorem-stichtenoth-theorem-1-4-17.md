---
declaration: theorem
origin: cited
lean: TauCeti.Divisor.degree_add_one_sub_genus_le_dim, TauCeti.Divisor.degree_add_one_sub_dim_le_genus, TauCeti.Divisor.degree_add_one_le_dim_ratFunc
statement: formalized
proof: formalized
---

# Riemann's theorem (Stichtenoth, Theorem 1.4.17)

`ℓ(D) ≥ deg D + 1 - g`.  No hypothesis on
the constant field is needed for the inequality.

```lean
TauCeti.Divisor.degree_add_one_sub_genus_le_dim.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k]
  [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F) (D : TauCeti.Divisor k F) :
  TauCeti.Divisor.degree D + 1 - ↑(TauCeti.genus k F) ≤ ↑D.dim
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Divisor.degree_add_one_sub_genus_le_dim`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.html#TauCeti.Divisor.degree_add_one_sub_genus_le_dim).

## Other forms

**Riemann's theorem (Stichtenoth, Theorem 1.4.17), in the form that unwinds the definition of the genus.** Formalized in Tau Ceti as [`TauCeti.Divisor.degree_add_one_sub_dim_le_genus`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.html#TauCeti.Divisor.degree_add_one_sub_dim_le_genus).

```lean
TauCeti.Divisor.degree_add_one_sub_dim_le_genus.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k]
  [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F) (D : TauCeti.Divisor k F) :
  TauCeti.Divisor.degree D + 1 - ↑D.dim ≤ ↑(TauCeti.genus k F)
```

**Riemann's theorem on `k(x)`, with the genus evaluated.** Formalized in Tau Ceti as [`TauCeti.Divisor.degree_add_one_le_dim_ratFunc`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/RatFunc.html#TauCeti.Divisor.degree_add_one_le_dim_ratFunc).

```lean
TauCeti.Divisor.degree_add_one_le_dim_ratFunc.{u_1} {k : Type u_1} [Field k]
  (D : TauCeti.Divisor k (RatFunc k)) : TauCeti.Divisor.degree D + 1 ≤ ↑D.dim
```

## Sources

- [Tau Ceti documentation: `TauCeti.Divisor.degree_add_one_sub_genus_le_dim`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.html#TauCeti.Divisor.degree_add_one_sub_genus_le_dim)
- [Source of `TauCeti.Divisor.degree_add_one_sub_genus_le_dim` in TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.lean#L225)

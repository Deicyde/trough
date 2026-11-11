---
declaration: theorem
origin: cited
lean: TauCeti.Divisor.degree_add_one_sub_dim_le_genus, TauCeti.Divisor.degree_add_one_sub_genus_le_dim, TauCeti.Divisor.degree_add_one_le_dim_ratFunc
statement: formalized
proof: formalized
---

# Riemann's theorem

**Riemann's theorem** (Stichtenoth, Theorem 1.4.17), in the form that unwinds the definition
of the genus: `deg D + 1 - ℓ(D) ≤ g` for every divisor `D`.

```lean
TauCeti.Divisor.degree_add_one_sub_dim_le_genus.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k]
  [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F) (D : TauCeti.Divisor k F) :
  TauCeti.Divisor.degree D + 1 - ↑D.dim ≤ ↑(TauCeti.genus k F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The weak approximation theorem](the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Divisor.degree_add_one_sub_dim_le_genus`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.html#TauCeti.Divisor.degree_add_one_sub_dim_le_genus).

## Other forms

**Riemann's theorem (Stichtenoth, Theorem 1.4.17).** Formalized in Tau Ceti as [`TauCeti.Divisor.degree_add_one_sub_genus_le_dim`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.html#TauCeti.Divisor.degree_add_one_sub_genus_le_dim).

```lean
TauCeti.Divisor.degree_add_one_sub_genus_le_dim.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k]
  [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F) (D : TauCeti.Divisor k F) :
  TauCeti.Divisor.degree D + 1 - ↑(TauCeti.genus k F) ≤ ↑D.dim
```

**Riemann's theorem on `k(x)`, with the genus evaluated.** Formalized in Tau Ceti as [`TauCeti.Divisor.degree_add_one_le_dim_ratFunc`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/RatFunc.html#TauCeti.Divisor.degree_add_one_le_dim_ratFunc).

```lean
TauCeti.Divisor.degree_add_one_le_dim_ratFunc.{u_1} {k : Type u_1} [Field k]
  (D : TauCeti.Divisor k (RatFunc k)) : TauCeti.Divisor.degree D + 1 ≤ ↑D.dim
```

## Sources

- [Tau Ceti documentation: `TauCeti.Divisor.degree_add_one_sub_dim_le_genus`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.html#TauCeti.Divisor.degree_add_one_sub_dim_le_genus)
- [Source of `TauCeti.Divisor.degree_add_one_sub_dim_le_genus` in TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/FunctionField/RiemannRoch/Genus.lean#L218)

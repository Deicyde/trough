---
declaration: theorem
origin: cited
lean: Representation.mul_coeff_reverse_charpoly_eq_neg_sum
statement: formalized
proof: formalized
---

# Newton's identities in character form

the coefficients `c_r` of `det (1 - X ρ g)`, the
reverse of the characteristic polynomial of `ρ g`, satisfy
`r c_r = -(c_(r-1) χ(g) + c_(r-2) χ(g ^ 2) + ⋯ + c_0 χ(g ^ r))`, in every characteristic.

```lean
Representation.mul_coeff_reverse_charpoly_eq_neg_sum.{u_1, u_2, u_4} {k : Type u_1} {G : Type u_2}
  {V : Type u_4} [Field k] [Monoid G] [AddCommGroup V] [_root_.Module k V] [FiniteDimensional k V]
  (ρ : Representation k G V) (g : G) (r : ℕ) :
  ↑r * (ρ g).charpoly.reverse.coeff r =
    -∑ j ∈ Finset.range r, (ρ g).charpoly.reverse.coeff (r - (j + 1)) * ρ.character (g ^ (j + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Newton's identities](../../linear-algebra/part-01/matrix/newtons-identities.md)

## Lean

Formalized in Tau Ceti as [`Representation.mul_coeff_reverse_charpoly_eq_neg_sum`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Character/Charpoly.html#Representation.mul_coeff_reverse_charpoly_eq_neg_sum).

## Sources

- [Tau Ceti documentation: `Representation.mul_coeff_reverse_charpoly_eq_neg_sum`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Character/Charpoly.html#Representation.mul_coeff_reverse_charpoly_eq_neg_sum)
- [Source of `Representation.mul_coeff_reverse_charpoly_eq_neg_sum` in TauCeti/RepresentationTheory/Character/Charpoly.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Character/Charpoly.lean#L50)

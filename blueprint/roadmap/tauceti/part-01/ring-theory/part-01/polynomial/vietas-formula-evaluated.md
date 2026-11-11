---
declaration: theorem
origin: cited
lean: Multiset.prod_map_sub_eq_sum_esymm, Multiset.prod_map_sub_eq_pow_add_sum_esymm
statement: formalized
proof: formalized
---

# Vieta's formula, evaluated

`∏_{w ∈ s} (v - w) = ∑_{i=0}^{m} (-1)ⁱ eᵢ(s) v^(m-i)`, where
`m` is the cardinality of `s`.

```lean
Multiset.prod_map_sub_eq_sum_esymm.{u_1} {R : Type u_1} [CommRing R] (s : Multiset R) (v : R) :
  (Multiset.map (fun w => v - w) s).prod =
    ∑ i ∈ Finset.range (s.card + 1), (-1) ^ i * s.esymm i * v ^ (s.card - i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Multiset.prod_map_sub_eq_sum_esymm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Vieta.html#Multiset.prod_map_sub_eq_sum_esymm).

## Other forms

**Vieta's formula, evaluated, with the leading term separated.** Formalized in Tau Ceti as [`Multiset.prod_map_sub_eq_pow_add_sum_esymm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Vieta.html#Multiset.prod_map_sub_eq_pow_add_sum_esymm).

```lean
Multiset.prod_map_sub_eq_pow_add_sum_esymm.{u_1} {R : Type u_1} [CommRing R] {s : Multiset R}
  {m : ℕ} (hs : s.card = m) (v : R) :
  (Multiset.map (fun w => v - w) s).prod =
    v ^ m + ∑ j ∈ Finset.Icc 1 m, (-1) ^ j * s.esymm j * v ^ (m - j)
```

## Sources

- [Tau Ceti documentation: `Multiset.prod_map_sub_eq_sum_esymm`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Vieta.html#Multiset.prod_map_sub_eq_sum_esymm)
- [Source of `Multiset.prod_map_sub_eq_sum_esymm` in TauCeti/RingTheory/Polynomial/Vieta.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Polynomial/Vieta.lean#L97)

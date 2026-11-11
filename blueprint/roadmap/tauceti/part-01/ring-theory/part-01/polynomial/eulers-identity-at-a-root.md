---
declaration: theorem
origin: cited
lean: Multiset.sum_mul_esymm_eq_mul_prod_map_sub_erase
statement: formalized
proof: formalized
---

# Euler's identity at a root

If `v ∈ s` and `s` has `m` elements, then
`∑_{j=1}^{m} (-1)^(j-1) v^(m-j) j e_j(s) = v ∏_{w ∈ s ∖ v} (v - w)`: at a zero `v` of
`P = ∏_{w ∈ s} (W - w)`, `v P'(v) = m P(v) - ∑ (-1)ʲ j e_j(s) v^(m-j)`.

```lean
Multiset.sum_mul_esymm_eq_mul_prod_map_sub_erase.{u_1} {R : Type u_1} [CommRing R] {s : Multiset R}
  {v : R} {m : ℕ} [DecidableEq R] (hs : s.card = m) (hv : v ∈ s) :
  ∑ j ∈ Finset.Icc 1 m, (-1) ^ (j - 1) * v ^ (m - j) * (↑j * s.esymm j) =
    v * (Multiset.map (fun w => v - w) (s.erase v)).prod
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Vieta's formula, evaluated](vietas-formula-evaluated.md)

## Lean

Formalized in Tau Ceti as [`Multiset.sum_mul_esymm_eq_mul_prod_map_sub_erase`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Vieta.html#Multiset.sum_mul_esymm_eq_mul_prod_map_sub_erase).

## Sources

- [Tau Ceti documentation: `Multiset.sum_mul_esymm_eq_mul_prod_map_sub_erase`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/Vieta.html#Multiset.sum_mul_esymm_eq_mul_prod_map_sub_erase)
- [Source of `Multiset.sum_mul_esymm_eq_mul_prod_map_sub_erase` in TauCeti/RingTheory/Polynomial/Vieta.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Polynomial/Vieta.lean#L155)

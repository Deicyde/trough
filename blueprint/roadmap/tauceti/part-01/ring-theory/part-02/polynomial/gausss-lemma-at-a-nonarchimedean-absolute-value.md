---
declaration: theorem
origin: cited
lean: Polynomial.IsPrimitive.gaussNorm_map_eq_one
statement: formalized
proof: formalized
---

# Gauss's lemma at a nonarchimedean absolute value

A primitive polynomial with integer
coefficients has Gauss norm of radius one equal to `1` at every nonarchimedean absolute value,
in any characteristic.

```lean
Polynomial.IsPrimitive.gaussNorm_map_eq_one.{u_1} {R : Type u_1} [Ring R] [Nontrivial R]
  {v : AbsoluteValue R ℝ} (hna : IsNonarchimedean ⇑v) {p : Polynomial ℤ} (hp : p.IsPrimitive) :
  Polynomial.gaussNorm v 1 (Polynomial.map (Int.castRingHom R) p) = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.IsPrimitive.gaussNorm_map_eq_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/GaussNorm.html#Polynomial.IsPrimitive.gaussNorm_map_eq_one).

## Sources

- [Tau Ceti documentation: `Polynomial.IsPrimitive.gaussNorm_map_eq_one`](https://taucetiproject.org/docs/TauCeti/RingTheory/Polynomial/GaussNorm.html#Polynomial.IsPrimitive.gaussNorm_map_eq_one)
- [Source of `Polynomial.IsPrimitive.gaussNorm_map_eq_one` in TauCeti/RingTheory/Polynomial/GaussNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Polynomial/GaussNorm.lean#L134)

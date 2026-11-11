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
- [Source of `Polynomial.IsPrimitive.gaussNorm_map_eq_one` in TauCeti/RingTheory/Polynomial/GaussNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Polynomial/GaussNorm.lean#L134)

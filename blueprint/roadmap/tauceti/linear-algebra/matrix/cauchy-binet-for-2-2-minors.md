---
declaration: theorem
origin: cited
lean: Matrix.pairMinor_mul, Matrix.pairMinor_mul_fin_four
statement: formalized
proof: formalized
---

# Cauchy--Binet for `2 × 2` minors

A minor of a product is the sum, over the increasing
pairs of the middle index type, of the products of the corresponding minors of the two factors.

```lean
Matrix.pairMinor_mul.{u, u_1, u_2, u_3} {m : Type u_1} {n : Type u_2} {R : Type u} [CommRing R]
  {l : Type u_3} [Fintype l] [LinearOrder l] (g : Matrix m l R) (h : Matrix l n R) (p : m × m)
  (q : n × n) : (g * h).pairMinor p q = ∑ ij with ij.1 < ij.2, g.pairMinor p ij * h.pairMinor ij q
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.pairMinor_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Minor.html#Matrix.pairMinor_mul).

## Other forms

**Cauchy--Binet across a four-element middle index type, with the six increasing pairs written out.** Formalized in Tau Ceti as [`Matrix.pairMinor_mul_fin_four`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Minor.html#Matrix.pairMinor_mul_fin_four).

```lean
Matrix.pairMinor_mul_fin_four.{u, u_1, u_2} {m : Type u_1} {n : Type u_2} {R : Type u} [CommRing R]
  (g : Matrix m (Fin 4) R) (h : Matrix (Fin 4) n R) (p : m × m) (q : n × n) :
  (g * h).pairMinor p q =
    g.pairMinor p (0, 1) * h.pairMinor (0, 1) q + g.pairMinor p (0, 2) * h.pairMinor (0, 2) q +
            g.pairMinor p (0, 3) * h.pairMinor (0, 3) q +
          g.pairMinor p (1, 2) * h.pairMinor (1, 2) q +
        g.pairMinor p (1, 3) * h.pairMinor (1, 3) q +
      g.pairMinor p (2, 3) * h.pairMinor (2, 3) q
```

## Sources

- [Tau Ceti documentation: `Matrix.pairMinor_mul`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Minor.html#Matrix.pairMinor_mul)
- [Source of `Matrix.pairMinor_mul` in TauCeti/LinearAlgebra/Matrix/Minor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Matrix/Minor.lean#L125)

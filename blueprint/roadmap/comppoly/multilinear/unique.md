---
catalog: module
lean: CompPoly.CMlPolynomialEval.vertex, CompPoly.CMlPolynomialEval.exists_vertex_get_eq, CompPoly.CMlPolynomialEval.lagrangeBasis_vertex, CompPoly.CMlPolynomialEval.eval_vertex, CompPoly.CMlPolynomialEval.ext_of_eval_vertex, CompPoly.CMlPolynomial.monomialBasis_vertex, CompPoly.CMlPolynomial.eval_vertex, CompPoly.CMlPolynomial.eval_lagrangeToMono_vertex, CompPoly.CMlPolynomial.ext_of_eval_vertex, CompPoly.CMlPolynomial.eval_toMvPolynomial, CompPoly.CMlPolynomial.degreeOf_toMvPolynomial_le_one, CompPoly.CMlPolynomial.toMvPolynomial_eq_of_eval_vertex, CompPoly.CMlPolynomialEval.eval_toMvPolynomial_vertex, CompPoly.CMlPolynomialEval.toMvPolynomial_eq_of_eval_vertex
statement: formalized
proof: formalized
---

# Multilinear extensions on the Boolean hypercube

`CompPoly.Multilinear.Unique`, in [CompPoly/Multilinear/Unique.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean), by Thomas Coratger.

> - evaluation: a hypercube table evaluates to its entries at the Boolean vertices.
> - bridge: a coefficient form and its `MvPolynomial` image evaluate alike at every point.
> - uniqueness: no other polynomial of degree at most one per variable has those vertex values.
>
> So the multilinear extension computed by CompPoly is the multilinear extension.
>
> The reference is Thaler, "Proofs, Arguments, and Zero-Knowledge", Lemma 3.6.

`CompPoly.CMlPolynomialEval.vertex` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L35))

> The Boolean vertex with index `i`, in little-endian order: coordinate `j` is bit `j` of `i`.

```lean
def vertex [Zero R] [One R] (i : Fin (2 ^ n)) : Vector R n
```

`CompPoly.CMlPolynomialEval.exists_vertex_get_eq` (theorem, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L39))

> Every point with coordinates in `{0, 1}` is a Boolean vertex.

```lean
theorem exists_vertex_get_eq [Zero R] [One R] {x : Fin n → R}
    (hx : ∀ j, x j = 0 ∨ x j = 1) : ∃ i : Fin (2 ^ n), (vertex i).get = x
```

`CompPoly.CMlPolynomialEval.lagrangeBasis_vertex` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L65))

> At a Boolean vertex the Lagrange basis is the indicator of that vertex.

```lean
theorem lagrangeBasis_vertex (i k : Fin (2 ^ n)) :
    (lagrangeBasis (vertex (R := R) i))[(k : ℕ)] = if i = k then 1 else 0
```

`CompPoly.CMlPolynomialEval.eval_vertex` (theorem, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L80))

> A hypercube table evaluates to its entry `i` at the vertex `i`.

```lean
theorem eval_vertex (p : CMlPolynomialEval R n) (i : Fin (2 ^ n)) :
    eval p (vertex i) = p[i]
```

`CompPoly.CMlPolynomialEval.ext_of_eval_vertex` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L89))

> Hypercube tables with the same values at every vertex are equal.

```lean
theorem ext_of_eval_vertex {p q : CMlPolynomialEval R n}
    (h : ∀ i : Fin (2 ^ n), eval p (vertex i) = eval q (vertex i)) : p = q
```

`CompPoly.CMlPolynomial.monomialBasis_vertex` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L100))

> At a Boolean vertex the monomial basis indicates the bitwise subsets of that vertex.

```lean
theorem monomialBasis_vertex [CommSemiring R] (i k : Fin (2 ^ n)) :
    (monomialBasis (vertex (R := R) i))[(k : ℕ)] = if (i : ℕ) &&& k = k then 1 else 0
```

`CompPoly.CMlPolynomial.eval_vertex` (theorem, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L123))

> A coefficient form evaluates at the vertex `i` to entry `i` of its hypercube table.

```lean
theorem eval_vertex [CommRing R] (p : CMlPolynomial R n) (i : Fin (2 ^ n)) :
    eval p (vertex i) = (monoToLagrange n p)[i]
```

`CompPoly.CMlPolynomial.eval_lagrangeToMono_vertex` (theorem, [line 131](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L131))

> The coefficient form of a hypercube table evaluates to the table entries at the vertices.

```lean
theorem eval_lagrangeToMono_vertex [CommRing R] (f : CMlPolynomialEval R n) (i : Fin (2 ^ n)) :
    eval (lagrangeToMono n f) (vertex i) = f[i]
```

`CompPoly.CMlPolynomial.ext_of_eval_vertex` (theorem, [line 137](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L137))

> Coefficient forms with the same values at every vertex are equal.

```lean
theorem ext_of_eval_vertex [CommRing R] {p q : CMlPolynomial R n}
    (h : ∀ i : Fin (2 ^ n), eval p (vertex i) = eval q (vertex i)) : p = q
```

`CompPoly.CMlPolynomial.eval_toMvPolynomial` (theorem, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L144))

> The `MvPolynomial` image of a coefficient form evaluates like it at every point.

```lean
theorem eval_toMvPolynomial [CommSemiring R] (p : CMlPolynomial R n) (x : Vector R n) :
    MvPolynomial.eval x.get (toMvPolynomial p) = eval p x
```

`CompPoly.CMlPolynomial.degreeOf_toMvPolynomial_le_one` (theorem, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L154))

> The `MvPolynomial` image of a coefficient form has degree at most one in each variable.

```lean
theorem degreeOf_toMvPolynomial_le_one [CommSemiring R] (p : CMlPolynomial R n) (j : Fin n) :
    (toMvPolynomial p).degreeOf j ≤ 1
```

`CompPoly.CMlPolynomial.toMvPolynomial_eq_of_eval_vertex` (theorem, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L163))

> The `MvPolynomial` image of a coefficient form is fixed by its vertex values.
>
> Any polynomial of degree at most one per variable that matches the form on the vertices equals it.

```lean
theorem toMvPolynomial_eq_of_eval_vertex [CommRing R] [IsDomain R] {p : CMlPolynomial R n}
    {q : MvPolynomial (Fin n) R} (hq : ∀ j, q.degreeOf j ≤ 1)
    (h : ∀ i : Fin (2 ^ n), MvPolynomial.eval (vertex i).get q = eval p (vertex i)) :
    toMvPolynomial p = q
```

`CompPoly.CMlPolynomialEval.eval_toMvPolynomial_vertex` (theorem, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L178))

> The `MvPolynomial` image of a hypercube table evaluates to entry `i` at the vertex `i`.

```lean
theorem eval_toMvPolynomial_vertex (f : CMlPolynomialEval R n) (i : Fin (2 ^ n)) :
    MvPolynomial.eval (vertex i).get (toMvPolynomial f) = f[i]
```

`CompPoly.CMlPolynomialEval.toMvPolynomial_eq_of_eval_vertex` (theorem, [line 186](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean#L186))

> The `MvPolynomial` image of a hypercube table is its unique multilinear extension.
>
> Any polynomial of degree at most one per variable taking the table values on the vertices equals it.

```lean
theorem toMvPolynomial_eq_of_eval_vertex [IsDomain R] {f : CMlPolynomialEval R n}
    {q : MvPolynomial (Fin n) R} (hq : ∀ j, q.degreeOf j ≤ 1)
    (h : ∀ i : Fin (2 ^ n), MvPolynomial.eval (vertex i).get q = f[i]) :
    toMvPolynomial f = q
```

## Depends on

- [Equivalence between `CMlPolynomial` and multilinear polynomials in `MvPolynomial`](equiv.md)

## Proof depends on

- [Fast ↔ Spec equivalence for the multilinear zeta / Möbius transforms](transformequiv.md)
- [Polynomials of degree at most one per variable](../tomathlib/mvpolynomial/nullstellensatz.md)

## Sources

- [CompPoly/Multilinear/Unique.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Multilinear/Unique.lean)
- [Declaration ledger](../../../sources/comppoly/CompPoly.Multilinear.Unique.json)

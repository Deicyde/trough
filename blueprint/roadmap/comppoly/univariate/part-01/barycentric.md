---
catalog: module
lean: CompPoly.CPolynomial.CLagrange.BarycentricDomain, CompPoly.CPolynomial.CLagrange.BarycentricDomain.mk', CompPoly.CPolynomial.CLagrange.BarycentricDomain.weights_eq_nodalWeight, CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval, CompPoly.CPolynomial.CLagrange.BarycentricDomain.evalStep, CompPoly.CPolynomial.CLagrange.BarycentricDomain.evalFast, CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval_eq_evalFast, CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval_at_node, CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval_eq_interpolate_eval, CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval_eq_cinterpolate_eval, CompPoly.CPolynomial.CLagrange.BarycentricDomain.ofPow, CompPoly.CPolynomial.CLagrange.BarycentricDomain.ofPow_eval_eq_interpolatePow_eval
statement: formalized
proof: formalized
---

# Barycentric Interpolation

`CompPoly.Univariate.Barycentric`, in [CompPoly/Univariate/Barycentric.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean), by Elias Judin, Aristotle (Harmonic).

> This file provides a **fixed-domain barycentric interpolation** structure and evaluator
> for univariate computable polynomials.
>
> ## Main definitions
>
> * `CLagrange.BarycentricDomain` – a structure bundling `n` distinct nodes in `R` together with
>   precomputed barycentric weights `w_i = ∏_{j ≠ i} (x_i − x_j)⁻¹`.
>
> * `CLagrange.BarycentricDomain.eval` – the standard second-form barycentric evaluator:
>   - if `z` equals a node `x_i`, returns `y_i` (the explicit node-hit fast path);
>   - otherwise returns
>     `(∑ w_i y_i / (z − x_i)) / (∑ w_i / (z − x_i))`.
>
> ## Main results
>
> * `weights_eq_nodalWeight` – stored weights agree with `Lagrange.nodalWeight`.
> * `eval_at_node` – the evaluator returns `y i` at node `x_i`.
> * `eval_eq_cinterpolate_eval` – the evaluator equals
>   `(CLagrange.interpolate Finset.univ nodes y).eval z`.
> * `eval_eq_interpolate_eval` – variant in terms of `Lagrange.interpolate`.
> * `ofPow_eval_eq_interpolatePow_eval` – specialization to `CLagrange.interpolatePow`.

`CompPoly.CPolynomial.CLagrange.BarycentricDomain` (structure, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L50))

> A fixed-domain barycentric interpolation structure.
>
> Bundles `n` distinct evaluation nodes together with precomputed barycentric weights.
> The evaluator `BarycentricDomain.eval` can then be called repeatedly for different
> value vectors and query points with no redundant per-query work on the nodes.

```lean
structure BarycentricDomain (R : Type*) [Field R] [DecidableEq R] (n : ℕ) where
  /-- The evaluation nodes. -/
  nodes : Fin n → R
  /-- The nodes are pairwise distinct. -/
  nodes_injective : Function.Injective nodes
  /-- Precomputed barycentric weights. -/
  weights : Fin n → R
  /-- The stored weights satisfy the standard product-inverse formula:
  `w_i = ∏_{j ≠ i} (x_i − x_j)⁻¹`. -/
  weights_spec : ∀ i, weights i =
    ((Finset.univ : Finset (Fin n)).erase i).prod (fun j => (nodes i - nodes j)⁻¹)
```

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.mk'` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L66))

> Construct a `BarycentricDomain` from nodes and an injectivity proof,
> computing the weights automatically.

```lean
def BarycentricDomain.mk' (nodes : Fin n → R) (hinj : Function.Injective nodes) :
    BarycentricDomain R n
```

> ### Weight correctness

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.weights_eq_nodalWeight` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L81))

> The stored weights are exactly `Lagrange.nodalWeight Finset.univ nodes`.

```lean
theorem BarycentricDomain.weights_eq_nodalWeight (dom : BarycentricDomain R n) (i : Fin n) :
    dom.weights i = Lagrange.nodalWeight Finset.univ dom.nodes i
```

> ### The barycentric evaluator

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval` (definition, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L94))

> The standard second-form barycentric evaluator.
>
> * If `z` equals a node `x_i`, returns `y i` (the explicit node-hit fast path).
>   The node-hit is found by a computable finite search over `Fin n` via `Fin.find`.
> * Otherwise returns
>   `(∑ i, w_i * y_i * (z − x_i)⁻¹) / (∑ i, w_i * (z − x_i)⁻¹)`,
>   the classical barycentric ratio.

```lean
def BarycentricDomain.eval (dom : BarycentricDomain R n) (y : Fin n → R) (z : R) : R
```

> ### One-inversion evaluation

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.evalStep` (definition, [line 107](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L107))

> One step of the single-inversion barycentric fold.
>
> The state `(a, b, p)` carries both barycentric sums over a common denominator: after the
> nodes `l` it is `(p·∑ wᵢyᵢ/dᵢ, p·∑ wᵢ/dᵢ, p)` with `p = ∏ dᵢ` and `dᵢ = z - xᵢ`.

```lean
def BarycentricDomain.evalStep (dom : BarycentricDomain R n) (y : Fin n → R) (z : R)
    (acc : R × R × R) (i : Fin n) : R × R × R
```

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.evalFast` (definition, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L117))

> The barycentric evaluator with a single field division off the nodes.
>
> It agrees with `eval` everywhere (`eval_eq_evalFast`), and the compiler uses it in place of
> `eval`.

```lean
def BarycentricDomain.evalFast (dom : BarycentricDomain R n) (y : Fin n → R) (z : R) : R
```

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval_eq_evalFast` (theorem, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L141))

> The single-division evaluator agrees with the two-sum evaluator.

```lean
theorem BarycentricDomain.eval_eq_evalFast :
    @BarycentricDomain.eval = @BarycentricDomain.evalFast
```

> ### Evaluation at a node

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval_at_node` (theorem, [line 159](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L159))

> At a node, the barycentric evaluator returns the corresponding value.

```lean
theorem BarycentricDomain.eval_at_node (dom : BarycentricDomain R n) (y : Fin n → R)
    (i : Fin n) : dom.eval y (dom.nodes i) = y i
```

> ### Equivalence with `Lagrange.interpolate`

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval_eq_interpolate_eval` (theorem, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L191))

```lean
theorem BarycentricDomain.eval_eq_interpolate_eval (dom : BarycentricDomain R n)
    (y : Fin n → R) (z : R) :
    dom.eval y z = (Lagrange.interpolate Finset.univ dom.nodes y).eval z
```

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.eval_eq_cinterpolate_eval` (theorem, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L208))

> The barycentric evaluator equals
> `(CLagrange.interpolate Finset.univ dom.nodes y).eval z`.

```lean
theorem BarycentricDomain.eval_eq_cinterpolate_eval [BEq R] [LawfulBEq R]
    (dom : BarycentricDomain R n) (y : Fin n → R) (z : R) :
    dom.eval y z = (CLagrange.interpolate Finset.univ dom.nodes y).eval z
```

> ### Specialization to `interpolatePow`

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.ofPow` (definition, [line 217](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L217))

> Build a barycentric domain from a primitive root of unity `ω` with
> `n ≤ orderOf ω`, so nodes are `ω^0, ω^1, …, ω^{n-1}`.

```lean
def BarycentricDomain.ofPow (ω : Rˣ) (hord : n ≤ orderOf ω) :
    BarycentricDomain R n
```

`CompPoly.CPolynomial.CLagrange.BarycentricDomain.ofPow_eval_eq_interpolatePow_eval` (theorem, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean#L227))

> The barycentric evaluator on power-of-ω nodes agrees with
> `(CLagrange.interpolatePow ω r).eval z`.

```lean
theorem BarycentricDomain.ofPow_eval_eq_interpolatePow_eval [BEq R] [LawfulBEq R]
    (ω : Rˣ) (hord : n ≤ orderOf ω) (r : Vector R n) (z : R) :
    (BarycentricDomain.ofPow ω hord).eval r.get z =
    (CLagrange.interpolatePow ω.1 r).eval z
```

## Depends on

- [Lagrange Interpolation](lagrange.md)

## Sources

- [CompPoly/Univariate/Barycentric.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Barycentric.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.Barycentric.json)

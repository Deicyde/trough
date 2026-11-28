---
catalog: module
lean: CompPoly.CPolynomial.NTT.evalOnCoset, CompPoly.CPolynomial.NTT.size_evalOnCoset, CompPoly.CPolynomial.NTT.Coset.scale, CompPoly.CPolynomial.NTT.Coset.size_scale, CompPoly.CPolynomial.NTT.Coset.getD_scale, CompPoly.CPolynomial.NTT.Coset.eval_eq_sum_fin, CompPoly.CPolynomial.NTT.Coset.natDegree_lt_of_size_le, CompPoly.CPolynomial.NTT.Coset.eval_scale, CompPoly.CPolynomial.NTT.Coset.eval_scale_inv, CompPoly.CPolynomial.NTT.Coset.forwardImpl, CompPoly.CPolynomial.NTT.Coset.inverseImpl, CompPoly.CPolynomial.NTT.Coset.forwardImpl_eq_evalOnCoset, CompPoly.CPolynomial.NTT.Coset.natDegree_inverseImpl_lt, CompPoly.CPolynomial.NTT.Coset.inverseImpl_eval_node_eq, CompPoly.CPolynomial.NTT.Coset.inverseImpl_evalOnCoset_eq, CompPoly.CPolynomial.NTT.Coset.forwardImpl_inverseImpl, CompPoly.CPolynomial.NTT.Coset.interpolate, CompPoly.CPolynomial.NTT.Coset.eval_interpolate_node, CompPoly.CPolynomial.NTT.Coset.interpolate_eq_interpolate
statement: formalized
proof: formalized
---

# Coset NTT

`CompPoly.Univariate.NTT.Coset`, in [CompPoly/Univariate/NTT/Coset.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean), by Derek Sorensen.

> Evaluation and interpolation on a multiplicative coset `g·⟨ω⟩ = {g·ωᵏ}` of an NTT domain,
> the shape of a STARK/FRI low-degree extension. Both reduce to the plain transform by
> scaling coefficients: `p(g·x) = (∑ gʲ pⱼ xʲ)`, so evaluating `p` on the coset is the
> forward NTT of `(gʲ pⱼ)ⱼ`, and interpolating on the coset is the inverse NTT followed by
> scaling with `g⁻¹`.
>
> ## Main definitions
>
> * `NTT.Coset.scale g m a`: the coefficient array `(gʲ · aⱼ)ⱼ<m`.
> * `NTT.evalOnCoset D g p`: `p` evaluated at every coset node `g·ωᵏ`, in natural order.
> * `NTT.Coset.forwardImpl`, `NTT.Coset.inverseImpl`: the coset transforms.
> * `NTT.Coset.interpolate`: interpolation of natural-order values on the coset.
>
> ## Main results
>
> * `NTT.Coset.eval_scale`: `(scale g m p).eval x = p.eval (g * x)` below the size bound.
> * `NTT.Coset.forwardImpl_eq_evalOnCoset`: the coset forward transform evaluates on the coset.
> * `NTT.Coset.inverseImpl_evalOnCoset_eq`: the coset inverse transform interpolates.
> * `NTT.Coset.interpolate_eq_interpolate`: coset interpolation is Lagrange interpolation on
>   the nodes `g·ωᵏ`.

`CompPoly.CPolynomial.NTT.evalOnCoset` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L50))

> Evaluate a raw polynomial at every coset node `g·ωᵏ`, in natural order.

```lean
def evalOnCoset (D : Domain R) (g : R) (p : CPolynomial.Raw R) : Array R
```

`CompPoly.CPolynomial.NTT.size_evalOnCoset` (theorem, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L53))

```lean
theorem size_evalOnCoset (D : Domain R) (g : R) (p : CPolynomial.Raw R) :
    (evalOnCoset D g p).size = D.n
```

`CompPoly.CPolynomial.NTT.Coset.scale` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L60))

> Scale the first `m` coefficients by powers of `g`: `(gʲ · aⱼ)ⱼ<m`.

```lean
def scale (g : R) (m : Nat) (a : Array R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTT.Coset.size_scale` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L63))

```lean
theorem size_scale (g : R) (m : Nat) (a : Array R) : (scale g m a).size = m
```

`CompPoly.CPolynomial.NTT.Coset.getD_scale` (theorem, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L66))

```lean
theorem getD_scale (g : R) (m : Nat) (a : Array R) (j : Nat) (hj : j < m) :
    (scale g m a).getD j 0 = g ^ j * a.getD j 0
```

`CompPoly.CPolynomial.NTT.Coset.eval_eq_sum_fin` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L71))

> A raw polynomial below degree `m` is the sum of its first `m` monomials.

```lean
theorem eval_eq_sum_fin (p : CPolynomial.Raw R) (m : Nat)
    (hdeg : p.toPoly.natDegree < m) (x : R) :
    p.eval x = ∑ j : Fin m, p.getD j 0 * x ^ (j : Nat)
```

`CompPoly.CPolynomial.NTT.Coset.natDegree_lt_of_size_le` (theorem, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L81))

> A raw polynomial of size at most `m > 0` has degree below `m`.

```lean
theorem natDegree_lt_of_size_le (p : CPolynomial.Raw R) {m : Nat} (hm : 0 < m)
    (hsize : p.size ≤ m) : p.toPoly.natDegree < m
```

`CompPoly.CPolynomial.NTT.Coset.eval_scale` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L94))

> Scaling coefficients by powers of `g` composes the polynomial with `x ↦ g·x`.

```lean
theorem eval_scale (g : R) (m : Nat) (p : CPolynomial.Raw R)
    (hdeg : p.toPoly.natDegree < m) (x : R) :
    CPolynomial.Raw.eval x (scale g m p) = p.eval (g * x)
```

`CompPoly.CPolynomial.NTT.Coset.eval_scale_inv` (theorem, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L106))

> Scaling by `g` and then by `g⁻¹` restores the first `m` coefficients.

```lean
theorem eval_scale_inv (g : R) (hg : g ≠ 0) (m : Nat) (p : CPolynomial.Raw R)
    (hdeg : p.toPoly.natDegree < m) (x : R) :
    CPolynomial.Raw.eval (g * x) (scale g⁻¹ m p) = p.eval x
```

`CompPoly.CPolynomial.NTT.Coset.forwardImpl` (definition, [line 112](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L112))

> Forward transform on the coset `g·⟨ω⟩`: values `p(g·ωᵏ)` in natural order.

```lean
def forwardImpl (D : Domain R) (g : R) (p : CPolynomial.Raw R) : Array R
```

`CompPoly.CPolynomial.NTT.Coset.inverseImpl` (definition, [line 116](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L116))

> Inverse transform on the coset `g·⟨ω⟩`, from natural-order values.

```lean
def inverseImpl (D : Domain R) (g : R) (v : Array R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTT.Coset.forwardImpl_eq_evalOnCoset` (theorem, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L120))

> The coset forward transform evaluates the polynomial on the coset.

```lean
theorem forwardImpl_eq_evalOnCoset (D : Domain R) (g : R) (p : CPolynomial.Raw R)
    (hdeg : p.toPoly.natDegree < D.n) :
    forwardImpl D g p = evalOnCoset D g p
```

`CompPoly.CPolynomial.NTT.Coset.natDegree_inverseImpl_lt` (theorem, [line 133](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L133))

> The coset inverse transform has degree below the domain size.

```lean
theorem natDegree_inverseImpl_lt (D : Domain R) (g : R) (v : Array R) :
    (inverseImpl D g v).toPoly.natDegree < D.n
```

`CompPoly.CPolynomial.NTT.Coset.inverseImpl_eval_node_eq` (theorem, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L138))

> The coset inverse transform takes each value at its coset node.

```lean
theorem inverseImpl_eval_node_eq (D : Domain R) (g : R) (hg : g ≠ 0) (v : Array R)
    (k : D.Idx) :
    CPolynomial.Raw.eval (g * D.node k) (inverseImpl D g v) = v.getD k.1 0
```

`CompPoly.CPolynomial.NTT.Coset.inverseImpl_evalOnCoset_eq` (theorem, [line 148](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L148))

> The coset inverse transform evaluates back to its input on the coset.

```lean
theorem inverseImpl_evalOnCoset_eq (D : Domain R) (g : R) (hg : g ≠ 0) (v : Array R) :
    evalOnCoset D g (inverseImpl D g v) = loadNaturalArray D v
```

`CompPoly.CPolynomial.NTT.Coset.forwardImpl_inverseImpl` (theorem, [line 157](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L157))

> The coset forward transform inverts the coset inverse transform.

```lean
theorem forwardImpl_inverseImpl (D : Domain R) (g : R) (hg : g ≠ 0) (v : Array R) :
    forwardImpl D g (inverseImpl D g v) = loadNaturalArray D v
```

`CompPoly.CPolynomial.NTT.Coset.interpolate` (definition, [line 163](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L163))

> Interpolate natural-order values on the coset `g·⟨ω⟩`, in `O(n log n)`.

```lean
def interpolate [BEq R] [LawfulBEq R] (D : Domain R) (g : R) (values : Vector R D.n) :
    CPolynomial R
```

`CompPoly.CPolynomial.NTT.Coset.eval_interpolate_node` (theorem, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L169))

> Coset interpolation takes each value at its coset node.

```lean
theorem eval_interpolate_node [BEq R] [LawfulBEq R] (D : Domain R) (g : R) (hg : g ≠ 0)
    (values : Vector R D.n) (k : D.Idx) :
    (interpolate D g values).eval (g * D.node k) = values.get k
```

`CompPoly.CPolynomial.NTT.Coset.interpolate_eq_interpolate` (theorem, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean#L178))

> Coset interpolation is Lagrange interpolation on the nodes `g·ωᵏ`.

```lean
theorem interpolate_eq_interpolate [BEq R] [LawfulBEq R] (D : Domain R) (g : R) (hg : g ≠ 0)
    (values : Vector R D.n) :
    interpolate D g values =
      CLagrange.interpolate Finset.univ (fun k : D.Idx => g * D.node k) values.get
```

## Depends on

- [Lagrange Interpolation](../lagrange.md)
- [Inverse NTT](inverse.md)

## Proof depends on

- [NTT and Interpolation](interpolation.md)
- [`C`, `eval₂`, and coefficient-mapping as ring homomorphisms](../../part-02/topoly/ringhom.md)

## Sources

- [CompPoly/Univariate/NTT/Coset.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Coset.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.Coset.json)

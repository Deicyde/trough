---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.powersAux, CompPoly.CPolynomial.NTTFast.powers, CompPoly.CPolynomial.NTTFast.powers_eq_ofFn, CompPoly.CPolynomial.NTTFast.scaleWith, CompPoly.CPolynomial.NTTFast.scaleWith_powers, CompPoly.CPolynomial.NTTFast.CosetPlan, CompPoly.CPolynomial.NTTFast.CosetPlan.ofPlan, CompPoly.CPolynomial.NTTFast.CosetPlan.WellFormed, CompPoly.CPolynomial.NTTFast.CosetPlan.ofPlan_wellFormed, CompPoly.CPolynomial.NTTFast.CosetPlan.forwardImpl, CompPoly.CPolynomial.NTTFast.CosetPlan.inverseImpl, CompPoly.CPolynomial.NTTFast.CosetPlan.forwardImpl_eq_bitRevPermute_evalOnCoset, CompPoly.CPolynomial.NTTFast.CosetPlan.inverseImpl_correct, CompPoly.CPolynomial.NTTFast.CosetPlan.interpolate, CompPoly.CPolynomial.NTTFast.CosetPlan.interpolate_eq_coset_interpolate, CompPoly.CPolynomial.NTTFast.CosetPlan.interpolate_eq_interpolate
statement: formalized
proof: formalized
---

# Planned Coset NTT

`CompPoly.Univariate.NTTFast.Coset`, in [CompPoly/Univariate/NTTFast/Coset.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean), by Derek Sorensen.

> The coset transforms of `NTT/Coset.lean` over a reusable `NTTFast.Plan`, with the shift
> powers `gⁱ` and `g⁻ⁱ` computed once per plan rather than once per coefficient. As with
> `Plan.forwardImpl`, the forward transform returns values in bit-reversed order and the
> inverse transform consumes them in that order.
>
> ## Main definitions
>
> * `NTTFast.powers g m`: the array `#[1, g, …, g^(m-1)]` by a running product.
> * `NTTFast.CosetPlan`: a plan together with a shift `g` and its cached powers.
> * `CosetPlan.forwardImpl`, `CosetPlan.inverseImpl`, `CosetPlan.interpolate`.
>
> ## Main results
>
> * `powers_eq_ofFn`: the running product computes the powers.
>
> …

`CompPoly.CPolynomial.NTTFast.powersAux` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L45))

> Tail-recursive running product appending `w, w·g, …, w·g^(k-1)` to `acc`.

```lean
def powersAux (g : R) : Nat → R → Array R → Array R
```

`CompPoly.CPolynomial.NTTFast.powers` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L50))

> The powers `#[1, g, …, g^(m-1)]`, by a running product.

```lean
def powers (g : R) (m : Nat) : Array R
```

`CompPoly.CPolynomial.NTTFast.powers_eq_ofFn` (theorem, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L62))

> The running product computes the powers of `g`.

```lean
theorem powers_eq_ofFn (g : R) (m : Nat) :
    powers g m = Array.ofFn (fun i : Fin m => g ^ (i : Nat))
```

`CompPoly.CPolynomial.NTTFast.scaleWith` (definition, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L68))

> Scale the first `m` coefficients by a cached power table.

```lean
def scaleWith (pows : Array R) (m : Nat) (a : Array R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTTFast.scaleWith_powers` (theorem, [line 72](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L72))

> Scaling with the cached powers of `g` is `NTT.Coset.scale g`.

```lean
theorem scaleWith_powers (g : R) (m : Nat) (a : Array R) :
    scaleWith (powers g m) m a = NTT.Coset.scale g m a
```

`CompPoly.CPolynomial.NTTFast.CosetPlan` (structure, [line 80](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L80))

> A reusable plan for transforms on the coset `g·⟨ω⟩` of the plan's domain.

```lean
structure CosetPlan (R : Type*) [Field R] where
  plan : Plan R
  shift : R
  shiftPowers : Array R
  shiftInvPowers : Array R
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.ofPlan` (definition, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L89))

> Build a coset plan from a domain plan and a shift `g`.

```lean
def ofPlan (P : Plan R) (g : R) : CosetPlan R
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.WellFormed` (definition, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L96))

> A coset plan is well formed when its domain plan is and its power tables are exact.

```lean
def WellFormed (C : CosetPlan R) : Prop
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.ofPlan_wellFormed` (theorem, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L100))

```lean
theorem ofPlan_wellFormed (P : Plan R) (hP : Plan.WellFormed P) (g : R) :
    WellFormed (ofPlan P g)
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.forwardImpl` (definition, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L105))

> Forward transform on the coset, returning values in bit-reversed order.

```lean
def forwardImpl (C : CosetPlan R) (p : CPolynomial.Raw R) : Array R
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.inverseImpl` (definition, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L109))

> Inverse transform on the coset, from values in bit-reversed order.

```lean
def inverseImpl (C : CosetPlan R) (v : Array R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.forwardImpl_eq_bitRevPermute_evalOnCoset` (theorem, [line 113](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L113))

> …

```lean
theorem forwardImpl_eq_bitRevPermute_evalOnCoset (C : CosetPlan R) (hC : WellFormed C)
    (p : CPolynomial.Raw R) (hdeg : p.toPoly.natDegree < C.plan.domain.n) :
    forwardImpl C p =
      NTT.Transform.bitRevPermute C.plan.domain
        (NTT.evalOnCoset C.plan.domain C.shift p)
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.inverseImpl_correct` (theorem, [line 127](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L127))

> …

```lean
theorem inverseImpl_correct (C : CosetPlan R) (hC : WellFormed C) (v : Array R) :
    inverseImpl C (NTT.Transform.bitRevPermute C.plan.domain v) =
      NTT.Coset.inverseImpl C.plan.domain C.shift v
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.interpolate` (definition, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L136))

> Interpolate natural-order values on the coset through the cached plan.

```lean
def interpolate [BEq R] [LawfulBEq R] (C : CosetPlan R) (values : Vector R C.plan.domain.n) :
    CPolynomial R
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.interpolate_eq_coset_interpolate` (theorem, [line 142](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L142))

> A well-formed coset plan interpolates as `NTT.Coset.interpolate`.

```lean
theorem interpolate_eq_coset_interpolate [BEq R] [LawfulBEq R] (C : CosetPlan R)
    (hC : WellFormed C) (values : Vector R C.plan.domain.n) :
    interpolate C values = NTT.Coset.interpolate C.plan.domain C.shift values
```

`CompPoly.CPolynomial.NTTFast.CosetPlan.interpolate_eq_interpolate` (theorem, [line 149](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean#L149))

> …

```lean
theorem interpolate_eq_interpolate [BEq R] [LawfulBEq R] (C : CosetPlan R)
    (hC : WellFormed C) (hg : C.shift ≠ 0) (values : Vector R C.plan.domain.n) :
    interpolate C values =
      CLagrange.interpolate Finset.univ
        (fun k : C.plan.domain.Idx => C.shift * C.plan.domain.node k) values.get
```

## Depends on

- [Coset NTT](../ntt/coset.md)
- [Basic NTTFast correctness facts](correctness/basic.md)

## Proof depends on

- [NTTFast and Evaluation](evaluation.md)

## Sources

- [CompPoly/Univariate/NTTFast/Coset.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Coset.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Coset.json)

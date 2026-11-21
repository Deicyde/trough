---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Plan.forwardImpl_correct, CompPoly.CPolynomial.NTTFast.Plan.forwardImpl_ofDomain_correct, CompPoly.CPolynomial.NTTFast.Plan.forwardPairImpl_eq_pair, CompPoly.CPolynomial.NTTFast.Plan.forwardPairImpl_correct, CompPoly.CPolynomial.NTTFast.Plan.normalize_eq_ntt_normalize, CompPoly.CPolynomial.NTTFast.Plan.inverseImpl_correct, CompPoly.CPolynomial.NTTFast.Plan.pointwiseMul_bitRevPermute_forwardSpec_eq, CompPoly.CPolynomial.NTTFast.Plan.Raw.fastMulImpl_correct, CompPoly.CPolynomial.NTTFast.Plan.Raw.fastMulImpl_trim_eq_mul, CompPoly.CPolynomial.NTTFast.Plan.fastMulImpl_correct, CompPoly.CPolynomial.NTTFast.Plan.fastMulImpl_eq_mul, CompPoly.CPolynomial.NTTFast.Raw.fastMulImpl_correct, CompPoly.CPolynomial.NTTFast.Raw.fastMulImpl_trim_eq_mul, CompPoly.CPolynomial.NTTFast.fastMulImpl_correct, CompPoly.CPolynomial.NTTFast.fastMulImpl_eq_mul, CompPoly.CPolynomial.NTTFast.safeFastMul_eq_mul, CompPoly.CPolynomial.NTTFast.withFallback_eq_mul
statement: formalized
proof: formalized
---

# NTTFast multiplication correctness

`CompPoly.Univariate.NTTFast.Correctness.Pipeline`, in [CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean), by Valerii Huhnin.

> Plan-level and one-shot correctness theorems for `NTTFast` multiplication.

`CompPoly.CPolynomial.NTTFast.Plan.forwardImpl_correct` (theorem, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L29))

> A well-formed plan's forward transform computes the bit-reversed forward NTT.

```lean
theorem forwardImpl_correct (P : Plan R) (hP : WellFormed P) (p : CPolynomial.Raw R) :
    forwardImpl P p =
      NTT.Transform.bitRevPermute P.domain (NTT.Forward.forwardSpec P.domain p)
```

`CompPoly.CPolynomial.NTTFast.Plan.forwardImpl_ofDomain_correct` (theorem, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L36))

> A plan built from a domain has a correct forward transform.

```lean
theorem forwardImpl_ofDomain_correct (D : NTT.Domain R) (p : CPolynomial.Raw R) :
    forwardImpl (ofDomain D) p =
      NTT.Transform.bitRevPermute D (NTT.Forward.forwardSpec D p)
```

`CompPoly.CPolynomial.NTTFast.Plan.forwardPairImpl_eq_pair` (theorem, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L42))

> The paired forward transform equals the pair of individual forward transforms.

```lean
theorem forwardPairImpl_eq_pair
    (P : Plan R) (hP : WellFormed P) (p q : CPolynomial.Raw R) :
    forwardPairImpl P p q = (forwardImpl P p, forwardImpl P q)
```

`CompPoly.CPolynomial.NTTFast.Plan.forwardPairImpl_correct` (theorem, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L50))

> The paired forward transform computes the two bit-reversed forward NTT outputs.

```lean
theorem forwardPairImpl_correct
    (P : Plan R) (hP : WellFormed P) (p q : CPolynomial.Raw R) :
    forwardPairImpl P p q =
      (NTT.Transform.bitRevPermute P.domain (NTT.Forward.forwardSpec P.domain p),
        NTT.Transform.bitRevPermute P.domain (NTT.Forward.forwardSpec P.domain q))
```

`CompPoly.CPolynomial.NTTFast.Plan.normalize_eq_ntt_normalize` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L59))

> Plan normalization agrees with `NTT.Inverse.normalize` for the same domain.

```lean
theorem normalize_eq_ntt_normalize (P : Plan R) (hP : WellFormed P) (a : Array R) :
    normalize P a = NTT.Inverse.normalize P.domain a
```

`CompPoly.CPolynomial.NTTFast.Plan.inverseImpl_correct` (theorem, [line 65](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L65))

> A well-formed plan's inverse transform computes the inverse NTT spec.

```lean
theorem inverseImpl_correct (P : Plan R) (hP : WellFormed P) (v : Array R) :
    inverseImpl P (NTT.Transform.bitRevPermute P.domain v) =
      NTT.Inverse.inverseSpec P.domain v
```

`CompPoly.CPolynomial.NTTFast.Plan.pointwiseMul_bitRevPermute_forwardSpec_eq` (theorem, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L84))

> Pointwise multiplication commutes with applying the bit-reversal permutation.

```lean
theorem pointwiseMul_bitRevPermute_forwardSpec_eq
    (D : NTT.Domain R) (p q : CPolynomial.Raw R) :
    NTT.FastMul.pointwiseMul D
        (NTT.Transform.bitRevPermute D (NTT.Forward.forwardSpec D p))
        (NTT.Transform.bitRevPermute D (NTT.Forward.forwardSpec D q)) =
      NTT.Transform.bitRevPermute D
        (NTT.FastMul.pointwiseMul D
          (NTT.Forward.forwardSpec D p) (NTT.Forward.forwardSpec D q))
```

`CompPoly.CPolynomial.NTTFast.Plan.Raw.fastMulImpl_correct` (theorem, [line 105](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L105))

> …

```lean
theorem fastMulImpl_correct [BEq R] [LawfulBEq R]
    (P : Plan R) (hP : WellFormed P) (p q : CPolynomial.Raw R) :
    fastMulImpl P p q = NTT.FastMul.Raw.fastMulSpec P.domain p q
```

`CompPoly.CPolynomial.NTTFast.Plan.Raw.fastMulImpl_trim_eq_mul` (theorem, [line 115](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L115))

> …

```lean
theorem fastMulImpl_trim_eq_mul [BEq R] [LawfulBEq R]
    (P : Plan R) (hP : WellFormed P) (p q : CPolynomial.Raw R)
    (hfit : NTT.Domain.fits P.domain p q) :
    (fastMulImpl P p q).trim = p * q
```

`CompPoly.CPolynomial.NTTFast.Plan.fastMulImpl_correct` (theorem, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L125))

> …

```lean
theorem fastMulImpl_correct [BEq R] [LawfulBEq R]
    (P : Plan R) (hP : WellFormed P) (p q : CPolynomial R) :
    fastMulImpl P p q = NTT.FastMul.fastMulSpec P.domain p q
```

`CompPoly.CPolynomial.NTTFast.Plan.fastMulImpl_eq_mul` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L132))

> …

```lean
theorem fastMulImpl_eq_mul [BEq R] [LawfulBEq R]
    (P : Plan R) (hP : WellFormed P) (p q : CPolynomial R)
    (hfit : NTT.Domain.fits P.domain p.val q.val) :
    fastMulImpl P p q = p * q
```

`CompPoly.CPolynomial.NTTFast.Raw.fastMulImpl_correct` (theorem, [line 144](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L144))

> The one-shot raw multiplication implementation computes the raw NTT multiplication spec.

```lean
theorem fastMulImpl_correct [BEq R] [LawfulBEq R]
    (D : NTT.Domain R) (p q : CPolynomial.Raw R) :
    fastMulImpl D p q = NTT.FastMul.Raw.fastMulSpec D p q
```

`CompPoly.CPolynomial.NTTFast.Raw.fastMulImpl_trim_eq_mul` (theorem, [line 151](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L151))

> The one-shot raw multiplication implementation trims to ordinary multiplication.

```lean
theorem fastMulImpl_trim_eq_mul [BEq R] [LawfulBEq R]
    (D : NTT.Domain R) (p q : CPolynomial.Raw R)
    (hfit : NTT.Domain.fits D p q) :
    (fastMulImpl D p q).trim = p * q
```

`CompPoly.CPolynomial.NTTFast.fastMulImpl_correct` (theorem, [line 161](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L161))

> The one-shot multiplication implementation computes the NTT multiplication spec.

```lean
theorem fastMulImpl_correct [BEq R] [LawfulBEq R]
    (D : NTT.Domain R) (p q : CPolynomial R) :
    fastMulImpl D p q = NTT.FastMul.fastMulSpec D p q
```

`CompPoly.CPolynomial.NTTFast.fastMulImpl_eq_mul` (theorem, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L168))

> The one-shot multiplication implementation agrees with ordinary multiplication.

```lean
theorem fastMulImpl_eq_mul [BEq R] [LawfulBEq R]
    (D : NTT.Domain R) (p q : CPolynomial R)
    (hfit : NTT.Domain.fits D p.val q.val) :
    fastMulImpl D p q = p * q
```

`CompPoly.CPolynomial.NTTFast.safeFastMul_eq_mul` (theorem, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L176))

> The safe one-shot wrapper agrees with ordinary multiplication.

```lean
theorem safeFastMul_eq_mul [BEq R] [LawfulBEq R]
    (D : NTT.Domain R) (p q : CPolynomial R)
    (hfit : NTT.Domain.fits D p.val q.val) :
    safeFastMul D p q hfit = p * q
```

`CompPoly.CPolynomial.NTTFast.withFallback_eq_mul` (theorem, [line 183](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean#L183))

> `withFallback` agrees with canonical polynomial multiplication.

```lean
theorem withFallback_eq_mul [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen))
    (p q : CPolynomial R) :
    withFallback bestDomainForLength? p q = p * q
```

## Depends on

- [Basic NTTFast correctness facts](basic.md)
- [Fast multiplication via NTT](../fastmul.md)

## Proof depends on

- [Paired forward NTTFast correctness](pair.md)
- [Radix-4 DIF NTTFast correctness](radix4dif.md)
- [Radix-4 DIT NTTFast correctness](radix4dit.md)

## Sources

- [CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Pipeline.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Correctness.Pipeline.json)

---
catalog: module
lean: CompPoly.CPolynomial.Raw.MulContext, CompPoly.CPolynomial.Raw.ModContext, CompPoly.CPolynomial.Raw.MulContext.naive, CompPoly.CPolynomial.Raw.MulContext.ntt, CompPoly.CPolynomial.Raw.MulContext.nttFast, CompPoly.CPolynomial.Raw.ModContext.naive, CompPoly.CPolynomial.Raw.ModContext.remainderOnly, CompPoly.CPolynomial.Raw.ModContext.reversal, CompPoly.CPolynomial.Raw.ModContext.reversalNtt, CompPoly.CPolynomial.Raw.ModContext.reversalNttFast
statement: formalized
proof: formalized
---

# Raw Univariate Algorithm Contexts

`CompPoly.Univariate.Raw.Context`, in [CompPoly/Univariate/Raw/Context.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean), by Valerii Huhnin.

> Array-level execution dictionaries for reusable raw univariate polynomial
> kernels.

`CompPoly.CPolynomial.Raw.MulContext` (structure, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L33))

> Internal raw multiplication backend for array-level polynomial kernels.

```lean
structure MulContext (R : Type*) [Semiring R] [BEq R] [LawfulBEq R] where
  /-- Multiply two raw polynomials, returning the trimmed raw product. -/
  mul : CPolynomial.Raw R → CPolynomial.Raw R → CPolynomial.Raw R
  /-- The backend agrees with raw polynomial multiplication. -/
  mul_eq_mul : ∀ p q, mul p q = p * q
```

`CompPoly.CPolynomial.Raw.ModContext` (structure, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L40))

> Internal raw monic-remainder backend for array-level polynomial kernels.

```lean
structure ModContext (R : Type*) [Field R] [BEq R] [LawfulBEq R] where
  /-- Reduce the first raw polynomial modulo the second raw monic divisor. -/
  modByMonic : CPolynomial.Raw R → CPolynomial.Raw R → CPolynomial.Raw R
  /-- The backend agrees with raw monic remainders for canonical raw inputs. -/
  modByMonic_eq_modByMonic :
    ∀ p q, p.trim = p → q.trim = q → modByMonic p q = CPolynomial.Raw.modByMonic p q
```

`CompPoly.CPolynomial.Raw.MulContext.naive` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L50))

> The default raw multiplication context, backed by raw polynomial multiplication.

```lean
def naive [Semiring R] [BEq R] [LawfulBEq R] : MulContext R
```

`CompPoly.CPolynomial.Raw.MulContext.ntt` (definition, [line 55](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L55))

> NTT-backed raw multiplication context with raw multiplication for unsupported lengths.

```lean
def ntt [Field R] [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen)) :
    MulContext R
```

`CompPoly.CPolynomial.Raw.MulContext.nttFast` (definition, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L75))

> NTTFast-backed raw multiplication context with raw multiplication for unsupported lengths.

```lean
def nttFast [Field R] [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen)) :
    MulContext R
```

`CompPoly.CPolynomial.Raw.ModContext.naive` (definition, [line 99](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L99))

> The default raw monic-remainder context, backed by raw `modByMonic`.

```lean
def naive [Field R] [BEq R] [LawfulBEq R] : ModContext R
```

`CompPoly.CPolynomial.Raw.ModContext.remainderOnly` (definition, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L104))

> Raw remainder-only monic-remainder context.

```lean
def remainderOnly [Field R] [BEq R] [LawfulBEq R] : ModContext R
```

`CompPoly.CPolynomial.Raw.ModContext.reversal` (definition, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L109))

> Raw reversal-based monic-remainder context parameterized by low-product multiplication.

```lean
def reversal [Field R] [BEq R] [LawfulBEq R]
    (M : Raw.MulLowContext R) : ModContext R
```

`CompPoly.CPolynomial.Raw.ModContext.reversalNtt` (definition, [line 121](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L121))

> Raw monic remainders by reversal, using an NTT low-product backend.

```lean
def reversalNtt [Field R] [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen)) :
    ModContext R
```

`CompPoly.CPolynomial.Raw.ModContext.reversalNttFast` (definition, [line 128](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean#L128))

> Raw monic remainders by reversal, using an NTTFast low-product backend.

```lean
def reversalNttFast [Field R] [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen)) :
    ModContext R
```

## Depends on

- [Low Product via NTT](../ntt/fastmullow.md)
- [Low Product via NTTFast](../nttfast/fastmullow.md)

## Proof depends on

- [Univariate Division Correctness](../divisioncorrectness.md)

## Sources

- [CompPoly/Univariate/Raw/Context.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Raw/Context.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Raw.Context.json)

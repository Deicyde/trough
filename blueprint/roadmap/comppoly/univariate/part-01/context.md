---
catalog: module
lean: CompPoly.CPolynomial.MulContext, CompPoly.CPolynomial.ModContext, CompPoly.CPolynomial.MulContext.naive, CompPoly.CPolynomial.MulContext.ntt, CompPoly.CPolynomial.MulContext.nttFast, CompPoly.CPolynomial.ModContext.naive, CompPoly.CPolynomial.ModContext.remainderOnly, CompPoly.CPolynomial.ModContext.reversal, CompPoly.CPolynomial.ModContext.reversalNtt, CompPoly.CPolynomial.ModContext.reversalNttFast
statement: formalized
proof: formalized
---

# Univariate Algorithm Contexts

`CompPoly.Univariate.Context`, in [CompPoly/Univariate/Context.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean), by Valerii Huhnin.

> Algorithm dictionaries for reusable univariate polynomial operations, including
> canonical, NTT, and NTTFast-backed implementations.

`CompPoly.CPolynomial.MulContext` (structure, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L30))

> Explicit multiplication backend for univariate polynomial algorithms.

```lean
structure MulContext (R : Type*) [Semiring R] [BEq R] [LawfulBEq R] where
  /-- Multiply two canonical polynomials. -/
  mul : CPolynomial R → CPolynomial R → CPolynomial R
  /-- The backend agrees with canonical polynomial multiplication. -/
  mul_eq_mul : ∀ p q, mul p q = p * q
```

`CompPoly.CPolynomial.ModContext` (structure, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L37))

> Explicit remainder backend for algorithms that only need reduction modulo monic divisors.

```lean
structure ModContext (R : Type*) [Field R] [BEq R] [LawfulBEq R] where
  /-- Reduce the first polynomial modulo the second, assuming the divisor is monic. -/
  modByMonic : CPolynomial R → CPolynomial R → CPolynomial R
  /-- The backend agrees with the canonical monic-remainder operation. -/
  modByMonic_eq_modByMonic : ∀ p q, modByMonic p q = CPolynomial.modByMonic p q
```

`CompPoly.CPolynomial.MulContext.naive` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L46))

> The default multiplication context, backed by canonical `CPolynomial` multiplication.

```lean
def naive [Semiring R] [BEq R] [LawfulBEq R] : MulContext R
```

`CompPoly.CPolynomial.MulContext.ntt` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L56))

> NTT-backed multiplication context with canonical multiplication for unsupported lengths.
>
> The context asks the selector for a domain that fits the current operands. If no
> supported domain is available, it uses ordinary `CPolynomial` multiplication.

```lean
def ntt [Field R] [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen)) :
    MulContext R
```

`CompPoly.CPolynomial.MulContext.nttFast` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L69))

> NTTFast-backed multiplication context with canonical multiplication for unsupported lengths.
>
> The context asks the selector for a domain that fits the current operands. If no
> supported domain is available, it uses ordinary `CPolynomial` multiplication.

```lean
def nttFast [Field R] [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen)) :
    MulContext R
```

`CompPoly.CPolynomial.ModContext.naive` (definition, [line 81](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L81))

> The default monic-remainder context, backed by `CPolynomial.modByMonic`.

```lean
def naive [Field R] [BEq R] [LawfulBEq R] : ModContext R
```

`CompPoly.CPolynomial.ModContext.remainderOnly` (definition, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L86))

> A remainder-only backend for monic remainders.

```lean
def remainderOnly [Field R] [BEq R] [LawfulBEq R] : ModContext R
```

`CompPoly.CPolynomial.ModContext.reversal` (definition, [line 91](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L91))

> A reversal-based monic-remainder backend parameterized by low-product multiplication.

```lean
def reversal [Field R] [BEq R] [LawfulBEq R]
    (M : Raw.MulLowContext R) : ModContext R
```

`CompPoly.CPolynomial.ModContext.reversalNtt` (definition, [line 97](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L97))

> Monic remainders by reversal, using an NTT low-product backend.

```lean
def reversalNtt [Field R] [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen)) :
    ModContext R
```

`CompPoly.CPolynomial.ModContext.reversalNttFast` (definition, [line 104](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean#L104))

> Monic remainders by reversal, using an NTTFast low-product backend.

```lean
def reversalNttFast [Field R] [BEq R] [LawfulBEq R]
    (bestDomainForLength? : (requiredLen : Nat) →
      Option (NTT.FittingDomain R requiredLen)) :
    ModContext R
```

## Depends on

- [Univariate Division Correctness](divisioncorrectness.md)
- [Low Product via NTT](ntt/fastmullow.md)
- [NTTFast multiplication correctness](nttfast/correctness/pipeline.md)
- [Low Product via NTTFast](nttfast/fastmullow.md)

## Sources

- [CompPoly/Univariate/Context.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Context.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.Context.json)

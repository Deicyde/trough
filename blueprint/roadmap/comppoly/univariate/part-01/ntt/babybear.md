---
catalog: module
lean: CompPoly.CPolynomial.NTT.BabyBear.bitsOfLogN, CompPoly.CPolynomial.NTT.BabyBear.domainOfLogN, CompPoly.CPolynomial.NTT.BabyBear.bestDomainForLength?, CompPoly.CPolynomial.NTT.BabyBear.fastDomainOfLogN, CompPoly.CPolynomial.NTT.BabyBear.fastBestDomainForLength?
statement: formalized
proof: formalized
---

# BabyBear NTT Domains

`CompPoly.Univariate.NTT.BabyBear`, in [CompPoly/Univariate/NTT/BabyBear.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/BabyBear.lean), by Valerii Huhnin.

> Concrete radix-2 NTT domains over the BabyBear field.

`CompPoly.CPolynomial.NTT.BabyBear.bitsOfLogN` (definition, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/BabyBear.lean#L25))

> Build a finite index into the BabyBear two-adic generator table.

```lean
def bitsOfLogN (logN : Nat) (hlogN : logN ≤ BabyBear.twoAdicity) :
    Fin (BabyBear.twoAdicity + 1)
```

`CompPoly.CPolynomial.NTT.BabyBear.domainOfLogN` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/BabyBear.lean#L30))

> BabyBear radix-2 NTT domain for a supported two-adic size.

```lean
def domainOfLogN (logN : Nat) (hlogN : logN ≤ BabyBear.twoAdicity) :
    Domain BabyBear.Field
```

`CompPoly.CPolynomial.NTT.BabyBear.bestDomainForLength?` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/BabyBear.lean#L39))

> BabyBear NTT domain lookup for dynamic multiplication contexts.

```lean
def bestDomainForLength? (requiredLen : Nat) :
    Option (FittingDomain BabyBear.Field requiredLen)
```

`CompPoly.CPolynomial.NTT.BabyBear.fastDomainOfLogN` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/BabyBear.lean#L45))

> Fast BabyBear radix-2 NTT domain for a supported two-adic size.

```lean
def fastDomainOfLogN (logN : Nat) (hlogN : logN ≤ BabyBear.twoAdicity) :
    Domain BabyBear.Fast.Field
```

`CompPoly.CPolynomial.NTT.BabyBear.fastBestDomainForLength?` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/BabyBear.lean#L56))

> Fast BabyBear NTT domain lookup for dynamic multiplication contexts.

```lean
def fastBestDomainForLength? (requiredLen : Nat) :
    Option (FittingDomain BabyBear.Fast.Field requiredLen)
```

## Depends on

- [Fast BabyBear Field](../../../fields/babybear/fast.md)
- [NTT Domain](domain.md)

## Sources

- [CompPoly/Univariate/NTT/BabyBear.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/BabyBear.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.BabyBear.json)

---
catalog: module
lean: CompPoly.CPolynomial.NTT.KoalaBear.bitsOfLogN, CompPoly.CPolynomial.NTT.KoalaBear.domainOfLogN, CompPoly.CPolynomial.NTT.KoalaBear.bestDomainForLength?, CompPoly.CPolynomial.NTT.KoalaBear.fastDomainOfLogN, CompPoly.CPolynomial.NTT.KoalaBear.fastBestDomainForLength?
statement: formalized
proof: formalized
---

# KoalaBear NTT Domains

`CompPoly.Univariate.NTT.KoalaBear`, in [CompPoly/Univariate/NTT/KoalaBear.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/KoalaBear.lean), by Valerii Huhnin.

> Concrete radix-2 NTT domains over the KoalaBear field.

`CompPoly.CPolynomial.NTT.KoalaBear.bitsOfLogN` (definition, [line 25](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/KoalaBear.lean#L25))

> Build a finite index into the KoalaBear two-adic generator table.

```lean
def bitsOfLogN (logN : Nat) (hlogN : logN ≤ KoalaBear.twoAdicity) :
    Fin (KoalaBear.twoAdicity + 1)
```

`CompPoly.CPolynomial.NTT.KoalaBear.domainOfLogN` (definition, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/KoalaBear.lean#L30))

> KoalaBear radix-2 NTT domain for a supported two-adic size.

```lean
def domainOfLogN (logN : Nat) (hlogN : logN ≤ KoalaBear.twoAdicity) :
    Domain KoalaBear.Field
```

`CompPoly.CPolynomial.NTT.KoalaBear.bestDomainForLength?` (definition, [line 39](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/KoalaBear.lean#L39))

> KoalaBear NTT domain lookup for dynamic multiplication contexts.

```lean
def bestDomainForLength? (requiredLen : Nat) :
    Option (FittingDomain KoalaBear.Field requiredLen)
```

`CompPoly.CPolynomial.NTT.KoalaBear.fastDomainOfLogN` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/KoalaBear.lean#L45))

> Fast KoalaBear radix-2 NTT domain for a supported two-adic size.

```lean
def fastDomainOfLogN (logN : Nat) (hlogN : logN ≤ KoalaBear.twoAdicity) :
    Domain KoalaBear.Fast.Field
```

`CompPoly.CPolynomial.NTT.KoalaBear.fastBestDomainForLength?` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/KoalaBear.lean#L56))

> Fast KoalaBear NTT domain lookup for dynamic multiplication contexts.

```lean
def fastBestDomainForLength? (requiredLen : Nat) :
    Option (FittingDomain KoalaBear.Fast.Field requiredLen)
```

## Depends on

- [Fast KoalaBear Field](../../../fields/koalabear/fast.md)
- [NTT Domain](domain.md)

## Sources

- [CompPoly/Univariate/NTT/KoalaBear.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/KoalaBear.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.KoalaBear.json)

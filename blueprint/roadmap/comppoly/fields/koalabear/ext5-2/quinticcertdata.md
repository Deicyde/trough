---
catalog: module
lean: KoalaBear.QuinticCert.traceSteps, KoalaBear.QuinticCert.frobSteps, KoalaBear.QuinticCert.rp, KoalaBear.QuinticCert.w, KoalaBear.QuinticCert.u, KoalaBear.QuinticCert.v
statement: formalized
proof: formalized
---

# Rabin certificate data for `p = 2130706433` (QuinticCertData)

`CompPoly.Fields.KoalaBear.Ext5.QuinticCertData`, in [CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean), by Derek Sorensen.

> The modulus `f` has little-endian coefficients `[2130706432, 0, 1, 0, 0, 1]`.
>
> GENERATED. Do not edit by hand; regenerate with:
>
> ```sh
> uv run --no-project --python 3.12 python scripts/gen_rabin_certificate.py --p 2130706433 \
>   --f='-1,0,1,0,0,1' \
>   --lean <this file> --namespace KoalaBear.QuinticCert \
>   --authors 'Derek Sorensen'
> ```
>
> These lists are untrusted data. Consumers validate them with kernel-checked
> `CompPoly.RabinCert.runChain` equations and certificate-soundness theorems for
> their specified polynomial. Defining the lists alone establishes no such theorem.

`KoalaBear.QuinticCert.traceSteps` (definition, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean#L36))

> Square-and-multiply chain for `X^(p^5) mod f` (211 steps).

```lean
def traceSteps : List Step
```

`KoalaBear.QuinticCert.frobSteps` (definition, [line 374](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean#L374))

> Square-and-multiply chain for `X^p mod f` (37 steps).

```lean
def frobSteps : List Step
```

`KoalaBear.QuinticCert.rp` (definition, [line 439](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean#L439))

> The residue `X^p mod f`.

```lean
def rp : List ℕ
```

`KoalaBear.QuinticCert.w` (definition, [line 442](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean#L442))

> `w = (X^p mod f) - X`, the reduced form of `X^p - X`.

```lean
def w : List ℕ
```

`KoalaBear.QuinticCert.u` (definition, [line 445](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean#L445))

> Bézout coefficient: `u·f + v·w = 1`.

```lean
def u : List ℕ
```

`KoalaBear.QuinticCert.v` (definition, [line 448](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean#L448))

> Bézout coefficient: `u·f + v·w = 1`.

```lean
def v : List ℕ
```

## Depends on

- [Kernel-checkable Rabin irreducibility certificates over prime fields](../../../data/polynomial/rabincertificate.md)

## Sources

- [CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext5/QuinticCertData.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.KoalaBear.Ext5.QuinticCertData.json)

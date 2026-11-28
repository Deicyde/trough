---
catalog: module
lean: KoalaBear.SexticCert.traceSteps, KoalaBear.SexticCert.cop3Steps, KoalaBear.SexticCert.cop3Rp, KoalaBear.SexticCert.cop3W, KoalaBear.SexticCert.cop3U, KoalaBear.SexticCert.cop3V, KoalaBear.SexticCert.cop2Steps, KoalaBear.SexticCert.cop2Rp, KoalaBear.SexticCert.cop2W, KoalaBear.SexticCert.cop2U, KoalaBear.SexticCert.cop2V
statement: formalized
proof: formalized
---

# Rabin certificate data for `p = 2130706433` (SexticCertData)

`CompPoly.Fields.KoalaBear.Ext6.SexticCertData`, in [CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean), by Derek Sorensen.

> The modulus `f` has little-endian coefficients `[1, 0, 0, 1, 0, 0, 1]`.
>
> `d = 6` is composite, so Rabin's coprimality condition needs one certificate per
> prime factor of `d` (2, 3), at exponents p^3, p^2 respectively. Checking only the
> linear-factor case would admit a product of equal-degree factors.
>
> GENERATED. Do not edit by hand; regenerate with:
>
> ```sh
> uv run --no-project --python 3.12 python scripts/gen_rabin_certificate.py --p 2130706433 \
>   --f='1,0,0,1,0,0,1' \
>   --lean <this file> --namespace KoalaBear.SexticCert \
>   --authors 'Derek Sorensen'
> ```
>
> These lists are untrusted data. Consumers validate them with kernel-checked
> `CompPoly.RabinCert.runChain` equations and certificate-soundness theorems for
> their specified polynomial. Defining the lists alone establishes no such theorem.

`KoalaBear.SexticCert.traceSteps` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L40))

> Square-and-multiply chain for `X^(p^6) mod f` (258 steps).

```lean
def traceSteps : List Step
```

> ### Coprimality with `X^(p^3) - X`, for the prime factor `2` of `d = 6`.

`KoalaBear.SexticCert.cop3Steps` (definition, [line 303](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L303))

> Square-and-multiply chain for `X^(p^3) mod f` (121 steps).

```lean
def cop3Steps : List Step
```

`KoalaBear.SexticCert.cop3Rp` (definition, [line 427](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L427))

> The residue `X^(p^3) mod f`.

```lean
def cop3Rp : List ℕ
```

`KoalaBear.SexticCert.cop3W` (definition, [line 430](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L430))

> `cop3W = (X^(p^3) mod f) - X`, the reduced form of `X^(p^3) - X`.

```lean
def cop3W : List ℕ
```

`KoalaBear.SexticCert.cop3U` (definition, [line 433](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L433))

> Bézout coefficient: `cop3U·f + cop3V·cop3W = 1`.

```lean
def cop3U : List ℕ
```

`KoalaBear.SexticCert.cop3V` (definition, [line 436](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L436))

> Bézout coefficient: `cop3U·f + cop3V·cop3W = 1`.

```lean
def cop3V : List ℕ
```

> ### Coprimality with `X^(p^2) - X`, for the prime factor `3` of `d = 6`.

`KoalaBear.SexticCert.cop2Steps` (definition, [line 441](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L441))

> Square-and-multiply chain for `X^(p^2) mod f` (75 steps).

```lean
def cop2Steps : List Step
```

`KoalaBear.SexticCert.cop2Rp` (definition, [line 519](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L519))

> The residue `X^(p^2) mod f`.

```lean
def cop2Rp : List ℕ
```

`KoalaBear.SexticCert.cop2W` (definition, [line 522](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L522))

> `cop2W = (X^(p^2) mod f) - X`, the reduced form of `X^(p^2) - X`.

```lean
def cop2W : List ℕ
```

`KoalaBear.SexticCert.cop2U` (definition, [line 525](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L525))

> Bézout coefficient: `cop2U·f + cop2V·cop2W = 1`.

```lean
def cop2U : List ℕ
```

`KoalaBear.SexticCert.cop2V` (definition, [line 528](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean#L528))

> Bézout coefficient: `cop2U·f + cop2V·cop2W = 1`.

```lean
def cop2V : List ℕ
```

## Depends on

- [Kernel-checkable Rabin irreducibility certificates over prime fields](../../../data/polynomial/rabincertificate.md)

## Sources

- [CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Fields/KoalaBear/Ext6/SexticCertData.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Fields.KoalaBear.Ext6.SexticCertData.json)

---
declaration: definition
origin: cited
lean: Exchangeability.DeFinetti.ViaKoopman.blockAvg
statement: formalized
---

# Block average

The *block average* $A_{m,n,k}(f)(\omega) = \frac{1}{n} \sum_{j=0}^{n-1} f(\omega_{k \cdot n + j})$ averages $f$ over the $k$-th block of size $n$ (indices $[kn, kn+n)$). For $n = 0$, the block average is defined as $0$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Exchangeability.DeFinetti.ViaKoopman.blockAvg`](https://cameronfreer.github.io/exchangeability/docs/find/#doc/Exchangeability.DeFinetti.ViaKoopman.blockAvg).

## Sources

- [Exchangeability and de Finetti blueprint: content.tex, line 433](https://github.com/cameronfreer/exchangeability/blob/e0532e59ceff23edab44dda9ab0655debbc9cc22/blueprint/src/content.tex#L433)

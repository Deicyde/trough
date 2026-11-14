---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Simul.padM, MIPRE.LIDT.Simul.le_padM, MIPRE.LIDT.Simul.padM_le, MIPRE.LIDT.Simul.padM_le_mul, MIPRE.LIDT.Simul.padM_dvd, MIPRE.LIDT.Simul.simA, MIPRE.LIDT.Simul.deltaSim, MIPRE.LIDT.Simul.forty_le_simA, MIPRE.LIDT.Simul.clA_add_one_le_simA, MIPRE.LIDT.Simul.rpow_le_rpow_simA, MIPRE.LIDT.Simul.deltaCL_padded_le, MIPRE.LIDT.Simul.one_le_deltaSim, MIPRE.LIDT.Simul.constPM, MIPRE.LIDT.Simul.inconsistency_le_one
statement: formalized
proof: formalized
---

# Absorbing the simultaneous reduction's error

Let $q=2^k$, $m,d,r\geq1$ and let $M$ be the least power of two at least $m+r$. If $m+r\leq q$ then $M\mid q$ and $M\leq2(m+r)\leq4mr$, and with $K=M-m$ the losses of Lemma [Several codewords: the simultaneity reduction](lem-lidt-ldc.md), $\delta_{\mathrm{CL}}(9(K+1)\varepsilon,q,M,d,1)+Md/q$, are bounded by

$$
\delta_{\mathrm{sim}}(\varepsilon,q,m,d,r)=a(dmr)^a(\varepsilon^b+q^{-b}+2^{-bmd}),
$$

with $b$ the exponent of Theorem [Quantum soundness of the seeded CL test, one codeword](thm-lidt-cl-soundness-one.md) and $a=40a_1 4^{a_1}$, $a_1$ its constant. If $m+r>q$ then $\delta_{\mathrm{sim}}\geq1$, and arbitrary complete projective measurements do. This separates the trivial regime from the padding argument that requires $M\mid q$.

## Depends on

- [Extracting exactly linear combined codewords](lem-lidt-ldc-extraction.md)
- [The parameter choice](lem-lidt-cl-adapter-params.md)

## Proof

Use $M\leq4mr$ for the polynomial factor and the extraction term, $x^b\leq x$ for $x\geq1$ for the failure blow-up $9(K+1)\leq9M$, $q^{-1}\leq q^{-b}$, and $M\geq m$ in the exponential term. When $m+r>q$, $q<2dmr$ gives $q^{-b}\geq(2dmr)^{-1}$.

## Lean

Formalized as [`MIPRE.LIDT.Simul.padM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.padM), [`MIPRE.LIDT.Simul.le_padM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.le_padM), [`MIPRE.LIDT.Simul.padM_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.padM_le), [`MIPRE.LIDT.Simul.padM_le_mul`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.padM_le_mul), [`MIPRE.LIDT.Simul.padM_dvd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.padM_dvd), [`MIPRE.LIDT.Simul.simA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.simA), [`MIPRE.LIDT.Simul.deltaSim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.deltaSim), [`MIPRE.LIDT.Simul.forty_le_simA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.forty_le_simA), [`MIPRE.LIDT.Simul.clA_add_one_le_simA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.clA_add_one_le_simA), [`MIPRE.LIDT.Simul.rpow_le_rpow_simA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.rpow_le_rpow_simA), [`MIPRE.LIDT.Simul.deltaCL_padded_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.deltaCL_padded_le), [`MIPRE.LIDT.Simul.one_le_deltaSim`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.one_le_deltaSim), [`MIPRE.LIDT.Simul.constPM`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.constPM), [`MIPRE.LIDT.Simul.inconsistency_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.inconsistency_le_one).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 1399](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L1399)

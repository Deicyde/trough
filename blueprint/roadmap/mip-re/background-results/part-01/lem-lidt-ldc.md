---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Simul.clSoundness_padded
statement: formalized
proof: formalized
---

# Several codewords: the simultaneity reduction

For admissible $q$, $m,d,r\geq1$, $m\mid q$, and $r=\mathrm{ldc}$, the single-codeword seeded CL contract implies the simultaneous contract of Theorem [Quantum soundness of the seeded CL test](thm-lidt-cl-soundness.md), including a projective measurement of complete $r$-tuples on each player's original space and full-tuple consistency. The chosen input contract is the proved Theorem [Quantum soundness of the seeded CL test, one codeword](thm-lidt-cl-soundness-one.md). This extension is needed at $(q,m',d,m'+6)$ in answer reduction; QLD uses only $(q,4m,d,1)$. The separate tensor-code route is alternative provenance.

In Lean the reduction is stated at any padding $K$ with $r\leq K$, $K\geq1$ and $(K+m)\mid q$: the three conclusions hold with errors $\delta_{\mathrm{CL}}(9(K+1)\varepsilon,q,K+m,d,1)+(K+m)d/q$ for the two point conclusions and $\delta_{\mathrm{CL}}(9(K+1)\varepsilon,q,K+m,d,1)$ for the full-tuple one.

## Depends on

- [The padded multi-codeword game adapter](lem-lidt-ldc-adapter.md)
- [Extracting exactly linear combined codewords](lem-lidt-ldc-extraction.md)
- [Quantum soundness of the seeded CL test, one codeword](thm-lidt-cl-soundness-one.md)

## Proof

Lemma [The padded multi-codeword game adapter](lem-lidt-ldc-adapter.md) gives, on the same state and spaces, a strategy at $(q,K+m,d,1)$ of failure at most $9(K+1)\varepsilon$ whose point measurements are the combined ones. Theorem [Quantum soundness of the seeded CL test, one codeword](thm-lidt-cl-soundness-one.md) gives $R^\textsc{A}$, $R^\textsc{B}$ satisfying the three single-codeword conclusions against them with error $\delta_{\mathrm{CL}}(9(K+1)\varepsilon,q,K+m,d,1)$, and Lemma [Extracting exactly linear combined codewords](lem-lidt-ldc-extraction.md) turns those into $G^\textsc{A}$, $G^\textsc{B}$.

## Lean

Formalized as [`MIPRE.LIDT.Simul.clSoundness_padded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.clSoundness_padded).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 1219](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L1219)

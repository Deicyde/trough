---
declaration: theorem
origin: cited
lean: MIPRE.LIDT.Simul.clSoundness
statement: formalized
proof: formalized
---

# Quantum soundness of the seeded CL test

There are universal constants $a\geq 1$ and $0\lt b<1$ such that every projective strategy passing the seeded CL test with probability at least $1-\varepsilon$, for $\varepsilon>0$, admits projective measurements $G^\textsc{A},G^\textsc{B}$ on the respective players' spaces with outcomes tuples $(g_1,\ldots,g_{\mathrm{ldc}})$ of polynomials of individual degree at most $d$. Their evaluations are consistent with the other player's point measurement on average over uniform $u\in\mathbb{F}_q^m$, and the two full tuple measurements are consistent with each other, all with error at most

$$
\delta_{\mathrm{CL}}(\varepsilon,q,m,d,\mathrm{ldc})
= a(dm\,\mathrm{ldc})^a\bigl(\varepsilon^b+q^{-b}+2^{-bmd}\bigr).
$$

The full tuple consistency has no question average. The Lean statement takes $q=2^k$, $m\mid q$ and $m,d,\mathrm{ldc}\geq1$; $b$ is the exponent of Theorem [Quantum soundness of the seeded CL test, one codeword](thm-lidt-cl-soundness-one.md) and $a$ is the constant of Lemma [Absorbing the simultaneous reduction's error](lem-lidt-ldc-error.md). The tensor-code intermediates below remain separate targets.

## Depends on

- [Seeded CL low individual degree test](def-lidt-cl.md)
- [Several codewords: the simultaneity reduction](lem-lidt-ldc.md)
- [Inconsistency](../../foundations/part-02/def-inconsistency.md)

## Proof depends on

- [Absorbing the simultaneous reduction's error](lem-lidt-ldc-error.md)

## Proof

If $m+\mathrm{ldc}\leq q$, Lemma [Several codewords: the simultaneity reduction](lem-lidt-ldc.md) at the padding of Lemma [Absorbing the simultaneous reduction's error](lem-lidt-ldc-error.md), whose error that lemma absorbs. Otherwise the error bound is at least one, and any complete projective measurements satisfy the three conclusions.

## Lean

Formalized as [`MIPRE.LIDT.Simul.clSoundness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Simul.clSoundness).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 742](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L742)

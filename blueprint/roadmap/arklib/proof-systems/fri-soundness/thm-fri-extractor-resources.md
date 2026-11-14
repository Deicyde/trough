---
declaration: theorem
origin: cited
lean: Fri.Spec.Extractor.profile_extractProgram_word_le, Fri.Spec.Extractor.profile_extractProgram_apply_le, Fri.Spec.Extractor.profile_extractProgram_inv_le, Fri.Spec.Extractor.profile_extractProgram_domainRead_le, Fri.Spec.Extractor.profile_extractProgram_challengeRead_le, Fri.Spec.Extractor.profile_extractProgram_finalPolynomialRead, Fri.Spec.Extractor.profile_extractProgram_add_sub_le, Fri.Spec.Extractor.profile_extractProgram_mul_le, Fri.Spec.Extractor.profile_extractProgram_eq_le
statement: formalized
proof: formalized
---

# fri-extractor-resources

Put $I(m)=100(m+1)^3$, $E(m)=(m+1)^2$, and

$$
G=2(n+2)+\sum_i(4b_i+8)(n+1),\qquad
J=1+\sum_i(n-s_i).
$$

For every retained history with $\sum_i s_i\leq n$, including rejected histories, the measured extractor performs at most

$$
N\left(\sum_i b_i+k\right)+M
\quad\text{word reads},\qquad
1+N\sum_i b_i(b_i-1)+M(M-1)
\quad\text{inversions}.
$$

It performs at most two original-domain reads, at most $k+1$ folding-challenge reads, and exactly one final-polynomial retrieval. Each of the combined addition/subtraction count, the multiplication count, and the field-equality count is bounded by

$$
B=N\left[G+\sum_i\bigl(I(b_i)+E(b_i)+1\bigr)+E(d)\right]+I(M)+J.
$$

Every coefficient, node-cache, value-cache, and designated metadata coordinate also obeys the explicit whole-program profile envelope.

## Depends on

- [fri-measured-extractor](def-fri-measured-extractor.md)

## Proof

Add the initialization envelope, all $N$ scan-cell envelopes, and the final interpolation envelope. The selected cache contributes at most $M$ extra word reads. Every interpolation of size $m$ uses exactly $m(m-1)$ inverse requests. Its combined additions/subtractions fit one $I(m)$ budget, as do its multiplications and equality tests separately. Power-sum evaluation fits $E(m)$. Only the final round evaluates the transmitted polynomial, giving one $E(d)$ per position. Explicit squaring and binary-power bounds fit $G$; initialization multiplications fit $J$. All branches, including the initial degree rejection, are included. No safe-history, honesty, radius, or $M\leq N$ premise is used.

## Lean

Formalized as [`Fri.Spec.Extractor.profile_extractProgram_word_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.profile_extractProgram_word_le), [`Fri.Spec.Extractor.profile_extractProgram_apply_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.profile_extractProgram_apply_le), [`Fri.Spec.Extractor.profile_extractProgram_inv_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.profile_extractProgram_inv_le), [`Fri.Spec.Extractor.profile_extractProgram_domainRead_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.profile_extractProgram_domainRead_le), [`Fri.Spec.Extractor.profile_extractProgram_challengeRead_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.profile_extractProgram_challengeRead_le), [`Fri.Spec.Extractor.profile_extractProgram_finalPolynomialRead`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.profile_extractProgram_finalPolynomialRead), [`Fri.Spec.Extractor.profile_extractProgram_add_sub_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.profile_extractProgram_add_sub_le), [`Fri.Spec.Extractor.profile_extractProgram_mul_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.profile_extractProgram_mul_le), [`Fri.Spec.Extractor.profile_extractProgram_eq_le`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.Spec.Extractor.profile_extractProgram_eq_le).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 224](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L224)

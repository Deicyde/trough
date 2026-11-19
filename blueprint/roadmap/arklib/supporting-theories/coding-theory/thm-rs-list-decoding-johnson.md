---
declaration: theorem
origin: cited
lean: ReedSolomon.listDecodable_reedSolomon
statement: formalized
proof: formalized
---

# List decoding of Reed–Solomon codes up to the Johnson bound

Let $\mathcal{L}$ be a nonempty finite domain embedded in a field $\mathbb{F}$, let $d>0$, and let $\rho=\min\{d,|\mathcal{L}|\}/|\mathcal{L}|$ be the rate of $\mathrm{RS}[\mathbb{F},\mathcal{L},d]$. For every real $\eta>0$, the code $\mathrm{RS}[\mathbb{F},\mathcal{L},d]$ is $\bigl(1-\sqrt{\rho}-\eta,\ 1/(2\eta\sqrt{\rho})\bigr)$-list decodable. The field need not be finite, and the bound does not depend on $|\mathbb{F}|$.

## Depends on

- [Reed-Solomon Code](def-reed-solomon-code.md)
- [List Decodability](def-list-decodable.md)

## Proof

Two distinct codewords agree in fewer than $d$ positions, so their agreement is at most $\min\{d,|\mathcal{L}|\}=\rho|\mathcal{L}|$. A counting bound for any code whose pairwise agreements are this small gives at most $1/(2\eta\sqrt{\rho})$ codewords within relative distance $1-\sqrt{\rho}-\eta$ of any word. This is Theorem 4.3 of ([Arnon et al. 2024](https://eprint.iacr.org/2024/1586)).

## Lean

Formalized as [`ReedSolomon.listDecodable_reedSolomon`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/ReedSolomon.listDecodable_reedSolomon).

## Sources

- [ArkLib blueprint: coding_theory/defs.tex, line 136](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/coding_theory/defs.tex#L136)

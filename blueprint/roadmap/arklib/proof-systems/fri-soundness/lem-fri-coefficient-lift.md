---
declaration: lemma
origin: cited
lean: Fri.exists_codeword_agree_of_coefficients
statement: formalized
proof: formalized
---

# fri-coefficient-lift

If every $f_j$ agrees with a codeword in $C'$ on $T\subseteq D'$, then a single codeword in $C$ agrees with $f$ on the whole preimage of $T$ under $x\mapsto x^m$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Choose degree-$\lt d$ polynomials $p_j$ witnessing agreement on $T$ and recombine them as $p(X)=\sum_{j\lt m}X^j p_j(X^m)$. This polynomial has degree less than $md$. Evaluation on every block above $T$ recovers its interpolant and hence the word.

## Lean

Formalized as [`Fri.exists_codeword_agree_of_coefficients`](https://verified-zkevm.github.io/ArkLib/docs/find/#doc/Fri.exists_codeword_agree_of_coefficients).

## Sources

- [ArkLib blueprint: proof_systems/fri.tex, line 18](https://github.com/Verified-zkEVM/ArkLib/blob/e1c185ba001d225d1f3ea84071d67a8c6c56d6a0/blueprint/src/proof_systems/fri.tex#L18)

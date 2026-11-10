---
declaration: lemma
origin: cited
lean: IsSimpleRing.mulLeft_det_eq_mulRight_det
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/518
---

# IsSimpleRing.mulLeft_det_eq_mulRight_det

Say $B$ is a finite-dimensional central simple algebra over a field $k$, and $u\in B^\times$. Let $\ell_u:B\to B$ be the $k$-linear mapping $x$ to $ux$ and let $r_u:B\to B$ be the $k$-linear map sending $x$ to $xu$. Then $\det(\ell_u)=\det(r_u)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Determinants are unchanged by base extension, so WLOG $k$ is algebraically closed. Then it's known that $B$ must be a matrix algebra, say $M_n(k)$. Now $u$ can be thought of as a matrix which has its own intrinsic determinant $d$, and $B$ as a left $B$-module becomes a direct sum of $n$ copies of $V$, the standard $n$-dimensional representation of $B$. Thus $\det(\ell_u)=d^n$. Similarly $\det(r_u)=d^n$ and in particular they are equal.

## Lean

Formalized as [`IsSimpleRing.mulLeft_det_eq_mulRight_det`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsSimpleRing.mulLeft_det_eq_mulRight_det).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 416](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L416)

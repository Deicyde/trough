---
declaration: theorem
origin: cited
lean: chapter7.Theorem₁
statement: formalized
---

# diagonalize_real_symmetric

For every real symmetric matrix $A$ there is a real orthogonal matrix $Q$ such that $Q^{T}AQ$ is diagonal.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The theorem follows in three quick steps. Let $A$ be a real symmetric $n \times n$ matrix.

- (A) Consider the map $f_A : O(n) \to \mathbb{R}^{n \times n}$ with $f_A(P) := P^T A P$. The map $f_A$ is continuous on the compact set $O(n)$, and so the image $f_A(O(n))$ is compact.
- (B) The function $\operatorname{Od} : f_A(O(n)) \to \mathbb{R}$ is continuous, hence it assumes a minimum, say at $D = Q^T A Q \in f_A(O(n))$.
- (C) The value $\operatorname{Od}(D)$ must be zero, and hence $D$ is a diagonal matrix as required.

Indeed, if $\operatorname{Od}(D) > 0$, then applying the Lemma we find $U \in O(n)$ with $\operatorname{Od}(U^T D U) < \operatorname{Od}(D)$. But

$$
U^T D U = U^T Q^T A Q U = (QU)^T A (QU)
$$

is in $f_A(O(n))$ (remember $O(n)$ is a group!) with $\operatorname{Od}$-value smaller than that of $D$ — contradiction, and end of proof.

## Lean

Stated as [`chapter7.Theorem₁`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter7.Theorem₁); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter07.tex, line 78](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter07.tex#L78)

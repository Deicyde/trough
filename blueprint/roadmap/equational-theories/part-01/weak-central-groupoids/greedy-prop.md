---
declaration: proposition
origin: cited
lean: RelaxedVeryWeakCentralGroupoid.Greedy.exists_extension
statement: formalized
---

# Completion property

Let $G_0$ be a directed graph satisfying claims 1', 2, 3, 4. Then any finite partial extension of $G_0$ with carrier $G_0 \times \mathbb{N}$ (and projection map $\pi(a,n) = a$) can be completed to a complete extension.

## Depends on

- [Equation 1485](../selected-laws/part-02/eq1485.md)

## Proof

By the previous comments, we can ignore Claim 4 as it is automatic, and focus on completing the partial weak central groupoid on $G$ to a complete weak central groupoid by ensuring Claims 1, 2, 3 hold. By the usual greedy algorithm, it suffices to show that any individual failure of Claim 1, 2 or 3 can be resolved by adding some finite number of edges to the graph.

Suppose first that Claim 2 fails, that is to say the partial weak central groupoid contains an edge $(a,n) \to (b,m)$ that is not the initial segment of any good path. Since the base relaxed weak central groupoid $G_0$ satisfies Claim 2, we can find a good path $a \to b \to c$ in the base. We then pick a natural number $l$ not previously occurring in the partial weak central groupoid, and adjoin the edge $(b,m) \to (c,l)$ to that partial weak central groupoid. All new paths created in this way are declared good or bad depending on whether their images in $G_0$ are good or bad, in particular $(a,n) \to (b,m) \to (c,l)$ is good. This can be checked to still be a partial extension of $G_0$ (no violation of Claim 1” is created), and now Claim 2 is resolved at for the edge $(a,n) \to (b,m)$. A similar argument permits one to resolve any violations of Claim 3.

If Claim 1 is violated, then there is a pair $(a,n), (b,m)$ that currently has no good path of length two in the partial weak central groupoid. As the base relaxed weak central groupoid $G_0$ satisfies Claim 1', we can find a good path $a \to c \to b$ in $G_0$. We then pick a natural number $l$ not previously occurring, and adjoin the edges $(a,n) \to (c,l) \to (b,m)$. All new paths created in this way are declared good or bad depending on whether their images in $G_0$ are good or bad, in particular $(a,n) \to (c,l) \to (b,m) \to (c,l)$. One can check that this is still a partial extension of $G_0$ (no violation of Claim 1” is created), and now Claim 1 is resolved at the pair $(a,n), (b,m)$.

## Lean

Formalized as [`RelaxedVeryWeakCentralGroupoid.Greedy.exists_extension`](https://teorth.github.io/equational_theories/docs/find/#doc/RelaxedVeryWeakCentralGroupoid.Greedy.exists_extension).

## Sources

- [Equational Theories blueprint: chapter/weak_central_groupoids.tex, line 87](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/weak_central_groupoids.tex#L87)

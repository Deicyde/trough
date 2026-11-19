---
declaration: proposition
origin: cited
lean: ConNF.BaseApprox.addOrbit
statement: formalized
proof: formalized
---

# adding orbits

Let $\psi$ be a base approximation, and let $L : \mathbb N \to {\mathcal L}$ be a function such that

$$
L(m) = L(n) \to L(m+k) = L(n+k)
$$

for all integers $m, n, k : \mathbb Z$. Suppose that for all $n$, $L(n) \notin \operatorname{\mathsf{coim}} \psi^{\mathcal L}$. Then there is an extension $\chi \geq \psi$ such that $\chi^{\mathcal L}(L(n)) = L(n+1)$ and $\operatorname{\mathsf{coim}} \chi^{\mathcal L} = \operatorname{\mathsf{coim}} \psi^{\mathcal L} \cup \operatorname{\mathsf{ran}} L$.

## Depends on

- [BaseApprox.LE](def-baseapprox-le.md)

## Proof

Define the relation

$$
R = \{ (L(n), L(n+1)) \mid n : \mathbb Z \}
$$

This clearly has equal image and coimage. It is injective: if $(L_1, L_3), (L_2, L_3) \in R$, then there are $m, n : \mathbb Z$ such that

$$
L_1 = L(m);\quad L_3 = L(m + 1);\quad L_2 = L(n);\quad L_3 = L(n + 1)
$$

So $L(m + 1) = L(n + 1)$, giving $L_1 = L(m) = L(n) = L_2$ by substituting $k = -1$ in the hypothesis. It is also coinjective by substituting $k = 1$ in the hypothesis. So $R$ is permutative. Therefore, $\psi^{\mathcal L} \sqcup R$ is a permutative relation, so $(\psi^{E{\mathcal A}}, \psi^{\mathcal L} \sqcup R)$ is an extension of $\psi$, and it clearly satisfies the result.

## Lean

Formalized as [`ConNF.BaseApprox.addOrbit`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox.addOrbit).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 144](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L144)

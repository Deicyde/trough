---
declaration: proposition
origin: cited
lean: Rel.permutativeExtension
statement: formalized
proof: formalized
---

# completing restricted orbits

Let $R : \tau \to \tau \to \mathsf{Prop}$ be a one-to-one relation, and let $(t, f, \pi)$ be an orbit restriction for $\operatorname{\mathsf{field}} R$ over some type $\sigma$. Then there is a permutative relation $T$ such that

- $\operatorname{\mathsf{coim}} T \subseteq \operatorname{\mathsf{field}} R \cup t$;
- $\#\operatorname{\mathsf{coim}} T \leq \max(\aleph_0, \#\operatorname{\mathsf{coim}} R)$;
- $R \leq T$; and
- if $(x, y) \in T$, then $(x, y) \in R \vee f(y) = \pi(f(x))$.

## Depends on

- [OrbitRestriction](def-orbitrestriction.md)

## Proof

For each $u : \sigma$, define an injection $i_u : \operatorname{\mathsf{field}} R \times \mathbb N \to \tau$ where $\operatorname{\mathsf{im}} i_u \subseteq t \cap f^{-1}(u)$. Define a relation $S$ on $\tau$ by the following constructors.

$$
\begin{aligned}
\forall x \in \operatorname{\mathsf{coim}} R \setminus \operatorname{\mathsf{im}} R,\, &(i_{\pi^{-1}(f(x))}(x, 0), x) \in S \\
\forall n : \mathbb N,\, \forall x \in \operatorname{\mathsf{coim}} R \setminus \operatorname{\mathsf{im}} R,\, &(i_{\pi^{-n-2}(x)}(x, n+1), i_{\pi^{-n-1}(x)}(x, n)) \in S \\
\forall x \in \operatorname{\mathsf{im}} R \setminus \operatorname{\mathsf{coim}} R,\, &(x, i_{\pi(f(x))}(x, 0)) \in S \\
\forall n : \mathbb N,\, \forall x \in \operatorname{\mathsf{im}} R \setminus \operatorname{\mathsf{coim}} R,\, &(i_{\pi^{n+1}(f(x))}(x, n), i_{\pi^{n+2}(f(x))}(x, n+1)) \in S
\end{aligned}
$$

Note that $(x, y) \in S$ implies $f(y) = \pi(f(x))$. Finally, as $R \sqcup S$ is permutative, it satisfies the required conclusion.

## Lean

Formalized as [`Rel.permutativeExtension`](https://leanprover-community.github.io/con-nf/doc/find/#doc/Rel.permutativeExtension).

## Sources

- [Consistency of New Foundations blueprint: chapters/auxiliary.tex, line 58](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/auxiliary.tex#L58)

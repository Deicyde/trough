# Conventions

- We are working in Lean's type theory, so cardinals and ordinals are quotients of a large type. In particular, cardinals are not just specific ordinals, and types cannot be ordinals.
- We write $\#\tau$ for the cardinality of a type $\tau$.
- If $\tau$ is a type endowed with a well-order $<$, we write $\operatorname{\mathsf{ot}}(\tau)$ for the order type of $\tau$ with this well-ordering.
- The initial ordinal corresponding to a cardinal $c$ is denoted $\operatorname{\mathsf{ord}}(c)$. The cofinality of an ordinal $o$ is $\operatorname{\mathsf{cof}}(o)$, and this is a cardinal.
- The symmetric difference of two sets is denoted $s \mathrel{\triangle} t := (s \setminus t) \cup (t \setminus s)$. Note that $(s \mathrel{\triangle} t) \cup (s \cap t) = s \cup t$, and the union on the left-hand side is disjoint.
- We use $f[s]$ for the direct image $\{ f(x) \mid x \in s \}$. We write $f^{-1}[s]$ for the inverse image $\{ x \mid f(x) \in s \}$, and $f^{-1}(x)$ for the fibre $\{ y \mid f(y) = x \}$.
- For any type $\alpha$, we write $\operatorname{\mathsf{Part}} \alpha$ for the type $\sum_{p : \mathsf{Prop}} (p \to \alpha)$.

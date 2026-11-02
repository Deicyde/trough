---
declaration: corollary
origin: cited
lean: cor_multiDist_chainRule
statement: formalized
proof: formalized
---

# cor-multid

Let $G$ be an abelian group and let $m \geq 2$. Suppose that $X_{i,j}$, $1 \leq i, j \leq m$, are independent $G$-valued random variables. Then

$$
\begin{aligned}
&\mathbb{I}[ \bigl(\sum_{i=1}^m X_{i,j}\bigr)_{j =1}^{m} : \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i = 1}^m \; \big| \; \sum_{i=1}^m \sum_{j = 1}^m  X_{i,j} ] \\
&\quad \leq \sum_{j=1}^{m-1} \Bigl(D[(X_{i, j})_{i = 1}^m] - D[ (X_{i, j})_{i = 1}^m  \; \big| \; (X_{i,j} + \cdots + X_{i,m})_{i =1}^m ]\Bigr) \\ & \qquad\qquad\qquad\qquad +  D[(X_{i,m})_{i=1}^m] - D[ \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i=1}^m ],
\end{aligned}
$$

where all the multidistances here involve the indexing set $\{1,\dots, m\}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [multidist-chain-rule-iter](multidist-chain-rule-iter.md)
- [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md)

## Proof

In [Lemma multidist-chain-rule-iter](multidist-chain-rule-iter.md) we take $G_d := G^d$ with the maps $\pi_d \colon G^m \to G^d$ for $d=1,\dots,m$ defined by

$$
\pi_d(x_1,\dots,x_m) := (x_1,\dots,x_{d-1}, x_d + \cdots + x_m)
$$

with $\pi_0=0$. Since $\pi_{d-1}(x)$ can be obtained from $\pi_{d}(x)$ by applying a homomorphism, we obtain a sequence of the form (g-seq).

Now we apply [Lemma multidist-chain-rule-iter](multidist-chain-rule-iter.md) with $I = \{1,\dots, m\}$ and $X_i := (X_{i,j})_{j = 1}^m$. Using joint independence and [Additivity of entropy](../../shannon-entropy-inequalities/part-02/add-entropy.md), we find that

$$
D[ X_{[m]} ] = \sum_{j=1}^m D[ (X_{i,j})_{1 \leq i \leq m} ].
$$

On the other hand, for $1 \leq j \leq m-1$, we see that once $\pi_{j}(X_i)$ is fixed, $\pi_{j+1}(X_i)$ is determined by $X_{i, j}$ and vice versa, so

$$
D[ \pi_{j+1}(X_{[m]}) \; | \; \pi_{j}(X_{[m]}) ] = D[ (X_{i, j})_{1 \leq i \leq m} \; | \; \pi_{j}(X_{[m]} )].
$$

Since the $X_{i,j}$ are jointly independent, we may further simplify:

$$
D[ (X_{i, j})_{1 \leq i \leq m} \; | \; \pi_{j}(X_{[m]})] = D[ (X_{i,j})_{1 \leq i \leq m} \; | \; ( X_{i, j} + \cdots + X_{i, m})_{1 \leq i \leq m} ].
$$

Putting all this into the conclusion of [Lemma multidist-chain-rule-iter](multidist-chain-rule-iter.md), we obtain

$$
\sum_{j=1}^{m} D[ (X_{i,j})_{1 \leq i \leq m} ]
\geq
\begin{aligned}[t]
&\sum_{j=1}^{m-1} D[ (X_{i,j})_{1 \leq i \leq m} \; | \; (X_{i,j} + \cdots + X_{i,m})_{1 \leq i \leq m} ] \\
&\!\!\!+
D[ \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{1 \leq i \leq m}] \\
&\!\!\!+\mathbb{I}[  \bigl(\sum_{i=1}^m X_{i,j}\bigr)_{j =1}^{m} : \bigl(\sum_{j=1}^m X_{i,j}\bigr)_{i = 1}^m \; \big| \; \sum_{i=1}^m \sum_{j = 1}^m  X_{i,j} ]
\end{aligned}
$$

and the claim follows by rearranging.

## Lean

Formalized as [`cor_multiDist_chainRule`](https://teorth.github.io/pfr/docs/find/#doc/cor_multiDist_chainRule).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 455](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L455)

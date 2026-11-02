---
declaration: theorem
origin: cited
lean: approx_hom_pfr
statement: formalized
proof: formalized
---

# Approximate homomorphism form of PFR

Let $G,G'$ be finite abelian $2$-groups. Let $f: G \to G'$ be a function, and suppose that there are at least $|G|^2 / K$ pairs $(x,y) \in G^2$ such that

$$
f(x+y) = f(x) + f(y).
$$

Then there exists a homomorphism $\phi: G \to G'$ and a constant $c \in G'$ such that $f(x) = \phi(x)+c$ for at least $|G| / (2 ^ {144} * K ^ {122})$ values of $x \in G$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Goursat type theorem](../homomorphism-version-of-pfr/goursat.md)
- [Cauchy–Schwarz bound](cs-bound.md)
- [Balog–Szemerédi–Gowers lemma](bsg.md)
- [pfr-9-aux'](../further-improvement-to-exponent/studying-a-minimizer/pfr-9-aux-2.md)

## Proof

Consider the graph $A \subset G \times G'$ defined by

$$
A := \{ (x,f(x)): x \in G \}.
$$

Clearly, $|A| = |G|$. By hypothesis, we have $a+a' \in A$ for at least $|A|^2/K$ pairs $(a,a') \in A^2$. By [Cauchy–Schwarz bound](cs-bound.md), this implies that $E(A) \geq \frac{1}{K^2} \left( \frac{|A|}{|G \times G'|} \right)^3$. Applying [Balog–Szemerédi–Gowers lemma](bsg.md), we conclude that there exists a subset $A' \subset A$ with $|A'| \geq |A|/C_1 K^{2C_2}$ and $|A'+A'| \leq C_1C_3 K^{2(C_2+C_4)} |A'|$. Applying [Corollary pfr-9-aux'](../further-improvement-to-exponent/studying-a-minimizer/pfr-9-aux-2.md), we may find a subspace $H \subset G \times G'$ such that $|H| / |A'| \in [L^{-8}, L^{8}]$ and a subset $c$ of cardinality at most $L^5 |A'|^{1/2} / |H|^{1/2}$ such that $A' \subseteq c + H$, where $L = C_1C_3 K^{2(C_2+C_4)}$. If we let $H_0,H_1$ be as in [Goursat type theorem](../homomorphism-version-of-pfr/goursat.md), this implies on taking projections the projection of $A'$ to $G$ is covered by at most $|c|$ translates of $H_0$. This implies that

$$
|c| |H_0| \geq |A'|;
$$

since $|H_0| |H_1| = |H|$, we conclude that

$$
|H_1| \leq |c| |H|/|A'|.
$$

By hypothesis, $A'$ is covered by at most $|c|$ translates of $H$, and hence by at most $|c| |H_1|$ translates of $\{ (x,\phi(x)): x \in G \}$. As $\phi$ is a homomorphism, each such translate can be written in the form $\{ (x,\phi(x)+c): x \in G \}$ for some $c \in G'$. The number of translates is bounded by

$$
|c|^2 \frac{|H|}{|A'|} \leq \left(L^5 \frac{|A'|^{1/2}}{|H|^{1/2}}\right)^2 \frac{|H|}{|A'|} = L^{10}.
$$

By the pigeonhole principle, one of these translates must then contain at least $|A'|/L^{10} \geq |G| / (C_1C_3 K^{2(C_2+C_4)})^{10} (C_1 K^{2C_2})$ elements of $A'$ (and hence of $A$), and the claim follows.

## Lean

Formalized as [`approx_hom_pfr`](https://teorth.github.io/pfr/docs/find/#doc/approx_hom_pfr).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/approx_hom_pfr.tex, line 62](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/approx_hom_pfr.tex#L62)

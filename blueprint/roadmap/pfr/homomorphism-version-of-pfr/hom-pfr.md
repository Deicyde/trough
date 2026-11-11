---
declaration: theorem
origin: cited
lean: homomorphism_pfr
statement: formalized
proof: formalized
---

# Homomorphism form of PFR

Let $f: G \to G'$ be a function, and let $S$ denote the set

$$
S := \{ f(x+y)-f(x)-f(y): x,y \in G \}.
$$

Then there exists a homomorphism $\phi: G \to G'$ such that

$$
|\{ f(x) - \phi(x): x \in G \}| \leq |S|^{10}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Goursat type theorem](goursat.md)
- [pfr-9-aux'](../further-improvement-to-exponent/studying-a-minimizer/pfr-9-aux-2.md)

## Proof

Consider the graph $A \subset G \times G'$ defined by

$$
A := \{ (x,f(x)): x \in G \}.
$$

Clearly, $|A| = |G|$. By hypothesis, we have

$$
A+A \subset \{ (x,f(x)+s): x \in G, s \in S\}
$$

and hence $|A+A| \leq |S| |A|$. Applying [Corollary pfr-9-aux'](../further-improvement-to-exponent/studying-a-minimizer/pfr-9-aux-2.md), we may find a subspace $H \subset G \times G'$ such that $|H|/ |A| \in [|S|^{-8}, |S|^{8}]$ and $A$ is covered by $c + H$ with $|c| \le |S|^5|A|^{1/2} / |H|^{1/2}$. If we let $H_0, H_1$ be as in [Goursat type theorem](goursat.md), this implies on taking projections that $G$ is covered by at most $|c|$ translates of $H_0$. This implies that

$$
|c| |H_0| \geq |G|;
$$

since $|H_0| |H_1| = |H|$, we conclude that

$$
|H_1| \leq |c| |H|/|G| = |c| |H|/|A|.
$$

By hypothesis, $A$ is covered by at most $|c|$ translates of $H$, and hence by at most $|c| |H_1|$ translates of $\{ (x,\phi(x)): x \in G \}$. As $\phi$ is a homomorphism, each such translate can be written in the form $\{ (x,\phi(x)+d): x \in G \}$ for some $d \in G'$. Since

$$
|c| |H_1| \le |c|^2 \frac{|H|}{|A|} \le \left(|S|^5 \frac{|A|^{1/2}}{|H|^{1/2}}\right)^2 \frac{|H|}{|A|}
= |S|^{10},
$$

the result follows.

## Lean

Formalized as [`homomorphism_pfr`](https://teorth.github.io/pfr/docs/find/#doc/homomorphism_pfr).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/hom_pfr.tex, line 19](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/hom_pfr.tex#L19)

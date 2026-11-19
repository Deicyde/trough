---
declaration: theorem
origin: cited
lean: book.quadratic_reciprocity.quadratic_reciprocity_2
statement: formalized
---

# Quadratic reciprocity II

Let $p$ and $q$ be different odd primes. Then

$$
(\frac{q}{p})(\frac{p}{q}) = (-1)^{\frac{p-1}{2} \frac{q-1}{2}}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [A](fact-a.md)
- [B](fact-b.md)

## Proof

The second proof does not use Gauss' lemma, instead it employs so-called “Gauss sums” in finite fields. Gauss invented them in his study of the equation $x^p - 1 = 0$ and the arithmetical properties of the field $\mathbb{Q}(\zeta)$ (called cyclotomic field), where $\zeta$ is a $p$-th root of unity. They have been the starting point for the search for higher reciprocity laws in general number fields.

Consider the *Gauss sum*

$$
G := \sum_{i=1}^{p-1} (\frac{i}{p}) \zeta^i \in F,
$$

where $(\frac{i}{p})$ is the Legendre symbol. For the proof we derive two different expressions for $G^q$ and then set them equal.

**First expression.** We have

$$
G^q = \sum_{i=1}^{p-1} (\frac{i}{p})^q \zeta^{iq} = \sum_{i=1}^{p-1} (\frac{i}{p}) \zeta^{iq} = (\frac{q}{p}) \sum_{i=1}^{p-1} (\frac{iq}{p}) \zeta^{iq} = (\frac{q}{p}) G,\qquad\text{(6)}
$$

where the first equality follows from $(a + b)^q = a^q + b^q$, the second uses that $(\frac{i}{p})^q = (\frac{i}{p})$ since $q$ is odd, the third one is derived from [(1)](product-rule.md), which yields $(\frac{i}{p}) = (\frac{q}{p}) (\frac{iq}{p})$, and the last one holds since $iq$ runs with $i$ through all nonzero residues modulo $p$.

**Second expression.** Suppose we can prove

$$
G^2 = (-1)^{\frac{p-1}{2}} p,\qquad\text{(7)}
$$

then we are quickly done. Indeed,

$$
G^q = G (G^2)^{\frac{q-1}{2}} = G (-1)^{\frac{p-1}{2} \frac{q-1}{2}} p^{\frac{q-1}{2}} = G (\frac{p}{q}) (-1)^{\frac{p-1}{2} \frac{q-1}{2}}.\qquad\text{(8)}
$$

Equating the expressions in (6) and (8) and cancelling $G$, which is nonzero by (7), we find $(\frac{q}{p}) = (\frac{p}{q}) (-1)^{\frac{p-1}{2} \frac{q-1}{2}}$, and thus

$$
(\frac{q}{p}) (\frac{p}{q}) = (-1)^{\frac{p-1}{2} \frac{q-1}{2}}.
$$

It remains to verify (7), and for this we first make two simple observations:

- $\sum_{i=1}^{p} \zeta^i = 0$ and thus $\sum_{i=1}^{p-1} \zeta^i = -1$. Just note that $-\sum_{i=1}^{p} \zeta^i$ is the coefficient of $x^{p-1}$ in $x^p - 1 = \prod_{i=1}^{p} (x - \zeta^i)$, and thus 0.
- $\sum_{k=1}^{p-1} (\frac{k}{p}) = 0$ and thus $\sum_{k=1}^{p-2} (\frac{k}{p}) = - (\frac{-1}{p})$, since there are equally many quadratic residues and nonresidues.

We have

$$
G^2 = \left(\sum_{i=1}^{p-1} (\frac{i}{p}) \zeta^i\right) \left(\sum_{j=1}^{p-1} (\frac{j}{p}) \zeta^j\right) = \sum_{i,j} (\frac{ij}{p}) \zeta^{i+j}.
$$

Setting $j \equiv ik \pmod{p}$ we find

$$
G^2 = \sum_{i,k} (\frac{k}{p}) \zeta^{i(1+k)} = \sum_{k=1}^{p-1} (\frac{k}{p}) \sum_{i=1}^{p-1} \zeta^{(1+k)i}.
$$

For $k = p - 1 \equiv -1 \pmod{p}$ this gives $(\frac{-1}{p}) (p - 1)$, since $\zeta^{1+k} = 1$. Move $k = p - 1$ in front and write

$$
G^2 = (\frac{-1}{p}) (p - 1) + \sum_{k=1}^{p-2} (\frac{k}{p}) \sum_{i=1}^{p-1} \zeta^{(1+k)i}.
$$

Since $\zeta^{1+k}$ is a generator of the group for $k \ne p - 1$, the inner sum equals $\sum_{i=1}^{p-1} \zeta^i = -1$ for all $k \ne p - 1$ by our first observation. Hence the second summand is $-\sum_{k=1}^{p-2} (\frac{k}{p}) = (\frac{-1}{p})$ by our second observation. It follows that $G^2 = (\frac{-1}{p}) p$ and thus with Euler's criterion $G^2 = (-1)^{\frac{p-1}{2}} p$, which completes the proof.

## Lean

Stated as [`book.quadratic_reciprocity.quadratic_reciprocity_2`](https://mo271.github.io/FormalBook/docs/find/#doc/book.quadratic_reciprocity.quadratic_reciprocity_2); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter05.tex, line 176](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter05.tex#L176)

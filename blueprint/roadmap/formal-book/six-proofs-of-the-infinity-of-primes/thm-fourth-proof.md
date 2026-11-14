---
declaration: theorem
origin: cited
lean: infinity_of_primes₄
statement: formalized
---

# Fourth Proof

The prime counting function is unbounded

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $\pi(x) := \#\{p \leq x : p \in \mathbb{P}\}$ be the number of primes that are less than or equal to the real number $x$. We number the primes $\mathbb{P} = \{p_1, p_2, p_3, \dots \}$ in increasing order. Consider the natural logarithm $\log x$, defined as

$$
\log x = \int_1^x \frac{1}{t} dt.
$$

Now we compare the area below the graph of $f(t) = \frac{1}{t}$ with an upper step function. (See also the appendix for this method.) Thus for $n \leq x < n+1$ we have

$$
\log x \leq 1 + \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{n-1} + \frac{1}{n} \leq \sum \frac{1}{m},
$$

where the sum extends over all $m \in \mathbb{N}$ which have only prime divisors $p \leq x$.

Since every such $m$ can be written in a unique way as a product of the form $\prod_{p \leq x} p^{k_p}$, we see that the last sum is equal to

$$
\prod_{p \in \mathbb{P}, p \leq x} \left( \sum_{k \geq 0} \frac{1}{p^k} \right).
$$

The inner sum is a geometric series with ratio $\frac{1}{p}$, hence

$$
\log x \leq \prod_{p \leq x} \frac{1}{1 - \frac{1}{p}} = \prod_{p \leq x} \frac{p}{p - 1} = \prod_{k=1}^{\pi(x)} \frac{p_k}{p_k - 1}.
$$

Now clearly $p_k \geq k+1$, and thus

$$
\frac{p_k}{p_k - 1} = 1 + \frac{1}{p_k - 1} \leq 1 + \frac{1}{k} = \frac{k+1}{k},
$$

and therefore

$$
\log x \leq \prod_{k=1}^{\pi(x)} \frac{k+1}{k} = \pi(x) + 1.
$$

Everybody knows that $\log x$ is not bounded, so we conclude that $\pi(x)$ is unbounded as well, and so there are infinitely many primes.

## Lean

Stated as [`infinity_of_primes₄`](https://mo271.github.io/FormalBook/docs/find/#doc/infinity_of_primes₄); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter01.tex, line 67](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter01.tex#L67)

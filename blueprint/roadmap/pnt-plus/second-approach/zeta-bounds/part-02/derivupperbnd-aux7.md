---
declaration: lemma
origin: cited
lean: DerivUpperBnd_aux7
statement: formalized
proof: formalized
---

# DerivUpperBnd-aux7

For any $s = \sigma + tI \in \mathbb{C}$, $1/2 \le \sigma\le 2, 3 < |t|$, and any $0 < A < 1$ sufficiently small, and $1-A/\log |t| \le \sigma$, we have

$$
\left\|s \cdot \int_{N}^{\infty}
\left(\left\lfloor x \right\rfloor + \frac{1}{2} - x\right) \cdot x^{-s-1} \cdot (-\log x)
\right\|
\le 2 \cdot |t| \cdot N^{-\sigma} / \sigma \cdot \log |t|.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Estimate $|s|= |\sigma + tI|$ by $|s|\le 2 +|t| \le 2|t|$ (since $|t|>3$). Estimating $|\left\lfloor x \right\rfloor+1/2-x|$ by $1$, and using $|x^{-s-1}| = x^{-\sigma-1}$, we have

$$
\left\| s \cdot \int_{N}^{\infty}
\left(\left\lfloor x \right\rfloor + \frac{1}{2} - x\right) \cdot x^{-s-1} \cdot (-\log x)
\right\|
\le 2 \cdot |t|
\int_{N}^{\infty} x^{-\sigma} \cdot (\log x).
$$

For the last integral, integrate by parts, getting:

$$
\int_{N}^{\infty} x^{-\sigma-1} \cdot (\log x) =
\frac{1}{\sigma}N^{-\sigma} \cdot \log N + \frac1{\sigma^2} \cdot N^{-\sigma}.
$$

Now use $\log N \le \log |t|$ to get the result.

## Lean

Formalized as [`DerivUpperBnd_aux7`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/DerivUpperBnd_aux7).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)

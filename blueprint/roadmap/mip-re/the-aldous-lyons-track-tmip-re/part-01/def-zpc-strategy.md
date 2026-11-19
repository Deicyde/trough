---
declaration: definition
origin: cited
lean: MIPRE.Tailored.PermStrategy, MIPRE.Tailored.PermStrategy.proj, MIPRE.Tailored.PermStrategy.value, MIPRE.Tailored.TailoredGame.HasPerfectZPC
statement: formalized
---

# Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283

A *signed permutation matrix* on $\mathbb{C}^m$ is a matrix $e_j \mapsto (-1)^{s(j)} e_{\sigma(j)}$ for a permutation $\sigma$ of $\{1, \dots, m\}$ and signs $s$: the action of a signed permutation of $\{\pm\} \times \{1, \dots, m\}$ on the anti-symmetric functions, in their standard basis. A *permutation strategy* for a tailored game assigns to each variable $X$ at each question $x$ an observable $U(x, X)$ on $\mathbb{C}^m$ that is a signed permutation matrix and an involution, the observables at a question commuting with each other; its measurement at $x$ is the Fourier transform

$$
P^x_a \;=\; \prod_{X \in S_x} \tfrac12\bigl({I} + (-1)^{a_X}\, U(x, X)\bigr),
\qquad a \in \mathbb{F}_2^{S_x},
$$

and its value is $\sum_{x, y} \mu(x, y) \sum_{a, b} \mathrm{tr}(P^x_a P^y_b)/m$ over the accepted $(a, b)$. It is *Z-aligned* when the observables of readable variables are diagonal, and *commutes along edges* when $U(x, X)$ and $U(y, Y)$ commute whenever $\mu(x, y) > 0$. A ZPC strategy is a Z-aligned permutation strategy commuting along edges, and it is *perfect* when its value is $1$.

## Depends on

- [Tailored game; II:1243](def-tailored-game.md)
- [The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006](def-fourier-forms.md)
- [Signed permutations; II:1008–1069](def-signed-perm.md)

## Lean

Formalized as [`MIPRE.Tailored.PermStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy), [`MIPRE.Tailored.PermStrategy.proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.proj), [`MIPRE.Tailored.PermStrategy.value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.value), [`MIPRE.Tailored.TailoredGame.HasPerfectZPC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredGame.HasPerfectZPC).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 103](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L103)

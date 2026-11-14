---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.PermStrategy.isPVMIn_proj, MIPRE.Tailored.PermStrategy.commute_proj, MIPRE.Tailored.PermStrategy.value_eq_one_of, MIPRE.Tailored.PermStrategy.dotBit_of_obsChar, MIPRE.Tailored.satisfies_ofFn_iff
statement: formalized
proof: formalized
---

# When a permutation strategy is perfect

The measurements of a permutation strategy are projective, and those at the two ends of an edge commute. The strategy is perfect when $P^x_a P^y_b = 0$ for every answer pair $(a, b)$ that the canonical decider rejects at an edge $(x, y)$. The canonical decider's check of a constraint $(\alpha, \beta, \gamma)$ on answers $(a, b)$ is $\langle \alpha, a\rangle + \langle \beta, b\rangle = \gamma$; and at an edge, if $U^\alpha V^\beta$ acts as $(-1)^\gamma$ on the range of $P^x_a P^y_b \neq 0$, where $U$ and $V$ are the observables at $x$ and $y$, then $(a, b)$ satisfies it (Claim II:2870).

## Depends on

- [Z-aligned permutation strategies commuting along edges; II:1043–1057, II:1279–1283](def-zpc-strategy.md)
- [Signed permutation matrices](lem-signed-perm.md)
- [The Fourier transform; II:974–1006](lem-fourier-pvm.md)

## Proof

The observables are involutive signed permutation matrices, hence self-adjoint (Lemma [Signed permutation matrices](lem-signed-perm.md)), and Lemma [The Fourier transform; II:974–1006](lem-fourier-pvm.md) applies. If the rejected pairs have $P^x_a P^y_b = 0$, the accepted pairs carry $\sum_{a, b} \mathrm{tr}(P^x_a P^y_b)/m = 1$ at each edge. The parity of the number of common ones of two vectors is their inner product. By the eigenvalue relations, $U^\alpha V^\beta P^x_a P^y_b = (-1)^{\langle \alpha, a\rangle + \langle \beta, b\rangle} P^x_a P^y_b$, as $V^\beta$ commutes with $P^x_a$ along an edge; comparing with $(-1)^\gamma P^x_a P^y_b \neq 0$ gives the constraint.

## Lean

Formalized as [`MIPRE.Tailored.PermStrategy.isPVMIn_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.isPVMIn_proj), [`MIPRE.Tailored.PermStrategy.commute_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.commute_proj), [`MIPRE.Tailored.PermStrategy.value_eq_one_of`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.value_eq_one_of), [`MIPRE.Tailored.PermStrategy.dotBit_of_obsChar`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.PermStrategy.dotBit_of_obsChar), [`MIPRE.Tailored.satisfies_ofFn_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.satisfies_ofFn_iff).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 229](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L229)

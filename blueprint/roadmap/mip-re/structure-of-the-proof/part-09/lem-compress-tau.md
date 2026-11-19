---
declaration: lemma
origin: cited
lean: MIPRE.Pipeline.exists_eps2_lower, MIPRE.Pipeline.exists_tau
statement: formalized
proof: formalized
---

# A universal repetition exponent

With $\varepsilon_2$ as in Lemma [The margin claim](lem-compress-margin.md), $1 / \varepsilon_2 \leq x^P$ for a universal $P$ and all $x$ past a threshold. Consequently, for every $c > 0$ and every $\beta$ there is a universal integer $\tau$ such that, with $z = \lambda n + 1$, for every $k \geq z^\tau$ and every $0 \leq B \leq z^\beta$, the repetition bound $\exp\bigl( -c\, \varepsilon^{13} k / (B + 1) \bigr)$ of Theorem [Parallel repetition of normal form verifiers](thm-parallel-repetition.md) is at most $\frac12$ for all $n \geq \tau$, all integers $\lambda \geq 1$ and all $\varepsilon \geq z^{-P}$; the counts $k(n) \geq z^\tau$ and $B(n) \leq z^{6\beta}$ of that theorem qualify.

## Depends on

- [The margin claim](lem-compress-margin.md)

## Proof

$1 / \varepsilon_2 = \bigl( 3 \sigma^{a_2} x^{\mu a_2} (8 a_1)^{1/b_1} x^{a_1/b_1} \bigr)^{1/b_2}$, and each factor is a power of $x$ once $x \geq \max\{3, 8 a_1\}$ and $\sigma \leq x^K$. Then $c\, \varepsilon^{13} z^\tau / (z^\beta + 1) \geq \frac{c}{2} z^{\tau - 13 P - \beta} \geq \frac{c}{2} z \geq \log 2$ for $\tau \geq 13 P + \beta + 1 + 2/c$ and $z \geq \tau$. Purely arithmetic, and computationally testable — the companion repository tests it.

## Lean

Formalized as [`MIPRE.Pipeline.exists_eps2_lower`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.exists_eps2_lower), [`MIPRE.Pipeline.exists_tau`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Pipeline.exists_tau).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 6515](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L6515)

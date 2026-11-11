---
declaration: section
origin: cited
lean: MetaMathlibExt.telescopicGcd, MetaMathlibExt.telescopicC, MetaMathlibExt.IsTelescopic
statement: formalized
proof: formalized
---

# Telescopic numerical semigroups

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/telescopic-numerical-semigroups/index.html).

## Prefix gcds of a sequence

For a finite sequence $G = (g_1, \dots, g_k)$ of natural numbers
and a natural number $j$, $d_j$ is the greatest common divisor of the first $j$ entries of $G$
(of all of $G$ when $j > k$), with $d_0 = 0$.

Formalized by `MetaMathlibExt.telescopicGcd`, a definition declared in [MathlibExt/NumberTheory/TelescopicSequence.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TelescopicSequence.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/telescopic-numerical-semigroups/index.html#telescopic-gcd).

## Successive gcd quotients

For a finite sequence $G = (g_1, \dots, g_k)$ of natural numbers,
let $d_i$ be the greatest common divisor of the first $i$ entries of $G$ (of all of $G$ when
$i > k$), with $d_0 = 0$. For $j \ge 1$ the successive gcd quotient is $c_j = d_{j-1} / d_j$,
taken to be $0$ when $d_j = 0$, that is, when the first $j$ entries are all zero; and $c_0 = 0$.

The source always assumes $g_1 > 0$ or $\gcd(G) = 1$, which avoids the degenerate case
$d_j = 0$. For example, $(660, 550, 352, 50, 201)$ has $(c_2, \dots, c_5) = (6, 5, 11, 2)$ and
$(3, 4, 5)$ has $(c_2, c_3) = (3, 1)$.

Formalized by `MetaMathlibExt.telescopicC`, a definition declared in [MathlibExt/NumberTheory/TelescopicSequence.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TelescopicSequence.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/telescopic-numerical-semigroups/index.html#telescopic-c).

## Telescopic sequences

Let $G = (g_1, \dots, g_k)$ be a finite sequence of natural numbers.
For $0 \le i \le k$ let $d_i$ be the greatest common divisor of $g_1, \dots, g_i$, with $d_0 = 0$,
and for $1 \le j \le k$ let $c_j = d_{j-1} / d_j$ be the successive gcd quotient, taken to be $0$
when $d_j = 0$. The sequence $G$ is telescopic when $k \ge 2$, $g_1 + g_2 > 0$, and for every $j$
with $2 \le j \le k$ the number $c_j g_j$ lies in the additive submonoid of $\mathbb{N}$ generated
by $g_1, \dots, g_{j-1}$.

Formalized by `MetaMathlibExt.IsTelescopic`, a definition declared in [MathlibExt/NumberTheory/TelescopicSequence.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/TelescopicSequence.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/telescopic-numerical-semigroups/index.html#is-telescopic).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Telescopic numerical semigroups](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/numerical-semigroups/telescopic-numerical-semigroups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/numerical-semigroups/telescopic-numerical-semigroups)

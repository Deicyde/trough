---
declaration: section
origin: cited
lean: MetaMathlibExt.spivey_bell_number_add, MetaMathlibExt.spivey_bell_recurrence, MetaMathlibExt.spivey_pq_bell
statement: formalized
proof: formalized
---

# Spivey's Bell number formula

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/spivey-s-bell-number-formula/index.html).

## Spivey's Bell number formula

For all natural numbers $m$ and $n$,

$$B_{n+m} = \sum_{j=0}^{m} \sum_{k=0}^{n} j^{n-k} \, S(m, j) \binom{n}{k} B_k,$$

where $B_k$ is the $k$-th Bell number, $S(m, j)$ is the Stirling number of the second kind, and
$0^0 = 1$.

## Sources

- Michael Z. Spivey, *A Generalized Recurrence for Bell Numbers*, Journal of Integer Sequences 11 (2008), Article 08.2.5, equation `Bell_Gen`, lines 113–117, <https://cs.uwaterloo.ca/journals/JIS/VOL11/Spivey/spivey25.tex>.

Formalized by `MetaMathlibExt.spivey_bell_number_add`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SpiveyBellNumberAddition.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/SpiveyBellNumberAddition.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/spivey-s-bell-number-formula/index.html#spivey-bell-number-add).

## Spivey's recurrence for Bell numbers

For all natural numbers $n$ and $m$,

$$B_{n+m} = \sum_{k=0}^{n} \sum_{j=0}^{m} j^{n-k} \, S(m, j) \binom{n}{k} B_k,$$

where $B_k$ is the $k$-th Bell number, $S(m, j)$ is the Stirling number of the second kind, and
$0^0 = 1$. This is Spivey's Bell number formula with the two finite sums interchanged.

## Sources

- Jacob Katriel, "On a Generalized Recurrence for Bell Numbers", Journal of Integer Sequences 11 (2008), Article 08.3.8, equation (Spivey), lines 77–81, https://cs.uwaterloo.ca/journals/JIS/VOL11/Katriel/katriel6.tex (quoting Michael Z. Spivey, "A generalized recurrence for Bell numbers", Journal of Integer Sequences 11 (2008), Article 08.2.5).

Formalized by `MetaMathlibExt.spivey_bell_recurrence`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SpiveyBellNumberAddition.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/SpiveyBellNumberAddition.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/spivey-s-bell-number-formula/index.html#spivey-bell-recurrence).

## The (p, q)-deformed Spivey formula

Let $p$ and $q$ be real numbers with
$0 < q < p \le 1$, and for $k \in \mathbb{N}$ put $[k] = (p^k - q^k)/(p - q)$. Define real numbers
$S(n, k)$ for $n, k \in \mathbb{N}$ by $S(0, 0) = 1$, $S(0, k) = 0$ for $k \ge 1$,
$S(n + 1, 0) = 0$, and, for $k \ge 1$,
$S(n + 1, k) = p^{n + 1 - k} q^{k - 1} S(n, k - 1) + [k] \, S(n, k)$, where the exponent
$n + 1 - k$ is read as $0$ when $k > n + 1$. Put $\tilde S(n, k) = p^{\binom{k}{2}} S(n, k)$ and
$\tilde B_n(x) = \sum_{k=0}^{n} \tilde S(n, k) \, x^k$ for real $x$. Then for all
$m, n \in \mathbb{N}$,

$$\tilde B_{n+m}(1) = \sum_{k=0}^{m} \sum_{j=0}^{n} \binom{n}{j} \tilde S(m, k) \, [k]^{n-j} \,
q^{jk} \, \tilde B_j\bigl(p^{n+m-j}\bigr),$$

with $0^0 = 1$.

Proof: We formalize the operator proof around equations `eq1`, `eq2'`, `eq4`, `meq`,
`pqexpn`, and `lasteq` in Oussi's paper, using formal power series in place of convergent series.

## Sources

- L. Oussi, *A (p,q)-Deformed Recurrence for the Bell Numbers*, Journal of Integer Sequences 23 (2020), Article 20.5.2, main theorem equation `lasteq`, lines 214-220, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Oussi/oussi5.tex>.

Formalized by `MetaMathlibExt.spivey_pq_bell`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/SpiveyPQBell.lean, line 1053](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/SpiveyPQBell.lean#L1053). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/spivey-s-bell-number-formula/index.html#spivey-pq-bell).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spivey's Bell number formula](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/spivey-s-bell-number-formula/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/spivey-s-bell-number-formula)

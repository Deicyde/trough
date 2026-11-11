---
declaration: section
origin: cited
lean: MetaMathlibExt.binomial_tMotzkin_generatingFunction
statement: formalized
proof: formalized
---

# Motzkin numbers and Motzkin paths: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/index.html).

Motzkin numbers and paths: colored, weighted and (u,l,d) Motzkin paths, humps and peaks, the Motzkin triangle, links with central trinomial coefficients, alternating Motzkin sums, Aigner's inequality, and Motzkin-related sequences such as A005773; weighted Motzkin paths used to compute Hankel determinants go to Hankel determinants and continued fractions.

## Generating function of binomial Motzkin paths

Let $t \ge 1$. A binomial $[t]$-Motzkin step
is one of $\binom{t}{k}$ differently colored steps that change the height by $1 - k$, for some
$k \in \{0, 1, \dots, t\}$. For $n \ge 0$ let $M_n$ be the number of sequences of $n$ such steps
for which, starting from height $0$, the height after the first $m$ steps is nonnegative for
every $0 \le m \le n$ and the height after all $n$ steps is $0$. Then, as formal power series
over $\mathbb{Q}$,

$$\sum_{n \ge 0} M_n z^n = C_t(z)^t, \qquad
C_t(z) = \sum_{n \ge 0} \frac{1}{(t-1)n + 1} \binom{tn}{n} z^n.$$

## Sources

- Naiomi T. Cameron and Jillian E. McLeod, "Returns and Hills on Generalized Dyck Paths," Journal of Integer Sequences 19 (2016), Article 16.6.1, Theorem (binomial `[t]`-Motzkin generating function), lines 987–989, https://cs.uwaterloo.ca/journals/JIS/VOL19/McLeod/mcleod3.tex

Formalized by `MetaMathlibExt.binomial_tMotzkin_generatingFunction`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BinomialTMotzkinPaths.lean, line 756](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/BinomialTMotzkinPaths.lean#L756). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/index.html#binomial-t-motzkin-generating-function).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Motzkin numbers and Motzkin paths](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers)

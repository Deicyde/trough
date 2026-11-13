---
declaration: section
origin: cited
lean: MetaMathlibExt.a005773Recurrence_ratio_bounds, MetaMathlibExt.a005773Recurrence_diff_logBalanced, MetaMathlibExt.a005773Recurrence_thirdDiff_logConvex_logBalanced, MetaMathlibExt.a005773Recurrence_weighted_logConcave, MetaMathlibExt.a005773Recurrence_pow_logConvex
statement: formalized
---

# Log-behavior of Motzkin prefix numbers

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/log-behavior-of-motzkin-prefix-numbers/index.html).

## Ratio bounds for the A005773 recurrence

Let $(A_n)_{n \ge 0}$ be a sequence of real numbers with $A_0 = A_1 = 1$ and
$(n+1) A_{n+1} = 2(n+1) A_n + 3(n-1) A_{n-1}$ for every $n \ge 1$. Write
$x_n = A_{n+1}/A_n$ and $\varphi_n = 3(2n+1)/(2(n+1))$. Then for every $n \ge 0$ we have
$x_n \le \varphi_n$ and

$$\frac{x_{n+1}}{x_n} \ge \frac{2(3n^2+6n+2)}{(n+2)(2n+1)\,\varphi_n}.$$

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to a Linear Recurrence Sequence*, INTEGERS 25 (2025), Article A100, Lemma 1.

Stated but not proved: `MetaMathlibExt.a005773Recurrence_ratio_bounds` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/log-behavior-of-motzkin-prefix-numbers/index.html#a005773-recurrence-ratio-bounds).

## The first and second differences of A005773 are log-balanced

Let $(A_n)_{n \ge 0}$ be a sequence of real numbers with $A_0 = A_1 = 1$ and
$(n+1) A_{n+1} = 2(n+1) A_n + 3(n-1) A_{n-1}$ for every $n \ge 1$, and write
$\Delta A_n = A_{n+1} - A_n$ and $\Delta^2 A_n = A_{n+2} - 2A_{n+1} + A_n$. Then for every
$n \ge 4$, each of the sequences $z = \Delta A$ and $z = \Delta^2 A$ satisfies
$z_n^2 \le z_{n-1} z_{n+1}$ and

$$\frac{z_{n-1}}{(n-1)!} \cdot \frac{z_{n+1}}{(n+1)!} \le \left(\frac{z_n}{n!}\right)^2.$$

That is, $(\Delta A_n)_{n \ge 3}$ and $(\Delta^2 A_n)_{n \ge 3}$ are log-balanced: log-convex, with
$(z_n / n!)_{n \ge 3}$ log-concave.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to a Linear Recurrence Sequence*, INTEGERS 25 (2025), Article A100, Theorem 1.

Stated but not proved: `MetaMathlibExt.a005773Recurrence_diff_logBalanced` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/log-behavior-of-motzkin-prefix-numbers/index.html#a005773-recurrence-diff-log-balanced).

## The third differences of A005773 are log-convex and log-balanced

Let $(A_n)_{n \ge 0}$ be a sequence of real numbers with $A_0 = A_1 = 1$ and
$(n+1) A_{n+1} = 2(n+1) A_n + 3(n-1) A_{n-1}$ for every $n \ge 1$, and write
$z_n = \Delta^3 A_n = A_{n+3} - 3A_{n+2} + 3A_{n+1} - A_n$. Then $z_n^2 \le z_{n-1} z_{n+1}$
for every $n \ge 3$, and

$$\frac{z_{n-1}}{(n-1)!} \cdot \frac{z_{n+1}}{(n+1)!} \le \left(\frac{z_n}{n!}\right)^2$$

for every $n \ge 4$. That is, $(\Delta^3 A_n)_{n \ge 2}$ is log-convex and
$(z_n / n!)_{n \ge 3}$ is log-concave, so $(\Delta^3 A_n)_{n \ge 3}$ is log-balanced.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to a Linear Recurrence Sequence*, INTEGERS 25 (2025), Article A100, Theorem 2.

Stated but not proved: `MetaMathlibExt.a005773Recurrence_thirdDiff_logConvex_logBalanced` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/log-behavior-of-motzkin-prefix-numbers/index.html#a005773-recurrence-third-diff-log-convex).

## Log-concave weighted sequences built from A005773

Let $(A_n)_{n \ge 0}$ be a sequence of real numbers with $A_0 = A_1 = 1$ and
$(n+1) A_{n+1} = 2(n+1) A_n + 3(n-1) A_{n-1}$ for every $n \ge 1$, and write
$\Delta A_n = A_{n+1} - A_n$ and $\Delta^2 A_n = A_{n+2} - 2A_{n+1} + A_n$. Then for every
$n \ge 2$, each of the four sequences $z_m = m A_m$, $z_m = (m+1) A_{m+1} - m A_m$,
$z_m = m\,\Delta A_m$ and $z_m = m\,\Delta^2 A_m$ satisfies $z_{n-1} z_{n+1} \le z_n^2$. That
is, these four sequences, indexed from $m = 1$, are log-concave.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to a Linear Recurrence Sequence*, INTEGERS 25 (2025), Article A100, Theorem 3.

Stated but not proved: `MetaMathlibExt.a005773Recurrence_weighted_logConcave` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/log-behavior-of-motzkin-prefix-numbers/index.html#a005773-recurrence-weighted-log-concave).

## Log-convexity of $(n A_n)^n$ for A005773

Let $(A_n)_{n \ge 0}$ be a sequence of real numbers with $A_0 = A_1 = 1$ and
$(n+1) A_{n+1} = 2(n+1) A_n + 3(n-1) A_{n-1}$ for every $n \ge 1$, and let
$z_m = (m A_m)^m$. Then $z_n^2 \le z_{n-1} z_{n+1}$ for every $n \ge 2$; that is, the sequence
$(n^n A_n^n)_{n \ge 1}$ is log-convex.

## Sources

- Feng-Zhen Zhao, *The Log-Behavior of Some Sequences Related to a Linear Recurrence Sequence*, INTEGERS 25 (2025), Article A100, Theorem 4.

Stated but not proved: `MetaMathlibExt.a005773Recurrence_pow_logConvex` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/LinearRecurrenceLogBehaviorWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/log-behavior-of-motzkin-prefix-numbers/index.html#a005773-recurrence-pow-log-convex).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Log-behavior of Motzkin prefix numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/log-behavior-of-motzkin-prefix-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/log-behavior-of-motzkin-prefix-numbers)

---
declaration: section
origin: cited
lean: MetaMathlibExt.bell_turan_identity, MetaMathlibExt.engel_bell_log_convexity
statement: formalized
proof: formalized
---

# Log-convexity of Bell numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/log-convexity-of-bell-numbers/index.html).

## Turán-type identity for the Bell numbers

For every natural number $n \ge 2$, the Bell
numbers $B_m$ satisfy

$$B_{n-1} B_{n+1} - B_n^2 = \frac{1}{2e^2} \sum_{k=2}^{\infty} \sum_{j=1}^{k-1}
\frac{j^{n-1} (k-j)^{n-1}}{j! \, (k-j)!} \, (k-2j)^2,$$

where $e = \exp(1)$.

Every summand is nonnegative and the summand with $k = 3$, $j = 1$ is positive, so the identity
refines Engel's inequality $B_n^2 \le B_{n-1} B_{n+1}$ to a strict inequality.

## Sources

- Horst Alzer, "On Engel's Inequality for Bell Numbers," Journal of Integer Sequences 22 (2019), Article 19.7.1, Theorem with Equation (E3), lines 114–120, <https://cs.uwaterloo.ca/journals/JIS/VOL22/Alzer/alzer6.tex>.

Formalized by `MetaMathlibExt.bell_turan_identity`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/BellTuranIdentity.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/BellTuranIdentity.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/log-convexity-of-bell-numbers/index.html#bell-turan-identity).

## Engel's inequality for Bell numbers

For every integer $n \ge 1$, the Bell numbers
satisfy $B_n^2 \le B_{n-1} B_{n+1}$, where $B_n$ is the number of partitions of an $n$-element
set.

This non-strict inequality is Eq. (E2) of Horst Alzer, "On Engel's Inequality for Bell
Numbers," Journal of Integer Sequences 22 (2019); Alzer's strict refinement is a different
result.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL22/Alzer/alzer6.tex>, lines 79--104, where `B_n` is defined as the Bell number and Eq. (E2) states `B_n^2 ≤ B_{n-1} B_{n+1}` for every integer `n ≥ 1`. The source attributes this inequality to K. Engel, "On the average rank of an element in a filter of the partition lattice," J. Combin. Theory Ser. A 65 (1994), 67--78.

Formalized by `MetaMathlibExt.engel_bell_log_convexity`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/EngelBellLogConvexity.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Enumerative/EngelBellLogConvexity.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/log-convexity-of-bell-numbers/index.html#engel-bell-log-convexity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Log-convexity of Bell numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/log-convexity-of-bell-numbers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/stirling-bell-eulerian/bell-fubini-numbers/log-convexity-of-bell-numbers)

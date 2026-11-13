---
declaration: section
origin: cited
lean: MetaMathlibExt.aigner_motzkin_ratio_inequality, MetaMathlibExt.motzkinNumber_ratio_inequality
statement: formalized
proof: formalized
---

# Aigner's ratio inequality for Motzkin numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/aigner-s-ratio-inequality-for-motzkin-numbers/index.html).

## Aigner's ratio inequality for Motzkin numbers, explicit sum form

For $r \ge 0$ let
$M_r = \sum_{k=0}^{\lfloor r/2 \rfloor} \frac{1}{k+1}\binom{2k}{k}\binom{r}{2k}$, where each
factor $\frac{1}{k+1}\binom{2k}{k}$ is the $k$-th Catalan number, an integer. Then for every
$n \ge 1$, in the rational numbers,

$$
\frac{M_n - M_{n-1}}{M_{n+1} - M_n} \le \frac{M_n}{M_{n+1}}.
$$

## Sources

- Takashi Agoh and Horst Alzer, "Mean Value Inequalities for Motzkin Numbers", Journal of Integer Sequences 24 (2021), Article 21.6.8: Motzkin-number definition, lines 89--107; Aigner ratio inequality, lines 373--386, equation (11). The same inequality for the canonical `MetaMathlibExt.motzkinNumber` is `motzkinNumber_ratio_inequality`.
- <https://cs.uwaterloo.ca/journals/JIS/VOL24/Alzer/alzer8.tex>.

Formalized by `MetaMathlibExt.aigner_motzkin_ratio_inequality`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/AignerMotzkinInequality.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/AignerMotzkinInequality.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/aigner-s-ratio-inequality-for-motzkin-numbers/index.html#aigner-motzkin-ratio-inequality).

## Aigner's ratio inequality for Motzkin numbers

Let $M_n$ denote the $n$-th Motzkin
number. For every $n \ge 1$,

$$
\frac{M_n - M_{n-1}}{M_{n+1} - M_n} \le \frac{M_n}{M_{n+1}}.
$$

## Sources

- Takashi Agoh and Horst Alzer, *Mean Value Inequalities for Motzkin Numbers*, Journal of Integer Sequences 24 (2021), Article 21.6.8, equation (11).

Formalized by `MetaMathlibExt.motzkinNumber_ratio_inequality`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/AignerMotzkinInequality.lean, line 720](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/AignerMotzkinInequality.lean#L720). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/aigner-s-ratio-inequality-for-motzkin-numbers/index.html#motzkin-number-ratio-inequality).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Aigner's ratio inequality for Motzkin numbers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/aigner-s-ratio-inequality-for-motzkin-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/motzkin-numbers/aigner-s-ratio-inequality-for-motzkin-numbers)

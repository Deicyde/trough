---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.JerrumSinclairVigoda.permOf, MetaMathlibExt.Complexity.KeyTheorems.JerrumSinclairVigoda.jerrum_sinclair_vigoda_permanent, MetaMathlibExt.Complexity.KeyTheorems.PermanentSharpPComplete.permFun, MetaMathlibExt.Complexity.KeyTheorems.PermanentSharpPComplete.permanent_sharpP_complete
statement: formalized
---

# Complexity of the permanent

4 results, 2 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/complexity-of-the-permanent/index.html).

## Permanent of an encoded 0-1 matrix

For a bitstring $x$: if $x$ decodes, under the
canonical bitstring encoding, to a pair $(n, e)$ of a natural number $n$ and a list
$e = (e_0, \dots, e_{n^2 - 1})$ of $n^2$ natural numbers each at most $1$, the value at $x$ is the
permanent $\sum_{\sigma} \prod_{i=0}^{n-1} e_{in + \sigma(i)}$ of the $n \times n$ matrix with
row-major entries $e$, where $\sigma$ ranges over the permutations of $\{0, \dots, n - 1\}$;
otherwise the value is $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.JerrumSinclairVigoda.permOf`, a definition declared in [WantedExt/Complexity/KeyTheorems/JerrumSinclairVigodaWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/JerrumSinclairVigodaWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/complexity-of-the-permanent/index.html#perm-of).

## Jerrum-Sinclair-Vigoda: FPRAS for the permanent

For a bitstring $x$, let
$\operatorname{perm}(x)$ be the permanent of the 0-1 matrix encoded by $x$: if $x$ decodes, under
the canonical bitstring encoding, to a pair $(k, e)$ of a natural number $k$ and a list $e$ of
$k^2$ natural numbers each at most $1$, then $\operatorname{perm}(x)$ is the permanent of the
$k \times k$ matrix with row-major entries $e$, and otherwise $\operatorname{perm}(x) = 0$. There
are a polynomial $p$ with natural-number coefficients and a polynomial-time computable function
$E$ from triples of bitstrings to natural numbers such that for all bitstrings $x$ and $w$ with
$n = |w| \ge 1$ (the precision, given in unary), at least two thirds of the bitstrings $r$ of
length $p(|x| + n)$ satisfy
$|E(x, r, w) - \operatorname{perm}(x)| \le \operatorname{perm}(x) / n$.

## Sources

- M. Jerrum, A. Sinclair, and E. Vigoda, "A polynomial-time approximation algorithm for the permanent of a matrix with nonnegative entries", Journal of the ACM 51 (2004), 671-697 (STOC 2001); M. Jerrum and A. Sinclair, "Approximating the permanent", SIAM Journal on Computing 18 (1989), 1149-1178 (precursor with restricted guarantees).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.JerrumSinclairVigoda.jerrum_sinclair_vigoda_permanent` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/JerrumSinclairVigodaWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/JerrumSinclairVigodaWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/complexity-of-the-permanent/index.html#jerrum-sinclair-vigoda-permanent).

## Permanent of an encoded 0-1 matrix

For a bitstring $x$ that decodes to a pair $(n, e)$ of
a natural number $n$ and a list $e = (e_0, \dots, e_{m-1})$ of natural numbers with $m = n^2$
and every $e_j \le 1$, the value at $x$ is the permanent
$\sum_{\sigma} \prod_{i < n} e_{in + \sigma(i)}$ of the $n \times n$ matrix with entries $e$ in
row-major order, the sum running over all permutations $\sigma$ of $\{0, \dots, n - 1\}$. For
every other bitstring the value is $0$.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.PermanentSharpPComplete.permFun`, a definition declared in [WantedExt/Complexity/KeyTheorems/PermanentSharpPCompleteWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/PermanentSharpPCompleteWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/complexity-of-the-permanent/index.html#perm-fun).

## The permanent is #P-complete (Valiant)

The function that sends a bitstring encoding a
square 0-1 matrix to its permanent, and every other bitstring to $0$, is $\#P$-complete.

## Sources

- L. G. Valiant, "The complexity of computing the permanent", Theoretical Computer Science 8 (1979), 189-201.

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.PermanentSharpPComplete.permanent_sharpP_complete` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/PermanentSharpPCompleteWanted.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/PermanentSharpPCompleteWanted.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/complexity-of-the-permanent/index.html#permanent-sharp-p-complete).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Complexity of the permanent](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/complexity-of-the-permanent/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/counting-complexity/complexity-of-the-permanent)

---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.MonotoneColumnPermanentAMR156Problem0025Wanted.permanentAddXJ, MathlibExt.Combinatorics.MonotoneColumnPermanentAMR156Problem0025Wanted.monotoneColumnPermanentConjecture, MathlibExt.Combinatorics.MonotoneColumnPermanentAMR156Problem0025Wanted.monotoneColumnPermanentConjecture_holds
statement: formalized
---

# Monotone column permanent conjecture

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/monotone-column-permanent-conjecture/index.html).

## The polynomial $\operatorname{per}(A + xJ)$

For a real $n \times n$ matrix $A$, this is
the polynomial $\operatorname{per}(A + xJ) \in \mathbb{R}[x]$, where $J$ is the $n \times n$
all-ones matrix: the permanent of the $n \times n$ matrix of polynomials whose $(i, j)$ entry is
$A_{ij} + x$.

Formalized by `MathlibExt.Combinatorics.MonotoneColumnPermanentAMR156Problem0025Wanted.permanentAddXJ`, a definition declared in [WantedExt/Combinatorics/MonotoneColumnPermanentAMR156Problem0025Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MonotoneColumnPermanentAMR156Problem0025Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/monotone-column-permanent-conjecture/index.html#permanent-add-xj).

## The Haglund–Ono–Wagner monotone column permanent conjecture

This is the statement that
for every $n \in \mathbb{N}$ and every real $n \times n$ matrix $A$ whose columns are weakly
increasing ($A_{ij} \le A_{i'j}$ whenever $i \le i'$), every complex root of the polynomial
$\operatorname{per}(A + xJ) \in \mathbb{R}[x]$ is real, where $J$ is the $n \times n$ all-ones
matrix.

Formalized by `MathlibExt.Combinatorics.MonotoneColumnPermanentAMR156Problem0025Wanted.monotoneColumnPermanentConjecture`, a definition declared in [WantedExt/Combinatorics/MonotoneColumnPermanentAMR156Problem0025Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MonotoneColumnPermanentAMR156Problem0025Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/monotone-column-permanent-conjecture/index.html#monotone-column-permanent-conjecture).

## Brändén–Haglund–Visontai–Wagner theorem (monotone column permanent conjecture)

For every
$n \in \mathbb{N}$ and every real $n \times n$ matrix $A$ whose columns are weakly increasing
($A_{ij} \le A_{i'j}$ whenever $i \le i'$), every complex root of the polynomial
$\operatorname{per}(A + xJ) \in \mathbb{R}[x]$ is real, where $J$ is the $n \times n$ all-ones
matrix.

Brändén, Haglund, Visontai and Wagner prove the stronger statement that the multivariate
polynomial $\operatorname{per}(z_j + A_{ij})$, in one variable $z_j$ for each column $j$, is real
stable.

## Sources

- R. P. Stanley, Positivity Problems and Conjectures in Algebraic Combinatorics (1999), Problem 24 (Haglund–Ono–Wagner monotone column permanent conjecture); resolution: P. Brändén, J. Haglund, M. Visontai and D. G. Wagner, Proof of the monotone column permanent conjecture, in Notions of Positivity and the Geometry of Polynomials, Trends Math., Birkhäuser (2011), 63-78, arXiv:1010.2565, Section 1 and abstract: for every n × n monotone column matrix A, per(zJₙ + A) is a polynomial in z with only real roots (the MCPC, Conjecture 2 of Haglund-Ono-Wagner), proved in full generality via the multivariate (real stable) version, https://arxiv.org/abs/1010.2565.

Stated but not proved: `MathlibExt.Combinatorics.MonotoneColumnPermanentAMR156Problem0025Wanted.monotoneColumnPermanentConjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/MonotoneColumnPermanentAMR156Problem0025Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/MonotoneColumnPermanentAMR156Problem0025Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/monotone-column-permanent-conjecture/index.html#monotone-column-permanent-conjecture-hol).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Monotone column permanent conjecture](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/monotone-column-permanent-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/symmetric-functions-q-analogues/monotone-column-permanent-conjecture)

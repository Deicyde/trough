---
declaration: section
origin: cited
lean: MetaMathlibExt.gamma_closed_form, MetaMathlibExt.palindromicNarayanaNumber, MetaMathlibExt.touchard_catalan_identity, MetaMathlibExt.von_szily_super_catalan_identity
statement: formalized
proof: formalized
---

# Catalan numbers and their generalizations: its own results

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/index.html).

Catalan numbers and generalizations defined by formulas or recurrences: Fuss–Catalan, super Catalan, (p,q)-Patalan, Whitt and Sabar arrays, generalized Catalan–Schröder, Fine and Riordan numbers, Narayana numbers and polynomials, Touchard's identity, Raney's cycle lemma, and divisibility or growth of these numbers.

## Closed form of the Eloe–Kublik gamma array

Let $\gamma_{n,k}$, for natural numbers $n$ and
$k$, be real numbers such that $\gamma_{n,0} = 1$ for every $n$, $\gamma_{2n-1,n} = 0$ for every
$n \ge 1$, and

$$\gamma_{n,k} = (1 + \frac{2k}{n+2})\,\gamma_{n-1,k} + \frac{2k-n-1}{n+2}\,\gamma_{n-1,k-1}$$

whenever $n \ge 2$ and $1 \le k \le \lfloor n/2 \rfloor$. Then
$\gamma_{n,k} = (-\frac{1}{4})^k \binom{n}{2k} C_k$ for all natural numbers $n$ and $k$ with
$k \le \lfloor n/2 \rfloor$, where $C_k$ is the $k$-th Catalan number.

## Sources

- Paul Eloe and Catherine Kublik, "When Numerical Analysis Crosses Paths with Catalan and Generalized Motzkin Numbers," Journal of Integer Sequences 21 (2018), Article 18.8.4, Theorem `closedform_thm`, lines 390-396, <https://cs.uwaterloo.ca/journals/JIS/VOL21/Kublik/kublik2.tex>; the recursion and initial conditions are equation `gamma_linear_recursion`, lines 87-91.

Formalized by `MetaMathlibExt.gamma_closed_form`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/GammaClosedForm.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/GammaClosedForm.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/index.html#gamma-closed-form).

## Palindromic Narayana numbers

For natural numbers $n$ and $k$, the palindromic Narayana
number is the rational number $\tilde{N}(n, k) = \binom{n}{k} \binom{n+1}{k} / (k+1)$.

The value is taken in $\mathbb{Q}$ so that the displayed quotient is represented literally.

## Sources

- Paul Barry, "Generalized Catalan Numbers Associated with a Family of Pascal-like Triangles," <https://cs.uwaterloo.ca/journals/JIS/VOL22/Barry3/barry422.tex>.

Formalized by `MetaMathlibExt.palindromicNarayanaNumber`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PalindromicNarayanaNumber.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PalindromicNarayanaNumber.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/index.html#palindromic-narayana-number).

## Touchard's Catalan identity

For every natural number $n$, writing
$C_k = \binom{2k}{k}/(k+1)$ for the $k$-th Catalan number,

$$C_{n+1} = \sum_{i=0}^{\lfloor n/2 \rfloor} \binom{n}{2i} 2^{n-2i} C_i.$$

## Sources

- https://cs.uwaterloo.ca/journals/JIS/VOL20/Dershowitz/dersh3.tex, lines 274-277. A second JIS source prints the finite upper bound as `floor(n/2)`.

Formalized by `MetaMathlibExt.touchard_catalan_identity`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/TouchardCatalanIdentity.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/TouchardCatalanIdentity.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/index.html#touchard-catalan-identity).

## Von Szily's identity for super Catalan numbers

For all natural numbers $m$ and $n$,

$$
\left\lfloor \frac{(2m)!\,(2n)!}{m!\,n!\,(m+n)!} \right\rfloor
= \sum_{k=\max(-m,-n)}^{\min(m,n)} (-1)^k \binom{2m}{m+k} \binom{2n}{n+k},
$$

where the sum runs over the integers $k$ with $\max(-m, -n) \le k \le \min(m, n)$.

The quotient inside the floor is the super Catalan number $S(m, n)$. The source sums over all
$k \in \mathbb{Z}$; only the terms in this range are nonzero.

## Sources

- Kendra Killpatrick, *Super FiboCatalan Numbers and Their Lucas Analogues*, Journal of Integer Sequences 28 (2025), Article 25.5.8, von Szily identity quoted in the Open problems section, lines 671–674, <https://cs.uwaterloo.ca/journals/JIS/VOL28/Killpatrick/killp6.tex>, citing I. Gessel, *Super ballot numbers*, J. Symbolic Comput. 14 (1992), p. 11.

Formalized by `MetaMathlibExt.von_szily_super_catalan_identity`, a theorem declared in [MathlibExt/Combinatorics/VonSzilySuperCatalan.lean, line 901](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/VonSzilySuperCatalan.lean#L901). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/index.html#von-szily-super-catalan-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Catalan numbers and their generalizations](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/catalan-numbers-lattice-paths/catalan-numbers)

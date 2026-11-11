---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.QTSPPWanted.QTSPP.q_tspp, MetaMathlibExt.zeilberger_gamma_coefficient
statement: formalized
---

# Symmetric functions, tableaux and q-analogues: its own results

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/index.html).

Algebraic combinatorics of symmetric functions and Young tableaux, Gaussian binomial coefficients and other q-analogues, alternating sign matrices and plane partitions (q-TSPP, Robbins numbers), Coxeter–Catalan positivity, chromatic symmetric functions, minuscule polynomials, and positivity or real-rootedness of permanents and gamma vectors.

## The $q$-TSPP theorem

Fix $n$ and let $B_n = \{0, \dots, n - 1\}^3$. A totally symmetric
plane partition in $B_n$ is a subset $\pi \subseteq B_n$ that is a lower set of $\mathbb{N}^3$ for
the componentwise order and is invariant under every permutation of the three coordinates; the
empty set is one. Let $T_n$ be the set of triples $(i, j, k) \in B_n$ with $i \le j \le k$, and
let $o(\pi)$ be the number of elements of $\pi$ in $T_n$ (the number of orbits of $\pi$ under the
permutations of the coordinates). Then, in $\mathbb{Z}[q]$,

$$
\Big(\sum_{\pi} q^{o(\pi)}\Big) \prod_{(i,j,k) \in T_n} \big(1 - q^{i+j+k+1}\big) =
\prod_{(i,j,k) \in T_n} \big(1 - q^{i+j+k+2}\big),
$$

where the sum runs over all totally symmetric plane partitions $\pi$ in $B_n$.

Coordinates start at $0$ and the denominator is cleared: with coordinates $1, \dots, n$ this is
the formula $\sum_{\pi} q^{o(\pi)} = \prod_{1 \le i \le j \le k \le n}
(1 - q^{i+j+k-1}) / (1 - q^{i+j+k-2})$ of Koutschan, Kauers and Zeilberger.

## Sources

- Koutschan, Kauers, and Zeilberger (2011), Theorem 1. DOI: 10.1073/pnas.1019186108. Problem `q_tspp` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Combinatorics.QTSPPWanted.QTSPP.q_tspp` is written with `theorem_wanted` in [WantedExt/Combinatorics/QTSPPWanted.lean, line 127](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/QTSPPWanted.lean#L127). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/index.html#q-tspp).

## Zeilberger's lemma for gamma vectors

Let $n$ be a natural number, let
$\gamma_0, \gamma_1, \gamma_2, \dots$ be rational numbers, and let $h \in \mathbb{Q}[x]$ be the
polynomial $h(x) = \sum_{j=0}^{\lfloor n/2 \rfloor} \gamma_j \, x^j (1 + x)^{n - 2j}$. Let
$c(x) = \sum_{m \ge 0} C_m x^m \in \mathbb{Q}[[x]]$ be the generating function of the Catalan
numbers $C_m$. Then for every natural number $k \le \lfloor n/2 \rfloor$, the number $\gamma_k$
is the coefficient of $x^k$ in the power series $h(x \, c(x)^2) \cdot c(x)^{-n}$.

## Sources

- Paul Barry, "The γ-Vectors of Pascal-like Triangles Defined by Riordan Arrays", Journal of Integer Sequences 22 (2019), Article 19.1.4, Zeilberger's Lemma proposition lines 281–283, <https://cs.uwaterloo.ca/journals/JIS/VOL22/Barry2/barry402.tex>. The gamma-matrix setup and `h` notation use supporting lines 110–120; the Catalan generating function `c(x) = (1 - sqrt (1 - 4 * x)) / (2 * x)` has coefficients `C_n = (1 / (n + 1)) * choose (2 * n) n` (A000108). The malformed recalled display at source line 275 printing `gamma_n` on both sides is excluded; the correctly printed proposition with `h_n` on the left is formalized.

Formalized by `MetaMathlibExt.zeilberger_gamma_coefficient`, a theorem declared in [MathlibExt/Combinatorics/Polynomial/ZeilbergerGamma.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Combinatorics/Polynomial/ZeilbergerGamma.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/index.html#zeilberger-gamma-coefficient).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Symmetric functions, tableaux and q-analogues](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/symmetric-functions-q-analogues/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/symmetric-functions-q-analogues)
